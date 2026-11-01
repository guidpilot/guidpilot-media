"""Stories Instagram de la semaine du 02 au 08/11/2026 (tâche du dimanche 01/11/2026) — 13 stories.
12h30 : rotation conseil express / mot-clé THÉRAPEUTE (mar, sam) / question / fonction ; 20h00 : teaser du post du jour.
Mardi 03/11 : le post du jour est le Reel partenaires déjà programmé (12h15).
Règles : vouvoiement, aucune personne représentée, aucun prix, aucun superlatif, jamais « Répondez GUIDANCE à cette story »."""
REEL = "Nouveau Reel sur le profil 👆"
POST = "Nouveau post sur le profil 👆"

STORIES = [
 {"name": "lun-02_1230_conseil-question-avant", "type": "tip", "pill": "Astuce guidance",
  "title": "Demandez sa question [avant la séance]", "size": 100,
  "sub": "Vous commencez concentrée, et votre cliente se sent attendue."},
 {"name": "lun-02_2000_teaser-avis", "type": "teaser", "pill": "Nouveau Reel",
  "title": "Elle a adoré sa guidance. [Pourtant, aucun avis.]", "size": 96, "sub": "Le problème, c'est le moment.", "cta": REEL},
 {"name": "mar-03_1230_mot-cle-therapeute", "type": "keyword", "kw": "THÉRAPEUTE", "kick": "Coach de vie, réflexologue, magnétiseuse ?",
  "title": "Moins de messages pour caler vos séances, [plus de temps pour vos clients].", "size": 86},
 {"name": "mar-03_2000_teaser-partenaires", "type": "teaser", "pill": "Nouveau Reel",
  "title": "Vous recommandez des outils [à votre communauté] ?", "size": 96, "sub": "Devenez partenaire GuidPilot.", "cta": REEL},
 {"name": "mer-04_1230_question-ecrit-ou-vocal", "type": "question", "pill": "Petite question",
  "title": "Après la séance, votre guidance : [écrite ou vocale] ?", "size": 96,
  "note": "Ou les deux ? Je lis toutes les réponses."},
 {"name": "mer-04_2000_teaser-voyante-visio", "type": "teaser", "pill": "Nouveau Reel",
  "title": "Voyante en visio : [votre outil suit-il ?]", "size": 100, "sub": "Paiement, lien, guidance.", "cta": REEL},
 {"name": "jeu-05_1230_fonction-actions-rapides", "type": "feature", "pill": "Dans GuidPilot", "title": "4 actions, [un seul écran]", "size": 96,
  "sub": "Rendez-vous, cliente, compte rendu, facture : tout part de votre tableau de bord.",
  "img": "kit/assets/dash_np.png", "W": 1270, "box": (840, 590, 1225, 990), "maxh": 420},
 {"name": "jeu-05_2000_teaser-acompte", "type": "teaser", "pill": "Nouveau post",
  "title": "Un acompte, [ça fait fuir vos clientes ?]", "size": 100, "sub": "5 idées reçues à revoir.", "cta": POST},
 {"name": "ven-06_1230_conseil-relire-notes", "type": "tip", "pill": "Astuce guidance",
  "title": "Relisez vos notes [5 minutes avant] chaque séance", "size": 96,
  "sub": "Votre cliente sent que vous vous souvenez d'elle."},
 {"name": "ven-06_2000_teaser-novembre", "type": "teaser", "pill": "Nouveau Reel",
  "title": "Agenda vide en novembre ? [Ne baissez pas vos prix.]", "size": 96, "cta": REEL},
 {"name": "sam-07_1230_mot-cle-therapeute", "type": "keyword", "kw": "THÉRAPEUTE", "kick": "Sophrologue, hypnothérapeute ?",
  "title": "Séance à distance : le lien de visio part [sans que vous l'envoyiez].", "size": 86},
 {"name": "sam-07_2000_teaser-sophrologue", "type": "teaser", "pill": "Nouveau post",
  "title": "Sophrologue : [6 questions] avant de choisir votre outil", "size": 96, "sub": "La checklist à enregistrer.", "cta": POST},
 {"name": "dim-08_1230_question-phrase-cliente", "type": "question", "pill": "Petite question",
  "title": "Quelle phrase de cliente [vous déstabilise] le plus ?", "size": 100,
  "note": "Je lis toutes les réponses."},
]
