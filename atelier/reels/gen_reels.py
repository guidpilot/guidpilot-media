"""Génère deux Reels sans voix (9:16) au style GuidPilot : r1-pov et r2-avant-apres."""
import pathlib, shutil

BASE = pathlib.Path(__file__).resolve().parent.parent  # dossier atelier/
SRC = BASE / "kit"
VOIX = BASE.parent / "voix"  # dossier voix/ du dépôt

CSS = """
@font-face{font-family:"Inter";src:url("fonts/inter-latin-400-normal.woff2") format("woff2");font-weight:400}
@font-face{font-family:"Inter";src:url("fonts/inter-latin-600-normal.woff2") format("woff2");font-weight:600}
@font-face{font-family:"Inter";src:url("fonts/inter-latin-700-normal.woff2") format("woff2");font-weight:700}
@font-face{font-family:"Inter";src:url("fonts/inter-latin-800-normal.woff2") format("woff2");font-weight:800}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#0F172A}
#root{position:relative;width:100%;height:100%;overflow:hidden;font-family:"Inter",sans-serif;color:#0F172A}
.clip{position:absolute;inset:0}
.navy{background:#0F172A}.light{background:#F6F8FC}
.center{position:absolute;left:0;right:0;display:flex;flex-direction:column;align-items:center;text-align:center}
.kicker{font-weight:800;font-size:56px;letter-spacing:.16em;color:#E9C46A}
.big{font-weight:800;font-size:104px;line-height:1.06;color:#fff;letter-spacing:-.02em;width:920px}
.big span{color:#60A5FA}
.stitle{font-weight:800;font-size:84px;line-height:1.08;letter-spacing:-.02em;width:920px}
.stitle span{color:#2563EB}
.frame{position:absolute;left:60px;width:960px;background:#fff;border-radius:28px;overflow:hidden;border:2px solid #E2E8F0}
.bar{height:56px;background:#F1F5F9;border-bottom:2px solid #E2E8F0;display:flex;align-items:center;padding-left:24px;gap:12px}
.dot{width:16px;height:16px;border-radius:50%;background:#CBD5E1}
.demo{position:absolute;right:24px;top:12px;font-size:22px;font-weight:600;color:#64748B;background:#fff;border:2px solid #E2E8F0;border-radius:999px;padding:4px 16px}
.vp{position:relative;overflow:hidden}
.shot{position:absolute;left:0;top:0;display:block;max-width:none}
.pill{margin:16px 0;padding:28px 44px;border-radius:24px;background:#0F172A;color:#fff;font-weight:700;font-size:46px;white-space:nowrap}
.pill i{font-style:normal;color:#4ADE80;margin-right:18px}
.chip{position:absolute;padding:26px 42px;border-radius:999px;background:#1E293B;border:2px solid #334155;color:#E2E8F0;font-weight:600;font-size:46px;white-space:nowrap}
.check{display:flex;align-items:center;gap:24px;text-align:left;font-weight:700;font-size:54px;color:#0F172A;margin:22px 0;width:840px}
.check i{font-style:normal;flex:none;width:76px;height:76px;border-radius:50%;background:#DCFCE7;color:#16A34A;display:flex;align-items:center;justify-content:center;font-size:44px}
.offer{display:inline-block;background:#FBF3DC;color:#6B4E16;font-weight:700;font-size:38px;padding:16px 36px;border-radius:999px}
.big14{font-weight:800;font-size:200px;line-height:.95;color:#fff;letter-spacing:-.04em;margin-top:40px}
.big14 small{display:block;font-size:92px;margin-top:12px}
.nocard{margin-top:44px;font-weight:700;font-size:62px;color:#4ADE80}
.bio{margin-top:60px;display:inline-block;background:#2563EB;color:#fff;font-weight:800;font-size:58px;padding:30px 60px;border-radius:999px}
.red{color:#F87171}
.aibadge{position:absolute;left:40px;top:64px;z-index:50;padding:12px 24px;border-radius:999px;background:rgba(15,23,42,.72);color:#E2E8F0;font-weight:600;font-size:28px;border:1px solid rgba(255,255,255,.25)}
"""

def frame(id_, img, w, h, top, label="Compte de démonstration"):
    return f'''<div class="frame" id="{id_}" style="top:{top}px"><div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="demo">{label}</span></div><div class="vp" style="height:{h}px"><img class="shot" id="{id_}i" src="assets/{img}" alt="" style="width:{w}px" /></div></div>'''

def cta(start, dur):
    return f'''<div id="cta" class="clip navy" data-start="{start}" data-duration="{dur}" data-track-index="1">
  <div class="center" style="top:220px"><img id="cl" src="assets/logo_blanc.png" alt="GuidPilot" style="width:520px;display:block" /></div>
  <div class="center" style="top:520px"><div class="offer" id="co">Essai gratuit</div><div class="big14" id="cb">14 jours<small>gratuits</small></div><div class="nocard" id="cn">✓ Sans carte bancaire</div><div class="bio" id="cbio">Lien en bio ↓</div></div>
</div>'''

def cta_js(t, nc=None, bio=None):
    nc = t+1.0 if nc is None else nc
    bio = t+1.5 if bio is None else bio
    return f'''tl.fromTo("#cl",{{opacity:0,y:-30}},{{opacity:1,y:0,duration:.5,ease:E}},{t+.05});
tl.fromTo("#co",{{opacity:0,y:20}},{{opacity:1,y:0,duration:.4,ease:E}},{t+.2});
tl.fromTo("#cb",{{opacity:0,scale:.7}},{{opacity:1,scale:1,duration:.6,ease:"back.out(1.7)"}},{t+.35});
tl.fromTo("#cn",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45,ease:E}},{nc});
tl.fromTo("#cbio",{{opacity:0,y:40,scale:.9}},{{opacity:1,y:0,scale:1,duration:.5,ease:"back.out(2)"}},{bio});
tl.to("#cbio",{{scale:1.06,duration:.45,yoyo:true,repeat:3,ease:"sine.inOut"}},{bio+.6});'''

def page(dur, body, js, voice):
    return f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<script src="vendor/gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{dur}" data-width="1080" data-height="1920">
<div class="aibadge">Voix off générée par IA</div>
<audio id="voix" src="assets/{voice}" data-start="0" data-duration="{dur}" data-volume="1"></audio>
<audio id="musique" src="assets/ambient.wav" data-start="0" data-duration="{dur}" data-volume="0.06"></audio>
{body}
</div>
<script>
const tl=gsap.timeline({{paused:true}}); const E="power3.out";
{js}
window.__timelines["main"]=tl;
</script></body></html>'''

# ---------- Reel 1 : POV réservation à 23 h ----------
r1_body = f'''
<div id="a" class="clip navy" data-start="0" data-duration="5.0" data-track-index="1">
  <div class="center" style="top:620px"><div class="kicker" id="ak">POV</div>
  <div class="big" id="a1" style="margin-top:36px">Une cliente réserve votre tirage <span>à 23 h…</span></div>
  <div class="big" id="a2" style="margin-top:40px;color:#E9C46A">…et vous dormez.</div></div>
</div>
<div id="b" class="clip light" data-start="5.0" data-duration="3.8" data-track-index="1">
  <div class="center" style="top:170px"><div class="stitle" id="bt">Elle choisit sa séance <span>sur votre page</span></div></div>
  {frame("bf","page.png",1200,820,520)}
</div>
<div id="c" class="clip light" data-start="8.8" data-duration="8.8" data-track-index="1">
  <div class="center" style="top:170px"><div class="stitle" id="ct">Pendant ce temps, <span>GuidPilot s'occupe de tout</span></div></div>
  <div class="center" style="top:620px">
    <div class="pill" id="p1"><i>✓</i>Paiement reçu</div>
    <div class="pill" id="p2"><i>✓</i>Rendez-vous dans l'agenda</div>
    <div class="pill" id="p3"><i>✓</i>Facture créée</div>
    <div class="pill" id="p4"><i>✓</i>Confirmation envoyée</div>
  </div>
</div>
<div id="d" class="clip navy" data-start="17.6" data-duration="2.7" data-track-index="1">
  <div class="center" style="top:760px"><div class="big" id="d1">Le matin, <span>tout est prêt.</span></div></div>
</div>
{cta(20.3, 8.0)}'''
r1_js = '''
tl.fromTo("#ak",{opacity:0,y:30},{opacity:1,y:0,duration:.4,ease:E},.1);
tl.fromTo("#a1",{opacity:0,y:60},{opacity:1,y:0,duration:.6,ease:E},.35);
tl.fromTo("#a2",{opacity:0,scale:.85},{opacity:1,scale:1,duration:.5,ease:"back.out(1.8)"},3.9);
tl.fromTo("#bt",{opacity:0,y:40},{opacity:1,y:0,duration:.45,ease:E},5.05);
tl.fromTo("#bf",{opacity:0,y:160,scale:.92},{opacity:1,y:0,scale:1,duration:.6,ease:E},5.2);
tl.fromTo("#bfi",{x:0},{x:-240,duration:3.2,ease:"sine.inOut"},5.5);
tl.fromTo("#ct",{opacity:0,y:40},{opacity:1,y:0,duration:.45,ease:E},8.9);
["#p1","#p2","#p3","#p4"].forEach((p,i)=>tl.fromTo(p,{opacity:0,x:-80},{opacity:1,x:0,duration:.45,ease:"back.out(1.6)"},[12.0,13.25,14.65,16.25][i]));
tl.fromTo("#d1",{opacity:0,scale:.85},{opacity:1,scale:1,duration:.6,ease:"back.out(1.6)"},17.85);
''' + cta_js(20.3, 23.8, 25.3)

# ---------- Reel 2 : Avant / Après ----------
chips = [("Carnet papier",40,0),("WhatsApp",520,30),("PayPal",90,170),("Tableur clients",460,200),("E-mails",160,340),("Agenda papier",520,370)]
chips_html = "".join(f'<div class="chip" id="k{i}" style="left:{x}px;top:{y}px">{t}</div>' for i,(t,x,y) in enumerate(chips))
r2_body = f'''
<div id="a" class="clip navy" data-start="0" data-duration="8.6" data-track-index="1">
  <div class="center" style="top:300px"><div class="kicker red" id="ak">AVANT</div>
  <div class="big" id="a1" style="margin-top:30px">Votre activité, <span>éparpillée partout</span></div></div>
  <div style="position:absolute;left:60px;right:60px;top:880px;height:520px">{chips_html}</div>
</div>
<div id="b" class="clip navy" data-start="8.6" data-duration="2.0" data-track-index="1">
  <div class="center" style="top:640px"><div class="kicker" id="bk">APRÈS</div>
  <img id="bl" src="assets/logo_blanc.png" alt="GuidPilot" style="width:820px;display:block;margin-top:60px" /></div>
</div>
<div id="c" class="clip light" data-start="10.6" data-duration="2.9" data-track-index="1">
  <div class="center" style="top:170px"><div class="stitle" id="ct">Tout votre cabinet <span>dans un seul espace</span></div></div>
  {frame("cf","dash.png",1440,820,520)}
</div>
<div id="d" class="clip light" data-start="13.5" data-duration="8.3" data-track-index="1">
  <div class="center" style="top:430px">
    <div class="check" id="q1"><i>✓</i>Réservation en ligne</div>
    <div class="check" id="q2"><i>✓</i>Paiement sécurisé</div>
    <div class="check" id="q3"><i>✓</i>Guidances écrites et vocales</div>
    <div class="check" id="q4"><i>✓</i>Factures automatiques</div>
    <div class="check" id="q5"><i>✓</i>Avis clients</div>
  </div>
</div>
{cta(21.8, 7.7)}'''
r2_js = '''
tl.fromTo("#ak",{opacity:0,y:30},{opacity:1,y:0,duration:.4,ease:E},.1);
tl.fromTo("#a1",{opacity:0,y:60},{opacity:1,y:0,duration:.6,ease:E},.3);
''' + "".join(f'tl.fromTo("#k{i}",{{opacity:0,y:-90,scale:.6,rotation:{8 if i%2 else -8}}},{{opacity:1,y:0,scale:1,rotation:{-4 if i%2 else 4},duration:.4,ease:"back.out(2)"}},{0.9+i*0.75:.2f});\n' for i in range(6)) + '''
tl.to(["#k0","#k1","#k2","#k3","#k4","#k5"],{x:6,duration:.08,yoyo:true,repeat:7,ease:"none"},5.8);
tl.fromTo("#bk",{opacity:0,y:30},{opacity:1,y:0,duration:.4,ease:E},8.75);
tl.fromTo("#bl",{opacity:0,scale:.7},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},9.5);
tl.fromTo("#ct",{opacity:0,y:40},{opacity:1,y:0,duration:.45,ease:E},10.65);
tl.fromTo("#cf",{opacity:0,y:160,scale:.92},{opacity:1,y:0,scale:1,duration:.6,ease:E},10.8);
tl.fromTo("#cfi",{x:0,y:0},{x:-480,y:-150,duration:2.5,ease:"sine.inOut"},11.0);
''' + "".join(f'tl.fromTo("#q{i}",{{opacity:0,x:-60}},{{opacity:1,x:0,duration:.4,ease:"back.out(1.6)"}},{[0,13.6,15.35,16.85,18.85,20.55][i]:.2f});\n' for i in range(1,6)) + cta_js(21.8, 25.35, 26.6)

for name, dur, body, js, voice in [("r1-pov", 28.3, r1_body, r1_js, "voix_pov.wav"), ("r2-avant-apres", 29.5, r2_body, r2_js, "voix_avant_apres.wav")]:
    d = BASE / "build" / name
    if d.exists(): shutil.rmtree(d)
    (d / "assets").mkdir(parents=True)
    for sub in ("fonts", "vendor"): shutil.copytree(SRC / sub, d / sub)
    for f in ("hyperframes.json", "meta.json"): shutil.copy(SRC / f, d / f)
    for a in ("logo_blanc.png", "page.png", "dash.png"): shutil.copy(SRC / "assets" / a, d / "assets" / a)
    shutil.copy(str(VOIX) + "/" + {"voix_pov.wav":"2026-10-09_pov-23h.wav","voix_avant_apres.wav":"2026-10-11_avant-apres.wav"}[voice], d / "assets" / voice)
    shutil.copy(BASE / "reels" / "ambient30.wav", d / "assets" / "ambient.wav")
    (d / "index.html").write_text(page(dur, body, js, voice))
    print("ok", name)
