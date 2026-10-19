"""Tuto 20 · Support, nouveautés et notifications (série « Aller plus loin »).
Vérifié (commit 86ffbd2a) : cloche avec « Tout marquer comme lu », un clic ouvre l'élément concerné ; Nouveautés marquées lues à la visite ;
ticket Sujet + Message, l'équipe répond dans le fil, badge « Nouvelle réponse » (pas d'e-mail ni de notification) ;
Avis GuidPilot publié sur le site après validation."""

DLG = "[role=dialog][data-state=open]"

TUTO = {
    "slug": "tuto-20-support-nouveautes-et-notifications",
    "num": 20, "range": (15, 21),
    "series": "Aller plus loin",
    "title": "Support, nouveautés et notifications",
    "subtitle": "Rester informé et obtenir de l'aide de l'équipe GuidPilot",
    "music": "pilote",
    "next": None,
    "end_title": "Vous êtes prêt à piloter votre activité",
    "scenes": [
        {"type": "intro",
         "voice": "Dans ce tutoriel, vous découvrez vos notifications, les nouveautés de GuidPilot, et comment contacter notre équipe."},
        {"type": "shot", "snap": "r6_05_notifications", "step": 1,
         "caption": "La <b>cloche</b> : vos rendez-vous, messages, avis et ventes",
         "focus": "[data-radix-popper-content-wrapper] >> nth=0", "zoom": 1.4,
         "voice": "En haut du menu, la cloche réunit vos notifications : nouveaux rendez-vous, messages de vos clients, avis, ventes de cartes cadeaux. Un clic ouvre l'élément concerné. Tout marquer comme lu vide le compteur."},
        {"type": "shot", "snap": "r6_04_nouveautes", "step": 2,
         "caption": "Les <b>nouveautés</b> : chaque nouvelle fonction expliquée",
         "focus": "a[href='/nouveautes'] >> nth=0", "zoom": 2.2, "click": True,
         "voice": "L'icône à côté ouvre les Nouveautés : nous y annonçons chaque nouvelle fonction, avec la marche à suivre pour l'activer."},
        {"type": "shot", "snap": "r6_01_support", "step": 3,
         "caption": "Une question ? Ouvrez <b>Support</b>, puis <b>Nouveau ticket</b>",
         "focus": "main button:has-text('Nouveau ticket')", "zoom": 2.2, "click": True,
         "voice": "Une question ou un souci ? Dans le menu, ouvrez Support, puis cliquez sur Nouveau ticket."},
        {"type": "shot", "snap": "r6_02_ticket_nouveau", "step": 4,
         "caption": "Un <b>sujet</b>, votre <b>message</b>, puis <b>Envoyer le ticket</b>",
         "focus": f"{DLG} #ticket-subject", "focus2": f"{DLG} button:has-text('Envoyer le ticket')", "focus_pad": [40, 16, 0, 0], "zoom": 1.5,
         "click_sel": f"{DLG} button:has-text('Envoyer le ticket')",
         "voice": "Indiquez un sujet, expliquez votre besoin en quelques lignes, puis cliquez sur Envoyer le ticket."},
        {"type": "shot", "snap": "r6_01_support", "step": None, "kind": "result",
         "caption": "Notre réponse arrive dans le fil : badge <b>Nouvelle réponse</b>",
         "focus": "main :text('Question sur les cartes cadeaux') >> xpath=ancestor::*[contains(@class,'rounded')][1]", "zoom": 1.5,
         "voice": "Notre équipe vous répond dans le fil du ticket. Revenez dans Support : le badge Nouvelle réponse vous signale notre message."},
        {"type": "shot", "snap": "r6_03_avis_guidpilot", "step": None,
         "caption": "Satisfait ? Laissez votre <b>avis sur GuidPilot</b>",
         "focus": ":text('Votre avis sur GuidPilot') >> xpath=ancestor::*[contains(@class,'rounded')][1]", "zoom": 1.3,
         "voice": "Enfin, dans Paramètres, l'onglet Avis GuidPilot vous permet de nous laisser une note et un commentaire. Il est publié sur notre site après validation. Merci, cela aide d'autres praticiens à nous découvrir."},
        {"type": "recap",
         "items": ["La cloche pour vos notifications", "Les nouveautés de GuidPilot", "Support pour poser vos questions",
                   "Votre avis sur GuidPilot"],
         "voice": "En résumé : la cloche pour vos notifications, les nouveautés pour suivre GuidPilot, et le support pour toute question."},
        {"type": "outro",
         "voice": "Vous connaissez maintenant les fonctions avancées de GuidPilot. Retrouvez tous les tutoriels dans la rubrique Aide et tutoriels."},
    ],
}
