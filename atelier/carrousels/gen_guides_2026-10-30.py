"""Carrousels « guides offerts » du 30/10 et du 01/11/2026 — 1080x1350.
Chaque carrousel donne un vrai conseil tiré d'un des 3 guides, puis renvoie vers guidpilot.fr (la pop-up y propose les guides).
ManyChat non actif : pas de mot-clé, dernière slide = « 3 guides offerts sur guidpilot.fr ».
Usage : python3 carrousels/gen_guides_2026-10-30.py  → build/carrousels/<nom>-NN.png"""
import importlib, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
sem = importlib.import_module("gen_semaine_2026-10-19")
g, esc, cover_v2, second_hook, recap, gp, point = sem.g, sem.esc, sem.cover_v2, sem.second_hook, sem.recap, sem.gp, sem.point

REPO = pathlib.Path(__file__).resolve().parents[2]
COV = [sem._b64(REPO / "guides" / "couvertures" / f"guide-{i}.jpg") for i in (1, 2, 3)]

g.CSS += """
.covers{display:flex;gap:26px;margin-top:50px}
.covers img{width:250px;border-radius:16px;box-shadow:0 18px 40px rgba(15,23,42,.25)}
.covers img.on{outline:8px solid #E9C46A;outline-offset:4px}
.gline{margin-top:46px;font-weight:700;font-size:44px;line-height:1.3;color:#0F172A}
.gline b{color:#2563EB}
.qmark{font-weight:800;font-size:64px;line-height:1.12;letter-spacing:-.02em;color:#0F172A}
.qmark span{color:#2563EB}
.src{margin-top:30px;font-weight:600;font-size:26px;color:#94A3B8}
"""


def guides_end(n, total, question, which):
    """Dernière slide : question + les 3 couvertures (celle d'où vient le conseil mise en valeur) + guidpilot.fr."""
    imgs = "".join(f'<img class="{"on" if i == which else ""}" src="data:image/jpeg;base64,{b}">' for i, b in enumerate(COV, 1))
    return (f'<div class="s light"><div class="page">{n}/{total}</div><div class="qmark">{esc(question)}</div>'
            f'<div class="covers">{imgs}</div>'
            f'<div class="gline">Ce conseil vient du guide {which}.<br>Les 3 guides sont offerts sur <b>guidpilot.fr</b></div></div>')


def study(n, total, kicker, title, text, src):
    return (f'<div class="s light"><div class="page">{n}/{total}</div><div class="kicker">{esc(kicker)}</div>'
            f'<h2>{esc(title)}</h2><p>{esc(text)}</p><div class="src">{esc(src)}</div>{sem.FOOT}</div>')


T1, T3 = 9, 10
g.C = {
 # Vendredi 30/10 18h30 — guide 2 — le paradoxe du choix (les deux publics)
 "ven-30_guides-trop-de-choix": [
  cover_v2("12 prestations sur votre page… et [moins de réservations]", "Quand trop de choix fait hésiter"),
  second_hook(2, T1, "Vous connaissez ce message ?", "Je ne sais pas laquelle choisir… je reviendrai.",
              "Elle ne revient pas toujours. Et ce n'est pas une question de prix."),
  study(3, T1, "Ce que dit une étude célèbre", "Moins de choix, [plus de décisions]",
        "Sur un stand, 24 confitures attiraient plus de monde. Mais parmi les personnes qui s'arrêtaient, 30 % achetaient avec 6 choix, contre 3 % avec 24. L'effet ne se vérifie pas toujours, mais face à un choix qui l'engage, votre cliente aussi peut bloquer.",
        "Iyengar et Lepper, 2000 · nuancé par une synthèse de Chernev et al., 2015"),
  point(4, T1, "1", "Gardez [3 à 4 offres] principales",
        "Par exemple : une première séance, une séance complète, un suivi. Les autres formats peuvent rester sur demande."),
  point(5, T1, "2", "Un nom qui dit [ce qui se passe]",
        "« Tirage 3 questions · 30 min en visio » ou « Séance découverte · 45 min » se comprennent tout de suite. Un nom poétique seul, beaucoup moins."),
  point(6, T1, "3", "Une ligne [« pour qui ? »]",
        "Sous chaque offre : « Idéal pour une première séance » ou « Pour faire le point après plusieurs rendez-vous ». Votre cliente se reconnaît et choisit."),
  gp(7, T1, "Chaque prestation, [claire]",
     "Dans GuidPilot, chaque prestation de votre page de réservation a son nom, sa durée, son format (cabinet, visio ou écrit) et sa description. Votre cliente choisit, puis réserve son créneau."),
  recap(8, T1, "Une page qui aide à choisir", ["3 à 4 offres principales", "Nom + durée + format", "Une ligne « pour qui ? »", "Le reste, sur demande"]),
  guides_end(9, T1, "Combien de prestations affichez-vous [aujourd'hui] ?", 2),
 ],
 # Dimanche 01/11 18h30 — guide 3 — la règle du pic et de la fin (les deux publics)
 "dim-01_guides-fin-de-seance": [
  cover_v2("Votre cliente oubliera presque tout… [sauf la fin]", "5 minutes qui comptent double"),
  second_hook(2, T3, "Ce qu'elle dit en partant", "C'était bien… mais ça s'est fini un peu vite.",
              "Une heure de qualité peut se résumer à cette dernière impression."),
  study(3, T3, "Ce que dit la psychologie", "On retient [le moment fort et la fin]",
        "Les travaux du psychologue Daniel Kahneman l'ont montré : on juge une expérience surtout sur son moment le plus intense et sur sa fin, bien plus que sur sa durée.",
        "Règle « pic-fin », Kahneman et al., 1993"),
  point(4, T3, "1", "Annoncez la fin [5 minutes avant]",
        "« Il nous reste cinq minutes : qu'aimeriez-vous garder de cette séance ? » Elle a le temps de poser sa dernière question, sans être coupée."),
  point(5, T3, "2", "Résumez en [3 phrases]",
        "Ce qui est ressorti. Ce qu'elle peut faire d'ici la prochaine fois. Ce qui reste ouvert. Elle repart avec quelque chose de clair."),
  point(6, T3, "3", "L'argent [n'est pas] le dernier mot",
        "Si le règlement se fait avant ou en ligne, la dernière image de la séance reste votre échange, pas le terminal de paiement."),
  point(7, T3, "4", "Prolongez [le lendemain]",
        "Quelques lignes écrites ou un court message audio envoyés après la séance rappellent le moment fort. Un petit geste qui donne envie de revenir, et d'en parler autour de soi."),
  gp(8, T3, "Avant et après, [sans y penser]",
     "Dans GuidPilot, votre cliente peut régler en réservant. Après la séance, vous déposez un compte rendu écrit ou vocal dans son espace client, où elle le retrouve quand elle veut."),
  recap(9, T3, "Une fin de séance réussie", ["Annoncer la fin 5 min avant", "Résumer en 3 phrases", "Régler avant, pas à la fin", "Un mot le lendemain"]),
  guides_end(10, T3, "Comment terminez-vous [vos séances] aujourd'hui ?", 3),
 ],
}

if __name__ == "__main__":
    g.main()
