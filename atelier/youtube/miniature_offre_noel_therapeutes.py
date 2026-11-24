"""Miniature 1280x720 de la vidéo « Logiciel pour sophrologue, Reiki, hypnose : 1 an pour 99 €, ce que cela comprend » (24/11/2026, thérapeutes, offre de Noël).
Usage : python3 miniature_offre_noel_therapeutes.py <sortie.jpg>"""
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
h1{{position:absolute;left:70px;top:190px;font-weight:800;font-size:96px;line-height:1.02;letter-spacing:-.045em;color:#0F172A}}
h1 span{{color:#B7791F}}
h1 em{{font-style:normal;color:#2563EB;font-size:64px}}
.cd{{position:absolute;left:800px;top:140px;width:420px;border-radius:30px;background:#fff;border:3px solid #E2E8F0;box-shadow:0 30px 70px rgba(15,23,42,.22);transform:rotate(3deg);overflow:hidden}}
.cd .hd{{padding:24px 30px;background:#0F172A;color:#fff;font-weight:800;font-size:28px;white-space:nowrap}}
.cd .r{{display:flex;align-items:center;gap:18px;padding:24px 30px;border-top:2px solid #E2E8F0;font-weight:800;font-size:34px;color:#0F172A}}
.cd .r i{{font-style:normal;width:50px;height:50px;border-radius:14px;background:#16A34A;color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px}}
.q{{position:absolute;left:70px;top:478px;white-space:nowrap;padding:20px 34px;border-radius:999px;background:#E9C46A;color:#0F172A;font-weight:800;font-size:40px;transform:rotate(-2deg)}}
img{{position:absolute;left:74px;bottom:28px;width:250px}}
</style></head><body><div class="k">Sophrologie · Reiki · Hypnose</div>
<h1>1 an<br/>pour <span>99&nbsp;€</span><br/><em>Ce qui est compris</em></h1>
<div class="cd"><div class="hd">🎁 Compris dans l'année</div><div class="r"><i>✓</i>Réservation</div><div class="r"><i>✓</i>Paiement</div><div class="r"><i>✓</i>Factures</div></div>
<div class="q">🎁 Jusqu'au 31 décembre</div>
<img src="data:image/png;base64,{b64(A / "assets" / "logo_couleur.png")}"></body></html>'''
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1280, "height": 720})
    pg.set_content(html); pg.wait_for_timeout(300)
    png = pathlib.Path(sys.argv[1]).with_suffix(".png"); pg.screenshot(path=str(png)); b.close()
from PIL import Image
Image.open(png).convert("RGB").save(sys.argv[1], quality=92); png.unlink()
print("ok", sys.argv[1])
