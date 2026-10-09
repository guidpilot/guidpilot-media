"""Vidéo YouTube 1920x1080 : « Calendly, WhatsApp, agenda… pourquoi ce n'est pas adapté aux tarologues » + histoire de GuidPilot.
Usage : python3 gen_comparatif.py <voix.wav>  -> build/yt-comparatif/
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
base = (HERE / "gen_presentation.py").read_text().split("T = dict(")[0]
ns = {"__file__": str(HERE / "gen_presentation.py")}
exec(base, ns)
CSS, frame, ATELIER, KIT = ns["CSS"], ns["frame"], ns["ATELIER"], ns["KIT"]
DUR = 90.0

EXTRA = """
.toolchip{position:absolute;padding:24px 42px;border-radius:22px;background:#1E293B;border:2px solid #334155;color:#E2E8F0;font-weight:700;font-size:44px;white-space:nowrap}
.kick{font-weight:700;font-size:30px;letter-spacing:.16em;text-transform:uppercase;color:#E9C46A}
.evt{display:flex;align-items:center;gap:26px;margin:16px 0;padding:22px 34px;border-radius:20px;background:#1E293B;border:2px solid #334155;color:#E2E8F0;font-weight:600;font-size:36px;width:820px}
.evt b{color:#F87171;font-weight:800;width:110px}
table.cmp{position:absolute;left:150px;top:175px;width:1620px;border-collapse:separate;border-spacing:0 10px}
.cmp th{font-weight:800;font-size:32px;color:#0F172A;padding:10px 0;text-align:center}
.cmp th.gp{color:#2563EB}
.cmp td{background:#fff;font-weight:600;font-size:29px;padding:9px 24px;text-align:center;border-top:2px solid #E2E8F0;border-bottom:2px solid #E2E8F0}
.cmp td:first-child{text-align:left;border-left:2px solid #E2E8F0;border-radius:16px 0 0 16px;width:560px}
.cmp td:last-child{border-right:2px solid #E2E8F0;border-radius:0 16px 16px 0;background:#EFF6FF}
.y,.n{display:inline-flex;width:48px;height:48px;border-radius:50%;align-items:center;justify-content:center;font-size:30px;font-weight:800}
.y{background:#DCFCE7;color:#16A34A}.n{background:#FEE2E2;color:#DC2626}
.banner{position:absolute;left:150px;right:150px;bottom:30px;padding:22px 30px;border-radius:18px;background:#0F172A;color:#fff;text-align:center;font-weight:800;font-size:38px}
.banner span{color:#F87171}
.note{position:absolute;right:150px;top:110px;padding:14px 26px;border-radius:999px;background:#FBF3DC;color:#6B4E16;font-weight:700;font-size:28px}
.step{display:flex;align-items:center;gap:22px;margin:18px 0;font-weight:700;font-size:34px;color:#94A3B8}
.step i{font-style:normal;flex:none;width:58px;height:58px;border-radius:50%;background:#E2E8F0;color:#64748B;display:flex;align-items:center;justify-content:center;font-size:28px}
.step.on{color:#0F172A}.step.on i{background:#2563EB;color:#fff}
.card{width:500px;padding:50px 40px;border-radius:28px;background:#fff;border:2px solid #E2E8F0;text-align:center;box-shadow:0 20px 60px rgba(15,23,42,.08)}
.card .ic{font-weight:800;font-size:96px;color:#2563EB;line-height:1}
.card h3{font-weight:800;font-size:44px;margin-top:22px;line-height:1.15}
.card p{font-weight:500;font-size:28px;color:#64748B;margin-top:14px;line-height:1.35}
"""

rows = [("Réservation en ligne", "y", "n", "y"), ("Paiement en ligne", "y", "n", "y"), ("Factures automatiques", "n", "n", "y"),
        ("Livraison des guidances", "n", "n", "y"), ("Espace client sécurisé", "n", "n", "y"), ("Demande d'avis", "n", "n", "y"),
        ("Pensé pour la guidance", "n", "n", "y")]
sym = {"y": "✓", "n": "✕"}
trs = "".join(f'<tr><td>{r[0]}</td>' + "".join(f'<td><span class="{v}" id="c{ci}_{ri}">{sym[v]}</span></td>' for ci, v in enumerate(r[1:])) + "</tr>" for ri, r in enumerate(rows))

tools = [("Calendly", 180, 80), ("Agenda en ligne", 980, 40), ("WhatsApp", 520, 230), ("Tableur", 1240, 260), ("Logiciel de factures", 300, 400)]
tool_html = "".join(f'<div class="toolchip" id="t{i}" style="left:{x}px;top:{y}px">{n}</div>' for i, (n, x, y) in enumerate(tools))

body = f'''
<div id="a" class="clip navy" data-start="0" data-duration="12.6" data-track-index="1">
  <div style="position:absolute;left:0;right:0;top:120px;height:520px">{tool_html}</div>
  <div class="center" style="top:700px"><div class="big" id="a1" style="font-size:66px">Tarologue, voyante, praticienne en guidance : <span>vous jonglez avec tout ça ?</span></div></div>
  <div class="center" id="a2" style="top:380px"><div class="big" style="font-size:96px">Aucun n'a été pensé <span>pour votre métier.</span></div></div>
</div>
<div id="b" class="clip navy" data-start="12.6" data-duration="18.3" data-track-index="1">
  <div style="position:absolute;left:150px;top:150px;width:800px">
    <div class="kick" id="bk">L'histoire de GuidPilot</div>
    <div class="big" id="b1" style="width:800px;font-size:70px;margin-top:26px;text-align:left">Une praticienne en guidance, <span>débordée le soir</span></div>
  </div>
  <div style="position:absolute;left:150px;top:560px">
    <div class="evt" id="e1"><b>21 h</b>Répondre aux messages</div>
    <div class="evt" id="e2"><b>22 h</b>Relancer un paiement</div>
    <div class="evt" id="e3"><b>23 h</b>Préparer une facture</div>
  </div>
  <div style="position:absolute;left:1060px;top:260px;width:720px;text-align:center" id="b2">
    <div style="font-weight:700;font-size:40px;color:#CBD5E1">Normane, son compagnon, veut l'aider.</div>
    <div style="font-weight:800;font-size:56px;color:#fff;margin-top:24px">Il crée un outil <span style="color:#60A5FA">rien que pour elle.</span></div>
    <img src="assets/logo_blanc.png" alt="GuidPilot" style="width:480px;margin-top:60px" />
  </div>
  <div style="position:absolute;left:1060px;top:820px;width:720px;text-align:center" id="b3">
    <div class="offer">Aujourd'hui : pour toutes les praticiennes</div>
  </div>
</div>
<div id="c" class="clip light" data-start="30.9" data-duration="24.3" data-track-index="1">
  <div class="note" id="cn">Un agenda en ligne ne connaît pas vos clientes</div>
  <div style="position:absolute;left:150px;top:96px;font-weight:800;font-size:56px" id="ct">Comparons <span style="color:#2563EB">honnêtement</span></div>
  <table class="cmp"><tr><th></th><th id="h0">Outil de RDV<br/><span style="font-weight:600;font-size:24px;color:#64748B">type Calendly</span></th><th id="h1">WhatsApp</th><th class="gp" id="h2">GuidPilot</th></tr>{trs}</table>
  <div class="banner" id="cb">Résultat : <span>plusieurs outils, des copier-coller et des oublis</span></div>
</div>
<div id="d" class="clip light" data-start="55.2" data-duration="14.6" data-track-index="1">
  <img class="logo-corner" src="assets/logo_couleur.png" alt="GuidPilot" />
  <div class="col" style="width:620px">
    <div class="chap" id="dc"><b>✓</b>Avec GuidPilot</div>
    <div class="h" id="dh">Tout est <span>relié</span></div>
    <div style="margin-top:30px">
      <div class="step" id="s1"><i>1</i>Réservation et paiement</div>
      <div class="step" id="s2"><i>2</i>Agenda, fiche et facture</div>
      <div class="step" id="s3"><i>3</i>Guidance écrite ou vocale</div>
      <div class="step" id="s4"><i>4</i>Avis en un clic</div>
    </div>
  </div>
  {frame("f1","page.png",1000,760,150)}{frame("f2","dash.png",1000,760,150)}{frame("f3","guid.png",1000,442,300)}{frame("f4","avis.png",1000,260,400)}
</div>
<div id="e" class="clip light" data-start="69.8" data-duration="9.0" data-track-index="1">
  <div class="center" style="top:140px"><div class="big" style="color:#0F172A;font-size:64px" id="eh">Ce que ça change <span style="color:#2563EB">pour vous</span></div></div>
  <div style="position:absolute;left:0;right:0;top:400px;display:flex;justify-content:center;gap:50px">
    <div class="card" id="k1"><div class="ic">01</div><h3>Du temps gagné</h3><p>Moins d'administratif, plus de séances</p></div>
    <div class="card" id="k2"><div class="ic">02</div><h3>Des clientes gardées</h3><p>Une réponse et une réservation immédiates</p></div>
    <div class="card" id="k3"><div class="ic">03</div><h3>Sereine et pro</h3><p>Une image professionnelle et rassurante</p></div>
  </div>
</div>
<div id="g" class="clip navy" data-start="78.8" data-duration="{round(DUR-78.8,2)}" data-track-index="1">
  <div class="center" id="g6" style="top:150px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="offer" style="margin-top:46px">Essai gratuit</div>
    <div class="big14">14 jours gratuits</div>
    <div class="nocard" id="g7">✓ Sans carte bancaire</div>
    <div class="url" id="g8">guidpilot.fr</div>
    <div class="sub" id="g9"><i></i>Abonnez-vous : une vidéo par jour</div>
  </div>
</div>'''

def pop(sel, t, ease="back.out(1.6)", y=30):
    return f'tl.fromTo("{sel}",{{opacity:0,y:{y}}},{{opacity:1,y:0,duration:.45,ease:"{ease}"}},{t});\n'
def zoom(sel, t):
    return f'tl.fromTo("{sel}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,duration:.35,ease:"back.out(2.5)"}},{t});\n'

js = "".join(f'tl.fromTo("#t{i}",{{opacity:0,y:-80,rotation:{-10 if i%2 else 10}}},{{opacity:1,y:0,rotation:{-3 if i%2 else 3},duration:.5,ease:"back.out(2)"}},{t});\n' for i, t in enumerate([0.2, 1.0, 1.8, 2.5, 3.3]))
js += 'tl.to(["#t0","#t2","#t4"],{y:-18,duration:.6,yoyo:true,repeat:5,ease:"sine.inOut"},4.2);\ntl.to(["#t1","#t3"],{y:18,duration:.6,yoyo:true,repeat:5,ease:"sine.inOut"},4.2);\n'
js += pop("#a1", 5.0, "power3.out")
js += 'tl.to(["#t0","#t1","#t2","#t3","#t4","#a1"],{opacity:0,scale:.9,duration:.5,ease:"power2.in"},9.4);\n'
js += 'tl.fromTo("#a2",{opacity:0,scale:.8},{opacity:1,scale:1,duration:.7,ease:"back.out(1.6)"},9.9);\n'
js += pop("#bk", 12.8) + pop("#b1", 13.1, "power3.out")
js += "".join(f'tl.fromTo("#e{i+1}",{{opacity:0,x:-60}},{{opacity:1,x:0,duration:.45,ease:"back.out(1.6)"}},{t});\n' for i, t in enumerate([17.4, 19.2, 21.0]))
js += 'tl.fromTo("#b2",{opacity:0,x:80},{opacity:1,x:0,duration:.7,ease:"power3.out"},23.9);\n'
js += 'tl.to(["#e1","#e2","#e3"],{opacity:.35,duration:.5},24.4);\n'
js += 'tl.fromTo("#b3",{opacity:0,scale:.8},{opacity:1,scale:1,duration:.6,ease:"back.out(2)"},27.0);\n'
js += pop("#ct", 31.0, "power3.out") + pop("#h0", 32.6) + pop("#h1", 41.8) + pop("#h2", 52.9)
js += zoom("#c0_0", 33.6) + zoom("#c0_1", 34.6)
js += "".join(zoom(f"#c0_{r}", t) for r, t in [(2, 36.8), (3, 38.0), (4, 38.6), (5, 39.6), (6, 40.4)])
js += "".join(zoom(f"#c1_{r}", 42.4 + r * 0.45) for r in range(7))
js += pop("#cn", 47.6) + pop("#cb", 51.9, "back.out(1.4)", 40)
js += "".join(zoom(f"#c2_{r}", 53.2 + r * 0.25) for r in range(7))
js += pop("#dc", 55.3) + pop("#dh", 55.5, "power3.out")
steps = [(57.0, "f1"), (59.5, "f2"), (64.1, "f3"), (67.8, "f4")]
for i, (t, f) in enumerate(steps):
    js += f'tl.to("#s{i+1}",{{color:"#0F172A",duration:.3}},{t});\ntl.to("#s{i+1} i",{{backgroundColor:"#2563EB",color:"#fff",duration:.3}},{t});\n'
    js += f'tl.fromTo("#{f}",{{opacity:0,x:100,scale:.96}},{{opacity:1,x:0,scale:1,duration:.6,ease:"power3.out"}},{t});\n'
    if i < 3:
        js += f'tl.to("#{f}",{{opacity:0,x:-60,duration:.4,ease:"power2.in"}},{steps[i+1][0]-0.35});\n'
js += 'tl.fromTo("#f1i",{y:0},{y:-200,duration:2.2,ease:"sine.inOut"},57.4);\n'
js += 'tl.fromTo("#f2i",{y:0},{y:-120,duration:4,ease:"sine.inOut"},59.9);\n'
js += pop("#eh", 69.9, "power3.out") + pop("#k1", 70.0, y=60) + pop("#k2", 72.1, y=60) + pop("#k3", 75.3, y=60)
js += 'tl.fromTo("#g6",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},78.9);\n'
js += pop("#g7", 81.7) + pop("#g8", 82.9) + pop("#g9", 84.3)
js += 'tl.to("#g9",{scale:1.06,duration:.45,yoyo:true,repeat:5,ease:"sine.inOut"},85.0);\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1920" data-height="1080">
<div class="aibadge">Voix off générée par IA</div>
<audio id="voix" src="assets/voix.wav" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
{body}
</div>
<script>
const tl=gsap.timeline({{paused:true}}); const E="power3.out";
tl.set(["#a2","#b2","#b3"],{{opacity:0}},0);
{js}
window.__timelines["main"]=tl;
</script></body></html>'''

d = ATELIER / "build" / "yt-comparatif"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for a in ("page.png", "dash.png", "guid.png", "avis.png", "logo_blanc.png"): shutil.copy(KIT / "assets" / a, d / "assets" / a)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d)
