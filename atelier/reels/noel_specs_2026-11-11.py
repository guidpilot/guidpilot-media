"""Reels « Offre de Noël / offre fondatrice » — semaine du 11 au 15/11/2026 (lancement, en plus du lot déjà programmé).
Décision de Normane (09/11/2026) : 1 an de GuidPilot pour 99 € payés une fois (au lieu de 29 €/mois), jusqu'au 31/12/2026,
aucun prélèvement automatique ; ensuite renouvellement au tarif fondateur 149 €/an, mensuel 29 €, ou arrêt.
Exception validée aux règles habituelles : le prix (99 €) et la date (31 décembre) apparaissent à l'écran et dans la voix.
Toujours : vouvoiement, aucune personne, aucun superlatif, « Guide Pilote » prononcé, badge IA, CTA mi-vidéo + fin.
mer 11 · 10h · V3 (guidance) · ven 13 · 10h · V2 (guidance, captures démo) · sam 14 · 18h · V3 (thérapeutes).
Usage : python3 reels/noel_specs_2026-11-11.py <clé> <voix.wav>   (clé : mer | ven | sam)
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_tiktok_v3 as v3
import gen_v2 as v2

G = lambda a, b: f'{a} <span style="color:#E9C46A">{b}</span>'
MID = "1 an pour 99 € · <span>lien en bio</span>"

SPECS = {
# ---------- mercredi 11/11 · 10h · LANCEMENT · guidance · V3 · le « pourquoi » du fondateur ----------
"mer": {"gen": "v3", "slug": "mer-11_reel-noel-pourquoi-99", "music": "pilote", "mid_cta": MID, "scenes": [
  {"k": "hook", "static": True, "bg": "marine", "title": "Un an de GuidPilot pour [99 €.] Voilà pourquoi.", "size": 118, "top": 450,
   "sub": "Jusqu'au 31 décembre.", "subt": 1.8, "subtop": 1090,
   "say": "Un an de Guide Pilote pour quatre-vingt-dix-neuf euros. Voilà pourquoi."},
  {"k": "words", "bg": "creme", "title": "Nous cherchons nos [premières praticiennes.]", "size": 118, "top": 540,
   "say": "Nous cherchons nos premières praticiennes. Celles qui nous font confiance avant les avis et les témoignages."},
  {"k": "num", "bg": "or", "n": "1", "title": "Vous payez [une seule fois]", "sub": "Aucun prélèvement automatique, jamais.",
   "say": "Un : vous payez une seule fois. Aucun prélèvement automatique, jamais."},
  {"k": "num", "bg": "bleu", "n": "2", "title": "12 mois, [toutes les fonctions]", "size": 108, "sub": "Réservation, paiement, factures, espace client, avis.",
   "say": "Deux : douze mois, toutes les fonctions. Réservation, paiement, factures, espace client."},
  {"k": "num", "bg": "creme", "n": "3", "title": "Ensuite, [vous choisissez]", "sub": "Renouveler au tarif fondateur, passer au mensuel, ou arrêter.",
   "say": "Trois : ensuite, vous choisissez. Renouveler au tarif fondateur, passer au mensuel, ou arrêter."},
  {"k": "words", "bg": "marine", "title": "99 € au lieu de 348 €. [Jusqu'au 31 décembre.]", "size": 112, "top": 540,
   "say": "Quatre-vingt-dix-neuf euros au lieu de trois cent quarante-huit. Jusqu'au trente et un décembre."},
  {"k": "endad", "bg": "marine", "title": G("Un an pour organiser", "toute votre activité."), "top": 500,
   "pill": "🎁 1 an pour 99 €", "sub": "Jusqu'au 31 décembre · guidpilot.fr",
   "say": "Le lien est en bio. Guide Pilote, un outil pensé pour votre métier."},
 ]},

# ---------- vendredi 13/11 · 10h · PROMO · guidance · V2 captures démo · « le prix d'une consultation » ----------
"ven": {"gen": "v2", "slug": "ven-13_reel-noel-prix-consultation", "music": "elan", "mid_cta": MID, "scenes": [
  {"k": "hook2", "title": "Un an de GuidPilot pour le prix <span>d'une seule consultation.</span>", "size": 100,
   "sub": "99 €, payés une fois.", "subt": 2.0,
   "say": "Un an de Guide Pilote, pour le prix d'une seule consultation. Quatre-vingt-dix-neuf euros, payés une fois."},
  {"k": "shot", "tag": "PENDANT 12 MOIS", "title": "Vos clientes réservent <span>et règlent en ligne</span>", "img": "page_np.png", "W": 1100, "box": (310, 90, 960, 580),
   "say": "Pendant douze mois : vos clientes réservent et règlent en ligne, même à vingt-trois heures."},
  {"k": "shot", "tag": "PENDANT 12 MOIS", "title": "Vos guidances les attendent <span>dans leur espace</span>", "img": "guid.png", "W": 1270, "box": (430, 232, 820, 480),
   "say": "Vos guidances, écrites ou audio, les attendent dans leur espace sécurisé."},
  {"k": "shot", "tag": "PENDANT 12 MOIS", "title": "Factures et avis, <span>sans y penser</span>", "img": "avis.png", "W": 1270, "box": (20, 150, 930, 310),
   "say": "Les factures se créent seules. Les avis rejoignent votre page."},
  {"k": "quote", "title": "Aucun prélèvement automatique. <span>Ensuite, vous choisissez.</span>",
   "say": "Aucun prélèvement automatique. Au bout d'un an, vous choisissez : renouveler, passer au mensuel, ou arrêter."},
  {"k": "save", "offer": '1 an pour <span style="color:#E9C46A">99 €</span>', "q": "Jusqu'au 31 décembre · lien en bio",
   "say": "Jusqu'au trente et un décembre. Le lien est en bio."},
 ]},

# ---------- samedi 14/11 · 18h · PROMO · thérapeutes · V3 · « janvier, arriver équipée » ----------
"sam": {"gen": "v3", "slug": "sam-14_reel-noel-janvier-equipee", "music": "aube", "mid_cta": MID, "scenes": [
  {"k": "hook", "static": True, "bg": "or", "title": "En janvier, vous remettez votre activité [à plat.]", "size": 118, "top": 450,
   "sub": "Et si cette fois vous arriviez équipée ?", "subt": 1.9, "subtop": 1090,
   "say": "En janvier, vous remettez votre activité à plat. Et si cette fois, vous arriviez équipée ?"},
  {"k": "notifs", "bg": "creme", "title": "Dès la [première semaine]", "clock": "21:40", "date": "lundi 5 janvier",
   "items": [("📅", "Réservation", "Séance de sophrologie · jeudi 10 h", "Réservée depuis votre page"),
             ("💳", "Paiement", "Paiement reçu", "Facture n° 2027-001 créée"),
             ("🔔", "Rappel", "Rappel envoyé à votre cliente", "Lien de visio inclus")],
   "say": "Dès la première semaine : elle réserve depuis votre page, elle règle, la facture est créée, le rappel part tout seul."},
  {"k": "words", "bg": "marine", "title": "Le prix ? Celui [d'une seule séance.]", "size": 128, "top": 560,
   "say": "Le prix ? Celui d'une seule séance."},
  {"k": "tiles", "bg": "bleu", "title": "[99 €] pour 12 mois",
   "items": [("🎁", "Payé une fois"), ("🔒", "Aucun prélèvement auto"), ("📅", "Jusqu'au 31 décembre"), ("🔁", "Ensuite, vous choisissez")],
   "say": "Quatre-vingt-dix-neuf euros pour douze mois. Payés une fois. Aucun prélèvement automatique. Ensuite, vous choisissez."},
  {"k": "endad", "bg": "marine", "title": G("Une année sereine", "commence maintenant."), "top": 500,
   "pill": "🎁 1 an pour 99 €", "sub": "Jusqu'au 31 décembre · guidpilot.fr",
   "say": "Jusqu'au trente et un décembre, lien en bio. Guide Pilote, pensé pour les thérapeutes."},
 ]},
}

if __name__ == "__main__":
    s = SPECS[sys.argv[1]]
    (v3 if s["gen"] == "v3" else v2).build(s, sys.argv[2])
