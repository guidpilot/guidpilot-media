"""Stories de la semaine du 19 au 25/10/2026 (13 stories : 8h30 + 20h00 du lundi au samedi, 12h30 le dimanche)."""
CONCOURS_LEGAL = "Ce jeu n'est ni organisé, ni parrainé, ni géré par Instagram."
TEASE = "Nouveau Reel sur le profil 👆"

STORIES = [
 {"name": "lun-19_0830_mot-cle-guidance", "type": "keyword", "kw": "GUIDANCE", "kick": "Tarologue, voyante, médium ?",
  "title": "Votre activité, [dans un seul espace]."},
 {"name": "lun-19_2000_teaser-3-phrases", "type": "teaser", "pill": "Nouveau Reel", "title": "3 phrases qui font [fuir] vos clientes",
  "sub": "Sans que vous le sachiez."},
 {"name": "mar-20_0830_conseil-rappel-veille", "type": "tip", "pill": "Astuce cabinet", "title": "Le rappel, [la veille]. Pas le matin même.",
  "sub": "Votre cliente a le temps de s'organiser… ou de vous prévenir si elle doit décaler."},
 {"name": "mar-20_2000_teaser-seance-1h", "type": "teaser", "pill": "Nouveau Reel", "title": "Votre séance dure 1 h. Votre travail, [bien plus.]"},
 {"name": "mer-21_0830_concours-5-jours", "type": "concours", "pill": "Jeu-concours", "title": "Plus que [5 jours] pour gagner 1 an de GuidPilot",
  "cta": "Participez sous le Reel du concours sur notre profil 👆", "legal": CONCOURS_LEGAL},
 {"name": "mer-21_2000_teaser-ma-guidance", "type": "teaser", "pill": "Nouveau Reel", "title": "« Vous pouvez me renvoyer [ma guidance] ? »", "size": 100},
 {"name": "jeu-22_0830_mot-cle-therapeute", "type": "keyword", "kw": "THÉRAPEUTE", "kick": "Sophrologue, hypnothérapeute, praticienne Reiki ?",
  "title": "Votre cabinet, [dans un seul espace]."},
 {"name": "jeu-22_2000_teaser-premier-appel", "type": "teaser", "pill": "Nouveau Reel", "title": "Elle appelle pour [« se renseigner »]. Que dire ?", "size": 96},
 {"name": "ven-23_0830_question-malaise", "type": "question", "pill": "Petite question", "title": "Quelle question de cliente vous met [le plus mal à l'aise] ?", "size": 92},
 {"name": "ven-23_2000_teaser-rythme", "type": "teaser", "pill": "Nouveau Reel", "title": "Elle revient [chaque semaine]. Bonne nouvelle ?"},
 {"name": "sam-24_0830_fonction-journee", "type": "feature", "pill": "Dans GuidPilot", "title": "Votre journée, [d'un coup d'œil]", "size": 92,
  "sub": "Vos séances du jour et vos actions rapides, dès l'ouverture. Plus besoin de chercher dans trois outils.",
  "img": "kit/assets/dash_np.png", "W": 1270, "box": (20, 585, 1230, 1005)},
 {"name": "sam-24_2000_teaser-concours-2-jours", "type": "teaser", "pill": "Nouveau Reel", "title": "Plus que [2 jours]",
  "sub": "pour gagner 1 an de GuidPilot", "legal": CONCOURS_LEGAL},
 {"name": "dim-25_1230_mot-cle-guidance", "type": "keyword", "kw": "GUIDANCE", "kick": "Praticienne en guidance ?",
  "title": "Réservations, guidances, factures : [tout au même endroit].", "size": 92},
]
