"""Définition des 7 posts Instagram du 8 au 11 octobre 2026 (légendes + médias + horaires)."""
import json

CDN = "https://cdn.jsdelivr.net/gh/guidpilot/guidpilot-media@main/2026-10-08_au_11/"
CTA = "Testez GuidPilot gratuitement pendant 14 jours, sans carte bancaire.\n👉 Lien en bio : guidpilot.fr"
H_GUIDANCE = "#tarologue #voyance #guidance #cartomancie #oracle #medium #tarot #praticienne #entrepreneuse #logicielpraticien"
H_BIENETRE = "#soinsenergetiques #energeticienne #reiki #therapeuteholistique #praticiennebienetre #bienetre #entrepreneuse #organisation #guidance #guidpilot"

def car(name):
    return [f"{CDN}{name}-{i:02d}.jpg" for i in range(1, 8)]

POSTS = [
 {"date": "2026-10-08T18:00:00", "type": "REEL", "ai": True, "media": [CDN + "reel-specialiste-guidance.mp4"], "cover_ms": 9000,
  "text": f"""Logiciel pour tarologues, médiums et praticiennes en guidance : enfin un outil pensé pour votre métier.

Avec GuidPilot :
✔ votre propre page praticien, avec vos prestations et vos avis
✔ une place dans l'annuaire GuidPilot pour que de nouvelles clientes vous trouvent
✔ la facture créée automatiquement à chaque réservation payée
✔ 0 % de commission sur vos séances (hors frais du moyen de paiement)

{CTA}

Et vous, quel outil utilisez-vous aujourd'hui pour gérer vos rendez-vous ?

{H_GUIDANCE}"""},
 {"date": "2026-10-09T10:00:00", "type": "POST", "ai": False, "media": car("c1-organisation"),
  "text": f"""Praticienne en guidance ou en soins énergétiques : votre organisation vous fait-elle perdre des clientes ?

5 signes à repérer (faites défiler) :
1. Les rendez-vous se prennent par messages
2. Tout est noté dans un carnet
3. Le paiement se demande par message
4. Personne n'est relancé après la séance
5. Les guidances partent par WhatsApp

Combien en cochez-vous ? Dites-le en commentaire 👇

GuidPilot réunit réservation, paiement, agenda, guidances, factures et avis dans un seul espace.
{CTA}

Enregistrez ce post pour faire le point plus tard.

{H_BIENETRE}"""},
 {"date": "2026-10-09T18:00:00", "type": "REEL", "ai": False, "media": [CDN + "reel-pov-23h.mp4"], "cover_ms": 1500,
  "text": f"""POV : une cliente réserve votre tirage de tarot à 23 h… et vous dormez.

Avec GuidPilot, votre page de réservation travaille pour vous :
✔ la cliente choisit sa séance et paie en ligne
✔ le rendez-vous arrive dans votre agenda
✔ la facture est créée automatiquement
✔ la confirmation part toute seule

Le matin, tout est prêt.

{CTA}

{H_GUIDANCE}"""},
 {"date": "2026-10-10T10:00:00", "type": "POST", "ai": False, "media": car("c2-avis"),
  "text": f"""Demander un avis à vos clientes sans paraître insistante : 3 messages prêts à copier.

Les avis rassurent les futures clientes qui hésitent à réserver une guidance ou une séance. Le bon moment : 24 à 48 h après la séance.

À retenir : ne proposez jamais de réduction ou de cadeau en échange d'un avis.

Avec GuidPilot, la demande d'avis part en un clic et les avis s'affichent sur votre page praticien.
{CTA}

Enregistrez ce post pour avoir les messages sous la main.

{H_BIENETRE}"""},
 {"date": "2026-10-10T18:00:00", "type": "REEL", "ai": True, "media": [CDN + "reel-tout-en-un.mp4"], "cover_ms": 8000,
  "text": f"""Tarologue, médium ou praticienne en guidance ? Votre activité tient dans cinq applis différentes ?

Agenda, messagerie, tableur clients, paiements, factures… GuidPilot réunit tout dans un seul espace :
✔ vos rendez-vous, vos revenus et vos avis en un coup d'œil
✔ la réservation et le paiement en ligne depuis votre page
✔ vos guidances écrites ou vocales livrées dans un espace client sécurisé
✔ une demande d'avis en un clic après chaque séance

{CTA}

{H_GUIDANCE}"""},
 {"date": "2026-10-11T10:00:00", "type": "POST", "ai": False, "media": car("c3-paiement"),
  "text": f"""Paiement à l'avance pour une guidance ou une séance : comment le demander sans passer pour une arnaque ?

Beaucoup de clientes se méfient, et c'est compréhensible. 4 réflexes qui rassurent (faites défiler) :
1. Affichez vos tarifs clairement
2. Annoncez votre politique d'annulation
3. Utilisez un paiement en ligne sécurisé
4. Envoyez une vraie facture

GuidPilot vous donne une page de réservation avec vos tarifs, un paiement sécurisé et une facture créée automatiquement.
{CTA}

Et vous, demandez-vous le paiement avant ou après la séance ? 👇

{H_BIENETRE}"""},
 {"date": "2026-10-11T18:00:00", "type": "REEL", "ai": False, "media": [CDN + "reel-avant-apres.mp4"], "cover_ms": 2500,
  "text": f"""Avant / après : quand votre activité de praticienne était éparpillée partout.

Carnet papier, WhatsApp, PayPal, tableur, e-mails… Avec GuidPilot, tout votre cabinet tient dans un seul espace :
✔ réservation en ligne
✔ paiement sécurisé
✔ guidances écrites et vocales
✔ factures automatiques
✔ avis clients

{CTA}

Lequel de ces outils utilisez-vous encore ? 👇

{H_BIENETRE}"""},
]

def info(p, draft=True):
    ig = {"type": p["type"]}
    if p["ai"]: ig["isAiGenerated"] = True
    d = {"autoPublish": True, "descendants": [], "draft": draft, "firstCommentText": "", "hasNotReadNotes": False,
         "media": p["media"], "mediaAltText": [], "providers": [{"network": "instagram"}],
         "publicationDate": {"dateTime": p["date"], "timezone": "Europe/Paris"}, "shortener": False,
         "smartLinkData": {"ids": []}, "text": p["text"], "instagramData": ig}
    if p["type"] == "REEL": d["videoCoverMilliseconds"] = p["cover_ms"]
    return json.dumps(d, ensure_ascii=False)

if __name__ == "__main__":
    for i, p in enumerate(POSTS):
        open(f"post_{i+1}.json", "w").write(info(p))
        print(i + 1, p["date"], p["type"], len(p["text"]))
