"""Stories Instagram de la semaine du 26/10 au 01/11/2026 (créées le 25/10/2026 à la demande de Normane).
La story du lundi 26/10 à 12h30 (concours dernier jour) existe déjà (2026-10-26/stories). Ici : les 12 autres.
Teasers de 20h00 = post du jour déjà programmé (Reels démo 26 et 27/10, Reel « pendant que vous dormez » 28/10,
carrousels 29, 30 et 31/10). Concours terminé le 26/10 au soir : aucune story concours à partir du 27/10.
Directives : vouvoiement, aucune personne représentée, aucun prix, aucun superlatif, logo officiel uniquement."""
REEL = "Nouveau Reel sur le profil 👆"
POST = "Nouveau post sur le profil 👆"

STORIES = [
 {"name": "lun-26_2000_teaser-parcours-complet", "type": "teaser", "pill": "Nouveau Reel",
  "title": "Réservation, paiement, guidance : [le parcours complet]", "size": 96, "sub": "En moins de 2 minutes.", "cta": REEL},
 {"name": "mar-27_1230_mot-cle-therapeute", "type": "keyword", "kw": "THÉRAPEUTE", "kick": "Sophrologue, praticienne Reiki ou LaHoChi ?",
  "title": "Vos séances, vos règlements, vos factures : [au même endroit].", "size": 90},
 {"name": "mar-27_2000_teaser-cabinet-2-minutes", "type": "teaser", "pill": "Nouveau Reel",
  "title": "Votre cabinet, [en 2 minutes]", "sub": "Réservation, rappel, encaissement, compte rendu.", "cta": REEL},
 {"name": "mer-28_1230_conseil-resume-ecrit", "type": "tip", "pill": "Astuce guidance",
  "title": "Un court [résumé écrit] après chaque séance", "size": 96,
  "sub": "Votre cliente relit à tête reposée, et les « vous m'aviez dit quoi, déjà ? » disparaissent."},
 {"name": "mer-28_2000_teaser-pendant-que-vous-dormez", "type": "teaser", "pill": "Nouveau Reel",
  "title": "Et si vos clientes réservaient [pendant que vous dormez] ?", "size": 96, "cta": REEL},
 {"name": "jeu-29_1230_question-temps-hors-seance", "type": "question", "pill": "Petite question",
  "title": "En dehors des séances, qu'est-ce qui vous prend [le plus de temps] ?", "size": 90,
  "note": "Messages, paiements, factures… je lis toutes les réponses."},
 {"name": "jeu-29_2000_teaser-reserve-en-seance", "type": "teaser", "pill": "Nouveau post",
  "title": "Vous êtes en séance. [Elle réserve quand même.]", "size": 96, "cta": POST},
 {"name": "ven-30_1230_fonction-avis", "type": "feature", "pill": "Dans GuidPilot", "title": "Vos avis, [demandés en un clic]", "size": 92,
  "sub": "Après la séance, un lien à envoyer. Vous suivez votre note et les demandes à relancer.",
  "img": "kit/assets/avis.png", "W": 1270, "box": (15, 140, 625, 310)},
 {"name": "ven-30_2000_teaser-petite-question", "type": "teaser", "pill": "Nouveau post",
  "title": "« Juste une [petite question]… »", "sub": "3 réponses prêtes à copier, sans offrir votre séance.", "cta": POST},
 {"name": "sam-31_1230_mot-cle-therapeute", "type": "keyword", "kw": "THÉRAPEUTE", "kick": "Hypnothérapeute, réflexologue, magnétiseuse ?",
  "title": "Vos clients réservent en ligne. [Vous, vous restez en séance.]", "size": 88},
 {"name": "sam-31_2000_teaser-semaine-type", "type": "teaser", "pill": "Nouveau post",
  "title": "Votre semaine type, [sans déborder]", "sub": "Le modèle à recopier est sur le profil.", "cta": POST},
 {"name": "dim-01_1230_question-lien-en-bio", "type": "question", "pill": "Petite question",
  "title": "Aujourd'hui, votre lien en bio mène [où] ?", "size": 96,
  "note": "Vos messages privés, un site, une page de réservation ?"},
]
