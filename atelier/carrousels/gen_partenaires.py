"""Carrousel permanent « Devenir partenaire GuidPilot » (21/10/2026) — 6 slides 1080x1350.
Règles : aucun tarif ni montant, jamais le mot « affiliation », vouvoiement, aucune personne, mot-clé PARTENAIRE.
Usage : python3 carrousels/gen_partenaires.py → build/carrousels/partenaires-*.png"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_v2_test as v2
import gen_carrousels as g
from gen_carrousels import point, LOGO_W

esc = g.esc
g.CSS += """
.endlist .li{color:#fff;font-size:44px}
.endlist .li i{background:#E9C46A;color:#0F172A}
.kw{color:#E9C46A}
.site2{margin-top:40px;font-weight:700;font-size:38px;color:#93C5FD}
"""

def final(n, total):
    lis = "".join(f'<div class="li"><i>✓</i><span>{x}</span></div>' for x in (
        f'Commentez <span class="kw">PARTENAIRE</span>&nbsp;: le lien arrive en message privé',
        "Ou candidatez directement sur guidpilot.fr",
        "Chaque candidature est étudiée personnellement"))
    return (f'<div class="s navy"><div class="page">{n}/{total}</div><img class="biglogo" src="data:image/png;base64,{LOGO_W}">'
            f'<h2 style="color:#fff">Rejoignez le programme partenaire</h2><div class="list endlist">{lis}</div>'
            f'<div class="site2">guidpilot.fr</div></div>')

T = 6
g.C = {
 "partenaires": [
  v2.cover_v2("GuidPilot cherche des [partenaires]", "Vous vous reconnaissez ?"),
  point(2, T, "1", "Vous formez des [praticiens ou des thérapeutes]",
        "Reiki, tarot, sophrologie, magnétisme… À la fin de leur formation, vos élèves auront besoin d'un outil pour recevoir leurs premiers clients."),
  point(3, T, "2", "Vous partagez vos conseils [à une communauté]",
        "Créatrice de contenu, praticienne ou thérapeute suivie : on vous demande souvent quels outils vous utilisez."),
  point(4, T, "3", "Vous recommandez déjà [des outils]",
        "Logiciels, applications, formations : vous savez repérer ce qui aide vraiment les indépendants."),
  point(5, T, "4", "Le seul outil conçu [pour leur métier]",
        "Réservation et paiement en ligne, factures automatiques, espace client, guidances écrites et vocales, Google Meet : tout au même endroit.").replace('<div class="num">4</div>', '<div class="kicker">Pourquoi GuidPilot</div>'),
  final(6, T),
 ],
}

if __name__ == "__main__":
    g.main()
