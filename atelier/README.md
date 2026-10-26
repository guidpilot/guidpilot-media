# Atelier GuidPilot — production hebdomadaire Instagram

Ce dossier contient tout ce qu'il faut pour produire, dans une session neuve, le lot de la semaine.

## ⭐⭐⭐ CTA DE MI-VIDÉO — décision de Normane du 26/10/2026 (PRIORITAIRE)

Constat : le CTA n'était qu'à la fin des vidéos, alors que la majorité des gens décrochent avant.
- **Une seule action demandée, montrée deux fois** : un bandeau discret vers **35-40 % de la vidéo**, puis l'écran de fin habituel.
- Le bandeau arrive **après une première info utile**, jamais pendant l'accroche ni pendant l'écran de fin. Il reste ~3,5 s, **à l'écran seulement** (la voix n'est pas coupée), en zone sûre (y 1360 → 1490, x 60 → 930).
- Texte = la même action que la fin : Reel Instagram promo → « 💬 Commentez GUIDANCE / THÉRAPEUTE » ; conseil et TikTok → « 🔖 Enregistrez-la pour plus tard » ; vidéo dont la fin est l'offre → « 👉 14 jours gratuits · lien en bio ».
- **Automatique** dans `reels/gen_v2.py`, `gen_tiktok_v3.py`, `gen_conseils.py` (donc `gen_promos.py`) et `gen_manychat.py`, via `reels/mid_cta.py`. Désactiver : `"mid_cta": False` dans la spec ; texte forcé : `"mid_cta": "…"`. Le générateur affiche dans la console l'heure et le texte du bandeau : le vérifier.
- **YouTube long** : CTA oral vers 25-35 % (abonnement + lien en description pour l'essai), après le premier conseil utile, puis l'écran de fin.
- **Mesure** : sur 2 semaines, comparer dans Metricool les commentaires avec mot-clé, les enregistrements et la rétention, avant/après le 26/10/2026.

## ⭐⭐ STYLE ET ACCROCHE — décisions de Normane du 21, 22 et 25/10/2026 (PRIORITAIRE, s'ajoute à la V2)

- **Aucune personne représentée** (21/10/2026) : ni dessin, ni photo, ni image IA, ni banque d'images. Les scènes se racontent par le texte animé, des éléments d'interface (téléphone, notifications, bulles, agenda, factures) et les vraies captures du compte de démonstration.
- **Aucun superlatif** (22/10/2026) : jamais « le seul », « le meilleur », « n°1 ». Formule : « un outil conçu pour les praticiens en guidance et les thérapeutes ».
- **Varier les styles** (25/10/2026 — « on a l'impression que c'est toujours pareil ») : jamais deux fois le même gabarit d'affilée sur un même réseau ; sur une semaine, au moins 3 gabarits visuels différents et 4 formats différents. Gabarits : **V2** (`reels/gen_v2.py`, `gen_promos.py`, `gen_tiktok_demos.py` : marine/clair + cartes + captures) et **V3** (`reels/gen_tiktok_v3.py` : fonds unis qui changent à chaque plan crème/or/marine/bleu, texte géant mot par mot surligné or, barre de progression façon story, téléphone + notifications, grande liste numérotée, tuiles, cadenas, fin sur une question). V3 marche aussi pour les Reels Instagram (ajouter la fin « Commentez MOT-CLÉ » / « Enregistrez-la » selon la V2). Créer de nouveaux gabarits est encouragé (charte GuidPilot, aucune personne).
- **Accroche en boucle ouverte** (25/10/2026 — « au début, un hook qui donne envie de voir le reste ») : la 1re image et la 1re phrase posent une question ou une promesse que seule la suite résout (« Votre cliente a oublié son rendez-vous. Et ce n'est pas elle, le problème. » ; « Séance en visio : 3 messages que vous n'écrivez plus. » ; « Ce que voit votre cliente quand elle se connecte… le dernier point va vous rassurer. » ; « « Je vous fais le virement ce soir. » Vous connaissez la suite. »). 5 à 10 mots en très gros, la voix commence par cette phrase, relances en cours de vidéo (« Deux… », « Et le dernier… »).
- Skill de référence : `guidpilot-communication` (mis à jour le 25/10/2026 avec ces règles).

## ⭐ LIGNE ÉDITORIALE V2 — en vigueur depuis le 15/10/2026 (PRIORITAIRE sur tout le reste de ce fichier)

Décidée avec Normane le 15/10/2026 après analyse Metricool : ~22 abonnés, portée moyenne 9 personnes par Reel et 5 par post, 2 à 10 s de visionnage moyen, 0 partage et 0 enregistrement, 4 à 5 posts par jour dont des doublons. Diagnostic : trop de volume, trop de pub, accroches trop lentes, contenus répétés. **Moins, mieux, plus utile.**

### ⏱️ RYTHME EN VIGUEUR — décision de Normane du 17/10/2026 (PRIORITAIRE sur le planning « 1 post par jour à 12h30 » ci-dessous)
- **2 posts Instagram par jour, 7 jours sur 7**, aux 2 meilleurs créneaux Metricool (getBestTimeToPostByNetwork instagram, revérifié à chaque lot) : **10h00 et 18h00** (Europe/Paris). Si les 2 meilleurs créneaux non adjacents (≥ 5 h d'écart) changent, utiliser les nouveaux et le dire dans le récapitulatif.
- Public du jour : **guidance lun/mer/ven/dim, thérapeutes mar/jeu/sam** (les 2 posts du jour visent le même public, sur 2 sujets différents).
- **10h00 = CARROUSEL 8–10 slides** : CONSEIL du lundi au samedi sauf jeudi ; **jeudi et dimanche = carrousel PROMO douce** (problème réel → vraie fonction en 3–4 slides avec captures du compte de démonstration → bénéfice → « Commentez GUIDANCE/THÉRAPEUTE »).
- **18h00 = REEL 15–30 s → Instagram + YouTube Short** (même post Metricool) : lun CONSEIL, mar CONSEIL, **mer PROMO**, jeu CONSEIL, ven CONSEIL, **sam PROMO**, dim CONSEIL. → 14 posts/semaine (9 conseils + 5 promos), jamais plus de 2 posts par jour (stories non comptées).
- Publication sans validation (`draft: false`, `autoPublish: true`) ; un contenu qui échoue au contrôle final reste en `draft: true` et est signalé. Anti-double lancement : verrou `atelier/lots/AAAA-MM-JJ.lock` (date du lundi) créé et poussé avant toute production.
- **Prononciation (Normane, 16/10/2026)** : dans le TEXTE envoyé à generate-voiceover, écrire « Guide Pilote » (et « guide pilote point F R » pour le site) ; à l'écran, garder « GuidPilot » / « guidpilot.fr ».
- Générateurs de la semaine du 19/10 : Reels `reels/gen_v2.py <clé> <voix.wav>` (il importe désormais `gen_promos.py` → scènes `shot` / `phone` / `myth` utilisables dans les Reels V2 ; option `"size"` sur `hook2` pour les accroches longues) ; carrousels `carrousels/gen_semaine_2026-10-19.py` (ajoute `shot()` = capture recadrée « Compte de démonstration », `prob()` = slide « Le problème / Étape », `last_promo()` = dernière slide PROMO).

### 🎨 VARIÉTÉ ET LIEN AVEC GUIDPILOT — décision de Normane du 18/10/2026 (PRIORITAIRE)
Normane : « attention à ne pas toujours faire le même type de message, changer les thématiques, des contextes différents, des conseils pertinents et liés à GuidPilot ». Constat sur la semaine du 19/10 : 4 Reels conseil sur 5 et 4 carrousels conseil sur 5 en « liste 1-2-3 », légendes qui commencent presque toutes par « Tarologue, voyante… : », conseils sans lien avec l'outil.
- **Structures** : par semaine, au moins 5 structures différentes pour les 7 Reels et 5 pour les 7 carrousels ; jamais la même structure 2 jours de suite dans un même format ; « liste numérotée 1-2-3 » au maximum 3 fois par semaine, Reels et carrousels confondus.
  - Reels : mini-histoire / scène vécue (bulles de conversation `chat`), avant / après (`vs`), mythe / réalité (`myth`), erreur à éviter + bonne pratique (`bad`), question de cliente → réponse, démonstration à l'écran (`shot`), chiffre ou calcul concret, « ce qu'elle dit / ce qu'elle pense », checklist express, coulisses, face caméra de Normane quand il en tourne un.
  - Carrousels : messages prêts à copier, mythe / réalité, avant / après, cas d'exemple (clairement présenté comme fictif), checklist, erreurs à éviter, mini-guide pas à pas, « ce que vos clientes pensent sans le dire », FAQ, modèle à remplir, comparatif.
- **Accroches** : faire tourner situation vécue, question, erreur, chiffre, contre-pied, citation de cliente, « Et si… » ; 2 fois maximum le même type par semaine. Les légendes ne commencent pas toutes par la liste des métiers : varier (citation, question, chiffre, situation) en gardant le mot-clé de niche dans la 1re ligne.
- **Thématiques** : au moins 5 piliers différents par semaine parmi : attirer et trouver des clientes · relation et communication cliente · argent (tarifs, paiement, factures — prudemment) · organisation du temps et de l'agenda · posture, limites, éthique · visibilité (page, avis, réseaux) · suivi et fidélisation · outils, confidentialité des données · saison / actualité.
- **Contextes** : varier les moments (avant la réservation, premier contact, la veille, pendant, après la séance, fin de mois, fêtes, vacances, rentrée), les canaux (téléphone, messages Instagram, e-mail, cabinet, visio, salon du bien-être), les profils de clientes (nouvelle, fidèle, indécise, pressée, qui n'a pas payé, qui offre une séance) et les métiers cités (tarologue, voyante, médium, astrologue, numérologue, cartomancienne, énergéticienne ; sophrologue, hypnothérapeute, praticienne Reiki, réflexologue, magnétiseuse, coach de vie, thérapeute holistique).
- **Conseils pertinents ET liés à GuidPilot** : chaque CONSEIL répond à un vrai problème du quotidien et se relie naturellement à une vraie fonction : une slide (carrousel, juste avant le récap) ou une scène courte (Reel, juste avant la fin) « Dans GuidPilot : … » qui montre en une phrase, avec capture démo si possible, comment l'outil facilite ce conseil — ton informatif, pas publicitaire — et une phrase « Dans GuidPilot, … » dans la légende avant la ligne « Besoin d'un outil… ». Choisir des sujets où ce lien est réel ; jamais de fonction inventée.
- **Contrôle** : le plan de la semaine indique pour chaque post structure · type d'accroche · pilier · contexte · fonction GuidPilot reliée, et ces règles sont vérifiées avant de produire.

### 📱 Stories (décision de Normane du 16/10/2026, horaires du 17/10/2026)
- **13 stories/semaine** : **12h30** (pause de midi, choix de Normane le 18/10/2026 — avant : 8h30) et 20h00 du lundi au samedi, 12h30 le dimanche. Image fixe 1080×1920 (JPG), une idée, texte très gros, **rien d'important dans les 250 px du haut ni les 340 px du bas**, logo officiel petit en bas de la zone sûre. Story vidéo seulement avec voix off Claire + badge IA.
- **20h00 = teaser du Reel de 18h00** (« Nouveau Reel sur le profil 👆 ») ; si le Reel est en brouillon, teaser du carrousel de 10h.
- **12h30 (tous les jours)** : rotation sans répéter le même type deux jours de suite — (a) mot-clé ManyChat **GUIDANCE / THÉRAPEUTE** (2–3/semaine ; jamais « GuidPilot » comme mot-clé de story), (b) conseil express, (c) question ouverte « Répondez à cette story », (d) vraie fonction sur capture démo, (e) jusqu'au 26/10/2026 : 2 rappels concours max + mention « Ce jeu n'est ni organisé, ni parrainé, ni géré par Instagram ».
- Interdit en publication automatique : stickers sondage / quiz / question / lien / musique / mention ; jamais « votez », « cliquez sur le lien », « swipe up ».
- Générateur : `python3 stories/gen_stories.py stories/specs_AAAA-MM-JJ.py <dossier_semaine>/stories` (types `keyword`, `teaser`, `tip`, `question`, `feature`, `concours` ; `[mot]` = mis en valeur ; contrôle automatique de la zone sûre 250 → 1580 affiché « OK » / « HORS ZONE »). Exemple : `stories/specs_2026-10-19.py`.
- Metricool : un post par story, `providers [{"network":"instagram"}]`, `instagramData {"type":"STORY","isAiGenerated":false}` (true si voix IA), **aucun champ text**, media = URL jsDelivr au SHA, `draft: false`, `autoPublish: true`.

### Thèmes traités — semaine du 19 au 25/10/2026 (ne pas reprendre tels quels)
- Carrousels : ce que vos clientes pensent sans le dire (guidance) ; proposer un suivi en plusieurs séances sans forcer (thérapeutes) ; fêtes de fin d'année, 6 choses à préparer (guidance) ; PROMO réservation pendant la séance, parcours page → créneau → agenda → facture (thérapeutes) ; « Juste une petite question… » (guidance, validé) ; semaine type de cabinet en 5 blocs (thérapeutes) ; PROMO page praticienne / lien en bio (guidance).
- Reels : 3 phrases qui font fuir vos clientes (validé, liste) ; séance d'1 h = presque 2 h, calcul (thérapeutes, elan) ; PROMO « Vous pouvez me renvoyer ma guidance ? » module Guidances (lofi) ; premier appel « se renseigner », conversation en bulles (thérapeutes, cocon) ; « elle revient chaque semaine », mythe/réalité (aube) ; concours « Plus que 2 jours » (pilote) ; 3 signes pour augmenter ses tarifs, liste + tableau de bord (lofi).
- Carrousels révisés le 18/10 au soir : lundi « ce qu'elle pense / ce que vous pouvez dire », mardi « au lieu de / plutôt », mercredi checklist à cocher (5 points), samedi modèle de semaine en couleurs ; chaque conseil a sa slide « DANS GUIDPILOT ».
- Stories : mot-clé GUIDANCE ×2, THÉRAPEUTE ×1, rappel la veille, concours « Plus que 5 jours », question « mal à l'aise », fonction « votre journée d'un coup d'œil », 6 teasers.

### Planning (remplace 10h / 13h / 15h / 18h) — ⚠️ remplacé par le RYTHME du 17/10 ci-dessus
| Jour | Public | Heure | Format | Type |
|---|---|---|---|---|
| Lundi | guidance | 12h30 | Reel (+ Short YouTube) | CONSEIL |
| Mardi | thérapeutes | 12h30 | Carrousel 8–10 slides | CONSEIL |
| Mercredi | guidance | 12h30 | Reel (+ Short) | PROMO douce (démo d'une vraie fonction) |
| Jeudi | thérapeutes | 12h30 | Reel (+ Short) | CONSEIL |
| Vendredi | guidance | 12h30 | Carrousel 8–10 slides | CONSEIL |
| Samedi | thérapeutes | 12h30 | Reel (+ Short) | PROMO douce |
| Dimanche | — | — | pas de post (repos, stories seulement) | — |

- **6 posts par semaine, 1 par jour maximum, 4 conseils pour 2 promos, en alternance.** Jamais deux posts le même jour (sauf rappel de jeu-concours explicitement prévu).
- YouTube longue : **2 par semaine** (mardi thérapeutes, vendredi guidance, 18h30), plus soignées.
- **Interdit de republier** un contenu déjà publié (même vidéo, même carrousel ou même légende) : Instagram pénalise les doublons. Vérifier dans Metricool les 30 derniers jours avant de programmer.
- Pendant un jeu-concours : le créneau PROMO du mercredi ou du samedi peut devenir un rappel concours ; jamais un post de plus par jour.

### Style des Reels (remplace « 25–40 s »)
- **15 à 30 secondes.** Une seule idée par Reel.
- **La première seconde décide de tout** : pas de logo, pas d'intro, pas de titre de marque. Image 1 = une phrase-choc en très gros (5 à 8 mots) ET la voix commence directement par cette phrase. Formules qui marchent : situation vécue (« Elle annule 10 minutes avant. Encore. »), question qui pique (« Vous annoncez votre prix… et vous baissez les yeux ? »), erreur (« L'erreur qui fait fuir vos clientes »), chiffre concret (« 3 messages à ne plus jamais envoyer »), contre-pied (« Arrêtez de répondre à 23 h »).
- Rythme : un changement visuel toutes les 1,5 à 2 s, sous-titres gros et centrés dans la zone sûre, phrases courtes à l'oral.
- Fin courte (2 s max) : sur un CONSEIL → « Enregistrez-le pour plus tard » + question ; sur une PROMO → « Commentez GUIDANCE / THÉRAPEUTE » (Instagram) / « guidpilot.fr » (Short). Plus de grand écran final logo + offre sur les conseils.
- Badge « Voix off générée par IA » toujours présent, discret (petit, en haut), et `isAiGenerated` / `isAiGeneratedContent` toujours à true.
- Les PROMOS restent utiles : on part d'un problème réel, on montre la vraie fonction en 2–3 plans, on finit sur le bénéfice. Pas de liste de fonctions.

### Carrousels
- 8 à 10 slides, format 1080×1350. Slide 1 = accroche forte (promesse claire ou erreur) ; slide 2 = second hook (« La 3 est la plus oubliée ») ; 1 idée par slide ; avant-dernière = récapitulatif à enregistrer ; dernière = question + « Enregistrez ce post ». GuidPilot : une seule mention discrète sur la dernière slide.
- Formats à faire tourner : messages prêts à copier, erreurs à éviter, checklist, mythe / réalité, avant / après, « ce que vos clientes pensent sans le dire », mini-guide pas à pas.

### Légendes (remplace la section « Légendes Instagram »)
- Ligne 1 = l'accroche (≤ 125 caractères, avec le mot-clé de la niche). Puis 3 à 5 lignes utiles. Puis une question simple.
- **CONSEIL** : pas de bloc publicitaire. Terminer par la question + « Enregistrez ce post pour plus tard » + UNE ligne discrète : « Besoin d'un outil pour tout ça ? Commentez GUIDANCE (ou THÉRAPEUTE). »
- **PROMO** : bloc ManyChat complet (« 📩 Commentez GUIDANCE et recevez en message privé la présentation de GuidPilot : 14 jours gratuits, sans carte bancaire. » + « 👉 Ou lien en bio : guidpilot.fr »).
- **3 à 5 hashtags** de niche (plus 8–10).

### Boucle d'amélioration (chaque dimanche)
Avant de produire la semaine, lire les statistiques Metricool des 14 derniers jours (Reels : vues, portée, temps moyen, taux de vue > 3 s, partages, enregistrements ; posts : portée, enregistrements). Noter dans le dossier de la semaine (`bilan.md`) les 2 meilleurs et les 2 moins bons contenus, et refaire les formats / types d'accroche qui ont le mieux marché.

### Générateurs V2
- Reels : `reels/gen_v2.py <clé> <voix.wav>` (scènes `hook2` = phrase-choc lisible dès la frame 0, `save` = fin courte « Enregistrez-la » ou `kw` « Commentez MOT-CLÉ », + scènes de `gen_conseils.py`). Exemple validable : `test-3-phrases` (25 s).
- Carrousels : `carrousels/gen_v2_test.py` (couverture sans logo, second hook, récap à enregistrer, question finale). Modèle à copier pour chaque semaine.

### Contenu incarné (optionnel, proposé à Normane)
Chaque semaine, proposer dans le récapitulatif **1 script de Reel de 20 s à tourner face caméra par Normane** (téléphone, lumière naturelle), avec l'accroche, 3 phrases et la fin. Les comptes qui montrent un vrai visage sont mieux diffusés que les vidéos 100 % animées.

---

## Règles de marque (non négociables)

- Vouvoiement. Ton : simple, rassurant, professionnel, premium accessible. Pas d'ésotérisme excessif.
- Cible : tarologues, médiums, voyantes, cartomanciennes, praticiennes en guidance, énergéticiennes, praticiennes bien-être (France).
- **Thérapeutes (ajouté par Normane le 12/10/2026)** : produire aussi des contenus pour les thérapeutes du bien-être et de l'accompagnement — sophrologues, hypnothérapeutes, praticiennes Reiki, magnétiseuses, énergéticiennes, réflexologues, thérapeutes holistiques, coachs de vie. **Règle en vigueur depuis le 13/10/2026 (Normane) : DEUX VERSIONS, EN ALTERNANCE PAR JOUR.** Chaque journée s'adresse à UN seul public, avec son vocabulaire, ses exemples, ses mots-clés et ses hashtags : **lundi, mercredi, vendredi, dimanche = praticiennes en guidance** (tarologues, voyantes, médiums, énergéticiennes) ; **mardi, jeudi, samedi = thérapeutes** (sophrologues, hypnothérapeutes, praticiennes Reiki, réflexologues, magnétiseuses, thérapeutes holistiques, coachs de vie). Tous les contenus d'un même jour suivent ce public : carrousel 10h, Reel conseil 13h, Reel promo 18h (+ Shorts YouTube) et vidéo YouTube longue de 18h30. Un même sujet peut être décliné en deux versions sur deux jours différents (ex. version guidance le lundi, version thérapeutes le mardi), avec un texte réécrit — jamais une simple copie. Volume inchangé (pas de contenus supplémentaires). Contenus thérapeutes : respecter strictement les règles de vocabulaire ci-dessous (aucun terme médical). Règle du 12/10 « les deux publics dans chaque vidéo » : remplacée. Ancienne règle (remplacée) : environ 1 contenu sur 3 s'adresse spécifiquement aux thérapeutes, avec leur vocabulaire (« séance », « accompagnement », « suivi », « compte rendu de séance », « cabinet ») et des exemples de leur quotidien (séances de 1 h, suivis sur plusieurs séances, rappels de rendez-vous, compte rendu après séance, annulations de dernière minute).
  - ⚠️ Conformité renforcée : jamais « patient », « soigner », « guérir », « traiter », « traitement », « thérapie » au sens médical, « diagnostic », « consultation médicale », ni promesse d'effet sur la santé. Le contenu parle de **gestion du cabinet**, jamais des bienfaits des pratiques. Ne pas cibler les professions de santé réglementées (psychologues, kinés, etc.). Hashtags : #sophrologue #hypnotherapeute #reiki #magnetiseur #energeticienne #reflexologie #therapeuteholistique #praticienbienetre #cabinetbienetre #guidpilot.
- Couleurs : marine #0F172A, bleu #2563EB, or #E9C46A avec parcimonie, fond clair #F6F8FC. Police Inter. Logo officiel uniquement (`assets/logo_blanc.png`, `assets/logo_couleur.png`), jamais redessiné.
- Offre affichée : **« 14 jours gratuits, sans carte bancaire »**. **Aucun prix** dans les vidéos ni les visuels.
- Interdit : promesse de résultats (« +50 % de clientes »), vocabulaire médical/thérapeutique, faux avis ou faux témoignages, fonction inventée. Les captures d'écran viennent du compte de démonstration et portent la mention « Compte de démonstration ».
- Fonctions qu'on peut citer : page praticien publique, annuaire GuidPilot, réservation + paiement en ligne, agenda, fiches clientes, espace client sécurisé, messagerie, guidances écrites et vocales, Google Meet, factures automatiques, demandes et relances d'avis, 0 % de commission sur les séances (hors frais du moyen de paiement). Pas de chatbot, pas de publication automatique réseaux sociaux.
- Thèmes variés et intrigants d'une semaine à l'autre (POV, avant/après, erreurs à éviter, mythes, coulisses d'une journée, checklist, question/réponse, « 3 choses que vos clientes regardent avant de réserver »…). Ne pas réutiliser un thème des semaines précédentes (regarder les dossiers `AAAA-MM-JJ_au_JJ/` existants).

## Règles vidéo (Reels)

- 1080×1920, **15–30 s (ligne V2)**, dynamique (captures qui défilent, textes qui arrivent en rythme avec la voix).
- **Voix off obligatoire** : voix **ElevenLabs « Claire »** (choisie par Normane le 08/10/2026), générée automatiquement (voir plus bas). Aucune voix Google, même en secours.
- **Musique de fond ORIGINALE, audible mais sous la voix** (validé par Normane le 09/10/2026) : après le rendu HyperFrames, remplacer l'audio avec `musique/mixer.sh <video.mp4> <voix.wav> <preset> <sortie.mp4>` (musique composée par `musique/compose.py`, donc sans droits d'auteur ; volume 0.32 + baisse automatique quand la voix parle). Presets : `lofi`, `aube`, `elan`, `cocon`, `pilote` — **varier d'une vidéo à l'autre** (`elan`/`pilote` pour les Reels dynamiques, `aube`/`cocon` pour les sujets calmes, `lofi` polyvalent). Ne jamais utiliser de musique trouvée en ligne. Voix normalisée : `ffmpeg -i in.wav -af "loudnorm=I=-15:TP=-1.5:LRA=11" -ar 48000 -ac 2 out.wav`.
- **Mention à l'écran « Voix off générée par IA »** (badge `.aibadge` en haut à gauche, `top:64px`, ne doit chevaucher aucun titre).
- Écran final : logo + « 14 jours gratuits » + « ✓ Sans carte bancaire » + « Lien en bio · guidpilot.fr ».
- Dans Metricool : `instagramData.isAiGenerated = true` pour chaque Reel.

## Légendes Instagram

Chaque légende contient : une accroche avec mots-clés de la niche (1re ligne), le bénéfice concret (liste ✔), l'appel à l'action
`Testez GuidPilot gratuitement pendant 14 jours, sans carte bancaire.\n👉 Lien en bio : guidpilot.fr`, une question pour les commentaires,
puis **3 à 5 hashtags (ligne V2 — remplace « 8 à 10 »)** ciblés (voir `posts_semaine.py`, jeux `H_GUIDANCE` et `H_BIENETRE`, à faire tourner/varier).

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
# 25/10/2026 : si le chemin ci-dessus est vide, utiliser /opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell (ne pas lancer « hyperframes browser ensure » : téléchargement bloqué).
```
Rendu : `cd build/<nom> && npx hyperframes lint && npx hyperframes render --output ../<nom>.mp4` (vérifier avec `npx hyperframes snapshot` + regarder les images).

## Voix off automatique (ElevenLabs « Claire » UNIQUEMENT)

Le shell ne peut pas joindre ElevenLabs ni Google : on passe par la fonction Supabase **generate-voiceover** (projet `tcxhdtleencjqdphtgqu`),
qui génère la voix et la dépose directement dans `voix/<nom>.mp3` de ce dépôt.
- ⚠️ **Décision de Normane (10/10/2026) : ElevenLabs uniquement, jamais la voix Google.** La fonction (v5, source `atelier/outils/generate-voiceover/index.ts`) n'a plus de secours automatique : si ElevenLabs échoue, elle renvoie `tts_failed`. Dans ce cas, ne pas utiliser Google : réessayer une fois plus tard, sinon prévenir Normane.

- **Prononciation de la marque (Normane, 16/10/2026)** : on doit entendre « Guide Pilote » (guide comme « un guide », pilote à la française), jamais « Gouid-pilot ». La fonction generate-voiceover remplace automatiquement « GuidPilot » par « Guide Pilote » et « guidpilot.fr » par « Guide Pilote point F R » dans le texte lu (l'écran garde l'orthographe officielle « GuidPilot »). Écrire les scripts normalement ; à chaque contrôle final, vérifier à l'écoute que la marque est bien prononcée. Test de référence validé par Normane : `voix/tests/2026-10-16_prononciation-guide-pilote.mp3`.
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

- Marque `blogId` **7232477**, fuseau `Europe/Paris`. Réseaux : `instagram` pour tout ; **chaque Reel est AUSSI publié en YouTube Short** (même post, `providers` = instagram + youtube). TikTok = lives, rien à programmer. **Facebook (page « GuidPilot », connectée par Normane le 20/10/2026)** : provider `facebook`, `facebookData {"type":"POST"}` (ou `REEL`) ; 1er post publié le 20/10 à 17h43 = démo 01 (`youtube/demos/demo-01-logiciel-tarologue-voyante.mp4`) + texte de présentation guidance + thérapeutes, lien https://guidpilot.fr cliquable.
- **FACEBOOK — décision de Normane du 20/10/2026 : 2 posts par jour sur la page, 9h30 et 12h45** (Europe/Paris). On reprend les contenus existants (carrousels sans la dernière slide « Commentez … » propre à ManyChat Instagram, Reels finissant par « Enregistrez-la » en `facebookData.type REEL`, vidéos YouTube/démos 16:9 en `POST` avec `title`). Uniquement des vidéos dont la voix date du 16/10/2026 ou après (prononciation « Guide Pilote »). **Chaque texte cite les DEUX publics** (thérapeutes : Reiki, LaHoChi, sophrologie, hypnose… ET tarologues, voyantes, médiums) et **l'essai « 14 jours gratuits, sans carte bancaire »** avec https://guidpilot.fr. Pas de mot-clé ManyChat. **+ Reel de 18h00 aussi sur Facebook** (Normane, 20/10/2026) : post Facebook séparé (`facebookData.type REEL`, même vidéo, texte adapté aux deux publics + 14 jours), sauf Reel qui finit par « Commentez MOT-CLÉ » à l'écran ou jeu-concours Instagram. Toute vidéo avec voix IA : ligne « 🤖 Contenu créé avec l'IA : voix off générée par IA. » dans le texte (Metricool n'a pas de case « contenu IA » pour Facebook). Semaine du 21 au 25/10 programmée le 20/10 : pensent sans dire, démo 02, suivi sans forcer, Reel 3 phrases, fin d'année, Reel séance 1 h, réservation en séance, vidéo YouTube suivi plusieurs séances, Reel premier appel, « petite question ».
- YouTube Short : `youtubeData` = `{"title": "<accroche mots-clés, ≤ 90 caractères> #shorts", "type": "short", "privacy": "public", "madeForKids": false, "isAiGeneratedContent": true, "category": "HOWTO_STYLE", "tags": [6–8 mots-clés de niche]}`. Titre orienté recherche (ex. « Logiciel pour tarologue : … »). Le lien n'est pas cliquable dans un Short : « guidpilot.fr » doit rester visible sur l'écran de fin.
- **Depuis le 15/10/2026 (décision de Normane) : publication SANS validation** → `createScheduledPost` avec `draft: false`, `autoPublish: true`. Seul un post qui échoue au contrôle final reste en `draft: true` (et est signalé). Normane peut répondre « Stop » pour bloquer un post (repasser en brouillon). Reels : `instagramData.type = "REEL"`, `isAiGenerated: true`, `videoCoverMilliseconds` sur une image lisible. Carrousels : `type "POST"`, 7 médias.
- Erreur « Failed to normalize media » : passagère, réessayer.
- Avant de programmer, `getScheduledPosts` sur la semaine pour éviter les doublons de créneaux.

## Contrôle final (obligatoire)

Pour chaque Reel : regarder 4–6 images du rendu (badge IA lisible et sans chevauchement, aucun prix, texte sans faute), vérifier que la voix est audible et la musique quasi inaudible. Pour chaque carrousel : regarder chaque slide. Relire chaque légende (vouvoiement, lien, hashtags, pas de promesse). Puis vérifier dans `getScheduledPosts` que les 14 posts sont bien présents aux bons créneaux.

## Vidéos YouTube longues (2 par semaine depuis le 15/10/2026 : mardi thérapeutes, vendredi guidance)

- Format **1920×1080**, 1 min 30 à 3 min, voix Claire, musique originale via `musique/mixer.sh` (même règle que les Reels), badge « Voix off générée par IA », mention « Compte de démonstration » sur les captures.
- ⚠️ **Variété obligatoire (Normane, 10/10/2026)** : lire la section « Consignes de variété » de `youtube/prochains-sujets.md` avant chaque vidéo (mises en scène différentes, images illustrées liées au contexte, ne plus centrer sur l'agenda / la prise de rendez-vous, vouvoiement uniquement, jamais de tutoiement).
- Modèle : `youtube/gen_presentation.py` (sections numérotées : titre à gauche, capture à droite ; intro marine ; fin marine avec « 14 jours gratuits · Sans carte bancaire · guidpilot.fr » + bouton « Abonnez-vous : 2 vidéos par semaine »). Copier/adapter par sujet, caler les temps sur la voix (`silencedetect`, puis estimation par longueur de texte par paragraphe). Ne pas faire défiler une capture au-delà de ses bords (zone vide).
- Script : 230–420 mots, vouvoiement, un sujet utile au quotidien d'une praticienne (éduquer 35 %, montrer 25 %, raconter 20 %, prouver 10 %, convertir 10 %), fin = invitation à tester + à **s'abonner**.
- Miniature 1280×720 (fond marine, accroche 3–6 mots en très gros, capture inclinée, logo blanc) → `videoThumbnailUrl`.
- Metricool : provider `youtube`, `youtubeData.type = "video"`, titre ≤ 100 caractères **commençant par la requête recherchée par la niche** (« Logiciel pour tarologue… », « Comment trouver des clients en voyance… »), 12–16 tags, `madeForKids false`, `isAiGeneratedContent true`, `category HOWTO_STYLE`. Description : 2 phrases riches en mots-clés, lien https://guidpilot.fr, appel à s'abonner, **chapitres horodatés (0:00 obligatoire, ≥ 3 chapitres de ≥ 10 s)**, paragraphe de mots-clés naturels, mentions « Captures réalisées sur un compte de démonstration. Voix off générée par IA. », 3–5 hashtags.
- Fichiers : `youtube/AAAA-MM-JJ_<sujet>.mp4` et `_miniature.jpg`. Publication 18h30, en brouillon jusqu'au « Go » de Normane.
- Sujets déjà traités : 2026-10-08 présentation générale de GuidPilot — tuto/promo ; 2026-10-09 comparatif Calendly / WhatsApp / agenda + histoire de GuidPilot (créé par Normane pour sa compagne praticienne en guidance — sans la nommer) — tuto/promo ; 2026-10-10 Instagram, TikTok, Google Meet et l'annuaire : de la bio à la réservation (`gen_visibilite.py`, musique `aube`) — tuto/promo. ; 2026-10-11 Relancer une cliente sans paraître insistante : paiement en attente, avis, nouvelle séance (`gen_relancer.py`, musique `cocon`, scènes : téléphone à notifications, citation, frise, avant/après, liste à cocher, conversation, illustration du bouton de rappel) — conseil. Version verticale 1080×1920 (`_vertical.mp4`, rendu `gen_relancer.py <voix> social` avec fin « Lien en bio », puis vidéo 16:9 posée sur fond marine avec titre et mention IA lisible) demandée par Normane pour TikTok (11/10 20h30) et Instagram Reel (12/10 12h30). ; 2026-10-12 Le tableau de bord GuidPilot : où en est votre activité en 30 secondes (`gen_tableau_de_bord.py`, musique `lofi`, scènes : bureau du matin illustré, gros plans zoomés avec cercle sur `dash.png`, chiffre animé « À encaisser », clic curseur, liste à cocher, fiche cliente illustrée en frise, chronomètre + routine cochée, citation) — tuto/promo. ; 2026-10-13 Sophrologue, hypnothérapeute, praticienne Reiki : 5 tâches administratives à ne plus faire le soir (rendez-vous, paiements, factures, notes de séance, annulations ; `gen_therapeutes_soir.py`, musique `cocon`, scènes : bureau du soir illustré 21 h, titre à 5 cartes, téléphone à bulles puis grille de créneaux, relevé de règlements à cocher, pile de factures numérotées + tampon, notes éparpillées rangées dans une fiche cliente, frise des annulations + règle écrite, liste GuidPilot qui s'allume avec visuels dont `finance.png` zoomé, citation) — conseil, public thérapeutes. ; 2026-10-14 Fidéliser ses clientes en guidance : 5 habitudes pour qu'elles reviennent (suivi du lendemain, guidance rangée au même endroit, historique et notes privées, proposer une suite sans forcer, demander son avis ; `gen_fideliser_guidance.py`, musique `aube`, scènes : conversation téléphone + mois vides, chemin en 5 étapes, message qui s'écrit, avant/après éparpillé vs rangé, carnet de séance avec cadenas, « À éviter » barré vs « Préférez », étoiles qui se remplissent, liste GuidPilot avec espace client, fiche, `avis.png` entouré, bouton « Prendre un nouveau rendez-vous », citation) — conseil, public guidance. ; 2026-10-16 Espace client pour tarologue et voyante : ce que voit votre cliente (accès par lien e-mail, rendez-vous + Google Meet + reprise de rendez-vous, guidances écrites et vocales avec notification, messagerie privée vs WhatsApp perso, factures et règlements, ce qu'elle ne voit jamais, conseil + message prêt à copier ; `gen_espace_client_guidance.py`, musique `lofi`, scènes : téléphone « je ne retrouve plus ma guidance » + pièces éparpillées, chemin en 5 étapes, e-mail d'accès illustré, téléphone Mes rendez-vous, lecteur audio + notification, avant/après WhatsApp vs fil privé, relevé de factures, écran marine des 4 cadenas, message prêt à copier, citation, récap 3 cartes) — tuto/promo, public guidance. ; 2026-10-20 Sophrologue, hypnothérapeute, praticienne Reiki : organiser le suivi de vos clientes sur plusieurs séances (fiche par cliente, notes internes privées, compte rendu écrit ou vocal livré dans l'espace client, forfait de séances décomptées + date suivante + reprise de rendez-vous depuis l'espace, bilan de fin de cycle + demande d'avis ; `gen_suivi_therapeutes.py`, musique `cocon`, scènes : carnet papier + post-it + 3 questions, chemin en 5 étapes, fiche cliente illustrée en frise + onglets, bloc-notes « 2 minutes, 3 questions » + cadenas, écran partagé notes / compte rendu, flux écrit-vocal → rendez-vous → espace + téléphone notifié, carte forfait qui se décompte, bulles de bilan, capture `avis.png` entourée, récap 3 cartes) — tuto/promo, public thérapeutes.
- Vidéo de présentation complète (hors rotation quotidienne, demandée par Normane le 10/10/2026 pour YouTube + site) : `youtube/2026-10-10_presentation-complete-guidpilot.mp4` (3 min, `gen_presentation_complete.py`, musique `pilote`), non programmée.
- Les vidéos poussées doivent faire **moins de 20 Mo** (limite jsDelivr, sinon « Failed to normalize media ») : ré-encoder si besoin avec `ffmpeg -i in.mp4 -c:v libx264 -preset slow -crf 22 -pix_fmt yuv420p -movflags +faststart -c:a copy out.mp4`.

## Images réalistes générées par IA — EN PAUSE (décision de Normane le 10/10/2026 : « on fait sans pour l'instant »)

- **Ne pas utiliser generate-image ni aucune photo IA** tant que Normane ne l'a pas redemandé. Les images des vidéos sont des scènes dessinées en HTML/SVG dans la charte, plus les captures du compte de démonstration.


- Fonction Supabase **generate-image** (projet `tcxhdtleencjqdphtgqu`, source : `atelier/outils/generate-image/index.ts`), même appel que la voix off (`net.http_post` + `x-internal-secret`) avec `body := jsonb_build_object('path','images/<dossier>/<nom>.png','aspect','16:9','model','gemini-3.1-flash-image','prompt','<scène en anglais>')`. L'image est déposée dans `images/` du dépôt (`git pull` ensuite). `{"action":"models"}` liste les modèles disponibles.
- Style imposé par la fonction : photo réaliste éditoriale, lumière naturelle, intérieur français moderne, touches marine et or, **aucun texte, logo, étoile, cristal ou halo**. Décrire des scènes du quotidien d'une praticienne (bureau, téléphone, carnet, tasse, cliente qui lit sa guidance sur son téléphone…). Jamais de personne réelle identifiable, jamais de faux témoignage.
- ⚠️ État au 10/10/2026 : la clé Google est en offre gratuite, les modèles d'image renvoient « 429 quota exceeded ». Il faut activer la facturation du projet Google AI Studio lié à `GEMINI_API_KEY` (décision de Normane). En attendant : scènes illustrées en HTML/SVG.
- À l'écran : mention « Images générées par IA » à côté du badge voix (ou badge unique « Voix et images générées par IA ») ; dans Metricool, `isAiGeneratedContent: true` (déjà le cas).

## Reels CONSEILS (ancien créneau 13h00 — remplacé par le planning V2 à 12h30)

- Générateur : `reels/gen_conseils.py <clé> <voix.wav>` + textes/scènes dans `reels/conseils_specs.py` (scènes hook / étape numérotée / erreur à éviter / avant-après / bulles / liste / citation / logo ; calage automatique sur la voix). Médias : `AAAA-MM-JJ_au_JJ/conseils/`.
- Thèmes déjà traités (semaine du 12 au 18/10/2026) : annoncer ses tarifs sans gêne ; annulations et retards ; limites avec une cliente qui écrit à toute heure ; trouver ses premières clientes ; présenter ses prestations clairement ; livrer une guidance de façon professionnelle ; 4 garde-fous contre l'épuisement.

## Reels PROMO (ancien 18h00) et carrousels CONSEIL (ancien 10h00) — remplacés par le planning V2 à 12h30

- ~~Ligne éditoriale (Normane, 11/10/2026) : chaque jour 2 contenus conseils + 1 promo~~ → remplacée le 15/10/2026 par la ligne V2 (6 posts/semaine).
- Générateur promo : `reels/gen_promos.py <clé> <voix.wav>` + textes/scènes dans `reels/promos_specs.py` (réutilise `gen_conseils.py`, ajoute les scènes `shot` = capture démo avec panoramique, `phone` = téléphone dessiné « Illustration », `myth` = idée reçue / FAUX, extras `button` et `audio`). Captures sans montants : `kit/assets/dash_np.png`, `page_np.png` (prix floutés).
- Carrousels de la semaine : `carrousels/gen_semaine_AAAA-MM-JJ.py` (réutilise `gen_carrousels.py`, insécables automatiques avant « : ? ! » »). Légendes, titres YouTube et payloads Metricool : `posts_AAAA-MM-JJ.py <SHA>`.
- Semaine du 12 au 18/10/2026 — carrousels conseil : bio Instagram (5 éléments) ; checklist des 10 minutes avant une séance ; 5 messages prêts à copier pour vos clientes ; visio aussi chaleureuse qu'en cabinet ; notes de séance (quoi écrire / éviter) ; 5 chiffres à regarder chaque mois ; routine du dimanche (préparer sa semaine en 15 min).
- Semaine du 12 au 18/10/2026 — Reels promo : tableau de bord en 30 s (aube) ; rappel de paiement en un clic (lofi) ; le chemin d'un avis client (elan) ; annuaire GuidPilot / être trouvée (pilote) ; espace client vu par la cliente (cocon) ; factures automatiques (lofi) ; 4 idées reçues vrai/faux (elan).
