"""Stories FACEBOOK (23 au 29/11/2026) — reprise des stories Instagram de la semaine (specs_2026-11-23.py), adaptées à Facebook.
- Question / conseil / fonction / offre de Noël sans « lien en bio » : images Instagram reprises telles quelles
  (lun-23 12h30, mer-25 12h30, jeu-26 12h30 et 16h, ven-27 12h30 et 16h, sam-28 16h, dim-29 12h30 et 16h).
- Mot-clé THÉRAPEUTE (mar-24, sam-28 à 12h30) : variantes sans mot-clé, même accroche → offre d'essai + guidpilot.fr.
- Offre de Noël avec « lien en bio » (lun-23, mar-24, mer-25 à 16h) : variantes avec guidpilot.fr
  (prix 99 € et date du 31 décembre autorisés pour l'offre de Noël — exception du 09/11/2026, comme sur Instagram).
- Teasers lun-23, mer-25, ven-27 (Reels aussi publiés sur la page le même jour) : « Nouvelle vidéo sur notre page ».
- Teasers mar-24, jeu-26, sam-28 (posts Instagram NON publiés sur la page) : remplacés par un conseil express."""
OFFRE = "14 jours gratuits, sans carte bancaire · guidpilot.fr"
VIDEO = "Nouvelle vidéo sur notre page 👆"
NOEL = "Offre de Noël 🎁"

STORIES = [
 {"name": "fb_lun-23_1600_noel-5-semaines", "type": "tip", "pill": NOEL,
  "title": "L'offre de Noël, c'est [jusqu'au 31 décembre]", "size": 96,
  "sub": "1 an de GuidPilot pour 99 €, payé une fois, aucun prélèvement. Sur guidpilot.fr/offre-fondatrice"},
 {"name": "fb_lun-23_2000_teaser-petit-tirage", "type": "teaser", "pill": "Nouvelle vidéo",
  "title": "« Juste un petit tirage, gratuit ? » [Vous dites quoi ?]", "size": 92, "sub": "3 temps pour répondre.", "cta": VIDEO},

 {"name": "fb_mar-24_1230_cabinet-therapeute", "type": "teaser", "kick": "Sophrologue, hypnothérapeute, praticienne Reiki ?",
  "title": "La veille, votre cliente reçoit [son rappel par e-mail], sans que vous l'écriviez.", "size": 80, "cta": OFFRE},
 {"name": "fb_mar-24_1600_noel-factures", "type": "feature", "pill": NOEL, "title": "Vos factures [numérotées toutes seules,] pendant 12 mois", "size": 88,
  "sub": "1 an de GuidPilot pour 99 €, jusqu'au 31 décembre, sur guidpilot.fr",
  "img": "kit/assets/dash_np.png", "W": 1270, "box": (330, 430, 920, 530), "maxh": 300},
 {"name": "fb_mar-24_2000_conseil-premiere-seance", "type": "tip", "pill": "Astuce cabinet",
  "title": "Première séance : envoyez [l'adresse, l'heure et la durée] la veille", "size": 88,
  "sub": "Votre cliente arrive sereine, vous commencez à l'heure."},

 {"name": "fb_mer-25_1600_noel-une-soiree-de-plus", "type": "question", "pill": NOEL,
  "title": "Une soirée de plus par semaine, [vous en feriez quoi ?]", "size": 96,
  "note": "Répondez à cette story. 1 an pour 99 €, sur guidpilot.fr"},
 {"name": "fb_mer-25_2000_teaser-tarologue", "type": "teaser", "pill": "Nouvelle vidéo",
  "title": "Tarologue : où part [votre guidance vocale ?]", "size": 100, "sub": "Pensé pour votre métier.", "cta": VIDEO},

 {"name": "fb_jeu-26_2000_conseil-bon-cadeau", "type": "tip", "pill": "Astuce Noël",
  "title": "Bon cadeau : écrivez [la durée et la date de validité]", "size": 92,
  "sub": "« Séance de 45 min, valable jusqu'au 31 mars. » Aucun malentendu au printemps."},

 {"name": "fb_ven-27_2000_teaser-vocal-12-minutes", "type": "teaser", "pill": "Nouvelle vidéo",
  "title": "Votre guidance vocale dure [12 minutes ?]", "size": 104, "sub": "3 réglages simples.", "cta": VIDEO},

 {"name": "fb_sam-28_1230_cabinet-therapeute", "type": "teaser", "kick": "Hypnothérapeute, magnétiseuse, coach de vie ?",
  "title": "L'audio à réécouter, [rangé dans l'espace de votre cliente].", "size": 84, "cta": OFFRE},
 {"name": "fb_sam-28_2000_conseil-tester-outil", "type": "tip", "pill": "Astuce outil",
  "title": "Avant de choisir un outil, [réservez-vous un créneau]", "size": 92,
  "sub": "Faites le parcours comme une cliente. Vous verrez tout de suite ce qui coince."},
]
