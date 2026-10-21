"""Miniature 1280x720 de la vidéo « Devenir partenaire GuidPilot » (21/10/2026).
Usage : python3 miniature_partenaires.py <sortie.jpg>"""
import base64, pathlib, sys
from playwright.sync_api import sync_playwright

A = pathlib.Path(__file__).resolve().parent.parent
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
F = A / "kit" / "fonts"
html = f'''<html><head><meta charset=utf-8><style>
@font-face{{font-family:I;src:url(data:font/woff2;base64,{b64(F / "inter-latin-800-normal.woff2")});font-weight:800}}
@font-face{{font-family:I;src:url(data:font/woff2;base64,{b64(F / "inter-latin-700-normal.woff2")});font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1280px;height:720px;background:#0F172A;font-family:I;position:relative;overflow:hidden}}
.ring{{position:absolute;right:-160px;top:-160px;width:620px;height:620px;border-radius:50%;border:60px solid #1E293B}}
.k{{position:absolute;left:80px;top:90px;padding:12px 28px;border-radius:999px;background:#E9C46A;color:#0F172A;font-weight:800;font-size:34px}}
h1{{position:absolute;left:80px;top:190px;font-weight:800;font-size:150px;line-height:.98;letter-spacing:-.04em;color:#fff}}
h1 span{{color:#E9C46A}}
.s{{position:absolute;left:84px;top:520px;font-weight:700;font-size:38px;color:#93C5FD}}
img{{position:absolute;right:70px;bottom:60px;width:330px}}
</style></head><body><div class="ring"></div><div class="k">On recrute</div>
<h1>Devenez<br/><span>partenaire</span></h1><div class="s">Formateurs · Créateurs · Praticiens</div>
<img src="data:image/png;base64,{b64(A / "assets" / "logo_blanc.png")}"></body></html>'''
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1280, "height": 720})
    pg.set_content(html); pg.wait_for_timeout(300)
    png = pathlib.Path(sys.argv[1]).with_suffix(".png"); pg.screenshot(path=str(png)); b.close()
from PIL import Image
Image.open(png).convert("RGB").save(sys.argv[1], quality=92); png.unlink()
print("ok", sys.argv[1])
