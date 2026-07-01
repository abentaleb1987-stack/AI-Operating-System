# AOS_PROCESS.md

## Decision operationnelle

Le workflow automatise AOS repose sur la separation suivante :

Codex execute.
GitHub synchronise.
Aion audite.

Codex execute localement l'ensemble du processus de capitalisation, y compris :

- l'analyse de la source brute ;
- la detection de l'IA, du framework ou de l'outil IA concerne ;
- le routage vers le bon dossier ;
- la creation de la fiche de veille ;
- la mise a jour ciblee de la fiche permanente ;
- le deplacement de la source brute vers le dossier traite ;
- le commit Git ;
- le push GitHub ;
- le rapport final.

GitHub synchronise et conserve l'historique des modifications.

Aion audite periodiquement le repository GitHub afin de controler :

- la qualite des fiches de veille ;
- la qualite des fiches permanentes ;
- le bon classement des connaissances ;
- la pertinence des integrations permanentes ;
- les erreurs de routage ;
- les doublons ;
- les informations marketing integrees par erreur ;
- l'efficacite du protocole Codex.

## Workflow obligatoire

Le processus obligatoire est :

```text
Source brute
-> Detection IA / outil / framework
-> Routage
-> Fiche de veille
-> Validation des connaissances
-> Mise a jour fiche permanente
-> Deplacement source traitee
-> Git add
-> Git commit
-> Git push
-> Rapport final
```

## Regle fondamentale

La fiche permanente est la source de verite durable.

Elle ne doit jamais etre reecrite entierement.

Chaque source ne doit produire que des differences ciblees, pertinentes et justifiees.

La fiche permanente ne doit pas devenir une accumulation chronologique de sources.

Les references aux sources peuvent apparaitre dans l'historique des mises a jour, mais les sections principales doivent presenter une connaissance consolidee.

Lorsqu'une nouvelle source confirme une connaissance deja presente, Codex doit :

- renforcer ou preciser l'element existant ;
- eviter de creer un bloc redondant par source ;
- ne pas repeter une information deja integree ;
- conserver le detail de la source dans la fiche de veille.

La fiche permanente doit rester synthetique, structuree et orientee decision.

## Creation de nouvelles fiches permanentes

Une nouvelle fiche permanente ne doit etre creee que si l'outil, l'IA ou le framework est clairement un sujet principal de la source ou s'il apporte une connaissance durable utile a l'ecosysteme AOS.

Si l'outil est seulement mentionne brievement, Codex doit creer uniquement une note dans la fiche de veille de l'IA principale, sans creer de fiche permanente dediee.

En cas d'incertitude, Codex doit creer la fiche de veille, classer l'outil comme sujet secondaire et ne pas creer de fiche permanente.

## Protection des fiches permanentes majeures

Pour les IA majeures comme ChatGPT, Claude, Gemini, Codex ou Claude Code, une source YouTube non officielle ne doit pas initialiser largement ou restructurer massivement la fiche permanente.

Elle peut seulement :

- creer une fiche de veille ;
- ajouter des points a surveiller ;
- integrer des connaissances prudentes si elles sont durables, clairement formulees et non speculatives.

Les informations sur noms de modeles, disponibilite, prix, benchmarks ou capacites futures doivent rester en veille tant qu'elles ne sont pas recoupees par documentation officielle, experimentation interne ou source fiable.

## Sources brutes

Les sources brutes sont deposees dans :

```text
01_Collecte/sources_brutes/
```

Sous-dossiers :

- `videos/a_traiter/`
- `articles/a_traiter/`
- `docs/a_traiter/`
- `tests_personnels/a_traiter/`

Codex doit scanner les fichiers a traiter, analyser leur contenu et detecter automatiquement l'IA, le framework IA ou l'outil IA concerne.

## Batch processing

Un seul `GO AOS` doit traiter automatiquement toutes les sources presentes dans les dossiers `a_traiter/`.

Pour les videos, Codex doit scanner :

```text
01_Collecte/sources_brutes/videos/a_traiter/
```

Codex doit traiter les sources une par une, sans demander d'intervention intermediaire sauf blocage critique.

Pour chaque source, Codex doit :

- lire la source brute ;
- detecter l'IA, l'outil ou le framework concerne ;
- router vers le bon dossier `02_IA/` ;
- creer une fiche de veille ;
- mettre a jour la fiche permanente si l'information est claire, durable et justifiee ;
- deplacer la source vers `traitees/` uniquement si le traitement de cette source reussit.

Si une source echoue sans risque critique, Codex doit :

- ne pas deplacer cette source vers `traitees/` ;
- continuer le traitement des autres sources ;
- mentionner l'echec dans le rapport consolide.

Si une erreur critique apparait, Codex doit :

- arreter le batch ;
- ne pas creer de commit ;
- ne pas pousser vers GitHub ;
- produire un rapport de blocage.

A la fin d'un batch non critique, Codex doit executer un seul cycle Git global pour toutes les sources traitees avec succes, puis produire un rapport consolide.

## Routage

Codex ne doit jamais supposer le classement a partir du dossier d'entree.

Le dossier `01_Collecte` est une zone neutre.

Le dossier `02_IA` contient les connaissances classees.

Une source peut produire :

- une fiche de veille unique si elle concerne principalement une seule IA ;
- plusieurs fiches de veille si elle traite serieusement plusieurs IA.

Chaque fiche de veille doit rester centree sur une seule IA, un framework IA ou un outil IA.

## Renommage des sources traitees

Avant de deplacer une source brute vers `traitees/`, Codex doit generer un nom lisible a partir du sujet reel detecte.

Le nom du fichier d'entree ne doit pas etre conserve s'il est generique ou trompeur.

Pour les videos, le format obligatoire est :

```text
YYYY-MM-DD_youtube_nom-chaine_sujet-video_transcript.txt
```

Regles de nommage :

- utiliser la date de traitement ou la date de collecte si elle est deja connue ;
- utiliser la plateforme detectee, par exemple `youtube` ;
- utiliser la chaine YouTube detectee ;
- utiliser le sujet reel de la video, pas le nom generique du fichier d'entree ;
- convertir le nom final en minuscules ;
- supprimer les accents ;
- supprimer les caracteres speciaux ;
- remplacer les espaces et separateurs par des tirets ;
- conserver uniquement lettres, chiffres, tirets et underscores techniques ;
- terminer obligatoirement par `_transcript.txt`.

Exemples :

- `2026-07-01_youtube_parlons-ia_claude-opus-4-8-workflows_transcript.txt`
- `2026-07-01_youtube_mike-codeur_hermes-vps-tailscale-openwebui_transcript.txt`
- `2026-07-01_youtube_labo-des-reseaux_gemini-3-guide_transcript.txt`

Si deux fichiers produisent le meme nom final, Codex doit ajouter un suffixe avant `_transcript.txt` :

- `_01`
- `_02`
- `_03`

Exemple :

```text
2026-07-01_youtube_parlons-ia_claude-code-agentique_01_transcript.txt
```

Le rapport final doit afficher pour chaque source :

- nom source initial ;
- nom source traite final ;
- chemin final dans `traitees/`.

## Fiches transversales

Les fiches transversales comme `Agents IA`, `Orchestration IA`, `MCP` ou `Standards IA` ne doivent pas etre modifiees a chaque mention secondaire dans une source.

Elles ne doivent etre enrichies que si la source apporte :

- une regle generale durable ;
- un principe d'architecture reutilisable ;
- une limite transversale importante ;
- un workflow applicable a plusieurs IA ;
- une decision strategique utile pour l'ecosysteme AOS.

Une simple mention d'un outil, d'un modele, d'un provider ou d'un usage ne suffit pas pour modifier une fiche transversale.

Si l'information concerne surtout une IA principale, elle doit rester dans la fiche de cette IA et dans sa fiche de veille.

## Validation des connaissances

Integrer uniquement les informations ayant une valeur durable.

Une information peut etre integree si elle :

- ameliore la comprehension d'une IA ;
- decrit son architecture ;
- documente une capacite importante ;
- documente une limite importante ;
- apporte un workflow reproductible ;
- influence une decision technique ou strategique ;
- ameliore l'orchestration IA.

Ne pas integrer :

- marketing ;
- promesses commerciales ;
- demonstrations sans enseignement ;
- opinions non argumentees ;
- doublons ;
- speculations ;
- informations faibles ou incertaines.

Les informations faibles ou incertaines restent uniquement dans la fiche de veille, avec le statut `A surveiller`.

Une information issue uniquement d'une video de demonstration non officielle ne doit pas etre classee comme "cas d'usage valide" dans la fiche permanente.

Elle peut etre integree uniquement comme :

- cas d'usage a tester ;
- hypothese de workflow ;
- point a surveiller ;
- evolution a confirmer.

Le statut "Cas d'usage valide" est reserve aux usages confirmes par experimentation interne, documentation officielle fiable, ou retour d'experience reproductible.

## Mise a jour de la fiche permanente

Codex doit mettre a jour automatiquement la fiche permanente lorsque l'information est claire, durable et bien classable.

Codex doit modifier uniquement les sections concernees.

Codex ne doit jamais reformater toute la fiche permanente.

Codex ne doit jamais supprimer de contenu existant sauf si la suppression est explicitement justifiee dans le rapport final.

## Git

Apres traitement complet, Codex doit executer :

```text
git status --short
git add .
git commit -m "docs(aos): integrate source analysis"
git push origin main
git status --short
```

Le message de commit doit etre adapte si possible au sujet detecte.

Exemples :

- `docs(aos): integrate Hermes source analysis`
- `docs(aos): update Codex permanent knowledge`
- `docs(aos): add MCP source watch note`

Si aucune modification utile n'a ete produite, Codex ne doit pas creer de commit vide.

Pour un batch, Codex doit creer un seul commit global et ne jamais creer un commit par source.

Messages recommandes pour un batch :

- `docs(aos): process video source batch`
- `docs(aos): integrate multi-source AI watch batch`

## Rapport final

A la fin, Codex doit afficher un rapport contenant :

- sources traitees ;
- IA / outils detectes ;
- fichiers crees ;
- fichiers modifies ;
- fiches permanentes mises a jour ;
- sections modifiees ;
- connaissances integrees ;
- connaissances non integrees ;
- points a surveiller ;
- source deplacee vers traitees ;
- nom source initial ;
- nom source traite final ;
- chemin final dans `traitees/` ;
- hash du commit ;
- resultat du push ;
- resultat final de `git status --short` ;
- decision finale : `GO`, `GO partiel`, `A surveiller` ou `Rejete`.

Pour un batch, le rapport consolide doit obligatoirement contenir :

- nombre de sources detectees ;
- nombre de sources traitees ;
- nombre de sources echouees ;
- liste des IA principales detectees ;
- detail par source ;
- fiches de veille creees ;
- fiches permanentes modifiees ;
- sections modifiees ;
- sources deplacees ;
- noms sources initiaux ;
- noms sources traites finaux ;
- chemins finaux dans `traitees/` ;
- connaissances integrees ;
- connaissances non integrees ;
- points a surveiller consolides ;
- commit cree ;
- resultat du push ;
- resultat final de `git status --short` ;
- decision finale batch.

Contraintes generales :

- Ne pas inventer d'information absente de la source.
- Reformuler systematiquement.
- Ne pas copier de longs passages de la source brute.
- Ne pas integrer le marketing dans les fiches permanentes.
- Preserver la structure standard AOS.
- Privilegier la qualite a la quantite.
- En cas d'incertitude, creer la fiche de veille mais ne pas enrichir la fiche permanente.
- Toujours terminer par un rapport final clair.
