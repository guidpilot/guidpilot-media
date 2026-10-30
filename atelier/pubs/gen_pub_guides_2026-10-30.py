"""Publicités Meta « 3 guides offerts » — test du 30/10/2026, cible thérapeutes.
A : visuel fil 1080x1350 · B : story/reel 1080x1920 · C : carrousel 1080x1080 (4 cartes).
Usage : python3 atelier/pubs/gen_pub_guides_2026-10-30.py  → atelier/build/pubs/*.png"""
import base64, pathlib, sys
from playwright.sync_api import sync_playwright

ATELIER = pathlib.Path(__file__).resolve().parents[1]
REPO = ATELIER.parent
sys.path.insert(0, str(ATELIER / "carrousels"))
import gen_carrousels as g

OUT = ATELIER / "build" / "pubs"
OUT.mkdir(parents=True, exist_ok=True)
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
COV = [b64(REPO / "guides" / "couvertures" / f"guide-{i}.jpg") for i in (1, 2, 3)]
LOGO_W = b64(ATELIER / "assets" / "logo_blanc.png")
LOGO_C = b64(ATELIER / "assets" / "logo_couleur.png")
TITLES = ["Les 7 fausses croyances qui freinent votre activité",
          "Transformer vos abonnés et vos messages en rendez-vous",
          "Fidéliser, vous faire recommander et retrouver du temps"]

CSS = g.font_face() + """
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Inter,sans-serif;overflow:hidden;color:#fff;background:#0F172A}
.s{position:relative;width:100%;height:100%;padding:90px 84px;display:flex;flex-direction:column}
.kick{font-weight:700;font-size:30px;letter-spacing:.14em;text-transform:uppercase;color:#E9C46A}
h1{font-weight:800;line-height:1.06;letter-spacing:-.02em;margin-top:26px}
h1 span{color:#E9C46A}
.sub{font-weight:500;color:#CBD5E1;line-height:1.4;margin-top:26px}
.fan{position:relative;flex:1;display:flex;align-items:center;justify-content:center}
.fan img{position:absolute;border-radius:18px;box-shadow:0 30px 60px rgba(0,0,0,.45)}
.cta{align-self:flex-start;background:#E9C46A;color:#0F172A;font-weight:800;border-radius:999px}
.free{font-weight:600;color:#94A3B8;margin-top:22px}
.logo{position:absolute;right:84px;bottom:88px;height:46px}
.light{background:#F6F8FC;color:#0F172A}
.light .sub{color:#475569}
.light h1 span{color:#2563EB}
.light .kick{color:#B7892B}
.light .cta{background:#0F172A;color:#fff}
.light .free{color:#64748B}
.n{font-weight:800;font-size:120px;line-height:1;color:#E9C46A}
"""


def fan(w):
    """Éventail des 3 couvertures, largeur de couverture w."""
    h = int(w * 1287 / 909)
    pos = [(-0.62, -8, 0.92), (0.62, 8, 0.92), (0, 0, 1.0)]
    imgs = ""
    for (dx, rot, sc), i in zip(pos, (0, 2, 1)):
        imgs += (f'<img src="data:image/jpeg;base64,{COV[i]}" style="width:{int(w*sc)}px;height:{int(h*sc)}px;'
                 f'transform:translateX({int(dx*w)}px) rotate({rot}deg)">')
    return f'<div class="fan">{imgs}</div>'


SLIDES = {
 # A — fil Facebook / Instagram 4:5
 "pub-guides-fil-1080x1350": (1080, 1350, f'''<div class="s light">
   <div class="kick">Thérapeutes · énergéticiens · praticiens</div>
   <h1 style="font-size:84px">3 guides offerts pour <span>développer votre activité</span></h1>
   {fan(330)}
   <div class="cta" style="font-size:40px;padding:28px 50px">Recevoir les 3 guides</div>
   <div class="free" style="font-size:30px">Gratuit · Plus de 60 pages · Par e-mail</div>
   <img class="logo" src="data:image/png;base64,{LOGO_C}"></div>'''),
 # B — story / reel 9:16 (zones sûres : rien d'important dans les 250 px du haut ni du bas)
 "pub-guides-story-1080x1920": (1080, 1920, f'''<div class="s light" style="padding:270px 84px 300px">
   <div class="kick">Thérapeutes · énergéticiens · praticiens</div>
   <h1 style="font-size:92px">3 guides offerts pour <span>développer votre activité</span></h1>
   <div class="sub" style="font-size:40px">Trouver vos clientes, remplir votre agenda, retrouver du temps.</div>
   {fan(380)}
   <div class="cta" style="font-size:44px;padding:30px 56px">Recevoir les 3 guides</div>
   <div class="free" style="font-size:32px">Gratuit · Plus de 60 pages · Par e-mail</div>
   <img class="logo" style="bottom:300px" src="data:image/png;base64,{LOGO_C}"></div>'''),
}
# C — carrousel 1:1 : une carte par guide + une carte finale
for i, t in enumerate(TITLES):
    SLIDES[f"pub-guides-carrousel-{i+1}-1080x1080"] = (1080, 1080, f'''<div class="s light" style="flex-direction:row;gap:56px;align-items:center;padding:84px">
     <img src="data:image/jpeg;base64,{COV[i]}" style="width:400px;border-radius:16px;box-shadow:0 26px 50px rgba(15,23,42,.28)">
     <div><div class="kick" style="color:#2563EB">Guide {i+1} sur 3</div>
     <h1 style="font-size:60px">{g.esc(t)}</h1>
     <div class="sub" style="font-size:32px">Offert, avec les 2 autres guides.</div></div>
     <img class="logo" style="height:40px;bottom:64px" src="data:image/png;base64,{LOGO_C}"></div>''')
SLIDES["pub-guides-carrousel-4-1080x1080"] = (1080, 1080, f'''<div class="s" style="justify-content:center">
   <div class="kick">Gratuit</div>
   <h1 style="font-size:82px">Les 3 guides, <span>directement dans votre boîte mail</span></h1>
   <div class="sub" style="font-size:36px">Plus de 60 pages de conseils concrets pour les thérapeutes et praticiens.</div>
   <div class="cta" style="font-size:40px;padding:28px 50px;margin-top:56px">Recevoir les 3 guides</div>
   <img class="logo" src="data:image/png;base64,{LOGO_W}"></div>''')


def main():
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, (w, h, body) in SLIDES.items():
            pg = b.new_page(viewport={"width": w, "height": h})
            pg.set_content(f"<html><head><meta charset='utf-8'><style>{CSS}body{{width:{w}px;height:{h}px}}</style></head><body>{body}</body></html>")
            pg.wait_for_timeout(300)
            pg.screenshot(path=str(OUT / f"{name}.png"))
            pg.close()
            print("ok", name)
        b.close()


if __name__ == "__main__":
    main()
