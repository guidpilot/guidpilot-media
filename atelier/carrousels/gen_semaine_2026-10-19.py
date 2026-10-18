"""Carrousels de la semaine du 19 au 25/10/2026 (ligne V2, 2 posts/jour) — 1080x1350.
Copié de gen_v2_test.py + slide « shot » (capture du compte de démonstration recadrée) pour les carrousels PROMO.
Usage : python3 carrousels/gen_semaine_2026-10-19.py  → build/carrousels/<nom>-NN.png"""
import base64, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_carrousels as g
from gen_carrousels import point, quote

ATELIER = pathlib.Path(__file__).parent.parent
_esc = g.esc
def esc(t):
    out = _esc(t)
    for a, b in (("« ", "«&nbsp;"), (" »", "&nbsp;»"), (" :", "&nbsp;:"), (" ?", "&nbsp;?"), (" !", "&nbsp;!")):
        out = out.replace(a, b)
    return out
g.esc = esc

g.CSS += """
.hook h1{font-size:100px;margin-top:0}
.hook .badge{display:inline-block;margin-top:56px;background:#E9C46A;color:#0F172A;font-weight:800;font-size:36px;padding:18px 34px;border-radius:999px;align-self:flex-start}
.save{margin-top:56px;background:#fff;border:3px dashed #2563EB;border-radius:28px;padding:34px 40px;font-weight:700;font-size:42px;line-height:1.35;color:#0F172A}
.discreet{position:absolute;left:96px;right:96px;bottom:96px;font-weight:600;font-size:30px;color:#94A3B8;text-align:center}
.promo{margin-top:50px;background:#0F172A;color:#fff;border-radius:28px;padding:36px 40px;font-weight:700;font-size:40px;line-height:1.35}
.promo b{color:#E9C46A}
.promo small{display:block;margin-top:14px;font-weight:600;font-size:32px;color:#CBD5E1}
.recap .li{color:#fff;font-size:42px}
.recap .li i{background:#E9C46A;color:#0F172A}
.frame{margin-top:44px;background:#fff;border:2px solid #E2E8F0;border-radius:24px;overflow:hidden;box-shadow:0 18px 50px rgba(15,23,42,.10)}
.frame .bar{display:flex;align-items:center;gap:10px;padding:14px 20px;border-bottom:1px solid #E2E8F0;background:#F8FAFC}
.frame .bar i{width:14px;height:14px;border-radius:50%;background:#CBD5E1;display:block}
.frame .bar span{margin-left:auto;font-weight:600;font-size:22px;color:#64748B;background:#fff;border:1px solid #E2E8F0;border-radius:999px;padding:4px 16px}
.frame .vp{position:relative;overflow:hidden}
.frame .vp img{position:absolute;max-width:none}
.s.shot{justify-content:flex-start;padding-top:190px}
.s.shot h2{font-size:68px}
.s.shot p{font-size:40px;margin-top:26px}
"""

def _b64(path):
    return base64.b64encode(open(path, "rb").read()).decode()

def cover_v2(title, badge):
    return f'<div class="s navy hook"><h1>{esc(title)}</h1><div class="badge">{esc(badge)}</div><div class="swipe">Faites défiler →</div></div>'

def second_hook(n, total, kicker, msg, tip):
    return (f'<div class="s light"><div class="page">{n}/{total}</div><div class="kicker">{esc(kicker)}</div>'
            f'<div class="quote" style="font-size:54px">«&nbsp;{esc(msg)}&nbsp;»</div><div class="tip">{esc(tip)}</div></div>')

def recap(n, total, title, items):
    lis = "".join(f'<div class="li"><i>✓</i>{esc(x)}</div>' for x in items)
    return (f'<div class="s navy recap"><div class="page">{n}/{total}</div><div class="kicker">À enregistrer</div>'
            f'<h2 style="color:#fff">{esc(title)}</h2><div class="list">{lis}</div></div>')

def last(n, total, question, save, kw):
    return (f'<div class="s light"><div class="page">{n}/{total}</div><h2>{esc(question)}</h2>'
            f'<div class="save">🔖 {esc(save)}</div>'
            f'<div class="discreet">Besoin d\'un outil pour tout ça ? Commentez {kw}.</div></div>')

def last_promo(n, total, question, kw):
    return (f'<div class="s light"><div class="page">{n}/{total}</div><h2>{esc(question)}</h2>'
            f'<div class="promo">📩 Commentez <b>{kw}</b> et recevez la présentation de GuidPilot en message privé.'
            f'<small>14 jours gratuits, sans carte bancaire · guidpilot.fr</small></div></div>')

def prob(n, total, kicker, title, text):
    return (f'<div class="s light"><div class="page">{n}/{total}</div><div class="kicker">{esc(kicker)}</div>'
            f'<h2>{esc(title)}</h2><p>{esc(text)}</p><div class="foot"><img src="data:image/png;base64,{g.LOGO_C}"></div></div>')

def shot(n, total, kicker, title, text, img, W, box, maxh=640):
    """Capture du compte de démonstration : box = (x0, y0, x1, y1) en pixels de l'image d'origine (largeur W)."""
    x0, y0, x1, y1 = box
    s = min(888 / (x1 - x0), maxh / (y1 - y0))
    fw, fh = round((x1 - x0) * s), round((y1 - y0) * s)
    im = (f'<div class="frame" style="width:{fw}px"><div class="bar"><i></i><i></i><i></i><span>Compte de démonstration</span></div>'
          f'<div class="vp" style="height:{fh}px"><img src="data:image/png;base64,{_b64(img)}" style="width:{round(W*s)}px;left:{-round(x0*s)}px;top:{-round(y0*s)}px"></div></div>')
    return (f'<div class="s light shot"><div class="page">{n}/{total}</div><div class="kicker">{esc(kicker)}</div>'
            f'<h2>{esc(title)}</h2><p>{esc(text)}</p>{im}</div>')

K = ATELIER / "kit" / "assets"; A = ATELIER / "assets"

g.C = {
 # Lundi 19/10 10h — CONSEIL guidance — format « ce que vos clientes pensent sans le dire »
 "lun-19_carrousel-pensent-sans-dire": [
  cover_v2("Ce que vos clientes [pensent sans vous le dire]", "Avant, pendant et après la guidance"),
  second_hook(2, 9, "Vous connaissez ce silence ?", "Je n'ose pas lui demander…",
              "Chaque question non posée est une hésitation de plus avant de réserver."),
  point(3, 9, "1", "« Combien de temps [ça dure ?] »", "Indiquez la durée de chaque séance, noir sur blanc. Sans cette information, on hésite à réserver."),
  point(4, 9, "2", "« Et si je ne comprends pas [les cartes ?] »", "Dites dès le début que vous expliquez tout, et qu'elle peut vous interrompre à tout moment."),
  point(5, 9, "3", "« Je peux poser [plusieurs questions ?] »", "Annoncez le cadre : une question principale ou un thème. Elle se sent libre, sans déborder."),
  point(6, 9, "4", "« Je pourrai [relire tout ça ?] »", "Précisez si elle reçoit un compte rendu écrit ou un vocal après la séance, et où le retrouver."),
  point(7, 9, "5", "« Je n'ose pas [vous réécrire après] »", "Dites-lui comment vous joindre après la séance, et sous quel délai vous répondez."),
  recap(8, 9, "À dire avant chaque séance", ["La durée exacte", "Vous expliquez tout", "Le cadre des questions", "Ce qu'elle reçoit après", "Comment vous joindre"]),
  last(9, 9, "Laquelle de ces questions [entendez-vous le plus ?]", "Enregistrez ce post pour préparer votre prochaine séance.", "GUIDANCE"),
 ],
 # Mardi 20/10 10h — CONSEIL thérapeutes — mini-guide pas à pas
 "mar-20_carrousel-suivi-sans-forcer": [
  cover_v2("Proposer un suivi en plusieurs séances, [sans forcer]", "Sophrologie, hypnose, Reiki, réflexologie"),
  second_hook(2, 9, "Vous vous reconnaissez ?", "Je ne veux pas avoir l'air de vendre des séances…",
              "Proposer un cadre, ce n'est pas vendre : c'est rassurer votre cliente."),
  point(3, 9, "1", "Expliquez [dès la 1re séance]", "Comment se passe un accompagnement chez vous : la durée d'une séance, l'intervalle habituel entre deux rendez-vous."),
  point(4, 9, "2", "Un [rythme], pas un engagement", "« Je vous propose de nous revoir dans trois semaines, et on fera le point. » Votre cliente garde la main."),
  point(5, 9, "3", "La date [avant de vous quitter]", "Le rendez-vous suivant se cale à la fin de la séance, pas « quand vous voulez »."),
  point(6, 9, "4", "Notez [ce qui a été vu]", "Quelques lignes privées après chaque séance : vous reprenez le fil sans tout redemander."),
  point(7, 9, "5", "Un point [à mi-parcours]", "Demandez-lui simplement comment elle vit l'accompagnement, et ajustez le rythme ensemble."),
  recap(8, 9, "Un suivi qui rassure", ["Le cadre expliqué dès le début", "Un rythme proposé, jamais imposé", "La date fixée avant de partir", "Vos notes après chaque séance", "Un point à mi-parcours"]),
  last(9, 9, "Comment proposez-vous [la séance suivante ?]", "Enregistrez ce post pour votre prochaine première séance.", "THÉRAPEUTE"),
 ],
 # Mercredi 21/10 10h — CONSEIL guidance — checklist
 "mer-21_carrousel-fin-annee": [
  cover_v2("Fêtes de fin d'année : [6 choses à préparer dès maintenant]", "Checklist praticienne en guidance"),
  second_hook(2, 10, "Le piège classique", "Je verrai ça en décembre.",
              "Préparer en octobre, c'est vivre décembre plus sereinement."),
  point(3, 10, "1", "Vos [dates de congés]", "Bloquez-les dans votre agenda et annoncez-les dès maintenant à vos clientes."),
  point(4, 10, "2", "Vos [horaires des fêtes]", "Les 24 et 31 décembre, vous travaillez ou non ? Dites-le avant qu'on vous le demande."),
  point(5, 10, "3", "Une idée [de cadeau]", "Une séance à offrir, avec un message personnel : certaines clientes y pensent pour Noël."),
  point(6, 10, "4", "Vos [messages prêts]", "Préparez le message d'absence, et celui qui annonce votre reprise en janvier."),
  point(7, 10, "5", "Le point [sur vos clientes]", "Repérez celles que vous n'avez pas vues depuis longtemps. Un simple message de fin d'année suffit."),
  point(8, 10, "6", "Votre [planning de janvier]", "Ouvrez vos créneaux de janvier avant de partir : la rentrée se réserve aussi pendant les fêtes."),
  recap(9, 10, "Ma checklist des fêtes", ["Congés bloqués et annoncés", "Horaires du 24 et du 31", "Une séance à offrir", "Messages d'absence prêts", "Point sur mes clientes", "Janvier ouvert"]),
  last(10, 10, "Vous travaillez [pendant les fêtes ?]", "Enregistrez ce post et cochez au fur et à mesure.", "GUIDANCE"),
 ],
 # Jeudi 22/10 10h — PROMO thérapeutes — réservation pendant la séance
 "jeu-22_carrousel-reservation-en-seance": [
  cover_v2("Vous êtes en séance. [Une cliente réserve quand même.]", "Le parcours en 4 étapes"),
  prob(2, 8, "Le problème", "Le SMS [arrive pendant la séance]", "Vous répondez le soir. Entre-temps, le créneau qu'elle voulait est pris… ou elle a laissé tomber."),
  shot(3, 8, "Étape 1", "Elle ouvre [votre page]", "Depuis votre lien en bio : vos prestations et le bouton « Prendre rendez-vous ».",
       A / "pagepublique.png", 1600, (330, 140, 1270, 650)),
  prob(4, 8, "Étape 2", "Elle choisit [son créneau]", "Uniquement parmi les disponibilités que vous avez définies. Elle peut régler en ligne, de façon sécurisée."),
  shot(5, 8, "Étape 3", "Le rendez-vous arrive [dans votre agenda]", "Vous le découvrez en sortant de séance, sans rien avoir saisi.",
       K / "dash_np.png", 1270, (20, 585, 805, 845)),
  shot(6, 8, "Étape 4", "La facture [se crée toute seule]", "Et vous suivez ce qui est encaissé depuis votre tableau de bord.",
       K / "dash_np.png", 1270, (20, 360, 640, 550)),
  recap(7, 8, "Ce que vous y gagnez", ["Plus de SMS pendant vos séances", "Rien à ressaisir le soir", "Une cliente rassurée par un vrai parcours", "Tout au même endroit"]),
  last_promo(8, 8, "Combien de messages pour caler [un seul rendez-vous ?]", "THÉRAPEUTE"),
 ],
 # Samedi 24/10 10h — CONSEIL thérapeutes — mini-guide
 "sam-24_carrousel-semaine-type": [
  cover_v2("Votre semaine type de cabinet, [en 5 blocs]", "Pour ne plus déborder"),
  second_hook(2, 9, "Vous vous reconnaissez ?", "Je prends les rendez-vous quand mes clientes peuvent.",
              "Résultat : des trous partout, et des soirées qui débordent."),
  point(3, 9, "1", "Les blocs [séances]", "Choisissez 2 ou 3 plages fixes par jour. Vos clientes réservent dedans, pas ailleurs."),
  point(4, 9, "2", "Le bloc [administratif]", "Une heure par semaine, toujours le même jour : factures, messages, organisation."),
  point(5, 9, "3", "Les [pauses] entre deux séances", "15 minutes pour aérer la pièce, noter quelques lignes et souffler."),
  point(6, 9, "4", "Un créneau [pour répondre]", "Les messages, deux fois par jour à heure fixe. Pas entre deux séances."),
  point(7, 9, "5", "Un jour [vraiment off]", "Sans séance ni message. Notez-le dans votre agenda comme un rendez-vous."),
  recap(8, 9, "Ma semaine type", ["Des plages de séances fixes", "1 h d'administratif par semaine", "15 min entre deux séances", "2 créneaux de réponse par jour", "1 jour vraiment off"]),
  last(9, 9, "Quel bloc vous manque [le plus ?]", "Enregistrez ce post pour construire votre semaine ce week-end.", "THÉRAPEUTE"),
 ],
 # Dimanche 25/10 10h — PROMO guidance — page praticienne
 "dim-25_carrousel-lien-en-bio": [
  cover_v2("Votre lien en bio mène… [à vos messages privés ?]", "Une vraie page praticienne"),
  prob(2, 8, "Le problème", "Une cliente curieuse [n'ose pas écrire]", "Elle veut voir vos prestations, votre façon de travailler et des avis. Si elle doit vous écrire pour savoir, elle peut repartir."),
  shot(3, 8, "Votre page GuidPilot", "Qui vous [êtes]", "Votre photo, votre spécialité, le format (visio, écrite) et votre note moyenne.",
       A / "pagepublique.png", 1600, (330, 140, 1270, 650)),
  quote(4, 8, "Votre page GuidPilot", "Votre [façon de travailler]",
        "Praticienne en guidance depuis 8 ans, j'accompagne mes clients vers plus de clarté dans leurs choix.",
        '<div class="tip">Quelques lignes dans « À propos », avec vos mots. (Exemple : compte de démonstration)</div>'),
  shot(5, 8, "Votre page GuidPilot", "Un bouton [pour réserver]", "« Prendre rendez-vous » : elle choisit sa séance et son créneau, sans vous écrire.",
       A / "pagepublique.png", 1600, (560, 530, 1110, 640)),
  shot(6, 8, "Votre page GuidPilot", "Vos [avis]", "Les avis publiés par vos clientes s'affichent sur votre page.",
       A / "pagepublique.png", 1600, (570, 410, 780, 470)),
  recap(7, 8, "Un seul lien en bio", ["Qui vous êtes", "Vos prestations", "Vos avis", "La réservation en ligne"]),
  last_promo(8, 8, "Et vous, où mène [votre lien en bio ?]", "GUIDANCE"),
 ],
}

if __name__ == "__main__":
    g.main()
