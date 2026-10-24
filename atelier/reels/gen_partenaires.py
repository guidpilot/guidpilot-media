"""Reels de recrutement de partenaires (21/10/2026) — règles : aucun tarif ni montant, jamais « affiliation »,
vouvoiement, pas de personnage, mot-clé ManyChat PARTENAIRE, logo officiel en fin.
Usage : python3 reels/gen_partenaires.py <clé> <voix.wav>  → build/<slug>/
"""
import pathlib, sys, shutil
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_v2 as g
import gen_conseils as gc

LOGO_CSS = ".endlogo{position:absolute;left:0;right:0;bottom:250px;display:flex;justify-content:center}.endlogo img{width:340px}"

SPECS = {
"partenaires-formateurs": {"slug": "partenaires-formateurs", "music": "elan", "scenes": [
  {"k": "hook2", "title": "Vous formez des <span>praticiens</span>&nbsp;?", "sub": "ou des thérapeutes", "subt": 1.2,
   "say": "Vous formez des praticiens ou des thérapeutes ?"},
  {"k": "x", "tag": "APRÈS LA FORMATION", "title": "Vos élèves se posent <span>la même question</span>", "top": 300, "extop": 700,
   "ex": ("chat", [("in", "Comment je m'organise pour recevoir mes premiers clients&nbsp;?"), ("in", "Et les rendez-vous, les paiements, les factures&nbsp;?")], 1.2), "ext": 0.8,
   "say": "À la fin de leur formation, vos élèves se posent tous la même question : comment s'organiser pour recevoir leurs premiers clients ?"},
  {"k": "shot", "tag": "GUIDPILOT", "title": "L'outil conçu <span>pour leur métier</span>", "img": "page_np.png", "W": 1100, "box": (310, 90, 960, 590),
   "say": "GuidPilot est l'outil conçu pour leur métier."},
  {"k": "x", "tag": "AU MÊME ENDROIT", "title": "Tout ce dont <span>ils ont besoin</span>", "top": 300, "extop": 660,
   "ex": ("list", ["Réservation en ligne", "Paiement", "Factures", "Espace client"], "auto"), "ext": 0.5,
   "say": "Réservation, paiement, factures, espace client : tout est au même endroit."},
  {"k": "hook2", "title": "Nous cherchons des <span>partenaires</span>", "sub": "pour faire connaître GuidPilot", "subt": 0.9, "size": 112,
   "say": "Nous cherchons des partenaires pour le faire connaître."},
  {"k": "save", "kw": "PARTENAIRE", "q": "et recevez le lien pour candidater",
   "say": "Vous souhaitez en faire partie ? Commentez partenaire."},
]},
"partenaires-communaute": {"slug": "partenaires-communaute", "music": "lofi", "scenes": [
  {"k": "hook2", "title": "On vous demande <span>vos outils</span>&nbsp;?", "sub": "Souvent&nbsp;?", "subt": 1.4,
   "say": "On vous demande souvent quels outils vous utilisez ?"},
  {"k": "x", "tag": "VOTRE COMMUNAUTÉ", "title": "Elle vous fait <span>confiance</span>", "top": 300, "extop": 680,
   "ex": ("chat", [("in", "Vous utilisez quoi pour vos rendez-vous&nbsp;?"), ("in", "Vous me conseillez quel outil&nbsp;?")], 0.8), "ext": 0.4,
   "say": "Votre communauté vous fait confiance."},
  {"k": "shot", "tag": "GUIDPILOT", "title": "Pensé pour les praticiens <span>et les thérapeutes</span>", "img": "page_np.png", "W": 1100, "box": (310, 90, 960, 590), "size": 68,
   "say": "GuidPilot est l'outil pensé pour les praticiens et les thérapeutes :"},
  {"k": "shot", "tag": "AU QUOTIDIEN", "title": "Réservé, payé, <span>facturé</span>", "img": "dash_np.png", "W": 1270, "box": (20, 585, 805, 845),
   "say": "leurs clients réservent et paient en ligne, et la facture se crée toute seule."},
  {"k": "hook2", "title": "Recommandez-le à <span>votre communauté</span>", "sub": "Nous cherchons des partenaires", "subt": 0.9, "size": 104,
   "say": "Nous cherchons des partenaires qui souhaitent le recommander à leur communauté."},
  {"k": "save", "kw": "PARTENAIRE", "q": "et recevez le lien pour candidater",
   "say": "Pour découvrir le programme partenaire, commentez partenaire."},
]},
"partenaires-createurs-outils": {"slug": "partenaires-createurs-outils", "music": "pilote", "scenes": [
  {"k": "hook2", "title": "Vous recommandez déjà <span>des outils</span>&nbsp;?", "sub": "aux praticiens", "subt": 1.4, "size": 112,
   "say": "Vous recommandez déjà des outils aux praticiens ?"},
  {"k": "x", "tag": "VOTRE AUDIENCE", "title": "Elle compte sur vous <span>pour bien choisir</span>", "top": 300, "extop": 680,
   "ex": ("list", ["Logiciels", "Applications", "Formations"], "auto"), "ext": 0.4,
   "say": "Logiciels, applications, formations… Votre audience compte sur vous pour bien choisir."},
  {"k": "shot", "tag": "GUIDPILOT", "title": "Conçu pour la guidance <span>et les thérapeutes</span>", "img": "guid.png", "W": 1270, "box": (430, 150, 1235, 480), "size": 68,
   "say": "GuidPilot est un outil conçu pour les praticiens en guidance et les thérapeutes."},
  {"k": "hook2", "title": "Nous cherchons des <span>partenaires</span>", "sub": "qui connaissent ce public", "subt": 0.9, "size": 112,
   "say": "Nous cherchons des partenaires qui connaissent ce public."},
  {"k": "save", "kw": "PARTENAIRE", "q": "et recevez le lien pour candidater",
   "say": "Pour recevoir le lien de candidature, commentez partenaire."},
]},
}

if __name__ == "__main__":
    spec = SPECS[sys.argv[1]]
    g.build(spec, sys.argv[2])
    d = gc.BASE / "build" / spec["slug"]
    shutil.copy(gc.SRC / "assets" / "logo_blanc.png", d / "assets" / "logo_blanc.png")
    h = (d / "index.html").read_text()
    h = h.replace('<div class="site">guidpilot.fr</div>', '<div class="endlogo"><img src="assets/logo_blanc.png" alt="GuidPilot" /></div><div class="site" style="bottom:170px">Candidature sur guidpilot.fr</div>')
    h = h.replace("</style>", LOGO_CSS + "</style>", 1)
    (d / "index.html").write_text(h)
