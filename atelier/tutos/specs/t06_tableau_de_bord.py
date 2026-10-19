"""Tuto 6 · Découvrir votre tableau de bord (série « GuidPilot au quotidien »)."""

CARD = " >> xpath=ancestor::*[contains(@class,'rounded')][1]"
SERIE = "GuidPilot au quotidien"
RANGE = (6, 15)

TUTO = {
    "slug": "tuto-06-decouvrir-votre-tableau-de-bord",
    "num": 6, "range": RANGE,
    "series": SERIE,
    "title": "Découvrir votre tableau de bord",
    "subtitle": "Votre journée, vos chiffres et vos raccourcis en un coup d'œil",
    "music": "pilote",
    "next": "Tuto 7 · Gérer votre agenda",
    "scenes": [
        {"type": "intro",
         "voice": "Dans ce tutoriel, vous découvrez votre tableau de bord : la page d'accueil de GuidPilot, où vous retrouvez votre journée et vos raccourcis."},
        {"type": "shot", "snap": "q1_01_dashboard", "step": None,
         "caption": "Le <b>menu</b> : toutes les rubriques de votre activité",
         "focus": "aside a[href='/dashboard'] >> nth=-1", "focus2": "aside a[href='/parrainage']", "focus_pad": [12, 12, 0, 0], "zoom": 1.3,
         "voice": "À gauche, le menu vous donne accès à toutes les rubriques : agenda, clients, guidances, factures, avis, et votre page publique."},
        {"type": "shot", "snap": "q1_01_dashboard", "step": None,
         "caption": "Le <b>guide de démarrage</b> vous indique les étapes restantes",
         "focus": ":text('étapes complétées')", "focus2": "button:has-text('Configurer') >> nth=0", "focus_pad": [60, 70, 0, 0], "zoom": 1.2,
         "voice": "Tant que votre espace n'est pas entièrement configuré, le guide de démarrage vous montre les étapes restantes. Cliquez sur Configurer pour y aller directement."},
        {"type": "shot", "snap": "q1_02_accueil", "step": None,
         "caption": "Vos <b>chiffres du jour</b> : rendez-vous, guidances, revenus, avis",
         "focus": ":text(\"Rendez-vous aujourd'hui\")" + CARD, "focus2": ":text('Note moyenne')" + CARD, "zoom": 1.2,
         "voice": "En haut, vos chiffres du jour : les rendez-vous d'aujourd'hui, les guidances à livrer, vos revenus du mois et votre note moyenne."},
        {"type": "shot", "snap": "q1_02_accueil", "step": None,
         "caption": "Le <b>suivi financier</b> : encaissé, à encaisser, factures",
         "focus": ":text('Suivi financier')" + CARD, "zoom": 1.2,
         "voice": "Le suivi financier vous montre ce qui est encaissé ce mois-ci, et ce qui reste à encaisser."},
        {"type": "shot", "snap": "q1_03_actions", "step": None,
         "caption": "Les <b>actions rapides</b> pour gagner du temps",
         "focus": ":text('Actions rapides')" + CARD, "zoom": 1.5,
         "voice": "Avec les actions rapides, planifiez un rendez-vous, ajoutez un client, créez une guidance ou éditez une facture, en un clic."},
        {"type": "shot", "snap": "q1_03_actions", "step": None,
         "caption": "L'<b>activité récente</b> : les dernières réservations",
         "focus": ":text('Activité récente')" + CARD, "zoom": 1.2,
         "voice": "Plus bas, l'activité récente liste vos dernières réservations, pour ne rien manquer."},
        {"type": "recap",
         "items": ["Le menu pour chaque rubrique", "Le guide de démarrage", "Vos chiffres du jour", "Les actions rapides"],
         "voice": "En résumé : le menu pour naviguer, le guide de démarrage, vos chiffres du jour, et les actions rapides."},
        {"type": "outro",
         "voice": "Dans le prochain tutoriel, vous apprendrez à gérer votre agenda et vos rendez-vous."},
    ],
}
