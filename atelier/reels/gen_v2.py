"""Reels LIGNE ÉDITORIALE V2 (15/10/2026) : 15–30 s, accroche visible dès la 1re image, pas d'intro logo, fin courte.
Réutilise les scènes de gen_conseils.py (step / bad / list / vs / quote) et ajoute :
  - "hook2" : phrase-choc en très gros, déjà lisible à la frame 0 (pas de fondu depuis le noir) ;
  - "save"  : scène de fin courte « Enregistrez-la » (CONSEIL) ou « Commentez MOT-CLÉ » (PROMO, champ "kw"), + guidpilot.fr discret.
Pas de grand écran final logo + offre. Badge IA plus petit.
Usage : python3 reels/gen_v2.py <clé> <voix.wav>   (textes dans reels/v2_specs.py) → build/<slug>/
"""
import pathlib, shutil, sys, subprocess, re
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_conseils as gc

EXTRA_V2 = """
.aibadge{font-size:22px !important;padding:8px 18px !important;top:56px !important;opacity:.85}
.hook2{font-weight:800;font-size:124px;line-height:1.04;color:#fff;letter-spacing:-.03em;width:960px}
.hook2 span{color:#E9C46A}
.hsub{margin-top:48px;font-weight:700;font-size:52px;color:#93C5FD;width:900px;line-height:1.25}
.savebox{width:900px;border:4px dashed #E9C46A;border-radius:40px;padding:60px 50px}
.savebox .ic{font-size:130px;line-height:1}
.savebox .t{margin-top:30px;font-weight:800;font-size:84px;line-height:1.08;color:#fff}
.savebox .q{margin-top:34px;font-weight:600;font-size:46px;line-height:1.3;color:#CBD5E1}
.vs p{font-size:54px !important}.vs h4{font-size:46px !important}
.site{position:absolute;left:0;right:0;bottom:170px;text-align:center;font-weight:700;font-size:40px;color:#64748B}
"""

_scene = gc.scene

def scene(i, sc, t0, t1):
    k = sc["k"]; sid = f"s{i}"; d = round(t1 - t0, 2)
    if k == "hook2":
        body = f'''<div class="center" style="top:{sc.get("top",560)}px"><div class="hook2" id="{sid}t">{sc["title"]}</div>
{f'<div class="hsub" id="{sid}s">{sc["sub"]}</div>' if sc.get("sub") else ""}</div>'''
        js = [f'tl.fromTo("#{sid}t",{{scale:1.06}},{{scale:1,duration:.8,ease:E}},0);']
        if sc.get("sub"):
            js.append(f'tl.fromTo("#{sid}s",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.4,ease:E}},{round(t0 + sc.get("subt", 1.0),2)});')
        html = f'<div id="{sid}" class="clip navy" data-start="{round(t0,2)}" data-duration="{d}" data-track-index="1">{body}</div>'
        return html.replace(" ?", "&nbsp;?").replace(" !", "&nbsp;!").replace(" :", "&nbsp;:").replace("« ", "«&nbsp;").replace(" »", "&nbsp;»"), "\n".join(js)
    if k == "save":
        if sc.get("kw"):
            ic, t = "💬", f'Commentez <span style="color:#E9C46A">{sc["kw"]}</span>'
        else:
            ic, t = "🔖", "Enregistrez-la pour plus tard"
        body = f'''<div class="center" style="top:520px"><div class="savebox" id="{sid}b"><div class="ic">{ic}</div><div class="t">{t}</div>
{f'<div class="q">{sc["q"]}</div>' if sc.get("q") else ""}</div></div><div class="site">guidpilot.fr</div>'''
        js = [f'tl.fromTo("#{sid}b",{{opacity:0,scale:.85}},{{opacity:1,scale:1,duration:.5,ease:"back.out(1.7)"}},{round(t0+.05,2)});']
        html = f'<div id="{sid}" class="clip navy" data-start="{round(t0,2)}" data-duration="{d}" data-track-index="1">{body}</div>'
        return html.replace(" ?", "&nbsp;?"), "\n".join(js)
    return _scene(i, sc, t0, t1)


def build(spec, voix):
    gc.align(spec, voix)
    # V2 : pas d'écran final long — la dernière scène (save) va jusqu'à la fin de la voix + 1,2 s
    spec["dur"] = round(spec["cta"] - 0.35 + 1.2, 2)
    scs = spec["scenes"]; dur = spec["dur"]
    bodies, jss = [], []
    for i, sc in enumerate(scs):
        t1 = scs[i + 1]["t"] if i + 1 < len(scs) else dur
        h, j = scene(i, sc, sc["t"], t1)
        bodies.append(h); jss.append(j)
    d = gc.BASE / "build" / spec["slug"]
    if d.exists(): shutil.rmtree(d)
    (d / "assets").mkdir(parents=True)
    for sub in ("fonts", "vendor"): shutil.copytree(gc.SRC / sub, d / sub)
    for f in ("hyperframes.json", "meta.json"): shutil.copy(gc.SRC / f, d / f)
    shutil.copy(voix, d / "assets" / "voix.wav")
    shutil.copy(gc.BASE / "reels" / "ambient30.wav", d / "assets" / "ambient.wav")
    html = gc.page(dur, "\n".join(bodies), "\n".join(jss), "voix.wav").replace("</style>", gc.EXTRA + EXTRA_V2 + "</style>", 1)
    (d / "index.html").write_text(html)
    print("ok", d, "durée", dur)


SPECS = {
"test-3-phrases": {"slug": "v2-test-3-phrases", "scenes": [
  {"k": "hook2", "title": "3 phrases qui font <span>fuir</span> vos clientes", "sub": "Sans que vous le sachiez.", "subt": 1.7,
   "say": "Trois phrases qui font fuir vos clientes. Sans que vous le sachiez."},
  {"k": "step", "n": 1, "top": 430, "extop": 920, "size": 88, "title": "Quand on vous demande <span>le prix</span>",
   "ex": ("vs", "« Ça dépend… »", "La durée et le tarif, clairement", 0.9), "ext": 1.0,
   "say": "Un : « ça dépend », quand on vous demande le prix. Donnez la durée et le tarif, clairement."},
  {"k": "step", "n": 2, "top": 430, "extop": 920, "size": 88, "title": "Pour <span>prendre rendez-vous</span>",
   "ex": ("vs", "« Écrivez-moi quand vous voulez »", "Un lien pour réserver", 1.0), "ext": 0.9,
   "say": "Deux : « écrivez-moi quand vous voulez ». Proposez plutôt un lien pour réserver."},
  {"k": "step", "n": 3, "top": 430, "extop": 920, "size": 88, "title": "Pour <span>rassurer</span>",
   "ex": ("vs", "Promettre des réponses", "Décrire comment se passe la séance", 1.0), "ext": 0.9,
   "say": "Trois : promettre des réponses. Décrivez plutôt comment se passe la séance."},
  {"k": "save", "q": "Laquelle avez-vous déjà dite&nbsp;? 👇",
   "say": "Enregistrez cette vidéo. Et dites-moi en commentaire laquelle vous avez déjà dite."},
]},
}

if __name__ == "__main__":
    build(SPECS[sys.argv[1]], sys.argv[2])
