"""Relance partenaires du 01/12/2026 — carrousel 7 slides 1080x1350.
Cible : accompagnants d'indépendants (coachs en création d'activité).
Règles : aucun tarif ni montant, jamais le mot interdit, vouvoiement, aucune personne, aucun superlatif, mot-clé PARTENAIRE.
Usage : python3 carrousels/gen_partenaires_2026-12-01.py → build/carrousels/partenaires-coachs-*.png"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import importlib
s19 = importlib.import_module("gen_semaine_2026-10-19")
import gen_carrousels as g

esc = g.esc
K = s19.K
g.CSS += """
.endlist .li{color:#fff;font-size:42px;align-items:flex-start}
.endlist .li i{background:#E9C46A;color:#0F172A;margin-top:-4px}
.kw{color:#E9C46A}
.site2{margin-top:40px;font-weight:700;font-size:38px;color:#93C5FD}
"""

def final(n, total):
    lis = "".join(f'<div class="li"><i>✓</i><span>{x}</span></div>' for x in (
        'Commentez <span class="kw">PARTENAIRE</span> et recevez le lien pour candidater',
        "Candidature sur guidpilot.fr",
        "Chaque candidature est étudiée personnellement"))
    return (f'<div class="s navy"><div class="page">{n}/{total}</div><img class="biglogo" src="data:image/png;base64,{g.LOGO_W}">'
            f'<h2 style="color:#fff">Devenez partenaire GuidPilot</h2><div class="list endlist">{lis}</div>'
            f'<div class="site2">guidpilot.fr</div></div>')

T = 7
g.C = {
 "partenaires-coachs": [
  s19.cover_v2("« J'utilise quoi pour [mes rendez-vous] ? »", "Vous accompagnez des praticiennes qui se lancent ?").replace("rendez-vous", '<span style="white-space:nowrap">rendez-vous</span>'),
  s19.prob(2, T, "Coachs en création d'activité", "Cette question revient [à chaque lancement]",
           "Tarologues, voyantes, praticiennes Reiki, sophrologues, hypnothérapeutes : avant la première cliente, il faut pouvoir réserver, encaisser et facturer."),
  s19.swap(3, T, "Ce que vous pouvez leur répondre",
           "Un agenda, un lien de paiement, un tableur pour les factures et les messages pour le reste.",
           "Un outil conçu pour les praticiens en guidance et les thérapeutes, où tout est relié."),
  s19.shot(4, T, "Leur page publique", "Réserver et payer [en ligne]",
           "Leurs clientes choisissent une prestation et un créneau, puis règlent en ligne. La page apparaît aussi dans l'annuaire.",
           K / "page_np.png", 1100, (310, 90, 960, 590), maxh=520),
  s19.shot(5, T, "Après la séance", "Guidances écrites [et vocales]",
           "Le compte rendu arrive dans l'espace client, avec la facture automatique et les rappels par e-mail.",
           K / "guid.png", 1270, (0, 20, 1270, 490), maxh=520),
  s19.prob(6, T, "Le programme partenaire", "Vous restez [dans votre rôle de conseil]",
           "Vous présentez GuidPilot à vos accompagnées quand il correspond à leur métier. Un partenariat simple, pensé pour celles et ceux qui accompagnent les indépendants."),
  final(7, T),
 ],
}

if __name__ == "__main__":
    g.main()
