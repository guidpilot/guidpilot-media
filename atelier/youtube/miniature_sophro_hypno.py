"""Miniature 1280x720 de la vidéo « Logiciel pour sophrologue et hypnothérapeute : les 4 moments d'un cycle de séances » (03/11/2026).
Usage : python3 miniature_erreurs_admin.py <sortie.jpg>"""
import base64, pathlib, sys
from playwright.sync_api import sync_playwright

A = pathlib.Path(__file__).resolve().parent.parent
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
F = A / "kit" / "fonts"
html = f'''<html><head><meta charset=utf-8><style>
@font-face{{font-family:I;src:url(data:font/woff2;base64,{b64(F / "inter-latin-800-normal.woff2")});font-weight:800}}
@font-face{{font-family:I;src:url(data:font/woff2;base64,{b64(F / "inter-latin-700-normal.woff2")});font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1280px;height:720px;background:#F6F8FC;font-family:I;position:relative;overflow:hidden}}
.k{{position:absolute;left:70px;top:70px;padding:12px 30px;border-radius:999px;background:#0F172A;color:#fff;font-weight:800;font-size:34px}}
h1{{position:absolute;left:70px;top:190px;font-weight:800;font-size:104px;line-height:1.02;letter-spacing:-.045em;color:#0F172A}}
h1 span{{color:#DC2626}}
h1 em{{font-style:normal;color:#2563EB}}
.ag{{position:absolute;left:830px;top:110px;width:400px;height:420px;border-radius:24px;background:#fff;border:3px solid #E2E8F0;box-shadow:0 30px 70px rgba(15,23,42,.18);transform:rotate(5deg);padding:28px;overflow:hidden}}
.ag b{{display:block;font-weight:800;font-size:30px;color:#0F172A}}
.ag .e{{margin-top:22px;padding:18px 20px;border-radius:14px;background:#EFF6FF;border-left:10px solid #2563EB;font-weight:800;font-size:26px;color:#1E3A8A}}
.ag .e.ab{{background:#FEF2F2;border-left-color:#DC2626;color:#7F1D1D}}
.ag .e i{{display:block;font-style:normal;font-weight:700;font-size:20px;margin-top:4px}}
.x{{position:absolute;left:1000px;top:385px;white-space:nowrap;padding:12px 26px;border-radius:999px;background:#DC2626;color:#fff;font-weight:800;font-size:44px;transform:rotate(-6deg)}}
img{{position:absolute;left:74px;bottom:56px;width:280px}}
</style></head><body><div class="k">Sophrologue · Hypnothérapeute</div>
<h1>Votre cycle<br/>de séances<br/><em>en 4 étapes</em></h1>
<div class="ag"><b>Mardi</b><div class="e">17 h · Sophrologie<i>Séance de suivi</i></div><div class="e ab">18 h · Hypnose<i>Séance 3</i></div><div class="e">19 h · Visio<i>Séance de suivi</i></div></div>
<div class="x">Oubliée ?</div>
<img src="data:image/png;base64,{b64(A / "assets" / "logo_couleur.png")}"></body></html>'''
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1280, "height": 720})
    pg.set_content(html); pg.wait_for_timeout(300)
    png = pathlib.Path(sys.argv[1]).with_suffix(".png"); pg.screenshot(path=str(png)); b.close()
from PIL import Image
Image.open(png).convert("RGB").save(sys.argv[1], quality=92); png.unlink()
print("ok", sys.argv[1])
