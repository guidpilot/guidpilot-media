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
.think{margin-top:30px;background:#E2E8F0;color:#334155;border-radius:40px 40px 40px 10px;padding:34px 40px;font-weight:600;font-size:46px;line-height:1.35;font-style:italic}
.say{margin-top:34px;background:#2563EB;color:#fff;border-radius:40px 40px 10px 40px;padding:34px 40px;font-weight:600;font-size:42px;line-height:1.4}
.lab2{margin-top:44px;font-weight:800;font-size:28px;letter-spacing:.12em;color:#64748B;text-transform:uppercase}
.swap{margin-top:40px;display:flex;flex-direction:column;gap:26px}
.swap>div{border-radius:28px;padding:30px 36px;font-weight:600;font-size:42px;line-height:1.35}
.swap .no{background:#FEF2F2;border:2px solid #FECACA;color:#0F172A}.swap .yes{background:#F0FDF4;border:2px solid #BBF7D0;color:#0F172A}
.swap b{display:block;font-weight:800;font-size:28px;letter-spacing:.1em;margin-bottom:10px}.swap .no b{color:#B91C1C}.swap .yes b{color:#15803D}
.box{display:inline-flex;align-items:center;justify-content:center;width:120px;height:120px;border:8px solid #2563EB;border-radius:26px;font-size:80px;color:#2563EB;font-weight:800}
.chip{align-self:flex-start;display:inline-block;padding:14px 30px;border-radius:999px;font-weight:800;font-size:30px;letter-spacing:.08em}
.gpk{align-self:flex-start;display:inline-block;padding:14px 30px;border-radius:999px;background:#0F172A;color:#E9C46A;font-weight:800;font-size:30px;letter-spacing:.08em}
.week{margin-top:40px;display:grid;grid-template-columns:110px repeat(6,1fr);gap:10px;font-weight:700;font-size:26px}
.week .d{text-align:center;color:#64748B;padding-bottom:6px}.week .h{color:#94A3B8;font-size:24px;display:flex;align-items:center}
.week .c{height:74px;border-radius:14px;background:#fff;border:1px solid #E2E8F0}
.week .se{background:#DBEAFE;border-color:#93C5FD}.week .ad{background:#FEF3C7;border-color:#FCD34D}.week .re{background:#DCFCE7;border-color:#86EFAC}.week .of{background:#F1F5F9;border-color:#CBD5E1}
.legend{margin-top:30px;display:flex;flex-wrap:wrap;gap:18px 30px;font-weight:700;font-size:30px;color:#334155}
.legend i{display:inline-block;width:30px;height:30px;border-radius:8px;vertical-align:-6px;margin-right:10px}
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
FOOT = f'<div class="foot"><img src="data:image/png;base64,{g.LOGO_C}"></div>'

def thought(n, total, pense, title, dire):
    """Format « ce qu'elle pense / ce que vous pouvez dire » (bulle grise → bulle bleue)."""
    return (f'<div class="s light"><div class="page">{n}/{total}</div><div class="kicker">Ce qu\'elle pense</div>'
            f'<div class="think">«&nbsp;{esc(pense)}&nbsp;»</div><div class="lab2">{esc(title)}</div>'
            f'<div class="say">{esc(dire)}</div>{FOOT}</div>')

def swap(n, total, title, avant, apres):
    """Format avant / après : « Au lieu de… » → « Plutôt… »."""
    return (f'<div class="s light"><div class="page">{n}/{total}</div><h2 style="font-size:64px">{esc(title)}</h2>'
            f'<div class="swap"><div class="no"><b>✕ AU LIEU DE</b>{esc(avant)}</div><div class="yes"><b>✓ PLUTÔT</b>{esc(apres)}</div></div>{FOOT}</div>')

def check(n, total, title, text):
    """Format checklist : case à cocher à la place du numéro."""
    return (f'<div class="s light"><div class="page">{n}/{total}</div><div class="box">✓</div><h2>{esc(title)}</h2><p>{esc(text)}</p>{FOOT}</div>')

def block(n, total, label, cls, title, text):
    color = {"se": "#DBEAFE;color:#1E3A8A", "ad": "#FEF3C7;color:#78350F", "re": "#DCFCE7;color:#14532D", "of": "#E2E8F0;color:#334155"}[cls]
    return (f'<div class="s light"><div class="page">{n}/{total}</div><div class="chip" style="background:{color}">{esc(label)}</div>'
            f'<h2>{esc(title)}</h2><p>{esc(text)}</p>{FOOT}</div>')

def week(n, total, title):
    rows = [("9 h", ["se", "ad", "se", "se", "se", "of"]), ("11 h", ["se", "se", "se", "se", "se", "of"]),
            ("12 h", ["re", "re", "re", "re", "re", "of"]), ("14 h", ["se", "se", "of", "se", "se", "of"]),
            ("16 h", ["se", "se", "of", "se", "se", "of"]), ("17 h", ["re", "re", "of", "re", "re", "of"])]
    cells = '<div></div>' + "".join(f'<div class="d">{d}</div>' for d in ("Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"))
    for h, cs in rows:
        cells += f'<div class="h">{h}</div>' + "".join(f'<div class="c {c}"></div>' for c in cs)
    leg = ('<div class="legend"><span><i style="background:#DBEAFE"></i>Séances</span><span><i style="background:#FEF3C7"></i>Administratif</span>'
           '<span><i style="background:#DCFCE7"></i>Réponses aux messages</span><span><i style="background:#F1F5F9;border:1px solid #CBD5E1"></i>Off</span></div>')
    return (f'<div class="s light shot"><div class="page">{n}/{total}</div><div class="kicker">Modèle à recopier</div>'
            f'<h2>{esc(title)}</h2><div class="week">{cells}</div>{leg}</div>')

def gp(n, total, title, text, img=None, W=None, box=None, maxh=520):
    """Slide « Dans GuidPilot » : le lien concret entre le conseil et une vraie fonction (ton informatif)."""
    if img:
        x0, y0, x1, y1 = box; sc = min(888 / (x1 - x0), maxh / (y1 - y0))
        fw, fh = round((x1 - x0) * sc), round((y1 - y0) * sc)
        im = (f'<div class="frame" style="width:{fw}px"><div class="bar"><i></i><i></i><i></i><span>Compte de démonstration</span></div>'
              f'<div class="vp" style="height:{fh}px"><img src="data:image/png;base64,{_b64(img)}" style="width:{round(W*sc)}px;left:{-round(x0*sc)}px;top:{-round(y0*sc)}px"></div></div>')
        return (f'<div class="s light shot"><div class="page">{n}/{total}</div><div class="gpk">DANS GUIDPILOT</div>'
                f'<h2 style="font-size:64px">{esc(title)}</h2><p>{esc(text)}</p>{im}</div>')
    return (f'<div class="s light"><div class="page">{n}/{total}</div><div class="gpk">DANS GUIDPILOT</div>'
            f'<h2>{esc(title)}</h2><p>{esc(text)}</p>{FOOT}</div>')

g.C = {
 # Lundi 19/10 10h — CONSEIL guidance — format « ce que vos clientes pensent sans le dire »

 "lun-19_carrousel-pensent-sans-dire": [
  cover_v2("Ce que vos clientes [pensent sans vous le dire]", "Avant, pendant et après la guidance"),
  second_hook(2, 10, "Vous connaissez ce silence ?", "Je n'ose pas lui demander…",
              "Chaque question non posée est une hésitation de plus avant de réserver."),
  thought(3, 10, "Combien de temps ça dure ?", "Ce que vous pouvez dire, avant qu'elle réserve", "« La séance dure 45 minutes, en visio ou par écrit, à vous de choisir. »"),
  thought(4, 10, "Et si je ne comprends pas les cartes ?", "Ce que vous pouvez dire, en début de séance", "« Je vous explique chaque carte. N'hésitez pas à m'interrompre. »"),
  thought(5, 10, "Je peux poser plusieurs questions ?", "Ce que vous pouvez dire, pour poser le cadre", "« On part d'une question principale. Si une autre vient, on la garde pour la fin. »"),
  thought(6, 10, "Est-ce que je pourrai relire tout ça ?", "Ce que vous pouvez dire, en fin de séance", "« Vous recevez un compte rendu écrit, ou un vocal, d'ici demain. »"),
  thought(7, 10, "Je n'ose pas lui réécrire après.", "Ce que vous pouvez dire, en la quittant", "« Si une question vous revient, écrivez-moi : je réponds sous 48 h. »"),
  gp(8, 10, "Les réponses, [avant même la question]", "Chaque prestation de votre page affiche sa durée et son format. Après la séance, sa guidance écrite ou vocale l'attend dans son espace client.",
     K / "guid.png", 1270, (20, 232, 415, 480)),
  recap(9, 10, "À dire à chaque cliente", ["La durée et le format", "Vous expliquez tout", "Le cadre des questions", "Ce qu'elle reçoit après", "Comment vous joindre"]),
  last(10, 10, "Laquelle de ces questions [entendez-vous le plus ?]", "Enregistrez ce post pour préparer votre prochaine séance.", "GUIDANCE"),
 ],
 # Mardi 20/10 10h — CONSEIL thérapeutes — mini-guide pas à pas

 "mar-20_carrousel-suivi-sans-forcer": [
  cover_v2("Proposer un suivi en plusieurs séances, [sans forcer]", "4 phrases à changer dès demain"),
  second_hook(2, 9, "Vous vous reconnaissez ?", "Je ne veux pas avoir l'air de vendre des séances…",
              "Proposer un cadre, ce n'est pas vendre : c'est rassurer votre cliente."),
  swap(3, 9, "À la fin de la [première séance]", "« Revenez quand vous voulez. »", "« En général, on se revoit toutes les trois semaines. On fera le point ensemble. »"),
  swap(4, 9, "Quand elle hésite [à s'engager]", "« Il faudra au moins dix séances. »", "« On avance séance par séance. Vous restez libre à chaque fois. »"),
  swap(5, 9, "Avant qu'elle [reparte]", "« On se rappelle pour la suite ? »", "« Je vous propose mardi 14 h dans trois semaines, ça vous irait ? »"),
  swap(6, 9, "À la [séance suivante]", "Lui redemander tout ce qu'elle vous a déjà raconté.", "Relire vos notes avant qu'elle arrive, et reprendre là où vous en étiez."),
  gp(7, 9, "La suite, [prête avant qu'elle parte]", "Vous planifiez le prochain rendez-vous en un clic, et vos notes restent privées dans sa fiche : elle ne les voit jamais.",
     K / "dash_np.png", 1270, (840, 590, 1225, 990), maxh=480),
  recap(8, 9, "Un suivi qui rassure", ["Un rythme proposé, jamais imposé", "Sa liberté rappelée", "La date fixée avant de partir", "Vos notes relues avant la séance"]),
  last(9, 9, "Comment proposez-vous [la séance suivante ?]", "Enregistrez ce post pour votre prochaine première séance.", "THÉRAPEUTE"),
 ],
 # Mercredi 21/10 10h — CONSEIL guidance — checklist

 "mer-21_carrousel-fin-annee": [
  cover_v2("Fêtes de fin d'année : [5 choses à préparer dès maintenant]", "La checklist à cocher"),
  second_hook(2, 10, "Le piège classique", "Je verrai ça en décembre.",
              "Préparer en octobre, c'est vivre décembre plus sereinement."),
  check(3, 10, "Vos [dates de congés]", "Bloquez-les dans votre agenda et annoncez-les dès maintenant à vos clientes."),
  check(4, 10, "Vos [horaires des fêtes]", "Les 24 et 31 décembre, vous travaillez ou non ? Dites-le avant qu'on vous le demande."),
  check(5, 10, "Une idée [de cadeau]", "Une séance à offrir, avec un message personnel : certaines clientes y pensent pour Noël."),
  check(6, 10, "Vos [messages prêts]", "Le message d'absence, et celui qui annonce votre reprise en janvier."),
  check(7, 10, "Votre [planning de janvier]", "Ouvrez vos créneaux de janvier avant de partir : la rentrée se réserve aussi pendant les fêtes."),
  gp(8, 10, "Vos séances, [en carte cadeau]", "Vos clientes peuvent offrir une séance en carte cadeau à votre logo, avec un message personnel, directement depuis votre page. Et vos congés se bloquent dans votre agenda."),
  recap(9, 10, "Ma checklist des fêtes", ["Congés bloqués et annoncés", "Horaires du 24 et du 31", "Une séance à offrir", "Messages d'absence prêts", "Janvier ouvert"]),
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
  cover_v2("Votre semaine type de cabinet, [à recopier]", "Pour ne plus déborder"),
  second_hook(2, 9, "Vous vous reconnaissez ?", "Je prends les rendez-vous quand mes clientes peuvent.",
              "Résultat : des trous partout, et des soirées qui débordent."),
  week(3, 9, "Une semaine [qui respire]"),
  block(4, 9, "EN BLEU · LES SÉANCES", "se", "Des plages [fixes]", "Deux ou trois plages par jour, toujours les mêmes. Vos clientes réservent dedans, pas ailleurs."),
  block(5, 9, "EN JAUNE · L'ADMINISTRATIF", "ad", "Une heure, [le même jour]", "Factures, messages en retard, organisation : tout tient dans un seul créneau par semaine."),
  block(6, 9, "EN VERT · LES RÉPONSES", "re", "Deux fois par jour, [à heure fixe]", "Midi et fin d'après-midi. Entre deux séances, vous prenez 15 minutes pour aérer et souffler."),
  gp(7, 9, "Vos plages deviennent [vos disponibilités]", "Vous renseignez vos disponibilités une fois. Vos clientes ne peuvent réserver que dans les créneaux que vous ouvrez : votre semaine type se respecte toute seule."),
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
