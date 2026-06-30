# Knowledge Organization Framework

## 1. Objectif du Framework

Le Knowledge Organization Framework definit le processus officiel pour organiser, maintenir, consolider et faire evoluer la base de connaissances du projet AI Operating System - BDD IA.

Il repond a la question : comment garder l'AI Operating System lisible, fiable, coherent et maintenable a mesure que les connaissances s'accumulent ?

Objectifs principaux :

- maintenir une base lisible par un humain ;
- maintenir une base exploitable par des agents IA ;
- garantir la coherence entre fiches permanentes, veille, archives, Standards, Templates et Frameworks ;
- eviter l'accumulation de doublons ;
- encadrer l'evolution progressive des fiches permanentes ;
- conserver l'historique utile sans alourdir la connaissance active.

Regles principales :

- Les fiches permanentes restent synthetiques.
- Les connaissances validees sont integrees par differences.
- Les doublons sont consolides plutot qu'accumules.
- Les contradictions sont signalees avant modification.
- Les informations obsoletes sont datees ou archivees.
- Les agents IA executent les regles, ils ne redefinissent pas l'architecture.

## 2. Perimetre

Ce Framework couvre l'organisation et la maintenance de la base de connaissances dans le temps.

Il s'applique notamment a :

- la structure des connaissances dans le depot ;
- le classement des fiches permanentes et des contenus associes ;
- la consolidation des connaissances validees ;
- la gestion des doublons ;
- la gestion des contradictions ;
- la gestion de l'obsolescence ;
- l'evolution progressive des fiches permanentes ;
- l'archivage des elements utiles ;
- la maintenance Git liee a l'organisation de la base ;
- la compatibilite avec les agents IA.

Ce Framework ne definit pas :

- les regles transversales du projet, qui relevent des Standards ;
- les formats de fichiers, qui relevent des Templates ;
- le traitement d'une source brute, qui releve du Knowledge Processing Framework ;
- les arbitrages strategiques, qui relevent du Knowledge Decision Framework ;
- l'architecture generale du depot, qui releve des ADR.

Les Standards definissent les regles transversales. Les Frameworks definissent les processus. Les Templates appliquent les formats. Les agents IA executent les consignes validees.

## 3. Objets organises

Le Framework organise les objets suivants :

- fiches permanentes IA ;
- fiches de veille ;
- sources collectees ;
- prompts ;
- workflows ;
- integrations ;
- decisions ;
- retours d'experience ;
- archives ;
- Standards ;
- Frameworks ;
- Templates ;
- schemas systeme ;
- instructions agents ;
- conventions Git.

Regles :

- Chaque IA possede une fiche permanente.
- Chaque fiche permanente suit le format standard a 13 sections.
- Les connaissances validees alimentent la fiche permanente concernee.
- Les informations incertaines, marketing, speculatives ou non verifiees restent en veille.
- Les elements historiques utiles sont conserves en archive.
- Les objets de nature differente ne doivent pas etre melanges.

## 4. Principes d'organisation

L'organisation de la base repose sur les principes suivants :

- Une connaissance validee ne doit avoir qu'un emplacement principal de reference.
- Une fiche permanente est une synthese stable, pas un journal de veille.
- Une fiche de veille conserve les informations temporaires, incertaines ou en cours d'analyse.
- Une archive conserve l'historique utile, sans redevenir une base active.
- Un Standard definit une regle transversale.
- Un Framework definit un processus operationnel.
- Un Template applique un format valide.
- Un agent IA execute les regles existantes, il ne cree pas une nouvelle architecture.

Regles :

- Ne pas dupliquer une connaissance validee dans plusieurs emplacements principaux.
- Ne pas melanger source brute, analyse, decision et connaissance permanente.
- Preferer la consolidation a l'accumulation.
- Preferer la synthese exploitable aux details disperses.
- En cas de doute, conserver l'information en veille plutot que l'integrer.

## 5. Structure officielle de la base

La structure officielle de la base suit l'organisation suivante :

```text
AI Operating System

|-- 00_Documentation/
|-- 01_Collecte/
|-- 02_IA/
|-- 03_Frameworks/
|-- 04_Templates/
|-- 05_Archives/
|-- 06_Scripts/
|-- 07_Standards/
`-- 99_System/
```

Roles principaux :

- `00_Documentation/` contient la documentation generale du projet.
- `01_Collecte/` contient les sources entrantes et les elements a qualifier.
- `02_IA/` contient les connaissances permanentes et les contenus de travail par IA.
- `03_Frameworks/` contient les processus operationnels.
- `04_Templates/` contient les modeles Markdown officiels.
- `05_Archives/` contient l'historique utile et les elements sortis du cycle actif.
- `06_Scripts/` contient les automatisations futures ou existantes.
- `07_Standards/` contient les regles transversales.
- `99_System/` contient les ADR, schemas, instructions agents et conventions techniques.

Dans `02_IA/`, chaque dossier IA peut contenir :

- `fiche_permanente.md` ;
- `veille/` ;
- `prompts/` ;
- `workflows/` ;
- `integrations/` ;
- `decisions/`.

Regles :

- Les noms des dossiers IA doivent rester stables apres creation, sauf migration explicitement validee.
- Une IA principale doit avoir son propre dossier dans `02_IA/`.
- La fiche permanente doit rester a un emplacement stable.
- Les contenus de veille, prompts, workflows, integrations et decisions doivent rester separes.
- Une nouvelle categorie de dossier ne doit pas etre creee sans justification architecturale.
- Les sujets transversaux doivent etre classes dans un espace transversal uniquement lorsqu'ils depassent clairement une IA unique.

## 6. Regles de classement

Le classement doit permettre de retrouver rapidement l'information et de comprendre son statut.

Classement par nature :

- une connaissance validee va dans la fiche permanente concernee ;
- une information a verifier reste en veille ;
- une source brute reste dans la collecte ou dans les archives selon son statut ;
- une decision va dans le dossier `decisions/` concerne ;
- un prompt va dans le dossier `prompts/` concerne ;
- un workflow va dans le dossier `workflows/` concerne ;
- une integration va dans le dossier `integrations/` concerne ;
- un element obsolete ou historique va dans les archives si sa conservation est utile.

Classement par IA :

- l'IA principale determine l'emplacement principal ;
- les IA secondaires peuvent etre mentionnees dans le contenu, sans creer de duplication ;
- un contenu transversal doit etre classe dans un dossier transversal seulement s'il concerne plusieurs IA de maniere structurelle.

Regles :

- Ne pas classer une information non validee comme connaissance permanente.
- Ne pas creer plusieurs emplacements principaux pour la meme connaissance.
- Ne pas deplacer une connaissance sans conserver ou documenter la logique du changement.
- Ne pas utiliser les archives comme espace de travail actif.

## 7. Regles de consolidation

La consolidation consiste a integrer les connaissances validees dans une forme stable, synthetique et maintenable.

Actions attendues :

- comparer les differences validees avec la fiche permanente existante ;
- identifier les sections impactees ;
- fusionner les informations proches ;
- supprimer les formulations redondantes ;
- corriger les informations obsoletes ;
- conserver la structure standard a 13 sections ;
- maintenir la lisibilite globale de la fiche.

Regles :

- La fiche permanente n'est jamais reecrite entierement sans validation explicite.
- Les mises a jour se font par differences.
- Une consolidation doit reduire la complexite, pas l'augmenter.
- Les details secondaires restent en veille, en archive ou dans un fichier specialise.
- Une connaissance consolidee doit etre rattachee autant que possible a une source, une fiche de veille, une decision ou un traitement identifie.
- La synthese prime sur l'exhaustivite.

## 8. Gestion des doublons

Un doublon est une information identique, equivalente ou trop proche deja presente dans la base.

Types de doublons :

- doublon exact ;
- reformulation equivalente ;
- doublon partiel ;
- doublon entre fiche de veille et fiche permanente ;
- doublon entre deux fiches IA ;
- doublon entre Standard, Framework et Template ;
- doublon entre contenu actif et archive.

Processus de traitement :

1. Identifier l'emplacement principal de reference.
2. Comparer les formulations.
3. Conserver la version la plus fiable, synthetique et actuelle.
4. Fusionner les elements utiles.
5. Archiver ou retirer les repetitions inutiles lorsque c'est justifie.

Regles :

- Les doublons doivent etre consolides plutot qu'accumules.
- Une information validee ne doit pas etre repetee dans plusieurs fiches sans raison explicite.
- Une repetition peut etre acceptable si elle joue un role different, par exemple synthese permanente et trace historique.
- Une suppression de doublon ne doit pas effacer une justification utile.
- Les doublons detectes par un agent IA doivent etre signales clairement avant modification si leur traitement est incertain.

## 9. Gestion des contradictions

Une contradiction existe lorsqu'une information nouvelle entre en conflit avec une connaissance existante, une autre source ou une decision precedente.

Types de contradictions :

- contradiction entre une source et une fiche permanente ;
- contradiction entre deux sources ;
- contradiction entre deux fiches permanentes ;
- contradiction entre une decision ancienne et une decision recente ;
- contradiction entre usage observe et documentation officielle ;
- contradiction entre connaissance actuelle et information obsolete.

Processus de traitement :

1. Identifier precisement les elements en conflit.
2. Verifier les sources et les dates.
3. Evaluer le niveau de fiabilite.
4. Determiner si la contradiction corrige, nuance ou invalide la connaissance existante.
5. Choisir un statut : correction validee, rejet, a surveiller ou archivage.
6. Integrer uniquement les differences validees.

Regles :

- Une contradiction doit etre signalee avant modification.
- Une contradiction ne remplace jamais automatiquement la connaissance existante.
- La source la plus recente n'est pas automatiquement la plus fiable.
- Une correction permanente doit etre justifiee.
- En cas d'incertitude, la contradiction reste en veille ou a surveiller.

## 10. Gestion de l'obsolescence

Une information obsolete est une information qui n'est plus actuelle, qui a ete remplacee ou dont le contexte d'usage a change.

Cas possibles :

- fonctionnalite supprimee ;
- modele remplace ;
- workflow depasse ;
- integration devenue inutile ;
- decision strategique annulee ou remplacee ;
- information vraie historiquement mais non actuelle ;
- source ancienne conservee pour contexte.

Processus de traitement :

1. Identifier l'information potentiellement obsolete.
2. Verifier la cause de l'obsolescence.
3. Dater l'obsolescence lorsque c'est possible.
4. Mettre a jour la fiche permanente par differences si necessaire.
5. Archiver l'ancienne information si elle garde une valeur historique.
6. Signaler les sujets instables comme a surveiller.

Regles :

- Une information obsolete ne doit pas rester presentee comme actuelle.
- Les informations obsoletes doivent etre datees ou archivees.
- Une information ancienne peut etre conservee si elle aide a comprendre une evolution.
- Le retrait d'une connaissance permanente doit etre traite avec le meme niveau de rigueur qu'un ajout.
- Une obsolescence incertaine doit etre signalee plutot qu'appliquee directement.

## 11. Evolution des fiches permanentes

Les fiches permanentes evoluent progressivement vers un format stable, synthetique et coherent.

Format standard :

1. Fiche d'identite
2. Role principal
3. Architecture
4. Forces
5. Faiblesses
6. Cas d'usage valides
7. Cas d'usage a eviter
8. Workflows recommandes
9. Prompts & methodes
10. Integration dans mon ecosysteme
11. Orchestration IA
12. Evolutions
13. Decisions strategiques

Actions attendues :

- verifier la presence des 13 sections ;
- migrer progressivement les fiches anciennes ;
- integrer les connaissances validees par differences ;
- reduire les repetitions ;
- harmoniser les formulations ;
- conserver les decisions datees et justifiees ;
- maintenir une taille raisonnable.

Regles :

- Chaque fiche permanente doit suivre le format standard a 13 sections.
- Les fiches existantes sont mises a niveau progressivement.
- Une migration de format ne doit pas inventer de contenu.
- Une fiche permanente doit rester synthetique.
- Les details trop fins doivent etre places dans des fichiers specialises, en veille ou en archive.
- Les sections vides peuvent rester visibles si elles servent la compatibilite avec le format standard.

## 12. Archivage

L'archivage conserve l'historique utile lorsque des elements sortent du cycle actif.

Elements archivables :

- fiches de veille traitees ;
- sources traitees ;
- anciennes decisions ;
- experiences abandonnees ;
- versions obsoletes ;
- justifications de rejet ;
- informations non integrees mais utiles ;
- traces de migration.

Emplacements principaux :

- `05_Archives/fiches_veille_archivees/` ;
- `05_Archives/sources_archivees/` ;
- `05_Archives/anciennes_decisions/` ;
- `05_Archives/experiences_abandonnees/` ;
- `05_Archives/versions_obsoletes/`.

Regles :

- Archiver au lieu de supprimer lorsqu'une trace reste utile.
- Les archives ne doivent pas redevenir une base active.
- Une archive doit permettre de comprendre le contexte d'une decision ou d'un rejet.
- Les informations archivees ne doivent pas etre presentees comme connaissances actuelles.
- Les archives doivent rester classees et maintenables.

## 13. Maintenance Git

La base de connaissances est maintenue comme un projet versionne, auditable et evolutif.

Actions attendues :

- organiser les modifications par changements coherents ;
- separer les changements de contenu, de structure et de maintenance ;
- verifier l'etat Git avant et apres intervention ;
- limiter les modifications aux fichiers necessaires ;
- documenter les migrations significatives ;
- conserver une trace claire des ajouts, corrections, suppressions et archivages.

Regles :

- Les dossiers destines a exister dans Git doivent contenir un README.md ou un fichier .gitkeep.
- Les changements doivent etre atomiques autant que possible.
- Une mise a jour de connaissance doit etre comprehensible dans l'historique Git.
- Une migration de structure doit etre explicite.
- Les suppressions doivent etre prudentes et justifiees.
- Ne pas melanger une refonte d'organisation avec une integration de nouvelles connaissances.
- Respecter le Git Standard et les conventions Git du projet.

## 14. Compatibilite agents IA

Ce Framework doit pouvoir etre execute par Codex, Hermes, Claude Code ou tout autre agent IA autorise.

Comportements attendus :

- lire les instructions, ADR, Standards, Frameworks et Templates applicables ;
- identifier les objets concernes ;
- proposer des differences plutot que des reecritures globales ;
- signaler les doublons ;
- signaler les contradictions ;
- signaler les informations obsoletes ;
- distinguer faits, hypotheses, marketing, veille et connaissance validee ;
- respecter les emplacements officiels ;
- produire un rapport clair des actions realisees.

Limites :

- un agent IA ne redefinit pas l'architecture ;
- un agent IA ne cree pas de nouvelle structure sans validation ;
- un agent IA n'invente pas de source ;
- un agent IA ne transforme pas une hypothese en fait ;
- un agent IA ne remplace pas une connaissance contradictoire sans validation ;
- un agent IA ne reecrit pas entierement une fiche permanente sans demande explicite.

Regles :

- Les agents IA executent les regles, ils ne redefinissent pas l'architecture.
- Les incertitudes doivent etre signalees.
- Les modifications doivent rester tracables.
- Les propositions doivent respecter ADR-0001, les Standards, les Templates et les Frameworks existants.

## 15. Criteres de qualite

Une organisation est consideree comme correcte si les criteres suivants sont respectes :

- la structure officielle est respectee ;
- chaque IA possede une fiche permanente ;
- chaque fiche permanente suit ou converge vers les 13 sections standard ;
- les fiches permanentes restent synthetiques ;
- les connaissances validees sont integrees par differences ;
- les informations non validees restent en veille ;
- les doublons sont consolides ;
- les contradictions sont signalees avant modification ;
- les informations obsoletes sont datees ou archivees ;
- les archives conservent l'historique utile sans alourdir la base active ;
- les Standards, Frameworks et Templates restent separes dans leurs responsabilites ;
- les agents IA peuvent comprendre et executer le processus ;
- l'historique Git permet de comprendre les changements.

La qualite attendue privilegie la coherence, la lisibilite et la maintenabilite plutot que l'accumulation exhaustive.

## 16. Points de vigilance

Points a surveiller pendant l'organisation de la base :

- ne pas transformer la fiche permanente en espace de veille ;
- ne pas accumuler des informations equivalentes ;
- ne pas masquer un doublon par une reformulation ;
- ne pas remplacer une connaissance contradictoire sans validation ;
- ne pas conserver une information obsolete comme actuelle ;
- ne pas confondre Standard, Framework et Template ;
- ne pas creer une nouvelle categorie de dossier sans validation ;
- ne pas utiliser les archives comme espace actif ;
- ne pas effectuer de migration massive sans justification ;
- ne pas laisser un agent IA redefinir l'architecture ;
- ne pas melanger maintenance Git, ajout de contenu et refonte structurelle.

En cas de doute :

- conserver l'information en veille ;
- signaler la contradiction ;
- proposer une consolidation ;
- demander validation avant modification structurelle.

## 17. Statut et version

- Framework : Knowledge Organization Framework
- Version : 1.0
- Statut : Valide
- Date : 2026-06-30
- Compatibilite agents IA : oui

Documents lies :

- `PROJECT_RULES.md`
- `03_Frameworks/knowledge_processing/README.md`
- `04_Templates/template_fiche_permanente_ia.md`
- `04_Templates/template_fiche_veille.md`
- `07_Standards/documentation_standard.md`
- `07_Standards/git_standard.md`
- `07_Standards/knowledge_quality_standard.md`
- `07_Standards/markdown_standard.md`
- `07_Standards/naming_standard.md`
- `99_System/adr/ADR-0001-architecture-frameworks-standards.md`
- `99_System/agents/instructions_agents.md`
- `99_System/schemas/schema_fiche_permanente.md`
- `99_System/schemas/schema_fiche_veille.md`
