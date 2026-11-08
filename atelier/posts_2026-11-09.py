"""Légendes, titres YouTube et payloads Metricool — semaine du 09 au 15/11/2026.
Usage : python3 posts_2026-11-09.py <SHA>  → build/posts_2026-11-09.json (liste de {date, info})."""
import json, sys, pathlib
SHA = sys.argv[1] if len(sys.argv) > 1 else "SHA"
CDN = f"https://cdn.jsdelivr.net/gh/guidpilot/guidpilot-media@{SHA}/"
RAW = f"https://raw.githubusercontent.com/guidpilot/guidpilot-media/{SHA}/"
W = "2026-11-09_au_15/"
TZ = "Europe/Paris"
IA = "Captures réalisées sur un compte de démonstration. Voix off générée par IA."
FB_IA = "🤖 Contenu créé avec l'IA : voix off générée par IA."

def pub(dt): return {"dateTime": dt, "timezone": TZ}
def yt_short(title, tags): return {"title": title + " #shorts", "type": "short", "privacy": "public", "madeForKids": False, "isAiGeneratedContent": True, "category": "HOWTO_STYLE", "tags": tags}

POSTS = []
def add(dt, info): POSTS.append({"date": dt + "+01:00", "info": info})

# ---------- Instagram + YouTube Shorts ----------
REELS = {
 "2026-11-09T18:00:00": dict(file="lun-09_reel-c-est-combien.mp4",
  text="« C'est combien ? » Tarologue, voyante : 3 réponses à ne plus jamais envoyer en message privé.\n\n« Ça dépend… », « je vous explique par téléphone », « c'est sur ma page » sans le lien : trois façons de la perdre.\nCe qui marche : le tarif, la durée, et le lien pour réserver, en une phrase.\nDans GuidPilot, vos prestations, vos tarifs et vos créneaux sont sur votre page : votre lien répond à votre place.\n\nEt vous, que répondez-vous ? 👇\n\n🔖 Enregistrez ce post pour plus tard.\n\n#tarologue #voyance #guidance #praticienneguidance",
  yt=yt_short("Tarologue, voyante : que répondre à « c'est combien ? » en message privé", ["tarologue", "voyante", "guidance", "tarifs voyance", "message privé", "réservation en ligne", "praticienne guidance"])),
 "2026-11-11T18:00:00": dict(file="mer-11_reel-astrologue-theme-natal.mp4",
  text="Astrologue : votre thème natal écrit, vous l'envoyez comment ? 🪐\n\nElle commande et règle sur votre page → vous rédigez quand vous voulez, ses données de naissance dans sa fiche → l'étude, écrite ou audio, l'attend dans son espace sécurisé → son avis rejoint votre page.\nUn outil pensé pour votre métier, pas un agenda de plus.\n\n📩 Commentez GUIDANCE et recevez en message privé la présentation de GuidPilot : 14 jours gratuits, sans carte bancaire.\n👉 Ou lien en bio : guidpilot.fr\n\n" + IA + "\n\n#astrologue #astrologie #themenatal #guidance #logicielastrologue",
  yt=yt_short("Logiciel pour astrologue : livrer un thème natal écrit, du paiement à l'avis", ["astrologue", "astrologie", "thème natal", "logiciel astrologue", "guidance", "espace client", "paiement en ligne", "GuidPilot"])),
 "2026-11-13T18:00:00": dict(file="ven-13_reel-avant-de-reserver.mp4",
  text="Ce que vos clientes regardent avant de réserver un tirage… et que vous ne voyez pas. 👀\n\n1. Les avis des autres. 2. Un prix et une durée clairs. 3. Pouvoir réserver sans vous écrire, même à 23 h.\nDans GuidPilot, les trois sont sur votre page : avis publiés, prestations avec tarif, réservation en ligne.\n\nLequel des trois manque chez vous ? 👇\n\n🔖 Enregistrez ce post pour plus tard.\n\n#voyance #tarologue #medium #guidance",
  yt=yt_short("Voyante, tarologue : ce que vos clientes vérifient avant de réserver", ["voyante", "tarologue", "médium", "avis clients", "trouver des clientes voyance", "page de réservation", "guidance"])),
 "2026-11-15T18:00:00": dict(file="dim-15_reel-message-du-lendemain.mp4",
  text="Après le tirage, il y a un message que votre cliente attend… et qu'elle ne reçoit presque jamais. 💌\n\nPas une relance : une attention, le lendemain. Trois lignes : « j'espère que la nuit a porté conseil, si une question remonte, je suis là ».\nElle se sent suivie, elle revient d'elle-même, elle parle de vous.\nDans GuidPilot, ce message part depuis sa fiche, rangé avec sa guidance.\n\nEt vous, vous écrivez le lendemain ? 👇\n\n🔖 Enregistrez ce post pour plus tard.\n\n#tarologue #guidance #cartomancie #fideliser",
  yt=yt_short("Tarologue, médium : le message du lendemain qui fidélise vos clientes", ["tarologue", "médium", "guidance", "fidéliser ses clientes", "suivi client", "cartomancie", "relation cliente"])),
}
for dt, r in REELS.items():
    add(dt, {"autoPublish": True, "draft": False, "text": r["text"], "media": [CDN + W + r["file"]], "videoCoverMilliseconds": 500,
             "providers": [{"network": "instagram"}, {"network": "youtube"}], "publicationDate": pub(dt),
             "instagramData": {"type": "REEL", "showReelOnFeed": True, "isAiGenerated": True}, "youtubeData": r["yt"]})

CARR = {
 "2026-11-12T10:00:00": dict(name="jeu-12_carrousel-annulation-4-reponses",
  text="Elle annule une heure avant. Sophrologue, réflexologue, praticienne Reiki : 4 réponses prêtes à copier. 📋\n\nPremière fois, ça se répète, conditions acceptées, absence sans prévenir : un message pour chaque cas, posé et sans justification.\nDans GuidPilot, vos conditions d'annulation sont acceptées avant le paiement, et le rappel de la veille réduit les oublis.\n\nQuelle est votre règle d'annulation ? 👇\n\n🔖 Enregistrez ce post pour la prochaine fois.\n\n#sophrologue #reflexologue #reiki #praticienbienetre"),
 "2026-11-14T10:00:00": dict(name="sam-14_carrousel-reflexologue-journee",
  text="Réflexologue : une journée, deux façons de la vivre. ☀️\n\n8 h 30, 10 h, 12 h 15, 14 h, 18 h, 21 h : la même journée de cabinet, avec et sans outil pensé pour votre métier. Réservation pendant vos séances, paiement au cabinet en un clic, lien de visio automatique, compte rendu dans l'espace client, factures numérotées.\nUn outil pensé pour votre métier, pas un agenda de plus.\n\n📩 Commentez THÉRAPEUTE et recevez en message privé la présentation de GuidPilot : 14 jours gratuits, sans carte bancaire.\n👉 Ou lien en bio : guidpilot.fr\n\nCaptures réalisées sur un compte de démonstration.\n\n#reflexologue #reflexologie #cabinetbienetre #logicieltherapeute #praticienbienetre"),
}
for dt, c in CARR.items():
    add(dt, {"autoPublish": True, "draft": False, "text": c["text"], "media": [RAW + W + f"{c['name']}-{i:02d}.jpg" for i in range(1, 11)],
             "providers": [{"network": "instagram"}], "publicationDate": pub(dt), "instagramData": {"type": "POST", "isAiGenerated": False}})

# ---------- Stories Instagram ----------
STORIES = ["lun-09_1230_conseil-lien-bio", "lun-09_2000_teaser-c-est-combien", "mar-10_1230_mot-cle-therapeute", "mar-10_2000_teaser-partenaires",
           "mer-11_1230_question-etude-ecrite", "mer-11_2000_teaser-astrologue", "jeu-12_1230_fonction-avis-page", "jeu-12_2000_teaser-annulation",
           "ven-13_1230_conseil-tarif-duree", "ven-13_2000_teaser-avant-de-reserver", "sam-14_1230_mot-cle-therapeute", "sam-14_2000_teaser-reflexologue",
           "dim-15_1230_question-lendemain"]
for n in STORIES:
    d, h = n.split("_")[0], n.split("_")[1]
    day = {"lun": "09", "mar": "10", "mer": "11", "jeu": "12", "ven": "13", "sam": "14", "dim": "15"}[d[:3]]
    dt = f"2026-11-{day}T{h[:2]}:{h[2:]}:00"
    add(dt, {"autoPublish": True, "draft": False, "media": [RAW + W + "stories/" + n + ".jpg"], "providers": [{"network": "instagram"}],
             "publicationDate": pub(dt), "instagramData": {"type": "STORY", "isAiGenerated": False}})

# ---------- TikTok ----------
import importlib.util
spec = importlib.util.spec_from_file_location("tt", pathlib.Path(__file__).parent / "reels" / "tiktok_specs_2026-11-09.py")
tt = importlib.util.module_from_spec(spec); spec.loader.exec_module(tt)
for k, s in tt.SPECS.items():
    add(s["date"], {"autoPublish": True, "draft": False, "text": s["caption"], "media": [CDN + "tiktok/lot-2026-11-09/" + s["file"]],
                    "providers": [{"network": "tiktok"}], "publicationDate": pub(s["date"]),
                    "tiktokData": {"privacyOption": "PUBLIC_TO_EVERYONE", "commercialContentOwnBrand": True, "isAigc": True, "title": s["caption"], "disableComment": False, "disableDuet": False, "disableStitch": False}})

# ---------- Facebook ----------
FB_TAIL = "\n\n✨ GuidPilot : un outil conçu pour les praticiens en guidance (tarot, voyance, médiumnité, astrologie) et les thérapeutes du bien-être (Reiki, LaHoChi, sophrologie, hypnose, réflexologie).\n👉 14 jours gratuits, sans carte bancaire : https://guidpilot.fr"
FB = [
 ("2026-11-09T09:30:00", "POST", "youtube/2026-11-06_logiciel-medium-energeticienne.mp4",
  "Médium, énergéticienne : la checklist des consultations à distance. 📋\n\nUne prestation par format (visio, écrite, vocale) avec son délai, le règlement à la réservation, la guidance rangée dans un espace privé plutôt que dans une messagerie perso, et une page à votre nom." + FB_TAIL + "\n\n" + FB_IA,
  "Logiciel pour médium et énergéticienne : la checklist des consultations à distance"),
 ("2026-11-09T18:00:00", "REEL", W + "lun-09_reel-c-est-combien.mp4",
  "« C'est combien ? » Trois réponses à ne plus jamais envoyer en message privé, que vous soyez tarologue, voyante, sophrologue ou praticienne Reiki.\n\nCe qui marche : le tarif, la durée, et le lien pour réserver, en une phrase. Avec GuidPilot, vos prestations, vos tarifs et vos créneaux sont sur votre page : votre lien répond à votre place." + FB_TAIL + "\n\n" + FB_IA, None),
 ("2026-11-11T09:30:00", "POST", "youtube/2026-11-03_logiciel-sophrologue-hypnotherapeute.mp4",
  "Sophrologue, hypnothérapeute : les 4 moments d'un cycle de séances. 🔁\n\nAvant la première séance, la veille, juste après, et sur tout le cycle : ce qu'un outil pensé pour votre cabinet gère à votre place (conditions écrites, rappel automatique avec lien de visio, compte rendu dans l'espace client, forfait décompté, factures, demande d'avis)." + FB_TAIL + "\n\n" + FB_IA,
  "Logiciel pour sophrologue et hypnothérapeute : les 4 moments d'un cycle de séances"),
 ("2026-11-12T12:45:00", "POST", [RAW + W + f"jeu-12_carrousel-annulation-4-reponses-{i:02d}.jpg" for i in range(1, 11)],
  "Elle annule une heure avant : 4 réponses prêtes à copier. 📋\n\nPremière fois, ça se répète, conditions acceptées, absence sans prévenir : un message pour chaque cas, posé et sans justification. Utile aux thérapeutes (sophrologie, Reiki, réflexologie) comme aux praticiennes en guidance (tarot, voyance).\n\nAvec GuidPilot, vos conditions d'annulation sont acceptées avant le paiement, et le rappel par e-mail de la veille réduit les oublis." + FB_TAIL, None),
 ("2026-11-13T18:00:00", "REEL", W + "ven-13_reel-avant-de-reserver.mp4",
  "Ce que vos clientes regardent avant de réserver… et que vous ne voyez pas. 👀\n\nLes avis des autres, un prix et une durée clairs, et pouvoir réserver sans vous écrire, même à 23 h. Valable pour une séance de tarot comme pour un soin Reiki ou une séance de sophrologie. Avec GuidPilot, les trois sont sur votre page." + FB_TAIL + "\n\n" + FB_IA, None),
 ("2026-11-14T12:45:00", "POST", [RAW + W + f"sam-14_carrousel-reflexologue-journee-{i:02d}.jpg" for i in range(1, 10)],
  "Réflexologue : une journée, deux façons de la vivre. ☀️\n\n8 h 30, 10 h, 12 h 15, 14 h, 18 h, 21 h : la même journée de cabinet, avec et sans outil pensé pour votre métier. Réservation pendant vos séances, paiement au cabinet en un clic, lien de visio automatique, compte rendu dans l'espace client, factures numérotées. Le même parcours existe pour les praticiennes en guidance (tarot, voyance, astrologie)." + FB_TAIL + "\n\nCaptures réalisées sur un compte de démonstration.", None),
 ("2026-11-15T18:00:00", "REEL", W + "dim-15_reel-message-du-lendemain.mp4",
  "Après la séance, il y a un message que votre cliente attend… et qu'elle ne reçoit presque jamais. 💌\n\nPas une relance : une attention, le lendemain. Trois lignes suffisent. Elle se sent suivie, elle revient d'elle-même, elle parle de vous. Que vous soyez tarologue, médium, sophrologue ou praticienne Reiki. Avec GuidPilot, ce message part depuis sa fiche, rangé avec sa guidance ou son compte rendu." + FB_TAIL + "\n\n" + FB_IA, None),
]
for dt, typ, media, text, title in FB:
    med = media if isinstance(media, list) else [CDN + media]
    fbd = {"type": typ}
    if title: fbd["title"] = title
    info = {"autoPublish": True, "draft": False, "text": text, "media": med, "providers": [{"network": "facebook"}], "publicationDate": pub(dt), "facebookData": fbd}
    if typ == "REEL": info["videoCoverMilliseconds"] = 500
    add(dt, info)

out = pathlib.Path(__file__).parent / "build" / "posts_2026-11-09.json"
out.write_text(json.dumps(POSTS, ensure_ascii=False, indent=1))
print(len(POSTS), "posts →", out)
