"""Carrousels CONSEILS 10h00 — semaine du 12 au 18 octobre 2026 (7 slides 1080x1350, réutilise gen_carrousels.py).
Usage : python3 carrousels/gen_semaine_2026-10-12.py  → build/carrousels/k*.png"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_carrousels as g
from gen_carrousels import cover, point, quote, cta
_esc = g.esc
def _esc2(t):
    out = _esc(t)
    for a, b in (("« ", "«&nbsp;"), (" »", "&nbsp;»"), (" :", "&nbsp;:"), (" ?", "&nbsp;?"), (" !", "&nbsp;!"), (" ↓", "&nbsp;↓")):
        out = out.replace(a, b)
    return out
g.esc = _esc2

g.C = {
 "k1-bio-instagram": [
  cover("Instagram · praticiennes", "Votre bio : [5 éléments] qui donnent envie de réserver", "Tarologue, médium, énergéticienne : vérifiez la vôtre."),
  point(2,7,"1","Qui vous êtes, [en clair]","Votre métier en mots simples : « Tarologue et praticienne en guidance », plutôt qu'une formule mystérieuse."),
  point(3,7,"2","Pour [qui] vous travaillez","Une phrase sur les personnes que vous accompagnez et ce qu'elles viennent chercher."),
  point(4,7,"3","Ce que vous [proposez]","Les formats de séance : visio, cabinet, guidance écrite ou vocale."),
  point(5,7,"4","Une seule [action]","« Réservez votre séance ↓ » : un appel clair, pas cinq consignes différentes."),
  point(6,7,"5","Un seul [lien]","Une page avec vos prestations, vos avis et la réservation. Une longue liste de liens fait hésiter.", '<div class="tip">Le test : une inconnue comprend-elle en 3 secondes ce que vous faites ?</div>'),
  cta("Un lien en bio qui mène à tout", ["Votre page praticienne","Vos prestations et vos avis","Réservation et paiement en ligne"]),
 ],
 "k2-avant-seance": [
  cover("Checklist", "Les [10 minutes] avant une séance", "5 gestes pour commencer sereine et disponible."),
  point(2,7,"1","Relisez [sa fiche]","Ses dernières séances, ses questions, ce que vous aviez convenu. Elle se sentira écoutée."),
  point(3,7,"2","Préparez [votre espace]","Un lieu calme et rangé, un verre d'eau à portée de main."),
  point(4,7,"3","Testez [le son et la visio]","Lien, micro, connexion : deux minutes de test évitent dix minutes de stress."),
  point(5,7,"4","Coupez [les notifications]","Téléphone en silencieux, messageries fermées : la séance mérite toute votre attention."),
  point(6,7,"5","Rappelez [le cadre]","En début de séance : la durée, le déroulé, et comment elle recevra le compte rendu."),
  cta("Avec GuidPilot, tout est prêt", ["La fiche et l'historique de la cliente","Le lien Google Meet pour la visio","Le compte rendu livré dans son espace"]),
 ],
 "k3-messages-clientes": [
  cover("Messages prêts à copier", "[5 messages] à envoyer à vos clientes", "De la première prise de contact à l'après-séance."),
  quote(2,7,"Message 1","Accueillir une nouvelle cliente","Merci pour votre confiance. Notre séance durera 45 minutes, en visio. Vous pourrez me poser toutes vos questions."),
  quote(3,7,"Message 2","Confirmer le rendez-vous","Votre séance est bien confirmée pour jeudi à 18 h. Je vous envoie le lien de la visio la veille."),
  quote(4,7,"Message 3","Le rappel de la veille","Petit rappel pour notre séance de demain à 18 h. Voici le lien pour nous retrouver."),
  quote(5,7,"Message 4","Livrer une guidance","Votre guidance est prête. Prenez le temps de la lire au calme, et revenez vers moi si une question se pose."),
  quote(6,7,"Message 5","Reprendre contact","Je pensais à notre dernière séance. Si vous souhaitez faire le point, mes disponibilités sont en ligne."),
  cta("Avec GuidPilot, moins de messages à écrire", ["Confirmation de réservation envoyée","Messagerie avec chaque cliente","Guidances livrées dans son espace"]),
 ],
 "k4-visio-chaleureuse": [
  cover("Séances en visio", "Une visio aussi [chaleureuse] qu'en cabinet", "5 réflexes simples pour vos séances à distance."),
  point(2,7,"1","La lumière [face à vous]","Une fenêtre ou une lampe devant vous, jamais dans votre dos : votre visage reste lisible."),
  point(3,7,"2","La caméra [à hauteur des yeux]","Surélevez l'ordinateur avec quelques livres : le regard devient plus naturel."),
  point(4,7,"3","Le lien [envoyé à l'avance]","La cliente le reçoit avant la séance et n'a pas à le chercher au dernier moment."),
  point(5,7,"4","Un [plan B] prévu","Si la connexion coupe, vous rappelez par téléphone ? Dites-le dès le début."),
  point(6,7,"5","Une fin [soignée]","Résumez en une phrase et annoncez quand arrivera le compte rendu."),
  cta("Vos visios, simplement", ["Lien Google Meet prêt pour la séance","Rendez-vous dans votre agenda","Compte rendu dans l'espace client"]),
 ],
 "k5-notes-seance": [
  cover("Fiches clientes", "Vos notes de séance : [quoi écrire]… et quoi éviter", "Un suivi clair, sans y passer des heures."),
  point(2,7,"1","La [date] et le format","Visio, cabinet, guidance écrite : en un coup d'œil, vous savez où vous en êtes."),
  point(3,7,"2","Les [thèmes] abordés","Quelques mots-clés suffisent : travail, relation, décision à prendre…"),
  point(4,7,"3","La [suite] convenue","Ce que vous avez proposé pour la prochaine fois : vous reprendrez là où vous en étiez."),
  point(5,7,"4","Des faits, [pas de jugements]","Écrivez ce qui a été dit, sans étiquette sur la personne. Relisez-vous comme si elle lisait par-dessus votre épaule."),
  point(6,7,"5","Un endroit [protégé]","Pas de post-it ni de notes dans votre téléphone personnel : ses confidences méritent mieux."),
  cta("Vos fiches clientes, au même endroit", ["L'historique des séances","Des notes jamais visibles par la cliente","Guidances et factures liées"]),
 ],
 "k6-chiffres-du-mois": [
  cover("Praticienne indépendante", "[5 chiffres] à regarder chaque mois", "10 minutes pour savoir où vous en êtes."),
  point(2,7,"1","Le nombre de [séances]","Comparez avec le mois précédent, sans vous juger : une tendance compte plus qu'un chiffre isolé."),
  point(3,7,"2","Ce qui reste [à encaisser]","Un paiement oublié, c'est une séance offerte sans le vouloir. Faites le point une fois par mois."),
  point(4,7,"3","Les clientes [qui reviennent]","Combien ont repris une séance ? C'est un bon signe de confiance."),
  point(5,7,"4","Vos [avis]","La note moyenne, les nouveaux avis, les demandes restées sans réponse."),
  point(6,7,"5","D'où viennent [vos clientes]","Instagram, bouche-à-oreille, annuaire… Vous saurez où mettre votre énergie."),
  cta("Votre tableau de bord GuidPilot", ["Rendez-vous et guidances à livrer","Encaissé et à encaisser","Note moyenne et avis"]),
 ],
 "k7-routine-dimanche": [
  cover("Routine du dimanche", "Préparer votre semaine [en 15 minutes]", "5 étapes pour commencer lundi l'esprit tranquille."),
  point(2,7,"1","Regardez [vos rendez-vous]","Repérez les journées chargées et protégez vos pauses."),
  point(3,7,"2","Listez les [guidances] à livrer","Avec un délai réaliste pour chacune."),
  point(4,7,"3","Vérifiez les [paiements] en attente","Un rappel poli maintenant vaut mieux qu'un oubli dans un mois."),
  point(5,7,"4","Répondez aux [messages] en attente","Une réponse courte suffit : la cliente sait qu'elle a été lue."),
  point(6,7,"5","Bloquez [un moment pour vous]","Un créneau sans clientes, inscrit dans l'agenda comme un rendez-vous."),
  cta("Votre semaine sur un seul écran", ["Vos rendez-vous","Les guidances à livrer","Les paiements à encaisser"]),
 ],
}

if __name__ == "__main__":
    g.main()
