"""Tuto 13 · Demander un avis (série « GuidPilot au quotidien »).
Vérifié : « Demander un avis » génère un lien unique (Copier le lien / Ouvrir l'e-mail) ; aucun e-mail automatique ;
la page Avis affiche « À relancer » au bout de 3 jours ; « Masquer » retire un avis de la page publique."""

CARD = " >> xpath=ancestor::*[contains(@class,'rounded')][1]"
DLG = "[role=dialog]"

TUTO = {
    "slug": "tuto-13-demander-un-avis",
    "num": 13, "range": (6, 15),
    "series": "GuidPilot au quotidien",
    "title": "Demander un avis",
    "subtitle": "Recueillir les avis de vos clients et les afficher sur votre page",
    "music": "aube",
    "next": "Tuto 14 · Connecter Google Agenda",
    "scenes": [
        {"type": "intro",
         "voice": "Dans ce tutoriel, vous demandez un avis à vos clients après une séance, pour rassurer ceux qui découvrent votre page."},
        {"type": "shot", "snap": "q2_08_rdv_realise", "step": 1,
         "caption": "Ouvrez un rendez-vous <b>réalisé</b>, puis <b>Demander un avis</b>",
         "focus": f"{DLG} :text('Demande déjà envoyée')", "focus_pad": [20, 20, 0, 0], "zoom": 1.9,
         "voice": "Après la séance, ouvrez le rendez-vous réalisé et cliquez sur Demander un avis. Ici, la demande a déjà été faite."},
        {"type": "shot", "snap": "q7_02_lien", "step": 2,
         "caption": "Un <b>lien unique</b> est créé : <b>copiez-le</b> ou ouvrez un <b>e-mail</b>",
         "focus": "#avislien > div", "zoom": 1.6, "click_sel": "#copier",
         "voice": "GuidPilot crée un lien personnel, valable une seule fois. Copiez-le pour l'envoyer par message, ou cliquez sur Ouvrir l'e-mail : votre messagerie s'ouvre avec un texte prêt à envoyer."},
        {"type": "shot", "snap": "q7_01_avis", "step": 3,
         "caption": "Dans <b>Avis</b>, suivez votre <b>note</b> et les demandes <b>à relancer</b>",
         "focus": ":text('Note moyenne')" + CARD, "focus2": ":text('À relancer')" + CARD, "zoom": 1.2,
         "voice": "Dans le menu Avis, suivez votre note moyenne, le taux de réponse, et les demandes à relancer : elles apparaissent au bout de trois jours sans réponse."},
        {"type": "shot", "snap": "q7_01_avis", "step": None,
         "caption": "Pour relancer : <b>copiez à nouveau le lien</b> et renvoyez-le",
         "focus": ":text('À relancer')" + CARD, "zoom": 1.8,
         "voice": "Pour relancer, copiez à nouveau le lien et renvoyez-le à votre client, puis cliquez sur Relancer pour garder la trace de votre relance."},
        {"type": "shot", "snap": "q7_01_avis", "step": None, "kind": "result",
         "caption": "L'avis s'affiche sur votre <b>page publique</b> ; <b>Masquer</b> le retire",
         "focus": ":text('Publiée') >> nth=0" + CARD, "zoom": 1.4,
         "voice": "Une fois publié, l'avis apparaît sur votre page publique et compte dans votre note. Le bouton Masquer le retire de la page."},
        {"type": "shot", "snap": "p5_05_page", "step": None,
         "caption": "Votre <b>note moyenne</b> rassure les visiteurs de votre page",
         "focus": ":text('5.0 / 5')", "focus_pad": [16, 40, 0, 0], "zoom": 1.25,
         "voice": "Votre note moyenne s'affiche en haut de votre page publique : c'est l'un des premiers éléments que regardent vos futurs clients."},
        {"type": "recap",
         "items": ["Après chaque séance réalisée", "Un lien unique à copier ou envoyer", "Une relance au bout de trois jours",
                   "Une note visible sur votre page"],
         "voice": "En résumé : demandez un avis après chaque séance, envoyez le lien, relancez si besoin, et laissez votre note rassurer vos visiteurs."},
        {"type": "outro",
         "voice": "Dans le prochain tutoriel, vous connecterez votre Google Agenda."},
    ],
}
