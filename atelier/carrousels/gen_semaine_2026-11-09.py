"""Carrousels de la semaine du 09 au 15/11/2026 (10h00) — 1080x1350.
Réutilise les helpers de gen_semaine_2026-10-19.py et gen_semaine_2026-11-02.py, ajoute :
  - msg() : « message prêt à copier » (étiquette + carte de message) ;
Jeudi 12/11 (thérapeutes, CONSEIL) : annulation de dernière minute, 4 réponses prêtes à copier.
Samedi 14/11 (thérapeutes, PROMO série « Pensé pour votre métier ») : la journée d'une réflexologue, avant / après.
Usage : python3 carrousels/gen_semaine_2026-11-09.py  → build/carrousels/<nom>-NN.png"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import importlib
S2 = importlib.import_module("gen_semaine_2026-11-02")
S = importlib.import_module("gen_semaine_2026-10-19")
g = S.g
esc, cover_v2, second_hook, recap, last_promo, prob, gp, swap, FOOT, K = S.esc, S.cover_v2, S.second_hook, S.recap, S.last_promo, S.prob, S.gp, S.swap, S.FOOT, S.K
last_plain = S2.last_plain

g.CSS += """
.mlab{align-self:flex-start;display:inline-block;padding:14px 30px;border-radius:999px;background:#0F172A;color:#E9C46A;font-weight:800;font-size:30px;letter-spacing:.08em}
.s.m h2{font-size:60px;margin-top:30px}
.msg{margin-top:40px;background:#fff;border:2px solid #E2E8F0;border-radius:32px;padding:40px 44px;font-weight:600;font-size:40px;line-height:1.42;color:#0F172A;position:relative;box-shadow:0 20px 50px rgba(15,23,42,.08)}
.msg:before{content:"💬";position:absolute;right:30px;top:-34px;font-size:60px}
.msg small{display:block;margin-top:22px;font-weight:700;font-size:28px;color:#2563EB;letter-spacing:.06em;text-transform:uppercase}
.swap>div{font-size:40px !important}
"""


def msg(n, total, label, title, text, why):
    return (f'<div class="s light m"><div class="page">{n}/{total}</div><div class="mlab">{esc(label)}</div>'
            f'<h2>{esc(title)}</h2><div class="msg">«&nbsp;{esc(text)}&nbsp;»<small>{esc(why)}</small></div>{FOOT}</div>')


g.C = {
 # Jeudi 12/11 10h — CONSEIL thérapeutes — messages prêts à copier — pilier relation / limites — contexte : le jour J
 "jeu-12_carrousel-annulation-4-reponses": [
  cover_v2("Elle annule [une heure avant.] 4 réponses prêtes à copier", "À enregistrer pour le jour J"),
  second_hook(2, 10, "Vous connaissez ce message ?", "Désolée, je ne pourrai pas venir cet après-midi… on reporte ?",
              "Répondre à chaud, c'est le piège : trop sec, ou trop conciliant. Voici quoi écrire, selon le cas."),
  msg(3, 10, "Cas 1 · Première fois", "Elle prévient, [c'est la première fois]",
      "Merci de m'avoir prévenue. Ça arrive. Je vous propose de choisir un nouveau créneau avec mon lien de réservation, pour que la séance ait bien lieu.",
      "Pourquoi : vous restez souple, mais vous gardez la main sur la suite."),
  msg(4, 10, "Cas 2 · Ça se répète", "Deuxième annulation [en peu de temps]",
      "Je comprends. C'est la deuxième fois : pour la prochaine séance, je vous demanderai un acompte à la réservation, comme pour toutes mes clientes.",
      "Pourquoi : la règle s'applique à toutes, ce n'est pas contre elle."),
  msg(5, 10, "Cas 3 · Conditions acceptées", "Elle avait accepté [vos conditions]",
      "Comme indiqué lors de votre réservation, l'annulation à moins de 24 h entraîne la retenue de l'acompte. Je reste disponible pour une nouvelle date.",
      "Pourquoi : pas de négociation, pas de justification : la règle était écrite."),
  msg(6, 10, "Cas 4 · Absence sans prévenir", "Elle n'est [pas venue]",
      "Je vous attendais à 15 h aujourd'hui. J'espère que tout va bien de votre côté. Si vous souhaitez reprendre, voici mon lien pour choisir un créneau.",
      "Pourquoi : vous constatez, sans reproche. Elle décidera de la suite."),
  swap(7, 10, "Le ton qui protège la relation", "« Ce n'est pas grave, ne vous inquiétez pas ! » … et vous absorbez le créneau perdu.",
       "« Je comprends. Comme prévu dans mes conditions, … » : clair, doux, et sans discussion."),
  gp(8, 10, "Vos conditions, [acceptées avant la séance]",
     "Avec la réservation en ligne, vos conditions d'annulation sont affichées et acceptées avant le paiement ; l'acompte éventuel est déjà réglé. Et le rappel par e-mail la veille réduit les oublis."),
  recap(9, 10, "Annulation de dernière minute", ["Répondez posément, pas à chaud", "Rappelez la règle, sans vous justifier", "Proposez un nouveau créneau avec votre lien", "La même règle pour toutes"]),
  last_plain(10, 10, "Quelle est votre règle [d'annulation ?]", "Enregistrez ce post pour la prochaine fois."),
 ],
 # Samedi 14/11 10h — PROMO thérapeutes — série « Pensé pour votre métier » — métier : réflexologue — format avant / après sur une journée
 "sam-14_carrousel-reflexologue-journee": [
  cover_v2("Réflexologue : [une journée,] deux façons de la vivre", "Série « Pensé pour votre métier »"),
  prob(2, 10, "Le point de départ", "Un agenda en ligne, [c'est un bon début]",
       "Mais entre deux séances, il reste les messages, les paiements, les comptes rendus et les factures. Voici la même journée, avec un outil pensé pour votre cabinet."),
  swap(3, 10, "8 h 30 · Avant la première séance", "Relire vos SMS pour retrouver qui vient, et à quelle heure.",
       "Votre agenda du jour, avec la fiche de chaque cliente et vos notes privées."),
  swap(4, 10, "10 h · Une cliente réserve pendant votre séance", "Un message sans réponse jusqu'à midi… elle réserve ailleurs.",
       "Elle choisit son créneau sur votre page et règle en ligne. Vous le découvrez en sortant."),
  swap(5, 10, "12 h 15 · Fin de séance, paiement au cabinet", "« Payé en espèces » noté sur un carnet, la facture « plus tard ».",
       "Un clic : paiement enregistré, facture numérotée créée."),
  swap(6, 10, "14 h · Séance à distance", "Envoyer le lien de visio à la main, en espérant qu'elle le voie.",
       "Le lien Google Meet est parti avec la confirmation et le rappel par e-mail."),
  swap(7, 10, "18 h · Après la dernière séance", "Un compte rendu par SMS, perdu dans le fil de la conversation.",
       "Votre compte rendu, écrit ou vocal, déposé dans son espace sécurisé."),
  gp(8, 10, "21 h · [Votre soirée]",
     "Dans GuidPilot, les factures du jour sont faites, les paiements suivis, et les rappels de demain partiront seuls. Il ne reste rien à rattraper le soir.",
     K / "dash_np.png", 1270, (20, 360, 1250, 550), maxh=300),
  recap(9, 10, "Un outil pensé pour votre métier, pas un agenda de plus.",
        ["Fiches clientes et notes privées", "Réservation et paiement en ligne", "Paiement au cabinet en un clic", "Lien de visio automatique", "Compte rendu dans l'espace client", "Factures numérotées"]),
  last_promo(10, 10, "Votre journée ressemble [à laquelle ?]", "THÉRAPEUTE"),
 ],
}

if __name__ == "__main__":
    g.main()
