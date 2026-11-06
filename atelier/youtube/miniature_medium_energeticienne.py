"""Miniature 1280x720 de la vidéo « Logiciel pour médium et énergéticienne : la checklist des consultations à distance » (06/11/2026).
Usage : python3 miniature_medium_energeticienne.py <sortie.jpg>"""
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
h1 span{{color:#B7791F}}
h1 em{{font-style:normal;color:#2563EB}}
.cb{{position:absolute;left:820px;top:90px;width:410px;height:470px;border-radius:24px;background:#fff;border:3px solid #E2E8F0;box-shadow:0 30px 70px rgba(15,23,42,.18);transform:rotate(4deg);padding:56px 28px 20px}}
.cb:before{{content:"";position:absolute;left:50%;top:-18px;width:150px;height:44px;margin-left:-75px;border-radius:12px;background:#0F172A;border:5px solid #E9C46A}}
.r{{display:flex;align-items:center;gap:18px;margin-top:22px;padding:16px 18px;border-radius:16px;background:#F8FAFC;border:3px solid #E2E8F0;font-weight:800;font-size:27px;color:#0F172A}}
.r i{{flex:none;width:44px;height:44px;border-radius:12px;background:#2563EB;color:#fff;font-style:normal;display:flex;align-items:center;justify-content:center;font-size:28px}}
.r.o i{{background:#fff;border:4px solid #CBD5E1}}
.r.o{{border-color:#E9C46A;background:#FFFBEB}}
img{{position:absolute;left:74px;bottom:56px;width:280px}}
</style></head><body><div class="k">Médium · Énergéticienne</div>
<h1>Consultations<br/>à distance&nbsp;:<br/><em>la checklist</em></h1>
<div class="cb"><div class="r"><i>✓</i>Réservation</div><div class="r"><i>✓</i>Paiement</div><div class="r"><i>✓</i>Guidance rangée</div><div class="r o"><i></i>Votre page</div></div>
<img src="data:image/png;base64,{b64(A / "assets" / "logo_couleur.png")}"></body></html>'''
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1280, "height": 720})
    pg.set_content(html); pg.wait_for_timeout(300)
    png = pathlib.Path(sys.argv[1]).with_suffix(".png"); pg.screenshot(path=str(png)); b.close()
from PIL import Image
Image.open(png).convert("RGB").save(sys.argv[1], quality=92); png.unlink()
print("ok", sys.argv[1])
