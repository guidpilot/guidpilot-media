import "jsr:@supabase/functions-js/edge-runtime.d.ts";

// Génère une voix off ElevenLabs et la dépose dans le dépôt public guidpilot/guidpilot-media.
// Décision de Normane (10/10/2026) : ElevenLabs UNIQUEMENT. Plus aucun secours Google automatique :
// si ElevenLabs échoue, la fonction renvoie une erreur (Gemini seulement si provider "gemini" est demandé explicitement).
// Outil interne marketing : aucun accès aux données de la base GuidPilot.
// Protégé par le secret interne (même mécanisme que send-notification-email), appelé uniquement depuis la base via pg_net.
//
// Corps JSON :
//   { path: "voix/xxx.mp3", text: "...", provider?: "elevenlabs", voice: "<voice_id>", model?: "...", settings?: {...} }
//   { action: "voices" }                                  -> voix présentes dans le compte ElevenLabs
//   { action: "subscription" }                            -> quota ElevenLabs utilisé / restant
//   { action: "shared_voices", language?: "fr", search?: "", gender?: "", page_size?: 20 } -> bibliothèque publique ElevenLabs
//   { action: "add_voice", public_owner_id: "...", voice_id: "...", name: "..." } -> ajoute une voix de la bibliothèque au compte

const REPO = "guidpilot/guidpilot-media";
const DEFAULT_STYLE = "Native French speaker from France, natural Parisian accent. Calm, warm and reassuring, like a friend explaining something useful. Relaxed conversational pace with short pauses between sentences. Not salesy.";
const EL = "https://api.elevenlabs.io";
const DEFAULT_VOICE = "6vTyAgAT8PncODBcLjRf"; // Claire

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json" } });
}

function b64ToBytes(b64: string): Uint8Array {
  const bin = atob(b64);
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}

function bytesToB64(bytes: Uint8Array): string {
  let s = "";
  const chunk = 0x8000;
  for (let i = 0; i < bytes.length; i += chunk) s += String.fromCharCode(...bytes.subarray(i, i + chunk));
  return btoa(s);
}

function pcmToWav(pcm: Uint8Array, rate = 24000, channels = 1, bits = 16): Uint8Array {
  const header = new ArrayBuffer(44);
  const v = new DataView(header);
  const w = (o: number, s: string) => { for (let i = 0; i < s.length; i++) v.setUint8(o + i, s.charCodeAt(i)); };
  w(0, "RIFF"); v.setUint32(4, 36 + pcm.length, true); w(8, "WAVE"); w(12, "fmt ");
  v.setUint32(16, 16, true); v.setUint16(20, 1, true); v.setUint16(22, channels, true);
  v.setUint32(24, rate, true); v.setUint32(28, rate * channels * bits / 8, true);
  v.setUint16(32, channels * bits / 8, true); v.setUint16(34, bits, true); w(36, "data"); v.setUint32(40, pcm.length, true);
  const out = new Uint8Array(44 + pcm.length);
  out.set(new Uint8Array(header), 0); out.set(pcm, 44);
  return out;
}

async function gemini(apiKey: string, model: string, voice: string, style: string, text: string) {
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${encodeURIComponent(apiKey)}`;
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      contents: [{ parts: [{ text: `${style}\n\nRead the following French text exactly as written:\n${text}` }] }],
      generationConfig: { responseModalities: ["AUDIO"], speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: voice } } } },
    }),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) return { ok: false as const, error: `${model}/${voice}: ${res.status} ${JSON.stringify(data?.error?.message ?? data).slice(0, 300)}` };
  const part = data?.candidates?.[0]?.content?.parts?.find((p: any) => p?.inlineData?.data);
  if (!part) return { ok: false as const, error: `${model}/${voice}: réponse sans audio` };
  const mime: string = part.inlineData.mimeType ?? "";
  const rate = Number(/rate=(\d+)/.exec(mime)?.[1] ?? 24000);
  const pcm = b64ToBytes(part.inlineData.data);
  return { ok: true as const, bytes: pcmToWav(pcm, rate), ext: "wav", seconds: Math.round(pcm.length / (rate * 2) * 10) / 10, provider: "gemini", model, voice };
}

async function eleven(key: string, voiceId: string, model: string, text: string, settings: any) {
  const res = await fetch(`${EL}/v1/text-to-speech/${encodeURIComponent(voiceId)}?output_format=mp3_44100_128`, {
    method: "POST",
    headers: { "xi-api-key": key, "Content-Type": "application/json", Accept: "audio/mpeg" },
    body: JSON.stringify({
      text,
      model_id: model,
      language_code: "fr",
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0.15, use_speaker_boost: true, speed: 1.0, ...(settings ?? {}) },
    }),
  });
  if (!res.ok) return { ok: false as const, error: `elevenlabs ${model}/${voiceId}: ${res.status} ${(await res.text()).slice(0, 300)}` };
  const bytes = new Uint8Array(await res.arrayBuffer());
  return { ok: true as const, bytes, ext: "mp3", seconds: Math.round(bytes.length / 16000 * 10) / 10, provider: "elevenlabs", model, voice: voiceId };
}

async function elGet(key: string, url: string) {
  const res = await fetch(url, { headers: { "xi-api-key": key } });
  const data = await res.json().catch(() => ({}));
  return { status: res.status, data };
}

Deno.serve(async (req: Request) => {
  if (req.method !== "POST") return json({ error: "method_not_allowed" }, 405);
  const secret = Deno.env.get("INTERNAL_EMAIL_SECRET");
  if (!secret || req.headers.get("x-internal-secret") !== secret) return json({ error: "unauthorized" }, 401);

  const geminiKey = Deno.env.get("GEMINI_API_KEY");
  const elKey = Deno.env.get("ELEVENLABS_API_KEY");
  const ghToken = Deno.env.get("GITHUB_MEDIA_TOKEN");
  const body = await req.json().catch(() => null);

  // --- Actions de consultation ElevenLabs (aucune écriture GitHub) ---
  if (body?.action) {
    if (!elKey) return json({ error: "missing_secrets", elevenlabs: false }, 500);
    if (body.action === "voices") {
      const r = await elGet(elKey, `${EL}/v1/voices`);
      const voices = (r.data?.voices ?? []).map((v: any) => ({ voice_id: v.voice_id, name: v.name, category: v.category, labels: v.labels, preview_url: v.preview_url }));
      return json({ status: r.status, voices, error: r.status >= 400 ? r.data : undefined });
    }
    if (body.action === "subscription") {
      const r = await elGet(elKey, `${EL}/v1/user/subscription`);
      const d = r.data ?? {};
      return json({ status: r.status, tier: d.tier, character_count: d.character_count, character_limit: d.character_limit, next_reset_unix: d.next_character_count_reset_unix, error: r.status >= 400 ? d : undefined });
    }
    if (body.action === "shared_voices") {
      const q = new URLSearchParams({ page_size: String(body.page_size ?? 20), language: body.language ?? "fr" });
      if (body.search) q.set("search", body.search);
      if (body.gender) q.set("gender", body.gender);
      if (body.use_cases) q.set("use_cases", body.use_cases);
      if (body.sort) q.set("sort", body.sort);
      const r = await elGet(elKey, `${EL}/v1/shared-voices?${q}`);
      const voices = (r.data?.voices ?? []).map((v: any) => ({ public_owner_id: v.public_owner_id, voice_id: v.voice_id, name: v.name, gender: v.gender, age: v.age, accent: v.accent, language: v.language, locale: v.locale, use_case: v.use_case, descriptive: v.descriptive, cloned_by_count: v.cloned_by_count, usage_character_count_1y: v.usage_character_count_1y, preview_url: v.preview_url, description: (v.description ?? "").slice(0, 200) }));
      return json({ status: r.status, voices, error: r.status >= 400 ? r.data : undefined });
    }
    if (body.action === "add_voice") {
      if (!body.public_owner_id || !body.voice_id || !body.name) return json({ error: "invalid_request" }, 400);
      const res = await fetch(`${EL}/v1/voices/add/${encodeURIComponent(body.public_owner_id)}/${encodeURIComponent(body.voice_id)}`, {
        method: "POST", headers: { "xi-api-key": elKey, "Content-Type": "application/json" }, body: JSON.stringify({ new_name: String(body.name).slice(0, 60) }),
      });
      return json({ status: res.status, data: await res.json().catch(() => ({})) });
    }
    return json({ error: "unknown_action" }, 400);
  }

  // --- Génération d'une voix off ---
  if (!ghToken) return json({ error: "missing_secrets", github: false }, 500);
  const text = typeof body?.text === "string" ? body.text.trim() : "";
  let path = typeof body?.path === "string" ? body.path : "";
  if (!text || text.length > 5000 || !/^voix\/[A-Za-z0-9_\-\/]+\.(wav|mp3)$/.test(path)) return json({ error: "invalid_request" }, 400);
  // ElevenLabs par défaut (voix Claire). Gemini uniquement si demandé explicitement avec provider "gemini".
  const provider = body?.provider === "gemini" ? "gemini" : "elevenlabs";
  const errors: string[] = [];
  let result: any = null;

  if (provider === "elevenlabs") {
    if (!elKey) return json({ error: "tts_failed", details: ["elevenlabs: clé absente"] }, 502);
    const r = await eleven(elKey, typeof body?.voice === "string" && body.voice ? body.voice : DEFAULT_VOICE, body?.model ?? "eleven_multilingual_v2", text, body?.settings);
    if (r.ok) result = r; else return json({ error: "tts_failed", details: [r.error] }, 502);
  } else {
    if (!geminiKey) return json({ error: "tts_failed", details: ["gemini: clé absente"] }, 502);
    const style = typeof body?.style === "string" && body.style ? body.style : DEFAULT_STYLE;
    const r = await gemini(geminiKey, body?.model ?? "gemini-3.8-flash-tts", body?.voice ?? "Nika", style, text);
    if (r.ok) result = r; else return json({ error: "tts_failed", details: [r.error] }, 502);
  }

  // L'extension suit le format réellement produit (mp3 pour ElevenLabs).
  path = path.replace(/\.(wav|mp3)$/, `.${result.ext}`);
  const api = `https://api.github.com/repos/${REPO}/contents/${path}`;
  const gh = { Authorization: `Bearer ${ghToken}`, Accept: "application/vnd.github+json", "User-Agent": "guidpilot-voix" };
  let sha: string | undefined;
  const existing = await fetch(api, { headers: gh });
  if (existing.ok) sha = (await existing.json())?.sha;
  const put = await fetch(api, {
    method: "PUT",
    headers: { ...gh, "Content-Type": "application/json" },
    body: JSON.stringify({ message: `Voix off : ${path}`, content: bytesToB64(result.bytes), ...(sha ? { sha } : {}) }),
  });
  if (!put.ok) return json({ error: "github_failed", status: put.status, details: (await put.text()).slice(0, 300) }, 502);

  return json({ ok: true, path, provider: result.provider, model: result.model, voice: result.voice, bytes: result.bytes.length, seconds: result.seconds, fallback_errors: errors });
});
