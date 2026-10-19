"""Titre + description YouTube (avec chapitres) d'un tuto : python3 youtube_meta.py <spec.py>
Les chapitres sont calés sur build/<slug>/timing.json (début de chaque scène)."""
import json, pathlib, re, sys
from tuto_video import load_spec


def plain(html):
    return re.sub(r"<[^>]+>", "", html).replace("&nbsp;", " ").strip()


def ts(t):
    t = int(t)
    return f"{t // 60}:{t % 60:02d}"


def meta(spec_path):
    spec = load_spec(spec_path)
    tm = json.loads((pathlib.Path("build") / spec["slug"] / "timing.json").read_text())
    b = tm["bounds"]
    chap = [("0:00", "Introduction")]
    nsteps = sum(1 for sc in spec["scenes"] if sc["type"] == "shot" and sc.get("step"))
    for i, sc in enumerate(spec["scenes"]):
        if sc["type"] == "shot" and (sc.get("step") or nsteps < 3):
            chap.append((ts(b[i]), plain(sc["caption"])))
        elif sc["type"] == "recap":
            chap.append((ts(b[i]), "En résumé"))
    # YouTube : chapitres d'au moins 10 s. On écarte les « Cliquez sur Enregistrer », puis on décale un
    # chapitre trop proche du précédent (6 s maximum) ; au-delà, il est fusionné avec le précédent.
    chap = [c for c in chap if not re.match(r"(Cliquez sur Enregistrer|Tout en bas)", c[1])]
    def secs(s_):
        m_, s2 = s_.split(":"); return int(m_) * 60 + int(s2)
    kept = []
    for a_, c in chap:
        t = secs(a_)
        if kept:
            t2 = max(t, secs(kept[-1][0]) + 10)
            if t2 - t > 6:
                continue
            t = t2
        kept.append((ts(t), c))
    while len(kept) > 1 and tm["duration"] - secs(kept[-1][0]) < 10:
        kept.pop()
    chap = kept
    title = f"Tuto {spec['num']} · {spec['title']} | GuidPilot"
    desc = "\n".join([
        f"{spec['subtitle']}.",
        "",
        f"Série « {spec['series']} » : " + ("les tutoriels pour configurer votre espace GuidPilot pas à pas." if spec['series'] == "Mettre en place GuidPilot" else "les tutoriels pour utiliser GuidPilot pas à pas."),
        "",
        "Chapitres",
        *[f"{a} {c}" for a, c in chap],
        "",
        f"Prochain tutoriel : {spec['next'].split('·', 1)[-1].strip()}." if spec.get("next") else "",
        "Tous les tutoriels sont aussi dans GuidPilot, rubrique Aide & tutoriels.",
        "Une question ? Écrivez-nous depuis Support dans votre espace.",
        "",
        "Captures réalisées sur un compte de démonstration. Voix off générée par IA.",
        "",
        "https://guidpilot.fr",
    ])
    return {"title": title, "description": desc, "duration": tm["duration"]}


if __name__ == "__main__":
    m = meta(sys.argv[1])
    print(m["title"]); print(); print(m["description"])
