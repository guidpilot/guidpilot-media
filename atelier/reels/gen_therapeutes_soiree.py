"""Reel thérapeutes « La soirée administrative » (9:16) — scènes illustrées (horloge, to-do, téléphone).
Usage : python3 gen_therapeutes_soiree.py <voix.wav> '<json temps>'
Temps : dur, soir (« Votre dernière séance »), todo (« Mais la soirée »), t1..t4 (chaque tâche), gp (« Avec GuidPilot »),
        g1 (« réservent et paient »), g2 (« La facture »), g3 (« Et vos notes »), libre (« Votre soirée vous appartient »), cta (« Essai gratuit »)
"""
import json, pathlib, shutil, sys
HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_reels.py").read_text().split("# ---------- Reel 1")[0]
ns = {"__file__": str(HERE / "gen_reels.py")}
exec(src, ns)
page, cta, cta_js, BASE, SRC = ns["page"], ns["cta"], ns["cta_js"], ns["BASE"], ns["SRC"]
voix, T = sys.argv[1], json.loads(sys.argv[2])
DUR = T["dur"]

EXTRA = """
.aibadge{top:180px !important}
.prof{position:absolute;padding:24px 44px;border-radius:999px;background:#1E293B;border:2px solid #334155;color:#fff;font-weight:700;font-size:50px;white-space:nowrap}
.prof b{color:#E9C46A;font-weight:800}
.clock{position:absolute;left:50%;top:330px;width:380px;height:380px;margin-left:-190px}
.todo{position:absolute;left:90px;right:90px;top:800px}
.td{display:flex;align-items:center;gap:30px;margin:22px 0;padding:30px 36px;border-radius:26px;background:#fff;font-weight:700;font-size:48px;color:#0F172A;box-shadow:0 18px 40px rgba(0,0,0,.25)}
.td i{flex:none;width:70px;height:70px;border-radius:18px;border:5px solid #CBD5E1;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:46px;color:#fff}
.phone{position:absolute;left:50%;top:420px;width:620px;height:1000px;margin-left:-310px;border-radius:70px;background:#0F172A;border:14px solid #1E293B;box-shadow:0 40px 90px rgba(15,23,42,.35)}
.screen{position:absolute;inset:24px;border-radius:50px;background:#F6F8FC;overflow:hidden}
.notif{position:absolute;left:24px;right:24px;padding:26px 28px;border-radius:28px;background:#fff;box-shadow:0 10px 30px rgba(15,23,42,.12);font-size:30px;color:#334155;line-height:1.35}
.notif b{display:block;font-size:34px;color:#0F172A;margin-bottom:6px}
.notif .ok{color:#16A34A;font-weight:800}
.lab{position:absolute;left:0;right:0;text-align:center;font-weight:800;font-size:66px;color:#0F172A;line-height:1.1}
.lab span{color:#2563EB}
.libre{font-weight:800;font-size:110px;color:#fff;line-height:1.05;width:940px}
.libre span{color:#E9C46A}
"""
profs = [("Sophrologue", 90, 520), ("Hypnothérapeute", 300, 680), ("Praticienne <b>Reiki</b>", 130, 840), ("Réflexologue", 420, 1000), ("Énergéticienne", 160, 1160)]
prof_html = "".join(f'<div class="prof" id="p{i}" style="left:{x}px;top:{y}px">{t}</div>' for i, (t, x, y) in enumerate(profs))
clock_svg = '''<svg class="clock" id="clk" viewBox="0 0 200 200"><circle cx="100" cy="100" r="94" fill="#1E293B" stroke="#E9C46A" stroke-width="6"/>''' + "".join(
    f'<line x1="100" y1="14" x2="100" y2="26" stroke="#94A3B8" stroke-width="4" transform="rotate({a} 100 100)"/>' for a in range(0, 360, 30)) + '''
<line id="hh" x1="100" y1="100" x2="100" y2="52" stroke="#fff" stroke-width="8" stroke-linecap="round" transform="rotate(630 100 100)"/>
<line id="mh" x1="100" y1="100" x2="100" y2="30" stroke="#E9C46A" stroke-width="5" stroke-linecap="round" transform="rotate(180 100 100)"/>
<circle cx="100" cy="100" r="7" fill="#E9C46A"/></svg>'''
tasks = ["Confirmer les rendez-vous de demain", "Relancer un paiement", "Faire une facture", "Retrouver mes notes"]
todo_html = "".join(f'<div class="td" id="k{i}"><i id="ki{i}"></i><span>{t}</span></div>' for i, t in enumerate(tasks))

body = f'''
<div id="a" class="clip navy" data-start="0" data-duration="{T['soir']}" data-track-index="1">
  <div class="center" style="top:300px"><div class="kicker" id="ak" style="font-size:44px">THÉRAPEUTES</div></div>
  {prof_html}
</div>
<div id="b" class="clip navy" data-start="{T['soir']}" data-duration="{T['gp']-T['soir']}" data-track-index="1">
  {clock_svg}
  <div class="center" style="top:730px"><div class="big" id="bt" style="font-size:64px">Séance terminée… <span>la soirée commence</span></div></div>
  <div class="todo" style="top:900px">{todo_html}</div>
</div>
<div id="c" class="clip light" data-start="{T['gp']}" data-duration="{T['libre']-T['gp']}" data-track-index="1">
  <div class="lab" id="ct" style="top:250px">Avec <span>GuidPilot</span></div>
  <div class="phone" id="ph"><div class="screen">
    <div class="notif" id="n1" style="top:60px"><b>Nouvelle réservation</b>Séance de sophrologie · 1 h · mardi 18h<br/><span class="ok">✓ Payé en ligne</span></div>
    <div class="notif" id="n2" style="top:320px"><b>Facture créée automatiquement</b>N° 2026-0042 · envoyée à votre cliente</div>
    <div class="notif" id="n3" style="top:575px"><b>Fiche client · notes de séance</b>Historique des séances et notes<br/><span class="ok">✓ Privées, jamais visibles par le client</span></div>
  </div></div>
</div>
<div id="d" class="clip navy" data-start="{T['libre']}" data-duration="{T['cta']-T['libre']}" data-track-index="1">
  <div class="center" style="top:560px"><div class="libre" id="dl">Votre soirée <span>vous appartient.</span></div></div>
</div>
{cta(T['cta'], DUR - T['cta'])}'''

js = 'tl.fromTo("#ak",{opacity:0,y:30},{opacity:1,y:0,duration:.4,ease:E},.05);\n'
js += "".join(f'tl.fromTo("#p{i}",{{opacity:0,scale:.5,rotation:{-8 if i%2 else 8}}},{{opacity:1,scale:1,rotation:0,duration:.4,ease:"back.out(2.2)"}},{0.25+i*0.45:.2f});\n' for i in range(5))
js += f'tl.fromTo("#clk",{{opacity:0,scale:.6}},{{opacity:1,scale:1,duration:.5,ease:"back.out(1.8)"}},{T["soir"]+.05:.2f});\n'
js += f'tl.fromTo("#mh",{{rotation:0}},{{rotation:360,duration:{T["gp"]-T["soir"]:.2f},ease:"none",svgOrigin:"100 100"}},{T["soir"]:.2f});\n'
js += f'tl.fromTo("#hh",{{rotation:0}},{{rotation:30,duration:{T["gp"]-T["soir"]:.2f},ease:"none",svgOrigin:"100 100"}},{T["soir"]:.2f});\n'
js += f'tl.fromTo("#bt",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.45,ease:E}},{T["todo"]:.2f});\n'
for i in range(4):
    js += f'tl.fromTo("#k{i}",{{opacity:0,y:-60,rotation:{-3 if i%2 else 3}}},{{opacity:1,y:0,rotation:{-1.5 if i%2 else 1.5},duration:.4,ease:"back.out(2)"}},{T[f"t{i+1}"]:.2f});\n'
js += f'tl.to(["#k0","#k1","#k2","#k3"],{{x:8,duration:.07,yoyo:true,repeat:9,ease:"none"}},{T["gp"]-1.1:.2f});\n'
js += f'tl.fromTo("#ct",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.45,ease:E}},{T["gp"]+.05:.2f});\n'
js += f'tl.fromTo("#ph",{{opacity:0,y:300}},{{opacity:1,y:0,duration:.6,ease:"power3.out"}},{T["gp"]+.1:.2f});\n'
for k, key in ((1, "g1"), (2, "g2"), (3, "g3")):
    js += f'tl.fromTo("#n{k}",{{opacity:0,y:-80,scale:.9}},{{opacity:1,y:0,scale:1,duration:.45,ease:"back.out(1.8)"}},{T[key]:.2f});\n'
js += f'tl.fromTo("#dl",{{opacity:0,scale:.8}},{{opacity:1,scale:1,duration:.6,ease:"back.out(1.6)"}},{T["libre"]+.05:.2f});\n'
js += cta_js(T["cta"], T["cta"] + 1.6, T["cta"] + 2.6)

d = BASE / "build" / "therapeutes-soiree"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(SRC / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(SRC / f, d / f)
shutil.copy(SRC / "assets" / "logo_blanc.png", d / "assets" / "logo_blanc.png")
shutil.copy(voix, d / "assets" / "voix.wav")
shutil.copy(BASE / "reels" / "ambient30.wav", d / "assets" / "ambient.wav")
(d / "index.html").write_text(page(DUR, body, js, "voix.wav").replace("</style>", EXTRA + "</style>", 1).replace("Lien en bio ↓", "guidpilot.fr").replace('<div class="center" style="top:220px"><img id="cl"', '<div class="center" style="top:300px"><img id="cl"').replace('<div class="center" style="top:520px"><div class="offer"', '<div class="center" style="top:600px"><div class="offer"'))
print("ok", d)
