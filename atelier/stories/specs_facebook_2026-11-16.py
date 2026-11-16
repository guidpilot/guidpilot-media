"""Stories FACEBOOK (16 au 22/11/2026) — reprise des stories Instagram de la semaine (specs_2026-11-16.py), adaptées à Facebook.
- Question / conseil / fonction / offre de Noël sans « lien en bio » : images Instagram reprises telles quelles
  (lun-16 12h30, mar-17 16h, mer-18 12h30 et 16h, jeu-19 12h30 et 16h, ven-20 12h30 et 16h, dim-22 12h30 et 16h).
- Mot-clé THÉRAPEUTE (mar-17, sam-21 à 12h30) : variantes sans mot-clé → offre d'essai + guidpilot.fr.
- Offre de Noël avec « lien en bio » (lun-16, sam-21 à 16h) : variantes avec guidpilot.fr(/offre-fondatrice)
  (prix 99 € et date du 31 décembre autorisés pour l'offre de Noël — exception du 09/11/2026, comme sur Instagram).
- Teasers mar-17, mer-18, jeu-19 (Reels aussi publiés sur la page le même jour) : « Nouvelle vidéo sur notre page ».
- Teasers lun-16, ven-20, sam-21 (carrousels aussi publiés sur la page le même jour) : « Nouvelle publication sur notre page »."""
OFFRE = "14 jours gratuits, sans carte bancaire · guidpilot.fr"
VIDEO = "Nouvelle vidéo sur notre page 👆"
PUBLI = "Nouvelle publication sur notre page 👆"
NOEL = "Offre de Noël 🎁"

STORIES = [
 {"name": "fb_lun-16_1600_noel-8-25-par-mois", "type": "tip", "pill": NOEL,
  "title": "99 € pour un an, c'est [8,25 € par mois]", "size": 96,
  "sub": "Payé une fois, aucun prélèvement automatique. Jusqu'au 31 décembre : guidpilot.fr/offre-fondatrice"},
 {"name": "fb_lun-16_2000_teaser-bilan", "type": "teaser", "pill": "Nouvelle publication",
  "title": "Votre bilan 2026 [en 4 questions]", "size": 104, "sub": "10 minutes, un carnet.", "cta": PUBLI},
 {"name": "fb_mar-17_1230_cabinet-therapeute", "type": "teaser", "kick": "Sophrologue, hypnothérapeute, praticienne Reiki ?",
  "title": "Vos comptes rendus, écrits ou vocaux, [rangés dans l'espace de chaque cliente].", "size": 80, "cta": OFFRE},
 {"name": "fb_mar-17_2000_teaser-partenaires", "type": "teaser", "pill": "Nouvelle vidéo",
  "title": "En janvier, vos élèves [ouvrent leur cabinet.]", "size": 100, "sub": "Parlons partenariat.", "cta": VIDEO},
 {"name": "fb_mer-18_2000_teaser-le-calcul", "type": "teaser", "pill": "Nouvelle vidéo",
  "title": "99 € divisés par 12 mois. [Faites le calcul.]", "size": 100, "sub": "Le résultat tient en une ligne.", "cta": VIDEO},
 {"name": "fb_jeu-19_2000_teaser-coulisses", "type": "teaser", "pill": "Nouvelle vidéo",
  "title": "Notre bouton d'inscription était [hors de l'écran.]", "size": 96, "sub": "Coulisses de la semaine.", "cta": VIDEO},
 {"name": "fb_ven-20_2000_teaser-salon", "type": "teaser", "pill": "Nouvelle publication",
  "title": "Salon du bien-être : repartez avec [des rendez-vous]", "size": 96, "sub": "Le mini-guide en 5 étapes.", "cta": PUBLI},
 {"name": "fb_sam-21_1230_cabinet-therapeute", "type": "teaser", "kick": "Réflexologue, magnétiseuse, coach de vie ?",
  "title": "Vos clientes choisissent leur créneau [sans vous écrire].", "size": 88, "cta": OFFRE},
 {"name": "fb_sam-21_1600_noel-soirees-libres", "type": "tip", "pill": NOEL,
  "title": "Votre cadeau de Noël : [des soirées libres]", "size": 100,
  "sub": "1 an de GuidPilot pour 99 €, jusqu'au 31 décembre, sur guidpilot.fr"},
 {"name": "fb_sam-21_2000_teaser-liste-pere-noel", "type": "teaser", "pill": "Nouvelle publication",
  "title": "Votre liste au Père Noël tient [en 5 lignes]", "size": 100, "sub": "Cochez vos souhaits.", "cta": PUBLI},
]
