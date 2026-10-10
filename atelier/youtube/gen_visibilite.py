"""Vidéo YouTube 1920x1080 : « Instagram, TikTok, Google Meet et l'annuaire : votre visibilité simplifiée » (tuto/promo).
Usage : python3 gen_visibilite.py <voix.wav>  -> build/yt-visibilite/
Temps calés sur voix/2026-10-10_yt-visibilite-reseaux.mp3 (104,2 s).
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
base = (HERE / "gen_presentation.py").read_text().split("T = dict(")[0]
ns = {"__file__": str(HERE / "gen_presentation.py")}
exec(base, ns)
CSS, frame, section, ATELIER, KIT = ns["CSS"], ns["frame"], ns["section"], ns["ATELIER"], ns["KIT"]
DUR = 106.5
T = dict(b=17.0, c=28.4, d=42.4, e=58.8, f=70.6, g=82.5, h=92.1)

EXTRA = """
.phone{position:absolute;width:430px;height:840px;border-radius:56px;background:#fff;border:10px solid #1E293B;box-shadow:0 30px 80px rgba(15,23,42,.25);overflow:hidden}
.phone.dark{border-color:#334155}
.notch{position:absolute;left:50%;top:14px;width:120px;height:28px;margin-left:-60px;border-radius:999px;background:#1E293B}
.vid{position:absolute;left:20px;right:20px;top:60px;height:470px;border-radius:26px;background:#1E3A8A;display:flex;align-items:center;justify-content:center}
.play{width:110px;height:110px;border-radius:50%;background:rgba(255,255,255,.2);display:flex;align-items:center;justify-content:center;color:#fff;font-size:52px}
.vidcap{position:absolute;left:24px;bottom:22px;color:#fff;font-weight:700;font-size:26px}
.likes{position:absolute;left:28px;top:550px;font-weight:800;font-size:34px;color:#0F172A;display:flex;align-items:center;gap:12px}
.likes i{font-style:normal;color:#DC2626;font-size:40px}
.bub{position:absolute;max-width:330px;padding:16px 22px;border-radius:24px;font-weight:600;font-size:24px;line-height:1.3}
.bub.in{left:22px;background:#F1F5F9;color:#0F172A;border-bottom-left-radius:6px}
.bub.out{right:22px;background:#2563EB;color:#fff;border-bottom-right-radius:6px}
.seen{position:absolute;left:0;right:0;text-align:center;font-weight:700;font-size:24px;color:#DC2626}
.hk{position:absolute;left:130px;top:340px;width:1050px}
.hk .big{width:1050px;text-align:left;font-size:80px}
.titleA{position:absolute;left:0;right:0;top:270px;text-align:center;color:#fff}
.chips5{position:absolute;left:0;right:0;top:690px;display:flex;justify-content:center;gap:24px;flex-wrap:wrap;padding:0 120px}
.c5{padding:20px 34px;border-radius:999px;background:#1E293B;border:2px solid #334155;color:#E2E8F0;font-weight:700;font-size:34px;display:flex;align-items:center;gap:14px}
.c5 b{display:inline-flex;width:44px;height:44px;border-radius:50%;background:#2563EB;color:#fff;align-items:center;justify-content:center;font-size:24px}
.prof{position:absolute;left:0;right:0;top:70px;text-align:center}
.avatar{width:150px;height:150px;border-radius:50%;margin:0 auto;background:#E2E8F0;border:5px solid #E9C46A;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:56px;color:#0F172A}
.pname{font-weight:800;font-size:32px;margin-top:20px}
.pbio{font-weight:500;font-size:24px;color:#64748B;margin-top:10px;line-height:1.4;padding:0 30px}
.plink{display:inline-flex;align-items:center;gap:10px;margin-top:22px;padding:14px 26px;border-radius:999px;background:#EFF6FF;color:#2563EB;font-weight:800;font-size:26px;border:2px solid #BFDBFE}
.grid9{position:absolute;left:20px;right:20px;top:500px;display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.grid9 div{height:120px;border-radius:12px;background:#E2E8F0}
.x{display:flex;align-items:center;gap:18px;margin:14px 0;font-weight:700;font-size:34px;color:#94A3B8}
.x i{font-style:normal;flex:none;width:50px;height:50px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:26px;background:#FEE2E2;color:#DC2626}
.x.ok{color:#0F172A}.x.ok i{background:#DCFCE7;color:#16A34A}
.x s{text-decoration-thickness:3px}
.step{display:flex;align-items:center;gap:22px;margin:16px 0;font-weight:700;font-size:34px;color:#94A3B8}
.step i{font-style:normal;flex:none;width:58px;height:58px;border-radius:50%;background:#E2E8F0;color:#64748B;display:flex;align-items:center;justify-content:center;font-size:28px}
.mock{position:absolute;left:900px;top:170px;width:840px;padding:44px 50px;border-radius:28px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.mock h4{font-weight:800;font-size:38px}
.mock .sm{font-weight:600;font-size:24px;color:#64748B;margin-top:8px}
.slots{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:30px}
.slot{padding:20px 0;text-align:center;border-radius:16px;border:2px solid #E2E8F0;font-weight:700;font-size:30px;color:#0F172A;background:#F8FAFC}
.slot.off{color:#CBD5E1;text-decoration:line-through}
.payb{margin-top:34px;padding:24px;border-radius:18px;background:#0F172A;color:#fff;text-align:center;font-weight:800;font-size:32px}
.okpay{margin-top:24px;padding:22px;border-radius:18px;background:#DCFCE7;color:#166534;text-align:center;font-weight:800;font-size:32px}
.illus{position:absolute;right:30px;top:12px;font-size:18px;font-weight:600;color:#64748B;background:#F1F5F9;border-radius:999px;padding:4px 14px}
.msgcount{position:absolute;left:900px;top:820px;width:840px;text-align:center;font-weight:800;font-size:36px;color:#DC2626}
.node{position:absolute;width:420px;padding:40px 30px;border-radius:28px;text-align:center;background:#fff;border:2px solid #E2E8F0;box-shadow:0 20px 60px rgba(15,23,42,.08)}
.node h5{font-weight:800;font-size:40px}
.node p{font-weight:600;font-size:26px;color:#64748B;margin-top:12px;line-height:1.35}
.node.gp{border-color:#2563EB;background:#EFF6FF}
.soc{display:inline-flex;margin:6px;padding:10px 22px;border-radius:999px;background:#0F172A;color:#fff;font-weight:700;font-size:26px}
.arr{position:absolute;font-weight:700;font-size:28px;color:#2563EB;text-align:center;width:680px}
.arr .ln{height:6px;border-radius:3px;background:#2563EB;margin:10px 0;position:relative}
.arr.r .ln:after{content:"";position:absolute;right:-4px;top:-9px;border:12px solid transparent;border-left:18px solid #2563EB;border-right:0}
.arr.l .ln:before{content:"";position:absolute;left:-4px;top:-9px;border:12px solid transparent;border-right:18px solid #2563EB;border-left:0}
.split{position:absolute;left:900px;top:640px;width:880px;display:flex;gap:24px}
.split div{flex:1;padding:26px;border-radius:20px;font-weight:700;font-size:30px;text-align:center;line-height:1.3}
.split .you{background:#FBF3DC;color:#6B4E16}.split .gpb{background:#0F172A;color:#fff}
.meet{margin-top:34px;display:flex;align-items:center;justify-content:center;gap:16px;padding:26px;border-radius:18px;background:#2563EB;color:#fff;font-weight:800;font-size:32px}
.row{display:flex;justify-content:space-between;margin-top:18px;font-weight:600;font-size:28px;color:#475569}
.row b{color:#0F172A}
.cities{position:absolute;left:900px;top:780px;width:840px;display:flex;align-items:center;justify-content:center;gap:20px}
.city{white-space:nowrap;padding:16px 30px;border-radius:999px;background:#0F172A;color:#fff;font-weight:700;font-size:30px}
.dash{flex:none;width:120px;border-top:5px dashed #94A3B8}
.rec{display:flex;align-items:center;gap:22px;font-weight:700;font-size:44px;color:#fff;margin:16px 0}
.rec i{font-style:normal;flex:none;width:62px;height:62px;border-radius:50%;background:#2563EB;color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px}
"""

def phone(id_, inner, left, top, cls=""):
    return f'<div class="phone {cls}" id="{id_}" style="left:{left}px;top:{top}px"><div class="notch"></div>{inner}</div>'

hook_phone = phone("ph", '''
  <div class="vid"><div class="play">▶</div><div class="vidcap">Votre vidéo du jour</div></div>
  <div class="likes" id="lk"><i>♥</i><span id="lkn">0</span> j'aime</div>
  <div class="bub in" id="m1" style="top:620px">Bonjour ! Vous faites des tirages ?</div>
  <div class="bub out" id="m2" style="top:700px">Oui, je vous explique…</div>
  <div class="seen" id="m3" style="top:785px">… et plus de nouvelles</div>''', 1330, 120, "dark")

prof_phone = phone("pp", '''
  <div class="prof"><div class="avatar">CD</div><div class="pname">Camille Dubois</div>
  <div class="pbio">Guidance &amp; astrologie · Séances en visio</div>
  <div class="plink" id="pl">🔗 Réserver une séance</div></div>
  <div class="grid9"><div></div><div></div><div></div><div></div><div></div><div></div></div>''', 1180, 120)

chaps = ["Un seul lien", "Réservation", "Vos réseaux", "Visio", "Annuaire"]
c5 = "".join(f'<div class="c5" id="q{i}"><b>{i+1}</b>{t}</div>' for i, t in enumerate(chaps))

body = f'''
<div id="a" class="clip navy" data-start="0" data-duration="{T['b']}" data-track-index="1">
  <div class="hk" id="a1"><div class="big">Vous publiez sur <span>Instagram ou TikTok</span> pour trouver des clientes ?</div></div>
  {hook_phone}
  <div id="a2" style="position:absolute;inset:0">
    <div class="titleA"><div class="kick" style="font-weight:700;font-size:30px;letter-spacing:.16em;color:#E9C46A">TUTO GUIDPILOT</div>
      <div class="big" style="width:auto;margin-top:26px;font-size:78px">Instagram, TikTok, Google Meet, annuaire :<br/><span>votre visibilité simplifiée</span></div></div>
    <div class="chips5">{c5}</div>
  </div>
</div>
{section("b", T['b'], T['c'], 1, "Votre bio", "Un seul lien <span>dans votre bio</span>",
  '<div style="margin-top:30px">'
  '<div class="x" id="x1"><i>✕</i><s>Trois liens différents</s></div>'
  '<div class="x" id="x2"><i>✕</i><s>Un numéro de téléphone</s></div>'
  '<div class="x ok" id="x3"><i>✓</i>Le lien de votre page praticienne</div></div>'
  '<div class="p" id="bp" style="font-size:30px">Activité, prestations, avis et bouton « Prendre rendez-vous ».</div>',
  prof_phone + frame("bf", "page.png", 1000, 760, 150))}
{section("c", T['c'], T['d'], 2, "Réservation", "Elle réserve <span>et paie en ligne</span>",
  '<div style="margin-top:30px">'
  '<div class="step" id="s1"><i>1</i>Elle clique sur votre lien</div>'
  '<div class="step" id="s2"><i>2</i>Elle choisit sa séance</div>'
  '<div class="step" id="s3"><i>3</i>Elle choisit un créneau libre</div>'
  '<div class="step" id="s4"><i>4</i>Elle paie en ligne</div></div>'
  '<div class="tag" id="ct">Le rendez-vous arrive dans votre agenda</div>',
  '<div class="mock" id="cm"><span class="illus">Illustration</span><h4>Tirage de tarot · Visio</h4><div class="sm">Choisissez un créneau</div>'
  '<div class="slots"><div class="slot off">10:00</div><div class="slot" id="sl">14:00</div><div class="slot">16:30</div>'
  '<div class="slot">18:00</div><div class="slot off">19:00</div><div class="slot">20:30</div></div>'
  '<div class="payb" id="pb">Payer en ligne</div><div class="okpay" id="po">✓ Paiement reçu · Rendez-vous confirmé</div></div>'
  '<div class="msgcount" id="mc">Fini les 10 messages pour fixer une date</div>'
  + frame("cf", "dash.png", 1000, 760, 150))}
<div id="d" class="clip light" data-start="{T['d']}" data-duration="{round(T['e']-T['d'],2)}" data-track-index="1">
  <img class="logo-corner" src="assets/logo_couleur.png" alt="GuidPilot" />
  <div style="position:absolute;left:110px;top:120px">
    <div class="chap" id="dc"><b>3</b>Vos réseaux</div>
    <div class="h" id="dh" style="font-size:64px">Instagram et TikTok <span>sur votre page</span></div>
  </div>
  <div class="node" id="n1" style="left:150px;top:400px"><h5>Vos réseaux</h5><p><span class="soc">Instagram</span><span class="soc">TikTok</span></p><p>Vos vidéos, vos publications</p></div>
  <div class="node gp" id="n2" style="left:1350px;top:400px"><h5>Votre page GuidPilot</h5><p>Prestations, avis, réservation</p></div>
  <div class="arr r" id="r1" style="left:620px;top:440px">Le lien dans votre bio<div class="ln"></div></div>
  <div class="arr l" id="r2" style="left:620px;top:560px"><div class="ln"></div>Vos liens affichés sur votre page</div>
  <div class="split" id="sp" style="left:150px;top:780px;width:1620px">
    <div class="you" id="sp1">Vous : vous publiez sur vos réseaux, à votre rythme</div>
    <div class="gpb" id="sp2">GuidPilot : tout ce qui vient après, la réservation</div>
  </div>
</div>
{section("e", T['e'], T['f'], 4, "Séances à distance", "En visio avec <span>Google Meet</span>",
  '<div class="p" id="ep">Le lien de la visio est prêt pour la séance. Votre cliente n\'a qu\'à cliquer à l\'heure du rendez-vous.</div>',
  '<div class="mock" id="em" style="top:250px"><span class="illus">Illustration</span><h4>Mardi · 14:00 – 14:45</h4><div class="sm">Tirage de tarot · Visio</div>'
  '<div class="row"><span>Cliente</span><b>Julie M.</b></div><div class="row"><span>Paiement</span><b style="color:#16A34A">Reçu</b></div>'
  '<div class="meet" id="mb">▶ Rejoindre la visio Google Meet</div></div>'
  '<div class="cities" id="ci"><div class="city">Lille</div><div class="dash"></div><div class="city" style="background:#2563EB">Votre séance</div><div class="dash"></div><div class="city">Marseille</div></div>')}
{section("f", T['f'], T['g'], 5, "Être trouvée", "L'annuaire <span>GuidPilot</span>",
  '<div class="p" id="fp">Votre page apparaît dans l\'annuaire des praticiens, où de nouvelles clientes peuvent vous trouver.</div>'
  '<div class="tag" id="ft">Une porte d\'entrée de plus, hors algorithmes</div>',
  frame("ff", "annuaire.png", 1000, 425, 290))}
<div id="g" class="clip navy" data-start="{T['g']}" data-duration="{round(T['h']-T['g'],2)}" data-track-index="1">
  <div style="position:absolute;left:0;right:0;top:110px;text-align:center"><div class="big" style="width:auto;font-size:72px" id="gh">Récapitulons</div></div>
  <div style="position:absolute;left:470px;top:300px">
    <div class="rec" id="r_1"><i>1</i>Un seul lien dans votre bio</div>
    <div class="rec" id="r_2"><i>2</i>Réservation et paiement en ligne</div>
    <div class="rec" id="r_3"><i>3</i>Vos réseaux affichés sur votre page</div>
    <div class="rec" id="r_4"><i>4</i>La visio avec Google Meet</div>
    <div class="rec" id="r_5"><i>5</i>L'annuaire pour être trouvée</div>
  </div>
</div>
<div id="h" class="clip navy" data-start="{T['h']}" data-duration="{round(DUR-T['h'],2)}" data-track-index="1">
  <div class="center" id="g6" style="top:150px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="offer" style="margin-top:46px">Essai gratuit</div>
    <div class="big14">14 jours gratuits</div>
    <div class="nocard" id="g7">✓ Sans carte bancaire</div>
    <div class="url" id="g8">guidpilot.fr</div>
    <div class="sub" id="g9"><i></i>Abonnez-vous : une vidéo par jour</div>
  </div>
</div>'''

E = "power3.out"
def pop(sel, t, ease="back.out(1.6)", y=30):
    return f'tl.fromTo("{sel}",{{opacity:0,y:{y}}},{{opacity:1,y:0,duration:.45,ease:"{ease}"}},{t});\n'
def out(sels, t, x=-60):
    s = ",".join(f'"{x_}"' for x_ in sels)
    return f'tl.to([{s}],{{opacity:0,x:{x},duration:.4,ease:"power2.in"}},{t});\n'
def fin(sel, t):
    return f'tl.fromTo("{sel}",{{opacity:0,x:120,scale:.95}},{{opacity:1,x:0,scale:1,duration:.7,ease:"{E}"}},{t});\n'
def head(i, t):
    return pop(f"#{i}c", t + .1, E) + pop(f"#{i}h", t + .25, E, 40)
def light(sel, t):
    return (f'tl.to("{sel}",{{color:"#0F172A",duration:.3}},{t});\n'
            f'tl.to("{sel} i",{{backgroundColor:"#2563EB",color:"#fff",duration:.3}},{t});\n')

# A : accroche (0 -> 17)
js = pop("#a1", 0.6, E, 50) + fin("#ph", 1.2)
js += 'const lk={v:0};tl.to(lk,{v:248,duration:2.2,ease:"power2.out",onUpdate:()=>{document.getElementById("lkn").textContent=Math.round(lk.v)}},6.3);\n'
js += 'tl.fromTo("#lk",{scale:1},{scale:1.15,duration:.25,yoyo:true,repeat:3,ease:"sine.inOut"},6.3);\n'
js += pop("#m1", 8.1) + pop("#m2", 9.0)
js += 'tl.to(["#m1","#m2"],{opacity:.35,duration:.5},9.8);\n' + pop("#m3", 10.0)
js += 'tl.to(["#a1","#ph"],{opacity:0,y:-30,duration:.5,ease:"power2.in"},11.2);\n'
js += 'tl.fromTo("#a2",{opacity:0,scale:.92},{opacity:1,scale:1,duration:.7,ease:"back.out(1.4)"},11.6);\n'
js += "".join(pop(f"#q{i}", 13.0 + i * .5, y=40) for i in range(5))

# B : un seul lien (17 -> 28.4)
js += head("b", T['b']) + fin("#pp", 17.6)
js += 'tl.fromTo("#pl",{scale:1},{scale:1.1,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"},18.6);\n'
js += pop("#x1", 20.2) + pop("#x2", 21.0) + pop("#x3", 22.5)
js += out(["#pp"], 24.0) + fin("#bf", 24.3) + pop("#bp", 24.4, E)
js += 'tl.fromTo("#bfi",{y:0},{y:-200,duration:3.6,ease:"sine.inOut"},25.0);\n'

# C : réservation (28.4 -> 42.4)
js += head("c", T['c']) + fin("#cm", 28.7)
js += "".join(light(f"#s{i+1}", t) for i, t in enumerate([28.8, 30.4, 31.9, 33.9]))
js += f'tl.to("#sl",{{backgroundColor:"#2563EB",color:"#fff",borderColor:"#2563EB",scale:1.08,duration:.35}},32.1);\n'
js += f'tl.fromTo("#pb",{{scale:1}},{{scale:.95,duration:.15,yoyo:true,repeat:1}},34.0);\n'
js += pop("#po", 34.5) + pop("#mc", 35.8, y=20)
js += out(["#cm", "#mc"], 37.4) + fin("#cf", 37.7) + pop("#ct", 38.0)
js += 'tl.fromTo("#cfi",{y:0},{y:-123,duration:2.5,ease:"sine.inOut"},38.6);\n'

# D : réseaux (42.4 -> 58.8)
js += head("d", T['d'])
js += 'tl.fromTo("#n1",{opacity:0,x:-80},{opacity:1,x:0,duration:.6,ease:"power3.out"},42.9);\n'
js += 'tl.fromTo("#n2",{opacity:0,x:80},{opacity:1,x:0,duration:.6,ease:"power3.out"},43.6);\n'
js += 'tl.fromTo("#r1",{opacity:0,scaleX:0,transformOrigin:"left center"},{opacity:1,scaleX:1,duration:.6,ease:"power2.out"},44.6);\n'
js += 'tl.fromTo("#r2",{opacity:0,scaleX:0,transformOrigin:"right center"},{opacity:1,scaleX:1,duration:.6,ease:"power2.out"},47.2);\n'
js += pop("#sp1", 51.3, y=40) + pop("#sp2", 56.4, y=40)
js += 'tl.fromTo("#sp2",{scale:1},{scale:1.04,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"},57.0);\n'

# E : Google Meet (58.8 -> 70.6)
js += head("e", T['e']) + fin("#em", 59.1) + pop("#ep", 62.7, E)
js += 'tl.fromTo("#mb",{scale:1},{scale:1.06,duration:.35,yoyo:true,repeat:5,ease:"sine.inOut"},63.4);\n'
js += 'tl.fromTo("#ci",{opacity:0,y:40},{opacity:1,y:0,duration:.6,ease:"back.out(1.6)"},66.5);\n'

# F : annuaire (70.6 -> 82.5)
js += head("f", T['f']) + fin("#ff", 71.0) + pop("#fp", 73.1, E)
js += 'tl.fromTo("#ffi",{scale:1,transformOrigin:"0 0"},{scale:1.04,duration:8,ease:"sine.inOut"},71.8);\n'
js += pop("#ft", 78.9)

# G : récap (82.5 -> 92.1)
js += pop("#gh", 82.6, E)
js += "".join(f'tl.fromTo("#r_{i+1}",{{opacity:0,x:-60}},{{opacity:1,x:0,duration:.45,ease:"back.out(1.6)"}},{t});\n'
              for i, t in enumerate([82.9, 85.2, 87.3, 89.3, 90.8]))

# H : fin (92.1 -> fin)
js += 'tl.fromTo("#g6",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},92.2);\n'
js += pop("#g7", 94.6) + pop("#g8", 95.8) + pop("#g9", 97.2)
js += 'tl.to("#g9",{scale:1.06,duration:.45,yoyo:true,repeat:7,ease:"sine.inOut"},98.0);\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1920" data-height="1080">
<div class="aibadge">Voix off générée par IA</div>
<audio id="voix" src="assets/voix.wav" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
{body}
</div>
<script>
const tl=gsap.timeline({{paused:true}});
tl.set(["#a2","#m3","#po","#mc","#ct","#x1","#x2","#x3","#bp","#r1","#r2","#sp1","#sp2","#ci","#ft","#g7","#g8","#g9"],{{opacity:0}},0);
{js}
window.__timelines["main"]=tl;
</script></body></html>'''

d = ATELIER / "build" / "yt-visibilite"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for a in ("page.png", "dash.png", "annuaire.png", "logo_blanc.png"): shutil.copy(KIT / "assets" / a, d / "assets" / a)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d)
