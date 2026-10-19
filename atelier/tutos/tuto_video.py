"""Monteur des tutoriels vidéo GuidPilot (1920x1080, voix Claire, vraies captures du compte de démonstration).

Usage :
  python3 tuto_video.py <spec.py> <voix.mp3> [--snaps DIR] [--out DIR] [--preview N] [--fps 30]

- <spec.py> définit TUTO (voir specs/t02_prestations.py) : une liste de scènes intro / shot / recap / outro.
- Chaque scène « shot » pointe une capture HTML (prise dans le navigateur intégré avec la fonction __s) :
  rendue en haute définition par render.py, avec la position réelle des éléments à mettre en valeur.
- La voix off est UN seul fichier : une pause <break time="1.3s"/> sépare les scènes ; le découpage se fait
  sur les silences les plus longs, dans l'ordre. Chaque scène dure exactement le temps de sa phrase.
- --preview N : n'écrit que N images témoins (contrôle rapide) au lieu de la vidéo.
"""
import importlib.util, json, math, pathlib, re, shutil, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
ATELIER = HERE.parent
TUTO_TOOLS = pathlib.Path("/home/claude/tuto") if pathlib.Path("/home/claude/tuto/render.py").exists() else HERE / "outils"  # outils/ : npm install pour les polices
sys.path.insert(0, str(TUTO_TOOLS))
from render import render  # noqa: E402

FS = TUTO_TOOLS / "node_modules" / "@fontsource" / "inter" / "files"
KIT = ATELIER / "kit" / "assets"
W, H = 1920, 1080
# zone écran (vraie capture) à droite
SX, SW = 620, 1230
SH = round(SW / 1.6)
SY = (H - SH) // 2 + 28
CSS_W, CSS_H = 1440, 900
LEAD = 0.45  # silence ajouté avant la voix


def load_spec(path):
    s = importlib.util.spec_from_file_location("spec", path)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m.TUTO


def sh(cmd):
    return subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)


def split_voice(mp3, n, workdir):
    wav = workdir / "voix.wav"
    sh(f'ffmpeg -y -loglevel error -i "{mp3}" -af "adelay={int(LEAD*1000)}|{int(LEAD*1000)},loudnorm=I=-15:TP=-1.5:LRA=11" -ar 48000 -ac 2 "{wav}"')
    dur = float(sh(f'ffprobe -v error -show_entries format=duration -of csv=p=0 "{wav}"').stdout)
    out = subprocess.run(f'ffmpeg -i "{wav}" -af silencedetect=noise=-38dB:d=0.55 -f null -', shell=True, capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    gaps = [(e - s, s, e) for s, e in zip(starts, ends) if s > LEAD + 0.5 and e < dur - 0.3]
    if len(gaps) < n - 1:
        raise SystemExit(f"Seulement {len(gaps)} silences pour {n} scènes : vérifier la voix.")
    chosen = sorted(sorted(gaps, reverse=True)[: n - 1], key=lambda g: g[1])
    bounds = [0.0] + [round((g[1] + g[2]) / 2, 3) for g in chosen] + [round(dur + 0.9, 3)]
    gap_list = [round(g[0], 2) for g in chosen]
    return wav, bounds, gap_list, dur


def resolve_shots(spec, snaps, workdir):
    cache = {}
    for i, sc in enumerate(spec["scenes"]):
        if sc["type"] != "shot":
            continue
        sels = {k: sc[k] for k in ("focus", "focus2", "click_sel") if sc.get(k)}
        png = workdir / f"{sc['snap']}.png"
        key = (sc["snap"], json.dumps(sels, sort_keys=True))
        if key not in cache:
            meta = render(snaps / f"{sc['snap']}.html", png if (not png.exists() or png.stat().st_mtime < (snaps / f"{sc['snap']}.html").stat().st_mtime) else None, scale=2, rects=sels)
            cache[key] = meta["rects"]
        r = cache[key]
        for k, v in r.items():
            if v is None:
                raise SystemExit(f"Scène {i} : élément introuvable pour {k} = {sels[k]}")
        f = dict(r["focus"])
        if r.get("focus2"):
            g = r["focus2"]
            x0, y0 = min(f["x"], g["x"]), min(f["y"], g["y"])
            x1, y1 = max(f["x"] + f["width"], g["x"] + g["width"]), max(f["y"] + f["height"], g["y"] + g["height"])
            f = {"x": x0, "y": y0, "width": x1 - x0, "height": y1 - y0}
        if sc.get("focus_pad"):  # haut, gauche, hauteur, largeur min
            t, l, hh, ww = sc["focus_pad"]
            f = {"x": f["x"] - l, "y": f["y"] - t, "width": max(f["width"] + 2 * l, ww), "height": max(f["height"] + 2 * t, hh)}
        else:
            f = {"x": f["x"] - 8, "y": f["y"] - 8, "width": f["width"] + 16, "height": f["height"] + 16}
        sc["_rect"] = f
        c = r.get("click_sel") or r["focus"]
        sc["_click"] = [c["x"] + c["width"] * 0.5, c["y"] + c["height"] * 0.55] if (sc.get("click") or sc.get("click_sel")) else None
        sc["_img"] = png.name


def font_css():
    out = []
    for w in (400, 500, 600, 700, 800):
        out.append(f"@font-face{{font-family:Inter;font-weight:{w};src:url('file://{FS}/inter-latin-{w}-normal.woff2')}}")
        out.append(f"@font-face{{font-family:Inter;font-weight:{w};src:url('file://{FS}/inter-latin-ext-{w}-normal.woff2');unicode-range:U+0100-024F,U+1E00-1EFF,U+20AC}}")
    return "\n".join(out)


CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1920px;height:1080px;overflow:hidden;background:#F6F8FC;font-family:Inter,sans-serif;color:#0F172A;-webkit-font-smoothing:antialiased}
.layer{position:absolute;inset:0;opacity:0}
.light{background:#F6F8FC}.dark{background:#0F172A;color:#fff}
.hdr{position:absolute;left:70px;top:44px;height:46px;display:flex;align-items:center;gap:22px}
.hdr img{height:44px}
.hdr .chip{font-weight:600;font-size:22px;color:#475569;padding:8px 18px;border:2px solid #E2E8F0;border-radius:999px;background:#fff}
.aib{position:absolute;right:70px;top:50px;font-size:17px;font-weight:600;color:#64748B;background:#fff;border:2px solid #E2E8F0;border-radius:999px;padding:6px 14px;z-index:50}
.dark .aib{background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.18);color:#CBD5E1}
.left{position:absolute;left:70px;top:0;width:500px;height:1080px}
.badge{position:absolute;left:0;top:300px;width:104px;height:104px;border-radius:50%;background:#0F172A;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:52px;box-shadow:0 14px 34px rgba(15,23,42,.18)}
.badge.info{background:#2563EB;font-size:46px}
.badge.ok{background:#16A34A}
.slabel{position:absolute;left:128px;top:338px;font-weight:700;font-size:24px;letter-spacing:.06em;text-transform:uppercase;color:#2563EB}
.cap{position:absolute;left:0;top:440px;width:500px;font-weight:700;font-size:46px;line-height:1.22;letter-spacing:-.01em;color:#0F172A}
.cap b{color:#2563EB;font-weight:800}
.prog{position:absolute;left:0;top:930px;display:flex;gap:10px}
.prog i{display:block;width:34px;height:8px;border-radius:4px;background:#E2E8F0}
.prog i.on{background:#2563EB}
.frame{position:absolute;left:__SX__px;top:__SY__px;width:__SW__px;height:__SH__px;border-radius:22px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.14);overflow:hidden}
.vp{position:absolute;inset:0;overflow:hidden}
.vp img.shot{position:absolute;left:0;top:0;transform-origin:0 0;max-width:none}
.ring{position:absolute;border:5px solid #E9C46A;border-radius:16px;box-shadow:0 0 0 3000px rgba(15,23,42,.26);pointer-events:none}
.demo{position:absolute;right:16px;top:14px;z-index:5;font-size:16px;font-weight:600;color:#64748B;background:rgba(255,255,255,.94);border:2px solid #E2E8F0;border-radius:999px;padding:4px 12px}
.cursor{position:absolute;width:44px;height:52px;z-index:6;filter:drop-shadow(0 4px 6px rgba(15,23,42,.35))}
.ripple{position:absolute;width:20px;height:20px;margin:-10px 0 0 -10px;border-radius:50%;border:4px solid #2563EB;z-index:5;opacity:0}
/* intro */
.in-logo{position:absolute;left:140px;top:130px;height:66px}
.in-chip{position:absolute;left:140px;top:300px;font-weight:700;font-size:26px;letter-spacing:.08em;text-transform:uppercase;color:#E9C46A}
.in-num{position:absolute;left:140px;top:356px;font-weight:800;font-size:40px;color:#93C5FD}
.in-title{position:absolute;left:140px;top:420px;font-weight:800;font-size:104px;line-height:1.04;letter-spacing:-.03em;width:1300px}
.in-sub{position:absolute;left:144px;top:660px;font-weight:500;font-size:40px;color:#CBD5E1;width:1250px;line-height:1.3}
.in-bar{position:absolute;left:144px;top:610px;height:8px;width:0;border-radius:4px;background:#2563EB}
.in-steps{position:absolute;left:144px;top:820px;display:flex;gap:14px}
.in-steps span{font-size:22px;font-weight:600;color:#94A3B8;padding:8px 16px;border:2px solid #334155;border-radius:999px}
.in-steps span.cur{color:#fff;border-color:#2563EB;background:#2563EB}
/* recap */
.rc-t{position:absolute;left:160px;top:170px;font-weight:800;font-size:76px;letter-spacing:-.02em}
.rc-l{position:absolute;left:160px;top:330px;width:1600px}
.rc-i{display:flex;align-items:center;gap:30px;margin-bottom:34px;font-weight:600;font-size:48px;opacity:0;transform:translateY(16px)}
.rc-i em{flex:none;width:72px;height:72px;border-radius:50%;background:#16A34A;color:#fff;font-style:normal;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center}
/* outro */
.ou-l{position:absolute;left:160px;top:250px;font-weight:700;font-size:30px;letter-spacing:.08em;text-transform:uppercase;color:#E9C46A}
.ou-t{position:absolute;left:160px;top:310px;font-weight:800;font-size:92px;letter-spacing:-.03em;width:1500px;line-height:1.06}
.ou-s{position:absolute;left:162px;top:560px;font-weight:500;font-size:38px;color:#CBD5E1;width:1500px;line-height:1.35}
.ou-s b{color:#fff}
.ou-logo{position:absolute;left:160px;bottom:120px;height:60px}
"""


def chip_label(spec):
    return spec.get("chip") or f'Tuto {spec["num"]} · {spec["title"]}'


def scene_html(i, sc, spec, nsteps):
    aib = '<div class="aib">Voix off générée par IA</div>'
    if sc["type"] == "intro":
        demo = spec.get("mode") == "demo"
        steps = "" if demo else "".join(f'<span class="{"cur" if k == spec["num"] else ""}">{k}</span>' for k in range(*(spec.get("range") or (1, spec.get("total", 5) + 1))))
        return (f'<div class="layer dark" id="L{i}">{aib}<img class="in-logo" src="logo_blanc.png">'
                f'<div class="in-chip">{spec["series"]}</div><div class="in-num">{spec.get("kicker") if demo else "Tutoriel " + str(spec["num"])}</div>'
                f'<div class="in-title" style="font-size:{min(104, int(1300 / (len(spec["title"]) * 0.52)))}px">{spec["title"]}</div><div class="in-bar" id="bar{i}"></div>'
                f'<div class="in-sub">{spec["subtitle"]}</div><div class="in-steps">{steps}</div></div>')
    if sc["type"] == "recap":
        items = "".join(f'<div class="rc-i" id="rc{i}_{k}"><em>✓</em>{t}</div>' for k, t in enumerate(sc["items"]))
        return (f'<div class="layer light" id="L{i}">{aib}<div class="hdr"><img src="logo_couleur.png"><span class="chip">{chip_label(spec)}</span></div>'
                f'<div class="rc-t">En résumé</div><div class="rc-l">{items}</div></div>')
    if sc["type"] == "outro":
        if spec.get("mode") == "demo":
            return (f'<div class="layer dark" id="L{i}">{aib}<div class="ou-l">{spec.get("cta_kicker", "Essayez GuidPilot")}</div><div class="ou-t">{spec.get("cta_title")}</div>'
                    f'<div class="ou-s">{spec.get("cta_sub")}</div>'
                    f'<img class="ou-logo" src="logo_blanc.png"></div>')
        return (f'<div class="layer dark" id="L{i}">{aib}<div class="ou-l">{"Prochain tutoriel" if spec.get("next") else "Félicitations"}</div><div class="ou-t">{spec["next"].split("·",1)[-1].strip() if spec.get("next") else spec.get("end_title", "Votre espace est prêt")}</div>'
                f'<div class="ou-s">Tous les tutoriels sont dans GuidPilot, rubrique <b>Aide &amp; tutoriels</b>.<br>Une question ? Écrivez-nous depuis <b>Support</b>.</div>'
                f'<img class="ou-logo" src="logo_blanc.png"></div>')
    # shot
    st = sc.get("step")
    if st:
        badge = f'<div class="badge">{st}</div><div class="slabel">Étape {st} sur {nsteps}</div>'
    elif sc.get("kind") == "result":
        badge = '<div class="badge ok">✓</div><div class="slabel">Résultat</div>'
    else:
        badge = '<div class="badge info">i</div><div class="slabel">Bon à savoir</div>'
    prog = "".join(f'<i class="{"on" if st and k <= st else ""}"></i>' for k in range(1, nsteps + 1)) if st else ""
    cursor = ('<svg class="cursor" id="cu{i}" viewBox="0 0 44 52"><path d="M4 3 L4 40 L14 31 L21 48 L28 45 L21 29 L35 29 Z" '
              'fill="#0F172A" stroke="#fff" stroke-width="3" stroke-linejoin="round"/></svg><div class="ripple" id="rp{i}"></div>').format(i=i)
    return (f'<div class="layer light" id="L{i}">{aib}<div class="hdr"><img src="logo_couleur.png"><span class="chip">{chip_label(spec)}</span></div>'
            f'<div class="left" id="lf{i}">{badge}<div class="cap">{sc["caption"]}</div><div class="prog">{prog}</div></div>'
            f'<div class="frame"><div class="vp"><img class="shot" id="im{i}" src="{sc["_img"]}"><div class="ring" id="rg{i}"></div>'
            f'{cursor if sc.get("_click") else ""}</div><span class="demo">{sc.get("badge", "Compte de démonstration")}</span></div></div>')


JS = r"""
const S = __SCENES__, K = __K__, VW = __SW__, VH = __SH__;
const ease = x => x<=0?0:x>=1?1:(x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2);
const lerp=(a,b,t)=>a+(b-a)*t;
function cam(sc, z){ // renvoie [z, ox, oy] pour centrer le rectangle
  const r=sc.rect; let cx=r.x+r.width/2, cy=r.y+r.height/2;
  const w=1440*K*z, h=900*K*z; let ox=VW/2-cx*K*z, oy=VH/2-cy*K*z;
  ox=Math.min(0,Math.max(VW-w,ox)); oy=Math.min(0,Math.max(VH-h,oy)); return [z,ox,oy];
}
let prevCursor = null;
function frame(t){
  for (let i=0;i<S.length;i++){
    const sc=S[i], el=document.getElementById('L'+i), lt=t-sc.t0, d=sc.t1-sc.t0;
    let op = 0;
    if (t>=sc.t0-0.45 && t<sc.t1+0.45) op = (i===0) ? 1 : Math.min(1,(t-(sc.t0-0.45))/0.45);
    el.style.opacity = op; el.style.zIndex = i;
    if (el.style.opacity==0) continue;
    const u = Math.max(0, lt);
    if (sc.type==='intro'){ const b=document.getElementById('bar'+i); b.style.width=(220*ease((u-0.5)/1.0))+'px'; }
    if (sc.type==='recap'){ sc.items.forEach((_,k)=>{ const e=document.getElementById('rc'+i+'_'+k); const a=ease((u-0.5-k*0.9)/0.5); e.style.opacity=a; e.style.transform=`translateY(${16*(1-a)}px)`; }); }
    if (sc.type==='shot'){
      const lf=document.getElementById('lf'+i); const a=ease(u/0.6); lf.style.opacity=a; lf.style.transform=`translateX(${-30*(1-a)}px)`;
      const zt = ease((u-0.5)/1.1); const z = lerp(1, sc.zoom, zt);
      const [zz,ox,oy] = cam(sc, z); const [z1,ox1,oy1]=cam(sc,1);
      const X = lerp(ox1,ox,zt), Y=lerp(oy1,oy,zt);
      const im=document.getElementById('im'+i); im.style.width=(1440*K*zz)+'px'; im.style.transform=`translate(${X}px,${Y}px)`;
      const rg=document.getElementById('rg'+i), r=sc.rect;
      rg.style.left=(X+r.x*K*zz)+'px'; rg.style.top=(Y+r.y*K*zz)+'px'; rg.style.width=(r.width*K*zz)+'px'; rg.style.height=(r.height*K*zz)+'px';
      rg.style.opacity = ease((u-1.2)/0.5);
      if (sc.click){
        const cu=document.getElementById('cu'+i), rp=document.getElementById('rp'+i);
        const tx=X+sc.click[0]*K*zz, ty=Y+sc.click[1]*K*zz;
        const sx = VW*0.62, sy = VH*0.92;
        const m = ease((u-1.0)/1.0);
        cu.style.left=(lerp(sx,tx,m)-4)+'px'; cu.style.top=(lerp(sy,ty,m)-3)+'px'; cu.style.opacity = u<0.8?0:1;
        const c=(u-2.1); if (c>0 && c<0.6){ const s=1+c*7; rp.style.opacity=1-c/0.6; rp.style.left=tx+'px'; rp.style.top=ty+'px'; rp.style.transform=`scale(${s})`; } else rp.style.opacity=0;
        cu.style.transform = (c>0&&c<0.15)?'scale(.88)':'scale(1)';
      }
    }
  }
}
window.frame = frame;
"""


def build(spec, workdir, bounds):
    nsteps = max([sc.get("step") or 0 for sc in spec["scenes"]] + [1])
    scenes = []
    for i, sc in enumerate(spec["scenes"]):
        d = {"type": sc["type"], "t0": bounds[i], "t1": bounds[i + 1]}
        if sc["type"] == "shot":
            r = sc["_rect"]; k = SW / CSS_W
            zmax = min(SW / (r["width"] * k), SH / (r["height"] * k)) * 0.88
            d.update(rect=r, zoom=max(1.0, min(sc.get("zoom", 1.0), zmax)), click=sc.get("_click"))
        if sc["type"] == "recap":
            d["items"] = sc["items"]
        scenes.append(d)
    body = "".join(scene_html(i, sc, spec, nsteps) for i, sc in enumerate(spec["scenes"]))
    js = (JS.replace("__SCENES__", json.dumps(scenes)).replace("__K__", str(SW / CSS_W))
          .replace("__SW__", str(SW)).replace("__SH__", str(SH)))
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()}{CSS.replace('__SX__', str(SX)).replace('__SY__', str(SY)).replace('__SW__', str(SW)).replace('__SH__', str(SH))}</style></head>"
            f"<body>{body}<script>{js}</script></body></html>")
    for a in ("logo_blanc.png",):
        shutil.copy(KIT / a, workdir / a)
    shutil.copy(ATELIER / "assets" / "logo_couleur.png", workdir / "logo_couleur.png")
    (workdir / "index.html").write_text(html)
    return scenes


def shoot(workdir, total, fps, preview=0):
    from playwright.sync_api import sync_playwright
    frames = workdir / "frames"
    shutil.rmtree(frames, ignore_errors=True)
    frames.mkdir()
    times = ([total * (k + 0.5) / preview for k in range(preview)] if preview else [k / fps for k in range(int(total * fps))])
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H})
        pg.goto(f"file://{workdir}/index.html")
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(500)
        for k, t in enumerate(times):
            pg.evaluate(f"frame({t:.4f})")
            pg.screenshot(path=str(frames / f"f{k:05d}.jpg"), type="jpeg", quality=92)
        b.close()
    return frames


def main():
    a = sys.argv[1:]
    spec = load_spec(a[0])
    mp3 = pathlib.Path(a[1]).resolve()
    snaps = pathlib.Path(a[a.index("--snaps") + 1] if "--snaps" in a else "/home/claude/tuto/snaps").resolve()
    out = pathlib.Path(a[a.index("--out") + 1] if "--out" in a else HERE / "build").resolve()
    fps = int(a[a.index("--fps") + 1]) if "--fps" in a else 30
    preview = int(a[a.index("--preview") + 1]) if "--preview" in a else 0
    workdir = out / spec["slug"]
    workdir.mkdir(parents=True, exist_ok=True)
    wav, bounds, gaps, dur = split_voice(mp3, len(spec["scenes"]), workdir)
    print("silences retenus :", gaps)
    print("découpage :", bounds)
    resolve_shots(spec, snaps, workdir)
    build(spec, workdir, bounds)
    total = bounds[-1]
    frames = shoot(workdir, total, fps, preview)
    if preview:
        print("aperçu :", frames)
        return
    raw = workdir / "video_muette.mp4"
    sh(f'ffmpeg -y -loglevel error -framerate {fps} -i "{frames}/f%05d.jpg" -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p "{raw}"')
    final = out / f"{spec['slug']}.mp4"
    sh(f'bash "{ATELIER}/musique/mixer.sh" "{raw}" "{wav}" {spec.get("music", "aube")} "{final}" 0.18')
    json.dump({"bounds": bounds, "gaps": gaps, "duration": total}, open(workdir / "timing.json", "w"))
    print("vidéo :", final, round(total, 1), "s")


if __name__ == "__main__":
    main()
