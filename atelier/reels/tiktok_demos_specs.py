"""TikTok — 6 démos « Comment gagner du temps avec GuidPilot : <action> » (lot du 25 au 27/10/2026).
Rendu : python3 reels/gen_tiktok_demos.py <clé> <voix.wav>  (réutilise gen_v2.py → gen_promos.py → gen_conseils.py).
⚠️ TikTok : aucun des mots guidance, tarot, tarologue, voyance, voyante, médium, cartomancie, divinatoire
(voix, écran, légende, hashtags). Les captures sont recadrées pour exclure « Guidance & Astrologie »,
« Guidances à livrer », « Créer une guidance », « Astrologie & Tarot » et la photo du profil démo.
Fonctions vérifiées le 21/10/2026 (base tcxhdtleencjqdphtgqu + specs tutos t06, t12, t13, t16) :
- rappel de paiement : RPC send_payment_reminder (e-mail avec montant + n° de facture, notification espace client, 1 fois / 24 h) ;
- avis : « Demander un avis » sur un rendez-vous réalisé → lien unique à copier ou e-mail prêt (pas d'envoi automatique), « À relancer » après 3 jours ;
- forfaits : session_packs (prestation, nb de séances, prix, validité), vente en ligne ou au cabinet, séance décomptée au paiement avec le code ;
- factures : créées à la réservation, numéro qui se suit (invoice_counters), « Marquer comme payée » + mode (espèces, chèque, virement, terminal).
"""

FIN = "Testez Guide Pilote gratuitement pendant quatorze jours, sans carte bancaire."
SUB = "Comment gagner du temps avec GuidPilot"

SPECS = {
"tt1": {"slug": "tt1-journee-coup-doeil", "music": "aube", "file": "01-votre-journee-d-un-coup-d-oeil.mp4",
 "caption": "Comment gagner du temps avec GuidPilot : votre journée d'un coup d'œil. #pourtoi #praticien #therapeute #organisation",
 "scenes": [
  {"k": "hook2", "title": "Votre journée, <span>d'un coup d'œil</span>", "sub": SUB, "subt": 0.9,
   "say": "Votre journée de praticienne, d'un seul coup d'œil."},
  {"k": "shot", "tag": "LE MATIN", "title": "Vos <span>rendez-vous</span> du jour", "img": "dash_np.png", "W": 1270, "box": (15, 145, 315, 335),
   "say": "En ouvrant Guide Pilote le matin, vous voyez d'abord vos rendez-vous du jour."},
  {"k": "shot", "title": "Votre <span>agenda du jour</span>", "img": "dash_np.png", "W": 1270, "box": (40, 600, 560, 845),
   "say": "Juste en dessous, l'agenda du jour : l'heure, la cliente et la séance prévue."},
  {"k": "shot", "title": "Ce qui reste <span>à encaisser</span>", "img": "dash_np.png", "W": 1270, "box": (30, 372, 640, 535),
   "say": "Le suivi financier vous montre ce qui est encaissé ce mois-ci, et ce qui reste à encaisser."},
  {"k": "shot", "title": "Les <span>actions rapides</span>", "img": "dash_np.png", "W": 1270, "box": (840, 590, 1225, 818),
   "say": "Et les actions rapides : planifier un rendez-vous ou ajouter une cliente, en un clic."},
  {"k": "x", "tag": "CHAQUE MATIN", "title": "Une seule page, <span>pas trois outils</span>", "top": 360, "extop": 760,
   "ex": ("list", ["Vos rendez-vous", "Vos encaissements", "Vos raccourcis"], "auto"), "ext": 0.6,
   "say": "Plus besoin d'ouvrir trois outils pour savoir où vous en êtes."},
  {"k": "brand", "title": "14 jours gratuits, <span>sans carte bancaire</span>", "say": FIN},
 ]},
"tt2": {"slug": "tt2-demande-avis", "music": "elan", "file": "02-demander-un-avis-apres-la-seance.mp4",
 "caption": "Comment gagner du temps avec GuidPilot : la demande d'avis après la séance. #pourtoi #praticien #therapeute #avisclients",
 "scenes": [
  {"k": "hook2", "title": "Vos clientes sont ravies. <span>Qui le sait&nbsp;?</span>", "size": 112, "sub": SUB, "subt": 1.2,
   "say": "Vos clientes sont ravies de leur séance. Mais qui le sait ?"},
  {"k": "x", "tag": "APRÈS LA SÉANCE", "title": "Un clic sur <span>Demander un avis</span>", "top": 330, "extop": 760,
   "ex": ("button", "DEPUIS LE RENDEZ-VOUS RÉALISÉ", "Demander un avis", "✓ Lien personnel créé"), "ext": 0.8,
   "say": "Avec Guide Pilote, après la séance, ouvrez le rendez-vous et cliquez sur Demander un avis."},
  {"k": "x", "tag": "UN LIEN UNIQUE", "title": "Par message <span>ou par e&#8209;mail</span>", "top": 330, "extop": 800,
   "ex": ("card", "VOTRE CLIENTE", "Elle clique sur le lien, puis laisse sa note et son commentaire."), "ext": 0.8,
   "say": "Un lien personnel est créé : copiez-le dans un message, ou ouvrez un e-mail déjà rédigé."},
  {"k": "shot", "title": "Suivez <span>vos retours</span>", "img": "avis.png", "W": 1270, "box": (10, 140, 620, 315), "to": (630, 140, 1240, 315),
   "say": "Dans le menu Avis, suivez votre note moyenne, et les demandes à relancer au bout de trois jours."},
  {"k": "shot", "tag": "SUR VOTRE PAGE", "title": "Votre note <span>rassure</span>", "img": "page_np.png", "W": 1100, "box": (320, 352, 860, 585),
   "say": "Et chaque avis publié s'affiche sur votre page de réservation, pour rassurer vos futures clientes."},
  {"k": "brand", "title": "14 jours gratuits, <span>sans carte bancaire</span>", "say": FIN},
 ]},
"tt3": {"slug": "tt3-forfait-seances", "music": "cocon", "file": "03-vendre-un-forfait-de-seances.mp4",
 "caption": "Comment gagner du temps avec GuidPilot : le forfait de séances décomptées. #pourtoi #therapeute #sophrologue #reiki",
 "scenes": [
  {"k": "hook2", "title": "Un suivi en 5 séances&nbsp;? <span>Vendez un forfait.</span>", "size": 108, "sub": SUB, "subt": 1.3,
   "say": "Vous suivez vos clientes sur plusieurs séances ? Proposez un forfait."},
  {"k": "x", "tag": "AVANT", "title": "Des comptes <span>sur un carnet</span>", "top": 330, "extop": 720,
   "ex": ("list", ["!Un paiement à chaque séance", "!Le décompte à la main", "!« Il m'en reste combien&nbsp;? »"], "auto"), "ext": 0.6,
   "say": "Fini le paiement à chaque séance, et le décompte tenu à la main."},
  {"k": "x", "tag": "DANS GUIDPILOT", "title": "Créez <span>votre forfait</span>", "top": 330, "extop": 720,
   "ex": ("list", ["Une prestation", "Un nombre de séances", "Un prix total", "Une durée de validité"], "auto"), "ext": 0.6,
   "say": "Dans Guide Pilote, créez votre forfait : la prestation, le nombre de séances, le prix total et la durée de validité."},
  {"k": "x", "tag": "EN LIGNE OU AU CABINET", "title": "Votre cliente <span>l'achète</span>", "top": 330, "extop": 800,
   "ex": ("card", "COMME ELLE PRÉFÈRE", "Sur votre page avec le paiement en ligne, ou directement au cabinet."), "ext": 0.8,
   "say": "Votre cliente l'achète sur votre page, ou directement au cabinet."},
  {"k": "phone", "title": "Les séances <span>se décomptent</span>", "size": 70,
   "items": [("🎟️", "Mes cartes et forfaits"), ("✓", "2 séances utilisées"), ("⏳", "3 séances restantes")],
   "say": "À chaque séance réglée avec le forfait, une séance est décomptée. Et votre cliente voit ce qu'il lui reste, dans son espace."},
  {"k": "brand", "title": "14 jours gratuits, <span>sans carte bancaire</span>", "say": FIN},
 ]},
"tt4": {"slug": "tt4-rappel-paiement", "music": "lofi", "file": "04-relancer-un-paiement-en-un-clic.mp4",
 "caption": "Comment gagner du temps avec GuidPilot : le rappel de paiement en un clic. #pourtoi #praticien #therapeute #independante",
 "scenes": [
  {"k": "hook2", "title": "La séance est faite. <span>Pas le paiement.</span>", "sub": SUB, "subt": 1.1,
   "say": "La séance est faite. Le paiement, pas encore."},
  {"k": "x", "tag": "AVANT", "title": "Le message <span>gênant</span>", "top": 330, "extop": 760,
   "ex": ("chat", [("out", "Bonjour… désolée de vous déranger, c'est pour le règlement 😬")], 0.8), "ext": 0.6,
   "say": "Plus besoin d'écrire vous-même ce message gênant."},
  {"k": "x", "tag": "AVEC GUIDPILOT", "title": "Un rappel <span>en un clic</span>", "top": 330, "extop": 760,
   "ex": ("button", "DEPUIS LE RENDEZ-VOUS", "Envoyer un rappel de paiement", "✓ Rappel envoyé par e-mail"), "ext": 0.8,
   "say": "Dans Guide Pilote, ouvrez le rendez-vous, et cliquez sur Envoyer un rappel de paiement."},
  {"k": "x", "title": "Votre cliente <span>est prévenue</span>", "top": 360, "extop": 720,
   "ex": ("list", ["Un e-mail avec le montant", "Le numéro de facture", "Une notification dans son espace"], "auto"), "ext": 0.6,
   "say": "Votre cliente reçoit un e-mail avec le montant et le numéro de facture, et une notification dans son espace."},
  {"k": "shot", "title": "Suivez <span>le reste à encaisser</span>", "img": "dash_np.png", "W": 1270, "box": (30, 372, 640, 535),
   "say": "Ensuite, sur votre tableau de bord, vous suivez ce qui reste à encaisser."},
  {"k": "brand", "title": "14 jours gratuits, <span>sans carte bancaire</span>", "say": FIN},
 ]},
"tt5": {"slug": "tt5-facture-automatique", "music": "pilote", "file": "05-la-facture-qui-se-cree-toute-seule.mp4",
 "caption": "Comment gagner du temps avec GuidPilot : la facture numérotée qui se crée toute seule. #pourtoi #praticien #therapeute #facturation",
 "scenes": [
  {"k": "hook2", "title": "Encore une facture <span>à faire ce soir&nbsp;?</span>", "sub": SUB, "subt": 1.1,
   "say": "Encore une facture à faire ce soir, après vos séances ?"},
  {"k": "x", "tag": "À LA RÉSERVATION", "title": "La facture <span>se crée toute seule</span>", "top": 330, "extop": 800,
   "ex": ("card", "NUMÉROTÉE AUTOMATIQUEMENT", "Chaque réservation crée sa facture, avec un numéro qui se suit."), "ext": 0.8,
   "say": "Dans Guide Pilote, chaque réservation crée sa facture automatiquement, avec un numéro qui se suit."},
  {"k": "x", "tag": "PAIEMENT EN LIGNE", "title": "Elle passe <span>à Payée</span>", "top": 360, "extop": 760,
   "ex": ("list", ["Réglée en ligne par la cliente", "Facture marquée Payée", "Rien à faire de votre côté"], "auto"), "ext": 0.6,
   "say": "Si votre cliente paie en ligne, la facture passe toute seule à Payée."},
  {"k": "x", "tag": "AU CABINET", "title": "Espèces <span>ou chèque&nbsp;?</span>", "top": 330, "extop": 760,
   "ex": ("button", "ESPÈCES, CHÈQUE, VIREMENT…", "Marquer comme payée", "✓ Mode et date enregistrés"), "ext": 0.8,
   "say": "Réglé en espèces ou par chèque ? Ouvrez la facture, cliquez sur Marquer comme payée, et choisissez le mode de règlement."},
  {"k": "x", "tag": "ESPACE CLIENT", "title": "Elle la retrouve <span>en PDF</span>", "top": 330, "extop": 800,
   "ex": ("card", "SANS VOUS LA REDEMANDER", "Votre cliente retrouve sa facture dans son espace."), "ext": 0.8,
   "say": "La facture se télécharge en PDF, et votre cliente la retrouve dans son espace."},
  {"k": "brand", "title": "14 jours gratuits, <span>sans carte bancaire</span>", "say": FIN},
 ]},
"tt6": {"slug": "tt6-page-reservation-bio", "music": "elan", "file": "06-votre-page-de-reservation-en-bio.mp4",
 "caption": "Comment gagner du temps avec GuidPilot : votre page de réservation en lien en bio. #pourtoi #praticien #therapeute #lienenbio",
 "scenes": [
  {"k": "hook2", "title": "Arrêtez d'envoyer <span>vos créneaux</span> par message", "size": 112, "sub": SUB, "subt": 1.3,
   "say": "Arrêtez d'envoyer vos créneaux par message."},
  {"k": "x", "tag": "INSTAGRAM · TIKTOK", "title": "Un seul lien <span>dans votre bio</span>", "top": 330, "extop": 800,
   "ex": ("card", "VOTRE BIO", "Le lien de votre page de réservation GuidPilot."), "ext": 0.8,
   "say": "Avec Guide Pilote, vous avez une page de réservation, et un seul lien à mettre dans votre bio Instagram ou TikTok."},
  {"k": "shot", "title": "Elle découvre <span>votre page</span>", "img": "page_np.png", "W": 1100, "box": (320, 352, 860, 585),
   "say": "Votre future cliente découvre votre page et vos avis, puis clique sur Prendre rendez-vous."},
  {"k": "x", "tag": "EN AUTONOMIE", "title": "Elle réserve <span>seule</span>", "top": 360, "extop": 720,
   "ex": ("list", ["Elle choisit sa séance", "Elle choisit un créneau libre", "Elle réserve, même le soir"], "auto"), "ext": 0.6,
   "say": "Elle choisit sa séance et un créneau libre, quand elle veut, même le soir."},
  {"k": "x", "tag": "DE VOTRE CÔTÉ", "title": "Tout <span>arrive au bon endroit</span>", "top": 360, "extop": 720,
   "ex": ("list", ["Le rendez-vous dans votre agenda", "La fiche cliente créée", "La facture prête"], "auto"), "ext": 0.6,
   "say": "Et chez vous, le rendez-vous arrive dans l'agenda, avec la fiche cliente et la facture."},
  {"k": "brand", "title": "14 jours gratuits, <span>sans carte bancaire</span>", "say": FIN},
 ]},
}

INTERDITS = ["guidance", "tarot", "tarolog", "voyan", "médium", "medium", "cartomanc", "divinatoire"]


def texte(key):
    return " ".join(sc["say"] for sc in SPECS[key]["scenes"])


if __name__ == "__main__":
    import re
    for k, s in SPECS.items():
        t = texte(k)
        blob = (str(s) ).lower()
        bad = [w for w in INTERDITS if w in blob]
        print(k, len(t.split()), "mots", len(t), "car.", "INTERDITS:" if bad else "ok", bad or "")
