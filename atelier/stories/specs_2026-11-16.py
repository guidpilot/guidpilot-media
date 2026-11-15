"""Stories Instagram de la semaine du 16 au 22/11/2026 (lot lancé à la main par Normane le 15/11) — 13 stories + 7 « Offre de Noël » à 16h00.
12h30 : rotation question / mot-clé THÉRAPEUTE (mar, sam) / conseil / fonction ; 20h00 : teaser du post du jour (lun → sam).
16h00 : offre de Noël (prix 99 € et date du 31 décembre autorisés — exception du 09/11/2026).
Règles : vouvoiement, aucune personne représentée, aucun superlatif, jamais « Répondez GUIDANCE à cette story »."""
REEL = "Nouveau Reel sur le profil 👆"
POST = "Nouveau post sur le profil 👆"
NOEL = "Offre de Noël 🎁"

STORIES = [
 {"name": "lun-16_1230_question-bilan-un-mot", "type": "question", "pill": "Petite question",
  "title": "Votre année 2026 en un mot, [ce serait lequel ?]", "size": 96,
  "note": "Je lis toutes les réponses."},
 {"name": "lun-16_1600_noel-8-25-par-mois", "type": "tip", "pill": NOEL,
  "title": "99 € pour un an, c'est [8,25 € par mois]", "size": 96,
  "sub": "Payé une fois, aucun prélèvement automatique. Jusqu'au 31 décembre, lien en bio."},
 {"name": "lun-16_2000_teaser-bilan", "type": "teaser", "pill": "Nouveau post",
  "title": "Votre bilan 2026 [en 4 questions]", "size": 104, "sub": "10 minutes, un carnet.", "cta": POST},

 {"name": "mar-17_1230_mot-cle-therapeute", "type": "keyword", "kw": "THÉRAPEUTE", "kick": "Sophrologue, hypnothérapeute, praticienne Reiki ?",
  "title": "Vos comptes rendus, écrits ou vocaux, [rangés dans l'espace de chaque cliente].", "size": 80},
 {"name": "mar-17_1600_noel-question-2027", "type": "question", "pill": "Petite question",
  "title": "Qu'aimeriez-vous [ne plus faire] en 2027 ?", "size": 100,
  "note": "Relances, factures du soir, messages… Dites-le moi."},
 {"name": "mar-17_2000_teaser-partenaires", "type": "teaser", "pill": "Nouveau Reel",
  "title": "En janvier, vos élèves [ouvrent leur cabinet.]", "size": 100, "sub": "Parlons partenariat.", "cta": REEL},

 {"name": "mer-18_1230_conseil-source-clientes", "type": "tip", "pill": "Astuce guidance",
  "title": "Notez d'où vient [chaque nouvelle cliente]", "size": 96,
  "sub": "Instagram, bouche-à-oreille, annuaire… En décembre, vous saurez où mettre votre énergie."},
 {"name": "mer-18_1600_noel-essai-d-abord", "type": "tip", "pill": NOEL,
  "title": "Vous essayez d'abord : [14 jours gratuits,] sans carte", "size": 90,
  "sub": "L'offre se prend ensuite depuis votre espace : 1 an pour 99 €, jusqu'au 31 décembre."},
 {"name": "mer-18_2000_teaser-le-calcul", "type": "teaser", "pill": "Nouveau Reel",
  "title": "99 € divisés par 12 mois. [Faites le calcul.]", "size": 100, "sub": "Le résultat tient en une ligne.", "cta": REEL},

 {"name": "jeu-19_1230_question-quitter-un-site", "type": "question", "pill": "Petite question",
  "title": "Sur téléphone, qu'est-ce qui vous fait [quitter un site ?]", "size": 92,
  "note": "Trop de texte, trop de champs… Vos réponses nous aident."},
 {"name": "jeu-19_1600_noel-12-mois-apres-essai", "type": "tip", "pill": NOEL,
  "title": "Vos 12 mois démarrent [à la fin de votre essai]", "size": 92,
  "sub": "Aucun jour perdu. 1 an pour 99 €, jusqu'au 31 décembre."},
 {"name": "jeu-19_2000_teaser-coulisses", "type": "teaser", "pill": "Nouveau Reel",
  "title": "Notre bouton d'inscription était [hors de l'écran.]", "size": 96, "sub": "Coulisses de la semaine.", "cta": REEL},

 {"name": "ven-20_1230_fonction-guidance-espace", "type": "feature", "pill": "Dans GuidPilot", "title": "Écrite ou vocale, votre guidance [l'attend dans son espace]", "size": 88,
  "sub": "Plus de pièce jointe perdue : elle la retrouve et la réécoute quand elle veut.",
  "img": "kit/assets/guid.png", "W": 1270, "box": (430, 232, 820, 480), "maxh": 460},
 {"name": "ven-20_1600_noel-toutes-les-fonctions", "type": "tip", "pill": NOEL,
  "title": "Toutes les fonctions, [pendant 12 mois]", "size": 100,
  "sub": "Réservation, paiement, factures, espace client, avis. 99 € une fois, jusqu'au 31 décembre."},
 {"name": "ven-20_2000_teaser-salon", "type": "teaser", "pill": "Nouveau post",
  "title": "Salon du bien-être : repartez avec [des rendez-vous]", "size": 96, "sub": "Le mini-guide en 5 étapes.", "cta": POST},

 {"name": "sam-21_1230_mot-cle-therapeute", "type": "keyword", "kw": "THÉRAPEUTE", "kick": "Réflexologue, magnétiseuse, coach de vie ?",
  "title": "Vos clientes choisissent leur créneau [sans vous écrire].", "size": 88},
 {"name": "sam-21_1600_noel-soirees-libres", "type": "tip", "pill": NOEL,
  "title": "Votre cadeau de Noël : [des soirées libres]", "size": 100,
  "sub": "1 an de GuidPilot pour 99 €, jusqu'au 31 décembre. Lien en bio."},
 {"name": "sam-21_2000_teaser-liste-pere-noel", "type": "teaser", "pill": "Nouveau post",
  "title": "Votre liste au Père Noël tient [en 5 lignes]", "size": 100, "sub": "Cochez vos souhaits.", "cta": POST},

 {"name": "dim-22_1230_conseil-calendrier-avent", "type": "tip", "pill": "Calendrier de l'Avent 🎄",
  "title": "24 astuces en stories, [dès le 1er décembre]", "size": 96,
  "sub": "Une par jour, à appliquer tout de suite. Abonnez-vous pour ne rien manquer."},
 {"name": "dim-22_1600_noel-question-offre", "type": "question", "pill": NOEL,
  "title": "Une question sur l'offre de Noël ? [Posez-la ici.]", "size": 96,
  "note": "Je réponds à toutes."},
]
