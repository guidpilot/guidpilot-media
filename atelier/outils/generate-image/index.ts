import "jsr:@supabase/functions-js/edge-runtime.d.ts";

// Génère une image réaliste (Google Gemini / Imagen) et la dépose dans le dépôt public guidpilot/guidpilot-media (dossier images/).
// Outil interne marketing : aucun accès aux données de la base GuidPilot.
// Protégé par le secret interne (même mécanisme que generate-voiceover), appelé uniquement depuis la base via pg_net.
//
// Corps JSON :
//   { path: "images/xxx.png", prompt: "...", aspect?: "16:9"|"9:16"|"1:1"|"4:3"|"3:4", model?: "..." }
//   { action: "models" }  -> modèles Gemini disponibles pour la clé (filtrés sur image / imagen)

const REPO = "guidpilot/guidpilot-media";
const G = "https://generativelanguage.googleapis.com/v1beta";
const STYLE = "Photorealistic editorial photograph, natural soft daylight, realistic skin and textures, shallow depth of field, " +
  "calm premium and reassuring mood, modern French interior, muted colors with navy blue and warm gold accents. " +
  "No text, no letters, no logos, no watermark, no mystical effects, no stars, no crystals, no glowing halos.";

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json" } });
}

async function viaGemini(key: string, model: string, prompt: string, aspect: string) {
  const res = await fetch(`${G}/models/${model}:generateContent?key=${encodeURIComponent(key)}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      contents: [{ parts: [{ text: `${prompt}\n\n${STYLE}` }] }],
      generationConfig: { responseModalities: ["IMAGE"], imageConfig: { aspectRatio: aspect } },
    }),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) return { ok: false as const, error: `${model}: ${res.status} ${JSON.stringify(data?.error?.message ?? data).slice(0, 300)}` };
  const part = data?.candidates?.[0]?.content?.parts?.find((p: any) => p?.inlineData?.data);
  if (!part) return { ok: false as const, error: `${model}: réponse sans image ${JSON.stringify(data?.candidates?.[0]?.finishReason ?? "")}` };
  return { ok: true as const, b64: part.inlineData.data as string, mime: part.inlineData.mimeType as string, model };
}

async function viaImagen(key: string, model: string, prompt: string, aspect: string) {
  const res = await fetch(`${G}/models/${model}:predict?key=${encodeURIComponent(key)}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ instances: [{ prompt: `${prompt}\n\n${STYLE}` }], parameters: { sampleCount: 1, aspectRatio: aspect, personGeneration: "allow_adult" } }),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) return { ok: false as const, error: `${model}: ${res.status} ${JSON.stringify(data?.error?.message ?? data).slice(0, 300)}` };
  const p = data?.predictions?.[0];
  if (!p?.bytesBase64Encoded) return { ok: false as const, error: `${model}: réponse sans image` };
  return { ok: true as const, b64: p.bytesBase64Encoded as string, mime: (p.mimeType as string) ?? "image/png", model };
}

Deno.serve(async (req: Request) => {
  if (req.method !== "POST") return json({ error: "method_not_allowed" }, 405);
  const secret = Deno.env.get("INTERNAL_EMAIL_SECRET");
  if (!secret || req.headers.get("x-internal-secret") !== secret) return json({ error: "unauthorized" }, 401);
  const key = Deno.env.get("GEMINI_API_KEY");
  const ghToken = Deno.env.get("GITHUB_MEDIA_TOKEN");
  if (!key) return json({ error: "missing_secrets", gemini: false }, 500);
  const body = await req.json().catch(() => null);

  if (body?.action === "models") {
    const res = await fetch(`${G}/models?pageSize=200&key=${encodeURIComponent(key)}`);
    const data = await res.json().catch(() => ({}));
    const models = (data?.models ?? []).map((m: any) => ({ name: m.name, methods: m.supportedGenerationMethods }))
      .filter((m: any) => /image|imagen/i.test(m.name));
    return json({ status: res.status, models });
  }

  if (!ghToken) return json({ error: "missing_secrets", github: false }, 500);
  const prompt = typeof body?.prompt === "string" ? body.prompt.trim() : "";
  let path = typeof body?.path === "string" ? body.path : "";
  const aspect = ["16:9", "9:16", "1:1", "4:3", "3:4"].includes(body?.aspect) ? body.aspect : "16:9";
  if (!prompt || prompt.length > 3000 || !/^images\/[A-Za-z0-9_\-\/]+\.(png|jpg|jpeg)$/.test(path)) return json({ error: "invalid_request" }, 400);

  const attempts: string[] = body?.model ? [body.model] : ["gemini-3.1-flash-image", "gemini-2.5-flash-image", "gemini-3-pro-image"];
  const errors: string[] = [];
  let result: any = null;
  for (const m of attempts) {
    const r = m.startsWith("imagen") ? await viaImagen(key, m, prompt, aspect) : await viaGemini(key, m, prompt, aspect);
    if (r.ok) { result = r; break; }
    errors.push(r.error);
  }
  if (!result) return json({ error: "image_failed", details: errors }, 502);

  const ext = /jpe?g/.test(result.mime) ? "jpg" : "png";
  path = path.replace(/\.(png|jpg|jpeg)$/, `.${ext}`);
  const api = `https://api.github.com/repos/${REPO}/contents/${path}`;
  const gh = { Authorization: `Bearer ${ghToken}`, Accept: "application/vnd.github+json", "User-Agent": "guidpilot-images" };
  let sha: string | undefined;
  const existing = await fetch(api, { headers: gh });
  if (existing.ok) sha = (await existing.json())?.sha;
  const put = await fetch(api, {
    method: "PUT",
    headers: { ...gh, "Content-Type": "application/json" },
    body: JSON.stringify({ message: `Image : ${path}`, content: result.b64, ...(sha ? { sha } : {}) }),
  });
  if (!put.ok) return json({ error: "github_failed", status: put.status, details: (await put.text()).slice(0, 300), image_errors: errors }, 502);
  return json({ ok: true, path, model: result.model, bytes: Math.round(result.b64.length * 3 / 4), fallback_errors: errors });
});
