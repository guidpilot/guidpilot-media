"""Posts + stories Metricool de la semaine du 19 au 25/10/2026 (2 posts/jour 10h00 et 18h00 + 13 stories).
Usage : python3 posts_2026-10-19.py <SHA>  → imprime un payload JSON par ligne (date|info)."""
import json, sys

SHA = sys.argv[1] if len(sys.argv) > 1 else "SHA"
B = f"https://cdn.jsdelivr.net/gh/guidpilot/guidpilot-media@{SHA}"
W = f"{B}/2026-10-19_au_25"
V = f"{B}/2026-10-19_au_24/v2-tests"
TZ = "Europe/Paris"
H_G = "#tarologue #voyance #guidance #medium #energeticienne"
H_T = "#sophrologue #hypnotherapeute #reiki #therapeuteholistique #cabinetbienetre"

def conseil(accroche, corps, question, kw, tags):
    return f"{accroche}\n\n{corps}\n\n{question} 👇\n\n🔖 Enregistrez ce post pour plus tard.\nBesoin d'un outil pour tout ça ? Commentez {kw}.\n\n{tags}"

def promo(accroche, corps, question, kw, tags):
    return (f"{accroche}\n\n{corps}\n\n{question} 👇\n\n📩 Commentez {kw} et recevez en message privé la présentation de GuidPilot : "
            f"14 jours gratuits, sans carte bancaire.\n👉 Ou lien en bio : guidpilot.fr\n\n{tags}")

def slides(prefix, n, base=W):
    return [f"{base}/{prefix}-{i:02d}.jpg" for i in range(1, n + 1)]

def yt(title, tags):
    assert len(title) <= 90, title
    return {"title": title, "type": "short", "privacy": "public", "madeForKids": False, "isAiGeneratedContent": True,
            "category": "HOWTO_STYLE", "tags": tags}

POSTS = [
 # ---------------- Lundi 19 — guidance ----------------
 ("2026-10-19T10:00:00", "carrousel", slides("lun-19_carrousel-pensent-sans-dire", 9), conseil(
   "Tarologue, voyante, médium : ce que vos clientes pensent sans oser vous le dire.",
   "Avant une guidance, beaucoup de questions restent silencieuses : la durée, le cadre, ce qu'elles recevront après…\nUne cliente qui a ses réponses réserve plus sereinement.\nDans ce carrousel : les 5 questions à anticiper, et quoi dire pour chacune.",
   "Laquelle entendez-vous le plus souvent ?", "GUIDANCE", H_G), None),
 ("2026-10-19T18:00:00", "reel", [f"{V}/lun-19_reel-3-phrases.mp4"], conseil(
   "Tarologue, voyante : 3 phrases qui font fuir vos clientes, sans que vous le sachiez.",
   "1. « Ça dépend… » quand on vous demande le prix → donnez la durée et le tarif, clairement.\n2. « Écrivez-moi quand vous voulez » → proposez un lien pour réserver.\n3. Promettre des réponses → décrivez plutôt comment se passe la séance.",
   "Laquelle avez-vous déjà dite ?", "GUIDANCE", "#tarologue #voyance #guidance #medium #cartomancie"),
  yt("3 phrases qui font fuir vos clientes (tarologue, voyante) #shorts",
     ["tarologue", "voyante", "guidance", "médium", "cartomancienne", "clientes voyance", "conseils tarologue", "praticienne en guidance"])),
 # ---------------- Mardi 20 — thérapeutes ----------------
 ("2026-10-20T10:00:00", "carrousel", slides("mar-20_carrousel-suivi-sans-forcer", 9), conseil(
   "Sophrologue, hypnothérapeute, praticienne Reiki : proposer un suivi en plusieurs séances, sans forcer.",
   "Beaucoup de praticiennes n'osent pas parler de la séance suivante, par peur d'avoir l'air de vendre.\nPourtant, un cadre clair rassure votre cliente : elle sait comment se passe l'accompagnement, et elle garde la main.\nLe mini-guide en 5 étapes, de la première séance au point à mi-parcours.",
   "Et vous, comment proposez-vous la séance suivante ?", "THÉRAPEUTE", H_T), None),
 ("2026-10-20T18:00:00", "reel", [f"{W}/mar-20_reel-seance-1h.mp4"], conseil(
   "Sophrologue, praticienne Reiki, réflexologue : votre séance dure 1 h… mais votre travail, bien plus.",
   "Messages pour caler le rendez-vous, rappel, facture, notes : c'est le temps invisible autour de chaque séance.\n✔ chronométrez-le pendant une semaine\n✔ remplacez les allers-retours de messages par votre lien de réservation\n✔ tenez-en compte dans votre tarif",
   "Combien de temps passez-vous autour d'une séance ?", "THÉRAPEUTE", "#sophrologue #reiki #reflexologie #therapeuteholistique #cabinetbienetre"),
  yt("Sophrologue, Reiki : le temps invisible autour de chaque séance #shorts",
     ["sophrologue", "praticienne reiki", "réflexologue", "thérapeute holistique", "gestion de cabinet", "cabinet bien-être", "temps administratif", "tarif séance"])),
 # ---------------- Mercredi 21 — guidance ----------------
 ("2026-10-21T10:00:00", "carrousel", slides("mer-21_carrousel-fin-annee", 10), conseil(
   "Tarologue, voyante, médium : 6 choses à préparer dès maintenant pour les fêtes de fin d'année.",
   "Congés, horaires du 24 et du 31, séance à offrir, messages d'absence, planning de janvier…\nPréparer en octobre, c'est vivre décembre plus sereinement, pour vous comme pour vos clientes.\nLa checklist complète est dans le carrousel.",
   "Travaillez-vous pendant les fêtes ?", "GUIDANCE", H_G), None),
 ("2026-10-21T18:00:00", "reel", [f"{W}/mer-21_reel-ma-guidance.mp4"], promo(
   "« Vous pouvez me renvoyer ma guidance ? » Tarologue, voyante : et vous la cherchez partout.",
   "Un vocal dans une conversation, un texte dans vos e-mails, un brouillon ailleurs…\nAvec GuidPilot :\n✔ toutes vos guidances, écrites ou vocales, au même endroit\n✔ brouillon ou finalisée : vous savez où vous en êtes\n✔ votre cliente la retrouve seule, dans son espace client sécurisé",
   "Où rangez-vous vos guidances aujourd'hui ?", "GUIDANCE", "#tarologue #voyance #guidance #guidanceecrite #medium"),
  yt("Tarologue, voyante : où ranger vos guidances écrites et vocales ? #shorts",
     ["logiciel tarologue", "guidance écrite", "guidance vocale", "voyante", "médium", "praticienne en guidance", "espace client", "organisation guidance"])),
 # ---------------- Jeudi 22 — thérapeutes ----------------
 ("2026-10-22T10:00:00", "carrousel", slides("jeu-22_carrousel-reservation-en-seance", 8), promo(
   "Sophrologue, hypnothérapeute, praticienne Reiki : vous êtes en séance, et une cliente réserve quand même.",
   "Fini le SMS qui arrive pendant la séance et auquel vous répondez le soir.\nAvec GuidPilot, le parcours en 4 étapes :\n✔ elle ouvre votre page depuis votre lien en bio\n✔ elle choisit son créneau parmi vos disponibilités, et peut régler en ligne\n✔ le rendez-vous arrive dans votre agenda\n✔ la facture se crée toute seule",
   "Combien de messages vous faut-il pour caler un seul rendez-vous ?", "THÉRAPEUTE", "#sophrologue #hypnotherapeute #reiki #cabinetbienetre #logicielpraticien"), None),
 ("2026-10-22T18:00:00", "reel", [f"{W}/jeu-22_reel-premier-appel.mp4"], conseil(
   "Sophrologue, hypnothérapeute, coach : une cliente appelle pour « se renseigner ». Que lui dire ?",
   "✔ demandez-lui d'abord ce qu'elle attend de l'accompagnement\n✔ expliquez simplement le déroulé : durée, lieu ou visio, première séance\n✔ proposez un créneau précis plutôt que « rappelez-moi »\n✖ ne promettez jamais de résultat : décrivez votre accompagnement",
   "Que dites-vous, vous, au premier appel ?", "THÉRAPEUTE", "#sophrologue #hypnotherapeute #coachdevie #therapeuteholistique #cabinetbienetre"),
  yt("Sophrologue, hypnothérapeute : que dire au premier appel d'une cliente #shorts",
     ["sophrologue", "hypnothérapeute", "coach de vie", "premier appel cliente", "thérapeute holistique", "gestion de cabinet", "trouver des clients", "praticienne bien-être"])),
 # ---------------- Vendredi 23 — guidance ----------------
 ("2026-10-23T10:00:00", "carrousel", slides("ven-23_carrousel-question-gratuite", 8, V), conseil(
   "« Juste une petite question… » : tarologue, voyante, comment répondre sans offrir votre guidance ?",
   "Ces petites questions par message n'ont ni le cadre ni le temps d'une vraie guidance.\nY répondre gratuitement apprend à vos clientes que votre travail ne se paie pas.\nDans le carrousel : 3 messages prêts à copier, pour une nouvelle cliente, une cliente fidèle, et quand elle insiste.",
   "Combien de « petites questions » recevez-vous par semaine ?", "GUIDANCE", "#tarologue #voyance #guidance #medium #cartomancie"), None),
 ("2026-10-23T18:00:00", "reel", [f"{W}/ven-23_reel-rythme-guidance.mp4"], conseil(
   "Tarologue, voyante : votre cliente revient chaque semaine ? Ce n'est pas forcément une bonne nouvelle.",
   "Quand les séances s'enchaînent, elle repose souvent la même question, avant d'avoir pu avancer.\n✔ proposez un rythme : quelques semaines entre deux séances\n✔ expliquez pourquoi, avec douceur\n✔ notez la date de chaque séance pour voir si elles se rapprochent",
   "Quel rythme conseillez-vous à vos clientes ?", "GUIDANCE", H_G),
  yt("Tarologue, voyante : à quel rythme proposer une nouvelle guidance ? #shorts",
     ["tarologue", "voyante", "guidance", "médium", "énergéticienne", "fréquence guidance", "éthique voyance", "praticienne en guidance"])),
 # ---------------- Samedi 24 — thérapeutes ----------------
 ("2026-10-24T10:00:00", "carrousel", slides("sam-24_carrousel-semaine-type", 9), conseil(
   "Sophrologue, praticienne Reiki, réflexologue : votre semaine type de cabinet en 5 blocs, pour ne plus déborder.",
   "Prendre les rendez-vous « quand les clientes peuvent », c'est souvent des trous partout et des soirées qui débordent.\nPlages de séances fixes, une heure d'administratif, des pauses, deux créneaux de réponse, un jour vraiment off.\nLe détail de chaque bloc est dans le carrousel.",
   "Quel bloc vous manque le plus ?", "THÉRAPEUTE", "#sophrologue #reiki #reflexologie #therapeuteholistique #cabinetbienetre"), None),
 ("2026-10-24T18:00:00", "concours", [f"{W}/sam-24_reel-concours-2-jours.mp4"],
  "⏳ Plus que 2 jours pour gagner 1 an de GuidPilot ! Praticiennes en guidance et thérapeutes du bien-être, c'est maintenant.\n\n"
  "À gagner :\n✔ 1 an d'abonnement GuidPilot offert\n✔ + 2 abonnements de 3 mois\n\n"
  "Pour participer :\n1️⃣ Abonnez-vous à @guidpilot.fr\n2️⃣ Aimez cette publication\n3️⃣ Commentez « GuidPilot »\n\n"
  "🗓️ Fin du jeu le lundi 26 octobre 2026 à 23h59, tirage au sort le mardi 27 octobre.\n\n"
  "📩 En commentant GuidPilot, vous recevez la confirmation de participation en message privé.\n\n"
  "Ce jeu n'est ni organisé, ni parrainé, ni géré par Instagram.\n\n#jeuconcours #tarologue #sophrologue #reiki #guidpilot", None),
 # ---------------- Dimanche 25 — guidance ----------------
 ("2026-10-25T10:00:00", "carrousel", slides("dim-25_carrousel-lien-en-bio", 8), promo(
   "Tarologue, voyante, médium : votre lien en bio mène… à vos messages privés ?",
   "Une cliente curieuse veut voir vos prestations, votre façon de travailler et des avis, sans avoir à vous écrire.\nAvec votre page praticienne GuidPilot :\n✔ qui vous êtes : photo, spécialité, format, note moyenne\n✔ votre façon de travailler, avec vos mots\n✔ un bouton « Prendre rendez-vous »\n✔ les avis de vos clientes",
   "Où mène votre lien en bio aujourd'hui ?", "GUIDANCE", "#tarologue #voyance #guidance #medium #logicielpraticien"), None),
 ("2026-10-25T18:00:00", "reel", [f"{W}/dim-25_reel-augmenter-tarifs.mp4"], conseil(
   "Tarologue, voyante, médium : 3 signes qu'il est temps d'augmenter vos tarifs.",
   "1. Votre agenda est plein plusieurs semaines à l'avance.\n2. Vos prix n'ont pas bougé depuis longtemps, alors que votre expérience a grandi.\n3. Vous travaillez plus, sans gagner mieux.\nPour le faire : prévenez un mois avant, gardez l'ancien prix pour les séances déjà réservées, et annoncez-le simplement.",
   "À quand remonte votre dernière hausse ?", "GUIDANCE", H_G),
  yt("Tarologue, voyante : 3 signes qu'il est temps d'augmenter vos tarifs #shorts",
     ["tarologue", "voyante", "tarif voyance", "augmenter ses prix", "médium", "praticienne en guidance", "fixer ses tarifs", "énergéticienne"])),
]

STORIES = [
 ("2026-10-19T08:30:00", "lun-19_0830_mot-cle-guidance"), ("2026-10-19T20:00:00", "lun-19_2000_teaser-3-phrases"),
 ("2026-10-20T08:30:00", "mar-20_0830_conseil-rappel-veille"), ("2026-10-20T20:00:00", "mar-20_2000_teaser-seance-1h"),
 ("2026-10-21T08:30:00", "mer-21_0830_concours-5-jours"), ("2026-10-21T20:00:00", "mer-21_2000_teaser-ma-guidance"),
 ("2026-10-22T08:30:00", "jeu-22_0830_mot-cle-therapeute"), ("2026-10-22T20:00:00", "jeu-22_2000_teaser-premier-appel"),
 ("2026-10-23T08:30:00", "ven-23_0830_question-malaise"), ("2026-10-23T20:00:00", "ven-23_2000_teaser-rythme"),
 ("2026-10-24T08:30:00", "sam-24_0830_fonction-journee"), ("2026-10-24T20:00:00", "sam-24_2000_teaser-concours-2-jours"),
 ("2026-10-25T12:30:00", "dim-25_1230_mot-cle-guidance"),
]


# ---- Révision du 18/10/2026 au soir (demande de Normane : varier structures, accroches, contextes, et relier chaque conseil à GuidPilot) ----
def conseil2(accroche, corps, gp, question, kw, tags):
    return f"{accroche}\n\n{corps}\n\n{gp}\n\n{question} 👇\n\n🔖 Enregistrez ce post pour plus tard.\nBesoin d'un outil pour tout ça ? Commentez {kw}.\n\n{tags}"

OVERRIDE_TEXT = {
 "2026-10-19T10:00:00": conseil2(
   "Et si vos clientes de guidance n'osaient pas vous poser leurs vraies questions ?",
   "« Combien de temps ça dure ? », « Je pourrai relire tout ça ? », « Je n'ose pas lui réécrire »…\n5 pensées silencieuses de vos clientes, et la phrase simple à leur dire pour chacune.\nUne cliente qui a ses réponses réserve plus sereinement.",
   "Dans GuidPilot, la durée et le format de chaque prestation s'affichent sur votre page, et la guidance l'attend ensuite dans son espace client.",
   "Laquelle entendez-vous le plus souvent ?", "GUIDANCE", "#tarologue #voyance #guidance #medium #energeticienne"),
 "2026-10-19T18:00:00": conseil2(
   "Vous dites peut-être ces 3 phrases à vos clientes de tarot ou de voyance… sans savoir qu'elles les font fuir.",
   "« Ça dépend… » quand on vous demande le prix → donnez la durée et le tarif, clairement.\n« Écrivez-moi quand vous voulez » → proposez un lien pour réserver.\nPromettre des réponses → décrivez plutôt comment se passe la séance.",
   "Dans GuidPilot, votre lien de réservation affiche la durée et le format de chaque séance : plus besoin de « ça dépend ».",
   "Laquelle avez-vous déjà dite ?", "GUIDANCE", "#tarologue #voyance #guidance #medium #cartomancie"),
 "2026-10-20T10:00:00": conseil2(
   "« Revenez quand vous voulez » : la phrase à remplacer pour proposer un suivi sans forcer (sophrologue, Reiki, hypnose).",
   "4 situations, 4 phrases à changer : à la fin de la première séance, quand elle hésite, avant qu'elle reparte, et à la séance suivante.\nUn cadre clair rassure votre cliente, et elle reste libre à chaque fois.",
   "Dans GuidPilot, vous planifiez le rendez-vous suivant en un clic, et vos notes de séance restent privées dans sa fiche cliente.",
   "Comment proposez-vous la séance suivante ?", "THÉRAPEUTE", "#sophrologue #hypnotherapeute #reiki #therapeuteholistique #cabinetbienetre"),
 "2026-10-20T18:00:00": conseil2(
   "1 h de séance, presque 2 h de travail : sophrologue, réflexologue, praticienne Reiki, faites le calcul.",
   "Par exemple : 15 min de messages pour caler le rendez-vous, 5 min de rappel, 15 min d'encaissement et de facture, 10 min de notes.\nLe premier temps à récupérer : les allers-retours. Envoyez votre lien de réservation au lieu de proposer des créneaux.",
   "Dans GuidPilot, la cliente réserve sur votre page, et la facture se crée toute seule.",
   "Combien de temps passez-vous autour d'une séance ?", "THÉRAPEUTE", "#sophrologue #reiki #reflexologie #therapeuteholistique #cabinetbienetre"),
 "2026-10-21T10:00:00": conseil2(
   "Décembre arrive plus vite qu'on ne croit : la checklist des fêtes pour tarologues, voyantes et médiums.",
   "Congés, horaires du 24 et du 31, séance à offrir, messages d'absence, planning de janvier.\nPréparer en octobre, c'est vivre décembre plus sereinement, pour vous comme pour vos clientes.",
   "Dans GuidPilot, vos clientes peuvent offrir une séance en carte cadeau à votre logo, et vos congés se bloquent dans votre agenda.",
   "Travaillez-vous pendant les fêtes ?", "GUIDANCE", "#tarologue #voyance #guidance #medium #energeticienne"),
 "2026-10-22T18:00:00": conseil2(
   "Le téléphone sonne : « Je voulais juste me renseigner… » Sophrologue, hypnothérapeute, voici quoi répondre.",
   "✖ le réflexe : raconter tout votre parcours\n✔ poser une question : « Qu'est-ce qui vous amène ? »\n✔ expliquer le déroulé en une phrase\n✔ proposer un créneau précis plutôt que « rappelez-moi »",
   "Dans GuidPilot, si elle préfère réserver plus tard, vous lui envoyez le lien de votre page : elle choisit son créneau seule.",
   "Que dites-vous, vous, au premier appel ?", "THÉRAPEUTE", "#sophrologue #hypnotherapeute #coachdevie #therapeuteholistique #cabinetbienetre"),
 "2026-10-23T10:00:00": conseil2(
   "« Juste une petite question… » : tarologue, voyante, comment répondre sans offrir votre guidance ?",
   "Ces petites questions par message n'ont ni le cadre ni le temps d'une vraie guidance.\nY répondre gratuitement apprend à vos clientes que votre travail ne se paie pas.\nDans le carrousel : 3 messages prêts à copier, pour une nouvelle cliente, une cliente fidèle, et quand elle insiste.",
   "Dans GuidPilot, votre page de réservation est le lien à glisser dans chacune de ces réponses.",
   "Combien de « petites questions » recevez-vous par semaine ?", "GUIDANCE", "#tarologue #voyance #guidance #medium #cartomancie"),
 "2026-10-23T18:00:00": conseil2(
   "Une cliente qui revient chaque semaine pour une guidance : bon signe ? Pas forcément.",
   "Une guidance a besoin de temps pour se vivre. Trop rapprochées, les séances tournent autour de la même question.\nProposez un rythme, avec douceur : « Laissons passer quelques semaines. »",
   "Dans GuidPilot, ses guidances sont rangées avec leur date : vous voyez tout de suite si elles se rapprochent.",
   "Quel rythme conseillez-vous à vos clientes ?", "GUIDANCE", "#tarologue #voyance #guidance #medium #energeticienne"),
 "2026-10-24T10:00:00": conseil2(
   "Modèle à recopier : la semaine type d'une sophrologue, praticienne Reiki ou réflexologue qui ne déborde plus.",
   "Des plages de séances fixes, une heure d'administratif par semaine, deux créneaux de réponse par jour, des pauses, un jour vraiment off.\nLe modèle en couleurs est dans le carrousel.",
   "Dans GuidPilot, vos clientes ne réservent que dans les disponibilités que vous ouvrez : votre semaine type se respecte toute seule.",
   "Quel bloc vous manque le plus ?", "THÉRAPEUTE", "#sophrologue #reiki #reflexologie #therapeuteholistique #cabinetbienetre"),
 "2026-10-25T18:00:00": conseil2(
   "Agenda plein, prix inchangés depuis longtemps ? Tarologue, voyante : 3 signes qu'il est temps d'augmenter vos tarifs.",
   "1. Votre agenda est plein plusieurs semaines à l'avance.\n2. Vos prix n'ont pas bougé, alors que votre expérience a grandi.\n3. Vous travaillez plus, sans gagner mieux.\nPour le faire : prévenez un mois avant, et gardez l'ancien prix pour les séances déjà réservées.",
   "Dans GuidPilot, votre tableau de bord suit vos revenus du mois et votre panier moyen.",
   "À quand remonte votre dernière hausse ?", "GUIDANCE", "#tarologue #voyance #guidance #medium #energeticienne"),
}
OVERRIDE_YT = {
 "2026-10-22T18:00:00": "Sophrologue : que répondre quand une cliente appelle pour se renseigner #shorts",
 "2026-10-23T18:00:00": "Tarologue : une cliente qui revient chaque semaine, bon signe ? #shorts",
}
STORY_TIME = {"08:30": "12:30"}  # stories de 8h30 déplacées à 12h30 (Normane, 18/10/2026)

def offset(dt):  # passage à l'heure d'hiver le dimanche 25/10/2026 à 3 h
    return "+01:00" if dt >= "2026-10-25T03:00:00" else "+02:00"

def payloads():
    for dt, kind, media, text, ytd in POSTS:
        info = {"autoPublish": True, "draft": False, "descendants": [], "firstCommentText": "", "hasNotReadNotes": False,
                "media": media, "mediaAltText": [], "publicationDate": {"dateTime": dt, "timezone": TZ}, "shortener": False,
                "smartLinkData": {"ids": []}, "text": OVERRIDE_TEXT.get(dt, text)}
        if kind == "carrousel":
            info["providers"] = [{"network": "instagram"}]
            info["instagramData"] = {"type": "POST", "isAiGenerated": False}
        else:
            info["instagramData"] = {"type": "REEL", "showReelOnFeed": True, "isAiGenerated": True}
            info["videoCoverMilliseconds"] = 1500 if kind == "concours" else 500
            if ytd:
                info["providers"] = [{"network": "instagram"}, {"network": "youtube"}]
                info["youtubeData"] = dict(ytd, title=OVERRIDE_YT.get(dt, ytd["title"]))
            else:
                info["providers"] = [{"network": "instagram"}]
        yield dt + offset(dt), info
    for dt, name in STORIES:
        dt = dt.replace("T08:30", "T12:30")
        info = {"autoPublish": True, "draft": False, "descendants": [], "firstCommentText": "", "hasNotReadNotes": False,
                "media": [f"{W}/stories/{name}.jpg"], "mediaAltText": [], "publicationDate": {"dateTime": dt, "timezone": TZ},
                "shortener": False, "smartLinkData": {"ids": []}, "providers": [{"network": "instagram"}],
                "instagramData": {"type": "STORY", "isAiGenerated": False}}
        yield dt + offset(dt), info

if __name__ == "__main__":
    for d, info in payloads():
        print(d + "|" + json.dumps(info, ensure_ascii=False))
