"""Carrousels de la semaine du 16 au 22/11/2026 (10h00) — 1080x1350. Lot lancé à la main par Normane (formats nouveaux).
Lundi 16/11 (guidance, CONSEIL, « modèle à remplir ») : votre bilan 2026 en 4 questions.
Vendredi 20/11 (guidance, CONSEIL, mini-guide pas à pas, contexte inédit : le salon) : repartir d'un salon avec des rendez-vous.
Samedi 21/11 (thérapeutes, OFFRE DE NOËL, checklist « liste de souhaits ») : la liste au Père Noël en 5 lignes.
Exception validée pour l'offre : le prix (99 €) et la date (31 décembre) apparaissent. Aucune personne représentée.
Usage : python3 carrousels/gen_semaine_2026-11-16.py  → build/carrousels/<nom>-NN.png"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import importlib
N = importlib.import_module("gen_noel_2026-11-11")   # price(), last_link() + CSS de l'offre
S2 = importlib.import_module("gen_semaine_2026-11-02")
S = importlib.import_module("gen_semaine_2026-10-19")
g = S.g
esc, cover_v2, second_hook, recap, prob, gp, check, K = S.esc, S.cover_v2, S.second_hook, S.recap, S.prob, S.gp, S.check, S.K
quest, last_plain = S2.quest, S2.last_plain
price, last_link = N.price, N.last_link

g.C = {
 # Lundi 16/11 10h — CONSEIL guidance — modèle à remplir — pilier pilotage / saison — contexte : fin d'année
 "lun-16_carrousel-bilan-2026-4-questions": [
  cover_v2("Votre bilan 2026 [en 4 questions]", "10 minutes, un carnet, pas de tableur"),
  second_hook(2, 9, "Le réflexe de fin d'année", "Je ferai le point en janvier… quand j'aurai le temps.",
              "Quatre questions suffisent. Répondez-y maintenant, pendant que l'année est encore fraîche."),
  prob(3, 9, "Question 1", "D'où sont venues [vos clientes ?]",
        "Instagram, bouche-à-oreille, annuaire, salon… Notez la source des dix dernières. C'est là qu'il faudra mettre votre énergie en 2027."),
  prob(4, 9, "Question 2", "Quelle prestation a été [la plus demandée ?]",
        "Celle qu'on vous réserve le plus n'est pas toujours celle que vous mettez en avant. Placez-la en premier sur votre page."),
  prob(5, 9, "Question 3", "Qu'est-ce qui vous a pris [le plus de temps] hors séance ?",
        "Messages pour caler un rendez-vous, paiements à vérifier, factures du soir… Nommez-le : c'est la première chose à simplifier."),
  prob(6, 9, "Question 4", "Qui n'est [pas revenue ?]",
        "Relisez la liste de vos clientes de l'année. Un message simple, sans promotion, suffit souvent à renouer."),
  gp(7, 9, "Dans GuidPilot, [une partie des réponses est déjà là]",
     "L'historique de chaque cliente et vos encaissements du mois sont dans votre espace : de quoi répondre sans tableur.",
     K / "dash_np.png", 1270, (20, 360, 1250, 550), maxh=300),
  recap(8, 9, "Mon bilan 2026", ["D'où viennent mes clientes", "Ma prestation la plus demandée", "Ce qui me prend trop de temps", "Celles à qui réécrire"]),
  last_plain(9, 9, "Quelle réponse vous a [surprise ?]", "Enregistrez ce post pour votre bilan de décembre."),
 ],
 # Vendredi 20/11 10h — CONSEIL guidance — mini-guide pas à pas — pilier attirer des clientes — contexte : salon du bien-être
 "ven-20_carrousel-salon-rendez-vous": [
  cover_v2("Salon du bien-être : repartez avec [des rendez-vous,] pas des cartes de visite", "Le mini-guide en 5 étapes"),
  second_hook(2, 10, "Le lendemain du salon", "J'ai parlé à soixante personnes… et personne n'a rappelé.",
              "Sur un stand, l'envie de réserver dure quelques minutes. Tout se joue sur place."),
  prob(3, 10, "Étape 1 · Avant le salon", "Une prestation [« spéciale salon »]",
       "Un format court, un tarif clair, une durée affichée. Une seule offre à expliquer : plus simple pour vous, plus simple pour elles."),
  prob(4, 10, "Étape 2 · Sur votre table", "Votre lien de réservation [en QR code]",
       "Imprimé en grand. Elles le scannent, voient vos créneaux et réservent pendant que vous parlez à la personne suivante."),
  prob(5, 10, "Étape 3 · Pendant l'échange", "Une question, [pas un discours]",
       "« Qu'est-ce qui vous amène aujourd'hui ? » Écoutez deux minutes avant de présenter quoi que ce soit."),
  prob(6, 10, "Étape 4 · Avant qu'elle parte", "Proposez [une date]",
       "« Je vous montre mes créneaux de la semaine prochaine ? » Une date choisie sur place vaut dix cartes de visite."),
  prob(7, 10, "Étape 5 · Le soir même", "Un message [aux personnes rencontrées]",
       "Court, personnel, avec votre lien. Demandez toujours leur accord avant de noter leurs coordonnées."),
  gp(8, 10, "Dans GuidPilot, [votre lien fait le reste]",
     "Il mène à votre page : prestations avec tarif et durée, créneaux ouverts, paiement en ligne possible. Le rendez-vous arrive dans votre agenda, sans rien ressaisir."),
  recap(9, 10, "Ma checklist salon", ["Une prestation courte, tarif affiché", "Mon lien en QR code sur la table", "Une question avant de parler de moi", "Une date proposée sur place", "Un message le soir même"]),
  last_plain(10, 10, "Vous exposez [cet hiver ?]", "Enregistrez ce post avant votre prochain salon."),
 ],
 # Samedi 21/11 10h — OFFRE DE NOËL thérapeutes — checklist « liste de souhaits » — angle cadeau
 "sam-21_carrousel-noel-liste-de-souhaits": [
  cover_v2("Cette année, votre liste au Père Noël tient [en 5 lignes.]", "Offre de Noël · jusqu'au 31 décembre"),
  second_hook(2, 9, "Cher Père Noël,", "Cette année, je ne veux ni bougie ni agenda papier. Je veux des soirées.",
              "Cinq souhaits que beaucoup de thérapeutes partagent. Cochez les vôtres."),
  check(3, 9, "Ne plus [relancer un paiement]", "Le règlement se fait à la réservation, ou s'enregistre en un clic au cabinet."),
  check(4, 9, "Ne plus faire [mes factures le soir]", "Chaque paiement crée sa facture numérotée, toute seule."),
  check(5, 9, "Ne plus répondre [« vous êtes dispo quand ? »]", "Vos clientes voient vos créneaux et réservent sans vous écrire."),
  check(6, 9, "Ne plus chercher [un compte rendu]", "Écrit ou vocal, il attend votre cliente dans son espace privé."),
  check(7, 9, "Oser [demander un avis]", "La demande part depuis votre espace, et l'avis s'affiche sur votre page."),
  price(8, 9, "OFFRE DE NOËL", "Les cinq, [dans un seul cadeau]", "99 €", "348 €", "1 an, payé une fois · aucun prélèvement automatique",
        "Un an de GuidPilot, toutes les fonctions. Ensuite, vous choisissez : renouveler au tarif fondateur, passer au mensuel, ou arrêter."),
  last_link(9, 9, "Quel souhait cochez-vous en premier ?", "guidpilot.fr/offre-fondatrice", "Lien en bio · jusqu'au 31 décembre"),
 ],
}

if __name__ == "__main__":
    g.main()
