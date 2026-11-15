"""Légendes, titres YouTube et payloads Metricool — semaine du 16 au 22/11/2026 (lot lancé à la main par Normane le 15/11).
Usage : python3 posts_2026-11-16.py <SHA>  → build/posts_2026-11-16.json (liste de {date, info})."""
import json, sys, pathlib, importlib.util
SHA = sys.argv[1] if len(sys.argv) > 1 else "SHA"
CDN = f"https://cdn.jsdelivr.net/gh/guidpilot/guidpilot-media@{SHA}/"
RAW = f"https://raw.githubusercontent.com/guidpilot/guidpilot-media/{SHA}/"
W = "2026-11-16_au_22/"
TZ = "Europe/Paris"
IA = "Voix off générée par IA."
FB_IA = "🤖 Contenu créé avec l'IA : voix off générée par IA."
LINK = "👉 Lien en bio : guidpilot.fr/offre-fondatrice"
RAPPEL = "🎁 Jusqu'au 31 décembre : 1 an de GuidPilot pour 99 €, lien en bio."

def pub(dt): return {"dateTime": dt, "timezone": TZ}
def yt_short(title, tags): return {"title": title + " #shorts", "type": "short", "privacy": "public", "madeForKids": False, "isAiGeneratedContent": True, "category": "HOWTO_STYLE", "tags": tags}

POSTS = []
def add(dt, info): POSTS.append({"date": dt + "+01:00", "info": info})

# ---------- Instagram + YouTube Shorts ----------
REELS = {
 "2026-11-17T18:00:00": dict(file="mar-17_reel-partenaires-janvier.mp4",
  text="En janvier, vos élèves ouvrent leur cabinet. Avec quel outil ? 🤝\n\nFormatrices, écoles, créatrices de contenu : à la fin d'une formation, c'est à vous qu'on demande par où commencer pour les rendez-vous, les paiements et les factures.\nGuidPilot est un outil conçu pour les praticiens en guidance et les thérapeutes. Et jusqu'au 31 décembre, votre communauté peut s'équiper pour un an à 99 €.\nNous cherchons des partenaires pour le faire connaître.\n\n💬 Commentez PARTENAIRE et recevez le lien pour candidater.\n\nCaptures réalisées sur un compte de démonstration. " + IA + "\n\n#formatrice #praticienbienetre #guidance #therapeute #partenariat",
  yt=yt_short("Programme partenaire et affiliation : logiciel pour thérapeutes et praticiens en guidance", ["programme partenaire", "affiliation", "logiciel thérapeute", "logiciel guidance", "formation Reiki", "formation tarot", "école sophrologie", "GuidPilot"])),
 "2026-11-18T18:00:00": dict(file="mer-18_reel-noel-le-calcul.mp4",
  text="99 € divisés par 12 mois. Tarologue, voyante, médium : faites le calcul. 🧮\n\n8,25 € par mois. Au mois, c'est 29 €, soit 348 € sur un an.\nPour ce prix : la réservation en ligne, le paiement et les factures, l'espace privé de vos clientes, les avis sur votre page.\nPayé une seule fois, aucun prélèvement automatique. Ensuite, vous choisissez.\n\nJusqu'au 31 décembre.\n" + LINK + "\n\n" + IA + "\n\n#tarologue #voyance #guidance #praticienneguidance #logicielguidance",
  yt=yt_short("Logiciel pour tarologue et voyante : 1 an pour 99 €, soit 8,25 € par mois", ["tarologue", "voyante", "médium", "logiciel voyance", "logiciel guidance", "GuidPilot", "réservation en ligne", "offre fondatrice"])),
 "2026-11-19T18:00:00": dict(file="jeu-19_reel-coulisses-bouton-inscription.mp4",
  text="Coulisses : sur téléphone, notre bouton d'inscription était hors de l'écran. 🙈\n\nOn l'a découvert cette semaine. Alors : la page d'inscription a été refaite pour le téléphone, la page d'essai a été allégée, et un assistant répond maintenant à vos questions sur le site.\nUn outil pour thérapeutes et praticiennes en guidance se construit avec vos retours.\n\nEt vous, qu'est-ce qui vous fait quitter une inscription ? 👇\n\n" + RAPPEL + "\n\n" + IA + "\n\n#sophrologue #reiki #praticienbienetre #coulisses",
  yt=yt_short("Coulisses de GuidPilot, logiciel pour thérapeutes : ce qu'on a corrigé cette semaine", ["GuidPilot", "logiciel thérapeute", "sophrologue", "praticien bien-être", "coulisses", "logiciel cabinet", "prise de rendez-vous en ligne"])),
 "2026-11-22T18:00:00": dict(file="dim-22_reel-calendrier-avent.mp4",
  text="24 jours, 24 astuces pour votre activité de tarologue, voyante ou médium. 🎄\n\nÀ partir du 1er décembre : un calendrier de l'Avent en stories. Une astuce par jour, à appliquer tout de suite : messages prêts à copier, agenda de janvier, paiements sans relance, avis.\nPour ne rien manquer, abonnez-vous au compte.\n\nQuelle astuce aimeriez-vous y trouver ? 👇\n\n" + RAPPEL + "\n\n" + IA + "\n\n#tarologue #guidance #cartomancie #praticienneguidance",
  yt=yt_short("Tarologue, voyante : 24 astuces pour votre activité, le calendrier de l'Avent", ["tarologue", "voyante", "médium", "guidance", "conseils praticienne", "calendrier de l'Avent", "développer son activité"])),
}
for dt, r in REELS.items():
    add(dt, {"autoPublish": True, "draft": False, "text": r["text"], "media": [CDN + W + r["file"]], "videoCoverMilliseconds": 500,
             "providers": [{"network": "instagram"}, {"network": "youtube"}], "publicationDate": pub(dt),
             "instagramData": {"type": "REEL", "showReelOnFeed": True, "isAiGenerated": True}, "youtubeData": r["yt"]})

CARR = {
 "2026-11-16T10:00:00": dict(name="lun-16_carrousel-bilan-2026-4-questions", n=9,
  text="Tarologue, voyante, médium : votre bilan 2026 en 4 questions. 📝\n\nD'où sont venues vos clientes ? Quelle prestation a été la plus demandée ? Qu'est-ce qui vous a pris le plus de temps hors séance ? Qui n'est pas revenue ?\n10 minutes, un carnet, pas de tableur.\nDans GuidPilot, l'historique de chaque cliente et vos encaissements du mois sont déjà dans votre espace.\n\nQuelle réponse vous a surprise ? 👇\n\n🔖 Enregistrez ce post pour votre bilan de décembre.\n" + RAPPEL + "\n\nCapture réalisée sur un compte de démonstration.\n\n#tarologue #voyance #guidance #praticienneguidance"),
 "2026-11-20T10:00:00": dict(name="ven-20_carrousel-salon-rendez-vous", n=10,
  text="Salon du bien-être : repartez avec des rendez-vous, pas des cartes de visite. 🎪\n\nMédium, tarologue, énergéticienne : sur un stand, l'envie de réserver dure quelques minutes. Une prestation « spéciale salon », votre lien en QR code, une question avant le discours, une date proposée sur place, un message le soir même.\nDans GuidPilot, votre lien mène à votre page : prestations, créneaux, paiement en ligne possible.\n\nVous exposez cet hiver ? 👇\n\n🔖 Enregistrez ce post avant votre prochain salon.\n" + RAPPEL + "\n\n#medium #tarologue #energeticienne #salonbienetre #guidance"),
 "2026-11-21T10:00:00": dict(name="sam-21_carrousel-noel-liste-de-souhaits", n=9,
  text="Sophrologue, réflexologue, praticienne Reiki : cette année, votre liste au Père Noël tient en 5 lignes. 🎁\n\nNe plus relancer un paiement. Ne plus faire vos factures le soir. Ne plus répondre « vous êtes dispo quand ? ». Ne plus chercher un compte rendu. Oser demander un avis.\nLes cinq, dans un seul cadeau : 1 an de GuidPilot pour 99 € au lieu de 348 €, payé une fois, aucun prélèvement automatique.\n\nJusqu'au 31 décembre.\n" + LINK + "\n\nQuel souhait cochez-vous en premier ? 👇\n\n#sophrologue #reflexologue #reiki #praticienbienetre #logicieltherapeute"),
}
for dt, c in CARR.items():
    add(dt, {"autoPublish": True, "draft": False, "text": c["text"], "media": [RAW + W + f"{c['name']}-{i:02d}.jpg" for i in range(1, c["n"] + 1)],
             "providers": [{"network": "instagram"}], "publicationDate": pub(dt), "instagramData": {"type": "POST", "isAiGenerated": False}})

# ---------- Stories Instagram (13 + 7 offre de Noël) ----------
def load(path, name):
    spec = importlib.util.spec_from_file_location(name, pathlib.Path(__file__).parent / path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
DAY = {"lun": "16", "mar": "17", "mer": "18", "jeu": "19", "ven": "20", "sam": "21", "dim": "22"}
for s in load("stories/specs_2026-11-16.py", "st").STORIES:
    n = s["name"]; h = n.split("_")[1]
    dt = f"2026-11-{DAY[n[:3]]}T{h[:2]}:{h[2:]}:00"
    add(dt, {"autoPublish": True, "draft": False, "media": [RAW + W + "stories/" + n + ".jpg"], "providers": [{"network": "instagram"}],
             "publicationDate": pub(dt), "instagramData": {"type": "STORY", "isAiGenerated": False}})

# ---------- TikTok ----------
for k, s in load("reels/tiktok_specs_2026-11-16.py", "tt").SPECS.items():
    add(s["date"], {"autoPublish": True, "draft": False, "text": s["caption"], "media": [CDN + "tiktok/lot-2026-11-16/" + s["file"]],
                    "providers": [{"network": "tiktok"}], "publicationDate": pub(s["date"]),
                    "tiktokData": {"privacyOption": "PUBLIC_TO_EVERYONE", "commercialContentOwnBrand": True, "isAigc": True, "title": s["caption"], "disableComment": False, "disableDuet": False, "disableStitch": False}})

# ---------- Facebook ----------
PUBLICS = "✨ GuidPilot : un outil conçu pour les praticiens en guidance (tarot, voyance, médiumnité, astrologie) et les thérapeutes du bien-être (Reiki, LaHoChi, sophrologie, hypnose, réflexologie)."
FB_TAIL = "\n\n" + PUBLICS + "\n👉 14 jours gratuits, sans carte bancaire : https://guidpilot.fr\n🎁 Jusqu'au 31 décembre : 1 an pour 99 €, payé une fois → https://guidpilot.fr/offre-fondatrice"
FB_NOEL = "\n\n🎁 Offre de Noël : 1 an de GuidPilot pour 99 € au lieu de 348 €, payé une fois, aucun prélèvement automatique. Jusqu'au 31 décembre.\n" + PUBLICS + "\n👉 https://guidpilot.fr/offre-fondatrice"
def imgs(name, n): return [RAW + W + f"{name}-{i:02d}.jpg" for i in range(1, n + 1)]
FB = [
 ("2026-11-16T09:30:00", "POST", [CDN + "youtube/2026-11-10_trouver-clients-sophrologie-reiki-hypnose.mp4"],
  "Sophrologie, Reiki, hypnose : les 5 questions que se pose une future cliente avant de réserver. 💭\n\n« C'est pour moi ? », « Ça se passe comment ? », « Je peux lui faire confiance ? », « Comment je réserve ? », « Je peux en parler ? » : une réponse simple à chacune, valable aussi pour les praticiennes en guidance." + FB_TAIL + "\n\n" + FB_IA,
  "Comment trouver des clients en sophrologie, Reiki ou hypnose : les 5 questions d'une future cliente"),
 ("2026-11-16T12:45:00", "POST", imgs("lun-16_carrousel-bilan-2026-4-questions", 9),
  "Votre bilan 2026 en 4 questions. 📝\n\nD'où sont venues vos clientes ? Quelle prestation a été la plus demandée ? Qu'est-ce qui vous a pris le plus de temps hors séance ? Qui n'est pas revenue ? Dix minutes, un carnet, pas de tableur : utile aux thérapeutes (sophrologie, Reiki, réflexologie) comme aux praticiennes en guidance (tarot, voyance)." + FB_TAIL + "\n\nCapture réalisée sur un compte de démonstration.", None),
 ("2026-11-17T18:00:00", "REEL", [CDN + W + "mar-17_reel-partenaires-janvier.mp4"],
  "En janvier, vos élèves ouvrent leur cabinet. Avec quel outil ? 🤝\n\nFormatrices, écoles, créatrices de contenu : à la fin d'une formation, c'est à vous qu'on demande par où commencer pour les rendez-vous, les paiements et les factures. Jusqu'au 31 décembre, votre communauté peut s'équiper pour un an à 99 €.\n\nNous cherchons des partenaires pour faire connaître GuidPilot. Candidature : https://guidpilot.fr/affiliation/candidature\n\n" + PUBLICS + "\n\nCaptures réalisées sur un compte de démonstration. " + FB_IA, None),
 ("2026-11-18T09:30:00", "POST", [CDN + "youtube/2026-11-13_payer-avant-guidance.mp4"],
  "Comment se faire payer avant une guidance, sans paraître insistante. 💳\n\nQuatre réflexes : tout annoncer avant (tarif, durée, format, délai), faire du règlement une étape de la réservation, répondre calmement à « je peux payer après ? », et écrire ses conditions avant le premier souci. Valable aussi pour une séance de Reiki ou de sophrologie." + FB_TAIL + "\n\n" + FB_IA,
  "Tarologue, voyante : comment se faire payer avant une guidance sans paraître insistante"),
 ("2026-11-18T18:00:00", "REEL", [CDN + W + "mer-18_reel-noel-le-calcul.mp4"],
  "99 € divisés par 12 mois. Faites le calcul. 🧮\n\n8,25 € par mois, pour la réservation en ligne, le paiement et les factures, l'espace privé de vos clientes et les avis sur votre page. Au mois, c'est 29 €, soit 348 € sur un an." + FB_NOEL + "\n\n" + FB_IA, None),
 ("2026-11-19T18:00:00", "REEL", [CDN + W + "jeu-19_reel-coulisses-bouton-inscription.mp4"],
  "Coulisses : sur téléphone, notre bouton d'inscription était hors de l'écran. 🙈\n\nOn l'a découvert cette semaine. La page d'inscription a été refaite pour le téléphone, la page d'essai allégée, et un assistant répond maintenant à vos questions sur le site. Un outil se construit avec vos retours : qu'est-ce qui vous fait quitter une inscription ?" + FB_TAIL + "\n\n" + FB_IA, None),
 ("2026-11-20T12:45:00", "POST", imgs("ven-20_carrousel-salon-rendez-vous", 10),
  "Salon du bien-être : repartez avec des rendez-vous, pas des cartes de visite. 🎪\n\nLe mini-guide en 5 étapes : une prestation « spéciale salon », votre lien de réservation en QR code, une question avant le discours, une date proposée sur place, un message le soir même. Pour les praticiennes en guidance comme pour les thérapeutes (Reiki, sophrologie, réflexologie)." + FB_TAIL, None),
 ("2026-11-21T12:45:00", "POST", imgs("sam-21_carrousel-noel-liste-de-souhaits", 9),
  "Cette année, votre liste au Père Noël tient en 5 lignes. 🎁\n\nNe plus relancer un paiement, ne plus faire vos factures le soir, ne plus répondre « vous êtes dispo quand ? », ne plus chercher un compte rendu, oser demander un avis. Les cinq, dans un seul cadeau." + FB_NOEL, None),
 ("2026-11-22T18:00:00", "REEL", [CDN + W + "dim-22_reel-calendrier-avent.mp4"],
  "24 jours, 24 astuces pour votre activité. 🎄\n\nÀ partir du 1er décembre, un calendrier de l'Avent en stories : une astuce par jour, à appliquer tout de suite. Messages prêts à copier, agenda de janvier, paiements sans relance, avis. Pour les praticiennes en guidance comme pour les thérapeutes. Abonnez-vous à la page pour ne rien manquer." + FB_TAIL + "\n\n" + FB_IA, None),
]
for dt, typ, media, text, title in FB:
    fbd = {"type": typ}
    if title: fbd["title"] = title
    info = {"autoPublish": True, "draft": False, "text": text, "media": media, "providers": [{"network": "facebook"}], "publicationDate": pub(dt), "facebookData": fbd}
    if typ == "REEL": info["videoCoverMilliseconds"] = 500
    add(dt, info)

out = pathlib.Path(__file__).parent / "build" / "posts_2026-11-16.json"
out.write_text(json.dumps(POSTS, ensure_ascii=False, indent=1))
print(len(POSTS), "posts →", out)
