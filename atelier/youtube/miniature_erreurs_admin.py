"""Miniature 1280x720 de la vidéo « Tarologue, voyante : 5 erreurs administratives à éviter » (30/10/2026).
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
.inv{{position:absolute;left:900px;top:100px;width:320px;height:470px;border-radius:18px;background:#fff;border:3px solid #E2E8F0;box-shadow:0 30px 70px rgba(15,23,42,.18);transform:rotate(6deg);padding:40px}}
.inv b{{display:block;font-weight:800;font-size:46px;color:#0F172A}}
.inv i{{display:block;font-style:normal;margin-top:10px;font-weight:800;font-size:34px;color:#94A3B8}}
.inv .l{{height:18px;border-radius:9px;background:#E2E8F0;margin-top:28px}}
.x{{position:absolute;left:860px;top:290px;white-space:nowrap;padding:12px 24px;border:7px solid #DC2626;border-radius:16px;color:#DC2626;font-weight:800;font-size:46px;transform:rotate(-12deg);background:rgba(255,255,255,.92)}}
img{{position:absolute;left:74px;bottom:56px;width:280px}}
</style></head><body><div class="k">Tarologue · Voyante</div>
<h1><span>5 erreurs</span><br/>administratives<br/><em>à éviter</em></h1>
<div class="inv"><b>Facture</b><i>N° ???</i><div class="l"></div><div class="l" style="width:70%"></div><div class="l"></div><div class="l" style="width:55%"></div><div class="l"></div></div>
<div class="x">SANS NUMÉRO</div>
<img src="data:image/png;base64,{b64(A / "assets" / "logo_couleur.png")}"></body></html>'''
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1280, "height": 720})
    pg.set_content(html); pg.wait_for_timeout(300)
    png = pathlib.Path(sys.argv[1]).with_suffix(".png"); pg.screenshot(path=str(png)); b.close()
from PIL import Image
Image.open(png).convert("RGB").save(sys.argv[1], quality=92); png.unlink()
print("ok", sys.argv[1])
