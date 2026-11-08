"""Reels Instagram (+ Shorts YouTube) — semaine du 09 au 15/11/2026, 18h00.
lun V3 (conseil guidance) · mer V2 (promo série « Pensé pour votre métier » : astrologue) · ven V2 (conseil guidance) · dim V3 (conseil guidance).
Alternance des gabarits : jamais deux fois le même d'affilée. Voix Claire, « Guide Pilote » dans le texte lu.
Usage : python3 reels/reels_specs_2026-11-09.py <clé> <voix.wav>   (clé : lun | mer | ven | dim)
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_tiktok_v3 as v3
import gen_v2 as v2

G = lambda a, b: f'{a} <span style="color:#E9C46A">{b}</span>'

SPECS = {
# ---------- lundi 09/11 · 18h · CONSEIL guidance · V3 · pilier argent · contexte : 1er contact en message privé ----------
"lun": {"gen": "v3", "slug": "lun-09_reel-c-est-combien", "music": "elan", "scenes": [
  {"k": "hook", "static": True, "bg": "marine", "title": "« C'est combien ? » [Vous répondez quoi ?]", "size": 122, "top": 450,
   "sub": "3 réponses à ne plus envoyer.", "subt": 1.9, "subtop": 1090,
   "say": "« C'est combien ? » Vous répondez quoi ? Trois réponses à ne plus envoyer."},
  {"k": "num", "bg": "creme", "n": "1", "title": "« Ça [dépend…] »", "sub": "Elle ne sait toujours pas. Elle passe son chemin.",
   "say": "Un : « ça dépend ». Elle passe son chemin."},
  {"k": "num", "bg": "or", "n": "2", "title": "« Je vous explique [par téléphone] »", "size": 104, "sub": "Un appel… pour connaître un prix ?",
   "say": "Deux : « je vous explique par téléphone ». Pour un prix ? Trop demander."},
  {"k": "num", "bg": "bleu", "n": "3", "title": "« C'est sur ma page », [sans le lien]", "size": 104, "sub": "Elle ne cherchera pas.",
   "say": "Trois : « c'est sur ma page », sans le lien. Elle ne cherchera pas."},
  {"k": "words", "bg": "marine", "title": "Le tarif, la durée, [et le lien.]", "size": 130, "top": 560,
   "say": "Ce qui marche : le tarif, la durée, et le lien pour réserver."},
  {"k": "shot", "bg": "creme", "title": "Dans GuidPilot, [votre page répond]", "size": 84, "img": "page_np.png", "stop": 560, "sh": 560,
   "imgstyle": "width:1420px;max-width:none;margin-left:-400px;margin-top:-116px", "ctop": 1180,
   "checks": ["Prestations et tarifs visibles", "Réservation en ligne, 24 h/24"],
   "say": "Dans Guide Pilote, tout est sur votre page. Votre lien répond à votre place."},
  {"k": "end", "bg": "marine", "title": G("Et vous, que répondez-vous à", "« c'est combien&nbsp;? »"),
   "save": "🔖 Enregistrez-la pour plus tard", "say": "Enregistrez cette vidéo. Et vous, que répondez-vous ?"},
 ]},

# ---------- mercredi 11/11 · 18h · PROMO série « Pensé pour votre métier » · astrologue · V2 ----------
"mer": {"gen": "v2", "slug": "mer-11_reel-astrologue-theme-natal", "music": "aube", "scenes": [
  {"k": "hook2", "title": "Astrologue&nbsp;: votre thème natal écrit, <span>vous l'envoyez comment&nbsp;?</span>", "size": 100, "sub": "Par mail, en pièce jointe… ?", "subt": 2.2,
   "say": "Astrologue : votre thème natal écrit, vous l'envoyez comment ? En pièce jointe ?"},
  {"k": "shot", "tag": "ÉTAPE 1", "title": "Elle commande <span>et règle en ligne</span>", "img": "page_np.png", "W": 1100, "box": (310, 90, 960, 580),
   "say": "Un : elle commande son étude sur votre page et règle en ligne, délai affiché."},
  {"k": "x", "tag": "ÉTAPE 2", "title": "Vous rédigez <span>quand vous voulez</span>", "top": 300, "extop": 680,
   "ex": ("list", ["Sa date, son heure, son lieu de naissance : dans sa fiche", "Vos notes privées, à part", "Brouillon → finalisée"], "auto"), "ext": 0.6,
   "say": "Deux : vous rédigez quand vous voulez. Ses données de naissance sont dans sa fiche."},
  {"k": "shot", "tag": "ÉTAPE 3", "title": "Son étude l'attend <span>dans son espace</span>", "img": "guid.png", "W": 1270, "box": (430, 232, 820, 480),
   "say": "Trois : votre étude, écrite ou en audio, l'attend dans son espace sécurisé."},
  {"k": "shot", "tag": "ÉTAPE 4", "title": "Et son avis rejoint <span>votre page</span>", "img": "avis.png", "W": 1270, "box": (20, 150, 930, 310),
   "say": "Quatre : la demande d'avis part en un clic, et l'avis rejoint votre page."},
  {"k": "quote", "title": "Un outil pensé pour votre métier, <span>pas un agenda de plus.</span>",
   "say": "Un outil pensé pour votre métier. Pas un agenda de plus."},
  {"k": "save", "kw": "GUIDANCE", "q": "et recevez la présentation en privé",
   "say": "Guide Pilote : quatorze jours gratuits, sans carte bancaire."},
 ]},

# ---------- vendredi 13/11 · 18h · CONSEIL guidance · V2 · pilier visibilité · contexte : avant la réservation ----------
"ven": {"gen": "v2", "slug": "ven-13_reel-avant-de-reserver", "music": "lofi", "scenes": [
  {"k": "hook2", "title": "Ce que vos clientes regardent <span>avant de réserver</span>", "size": 104, "sub": "Et que vous ne voyez pas.", "subt": 2.0,
   "say": "Ce que vos clientes regardent avant de réserver un tirage. Et que vous ne voyez pas."},
  {"k": "step", "n": 1, "top": 430, "extop": 920, "size": 84, "title": "Les avis <span>des autres</span>",
   "ex": ("card", "SANS AVIS", "Elle hésite, elle compare, elle attend."), "ext": 1.0,
   "say": "Un : les avis. Sans avis, elle hésite, elle compare, elle attend."},
  {"k": "step", "n": 2, "top": 430, "extop": 920, "size": 84, "title": "Un prix et une durée <span>clairs</span>",
   "ex": ("vs", "« Tarifs sur demande »", "« Tirage complet · 45 min · tarif affiché »", 0.9), "ext": 0.9,
   "say": "Deux : un prix et une durée clairs. « Tarifs sur demande », c'est un frein."},
  {"k": "step", "n": 3, "top": 430, "extop": 920, "size": 84, "title": "Réserver <span>sans vous écrire</span>",
   "ex": ("vs", "« Envoyez-moi un message »", "Un créneau choisi en 30 secondes", 0.9), "ext": 0.9,
   "say": "Trois : réserver sans vous écrire. À vingt-trois heures, elle n'attend pas votre réponse."},
  {"k": "shot", "at": 15.75, "tag": "DANS GUIDPILOT", "title": "Les trois, <span>sur une seule page</span>", "img": "page_np.png", "W": 1100, "box": (310, 280, 960, 580),
   "say": "Dans Guide Pilote, les trois sont sur votre page."},
  {"k": "save", "at": 18.9, "q": "Lequel des trois manque chez vous&nbsp;? 👇",
   "say": "Enregistrez cette vidéo. Lequel des trois manque chez vous ?"},
 ]},

# ---------- dimanche 15/11 · 18h · CONSEIL guidance · V3 · pilier suivi / fidélisation · contexte : le lendemain ----------
"dim": {"gen": "v3", "slug": "dim-15_reel-message-du-lendemain", "music": "cocon", "scenes": [
  {"k": "hook", "static": True, "bg": "creme", "title": "Après le tirage, le message [qu'elle attend…]", "size": 120, "top": 450,
   "sub": "Et qu'elle ne reçoit presque jamais.", "subt": 1.9, "subtop": 1090,
   "say": "Après le tirage, il y a un message que votre cliente attend. Et qu'elle ne reçoit presque jamais."},
  {"k": "words", "bg": "marine", "title": "Pas une relance. [Une attention.]", "size": 140, "top": 580,
   "say": "Pas une relance. Une attention, le lendemain."},
  {"k": "notifs", "bg": "or", "title": "Le [lendemain,] 3 lignes", "clock": "10:30", "date": "lundi 16 novembre",
   "items": [("💬", "Message", "« Bonjour Julie, j'espère que la nuit a porté conseil. »", "« Si une question remonte, je suis là. »")],
   "say": "Trois lignes suffisent : j'espère que la nuit a porté conseil. Si une question remonte, je suis là."},
  {"k": "tiles", "bg": "bleu", "title": "Ce que ça [change]",
   "items": [("🤍", "Elle se sent suivie"), ("🔁", "Elle revient d'elle-même"), ("★", "Elle laisse un avis plus volontiers"), ("💬", "Elle parle de vous")],
   "say": "Elle se sent suivie, elle revient d'elle-même, et elle parle de vous."},
  {"k": "lock", "bg": "marine", "title": "Dans [GuidPilot]", "card": "Sa guidance et vos échanges, au même endroit", "note": "Votre message part depuis sa fiche, rangé avec sa guidance.",
   "say": "Dans Guide Pilote, ce message part depuis sa fiche, rangé avec sa guidance."},
  {"k": "end", "bg": "marine", "title": G("Vous écrivez", "le lendemain&nbsp;?"),
   "save": "🔖 Enregistrez-la pour plus tard", "say": "Enregistrez cette vidéo. Et vous, vous écrivez le lendemain ?"},
 ]},
}

if __name__ == "__main__":
    s = SPECS[sys.argv[1]]
    (v3 if s["gen"] == "v3" else v2).build(s, sys.argv[2])
