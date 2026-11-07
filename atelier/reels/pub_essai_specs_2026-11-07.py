"""Publicités Meta « Essai GuidPilot » (campagne essai_2026_11), 3 vidéos 9:16, style V3 (gen_tiktok_v3.py).
Scripts validés par Normane le 07/11/2026 (15 h 36). Voix Claire. Aucune personne, captures du compte démo
(dash_np / agenda : sans photo), pas de prix, pas d'offre de lancement (règle communication du 22/10/2026).
Usage : python3 reels/pub_essai_specs_2026-11-07.py <clé> <voix.wav>
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_tiktok_v3 as v3

OFFER = "14 jours gratuits · <span>sans carte bancaire</span>"

SPECS = {
"A": {"slug": "pub-essai-A-outils", "music": "elan", "mid_cta": OFFER,
 "scenes": [
  {"k": "hook", "static": True, "bg": "marine", "title": "Cinq outils pour [une seule] consultation.", "size": 124, "top": 440,
   "sub": "Vous les reconnaissez ?", "subt": 1.6, "subtop": 1080,
   "say": "Cinq outils pour une seule consultation. Vous les reconnaissez ?"},
  {"k": "tiles", "bg": "creme", "title": "Le soir, [après vos séances]", "size": 84,
   "items": [("📅", "L'agenda"), ("🎥", "Le lien visio"), ("€", "Le paiement"), ("🧾", "La facture à la main")],
   "say": "L'agenda. Le lien visio. Le paiement. La facture. L'avis à demander. Et tout ça, le soir, après vos séances."},
  {"k": "shot", "bg": "bleu", "title": "Avec GuidPilot, [un seul espace]", "size": 84, "img": "dash_np.png", "stop": 600,
   "checks": ["Réservation en ligne", "Paiement et facture"], "ctop": 1150,
   "say": "Avec GuidPilot, votre cliente réserve, paie, reçoit son lien et sa facture. Vous n'avez rien à ressaisir."},
  {"k": "endad", "bg": "marine", "title": "Un outil conçu pour les thérapeutes et les praticiens <span style=\"color:#E9C46A\">en guidance.</span>",
   "say": "Un outil conçu pour les thérapeutes et les praticiens en guidance. Quatorze jours gratuits, sans carte bancaire."},
 ]},
"B": {"slug": "pub-essai-B-temps", "music": "pilote", "mid_cta": OFFER,
 "scenes": [
  {"k": "hook", "static": True, "bg": "bleu", "title": "« Je vous fais le virement [ce soir.] »", "size": 124, "top": 440,
   "sub": "Vous connaissez la suite.", "subt": 1.7, "subtop": 1080,
   "say": "« Je vous fais le virement ce soir. » Vous connaissez la suite."},
  {"k": "notifs", "bg": "marine", "title": "Cinq messages pour [un rendez-vous]", "size": 84, "clock": "23:47", "date": "jeudi soir",
   "items": [("💬", "Message", "Vous auriez un créneau jeudi ?", "Plutôt 18h30… le lien visio c'est où ?"),
             ("💬", "Message", "Et le règlement ?", "Je vous fais le virement ce soir…"),
             ("⏳", "Toujours pas confirmé", "Séance de jeudi", "5 messages · 0 paiement")],
   "say": "Cinq messages pour caler un rendez-vous. Un rappel pour le règlement. Et la séance n'est toujours pas confirmée."},
  {"k": "notifs", "bg": "creme", "title": "Avec GuidPilot, [elle réserve seule]", "size": 84, "clock": "21:14", "date": "jeudi 13 novembre",
   "items": [("✓", "GuidPilot", "Nouveau rendez-vous", "Jeudi 18:30 · réglé en ligne"),
             ("▶", "E-mail · GuidPilot", "Lien de la séance envoyé", "Rappel programmé la veille")],
   "say": "Avec GuidPilot, votre cliente choisit son créneau et règle en réservant. Le lien de visio et le rappel partent tout seuls."},
  {"k": "endad", "bg": "marine", "title": "Vous gardez votre énergie <span style=\"color:#E9C46A\">pour la séance.</span>",
   "say": "Vous gardez votre énergie pour la séance. Quatorze jours gratuits, sans carte bancaire."},
 ]},
"C": {"slug": "pub-essai-C-2027", "music": "aube", "mid_cta": OFFER,
 "scenes": [
  {"k": "hook", "static": True, "bg": "creme", "title": "Et si janvier commençait [sans la pile] de factures ?", "size": 118, "top": 430,
   "say": "Et si janvier commençait sans la pile de factures ?"},
  {"k": "tiles", "bg": "marine", "title": "Cette année [encore]", "size": 92,
   "items": [("💬", "Les rendez-vous par messages"), ("🔍", "Les paiements à vérifier"), ("🧾", "Les factures à la main"), ("🌙", "Le soir, après la dernière séance")],
   "say": "Cette année encore, les rendez-vous par messages, les paiements à vérifier, les factures faites à la main."},
  {"k": "shot", "bg": "bleu", "title": "Avec GuidPilot, [tout au même endroit]", "size": 80, "img": "dash_np.png", "stop": 600,
   "checks": ["Agenda rempli", "Paiement reçu", "Facture envoyée"], "ctop": 1120,
   "say": "Avec GuidPilot, tout est au même endroit : agenda, réservation, espace client, paiements, factures, avis."},
  {"k": "endad", "bg": "marine", "title": "Commencez 2027 avec un cabinet <span style=\"color:#E9C46A\">organisé.</span>",
   "say": "Quatorze jours suffisent pour tout installer. Commencez 2027 avec un cabinet organisé. Gratuit, sans carte bancaire."},
 ]},
}

if __name__ == "__main__":
    v3.build(SPECS[sys.argv[1]], sys.argv[2])
