"""Reel ManyChat (Instagram uniquement) : appel à commenter un mot-clé, reçu en message privé via ManyChat.
Usage : python3 reels/gen_manychat.py <voix.wav>
Réutilise les scènes de gen_conseils.py / gen_promos.py avec des temps fixés à la main (silencedetect),
et remplace l'écran final par un CTA « Commentez <MOT> et recevez la présentation en message privé ».
Version du 13/10/2026 : public thérapeutes, mot-clé THÉRAPEUTE. Sortie : build/<slug>/
"""
import pathlib, shutil, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import gen_promos as gp
gc = gp.gc

SLUG, MOT, DUR = "m1-therapeute", "THÉRAPEUTE", 25.8
# Temps calés sur voix/2026-10-13_manychat-therapeute.mp3 (22,4 s)
SCENES = [
  ({"k": "x", "tag": "THÉRAPEUTES", "title": "Votre cabinet, <span>éparpillé</span>", "ext": 0.1, "extop": 720,
    "ex": ("list", ["!Rendez-vous : un agenda", "!Paiements : une appli", "!Factures : un tableur", "!Notes de séance : un carnet"], 1.5)}, 0.0),
  ({"k": "hook", "kicker": "SOPHROLOGIE · HYPNOSE · REIKI", "title": "4 outils pour <span>un seul cabinet</span>&nbsp;?", "size": 100}, 6.4),
  ({"k": "shot", "tag": "AVEC GUIDPILOT", "title": "Tout dans <span>un seul espace</span>", "img": "dash_np.png", "W": 1270, "box": (15, 145, 620, 550)}, 8.1),
  ({"k": "x", "title": "Tout est <span>réuni</span>", "size": 84, "ext": 0.1, "extop": 600,
    "ex": ("list", ["Réservation et paiement en ligne", "Fiches clientes et historique", "Notes privées, jamais visibles par la cliente", "Factures automatiques"], 1.85)}, 11.05),
]
CTA_T = 18.4

CTA_CSS = """
.mc-lead{font-weight:800;font-size:76px;color:#fff;letter-spacing:-.01em}
.mc-box{margin-top:34px;display:flex;align-items:center;gap:26px;background:#fff;border-radius:36px;padding:34px 44px;box-shadow:0 30px 80px rgba(0,0,0,.35)}
.mc-box i{font-style:normal;flex:none;width:96px;height:96px;border-radius:50%;background:#E0E7FF;display:flex;align-items:center;justify-content:center;font-size:52px}
.mc-word{font-weight:800;font-size:104px;color:#0F172A;letter-spacing:.02em}
.mc-sub{margin-top:44px;font-weight:700;font-size:56px;line-height:1.25;color:#fff;width:900px}
.mc-sub span{color:#E9C46A}
.mc-offer{margin-top:56px;display:inline-block;background:#FBF3DC;color:#6B4E16;font-weight:700;font-size:40px;padding:18px 40px;border-radius:999px}
.mc-site{margin-top:40px;font-weight:800;font-size:52px;color:#60A5FA}
"""

def cta_html(t, d):
    return f'''<div id="cta" class="clip navy" data-start="{t}" data-duration="{d}" data-track-index="1">
  <div class="center" style="top:200px"><img id="cl" src="assets/logo_blanc.png" alt="GuidPilot" style="width:480px;display:block" /></div>
  <div class="center" style="top:520px"><div class="mc-lead" id="c1">Commentez</div>
  <div class="mc-box" id="c2"><i>💬</i><span class="mc-word">{MOT}</span></div>
  <div class="mc-sub" id="c3">et recevez la présentation <span>en message privé</span></div>
  <div class="mc-offer" id="c4">14 jours gratuits · sans carte bancaire</div>
  <div class="mc-site" id="c5">guidpilot.fr</div></div>
</div>'''

def cta_js(t):
    return f'''tl.fromTo("#cl",{{opacity:0,y:-30}},{{opacity:1,y:0,duration:.5,ease:E}},{t+.05});
tl.fromTo("#c1",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.4,ease:E}},{t+.15});
tl.fromTo("#c2",{{opacity:0,scale:.6}},{{opacity:1,scale:1,duration:.6,ease:"back.out(1.8)"}},{t+.4});
tl.fromTo("#c3",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45,ease:E}},{t+1.4});
tl.fromTo("#c4",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45,ease:E}},{t+2.6});
tl.fromTo("#c5",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45,ease:E}},{t+3.0});
tl.to("#c2",{{scale:1.06,duration:.45,yoyo:true,repeat:5,ease:"sine.inOut"}},{t+1.2});'''

def build(voix):
    gp.IMGS.clear()
    bodies, jss = [], []
    for i, (sc, t0) in enumerate(SCENES):
        t1 = SCENES[i + 1][1] if i + 1 < len(SCENES) else CTA_T
        h, j = gp.scene(i, sc, t0, t1)
        bodies.append(h); jss.append(j)
    bodies.append(cta_html(CTA_T, round(DUR - CTA_T, 2)))
    js = "\n".join(jss) + "\n" + cta_js(CTA_T)
    d = gc.BASE / "build" / SLUG
    if d.exists(): shutil.rmtree(d)
    (d / "assets").mkdir(parents=True)
    for sub in ("fonts", "vendor"): shutil.copytree(gc.SRC / sub, d / sub)
    for f in ("hyperframes.json", "meta.json"): shutil.copy(gc.SRC / f, d / f)
    for im in gp.IMGS | {"logo_blanc.png"}: shutil.copy(gc.SRC / "assets" / im, d / "assets" / im)
    shutil.copy(voix, d / "assets" / "voix.wav")
    shutil.copy(gc.BASE / "reels" / "ambient30.wav", d / "assets" / "ambient.wav")
    html = gc.page(DUR, "\n".join(bodies), js, "voix.wav").replace("</style>", gc.EXTRA + gp.PCSS + CTA_CSS + "</style>", 1)
    (d / "index.html").write_text(html)
    print("ok", d)

if __name__ == "__main__":
    build(sys.argv[1])
