"""Miniature 1280x720 de la vidéo « Se faire payer avant une guidance » (13/11/2026, guidance).
Usage : python3 miniature_payer_avant.py <sortie.jpg>"""
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
.ph{{position:absolute;left:820px;top:70px;width:380px;height:600px;border-radius:44px;background:#fff;border:10px solid #0F172A;box-shadow:0 30px 70px rgba(15,23,42,.25);transform:rotate(4deg);overflow:hidden}}
.ph .hd{{padding:26px 24px;background:#F1F5F9;font-weight:800;font-size:24px;color:#0F172A}}
.ph .b{{margin:22px 20px 0;padding:16px 20px;border-radius:22px;font-weight:700;font-size:24px;line-height:1.3;max-width:280px}}
.ph .me{{margin-left:auto;background:#2563EB;color:#fff}}
.ph .cl{{background:#fff;border:2px solid #E2E8F0;color:#0F172A}}
.ph .st{{margin:18px 20px 0 auto;width:fit-content;padding:10px 18px;border-radius:999px;background:#FEE2E2;color:#B91C1C;font-weight:800;font-size:22px}}
.q{{position:absolute;left:640px;top:520px;padding:18px 30px;border-radius:26px;border-bottom-left-radius:8px;background:#E9C46A;color:#0F172A;font-weight:800;font-size:40px;transform:rotate(-3deg)}}
img{{position:absolute;left:74px;bottom:56px;width:280px}}
</style></head><body><div class="k">Tarologue · Voyante · Médium</div>
<h1>Payée<br/><em>avant</em><br/>la séance</h1>
<div class="ph"><div class="hd">Émilie R.</div><div class="b me">Votre guidance audio est prête&nbsp;!</div><div class="b cl">Je vous fais le virement ce soir 🙏</div><div class="st">● En attente · 12 jours</div></div>
<div class="q">«&nbsp;Je peux payer après&nbsp;?&nbsp;»</div>
<img src="data:image/png;base64,{b64(A / "assets" / "logo_couleur.png")}"></body></html>'''
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1280, "height": 720})
    pg.set_content(html); pg.wait_for_timeout(300)
    png = pathlib.Path(sys.argv[1]).with_suffix(".png"); pg.screenshot(path=str(png)); b.close()
from PIL import Image
Image.open(png).convert("RGB").save(sys.argv[1], quality=92); png.unlink()
print("ok", sys.argv[1])
