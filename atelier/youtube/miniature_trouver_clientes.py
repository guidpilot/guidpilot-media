"""Miniature 1280x720 de la vidéo « Comment trouver des clients en sophrologie, Reiki ou hypnose » (10/11/2026).
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
.wk{{position:absolute;left:800px;top:80px;width:420px;border-radius:24px;background:#fff;border:3px solid #E2E8F0;box-shadow:0 30px 70px rgba(15,23,42,.18);transform:rotate(4deg);overflow:hidden}}
.wk .hd{{padding:22px 26px;background:#0F172A;color:#fff;font-weight:800;font-size:28px}}
.wk .d{{display:flex;align-items:center;gap:16px;padding:16px 26px;border-top:2px solid #E2E8F0;font-weight:800;font-size:24px;color:#0F172A}}
.wk .d span{{flex:1;height:44px;border-radius:12px;border:3px dashed #CBD5E1}}
.q{{position:absolute;left:700px;top:470px;padding:16px 28px;border-radius:26px;border-bottom-left-radius:8px;background:#E9C46A;color:#0F172A;font-weight:800;font-size:36px;transform:rotate(-3deg)}}
img{{position:absolute;left:74px;bottom:56px;width:280px}}
</style></head><body><div class="k">Sophrologue · Reiki · Hypnose</div>
<h1>Agenda<br/>vide&nbsp;?<br/><em>5 questions</em></h1>
<div class="wk"><div class="hd">Cette semaine</div><div class="d">Lun<span></span></div><div class="d">Mar<span></span></div><div class="d">Mer<span></span></div><div class="d">Jeu<span></span></div></div>
<div class="q">«&nbsp;C'est pour moi&nbsp;?&nbsp;»</div>
<img src="data:image/png;base64,{b64(A / "assets" / "logo_couleur.png")}"></body></html>'''
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1280, "height": 720})
    pg.set_content(html); pg.wait_for_timeout(300)
    png = pathlib.Path(sys.argv[1]).with_suffix(".png"); pg.screenshot(path=str(png)); b.close()
from PIL import Image
Image.open(png).convert("RGB").save(sys.argv[1], quality=92); png.unlink()
print("ok", sys.argv[1])
