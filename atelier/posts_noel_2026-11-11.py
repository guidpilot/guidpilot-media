"""Légendes et payloads Metricool — lot « Offre de Noël » n°1, 11 → 15/11/2026 (en plus du lot hebdo).
Créneaux choisis d'après getBestTimeToPostByNetwork (pic 10h, second pic 18h) sur les jours encore libres.
Usage : python3 posts_noel_2026-11-11.py <SHA> → build/posts_noel_2026-11-11.json"""
import json, sys, pathlib
SHA = sys.argv[1]
CDN = f"https://cdn.jsdelivr.net/gh/guidpilot/guidpilot-media@{SHA}/"
RAW = f"https://raw.githubusercontent.com/guidpilot/guidpilot-media/{SHA}/"
W = "2026-11-11_noel/"
TZ = "Europe/Paris"
IA = "Captures réalisées sur un compte de démonstration. Voix off générée par IA."
FB_IA = "🤖 Contenu créé avec l'IA : voix off générée par IA."
LINK = "👉 Lien en bio : guidpilot.fr/offre-fondatrice"
OFFRE = "🎁 Offre de Noël : 1 an de GuidPilot pour 99 € au lieu de 348 €, payé une fois, aucun prélèvement automatique. Jusqu'au 31 décembre."

def pub(dt): return {"dateTime": dt, "timezone": TZ}
def yt(title, tags): return {"title": title + " #shorts", "type": "short", "privacy": "public", "madeForKids": False, "isAiGeneratedContent": True, "category": "HOWTO_STYLE", "tags": tags}
POSTS = []
def add(dt, info): POSTS.append({"date": dt + "+01:00", "info": info})

REELS = {
 "2026-11-11T10:00:00": dict(file="mer-11_reel-noel-pourquoi-99.mp4",
  text="Un an de GuidPilot pour 99 €. Voilà pourquoi. 🎁\n\nNous cherchons nos premières praticiennes : celles qui nous font confiance avant les avis et les témoignages.\n1. Vous payez une seule fois, aucun prélèvement automatique.\n2. 12 mois, toutes les fonctions : réservation, paiement, factures, espace client, avis.\n3. Ensuite, vous choisissez : renouveler au tarif fondateur, passer au mensuel, ou arrêter.\n\n99 € au lieu de 348 €, jusqu'au 31 décembre.\n" + LINK + "\n\nVoix off générée par IA.\n\n#guidance #tarologue #voyance #praticienneguidance #logicielguidance",
  yt=yt("Offre de Noël GuidPilot : 1 an pour 99 €, pourquoi ce prix", ["GuidPilot", "logiciel guidance", "tarologue", "voyante", "offre fondatrice", "réservation en ligne", "praticienne guidance"])),
 "2026-11-13T10:00:00": dict(file="ven-13_reel-noel-prix-consultation.mp4",
  text="Un an de GuidPilot pour le prix d'une seule consultation. ✨\n\nPendant 12 mois : vos clientes réservent et règlent en ligne, même à 23 h ; vos guidances écrites ou audio les attendent dans leur espace ; les factures se créent seules et les avis rejoignent votre page.\n99 € payés une fois, aucun prélèvement automatique. Au bout d'un an, vous choisissez : renouveler, passer au mensuel, ou arrêter.\n\nJusqu'au 31 décembre.\n" + LINK + "\n\n" + IA + "\n\n#tarologue #voyante #medium #guidance #logicielvoyance",
  yt=yt("Logiciel pour tarologue et voyante : 1 an pour le prix d'une consultation", ["tarologue", "voyante", "médium", "logiciel voyance", "guidance", "GuidPilot", "réservation en ligne", "espace client"])),
 "2026-11-14T18:00:00": dict(file="sam-14_reel-noel-janvier-equipee.mp4",
  text="En janvier, vous remettez votre activité à plat. Et si cette fois vous arriviez équipée ? 🗓️\n\nSophrologue, réflexologue, praticienne Reiki, hypnothérapeute : dès la première semaine, vos clientes réservent depuis votre page, règlent, la facture est créée, le rappel part tout seul.\nLe prix ? Celui d'une seule séance : 99 € pour 12 mois, payés une fois, aucun prélèvement automatique. Ensuite, vous choisissez.\n\nJusqu'au 31 décembre.\n" + LINK + "\n\nVoix off générée par IA.\n\n#sophrologue #reflexologue #reiki #hypnotherapeute #logicieltherapeute",
  yt=yt("Logiciel pour thérapeute : commencer 2027 équipée, 1 an pour 99 €", ["sophrologue", "réflexologue", "Reiki", "hypnothérapeute", "logiciel thérapeute", "agenda en ligne", "GuidPilot", "facturation"])),
}
for dt, r in REELS.items():
    add(dt, {"autoPublish": True, "draft": False, "text": r["text"], "media": [CDN + W + r["file"]], "videoCoverMilliseconds": 500,
             "providers": [{"network": "instagram"}, {"network": "youtube"}], "publicationDate": pub(dt),
             "instagramData": {"type": "REEL", "showReelOnFeed": True, "isAiGenerated": True}, "youtubeData": r["yt"]})

CARR = {
 "2026-11-12T18:00:00": dict(name="jeu-12_carrousel-noel-99-ce-que-ca-comprend", n=10,
  text="Un an de GuidPilot pour 99 €. Ce que ça comprend, vraiment. 🎁\n\nRéservation en ligne 24 h/24 avec rappels, paiement en ligne ou au cabinet, factures numérotées automatiques, espace client privé avec vos comptes rendus, messagerie à part de votre téléphone, avis, annuaire, cartes cadeaux et forfaits.\nPayé une fois, aucun prélèvement automatique. Dans un an : 149 €/an au tarif fondateur, 29 €/mois, ou arrêt.\n\nJusqu'au 31 décembre.\n" + LINK + "\n\nCaptures réalisées sur un compte de démonstration.\n\n#sophrologue #reiki #reflexologue #praticienbienetre #logicieltherapeute"),
 "2026-11-15T10:00:00": dict(name="dim-15_carrousel-noel-et-apres", n=9,
  text="1 an pour 99 €… et après ? La question qu'on nous pose le plus. 🤔\n\nNon, vous ne serez pas prélevée sans rien avoir demandé : l'offre fondatrice ne se renouvelle jamais toute seule. Un mois avant la fin, vous choisissez : renouveler au tarif fondateur (149 €/an), passer au mensuel (29 €), ou arrêter, vos données restant consultables.\n\nJusqu'au 31 décembre.\n" + LINK + "\n\n#guidance #tarologue #voyance #cartomancie #praticienneguidance"),
}
for dt, c in CARR.items():
    add(dt, {"autoPublish": True, "draft": False, "text": c["text"], "media": [RAW + W + f"{c['name']}-{i:02d}.jpg" for i in range(1, c["n"] + 1)],
             "providers": [{"network": "instagram"}], "publicationDate": pub(dt), "instagramData": {"type": "POST", "isAiGenerated": False}})

STORIES = ["mer-11_1600_noel-un-an-99", "jeu-12_1600_noel-question", "ven-13_1600_noel-aucun-prelevement", "sam-14_1600_noel-fonction-reservation", "dim-15_1600_noel-prix-consultation"]
for n in STORIES:
    day = {"mer": "11", "jeu": "12", "ven": "13", "sam": "14", "dim": "15"}[n[:3]]
    dt = f"2026-11-{day}T16:00:00"
    add(dt, {"autoPublish": True, "draft": False, "media": [RAW + W + "stories/" + n + ".jpg"], "providers": [{"network": "instagram"}],
             "publicationDate": pub(dt), "instagramData": {"type": "STORY", "isAiGenerated": False}})

FB_TAIL = "\n\n" + OFFRE + "\n✨ GuidPilot : un outil conçu pour les praticiens en guidance (tarot, voyance, médiumnité, astrologie) et les thérapeutes du bien-être (Reiki, LaHoChi, sophrologie, hypnose, réflexologie).\n👉 https://guidpilot.fr/offre-fondatrice"
FB = [
 ("2026-11-11T10:00:00", "REEL", [CDN + W + "mer-11_reel-noel-pourquoi-99.mp4"],
  "Un an de GuidPilot pour 99 €. Voilà pourquoi. 🎁\n\nNous cherchons nos premières praticiennes et nos premiers thérapeutes : celles et ceux qui nous font confiance avant les avis et les témoignages. Vous payez une seule fois, vous avez toutes les fonctions pendant 12 mois, et ensuite vous choisissez : renouveler au tarif fondateur, passer au mensuel, ou arrêter." + FB_TAIL + "\n\n" + FB_IA),
 ("2026-11-12T18:00:00", "POST", [RAW + W + f"jeu-12_carrousel-noel-99-ce-que-ca-comprend-{i:02d}.jpg" for i in range(1, 11)],
  "Un an de GuidPilot pour 99 €. Ce que ça comprend, vraiment. 🎁\n\nRéservation en ligne 24 h/24 avec rappels, paiement en ligne ou au cabinet, factures numérotées automatiques, espace client privé, messagerie, avis, annuaire, cartes cadeaux et forfaits. Pour les thérapeutes (sophrologie, Reiki, réflexologie, hypnose) comme pour les praticiennes en guidance (tarot, voyance, astrologie)." + FB_TAIL + "\n\nCaptures réalisées sur un compte de démonstration."),
 ("2026-11-13T10:00:00", "REEL", [CDN + W + "ven-13_reel-noel-prix-consultation.mp4"],
  "Un an de GuidPilot pour le prix d'une seule consultation. ✨\n\nPendant 12 mois, vos clientes réservent et règlent en ligne, vos guidances ou comptes rendus les attendent dans leur espace, les factures se créent seules et les avis rejoignent votre page. 99 € payés une fois, aucun prélèvement automatique." + FB_TAIL + "\n\n" + FB_IA),
 ("2026-11-14T18:00:00", "REEL", [CDN + W + "sam-14_reel-noel-janvier-equipee.mp4"],
  "En janvier, vous remettez votre activité à plat. Et si cette fois vous arriviez équipée ? 🗓️\n\nDès la première semaine : réservation depuis votre page, paiement, facture créée, rappel envoyé tout seul. Le prix ? Celui d'une seule séance." + FB_TAIL + "\n\n" + FB_IA),
 ("2026-11-15T10:00:00", "POST", [RAW + W + f"dim-15_carrousel-noel-et-apres-{i:02d}.jpg" for i in range(1, 10)],
  "1 an pour 99 €… et après ? La question qu'on nous pose le plus. 🤔\n\nL'offre fondatrice ne se renouvelle jamais toute seule. Un mois avant la fin, vous choisissez : renouveler au tarif fondateur (149 €/an), passer au mensuel (29 €), ou arrêter, vos données restant consultables et exportables." + FB_TAIL),
]
for dt, typ, media, text in FB:
    info = {"autoPublish": True, "draft": False, "text": text, "media": media, "providers": [{"network": "facebook"}], "publicationDate": pub(dt), "facebookData": {"type": typ}}
    if typ == "REEL": info["videoCoverMilliseconds"] = 500
    add(dt, info)

out = pathlib.Path(__file__).parent / "build" / "posts_noel_2026-11-11.json"
out.write_text(json.dumps(POSTS, ensure_ascii=False, indent=1))
print(len(POSTS), "posts →", out)
