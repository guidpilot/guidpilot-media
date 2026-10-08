# Atelier GuidPilot — production hebdomadaire Instagram

Ce dossier contient tout ce qu'il faut pour produire, dans une session neuve, le lot de la semaine :
**14 posts Instagram (2 par jour, 10h et 18h, du lundi au dimanche)**, soit 7 Reels vidéo avec voix off et 7 carrousels.

## Règles de marque (non négociables)

- Vouvoiement. Ton : simple, rassurant, professionnel, premium accessible. Pas d'ésotérisme excessif.
- Cible : tarologues, médiums, voyantes, cartomanciennes, praticiennes en guidance, énergéticiennes, praticiennes bien-être (France).
- Couleurs : marine #0F172A, bleu #2563EB, or #E9C46A avec parcimonie, fond clair #F6F8FC. Police Inter. Logo officiel uniquement (`assets/logo_blanc.png`, `assets/logo_couleur.png`), jamais redessiné.
- Offre affichée : **« 14 jours gratuits, sans carte bancaire »**. **Aucun prix** dans les vidéos ni les visuels.
- Interdit : promesse de résultats (« +50 % de clientes »), vocabulaire médical/thérapeutique, faux avis ou faux témoignages, fonction inventée. Les captures d'écran viennent du compte de démonstration et portent la mention « Compte de démonstration ».
- Fonctions qu'on peut citer : page praticien publique, annuaire GuidPilot, réservation + paiement en ligne, agenda, fiches clientes, espace client sécurisé, messagerie, guidances écrites et vocales, Google Meet, factures automatiques, demandes et relances d'avis, 0 % de commission sur les séances (hors frais du moyen de paiement). Pas de chatbot, pas de publication automatique réseaux sociaux.
- Thèmes variés et intrigants d'une semaine à l'autre (POV, avant/après, erreurs à éviter, mythes, coulisses d'une journée, checklist, question/réponse, « 3 choses que vos clientes regardent avant de réserver »…). Ne pas réutiliser un thème des semaines précédentes (regarder les dossiers `AAAA-MM-JJ_au_JJ/` existants).

## Règles vidéo (Reels)

- 1080×1920, 25–40 s, dynamique (captures qui défilent, textes qui arrivent en rythme avec la voix).
- **Voix off obligatoire** : voix **ElevenLabs « Claire »** (choisie par Normane le 08/10/2026), générée automatiquement (voir plus bas). Secours automatique : Google Nika.
- **Musique : aucune, ou très basse** (`data-volume="0.06"` max, pad `reels/ambient30.wav`). La voix doit être parfaitement audible. Voix normalisée : `ffmpeg -i in.wav -af "loudnorm=I=-15:TP=-1.5:LRA=11" -ar 48000 -ac 2 out.wav`.
- **Mention à l'écran « Voix off générée par IA »** (badge `.aibadge` en haut à gauche, `top:64px`, ne doit chevaucher aucun titre).
- Écran final : logo + « 14 jours gratuits » + « ✓ Sans carte bancaire » + « Lien en bio · guidpilot.fr ».
- Dans Metricool : `instagramData.isAiGenerated = true` pour chaque Reel.

## Légendes Instagram

Chaque légende contient : une accroche avec mots-clés de la niche (1re ligne), le bénéfice concret (liste ✔), l'appel à l'action
`Testez GuidPilot gratuitement pendant 14 jours, sans carte bancaire.\n👉 Lien en bio : guidpilot.fr`, une question pour les commentaires,
puis 8 à 10 hashtags ciblés (voir `posts_semaine.py`, jeux `H_GUIDANCE` et `H_BIENETRE`, à faire tourner/varier).

## Outils

- `kit/` : polices, GSAP, captures (dash, page, avis, guid, annuaire, finance), logos, config HyperFrames.
- `reels/gen_reels.py` : modèle de générateur de Reels (2 exemples : POV 23 h, Avant/Après). Copier/adapter les scènes pour les nouveaux thèmes. Sortie dans `build/<nom>/`.
- `exemples/video1/index.html`, `exemples/video2/gen.py` : autres modèles de vidéos validés par Normane.
- `carrousels/gen_carrousels.py` : carrousels 1080×1350 (7 slides : couverture marine, 5 slides contenu claires, CTA marine). Ajouter les nouveaux carrousels dans le dict `C`. Sortie PNG dans `build/carrousels/` → convertir en JPG qualité 90 avant publication.
- `posts_semaine.py` : modèle de définition des posts (légende, médias, dates) et de payload Metricool.

### Installation dans une session neuve

```bash
cd /home/claude && git clone https://github.com/guidpilot/guidpilot-media.git && cd guidpilot-media/atelier
npm ci   # hyperframes, gsap
pip install playwright --break-system-packages 2>/dev/null || true
export PRODUCER_HEADLESS_SHELL_PATH=$(ls -d /opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell | head -1)
export HYPERFRAMES_BROWSER_PATH=$PRODUCER_HEADLESS_SHELL_PATH
```
Rendu : `cd build/<nom> && npx hyperframes lint && npx hyperframes render --output ../<nom>.mp4` (vérifier avec `npx hyperframes snapshot` + regarder les images).

## Voix off automatique (ElevenLabs « Claire », secours Google Nika)

Le shell ne peut pas joindre ElevenLabs ni Google : on passe par la fonction Supabase **generate-voiceover** (projet `tcxhdtleencjqdphtgqu`),
qui génère la voix et la dépose directement dans `voix/<nom>.mp3` de ce dépôt (`.wav` si le secours Google a été utilisé : le champ `path` de la réponse donne le vrai nom).

- Voix par défaut : **Claire**, `voice` = `6vTyAgAT8PncODBcLjRf`, `provider` = `elevenlabs`, modèle `eleven_multilingual_v2`. Abonnement ElevenLabs Creator (~131 000 crédits/mois ≈ 1 crédit par caractère).
- **Lancer les générations UNE PAR UNE** (attendre la réponse avant la suivante) : en parallèle, GitHub refuse les écritures simultanées (erreur 409).
- Quota restant : `body := '{"action":"subscription"}'`.

Appel via l'outil Supabase `execute_sql` :

```sql
select net.http_post(
  url := 'https://tcxhdtleencjqdphtgqu.supabase.co/functions/v1/generate-voiceover',
  headers := jsonb_build_object('Content-Type','application/json','x-internal-secret',
    (select decrypted_secret from vault.decrypted_secrets where name='internal_email_secret')),
  body := jsonb_build_object('path','voix/2026-10-13_mon-theme.mp3','text','Texte de la voix off, phrases courtes, vouvoiement.',
                           'provider','elevenlabs','voice','6vTyAgAT8PncODBcLjRf'),
  timeout_milliseconds := 120000) as id;
-- attendre ~25 s puis :
select id, status_code, content from net._http_response where id = <id>;
```
Puis `git pull` pour récupérer le fichier (convertir en wav pour le montage : `ffmpeg -i voix.mp3 -af loudnorm=I=-15:TP=-1.5:LRA=11 -ar 48000 -ac 2 voix.wav`). Synchroniser les animations sur la voix avec
`ffmpeg -i voix.wav -af silencedetect=noise=-35dB:d=0.25 -f null -` (début de chaque phrase). Un texte de ~70 mots ≈ 20–25 s avec Claire.
Ne jamais afficher ni copier les secrets.

## Hébergement des médias

Pousser les médias dans `AAAA-MM-JJ_au_JJ/` (dossier de la semaine) puis utiliser les URL jsDelivr **avec le SHA du commit** :
`https://cdn.jsdelivr.net/gh/guidpilot/guidpilot-media@<SHA>/<dossier>/<fichier>`.
Commit : `git -c user.name="GuidPilot" -c user.email="guidpilot@gmail.com" commit`. Ce dépôt est public : uniquement des visuels marketing, jamais de données clientes.

## Programmation Metricool

- Marque `blogId` **7232477**, fuseau `Europe/Paris`, réseau `instagram` uniquement (TikTok = lives, rien à programmer).
- `createScheduledPost` avec `draft: true` (brouillon : Normane valide) sauf instruction contraire. Reels : `instagramData.type = "REEL"`, `isAiGenerated: true`, `videoCoverMilliseconds` sur une image lisible. Carrousels : `type "POST"`, 7 médias.
- Erreur « Failed to normalize media » : passagère, réessayer.
- Avant de programmer, `getScheduledPosts` sur la semaine pour éviter les doublons de créneaux.

## Contrôle final (obligatoire)

Pour chaque Reel : regarder 4–6 images du rendu (badge IA lisible et sans chevauchement, aucun prix, texte sans faute), vérifier que la voix est audible et la musique quasi inaudible. Pour chaque carrousel : regarder chaque slide. Relire chaque légende (vouvoiement, lien, hashtags, pas de promesse). Puis vérifier dans `getScheduledPosts` que les 14 posts sont bien présents aux bons créneaux.
