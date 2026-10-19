"""Tuto 11 · Réaliser une séance en visio (série « GuidPilot au quotidien »).
Vérifié : le lien est saisi à la main (pas de création automatique de lien Meet). Il figure dans l'e-mail
de confirmation, le rappel de la veille et le bouton « Rejoindre » de l'espace client."""

DLG = "[role=dialog]"

TUTO = {
    "slug": "tuto-11-realiser-une-seance-en-visio",
    "num": 11, "range": (6, 15),
    "series": "GuidPilot au quotidien",
    "title": "Réaliser une séance en visio",
    "subtitle": "Ajouter votre lien de visio pour que votre client vous rejoigne",
    "music": "elan",
    "next": "Tuto 12 · Facturer et suivre vos encaissements",
    "scenes": [
        {"type": "intro",
         "voice": "Dans ce tutoriel, vous préparez une séance en visio : il suffit d'ajouter votre lien de visio au rendez-vous."},
        {"type": "shot", "snap": "q2_07_nouveau_bas", "step": 1,
         "caption": "Pour une prestation en visio, un champ <b>Lien de visio</b> apparaît",
         "focus": f"{DLG} input[name=meetingLink]", "focus_pad": [40, 16, 90, 0], "zoom": 1.7,
         "voice": "Quand vous créez un rendez-vous pour une prestation en visio, un champ Lien de visio apparaît."},
        {"type": "shot", "snap": "q2_04_lien_visio", "step": 2,
         "caption": "Collez votre lien <b>Google Meet</b> (ou un autre outil de visio)",
         "focus": f"{DLG} input[name=meetingLink]", "focus_pad": [40, 16, 50, 0], "zoom": 1.7, "click": True,
         "voice": "Créez votre réunion dans Google Meet, ou dans l'outil de visio de votre choix, copiez le lien, puis collez-le ici. Pour l'instant, ce lien se saisit à la main."},
        {"type": "shot", "snap": "q2_04_lien_visio", "step": 3,
         "caption": "Cliquez sur <b>Enregistrer</b>",
         "focus": f"{DLG} button:has-text('Enregistrer')", "zoom": 2.2, "click": True,
         "voice": "Cliquez sur Enregistrer. Vous pouvez aussi ajouter le lien plus tard, en modifiant le rendez-vous."},
        {"type": "shot", "snap": "q2_02_rdv", "step": None,
         "caption": "Sans lien, le rendez-vous vous le <b>signale</b>",
         "focus": f"{DLG} :text('Aucun lien de visio')", "focus_pad": [16, 16, 0, 0], "zoom": 1.9,
         "voice": "Tant qu'aucun lien n'est enregistré, le rendez-vous vous le signale : sans lien, votre client ne peut pas rejoindre la séance."},
        {"type": "shot", "snap": "q2_08_rdv_realise", "step": None, "kind": "result",
         "caption": "Votre client reçoit le lien par <b>e-mail</b> et le retrouve dans son <b>espace</b>",
         "focus": f"{DLG} a[href*='meet.google.com']", "focus_pad": [20, 20, 0, 0], "zoom": 1.9,
         "voice": "Votre client reçoit le lien dans l'e-mail de confirmation et dans le rappel de la veille. Il le retrouve aussi dans son espace, avec un bouton Rejoindre. Le jour venu, cliquez simplement sur le lien."},
        {"type": "recap",
         "items": ["Un lien de visio par rendez-vous", "Collé à la création, ou plus tard", "Envoyé dans la confirmation et le rappel",
                   "Enregistrer après chaque modification"],
         "voice": "En résumé : un lien de visio par rendez-vous, idéalement ajouté dès la création, pour qu'il parte dans la confirmation et le rappel. Et n'oubliez pas d'enregistrer après chaque modification."},
        {"type": "outro",
         "voice": "Dans le prochain tutoriel, vous verrez comment facturer et suivre vos encaissements."},
    ],
}
