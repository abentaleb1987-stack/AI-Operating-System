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

## Routage

Codex ne doit jamais supposer le classement a partir du dossier d'entree.

Le dossier `01_Collecte` est une zone neutre.

Le dossier `02_IA` contient les connaissances classees.

Une source peut produire :

- une fiche de veille unique si elle concerne principalement une seule IA ;
- plusieurs fiches de veille si elle traite serieusement plusieurs IA.

Chaque fiche de veille doit rester centree sur une seule IA, un framework IA ou un outil IA.

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
git push
git status --short
```

Le message de commit doit etre adapte si possible au sujet detecte.

Exemples :

- `docs(aos): integrate Hermes source analysis`
- `docs(aos): update Codex permanent knowledge`
- `docs(aos): add MCP source watch note`

Si aucune modification utile n'a ete produite, Codex ne doit pas creer de commit vide.

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
- hash du commit ;
- resultat du push ;
- resultat final de `git status --short` ;
- decision finale : `GO`, `GO partiel`, `A surveiller` ou `Rejete`.

Contraintes generales :

- Ne pas inventer d'information absente de la source.
- Reformuler systematiquement.
- Ne pas copier de longs passages de la source brute.
- Ne pas integrer le marketing dans les fiches permanentes.
- Preserver la structure standard AOS.
- Privilegier la qualite a la quantite.
- En cas d'incertitude, creer la fiche de veille mais ne pas enrichir la fiche permanente.
- Toujours terminer par un rapport final clair.
