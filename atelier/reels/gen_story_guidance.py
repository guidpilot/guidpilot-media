"""Story Instagram (9:16, 16 s) : « Votre guidance vocale mérite mieux qu'un message WhatsApp » — voix Claire."""
import pathlib, shutil, sys
HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_reels.py").read_text().split("# ---------- Reel 1")[0]
ns = {"__file__": str(HERE / "gen_reels.py")}
exec(src, ns)
frame, page, BASE, SRC = ns["frame"], ns["page"], ns["BASE"], ns["SRC"]

EXTRA = """
.bub{position:absolute;padding:28px 40px;border-radius:36px;font-weight:600;font-size:44px;white-space:nowrap}
.bub.in{left:90px;background:#1E293B;color:#E2E8F0;border-bottom-left-radius:8px}
.bub.out{right:90px;background:#14532D;color:#DCFCE7;border-bottom-right-radius:8px}
.lost{position:absolute;left:0;right:0;text-align:center;font-weight:800;font-size:64px;color:#F87171}
.badge2{display:inline-block;margin-top:40px;padding:22px 44px;border-radius:999px;background:#DCFCE7;color:#166534;font-weight:800;font-size:48px}
"""
DUR = 16.0
bubs = [("in", "Coucou ! Tu as vu mon message ?", 640), ("out", "▶ Message vocal · 4:12", 780), ("in", "Photo · Vacances", 920), ("in", "On se voit samedi ?", 1060), ("out", "▶ Message vocal · 0:47", 1200)]
bub_html = "".join(f'<div class="bub {c}" id="u{i}" style="top:{y}px">{t}</div>' for i, (c, t, y) in enumerate(bubs))
body = f'''
<div id="a" class="clip navy" data-start="0" data-duration="3.6" data-track-index="1">
  <div class="center" style="top:320px"><div class="big" id="a1" style="font-size:84px">Votre guidance vocale… <span>perdue dans WhatsApp ?</span></div></div>
  {bub_html}
  <div class="lost" id="al" style="top:1420px">Introuvable 3 semaines après</div>
</div>
<div id="b" class="clip light" data-start="3.6" data-duration="7.1" data-track-index="1">
  <div class="center" style="top:330px"><div class="stitle" id="bt">Livrée dans <span>l'espace client sécurisé</span></div></div>
  {frame("bf","guid.png",960,430,640)}
  <div class="center" style="top:1220px"><div class="badge2" id="bb">✓ Retrouvée quand elle veut</div></div>
</div>
<div id="cta" class="clip navy" data-start="10.7" data-duration="{DUR-10.7}" data-track-index="1">
  <div class="center" style="top:260px"><img id="cl" src="assets/logo_blanc.png" alt="GuidPilot" style="width:560px;display:block" /></div>
  <div class="center" style="top:560px"><div class="offer" id="co">Essai gratuit</div><div class="big14" id="cb">14 jours<small>gratuits</small></div><div class="nocard" id="cn">✓ Sans carte bancaire</div><div class="bio" id="cbio">guidpilot.fr</div></div>
</div>'''
js = '''
tl.fromTo("#a1",{opacity:0,y:50},{opacity:1,y:0,duration:.5,ease:E},.1);
''' + "".join(f'tl.fromTo("#u{i}",{{opacity:0,y:30,scale:.9}},{{opacity:1,y:0,scale:1,duration:.3,ease:"back.out(2)"}},{0.5+i*0.35:.2f});\n' for i in range(5)) + '''
tl.fromTo("#al",{opacity:0,scale:.8},{opacity:1,scale:1,duration:.4,ease:"back.out(2)"},2.5);
tl.fromTo("#bt",{opacity:0,y:40},{opacity:1,y:0,duration:.45,ease:E},3.65);
tl.fromTo("#bf",{opacity:0,y:140,scale:.92},{opacity:1,y:0,scale:1,duration:.6,ease:E},3.8);
tl.fromTo("#bb",{opacity:0,y:40,scale:.9},{opacity:1,y:0,scale:1,duration:.5,ease:"back.out(2)"},7.9);
tl.fromTo("#cl",{opacity:0,y:-30},{opacity:1,y:0,duration:.5,ease:E},10.75);
tl.fromTo("#co",{opacity:0,y:20},{opacity:1,y:0,duration:.4,ease:E},10.9);
tl.fromTo("#cb",{opacity:0,scale:.7},{opacity:1,scale:1,duration:.6,ease:"back.out(1.7)"},11.05);
tl.fromTo("#cn",{opacity:0,y:30},{opacity:1,y:0,duration:.45,ease:E},12.9);
tl.fromTo("#cbio",{opacity:0,y:40,scale:.9},{opacity:1,y:0,scale:1,duration:.5,ease:"back.out(2)"},13.6);
'''
d = BASE / "build" / "story-guidance"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(SRC / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(SRC / f, d / f)
for a in ("logo_blanc.png", "guid.png"): shutil.copy(SRC / "assets" / a, d / "assets" / a)
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
shutil.copy(BASE / "reels" / "ambient30.wav", d / "assets" / "ambient.wav")
(d / "index.html").write_text(page(DUR, body, js, "voix.wav").replace("</style>", EXTRA + ".aibadge{top:180px !important}</style>", 1))
print("ok", d)
