"""Lot du 12 au 18 octobre 2026 : 7 carrousels CONSEIL (10h00, Instagram) + 7 Reels PROMO (18h00, Instagram + YouTube Short).
Usage : python3 posts_2026-10-12.py <SHA>  → écrit build/metricool/*.json (payloads createScheduledPost, draft: true)."""
import json, sys, pathlib

DOSSIER = "2026-10-12_au_18"
CTA = "Testez GuidPilot gratuitement pendant 14 jours, sans carte bancaire.\n👉 Lien en bio : guidpilot.fr"

CARROUSELS = [
 ("2026-10-12", "k1-bio-instagram", """Bio Instagram de tarologue, médium ou praticienne en guidance : 5 éléments qui donnent envie de réserver.

Faites défiler, puis relisez votre bio :
✔ qui vous êtes, en mots simples
✔ pour qui vous travaillez
✔ ce que vous proposez (visio, cabinet, guidance écrite ou vocale)
✔ une seule action à faire
✔ un seul lien qui mène à tout

Avec GuidPilot, ce lien, c'est votre page praticienne : vos prestations, vos avis et la réservation en ligne.
{CTA}

Combien de ces 5 éléments votre bio contient-elle déjà ? 👇

#tarologue #voyance #guidance #medium #cartomancie #praticienne #bioinstagram #entrepreneuse #energeticienne"""),
 ("2026-10-13", "k2-avant-seance", """Avant une séance de guidance ou de tarot : la checklist des 10 minutes pour commencer sereine.

✔ relisez sa fiche et ses dernières séances
✔ préparez un espace calme
✔ testez le son et la visio
✔ coupez les notifications
✔ rappelez le cadre en début de séance

Avec GuidPilot, la fiche de la cliente, son historique et le lien Google Meet sont prêts au même endroit.
{CTA}

Quel est votre rituel juste avant une séance ? 👇

Enregistrez ce post pour l'avoir sous la main.

#tarologue #guidance #voyance #medium #praticiennebienetre #energeticienne #seanceenvisio #oracle #praticienne"""),
 ("2026-10-14", "k3-messages-clientes", """5 messages prêts à copier pour vos clientes, de la prise de contact à l'après-séance.

✔ accueillir une nouvelle cliente
✔ confirmer le rendez-vous
✔ le rappel de la veille
✔ livrer une guidance
✔ reprendre contact, sans insister

Adaptez-les à votre ton, et gardez toujours le vouvoiement professionnel.

Avec GuidPilot, la confirmation de réservation part toute seule, et vos échanges restent dans une messagerie dédiée à chaque cliente.
{CTA}

Lequel de ces messages écrivez-vous le plus souvent ? 👇

#tarologue #voyante #medium #guidance #cartomancie #praticienne #relationclient #energeticienne #entrepreneuse"""),
 ("2026-10-15", "k4-visio-chaleureuse", """Séance de voyance ou de guidance en visio : 5 réflexes pour qu'elle soit aussi chaleureuse qu'en cabinet.

✔ la lumière face à vous
✔ la caméra à hauteur des yeux
✔ le lien envoyé à l'avance
✔ un plan B si la connexion coupe
✔ une fin de séance soignée

Avec GuidPilot, vos séances en visio se font avec Google Meet, et le compte rendu arrive ensuite dans l'espace client.
{CTA}

Vous préférez les séances en visio ou en cabinet ? 👇

#voyance #guidance #tarologue #medium #seanceenvisio #praticiennebienetre #energeticienne #consultationenligne #praticienne"""),
 ("2026-10-16", "k5-notes-seance", """Vos notes de séance : quoi écrire dans une fiche cliente… et ce qu'il vaut mieux éviter.

✔ la date et le format de la séance
✔ les thèmes abordés, en quelques mots
✔ la suite convenue
✔ des faits, jamais de jugements
✔ un endroit protégé, pas des post-it

Avec GuidPilot, chaque cliente a sa fiche avec l'historique de ses séances, et vos notes personnelles ne sont jamais visibles par elle.
{CTA}

Où prenez-vous vos notes aujourd'hui : carnet, téléphone, ordinateur ? 👇

#tarologue #guidance #praticiennebienetre #energeticienne #medium #voyance #fichesclients #organisation #independante"""),
 ("2026-10-17", "k6-chiffres-du-mois", """Praticienne indépendante : 5 chiffres à regarder chaque mois pour savoir où vous en êtes.

✔ le nombre de séances
✔ ce qui reste à encaisser
✔ les clientes qui reviennent
✔ vos avis
✔ d'où viennent vos clientes

10 minutes par mois suffisent, sans vous juger : c'est la tendance qui compte.

Le tableau de bord GuidPilot affiche vos rendez-vous, vos guidances à livrer, l'encaissé, le reste à encaisser et votre note moyenne.
{CTA}

Lequel de ces chiffres suivez-vous déjà ? 👇

#praticiennebienetre #tarologue #energeticienne #guidance #voyance #independante #entrepreneuse #organisation #medium"""),
 ("2026-10-18", "k7-routine-dimanche", """Routine du dimanche : préparer votre semaine de praticienne en 15 minutes.

✔ regardez vos rendez-vous et protégez vos pauses
✔ listez les guidances à livrer
✔ vérifiez les paiements en attente
✔ répondez aux messages restés en attente
✔ bloquez un moment pour vous

Avec GuidPilot, vos rendez-vous, vos guidances à livrer et vos paiements à encaisser sont sur un seul écran.
{CTA}

Et vous, vous préparez votre semaine le dimanche ou le lundi matin ? 👇

#tarologue #voyance #guidance #medium #energeticienne #praticiennebienetre #organisation #routine #entrepreneuse"""),
]

REELS = [
 ("2026-10-12", "p1-tableau-de-bord", 3000, "Logiciel pour tarologue : votre journée en 30 secondes avec GuidPilot #shorts",
  ["logiciel tarologue", "tableau de bord praticienne", "organisation voyance", "praticienne guidance", "gestion cabinet bien-être", "GuidPilot", "énergéticienne"],
  """Tarologue, voyante, praticienne en guidance : votre journée en 30 secondes, avec un café.

Sur votre tableau de bord GuidPilot :
✔ vos rendez-vous du jour
✔ les guidances à livrer
✔ ce qui est encaissé et ce qui reste à encaisser
✔ les actions rapides : ajouter une cliente, créer une guidance, éditer une facture

Moins de temps à chercher, plus de temps pour vos clientes.

{CTA}

Quelle est la première chose que vous regardez le matin ? 👇

#tarologue #voyance #guidance #medium #cartomancie #praticienne #logicielpraticien #organisation #guidpilot"""),
 ("2026-10-13", "p2-rappel-paiement", 2500, "Séance non payée ? Le rappel de paiement en un clic pour praticiennes #shorts",
  ["rappel de paiement", "séance non payée", "tarologue", "voyante", "praticienne guidance", "logiciel praticien", "GuidPilot"],
  """POV : la séance de guidance est terminée… et le paiement n'est toujours pas arrivé.

Avec GuidPilot :
✔ vous ouvrez le rendez-vous
✔ vous cliquez sur « Envoyer un rappel de paiement »
✔ votre cliente reçoit le rappel, vous n'avez rien à rédiger
✔ vous suivez ce qui reste à encaisser sur votre tableau de bord

Être payée sans courir après vos clientes.

{CTA}

Avez-vous déjà dû relancer une cliente pour un paiement ? 👇

#tarologue #voyante #medium #guidance #praticiennebienetre #energeticienne #paiement #independante #guidpilot"""),
 ("2026-10-14", "p3-chemin-avis", 2500, "Avis clients pour tarologue et voyante : du clic à votre page #shorts",
  ["avis clients", "demander un avis", "tarologue", "voyante", "praticienne bien-être", "page praticien", "GuidPilot"],
  """Le chemin d'un avis client, de la séance jusqu'à votre page praticienne.

Avec GuidPilot :
✔ 1. la demande d'avis part en un clic après la séance
✔ 2. vous relancez si besoin, quand vous le souhaitez
✔ 3. vous suivez votre note moyenne et les avis à relancer
✔ 4. l'avis publié s'affiche sur votre page, là où vos futures clientes le liront

De vrais avis, sans relances gênantes.

{CTA}

Combien d'avis avez-vous reçus ce mois-ci ? 👇

#tarologue #voyance #guidance #medium #avisclients #praticiennebienetre #energeticienne #cartomancie #guidpilot"""),
 ("2026-10-15", "p4-annuaire", 2500, "Trouver des clientes en voyance ou guidance : l'annuaire GuidPilot #shorts",
  ["trouver des clientes voyance", "annuaire praticiens", "visibilité tarologue", "praticienne guidance", "page praticien", "énergéticienne", "GuidPilot"],
  """Et si de nouvelles clientes pouvaient vous trouver, sans publier tous les jours ?

Avec GuidPilot :
✔ votre profil peut apparaître dans l'annuaire des praticiens GuidPilot
✔ les personnes qui cherchent une séance comparent les approches, les prestations et les avis
✔ elles découvrent votre page praticienne, avec votre présentation et vos séances
✔ sur Instagram ou TikTok, un seul lien dans votre bio suffit pour réserver

{CTA}

Aujourd'hui, comment vos nouvelles clientes vous trouvent-elles ? 👇

#tarologue #voyante #guidance #medium #energeticienne #praticiennebienetre #visibilite #annuaire #guidpilot"""),
 ("2026-10-16", "p5-espace-client", 2500, "Espace client pour praticienne en guidance : ce que voit votre cliente #shorts",
  ["espace client", "guidance écrite", "guidance vocale", "praticienne guidance", "tarologue", "logiciel praticien", "GuidPilot"],
  """Et si on regardait GuidPilot du côté de votre cliente ?

Dans son espace client sécurisé, sur son téléphone :
✔ ses rendez-vous
✔ ses guidances écrites et vocales, à relire ou réécouter
✔ ses factures
✔ une messagerie privée avec vous

Et vos notes personnelles restent privées : votre cliente ne les voit jamais.

{CTA}

Vos clientes retrouvent-elles facilement leurs guidances aujourd'hui ? 👇

#guidance #guidanceecrite #tarologue #voyance #medium #cartomancie #praticienne #espaceclient #guidpilot"""),
 ("2026-10-17", "p6-factures", 2500, "Facture automatique pour tarologue et praticienne bien-être #shorts",
  ["facture automatique", "facturation praticienne", "tarologue", "praticienne bien-être", "énergéticienne", "logiciel facture", "GuidPilot"],
  """Encore des factures à faire le soir, après vos séances ?

Avec GuidPilot :
✔ la réservation est payée en ligne
✔ la facture est créée automatiquement
✔ votre cliente la retrouve dans son espace
✔ vous suivez vos factures et vos paiements depuis votre tableau de bord

Vos soirées, sans paperasse.

{CTA}

Combien de temps passez-vous sur vos factures chaque mois ? 👇

#praticiennebienetre #energeticienne #tarologue #reiki #soinsenergetiques #facturation #independante #entrepreneuse #guidpilot"""),
 ("2026-10-18", "p7-idees-recues", 2500, "Logiciel pour praticienne : 4 idées reçues (vrai ou faux ?) #shorts",
  ["logiciel praticienne", "logiciel tarologue", "idées reçues", "praticienne guidance", "voyante", "énergéticienne", "GuidPilot"],
  """Vrai ou faux ? 4 idées reçues sur les logiciels pour praticiennes.

✖ « C'est trop compliqué » → GuidPilot est pensé pour les praticiennes, pas pour les informaticiennes
✖ « Il faut sa carte bancaire pour essayer » → l'essai de 14 jours est sans carte bancaire
✖ « On prend une commission sur mes séances » → 0 % de commission (hors frais du moyen de paiement)
✖ « Il me faut cinq outils » → rendez-vous, clientes, guidances, factures et avis dans un seul espace

{CTA}

Quelle idée reçue vous a déjà freinée ? 👇

#tarologue #voyance #guidance #medium #energeticienne #praticiennebienetre #logicielpraticien #cartomancie #guidpilot"""),
]

def payloads(sha):
    cdn = f"https://cdn.jsdelivr.net/gh/guidpilot/guidpilot-media@{sha}/{DOSSIER}/"
    out = []
    for day, name, text in CARROUSELS:
        out.append({"autoPublish": True, "descendants": [], "draft": True, "firstCommentText": "", "hasNotReadNotes": False,
            "media": [f"{cdn}{name}-{i:02d}.jpg" for i in range(1, 8)], "mediaAltText": [], "providers": [{"network": "instagram"}],
            "publicationDate": {"dateTime": f"{day}T10:00:00", "timezone": "Europe/Paris"}, "shortener": False, "smartLinkData": {"ids": []},
            "text": text.replace("{CTA}", CTA), "instagramData": {"type": "POST", "showReelOnFeed": True, "isAiGenerated": False}})
    for day, name, cover, title, tags, text in REELS:
        assert len(title) <= 100 and len(title.replace(" #shorts", "")) <= 90, title
        out.append({"autoPublish": True, "descendants": [], "draft": True, "firstCommentText": "", "hasNotReadNotes": False,
            "media": [f"{cdn}{name}.mp4"], "mediaAltText": [], "providers": [{"network": "instagram"}, {"network": "youtube"}],
            "publicationDate": {"dateTime": f"{day}T18:00:00", "timezone": "Europe/Paris"}, "shortener": False, "smartLinkData": {"ids": []},
            "videoCoverMilliseconds": cover, "text": text.replace("{CTA}", CTA),
            "instagramData": {"type": "REEL", "showReelOnFeed": True, "isAiGenerated": True},
            "youtubeData": {"title": title, "type": "short", "privacy": "public", "madeForKids": False, "isAiGeneratedContent": True,
                            "category": "HOWTO_STYLE", "tags": tags}})
    return out

if __name__ == "__main__":
    d = pathlib.Path(__file__).parent / "build" / "metricool"; d.mkdir(parents=True, exist_ok=True)
    for i, p in enumerate(payloads(sys.argv[1])):
        (d / f"{i+1:02d}.json").write_text(json.dumps(p, ensure_ascii=False))
        print(i + 1, p["publicationDate"]["dateTime"], p["instagramData"]["type"], len(p["text"]), p.get("youtubeData", {}).get("title", ""))
