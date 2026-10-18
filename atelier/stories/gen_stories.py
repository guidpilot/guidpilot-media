"""Stories Instagram GuidPilot — images fixes 1080x1920 (JPG), charte V2.
Zones interdites (interface Instagram) : 250 px en haut, 340 px en bas → tout le contenu tient entre y=250 et y=1580.
Pas de sticker (sondage, quiz, lien, musique, mention) : uniquement « Répondez à cette story » ou « lien en bio : guidpilot.fr ».
Usage : python3 stories/gen_stories.py <fichier_specs.py> <dossier_sortie>
  Le fichier de specs définit STORIES = [ {"name": ..., "type": ..., ...}, ... ] (voir stories/specs_2026-10-19.py).
Types : keyword (mot-clé ManyChat GUIDANCE / THÉRAPEUTE), teaser (Reel du jour), tip (conseil express),
        question (question ouverte), feature (capture du compte de démonstration), concours.
Texte : [mot] = mis en valeur (or sur marine, bleu sur clair)."""
import base64, html, pathlib, runpy, sys
from playwright.sync_api import sync_playwright

ATELIER = pathlib.Path(__file__).resolve().parent.parent
FONTS = ATELIER / "kit" / "fonts"
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
LOGO_W, LOGO_C = b64(ATELIER / "assets" / "logo_blanc.png"), b64(ATELIER / "assets" / "logo_couleur.png")

def font_face():
    return "".join(f'@font-face{{font-family:Inter;src:url(data:font/woff2;base64,{b64(FONTS / f"inter-latin-{w}-normal.woff2")}) format("woff2");font-weight:{w}}}' for w in (400, 600, 700, 800))

CSS = font_face() + """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;font-family:Inter,sans-serif;overflow:hidden}
.st{position:relative;width:1080px;height:1920px}
.navy{background:#0F172A;color:#fff}.light{background:#F6F8FC;color:#0F172A}
.zone{position:absolute;left:90px;right:90px;top:250px;bottom:340px;display:flex;flex-direction:column;justify-content:center}
.pill{align-self:flex-start;background:#E9C46A;color:#0F172A;font-weight:800;font-size:36px;letter-spacing:.06em;padding:16px 32px;border-radius:999px;text-transform:uppercase}
.light .pill{background:#E0E7FF;color:#1E3A8A}
.kick{font-weight:700;font-size:44px;line-height:1.25;color:#93C5FD;margin-bottom:10px}
.light .kick{color:#2563EB}
h1{font-weight:800;font-size:104px;line-height:1.06;letter-spacing:-.025em;margin-top:44px}
h1 span{color:#E9C46A}.light h1 span{color:#2563EB}
.sub{margin-top:44px;font-weight:600;font-size:48px;line-height:1.3;color:#CBD5E1}
.light .sub{color:#475569}
.box{margin-top:64px;border:4px dashed #E9C46A;border-radius:36px;padding:44px 46px;font-weight:800;font-size:58px;line-height:1.2}
.box small{display:block;margin-top:20px;font-weight:600;font-size:40px;line-height:1.3;color:#CBD5E1}
.light .box{border-color:#2563EB;background:#fff}.light .box small{color:#475569}
.box b{color:#E9C46A}.light .box b{color:#2563EB}
.legal{margin-top:40px;font-weight:600;font-size:30px;line-height:1.35;color:#94A3B8}
.logo{position:absolute;left:0;right:0;bottom:370px;text-align:center}.logo img{height:52px;opacity:.9}
.frame{margin-top:54px;background:#fff;border:2px solid #E2E8F0;border-radius:28px;overflow:hidden;box-shadow:0 24px 60px rgba(15,23,42,.12)}
.frame .bar{display:flex;align-items:center;gap:10px;padding:16px 22px;border-bottom:1px solid #E2E8F0;background:#F8FAFC}
.frame .bar i{width:16px;height:16px;border-radius:50%;background:#CBD5E1;display:block}
.frame .bar span{margin-left:auto;font-weight:600;font-size:26px;color:#64748B;background:#fff;border:1px solid #E2E8F0;border-radius:999px;padding:4px 18px}
.frame .vp{position:relative;overflow:hidden}.frame .vp img{position:absolute;max-width:none}
"""

def esc(t):
    out = html.escape(t).replace("[", "<span>").replace("]", "</span>")
    for a, b in (("« ", "«&nbsp;"), (" »", "&nbsp;»"), (" :", "&nbsp;:"), (" ?", "&nbsp;?"), (" !", "&nbsp;!"), (" 👆", "&nbsp;👆"), (" 💬", "&nbsp;💬")):
        out = out.replace(a, b)
    return out

def render(s):
    t = s["type"]; light = t in ("tip", "question", "feature")
    cls = "light" if light else "navy"
    parts = []
    if s.get("pill"): parts.append(f'<div class="pill">{esc(s["pill"])}</div>')
    if s.get("kick"): parts.append(f'<div class="kick" style="margin-top:{40 if s.get("pill") else 0}px">{esc(s["kick"])}</div>')
    parts.append(f'<h1 style="font-size:{s.get("size", 104)}px">{esc(s["title"])}</h1>')
    if s.get("sub"): parts.append(f'<div class="sub">{esc(s["sub"])}</div>')
    if t == "feature":
        x0, y0, x1, y1 = s["box"]; sc = min(900 / (x1 - x0), s.get("maxh", 560) / (y1 - y0))
        fw, fh = round((x1 - x0) * sc), round((y1 - y0) * sc)
        parts.append(f'<div class="frame" style="width:{fw}px"><div class="bar"><i></i><i></i><i></i><span>Compte de démonstration</span></div>'
                     f'<div class="vp" style="height:{fh}px"><img src="data:image/png;base64,{b64(ATELIER / s["img"])}" style="width:{round(s["W"]*sc)}px;left:{-round(x0*sc)}px;top:{-round(y0*sc)}px"></div></div>')
    if t == "keyword":
        parts.append(f'<div class="box">Répondez <b>{s["kw"]}</b> à cette story<small>et recevez en privé la présentation de GuidPilot&nbsp;: 14&nbsp;jours gratuits, sans carte bancaire.</small></div>')
    elif t == "teaser":
        parts.append(f'<div class="box">{esc(s.get("cta", "Nouveau Reel sur le profil 👆"))}</div>')
    elif t == "question":
        parts.append(f'<div class="box">Répondez à cette story&nbsp;💬<small>{esc(s.get("note", "Je lis toutes les réponses."))}</small></div>')
    elif t == "concours":
        parts.append(f'<div class="box">{esc(s["cta"])}</div>')
    if s.get("legal"): parts.append(f'<div class="legal">{esc(s["legal"])}</div>')
    logo = f'<div class="logo"><img src="data:image/png;base64,{LOGO_C if light else LOGO_W}"></div>' if s.get("logo", True) else ""
    return f'<div class="st {cls}"><div class="zone">{"".join(parts)}</div>{logo}</div>'

def main(specs_file, out_dir):
    stories = runpy.run_path(specs_file)["STORIES"]
    out = pathlib.Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for s in stories:
            pg.set_content(f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{render(s)}</body></html>")
            pg.wait_for_timeout(200)
            # contrôle automatique : le contenu doit rester dans la zone sûre (250 → 1580)
            r = pg.evaluate("(() => {const z=document.querySelector('.zone');let t=1e9,b=0;for(const e of z.children){const q=e.getBoundingClientRect();t=Math.min(t,q.top);b=Math.max(b,q.bottom)};const l=document.querySelector('.logo img');return [t,b,l?l.getBoundingClientRect().bottom:0]})()")
            ok = r[0] >= 250 and r[1] <= 1580 and r[2] <= 1580
            png = out / f'{s["name"]}.png'
            pg.screenshot(path=str(png))
            from PIL import Image
            Image.open(png).convert("RGB").save(out / f'{s["name"]}.jpg', quality=92); png.unlink()
            print(("OK " if ok else "HORS ZONE ") + s["name"], [round(x) for x in r])
        b.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
