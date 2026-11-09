"""Carrousels « Offre de Noël / offre fondatrice » — 1080x1350 (décision de Normane du 09/11/2026).
Jeudi 12/11 18h (thérapeutes) : « 12 mois pour 99 € : ce que ça comprend ».
Dimanche 15/11 10h (guidance) : « Et après l'année ? » — les 3 choix, aucun prélèvement automatique.
Exception validée : le prix (99 €) et la date (31 décembre) apparaissent. Lien : guidpilot.fr/offre-fondatrice (pas de ManyChat).
Usage : python3 carrousels/gen_noel_2026-11-11.py  → build/carrousels/<nom>-NN.png"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import importlib
S2 = importlib.import_module("gen_semaine_2026-11-02")
S = importlib.import_module("gen_semaine_2026-10-19")
g = S.g
esc, cover_v2, second_hook, recap, prob, gp, swap, FOOT, K = S.esc, S.cover_v2, S.second_hook, S.recap, S.prob, S.gp, S.swap, S.FOOT, S.K
last_plain = S2.last_plain

g.CSS += """
.price{margin-top:40px;display:flex;align-items:baseline;gap:26px;flex-wrap:wrap}
.price b{font-size:170px;line-height:.9;font-weight:800;letter-spacing:-.05em;color:#0F172A}
.price s{font-size:60px;color:#94A3B8;font-weight:700}
.price small{display:block;width:100%;margin-top:18px;font-weight:700;font-size:38px;color:#2563EB}
.pill{align-self:flex-start;display:inline-block;padding:14px 30px;border-radius:999px;background:#E9C46A;color:#0F172A;font-weight:800;font-size:30px;letter-spacing:.06em}
.inc{margin-top:36px;display:flex;flex-direction:column;gap:22px}
.inc div{display:flex;gap:22px;align-items:flex-start;font-weight:600;font-size:40px;line-height:1.3;color:#0F172A}
.inc i{flex:none;font-style:normal;width:64px;height:64px;border-radius:18px;background:#0F172A;color:#E9C46A;display:flex;align-items:center;justify-content:center;font-size:34px}
.choice{margin-top:34px;background:#fff;border:2px solid #E2E8F0;border-radius:32px;padding:40px 44px;box-shadow:0 20px 50px rgba(15,23,42,.08)}
.choice h3{margin:0;font-weight:800;font-size:52px;color:#0F172A;letter-spacing:-.02em}
.choice p{margin:16px 0 0;font-weight:600;font-size:38px;line-height:1.4;color:#334155}
.link{margin-top:40px;font-weight:800;font-size:44px;color:#2563EB;word-break:break-all}
"""

def price(n, total, pill, title, big, strike, small, text):
    return (f'<div class="s light"><div class="page">{n}/{total}</div><div class="pill">{esc(pill)}</div><h2>{esc(title)}</h2>'
            f'<div class="price"><b>{esc(big)}</b><s>{esc(strike)}</s><small>{esc(small)}</small></div><p>{esc(text)}</p>{FOOT}</div>')

def inc(n, total, title, items, text=""):
    rows = "".join(f'<div><i>{ic}</i><span>{esc(t)}</span></div>' for ic, t in items)
    return (f'<div class="s light"><div class="page">{n}/{total}</div><div class="pill">PENDANT 12 MOIS</div><h2>{esc(title)}</h2>'
            f'<div class="inc">{rows}</div>{f"<p>{esc(text)}</p>" if text else ""}{FOOT}</div>')

def choice(n, total, num, title, text, label="APRÈS 12 MOIS · CHOIX"):
    return (f'<div class="s light"><div class="page">{n}/{total}</div><div class="pill">{esc(label)} {num}</div>'
            f'<div class="choice"><h3>{esc(title)}</h3><p>{esc(text)}</p></div>{FOOT}</div>')

def last_link(n, total, question, link, note):
    return (f'<div class="s navy hook"><div class="page" style="color:#CBD5E1">{n}/{total}</div><h1 style="font-size:84px">{esc(question)}</h1>'
            f'<div class="badge">{esc(note)}</div><div class="link" style="color:#E9C46A">{esc(link)}</div></div>')

g.C = {
 # Jeudi 12/11 18h — PROMO Noël — thérapeutes — « ce que ça comprend »
 "jeu-12_carrousel-noel-99-ce-que-ca-comprend": [
  cover_v2("Un an de GuidPilot pour [99 €.] Ce que ça comprend, vraiment.", "Offre de Noël · jusqu'au 31 décembre"),
  price(2, 10, "OFFRE FONDATRICE", "Payé [une seule fois]", "99 €", "348 €", "soit 8,25 € par mois · aucun prélèvement automatique",
        "348 €, c'est le prix d'une année au mois (29 € × 12). 99 €, c'est le prix fondateur, pour celles qui nous font confiance en premier."),
  inc(3, 10, "Vos séances [se réservent seules]", [("📅", "Votre page de réservation, ouverte 24 h/24"), ("🗓️", "Vos disponibilités, vos pauses, vos jours de repos"), ("🔔", "Rappel par e-mail la veille, lien de visio inclus")]),
  inc(4, 10, "Vous êtes [payée sans relancer]", [("💳", "Paiement en ligne (carte ou PayPal) ou au cabinet"), ("🧾", "Facture numérotée créée automatiquement"), ("📨", "Relance d'un impayé en un clic, par e-mail")]),
  inc(5, 10, "Vos clientes retrouvent [tout au même endroit]", [("🔒", "Un espace client privé par cliente"), ("📝", "Vos comptes rendus, écrits ou vocaux"), ("💬", "Une messagerie, à part de votre téléphone perso")]),
  inc(6, 10, "On vous trouve, [on vous recommande]", [("⭐", "Demandes d'avis et affichage sur votre page"), ("🧭", "Annuaire des praticiens"), ("🎁", "Cartes cadeaux et forfaits de séances")]),
  swap(7, 10, "Et dans un an ?", "Un abonnement qui se renouvelle tout seul, sans qu'on vous demande votre avis.",
       "Rien n'est prélevé. Vous choisissez : renouveler au tarif fondateur (149 €/an), passer au mensuel (29 €), ou arrêter."),
  prob(8, 10, "Comment ça marche", "Trois étapes, [aucun engagement]",
       "1. Vous créez votre compte (14 jours gratuits, sans carte). 2. Depuis votre espace, vous prenez l'offre : 99 €, paiement sécurisé. 3. Vos 12 mois démarrent à la fin de vos jours d'essai : rien n'est perdu."),
  recap(9, 10, "L'offre de Noël, en bref", ["1 an d'accès complet pour 99 €", "Payé une fois, aucun prélèvement automatique", "Toutes les fonctions, pour thérapeutes et praticiennes en guidance", "Ensuite : 149 €/an, 29 €/mois, ou arrêt", "Jusqu'au 31 décembre 2026"]),
  last_link(10, 10, "Vous vous équipez quand ?", "guidpilot.fr/offre-fondatrice", "Lien en bio · jusqu'au 31 décembre"),
 ],
 # Dimanche 15/11 10h — PROMO Noël — guidance — « et après l'année ? » (transparence)
 "dim-15_carrousel-noel-et-apres": [
  cover_v2("1 an pour 99 €… [et après ?]", "La question qu'on nous pose le plus"),
  second_hook(2, 9, "La vraie question", "Et dans un an, je me retrouve prélevée sans rien avoir demandé ?",
              "Non. Et c'est écrit noir sur blanc : l'offre fondatrice ne se renouvelle jamais toute seule."),
  choice(3, 9, "1", "Renouveler au tarif fondateur", "149 € pour 12 mois de plus, payés une fois. Un tarif garanti tant que vous renouvelez avant la fin de votre année. Personne d'autre ne l'aura."),
  choice(4, 9, "2", "Passer au mensuel", "29 € par mois, sans engagement, résiliable à tout moment. Pour celles qui préfèrent ne rien payer d'avance."),
  choice(5, 9, "3", "Arrêter", "Votre espace passe en lecture seule : vos clientes, vos guidances, vos factures restent consultables et exportables. Rien n'est supprimé."),
  prob(6, 9, "Et avant la fin ?", "On vous prévient [un mois avant]", "Un e-mail à J-30, un rappel à J-7, et le choix se fait depuis votre espace, en deux clics. Si vous ne faites rien, il ne se passe rien : aucun prélèvement."),
  price(7, 9, "POURQUOI 99 €", "Le prix de [notre confiance]", "99 €", "348 €", "soit le prix d'une seule consultation",
        "Nous cherchons nos premières praticiennes, celles qui nous rejoignent avant les avis et les témoignages. Ce prix est notre façon de dire merci."),
  recap(8, 9, "Ce que vous savez maintenant", ["99 € une fois, 12 mois d'accès complet", "Aucun renouvellement automatique", "Ensuite : 149 €/an, 29 €/mois, ou arrêt", "Vos données restent à vous", "Jusqu'au 31 décembre 2026"]),
  last_link(9, 9, "Une question avant de vous lancer ?", "guidpilot.fr/offre-fondatrice", "Écrivez-nous : support@guidpilot.fr"),
 ],
}

if __name__ == "__main__":
    g.main()
