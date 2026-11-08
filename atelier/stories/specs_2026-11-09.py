"""Stories Instagram de la semaine du 09 au 15/11/2026 (lot du dimanche 08/11/2026) — 13 stories.
12h30 : rotation conseil express / mot-clé THÉRAPEUTE (mar, sam) / question / fonction ; 20h00 : teaser du post du jour.
Mardi 10/11 : le post du jour est le Reel partenaires déjà programmé (12h15).
Règles : vouvoiement, aucune personne représentée, aucun prix, aucun superlatif, jamais « Répondez GUIDANCE à cette story »."""
REEL = "Nouveau Reel sur le profil 👆"
POST = "Nouveau post sur le profil 👆"

STORIES = [
 {"name": "lun-09_1230_conseil-lien-bio", "type": "tip", "pill": "Astuce guidance",
  "title": "Avant de répondre à « c'est combien ? », [vérifiez votre lien en bio]", "size": 88,
  "sub": "S'il mène à vos prestations et à la réservation, la question se pose moins."},
 {"name": "lun-09_2000_teaser-c-est-combien", "type": "teaser", "pill": "Nouveau Reel",
  "title": "« C'est combien ? » [Vous répondez quoi ?]", "size": 104, "sub": "3 réponses à ne plus envoyer.", "cta": REEL},
 {"name": "mar-10_1230_mot-cle-therapeute", "type": "keyword", "kw": "THÉRAPEUTE", "kick": "Réflexologue, praticienne Reiki, hypnothérapeute ?",
  "title": "Vos clientes réservent et règlent en ligne, [même pendant vos séances].", "size": 84},
 {"name": "mar-10_2000_teaser-partenaires", "type": "teaser", "pill": "Nouveau Reel",
  "title": "Vous conseillez des outils [aux praticiens] ?", "size": 100, "sub": "Parlons partenariat.", "cta": REEL},
 {"name": "mer-11_1230_question-etude-ecrite", "type": "question", "pill": "Petite question",
  "title": "Votre dernière guidance écrite, vous l'avez envoyée [comment] ?", "size": 92,
  "note": "Mail, WhatsApp, PDF… Je lis toutes les réponses."},
 {"name": "mer-11_2000_teaser-astrologue", "type": "teaser", "pill": "Nouveau Reel",
  "title": "Astrologue : votre thème natal écrit, [vous l'envoyez comment ?]", "size": 92, "sub": "Le parcours en 4 étapes.", "cta": REEL},
 {"name": "jeu-12_1230_fonction-avis-page", "type": "feature", "pill": "Dans GuidPilot", "title": "Vos avis, [suivis et relancés]", "size": 96,
  "sub": "Note moyenne, avis publiés, taux de réponse : vous voyez qui relancer, en un coup d'œil.",
  "img": "kit/assets/avis.png", "W": 1270, "box": (20, 150, 1250, 310), "maxh": 420},
 {"name": "jeu-12_2000_teaser-annulation", "type": "teaser", "pill": "Nouveau post",
  "title": "Elle annule [une heure avant.]", "size": 104, "sub": "4 réponses prêtes à copier.", "cta": POST},
 {"name": "ven-13_1230_conseil-tarif-duree", "type": "tip", "pill": "Astuce guidance",
  "title": "Affichez le [tarif et la durée] de chaque prestation", "size": 96,
  "sub": "« Tarifs sur demande » fait hésiter. Une info claire rassure et fait réserver."},
 {"name": "ven-13_2000_teaser-avant-de-reserver", "type": "teaser", "pill": "Nouveau Reel",
  "title": "Ce que vos clientes regardent [avant de réserver]", "size": 96, "sub": "Et que vous ne voyez pas.", "cta": REEL},
 {"name": "sam-14_1230_mot-cle-therapeute", "type": "keyword", "kw": "THÉRAPEUTE", "kick": "Sophrologue, réflexologue, magnétiseuse ?",
  "title": "Paiement au cabinet ou en ligne : [la facture se crée toute seule].", "size": 84},
 {"name": "sam-14_2000_teaser-reflexologue", "type": "teaser", "pill": "Nouveau post",
  "title": "Réflexologue : [une journée,] deux façons de la vivre", "size": 96, "sub": "Avant / après, heure par heure.", "cta": POST},
 {"name": "dim-15_1230_question-lendemain", "type": "question", "pill": "Petite question",
  "title": "Écrivez-vous à vos clientes [le lendemain] d'une séance ?", "size": 96,
  "note": "Oui, non, parfois ? Je lis toutes les réponses."},
]
