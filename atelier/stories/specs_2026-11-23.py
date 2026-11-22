"""Stories Instagram de la semaine du 23 au 29/11/2026 (lot automatique du 22/11) — 13 stories + 7 « Offre de Noël » à 16h00.
12h30 : rotation question / mot-clé THÉRAPEUTE (mar, sam) / conseil / fonction, jamais le même type deux jours de suite ;
20h00 : teaser du post du jour (lun → sam). 16h00 : offre de Noël (prix 99 € et date du 31 décembre autorisés — exception du 09/11/2026).
Règles : vouvoiement, aucune personne représentée, aucun superlatif, jamais « Répondez GUIDANCE à cette story »."""
REEL = "Nouveau Reel sur le profil 👆"
POST = "Nouveau post sur le profil 👆"
NOEL = "Offre de Noël 🎁"

STORIES = [
 {"name": "lun-23_1230_question-soir-ou-matin", "type": "question", "pill": "Petite question",
  "title": "Vos clientes vous écrivent plutôt [le soir ou le matin ?]", "size": 96,
  "note": "Répondez à cette story, je lis tout."},
 {"name": "lun-23_1600_noel-5-semaines", "type": "tip", "pill": NOEL,
  "title": "L'offre de Noël, c'est [jusqu'au 31 décembre]", "size": 96,
  "sub": "1 an de GuidPilot pour 99 €, payé une fois, aucun prélèvement. Lien en bio."},
 {"name": "lun-23_2000_teaser-petit-tirage", "type": "teaser", "pill": "Nouveau Reel",
  "title": "« Juste un petit tirage, gratuit ? » [Vous dites quoi ?]", "size": 92, "sub": "3 temps pour répondre.", "cta": REEL},

 {"name": "mar-24_1230_mot-cle-therapeute", "type": "keyword", "kw": "THÉRAPEUTE", "kick": "Sophrologue, hypnothérapeute, praticienne Reiki ?",
  "title": "La veille, votre cliente reçoit [son rappel par e-mail], sans que vous l'écriviez.", "size": 80},
 {"name": "mar-24_1600_noel-factures", "type": "feature", "pill": NOEL, "title": "Vos factures [numérotées toutes seules,] pendant 12 mois", "size": 88,
  "sub": "1 an de GuidPilot pour 99 €, jusqu'au 31 décembre. Lien en bio.",
  "img": "kit/assets/dash_np.png", "W": 1270, "box": (330, 430, 920, 530), "maxh": 300},
 {"name": "mar-24_2000_teaser-premiere-seance", "type": "teaser", "pill": "Nouveau post",
  "title": "Première séance : [5 infos] à envoyer avant", "size": 100, "sub": "La checklist à enregistrer.", "cta": POST},

 {"name": "mer-25_1230_conseil-delai-livraison", "type": "tip", "pill": "Astuce guidance",
  "title": "Annoncez le délai de votre guidance [avant qu'elle paie]", "size": 92,
  "sub": "« Votre guidance vous attend sous 48 h. » Elle n'a plus besoin de vous relancer."},
 {"name": "mer-25_1600_noel-une-soiree-de-plus", "type": "question", "pill": NOEL,
  "title": "Une soirée de plus par semaine, [vous en feriez quoi ?]", "size": 96,
  "note": "Répondez à cette story. 1 an pour 99 €, lien en bio."},
 {"name": "mer-25_2000_teaser-tarologue", "type": "teaser", "pill": "Nouveau Reel",
  "title": "Tarologue : où part [votre guidance vocale ?]", "size": 100, "sub": "Pensé pour votre métier.", "cta": REEL},

 {"name": "jeu-26_1230_fonction-avis", "type": "feature", "pill": "Dans GuidPilot", "title": "Les avis de vos clientes [s'affichent sur votre page]", "size": 88,
  "sub": "Vous envoyez la demande depuis votre espace, au bon moment.",
  "img": "kit/assets/avis.png", "W": 1270, "box": (20, 150, 930, 310), "maxh": 420},
 {"name": "jeu-26_1600_noel-cadeau-2027", "type": "tip", "pill": NOEL,
  "title": "Un cadeau qui sert [tous les jours de 2027]", "size": 100,
  "sub": "1 an de GuidPilot pour 99 €, payé une fois. Jusqu'au 31 décembre."},
 {"name": "jeu-26_2000_teaser-seance-offerte", "type": "teaser", "pill": "Nouveau post",
  "title": "« Je peux offrir une séance ? » [Voici comment.]", "size": 96, "sub": "Le mini-guide de Noël.", "cta": POST},

 {"name": "ven-27_1230_question-temps-messages", "type": "question", "pill": "Petite question",
  "title": "Combien de temps passez-vous [sur vos messages] chaque jour ?", "size": 92,
  "note": "Une estimation suffit. Répondez à cette story."},
 {"name": "ven-27_1600_noel-donnees", "type": "tip", "pill": NOEL,
  "title": "Vos données [restent à vous]", "size": 108,
  "sub": "Après l'année, même si vous arrêtez, elles restent consultables. 1 an pour 99 €, jusqu'au 31 décembre."},
 {"name": "ven-27_2000_teaser-vocal-12-minutes", "type": "teaser", "pill": "Nouveau Reel",
  "title": "Votre guidance vocale dure [12 minutes ?]", "size": 104, "sub": "3 réglages simples.", "cta": REEL},

 {"name": "sam-28_1230_mot-cle-therapeute", "type": "keyword", "kw": "THÉRAPEUTE", "kick": "Hypnothérapeute, magnétiseuse, coach de vie ?",
  "title": "L'audio à réécouter, [rangé dans l'espace de votre cliente].", "size": 84},
 {"name": "sam-28_1600_noel-espace-client", "type": "feature", "pill": NOEL, "title": "L'espace privé de vos clientes, [pendant 12 mois]", "size": 88,
  "sub": "Comptes rendus écrits ou vocaux, rendez-vous, factures. 1 an pour 99 €, jusqu'au 31 décembre.",
  "img": "kit/assets/guid.png", "W": 1270, "box": (20, 232, 415, 480), "maxh": 460},
 {"name": "sam-28_2000_teaser-hypnotherapeute", "type": "teaser", "pill": "Nouveau post",
  "title": "Hypnothérapeute : [6 questions] avant de choisir votre outil", "size": 92, "sub": "La checklist à enregistrer.", "cta": POST},

 {"name": "dim-29_1230_conseil-calendrier-avent", "type": "tip", "pill": "Calendrier de l'Avent 🎄",
  "title": "Mardi 1er décembre : [la 1re astuce]", "size": 104,
  "sub": "24 astuces en stories, une par jour. Abonnez-vous pour ne rien manquer."},
 {"name": "dim-29_1600_noel-payer-une-fois", "type": "tip", "pill": NOEL,
  "title": "Payé une fois, [tranquille pour l'année]", "size": 100,
  "sub": "Aucun abonnement à surveiller, aucun prélèvement. 99 €, jusqu'au 31 décembre."},
]
