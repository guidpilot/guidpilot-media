"""Reels Instagram (+ Shorts YouTube) — semaine du 23 au 29/11/2026, 18h00. Lot automatique du dimanche 22/11.
lun 23 · CONSEIL guidance · V3 · citation de cliente « un petit tirage gratuit ? » · pilier posture / limites · contexte : 1er contact en message privé
mer 25 · PROMO série « Pensé pour votre métier » : TAROLOGUE (guidance vocale) · V2 · fin = offre de Noël
ven 27 · CONSEIL guidance · V2 · guidance vocale de 12 minutes, 3 réglages · pilier suivi · contexte : après la séance
dim 29 · CONSEIL guidance · V3 · « Janvier se remplit en décembre » · pilier saison / organisation · contexte : avant les fêtes
Règles : vouvoiement, aucune personne, aucun superlatif, « Guide Pilote » écrit dans le texte lu, badge IA, une action montrée deux fois.
Usage : python3 reels/reels_specs_2026-11-23.py <clé> <voix.wav>   (clé : lun | mer | ven | dim)
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_tiktok_v3 as v3
import gen_v2 as v2

G = lambda a, b: f'{a} <span style="color:#E9C46A">{b}</span>'

SPECS = {
# ---------- lundi 23/11 · 18h · CONSEIL guidance · V3 ----------
"lun": {"gen": "v3", "slug": "lun-23_reel-petit-tirage-gratuit", "music": "elan", "scenes": [
  {"k": "hook", "static": True, "bg": "marine", "title": "«~Juste un petit tirage, gratuit~?~» [Vous dites quoi~?]", "size": 112, "top": 430,
   "sub": "Sans la vexer. Sans tout donner.", "subt": 2.0, "subtop": 1110,
   "say": "« Juste un petit tirage, gratuit ? » Vous répondez quoi, sans la vexer ?"},
  {"k": "words", "bg": "creme", "title": "Dire oui une fois, [c'est dire oui à chaque fois.]", "size": 118, "top": 520,
   "say": "Dire oui une fois, c'est souvent dire oui à chaque fois."},
  {"k": "num", "bg": "or", "n": "1", "title": "[Remerciez] sa confiance", "size": 112, "sub": "« Merci d'avoir pensé à moi. »",
   "say": "Un : remerciez sa confiance."},
  {"k": "num", "bg": "bleu", "n": "2", "title": "Posez [votre cadre]", "size": 120, "sub": "« Mes tirages sont des consultations à part entière. »",
   "say": "Deux : posez votre cadre. Mes tirages sont des consultations à part entière."},
  {"k": "num", "bg": "creme", "n": "3", "title": "Ouvrez [une porte]", "size": 120, "sub": "Votre prestation la plus courte, et le lien.",
   "say": "Trois : proposez votre prestation la plus courte, avec le lien."},
  {"k": "shot", "bg": "creme", "title": "Dans GuidPilot, [le lien fait le reste]", "size": 84, "img": "page_np.png", "stop": 560, "sh": 560,
   "imgstyle": "width:1420px;max-width:none;margin-left:-400px;margin-top:-116px", "ctop": 1180,
   "checks": ["Tarif et durée affichés", "Réservation et paiement en ligne"],
   "say": "Dans Guide Pilote, ce lien mène à votre page : tarif, durée, réservation."},
  {"k": "end", "bg": "marine", "title": G("Et vous, on vous demande", "des tirages gratuits&nbsp;?"),
   "save": "🔖 Enregistrez-la pour plus tard", "say": "Enregistrez-la. On vous en demande souvent ?"},
 ]},

# ---------- mercredi 25/11 · 18h · PROMO série « Pensé pour votre métier » · TAROLOGUE · V2 + offre de Noël ----------
"mer": {"gen": "v2", "slug": "mer-25_reel-tarologue-guidance-vocale", "music": "aube",
        "mid_cta": "1 an pour 99 € · <span>lien en bio</span>", "scenes": [
  {"k": "hook2", "title": "Tarologue&nbsp;: après le tirage, <span>où part votre guidance vocale&nbsp;?</span>", "size": 98, "sub": "WhatsApp, mail, pièce jointe… ?", "subt": 2.2,
   "say": "Tarologue : votre guidance vocale, vous l'envoyez où ? Sur WhatsApp ?"},
  {"k": "shot", "tag": "ÉTAPE 1", "title": "Elle choisit <span>et règle en ligne</span>", "img": "page_np.png", "W": 1100, "box": (310, 90, 960, 580),
   "say": "Un : elle réserve et règle sur votre page."},
  {"k": "x", "tag": "ÉTAPE 2", "title": "Vous préparez <span>au calme</span>", "top": 300, "extop": 680,
   "ex": ("list", ["Sa question, dans sa fiche", "Vos notes privées, à part", "Audio, texte, ou les deux"], "auto"), "ext": 0.6,
   "say": "Deux : vous préparez au calme. Vos notes restent privées."},
  {"k": "shot", "tag": "ÉTAPE 3", "title": "Elle la réécoute <span>dans son espace</span>", "img": "guid.png", "W": 1270, "box": (20, 232, 415, 480),
   "say": "Trois : l'audio et le texte l'attendent dans son espace sécurisé."},
  {"k": "quote", "title": "Un outil pensé pour votre métier, <span>pas un agenda de plus.</span>",
   "say": "Un outil pensé pour votre métier. Pas un agenda de plus."},
  {"k": "save", "offer": "1 an pour 99&nbsp;€", "q": "Offre de Noël · jusqu'au 31 décembre · lien en bio",
   "say": "Jusqu'au trente et un décembre : un an pour quatre-vingt-dix-neuf euros. Lien en bio."},
 ]},

# ---------- vendredi 27/11 · 18h · CONSEIL guidance · V2 ----------
"ven": {"gen": "v2", "slug": "ven-27_reel-guidance-vocale-12-minutes", "music": "lofi", "scenes": [
  {"k": "hook2", "title": "Votre guidance vocale dure 12 minutes. <span>Elle la réécoute vraiment&nbsp;?</span>", "size": 96, "sub": "3 réglages simples.", "subt": 2.2,
   "say": "Votre guidance vocale dure douze minutes. Elle la réécoute vraiment ?"},
  {"k": "step", "n": 1, "top": 430, "extop": 920, "size": 84, "title": "L'essentiel <span>dans la 1re minute</span>",
   "ex": ("card", "COMMENCEZ PAR", "« Ce que je retiens pour vous, c'est… »"), "ext": 1.0,
   "say": "Un : l'essentiel dès la première minute."},
  {"k": "step", "n": 2, "top": 430, "extop": 920, "size": 84, "title": "Trois parties, <span>annoncées</span>",
   "ex": ("vs", "Un long fil, d'une traite", "« D'abord… ensuite… pour finir… »", 0.9), "ext": 0.9,
   "say": "Deux : trois parties, annoncées à voix haute."},
  {"k": "step", "n": 3, "top": 430, "extop": 920, "size": 84, "title": "Trois lignes <span>écrites en plus</span>",
   "ex": ("card", "À RELIRE", "Les points clés, sans tout réécouter."), "ext": 1.0,
   "say": "Trois : trois lignes écrites en plus, pour relire sans tout réécouter."},
  {"k": "shot", "tag": "DANS GUIDPILOT", "title": "Audio et texte, <span>au même endroit</span>", "img": "guid.png", "W": 1270, "box": (20, 232, 415, 480),
   "say": "Dans Guide Pilote, l'audio et le texte l'attendent ensemble, dans son espace."},
  {"k": "save", "q": "Vos guidances vocales durent combien&nbsp;? 👇",
   "say": "Enregistrez-la. Vos guidances durent combien ?"},
 ]},

# ---------- dimanche 29/11 · 18h · CONSEIL guidance · V3 ----------
"dim": {"gen": "v3", "slug": "dim-29_reel-janvier-se-remplit-en-decembre", "music": "pilote", "scenes": [
  {"k": "hook", "static": True, "bg": "bleu", "title": "Janvier se remplit [en décembre.]", "size": 132, "top": 450,
   "sub": "3 choses à faire avant le 20.", "subt": 1.9, "subtop": 1090,
   "say": "Votre mois de janvier se remplit en décembre. Trois choses à faire avant le vingt."},
  {"k": "words", "bg": "creme", "title": "Début janvier, beaucoup veulent [reprendre rendez-vous.]", "size": 112, "top": 520,
   "say": "Début janvier, beaucoup veulent reprendre rendez-vous."},
  {"k": "num", "bg": "or", "n": "1", "title": "Ouvrez [vos créneaux] de janvier", "size": 108,
   "say": "Un : ouvrez dès maintenant vos créneaux de janvier."},
  {"k": "num", "bg": "marine", "n": "2", "title": "Annoncez [vos dates] de fermeture", "size": 108, "sub": "Sur votre page et en story.",
   "say": "Deux : annoncez vos dates de fermeture, sur votre page et en story."},
  {"k": "num", "bg": "creme", "n": "3", "title": "Écrivez aux clientes [de l'automne]", "size": 104, "sub": "Un message simple, sans promotion.",
   "say": "Trois : écrivez aux clientes de l'automne, sans promotion."},
  {"k": "tiles", "bg": "creme", "title": "Dans [GuidPilot]",
   "items": [("📅", "Créneaux de janvier ouverts"), ("🌙", "Réservation pendant vos congés"), ("✉️", "Rappel la veille"), ("💳", "Paiement en ligne")],
   "say": "Dans Guide Pilote, vos clientes réservent même pendant vos congés."},
  {"k": "end", "bg": "marine", "title": G("Vos créneaux de janvier", "sont ouverts&nbsp;?"),
   "save": "🔖 Enregistrez-la pour plus tard", "say": "Enregistrez-la. Vos créneaux de janvier sont ouverts ?"},
 ]},
}

if __name__ == "__main__":
    s = SPECS[sys.argv[1]]
    (v3 if s["gen"] == "v3" else v2).build(s, sys.argv[2])
    if s["gen"] == "v3":
        pass
