"""Vidéo YouTube horizontale (1920x1080) : présentation complète de GuidPilot, voix ElevenLabs Claire.
Usage : python3 gen_presentation.py <voix.wav>   -> build/yt-presentation/
Modèle réutilisable pour les vidéos longues : sections = (début, fin, numéro, titre, contenu).
"""
import pathlib, shutil, subprocess, sys

ATELIER = pathlib.Path(__file__).resolve().parent.parent
KIT = ATELIER / "kit"
DUR = 99.5

CSS = """
@font-face{font-family:"Inter";src:url("fonts/inter-latin-400-normal.woff2") format("woff2");font-weight:400}
@font-face{font-family:"Inter";src:url("fonts/inter-latin-600-normal.woff2") format("woff2");font-weight:600}
@font-face{font-family:"Inter";src:url("fonts/inter-latin-700-normal.woff2") format("woff2");font-weight:700}
@font-face{font-family:"Inter";src:url("fonts/inter-latin-800-normal.woff2") format("woff2");font-weight:800}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1920px;height:1080px;overflow:hidden;background:#0F172A}
#root{position:relative;width:100%;height:100%;overflow:hidden;font-family:"Inter",sans-serif;color:#0F172A}
.clip{position:absolute;inset:0}
.navy{background:#0F172A;color:#fff}.light{background:#F6F8FC}
.aibadge{position:absolute;left:36px;top:30px;z-index:50;padding:10px 22px;border-radius:999px;background:rgba(15,23,42,.72);color:#E2E8F0;font-weight:600;font-size:22px;border:1px solid rgba(255,255,255,.25)}
.logo-corner{position:absolute;right:48px;top:34px;height:46px;z-index:40}
.col{position:absolute;left:110px;top:0;bottom:0;width:640px;display:flex;flex-direction:column;justify-content:center}
.chap{display:inline-flex;align-items:center;gap:18px;font-weight:700;font-size:28px;letter-spacing:.12em;text-transform:uppercase;color:#2563EB}
.chap b{display:inline-flex;align-items:center;justify-content:center;width:58px;height:58px;border-radius:50%;background:#2563EB;color:#fff;font-size:30px;letter-spacing:0}
.h{font-weight:800;font-size:68px;line-height:1.08;letter-spacing:-.02em;margin-top:26px}
.h span{color:#2563EB}
.p{font-weight:500;font-size:32px;line-height:1.45;color:#475569;margin-top:26px}
.pill{display:inline-flex;align-items:center;gap:16px;margin-top:18px;padding:18px 30px;border-radius:18px;background:#0F172A;color:#fff;font-weight:700;font-size:32px;align-self:flex-start}
.pill i{font-style:normal;color:#4ADE80}
.tag{display:inline-block;margin-top:30px;padding:14px 28px;border-radius:999px;background:#FBF3DC;color:#6B4E16;font-weight:700;font-size:28px;align-self:flex-start}
.frame{position:absolute;left:820px;width:1000px;background:#fff;border-radius:22px;overflow:hidden;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.bar{height:46px;background:#F1F5F9;border-bottom:2px solid #E2E8F0;display:flex;align-items:center;padding-left:20px;gap:10px}
.dot{width:13px;height:13px;border-radius:50%;background:#CBD5E1}
.demo{position:absolute;right:18px;top:9px;font-size:18px;font-weight:600;color:#64748B;background:#fff;border:2px solid #E2E8F0;border-radius:999px;padding:3px 14px}
.vp{position:relative;overflow:hidden}
.shot{position:absolute;left:0;top:0;display:block;max-width:none}
.center{position:absolute;left:0;right:0;display:flex;flex-direction:column;align-items:center;text-align:center}
.big{font-weight:800;font-size:84px;line-height:1.08;letter-spacing:-.02em;width:1500px}
.big span{color:#60A5FA}
.chip{position:absolute;padding:20px 36px;border-radius:999px;background:#1E293B;border:2px solid #334155;color:#E2E8F0;font-weight:600;font-size:38px;white-space:nowrap}
.stat{font-weight:800;font-size:150px;line-height:1;color:#2563EB;letter-spacing:-.04em;margin-top:30px}
.check{display:flex;align-items:center;gap:20px;font-weight:700;font-size:40px;color:#fff;margin:12px 0}
.check i{font-style:normal;flex:none;width:56px;height:56px;border-radius:50%;background:#14532D;color:#4ADE80;display:flex;align-items:center;justify-content:center;font-size:30px}
.offer{display:inline-block;background:#FBF3DC;color:#6B4E16;font-weight:700;font-size:30px;padding:12px 30px;border-radius:999px}
.big14{font-weight:800;font-size:120px;line-height:1;color:#fff;letter-spacing:-.03em;margin-top:24px}
.nocard{margin-top:20px;font-weight:700;font-size:42px;color:#4ADE80}
.url{margin-top:34px;display:inline-block;background:#2563EB;color:#fff;font-weight:800;font-size:48px;padding:22px 54px;border-radius:999px}
.sub{display:inline-flex;align-items:center;gap:18px;margin-top:34px;padding:22px 44px;border-radius:999px;background:#fff;color:#0F172A;font-weight:800;font-size:40px}
.sub i{font-style:normal;display:inline-block;width:22px;height:22px;border-radius:50%;background:#DC2626}
"""

def frame(id_, img, w, h, top):
    return (f'<div class="frame" id="{id_}" style="top:{top}px"><div class="bar"><span class="dot"></span><span class="dot"></span>'
            f'<span class="dot"></span><span class="demo">Compte de démonstration</span></div>'
            f'<div class="vp" style="height:{h}px"><img class="shot" id="{id_}i" src="assets/{img}" alt="" style="width:{w}px" /></div></div>')

def section(id_, start, end, num, chap, title, inner_left, right=""):
    return (f'<div id="{id_}" class="clip light" data-start="{start}" data-duration="{round(end-start,2)}" data-track-index="1">'
            f'<img class="logo-corner" src="assets/logo_couleur.png" alt="GuidPilot" />'
            f'<div class="col"><div class="chap" id="{id_}c"><b>{num}</b>{chap}</div><div class="h" id="{id_}h">{title}</div>{inner_left}</div>{right}</div>')

T = dict(p2=20.4, p3=35.2, p4=49.2, p5=59.4, p6=70.75, p7=78.8)
chips = [("Messages",120,0),("Virements",760,40),("Factures à la main",1180,0),("WhatsApp",300,170),("Carnet papier",900,200)]
chips_html = "".join(f'<div class="chip" id="k{i}" style="left:{x}px;top:{y}px">{t}</div>' for i,(t,x,y) in enumerate(chips))

body = f'''
<div id="a" class="clip navy" data-start="0" data-duration="{T['p2']}" data-track-index="1">
  <div class="center" style="top:170px"><div class="big" id="a1">Tarologue, voyante, médium, <span>praticienne en guidance ?</span></div></div>
  <div style="position:absolute;left:110px;right:110px;top:520px;height:320px">{chips_html}</div>
  <div class="center" id="a3" style="top:300px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:620px;display:block" />
    <div class="big" style="margin-top:50px;font-size:72px">Tout votre cabinet <span>dans un seul espace</span></div></div>
</div>
{section("b", T['p2'], T['p3'], 1, "Votre vitrine", "Votre <span>page praticien</span>",
  '<div class="p" id="bp">Activité, prestations, tarifs et avis : tout est présenté au même endroit.</div>'
  '<div class="pill" id="b1"><i>✓</i>Visible dans l\'annuaire GuidPilot</div>'
  '<div class="pill" id="b2"><i>✓</i>Un simple lien pour votre bio</div>',
  frame("bf","page.png",1000,760,150) + frame("bg","annuaire.png",1000,430,300))}
{section("c", T['p3'], T['p4'], 2, "Réservation", "Réservation et <span>paiement en ligne</span>",
  '<div class="pill" id="c1"><i>1</i>La cliente choisit sa séance</div>'
  '<div class="pill" id="c2"><i>2</i>Elle choisit un créneau libre</div>'
  '<div class="pill" id="c3"><i>3</i>Elle paie en ligne</div>'
  '<div class="tag" id="c4">Visio : le lien Google Meet est prêt</div>',
  frame("cf","dash.png",1000,760,150))}
{section("d", T['p4'], T['p5'], 3, "Guidances", "Guidances <span>écrites et vocales</span>",
  '<div class="p" id="dp">Livrées dans l\'espace client sécurisé de votre cliente, avec vos échanges et ses documents.</div>'
  '<div class="tag" id="d1">Espace client sécurisé</div>',
  frame("df","guid.png",1000,442,280))}
{section("e", T['p5'], T['p6'], 4, "Gestion", "Factures <span>automatiques</span>",
  '<div class="p" id="ep">Chaque paiement génère sa facture. Revenus et règlements sont suivis sur votre tableau de bord.</div>',
  frame("ef","finance.png",1000,189,240) +
  '<div id="eb" style="position:absolute;left:820px;width:1000px;top:520px;text-align:center">'
  '<div class="stat">0 %</div><div style="font-weight:800;font-size:46px;margin-top:10px">de commission sur vos séances</div>'
  '<div style="font-weight:500;font-size:26px;color:#64748B;margin-top:12px">hors frais du moyen de paiement</div></div>')}
{section("f", T['p6'], T['p7'], 5, "Réputation", "Avis clients <span>en un clic</span>",
  '<div class="p" id="fp">Après la séance, la demande d\'avis part en un clic. Les avis publiés s\'affichent sur votre page.</div>',
  frame("ff","avis.png",1000,260,400))}
<div id="g" class="clip navy" data-start="{T['p7']}" data-duration="{round(DUR-T['p7'],2)}" data-track-index="1">
  <div id="g0" style="position:absolute;left:0;right:0;top:0;bottom:0">
    <div class="center" style="top:120px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:420px;display:block" /></div>
    <div style="position:absolute;left:560px;top:330px">
      <div class="check" id="g1"><i>✓</i>Réservation et paiement</div>
      <div class="check" id="g2"><i>✓</i>Agenda</div>
      <div class="check" id="g3"><i>✓</i>Guidances écrites et vocales</div>
      <div class="check" id="g4"><i>✓</i>Factures automatiques</div>
      <div class="check" id="g5"><i>✓</i>Avis clients</div>
    </div>
  </div>
  <div class="center" id="g6" style="top:150px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="offer" style="margin-top:46px">Essai gratuit</div>
    <div class="big14">14 jours gratuits</div>
    <div class="nocard" id="g7">✓ Sans carte bancaire</div>
    <div class="url" id="g8">guidpilot.fr</div>
    <div class="sub" id="g9"><i></i>Abonnez-vous : une vidéo par jour</div>
  </div>
</div>'''

js = f'''
tl.fromTo("#a1",{{opacity:0,y:50}},{{opacity:1,y:0,duration:.6,ease:E}},.2);
''' + "".join(f'tl.fromTo("#k{i}",{{opacity:0,y:-60,scale:.7}},{{opacity:1,y:0,scale:1,duration:.45,ease:"back.out(2)"}},{t});\n' for i,t in enumerate([4.0,5.6,7.3,9.9,11.4])) + f'''
tl.to(["#a1","#k0","#k1","#k2","#k3","#k4"],{{opacity:0,y:-30,duration:.5,ease:"power2.in"}},15.0);
tl.fromTo("#a3",{{opacity:0,scale:.85}},{{opacity:1,scale:1,duration:.8,ease:"back.out(1.5)"}},15.6);
'''
def sec_in(i, t):
    return (f'tl.fromTo("#{i}c",{{opacity:0,x:-40}},{{opacity:1,x:0,duration:.45,ease:E}},{t+.1});\n'
            f'tl.fromTo("#{i}h",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.55,ease:E}},{t+.25});\n')
def pop(sel, t, ease="back.out(1.6)"):
    return f'tl.fromTo("{sel}",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45,ease:"{ease}"}},{t});\n'
def frame_in(sel, t):
    return f'tl.fromTo("{sel}",{{opacity:0,x:120,scale:.95}},{{opacity:1,x:0,scale:1,duration:.7,ease:E}},{t});\n'

js += sec_in("b", T['p2']) + pop("#bp", 22.9, "power3.out") + frame_in("#bf", 20.9)
js += 'tl.fromTo("#bfi",{y:0},{y:-200,duration:5,ease:"sine.inOut"},21.8);\n'
js += 'tl.to("#bf",{opacity:0,x:-80,duration:.5,ease:"power2.in"},26.4);\n' + frame_in("#bg", 26.8) + pop("#b1", 26.8) + pop("#b2", 30.3)
js += sec_in("c", T['p3']) + pop("#c1", 35.6) + pop("#c2", 37.4) + pop("#c3", 39.0) + frame_in("#cf", 41.5)
js += 'tl.fromTo("#cfi",{y:0},{y:-120,duration:4.5,ease:"sine.inOut"},42.5);\n' + pop("#c4", 46.7)
js += sec_in("d", T['p4']) + pop("#dp", 51.0, "power3.out") + frame_in("#df", 49.7) + pop("#d1", 52.0)
js += sec_in("e", T['p5']) + pop("#ep", 60.5, "power3.out") + frame_in("#ef", 59.9)
js += 'tl.fromTo("#eb",{opacity:0,scale:.7},{opacity:1,scale:1,duration:.7,ease:"back.out(1.7)"},67.2);\n'
js += sec_in("f", T['p6']) + pop("#fp", 72.1, "power3.out") + frame_in("#ff", 71.2)
js += "".join(pop(f"#g{i+1}", t) for i, t in enumerate([79.0, 79.8, 80.5, 81.4, 82.1]))
js += 'tl.to("#g0",{opacity:0,duration:.5,ease:"power2.in"},82.8);\n'
js += 'tl.fromTo("#g6",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},83.2);\n'
js += 'tl.set("#g7",{opacity:0},0);tl.set("#g8",{opacity:0},0);tl.set("#g9",{opacity:0},0);\n'
js += pop("#g7", 87.5) + pop("#g8", 88.5) + pop("#g9", 92.2)
js += 'tl.to("#g9",{scale:1.06,duration:.45,yoyo:true,repeat:5,ease:"sine.inOut"},93.0);\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1920" data-height="1080">
<div class="aibadge">Voix off générée par IA</div>
<audio id="voix" src="assets/voix.wav" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
<audio id="musique" src="assets/ambient.wav" data-start="0" data-duration="{DUR}" data-volume="0.05"></audio>
{body}
</div>
<script>
const tl=gsap.timeline({{paused:true}}); const E="power3.out";
tl.set("#a3",{{opacity:0}},0);
{js}
window.__timelines["main"]=tl;
</script></body></html>'''

d = ATELIER / "build" / "yt-presentation"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for a in ("page.png", "annuaire.png", "dash.png", "guid.png", "finance.png", "avis.png", "logo_blanc.png"): shutil.copy(KIT / "assets" / a, d / "assets" / a)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-stream_loop", "-1", "-i", str(ATELIER / "reels" / "ambient30.wav"),
                "-t", str(DUR + 1), "-af", f"afade=t=out:st={DUR-3}:d=3", str(d / "assets" / "ambient.wav")], check=True)
(d / "index.html").write_text(html)
print("ok", d)
