"""Concours de lancement v2 — version dynamique, couleurs or/marine festives.
Usage : python3 gen_concours_v2.py <voix.wav> <reel|story> '<json des temps>'
Temps attendus : dur, prize2 (« deux abonnements »), adv (début avantages), a1..a6 (chaque avantage), tout (« Tout, dans un seul espace »),
                 cond (« Pour participer »), c1, c2, c3, fin (« Vous avez jusqu'au »), bonne (« Bonne chance »)
"""
import json, pathlib, shutil, sys
HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_reels.py").read_text().split("# ---------- Reel 1")[0]
ns = {"__file__": str(HERE / "gen_reels.py")}
exec(src, ns)
page, BASE, SRC = ns["page"], ns["BASE"], ns["SRC"]

voix, mode, T = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])
DUR = T["dur"]
GOLD, NAVY, CREAM = "#E9C46A", "#0F172A", "#FBF3DC"

EXTRA = f"""
.aibadge{{top:180px !important}}
.gold-bg{{background:{GOLD}}}
.boom{{font-weight:800;font-size:158px;letter-spacing:-.03em;color:{NAVY};line-height:1}}
.sub{{font-weight:800;font-size:58px;color:{NAVY};letter-spacing:.12em}}
.big1{{font-weight:800;font-size:230px;line-height:.9;color:#fff;letter-spacing:-.04em}}
.big1 small{{display:block;font-size:92px;color:{GOLD};margin-top:20px;letter-spacing:-.01em}}
.ribbon{{display:inline-block;margin-top:60px;padding:26px 50px;border-radius:999px;background:{GOLD};color:{NAVY};font-weight:800;font-size:60px}}
.conf{{position:absolute;width:26px;height:44px;border-radius:6px}}
.adv-title{{font-weight:800;font-size:76px;color:#fff;line-height:1.08}}
.adv-title span{{color:{GOLD}}}
.advcard{{position:absolute;left:60px;right:60px;top:540px;height:880px;border-radius:40px;background:#fff;overflow:hidden;box-shadow:0 40px 90px rgba(0,0,0,.35)}}
.advcard .lab{{position:absolute;left:0;right:0;top:0;height:150px;background:{CREAM};display:flex;align-items:center;justify-content:center;gap:24px;font-weight:800;font-size:58px;color:{NAVY}}}
.advcard .lab b{{display:flex;align-items:center;justify-content:center;width:84px;height:84px;border-radius:50%;background:{NAVY};color:{GOLD};font-size:44px}}
.advcard .pic{{position:absolute;left:30px;right:30px;top:180px;height:500px;overflow:hidden;border-radius:20px;border:2px solid #E2E8F0;display:flex;align-items:flex-start;justify-content:flex-start;background:#F6F8FC}}
.advcard .pic img{{width:100%;display:block;flex:none}}
.center{{z-index:5}}
.tagl{{position:absolute;left:30px;right:30px;bottom:50px;text-align:center;font-weight:800;font-size:58px;color:#0F172A}}
.tagl span{{color:#B7791F}}
.paybig{{text-align:center;width:100%;margin-top:110px}}
.paybig .amt{{font-weight:800;font-size:150px;color:{NAVY}}}
.paybig .ok{{margin-top:30px;display:inline-block;padding:22px 46px;border-radius:999px;background:#DCFCE7;color:#166534;font-weight:800;font-size:56px}}
.tout{{font-weight:800;font-size:96px;color:{NAVY};line-height:1.05}}
.st{{display:flex;align-items:center;gap:30px;margin:28px 0;padding:36px 42px;width:940px;border-radius:32px;background:#1E293B;border:3px solid #334155;text-align:left;font-weight:800;font-size:54px;line-height:1.15;color:#fff}}
.st b{{flex:none;display:flex;align-items:center;justify-content:center;width:100px;height:100px;border-radius:50%;background:{GOLD};color:{NAVY};font-size:56px}}
.st span{{color:{GOLD}}}
.date{{font-weight:800;font-size:76px;color:{NAVY};line-height:1.12}}
.go{{margin-top:56px;display:inline-block;background:{NAVY};color:{GOLD};font-weight:800;font-size:66px;padding:30px 66px;border-radius:999px}}
.small{{margin-top:50px;font-weight:600;font-size:30px;color:#5B4A1F;line-height:1.45;width:900px}}
"""

import random
random.seed(7)
def confetti(prefix, n, colors):
    out = ""
    for i in range(n):
        x = random.randint(20, 1040); c = random.choice(colors); r = random.randint(-40, 40)
        out += f'<div class="conf" id="{prefix}{i}" style="left:{x}px;top:-80px;background:{c};transform:rotate({r}deg)"></div>'
    return out

advs = [("Page de réservation", "page.png", "Vos clientes réservent <span>24 h/24</span>"), ("Paiement en ligne", None, "Payé <span>avant la séance</span>"), ("Agenda", "dash.png", "Votre semaine <span>d'un coup d'œil</span>"),
        ("Guidances écrites et vocales", "guid.png", "Livrées dans un <span>espace sécurisé</span>"), ("Factures automatiques", "finance.png", "Créées <span>toutes seules</span>"), ("Avis clients", "avis.png", "Demandés <span>en un clic</span>")]
adv_html = ""
for i, (lab, img, tg) in enumerate(advs):
    wmap = {"finance.png": "185%", "avis.png": "160%", "guid.png": "125%"}
    pic = f'<img src="assets/{img}" alt="" style="width:{wmap.get(img, "100%")}" />' if img else '<div class="paybig"><div class="amt">Payé ✓</div><div class="ok">Rendez-vous confirmé</div></div>'
    adv_html += f'<div class="advcard" id="v{i}"><div class="lab"><b>{i+1}</b>{lab}</div><div class="pic">{pic}</div><div class="tagl">{tg}</div></div>'

last = "Participez sur le post ↓" if mode == "story" else "Bonne chance !"
body = f'''
<div id="a" class="clip gold-bg" data-start="0" data-duration="{T['adv']}" data-track-index="1">
  {confetti("q", 34, [NAVY, "#fff", "#2563EB", CREAM])}
  <div class="center" style="top:300px"><div class="sub" id="as">LANCEMENT GUIDPILOT</div><div class="boom" id="ab" style="margin-top:20px">CONCOURS</div></div>
  <div id="a2" style="position:absolute;left:60px;right:60px;top:640px;bottom:220px;border-radius:50px;background:{NAVY};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
    <div class="big1" id="a3">1 AN<small>d'abonnement offert</small></div>
    <div class="ribbon" id="a4">+ 2 × 3 mois offerts</div>
  </div>
</div>
<div id="b" class="clip navy" data-start="{T['adv']}" data-duration="{T['cond']-T['adv']}" data-track-index="1">
  <div class="center" style="top:300px"><div class="adv-title" id="bt">GuidPilot, <span>c'est quoi ?</span></div></div>
  {adv_html}
  <div id="bw" class="gold-bg" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center">
    <div><div style="display:inline-block;background:#fff;border-radius:32px;padding:34px 50px;margin-bottom:60px"><img src="assets/logo_couleur.png" alt="GuidPilot" style="width:520px;display:block" /></div>
    <div class="tout">Tout,<br/>dans un seul espace</div></div>
  </div>
</div>
<div id="c" class="clip navy" data-start="{T['cond']}" data-duration="{T['fin']-T['cond']}" data-track-index="1">
  <div class="center" style="top:330px"><div class="adv-title" id="ct">Pour <span>participer</span></div></div>
  <div class="center" style="top:620px">
    <div class="st" id="s1"><b>1</b><div>Abonnez-vous à <span>@guidpilot.fr</span></div></div>
    <div class="st" id="s2"><b>2</b><div>Aimez ce post</div></div>
    <div class="st" id="s3"><b>3</b><div>Commentez <span>« GuidPilot »</span> + votre spécialité</div></div>
  </div>
</div>
<div id="d" class="clip gold-bg" data-start="{T['fin']}" data-duration="{DUR-T['fin']}" data-track-index="1">
  {confetti("z", 26, [NAVY, "#fff", "#2563EB"])}
  <div class="center" style="top:420px">
    <div class="date" id="d1">Jusqu'au<br/>lundi 26 octobre<br/>23h59</div>
    <div class="date" id="d2" style="font-size:52px;margin-top:30px">Tirage au sort le 27 octobre</div>
    <div class="go" id="d3">{last}</div>
    <div class="small" id="d4">Réservé aux praticiens et praticiennes en activité, 18 ans et plus, résidant en France. Participation gratuite. Jeu ni organisé ni sponsorisé par Instagram.</div>
  </div>
</div>'''

def fall(prefix, n, t0, span):
    s = ""
    for i in range(n):
        dl = t0 + random.random() * 0.8; dur = span * (0.7 + random.random() * 0.5)
        s += f'tl.fromTo("#{prefix}{i}",{{y:0,rotation:{random.randint(-90,90)}}},{{y:2100,rotation:{random.randint(200,720)},duration:{dur:.2f},ease:"none"}},{dl:.2f});\n'
    return s

js = f'''
tl.fromTo("#as",{{opacity:0,y:-40}},{{opacity:1,y:0,duration:.35,ease:E}},.05);
tl.fromTo("#ab",{{opacity:0,scale:3}},{{opacity:1,scale:1,duration:.45,ease:"power4.in"}},.15);
tl.to("#ab",{{x:12,duration:.05,yoyo:true,repeat:5,ease:"none"}},.6);
tl.fromTo("#a2",{{opacity:0,y:300,scale:.9}},{{opacity:1,y:0,scale:1,duration:.55,ease:"back.out(1.4)"}},.9);
tl.fromTo("#a3",{{opacity:0,scale:.4}},{{opacity:1,scale:1,duration:.55,ease:"back.out(2.2)"}},1.3);
tl.to("#a3",{{scale:1.06,duration:.3,yoyo:true,repeat:3,ease:"sine.inOut"}},2.0);
tl.fromTo("#a4",{{opacity:0,scale:.5,rotation:-6}},{{opacity:1,scale:1,rotation:0,duration:.5,ease:"back.out(2.5)"}},{T['prize2']});
''' + fall("q", 34, 0.5, 3.2) + f'''
tl.fromTo("#bt",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.4,ease:E}},{T['adv']+.05});
'''
for i in range(6):
    t = T[f"a{i+1}"]; nxt = T[f"a{i+2}"] if i < 5 else T["tout"]
    side = 1 if i % 2 == 0 else -1
    js += f'tl.fromTo("#v{i}",{{opacity:0,x:{1100*side},rotation:{8*side}}},{{opacity:1,x:0,rotation:0,duration:.4,ease:"power3.out"}},{t:.2f});\n'
    if i in (0, 2): js += f'tl.fromTo("#v{i} .pic img",{{y:0}},{{y:-160,duration:{max(nxt-t-0.4,0.6):.2f},ease:"sine.inOut"}},{t+0.3:.2f});\n'
    js += f'tl.to("#v{i}",{{opacity:0,x:{-1100*side},rotation:{-8*side},duration:.3,ease:"power2.in"}},{nxt-0.25:.2f});\n'
js += f'tl.fromTo("#bw",{{opacity:0,scale:1.2}},{{opacity:1,scale:1,duration:.45,ease:"power3.out"}},{T["tout"]:.2f});\n'
js += f'tl.fromTo("#ct",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.4,ease:E}},{T["cond"]+.05:.2f});\n'
for k in (1, 2, 3):
    js += f'tl.fromTo("#s{k}",{{opacity:0,scale:.6,y:60}},{{opacity:1,scale:1,y:0,duration:.45,ease:"back.out(2.2)"}},{T[f"c{k}"]:.2f});\n'
    js += f'tl.to("#s{k}",{{borderColor:"{GOLD}",duration:.2}},{T[f"c{k}"]+.3:.2f});\n'
js += f'''tl.fromTo("#d1",{{opacity:0,scale:.7}},{{opacity:1,scale:1,duration:.5,ease:"back.out(2)"}},{T["fin"]+.05:.2f});
tl.fromTo("#d2",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.4,ease:E}},{T["fin"]+.8:.2f});
tl.fromTo("#d4",{{opacity:0}},{{opacity:1,duration:.5}},{T["fin"]+.5:.2f});
tl.fromTo("#d3",{{opacity:0,scale:.5}},{{opacity:1,scale:1,duration:.5,ease:"back.out(2.5)"}},{T["bonne"]:.2f});
tl.to("#d3",{{scale:1.07,duration:.35,yoyo:true,repeat:5,ease:"sine.inOut"}},{T["bonne"]+.6:.2f});
''' + fall("z", 26, T["bonne"] - 0.2, 3.0)

d = BASE / "build" / f"concours2-{mode}"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(SRC / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(SRC / f, d / f)
for a in ("logo_blanc.png", "page.png", "dash.png", "guid.png", "finance.png", "avis.png"): shutil.copy(SRC / "assets" / a, d / "assets" / a)
shutil.copy(BASE / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(voix, d / "assets" / "voix.wav")
shutil.copy(BASE / "reels" / "ambient30.wav", d / "assets" / "ambient.wav")
(d / "index.html").write_text(page(DUR, body, js, "voix.wav").replace("</style>", EXTRA + "</style>", 1))
print("ok", d)
