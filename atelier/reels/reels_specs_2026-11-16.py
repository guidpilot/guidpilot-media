"""Reels Instagram + Shorts — semaine du 16 au 22/11/2026 (lot lancé à la main par Normane le 15/11, « formats nouveaux »).
Demande de Normane : du contenu différent de ce qui a déjà été fait, l'offre de Noël (jusqu'au 31/12) et le programme partenaires.
mar 17 · 18h · PARTENAIRES · V2 (angle inédit : les élèves qui s'installent en janvier + offre de Noël pour leur communauté)
mer 18 · 18h · OFFRE · V3 · « Le calcul » (99 € / 12 mois = 8,25 €) — message clé du plan du 09/11 jamais traité en vidéo
jeu 19 · 18h · COULISSES · V3 · journal de bord de la semaine (série jamais lancée ; faits vérifiés : audit du 11/11, refonte mobile, assistant du site)
dim 22 · 18h · TEASER · V3 · calendrier de l'Avent en stories dès le 1er décembre
Règles : vouvoiement, aucune personne, aucun superlatif, « Guide Pilote » prononcé, badge IA, une action montrée deux fois.
Partenaires : aucun montant de commission, jamais « affiliation », mot-clé PARTENAIRE (le 99 € est le prix de l'offre, pas une commission).
Usage : python3 reels/reels_specs_2026-11-16.py <clé> <voix.wav>   (clé : mar | mer | jeu | dim)
"""
import pathlib, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_tiktok_v3 as v3
import gen_v2 as v2
import gen_conseils as gc

G = lambda a, b: f'{a} <span style="color:#E9C46A">{b}</span>'
LOGO_CSS = ".endlogo{position:absolute;left:0;right:0;bottom:250px;display:flex;justify-content:center}.endlogo img{width:340px}"

SPECS = {
# ---------- mardi 17/11 · 18h · PARTENAIRES · V2 ----------
"mar": {"gen": "part", "slug": "mar-17_reel-partenaires-janvier", "music": "elan", "scenes": [
  {"k": "hook2", "title": "En janvier, vos élèves <span>ouvrent leur cabinet.</span>", "size": 104, "sub": "Avec quel outil ?", "subt": 1.9,
   "say": "En janvier, vos élèves ouvrent leur cabinet. Avec quel outil ?"},
  {"k": "x", "tag": "LA QUESTION DE FIN DE FORMATION", "title": "Ils vous demandent <span>par où commencer</span>", "top": 300, "extop": 700,
   "ex": ("chat", [("in", "Je prends mes rendez-vous comment&nbsp;?"), ("in", "Et pour me faire payer, les factures&nbsp;?")], 1.0), "ext": 0.6,
   "say": "Rendez-vous, paiements, factures : c'est à vous qu'ils demandent par où commencer."},
  {"k": "shot", "tag": "GUIDPILOT", "title": "Conçu pour la guidance <span>et les thérapeutes</span>", "img": "page_np.png", "W": 1100, "box": (310, 90, 960, 590), "size": 68,
   "say": "GuidPilot est un outil conçu pour les praticiens en guidance et les thérapeutes."},
  {"k": "hook2", "title": "Jusqu'au 31 décembre : <span>1 an pour 99 €</span>", "sub": "pour celles et ceux qui s'installent", "subt": 1.0, "size": 104,
   "say": "Et jusqu'au trente et un décembre, ils peuvent s'équiper pour un an, à quatre-vingt-dix-neuf euros."},
  {"k": "hook2", "title": "Nous cherchons des <span>partenaires</span>", "sub": "formatrices, écoles, créatrices de contenu", "subt": 0.9, "size": 112,
   "say": "Formatrices, écoles, créatrices de contenu : nous cherchons des partenaires pour le faire connaître."},
  {"k": "save", "kw": "PARTENAIRE", "q": "et recevez le lien pour candidater",
   "say": "Commentez partenaire, et recevez le lien pour candidater."},
 ]},

# ---------- mercredi 18/11 · 18h · OFFRE DE NOËL · guidance · V3 · « le calcul » ----------
"mer": {"gen": "v3", "slug": "mer-18_reel-noel-le-calcul", "music": "pilote", "mid_cta": "1 an pour 99 € · <span>lien en bio</span>", "scenes": [
  {"k": "hook", "static": True, "bg": "bleu", "title": "99~€ divisés par 12 mois. [Faites le calcul.]", "size": 122, "top": 450,
   "sub": "Le résultat tient en une ligne.", "subt": 2.0, "subtop": 1100,
   "say": "Quatre-vingt-dix-neuf euros, divisés par douze mois. Faites le calcul."},
  {"k": "words", "bg": "creme", "title": "[8,25~€] par mois.", "size": 190, "top": 560,
   "say": "Huit euros vingt-cinq par mois."},
  {"k": "words", "bg": "marine", "title": "Au mois : 29~€. Sur un an : [348~€.]", "size": 124, "top": 520,
   "say": "Au mois, c'est vingt-neuf euros. Soit trois cent quarante-huit euros sur un an."},
  {"k": "tiles", "bg": "or", "title": "Pour [8,25~€] par mois",
   "items": [("📅", "Réservation en ligne"), ("💳", "Paiement et factures"), ("🔒", "Espace client privé"), ("⭐", "Avis sur votre page")],
   "say": "Pour ce prix : la réservation en ligne, le paiement et les factures, l'espace privé de vos clientes, et les avis sur votre page."},
  {"k": "words", "bg": "creme", "title": "Payé [une seule fois.] Aucun prélèvement.", "size": 118, "top": 540,
   "say": "Payé une seule fois. Aucun prélèvement automatique."},
  {"k": "endad", "bg": "marine", "title": G("Le calcul est", "vite fait."), "top": 520,
   "pill": "🎁 1 an pour 99 €", "sub": "Jusqu'au 31 décembre · guidpilot.fr",
   "say": "Jusqu'au trente et un décembre. Le lien est en bio."},
 ]},

# ---------- jeudi 19/11 · 18h · COULISSES · V3 · journal de bord ----------
"jeu": {"gen": "v3", "slug": "jeu-19_reel-coulisses-bouton-inscription", "music": "lofi",
        "mid_cta": ("💬", "Votre avis <span>en commentaire</span>"), "scenes": [
  {"k": "hook", "static": True, "bg": "marine", "title": "Notre bouton d'inscription était [hors de l'écran.]", "size": 116, "top": 450,
   "sub": "Coulisses de GuidPilot, cette semaine.", "subt": 2.0, "subtop": 1100,
   "say": "Sur téléphone, notre bouton d'inscription était hors de l'écran. On l'a découvert cette semaine."},
  {"k": "words", "bg": "or", "title": "Il fallait [faire défiler] pour le trouver.", "size": 122, "top": 520,
   "say": "Il fallait faire défiler la page pour le trouver. Autant dire que presque personne ne le voyait."},
  {"k": "num", "bg": "creme", "n": "1", "title": "L'inscription, [refaite pour le téléphone]", "size": 100,
   "say": "Alors, un : la page d'inscription a été refaite pour le téléphone."},
  {"k": "num", "bg": "bleu", "n": "2", "title": "Une page d'essai [plus courte]", "size": 108,
   "say": "Deux : la page d'essai a été allégée."},
  {"k": "num", "bg": "marine", "n": "3", "title": "Un assistant [répond à vos questions]", "size": 100, "sub": "Sur le site, avant de vous inscrire.",
   "say": "Trois : sur le site, un assistant répond maintenant à vos questions."},
  {"k": "words", "bg": "creme", "title": "Un outil se construit [avec vos retours.]", "size": 122, "top": 540,
   "say": "Un outil se construit avec vos retours."},
  {"k": "end", "bg": "marine", "title": G("Qu'est-ce qui vous fait", "quitter une inscription&nbsp;?"),
   "save": "Répondez en commentaire 👇", "say": "Et vous, qu'est-ce qui vous fait quitter une inscription ?"},
 ]},

# ---------- dimanche 22/11 · 18h · TEASER calendrier de l'Avent · guidance · V3 ----------
"dim": {"gen": "v3", "slug": "dim-22_reel-calendrier-avent", "music": "aube",
        "mid_cta": ("🔔", "Abonnez-vous <span>avant le 1er décembre</span>"), "scenes": [
  {"k": "hook", "static": True, "bg": "or", "title": "24 jours, [24 astuces] pour votre activité.", "size": 124, "top": 450,
   "sub": "Ça commence le 1er décembre.", "subt": 2.0, "subtop": 1100,
   "say": "Vingt-quatre jours, vingt-quatre astuces pour votre activité. Ça commence le premier décembre."},
  {"k": "words", "bg": "marine", "title": "Un calendrier de l'Avent, [en stories.]", "size": 128, "top": 520,
   "say": "Un calendrier de l'Avent, en stories. Une astuce par jour, à appliquer tout de suite."},
  {"k": "tiles", "bg": "creme", "title": "Au [programme]",
   "items": [("💬", "Messages prêts à copier"), ("📅", "Votre agenda de janvier"), ("💳", "Paiements sans relance"), ("⭐", "Avis et fidélité")],
   "say": "Au programme : des messages prêts à copier, votre agenda de janvier, les paiements sans relance, les avis."},
  {"k": "words", "bg": "bleu", "title": "Pour ne rien manquer : [abonnez-vous.]", "size": 122, "top": 540,
   "say": "Pour ne rien manquer, abonnez-vous au compte."},
  {"k": "end", "bg": "marine", "title": G("Quelle astuce aimeriez-vous", "y trouver&nbsp;?"),
   "save": "Répondez en commentaire 👇", "say": "Et vous, quelle astuce aimeriez-vous y trouver ?"},
 ]},
}

if __name__ == "__main__":
    s = SPECS[sys.argv[1]]
    if s["gen"] == "v3":
        v3.build(s, sys.argv[2])
    else:
        v2.build(s, sys.argv[2])
        if s["gen"] == "part":  # fin partenaires : logo officiel + « Candidature sur guidpilot.fr » (comme gen_partenaires.py)
            d = gc.BASE / "build" / s["slug"]
            shutil.copy(gc.SRC / "assets" / "logo_blanc.png", d / "assets" / "logo_blanc.png")
            h = (d / "index.html").read_text()
            h = h.replace('<div class="site">guidpilot.fr</div>', '<div class="endlogo"><img src="assets/logo_blanc.png" alt="GuidPilot" /></div><div class="site" style="bottom:170px">Candidature sur guidpilot.fr</div>')
            h = h.replace("</style>", LOGO_CSS + "</style>", 1)
            (d / "index.html").write_text(h)
