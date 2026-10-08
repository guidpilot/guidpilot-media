"""Short / Reel : « 3 choses que vos clientes regardent avant de réserver » (voix ElevenLabs Claire)."""
import pathlib, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import importlib.util
spec = importlib.util.spec_from_file_location("gr", pathlib.Path(__file__).parent / "gen_reels.py")
# On réutilise CSS / frame / cta / page sans relancer la génération des autres Reels
src = (pathlib.Path(__file__).parent / "gen_reels.py").read_text().split("# ---------- Reel 1")[0]
ns = {"__file__": str(pathlib.Path(__file__).parent / "gen_reels.py")}
exec(src, ns)
CSS, frame, cta, cta_js, page, BASE, SRC = ns["CSS"], ns["frame"], ns["cta"], ns["cta_js"], ns["page"], ns["BASE"], ns["SRC"]

EXTRA_CSS = """
.num{display:inline-flex;align-items:center;justify-content:center;width:150px;height:150px;border-radius:50%;background:#2563EB;color:#fff;font-weight:800;font-size:92px}
.rating{display:inline-block;margin-top:56px;padding:26px 48px;border-radius:999px;background:#FBF3DC;color:#6B4E16;font-weight:800;font-size:58px}
.mini{margin-top:40px;font-weight:600;font-size:44px;color:#475569;width:900px;line-height:1.35}
.timer{display:inline-block;margin-top:50px;padding:22px 44px;border-radius:999px;background:#DCFCE7;color:#166534;font-weight:800;font-size:52px}
"""

DUR = 27.6
body = f'''
<div id="a" class="clip navy" data-start="0" data-duration="3.5" data-track-index="1">
  <div class="center" style="top:560px"><div class="kicker" id="ak" style="font-size:40px">TAROLOGUES · PRATICIENNES</div>
  <div class="big" id="a1" style="margin-top:40px">Avant de réserver, vos clientes regardent <span>3 choses</span></div></div>
</div>
<div id="b" class="clip light" data-start="3.5" data-duration="5.2" data-track-index="1">
  <div class="center" style="top:150px"><div class="num" id="bn">1</div><div class="stitle" id="bt" style="margin-top:30px">Votre <span>page</span></div></div>
  {frame("bf","page.png",960,980,560)}
</div>
<div id="c" class="clip light" data-start="8.7" data-duration="3.8" data-track-index="1">
  <div class="center" style="top:150px"><div class="num" id="cn">2</div><div class="stitle" id="ct" style="margin-top:30px">Vos <span>avis</span></div></div>
  {frame("cf","avis.png",960,250,640)}
  <div class="center" style="top:1150px"><div class="rating" id="cr">★ Ce qui rassure le plus</div></div>
</div>
<div id="d" class="clip light" data-start="12.5" data-duration="4.3" data-track-index="1">
  <div class="center" style="top:150px"><div class="num" id="dn">3</div><div class="stitle" id="dt" style="margin-top:30px">La <span>simplicité</span></div></div>
  <div class="center" style="top:760px">
    <div class="pill" id="p1"><i>✓</i>Elle choisit un créneau</div>
    <div class="pill" id="p2"><i>✓</i>Elle paie en ligne</div>
    <div class="pill" id="p3"><i>✓</i>C'est confirmé</div>
    <div class="timer" id="pt">En 2 minutes</div>
  </div>
</div>
<div id="e" class="clip navy" data-start="16.8" data-duration="2.7" data-track-index="1">
  <div class="center" style="top:560px"><img id="el" src="assets/logo_blanc.png" alt="GuidPilot" style="width:640px;display:block" />
  <div class="big" id="e1" style="margin-top:70px">Les 3, <span>dans un seul espace</span></div></div>
</div>
{cta(19.5, DUR - 19.5)}'''

js = '''
tl.fromTo("#ak",{opacity:0,y:30},{opacity:1,y:0,duration:.4,ease:E},.05);
tl.fromTo("#a1",{opacity:0,y:60},{opacity:1,y:0,duration:.6,ease:E},.25);
tl.fromTo("#bn",{opacity:0,scale:.4},{opacity:1,scale:1,duration:.45,ease:"back.out(2)"},3.55);
tl.fromTo("#bt",{opacity:0,y:40},{opacity:1,y:0,duration:.45,ease:E},3.7);
tl.fromTo("#bf",{opacity:0,y:160,scale:.92},{opacity:1,y:0,scale:1,duration:.6,ease:E},4.0);
tl.fromTo("#bfi",{y:0},{y:-60,duration:4.2,ease:"sine.inOut"},4.5);
tl.fromTo("#cn",{opacity:0,scale:.4},{opacity:1,scale:1,duration:.45,ease:"back.out(2)"},8.75);
tl.fromTo("#ct",{opacity:0,y:40},{opacity:1,y:0,duration:.45,ease:E},8.9);
tl.fromTo("#cf",{opacity:0,y:120,scale:.92},{opacity:1,y:0,scale:1,duration:.6,ease:E},9.1);
tl.fromTo("#cr",{opacity:0,y:40,scale:.9},{opacity:1,y:0,scale:1,duration:.5,ease:"back.out(2)"},10.6);
tl.fromTo("#dn",{opacity:0,scale:.4},{opacity:1,scale:1,duration:.45,ease:"back.out(2)"},12.55);
tl.fromTo("#dt",{opacity:0,y:40},{opacity:1,y:0,duration:.45,ease:E},12.7);
["#p1","#p2","#p3"].forEach((p,i)=>tl.fromTo(p,{opacity:0,x:-80},{opacity:1,x:0,duration:.4,ease:"back.out(1.6)"},[14.1,14.85,15.6][i]));
tl.fromTo("#pt",{opacity:0,scale:.7},{opacity:1,scale:1,duration:.45,ease:"back.out(2)"},16.1);
tl.fromTo("#el",{opacity:0,scale:.7},{opacity:1,scale:1,duration:.6,ease:"back.out(1.5)"},16.85);
tl.fromTo("#e1",{opacity:0,y:50},{opacity:1,y:0,duration:.5,ease:E},17.6);
''' + cta_js(19.5, 23.15, 24.3)

CTA_LABEL = sys.argv[2] if len(sys.argv) > 2 else "guidpilot.fr"
name = "s1-3-choses"
d = BASE / "build" / name
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(SRC / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(SRC / f, d / f)
for a in ("logo_blanc.png", "page.png", "avis.png"): shutil.copy(SRC / "assets" / a, d / "assets" / a)
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
shutil.copy(BASE / "reels" / "ambient30.wav", d / "assets" / "ambient.wav")
html = page(DUR, body, js, "voix.wav").replace("Lien en bio ↓", CTA_LABEL).replace("</style>", EXTRA_CSS + "</style>", 1)
(d / "index.html").write_text(html)
print("ok", d)
