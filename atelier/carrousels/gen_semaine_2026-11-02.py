"""Carrousels de la semaine du 02 au 08/11/2026 (1 post par jour, 10h00) — 1080x1350.
Réutilise les helpers de gen_semaine_2026-10-19.py et ajoute :
  - myth()  : « Idée reçue » (rouge) → « En réalité » (vert), format mythe / réalité ;
  - quest() : question numérotée de la série « Pensé pour votre métier » + réponse « Dans GuidPilot », capture optionnelle ;
  - last_plain() : dernière slide CONSEIL sans ligne mot-clé (règle du 20/10 : au plus 1 conseil par semaine avec mot-clé).
Usage : python3 carrousels/gen_semaine_2026-11-02.py  → build/carrousels/<nom>-NN.png"""
import base64, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import importlib
S = importlib.import_module("gen_semaine_2026-10-19")
g = S.g
esc, cover_v2, second_hook, recap, last_promo, prob, gp, FOOT, K, A = S.esc, S.cover_v2, S.second_hook, S.recap, S.last_promo, S.prob, S.gp, S.FOOT, S.K, S.A

g.CSS += """
.mr{margin-top:40px;display:flex;flex-direction:column;gap:30px}
.mr>div{border-radius:28px;padding:34px 40px;font-weight:600;font-size:44px;line-height:1.38}
.mr .no{background:#FEF2F2;border:2px solid #FECACA;color:#0F172A}
.mr .yes{background:#F0FDF4;border:2px solid #BBF7D0;color:#0F172A}
.mr b{display:block;font-weight:800;font-size:28px;letter-spacing:.1em;margin-bottom:12px}
.mr .no b{color:#B91C1C}.mr .yes b{color:#15803D}
.qn{align-self:flex-start;display:inline-block;padding:14px 30px;border-radius:999px;background:#2563EB;color:#fff;font-weight:800;font-size:30px;letter-spacing:.08em}
.ans{margin-top:36px;background:#fff;border:2px solid #E2E8F0;border-left:12px solid #E9C46A;border-radius:24px;padding:28px 36px;font-weight:600;font-size:38px;line-height:1.4;color:#334155}
.ans b{color:#0F172A}
.s.q h2{font-size:70px}
.s.qs{justify-content:flex-start;padding-top:180px}
.s.qs h2{font-size:62px}
.s.qs .ans{font-size:34px;margin-top:26px}
"""


def myth(n, total, idee, realite):
    return (f'<div class="s light"><div class="page">{n}/{total}</div><div class="kicker">Idée reçue n°{n - 2}</div>'
            f'<div class="mr"><div class="no"><b>✕ CE QU\'ON CROIT</b>«&nbsp;{esc(idee)}&nbsp;»</div>'
            f'<div class="yes"><b>✓ EN RÉALITÉ</b>{esc(realite)}</div></div>{FOOT}</div>')


def _frame(img, W, box, maxw=888, maxh=420):
    x0, y0, x1, y1 = box
    sc = min(maxw / (x1 - x0), maxh / (y1 - y0))
    fw, fh = round((x1 - x0) * sc), round((y1 - y0) * sc)
    b64 = base64.b64encode(open(img, "rb").read()).decode()
    return (f'<div class="frame" style="width:{fw}px"><div class="bar"><i></i><i></i><i></i><span>Compte de démonstration</span></div>'
            f'<div class="vp" style="height:{fh}px"><img src="data:image/png;base64,{b64}" style="width:{round(W * sc)}px;left:{-round(x0 * sc)}px;top:{-round(y0 * sc)}px"></div></div>')


def quest(n, total, num, question, answer, img=None, W=None, box=None, maxh=420):
    if img:
        return (f'<div class="s light qs"><div class="page">{n}/{total}</div><div class="qn">QUESTION {num}</div>'
                f'<h2>{esc(question)}</h2><div class="ans"><b>Dans GuidPilot&nbsp;:</b> {esc(answer)}</div>{_frame(img, W, box, maxh=maxh)}</div>')
    return (f'<div class="s light q"><div class="page">{n}/{total}</div><div class="qn">QUESTION {num}</div>'
            f'<h2>{esc(question)}</h2><div class="ans"><b>Dans GuidPilot&nbsp;:</b> {esc(answer)}</div>{FOOT}</div>')


def last_plain(n, total, question, save):
    return (f'<div class="s light"><div class="page">{n}/{total}</div><h2>{esc(question)}</h2>'
            f'<div class="save">🔖 {esc(save)}</div></div>')


g.C = {
 # Jeudi 05/11 10h — CONSEIL thérapeutes — mythe / réalité — pilier argent — contexte : avant la réservation
 "jeu-05_carrousel-acompte-idees-recues": [
  cover_v2("Un acompte, [ça fait fuir vos clientes ?]", "5 idées reçues à revoir"),
  second_hook(2, 10, "Vous l'avez déjà pensé ?", "Si je demande un acompte, elle va réserver ailleurs.",
              "Pourtant, un cadre clair rassure souvent plus qu'il ne fait peur."),
  myth(3, 10, "Demander un acompte, c'est montrer que je n'ai pas confiance.",
       "C'est un engagement réciproque : vous bloquez une heure pour elle, elle s'engage à venir."),
  myth(4, 10, "Mes clientes vont trouver ça trop cher.",
       "L'acompte n'ajoute rien au prix : c'est une partie de la séance, réglée à l'avance."),
  myth(5, 10, "Les absences sont rares, ça ne sert à rien.",
       "Une seule absence, c'est une heure que personne d'autre n'a pu réserver."),
  myth(6, 10, "C'est compliqué à mettre en place.",
       "Annoncez le montant et vos conditions par écrit, avant la réservation. C'est tout."),
  myth(7, 10, "Chaque cas est différent, je verrai au moment venu.",
       "Un délai d'annulation clair, appliqué à toutes, évite les malaises et les négociations."),
  gp(8, 10, "Acompte et conditions, [visibles avant de réserver]",
     "Avec le paiement en ligne, vous pouvez demander un acompte au moment de la réservation. Vos conditions d'annulation sont affichées avant que votre cliente confirme."),
  recap(9, 10, "Un acompte qui rassure", ["Annoncé avant la réservation", "Un montant raisonnable", "Un délai d'annulation clair", "Les mêmes règles pour toutes"]),
  last_plain(10, 10, "Et vous, demandez-vous [un acompte ?]", "Enregistrez ce post pour le jour où vous fixerez vos conditions."),
 ],
 # Samedi 07/11 10h — PROMO thérapeutes — série « Pensé pour votre métier » — métier : sophrologue
 "sam-07_carrousel-sophrologue-6-questions": [
  cover_v2("Sophrologue : [6 questions] à vous poser avant de choisir votre outil", "La checklist à enregistrer"),
  prob(2, 10, "Le point de départ", "Un agenda en ligne, [c'est pratique pour réserver]",
       "Mais votre journée de sophrologue ne s'arrête pas à la réservation : paiement, séances à distance, notes, comptes rendus, factures."),
  quest(3, 10, 1, "Vos clientes réservent-elles [seules], au cabinet ou à distance ?",
        "votre page publique, vos prestations au cabinet ou en visio, et uniquement les créneaux que vous ouvrez.",
        K / "page_np.png", 1100, (310, 480, 870, 590), maxh=300),
  quest(4, 10, 2, "Le paiement se fait-il [avant la séance, ou au cabinet] ?",
        "en ligne par carte ou PayPal, ou au cabinet, enregistré en un clic sur la facture."),
  quest(5, 10, 3, "Le lien de visio part-il [sans que vous l'envoyiez] ?",
        "pour une séance à distance, le lien Google Meet est transmis avec la confirmation et le rappel par e-mail."),
  quest(6, 10, 4, "Vos notes de séance sont-elles [vraiment privées] ?",
        "vos notes restent dans la fiche de votre cliente. Elle ne les voit jamais."),
  quest(7, 10, 5, "Où votre cliente retrouve-t-elle [votre compte rendu] ?",
        "écrit ou vocal, dans son espace client sécurisé, avec ses rendez-vous et ses factures.",
        K / "guid.png", 1270, (20, 232, 415, 480), maxh=380),
  quest(8, 10, 6, "Vos factures se créent-elles [toutes seules] ?",
        "numérotées automatiquement, et vous voyez ce qui est encaissé.",
        K / "dash_np.png", 1270, (330, 430, 920, 530), maxh=300),
  recap(9, 10, "Un outil pensé pour votre métier, pas un agenda de plus.",
        ["Réservation seule, cabinet ou visio", "Paiement en ligne ou au cabinet", "Lien de visio envoyé pour vous", "Notes privées", "Compte rendu dans son espace", "Factures automatiques"]),
  last_promo(10, 10, "Combien de ces cases [cochez-vous aujourd'hui ?]", "THÉRAPEUTE"),
 ],
}

if __name__ == "__main__":
    g.main()
