"""Carrousels de la semaine du 23 au 29/11/2026 (10h00) — 1080x1350. Lot automatique du dimanche 22/11.
Mardi 24/11 (thérapeutes, CONSEIL, checklist) : première séance, 5 infos à envoyer avant qu'elle arrive.
Jeudi 26/11 (thérapeutes, CONSEIL, mini-guide pas à pas, contexte fêtes / profil « qui offre une séance ») : la séance offerte à Noël.
Samedi 28/11 (thérapeutes, PROMO série « Pensé pour votre métier » : HYPNOTHÉRAPEUTE, format « 6 questions » + offre de Noël).
Exception validée pour l'offre : le prix (99 €) et la date (31 décembre) apparaissent sur le carrousel PROMO. Aucune personne représentée.
Usage : python3 carrousels/gen_semaine_2026-11-23.py  → build/carrousels/<nom>-NN.png"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import importlib
N = importlib.import_module("gen_noel_2026-11-11")
S2 = importlib.import_module("gen_semaine_2026-11-02")
S = importlib.import_module("gen_semaine_2026-10-19")
g = S.g
cover_v2, second_hook, recap, prob, gp, check, K = S.cover_v2, S.second_hook, S.recap, S.prob, S.gp, S.check, S.K
quest, last_plain = S2.quest, S2.last_plain
price, last_link = N.price, N.last_link

g.C = {
 # Mardi 24/11 10h — CONSEIL thérapeutes — checklist — pilier relation cliente — contexte : la veille de la 1re séance
 "mar-24_carrousel-premiere-seance-5-infos": [
  cover_v2("Première séance : [5 infos] à envoyer avant qu'elle arrive", "La checklist à enregistrer"),
  second_hook(2, 10, "9 h 55, sur votre téléphone", "Je suis devant. C'est quelle porte ?",
              "Une cliente qui arrive stressée commence sa séance avec dix minutes de retard dans la tête. Tout se prépare avant."),
  check(3, 10, "L'adresse, [et comment entrer]", "Code, étage, interphone, où se garer. Ou le lien de visio si la séance est à distance."),
  check(4, 10, "La durée [réelle]", "« Prévoyez 1 h 15 » : l'accueil et l'échange du début font partie de la séance."),
  check(5, 10, "Ce qu'il faut [prévoir]", "Une tenue confortable, une bouteille d'eau… ou rien du tout. Dites-le, même si c'est « rien »."),
  check(6, 10, "Comment [régler]", "Déjà réglé en ligne, ou au cabinet : elle ne doit pas le découvrir à la fin de la séance."),
  check(7, 10, "Vos conditions [d'annulation]", "Écrites, courtes, envoyées avant. Jamais au moment où elle annule."),
  gp(8, 10, "Dans GuidPilot, [la confirmation part toute seule]",
     "À la réservation, votre cliente reçoit un e-mail de confirmation, puis un rappel la veille, avec le lien Google Meet si la séance est à distance. Vos conditions sont acceptées avant le paiement."),
  recap(9, 10, "Avant sa 1re séance", ["L'adresse et comment entrer", "La durée réelle", "Ce qu'il faut prévoir", "Comment régler", "Mes conditions d'annulation"]),
  last_plain(10, 10, "Quelle info oubliez-vous [le plus souvent ?]", "Enregistrez ce post pour votre prochaine nouvelle cliente."),
 ],
 # Jeudi 26/11 10h — CONSEIL thérapeutes — mini-guide pas à pas — pilier attirer / fêtes — profil : la cliente qui offre une séance
 "jeu-26_carrousel-seance-offerte-noel": [
  cover_v2("« Je peux offrir une séance à ma sœur ? » [Oui. Voici comment.]", "Le mini-guide de Noël en 5 étapes"),
  second_hook(2, 10, "Mi-décembre, dans vos messages", "C'est pour un cadeau. Vous faites des bons ?",
              "Une séance offerte, c'est souvent une nouvelle cliente qui ne vous aurait jamais trouvée. Ça se prépare maintenant."),
  prob(3, 10, "Étape 1 · Choisir", "Une prestation [précise,] pas un montant",
       "« Une séance de Reiki d'une heure » parle plus qu'une somme. La personne qui offre sait exactement ce qu'elle donne."),
  prob(4, 10, "Étape 2 · Encaisser", "Le règlement [à la commande]",
       "La personne qui offre règle tout de suite. Notez qui a payé, pour qui, et à quelle date."),
  prob(5, 10, "Étape 3 · Dater", "Une validité [écrite]",
       "Six mois, un an : à vous de choisir, mais écrivez-la sur le bon. Pas de malentendu en juillet."),
  prob(6, 10, "Étape 4 · Remettre", "Un bon [simple et soigné]",
       "Le prénom de la personne, la prestation, la validité et le moyen de vous joindre. Rien de plus."),
  prob(7, 10, "Étape 5 · Accueillir", "Une [nouvelle cliente,] pas un cadeau à écouler",
       "Elle prend rendez-vous quand elle est prête. Accueillez-la comme une nouvelle cliente : c'est exactement ce qu'elle est."),
  gp(8, 10, "Dans GuidPilot, [elle a sa propre fiche]",
     "Dès son premier rendez-vous, sa fiche cliente se crée : historique, notes privées, et le rappel de la veille part tout seul."),
  recap(9, 10, "Ma séance offerte en 5 étapes", ["Une prestation précise", "Réglée à la commande", "Une validité écrite", "Un bon simple et soigné", "Accueillie comme une nouvelle cliente"]),
  last_plain(10, 10, "On vous a déjà demandé [un bon cadeau ?]", "Enregistrez ce post avant les demandes de décembre."),
 ],
 # Samedi 28/11 10h — PROMO série « Pensé pour votre métier » — HYPNOTHÉRAPEUTE — 6 questions + offre de Noël
 "sam-28_carrousel-hypnotherapeute-6-questions": [
  cover_v2("Hypnothérapeute : [6 questions] à vous poser avant de choisir votre outil", "La checklist à enregistrer"),
  prob(2, 10, "Le point de départ", "Réserver un créneau, [ce n'est que le début]",
       "Une séance d'hypnose, c'est aussi un premier échange, un règlement, parfois un audio à réécouter chez soi, vos notes et une facture."),
  quest(3, 10, 1, "Vos prestations affichent-elles [la vraie durée] ?",
        "chaque prestation a sa durée, son tarif et son format, au cabinet ou en visio, sur votre page publique.",
        K / "page_np.png", 1100, (310, 480, 870, 590), maxh=300),
  quest(4, 10, 2, "Le règlement est-il fait [avant le début de la séance] ?",
        "en ligne par carte ou PayPal à la réservation, ou au cabinet, enregistré en un clic."),
  quest(5, 10, 3, "Vos clientes reçoivent-elles [un rappel la veille] ?",
        "confirmation et rappel par e-mail, avec le lien Google Meet pour une séance à distance."),
  quest(6, 10, 4, "Où votre cliente retrouve-t-elle [l'audio à réécouter] ?",
        "dans son espace client sécurisé, avec vos écrits, ses rendez-vous et ses factures.",
        K / "guid.png", 1270, (20, 232, 415, 480), maxh=380),
  quest(7, 10, 5, "Vos notes restent-elles [hors de sa vue] ?",
        "elles sont rangées dans sa fiche, côté praticienne. Votre cliente ne les voit jamais."),
  quest(8, 10, 6, "Vos factures et vos avis [se font-ils sans y penser] ?",
        "factures numérotées automatiquement, demande d'avis envoyée depuis votre espace, avis affichés sur votre page."),
  price(9, 10, "OFFRE DE NOËL", "Un outil pensé pour votre métier, [pas un agenda de plus]", "99 €", "348 €", "1 an, payé une fois · aucun prélèvement automatique",
        "Les six réponses pendant 12 mois. Ensuite, vous choisissez : renouveler au tarif fondateur, passer au mensuel, ou arrêter."),
  last_link(10, 10, "Combien de cases cochez-vous aujourd'hui ?", "guidpilot.fr/offre-fondatrice", "Lien en bio · jusqu'au 31 décembre"),
 ],
}

if __name__ == "__main__":
    g.main()
