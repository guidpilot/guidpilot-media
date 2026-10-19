# Tutoriels vidéo « Mettre en place GuidPilot »

Vidéos 1920×1080 pour YouTube (non répertorié) et la rubrique **Aide & tutoriels** de l'app.
Montées à partir de **vraies captures du compte de démonstration**, avec la voix off Claire (ElevenLabs).

## Série

| # | Titre | Spec | État (19/10/2026) |
|---|---|---|---|
| 1 | Compléter votre profil | à écrire | captures à faire |
| 2 | Créer vos prestations | `specs/t02_prestations.py` | ✅ |
| 3 | Régler vos disponibilités | `specs/t03_disponibilites.py` | ✅ |
| 4 | Activer le paiement en ligne | `specs/t04_paiements.py` | ✅ |
| 5 | Personnaliser votre page publique | à écrire | captures à faire |
| 6 | (Google Agenda) | — | en attente de la vérification Google OAuth |

## Chaîne

1. **Capture** (navigateur intégré, compte démo, fenêtre 1440×900) : coller `outils/snap.js` dans la page → `window.__s()`
   renvoie le HTML autonome de l'écran (CSS, images en data URI réduites, valeurs des champs, défilement).
   Le résultat est enregistré dans un fichier, puis `python3 outils/grab.py <nom>` l'extrait dans `snaps/<nom>.html`.
   **Les captures ne vont jamais dans ce dépôt public** (données du compte démo) : elles restent dans l'atelier local.
2. **Masquer** toute donnée sensible dans la copie locale avant rendu (IBAN, titulaire, BIC, e-mails…).
3. **Spec** `specs/tNN_*.py` : scènes `intro` / `shot` / `recap` / `outro`. Pour un `shot` :
   `snap`, `step` (ou None = « Bon à savoir »), `kind: "result"`, `caption` (HTML avec `<b>`), `focus`, `focus2`,
   `focus_pad [haut, gauche, hautMin, largeurMin]`, `zoom` (plafonné automatiquement à la taille de l'élément),
   `click` / `click_sel`, `voice`. Vérifier les sélecteurs : `python3 check_rects.py specs/tNN.py`.
4. **Voix** : les phrases des scènes jointes par `<break time="1.3s" />`, une seule génération via la fonction
   `generate-voiceover` (voir `atelier/README.md`) → `voix/tutos/<slug>.mp3`.
5. **Montage** : `python3 tuto_video.py specs/tNN.py ../../voix/tutos/<slug>.mp3` → `build/<slug>.mp4`
   (découpage sur les silences, zoom caméra, anneau, curseur, musique `mixer.sh` à 0.18).
   Les captures modifiées sont re-rendues automatiquement (comparaison des dates).
6. **Contrôle** : une image par scène (planche contact) — texte lisible, cadrage, aucune donnée sensible, affirmations vraies.
7. **YouTube** : `python3 youtube_meta.py specs/tNN.py` → titre + description avec chapitres (≥ 10 s chacun).
   Metricool : `youtubeData` = `{"type":"video","privacy":"unlisted","madeForKids":false,"isAiGeneratedContent":true,"category":"HOWTO_STYLE"}`.
8. **App** : ajouter le lien YouTube dans la table `tutorials` (title, description, youtube_url, category, sort_order, is_published).

## Règles

Vouvoiement, aucun prix GuidPilot, mentions « Compte de démonstration » et « Voix off générée par IA » à l'écran et
en description. Ne jamais promettre une fonction qui n'existe pas (vérifier dans la base ou l'app avant d'écrire la voix).
