"""Reel + story « Concours de lancement » (9:16). Usage : python3 gen_concours.py <voix.wav> <reel|story> <durée> <t_steps> <t_s1> <t_s2> <t_s3> <t_fin> <t_bonne_chance>"""
import pathlib, shutil, sys
HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_reels.py").read_text().split("# ---------- Reel 1")[0]
ns = {"__file__": str(HERE / "gen_reels.py")}
exec(src, ns)
page, BASE, SRC = ns["page"], ns["BASE"], ns["SRC"]

voix, mode = sys.argv[1], sys.argv[2]
DUR, TS, T1, T2, T3, TF, TB = map(float, sys.argv[3:10])

EXTRA = """
.aibadge{top:180px !important}
.gold{font-weight:800;font-size:44px;letter-spacing:.14em;color:#E9C46A}
.prize{font-weight:800;font-size:150px;line-height:.95;color:#fff;letter-spacing:-.03em}
.prize small{display:block;font-size:84px;color:#60A5FA;margin-top:18px}
.plus{margin-top:50px;display:inline-block;padding:22px 44px;border-radius:999px;background:#FBF3DC;color:#6B4E16;font-weight:800;font-size:48px}
.st{display:flex;align-items:center;gap:30px;margin:26px 0;padding:34px 40px;width:920px;border-radius:30px;background:#fff;border:3px solid #E2E8F0;text-align:left;font-weight:800;font-size:52px;line-height:1.15;color:#0F172A}
.st b{flex:none;display:flex;align-items:center;justify-content:center;width:96px;height:96px;border-radius:50%;background:#2563EB;color:#fff;font-size:52px}
.st span{color:#2563EB}
.date{font-weight:800;font-size:66px;color:#fff;line-height:1.15}
.date span{color:#E9C46A}
.small{margin-top:40px;font-weight:600;font-size:32px;color:#94A3B8;line-height:1.45;width:900px}
.go{margin-top:50px;display:inline-block;background:#2563EB;color:#fff;font-weight:800;font-size:56px;padding:28px 60px;border-radius:999px}
"""
last = "Participez sur notre dernier post ↓" if mode == "story" else "Bonne chance !"
body = f'''
<div id="a" class="clip navy" data-start="0" data-duration="{TS}" data-track-index="1">
  <div class="center" style="top:330px"><div class="gold" id="ak">CONCOURS DE LANCEMENT</div></div>
  <div class="center" style="top:520px"><div class="prize" id="ap">1 an<small>de GuidPilot offert</small></div>
  <div class="plus" id="a2">+ 2 abonnements de 3 mois</div></div>
  <div class="center" style="top:1330px"><img id="al" src="assets/logo_blanc.png" alt="GuidPilot" style="width:440px;display:block" /></div>
</div>
<div id="b" class="clip light" data-start="{TS}" data-duration="{TF-TS}" data-track-index="1">
  <div class="center" style="top:330px"><div class="stitle" id="bt">Pour participer <span>c'est simple</span></div></div>
  <div class="center" style="top:640px">
    <div class="st" id="s1"><b>1</b><div>Abonnez-vous à <span>@guidpilot.fr</span></div></div>
    <div class="st" id="s2"><b>2</b><div>Aimez ce post</div></div>
    <div class="st" id="s3"><b>3</b><div>Commentez <span>« GuidPilot »</span> + votre spécialité</div></div>
  </div>
</div>
<div id="c" class="clip navy" data-start="{TF}" data-duration="{DUR-TF}" data-track-index="1">
  <div class="center" style="top:360px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:480px;display:block" id="cl" />
    <div class="date" id="cd" style="margin-top:80px">Jusqu'au <span>lundi 26 octobre</span><br/>à 23h59</div>
    <div class="date" id="ct" style="margin-top:30px;font-size:52px;color:#CBD5E1">Tirage au sort le 27 octobre</div>
    <div class="go" id="cg">{last}</div>
    <div class="small" id="cs">Réservé aux praticiens et praticiennes en activité, 18 ans et plus, résidant en France. Participation gratuite. Jeu ni organisé ni sponsorisé par Instagram.</div>
  </div>
</div>'''
js = f'''
tl.fromTo("#ak",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45,ease:E}},.1);
tl.fromTo("#ap",{{opacity:0,scale:.6}},{{opacity:1,scale:1,duration:.7,ease:"back.out(1.8)"}},.4);
tl.fromTo("#a2",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.5,ease:"back.out(2)"}},{max(TS-2.6,1.6)});
tl.fromTo("#al",{{opacity:0}},{{opacity:1,duration:.6}},1.0);
tl.fromTo("#bt",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.45,ease:E}},{TS+.05});
tl.fromTo("#s1",{{opacity:0,x:-80}},{{opacity:1,x:0,duration:.45,ease:"back.out(1.6)"}},{T1});
tl.fromTo("#s2",{{opacity:0,x:-80}},{{opacity:1,x:0,duration:.45,ease:"back.out(1.6)"}},{T2});
tl.fromTo("#s3",{{opacity:0,x:-80}},{{opacity:1,x:0,duration:.45,ease:"back.out(1.6)"}},{T3});
tl.fromTo("#cl",{{opacity:0,y:-30}},{{opacity:1,y:0,duration:.5,ease:E}},{TF+.05});
tl.fromTo("#cd",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.5,ease:E}},{TF+.2});
tl.fromTo("#ct",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.5,ease:E}},{TF+1.6});
tl.fromTo("#cg",{{opacity:0,scale:.8}},{{opacity:1,scale:1,duration:.5,ease:"back.out(2)"}},{TB});
tl.fromTo("#cs",{{opacity:0}},{{opacity:1,duration:.6}},{TF+.6});
'''
d = BASE / "build" / f"concours-{mode}"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(SRC / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(SRC / f, d / f)
shutil.copy(SRC / "assets" / "logo_blanc.png", d / "assets" / "logo_blanc.png")
shutil.copy(voix, d / "assets" / "voix.wav")
shutil.copy(BASE / "reels" / "ambient30.wav", d / "assets" / "ambient.wav")
(d / "index.html").write_text(page(DUR, body, js, "voix.wav").replace("</style>", EXTRA + "</style>", 1))
print("ok", d)
