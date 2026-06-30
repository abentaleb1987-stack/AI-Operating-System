# Knowledge Processing Framework

## 1. Objectif du Framework

Le Knowledge Processing Framework definit le processus officiel pour transformer une source d'information en connaissance durable, fiable et exploitable.

Il encadre le cycle complet allant de la source brute jusqu'au rapport final, en garantissant que la base de connaissances reste synthetique, tracable et maintenable.

Ce Framework repond a la question : comment traiter une information pour decider si elle peut alimenter une fiche permanente ?

Regles principales :

- Une source brute ne modifie jamais directement une fiche permanente.
- Chaque source produit une fiche de veille.
- Seules les connaissances validees alimentent la fiche permanente.
- La fiche permanente n'est jamais reecrite entierement.
- Chaque mise a jour produit uniquement les differences a integrer.
- Les informations marketing, speculatives ou non verifiees restent dans la fiche de veille.
- Les connaissances validees sont classees dans le format standard a 13 sections.
- Le processus doit pouvoir etre execute ulterieurement par des agents IA.

## 2. Perimetre

Ce Framework couvre le traitement operationnel des informations destinees a enrichir la base de connaissances du projet AI Operating System - BDD IA.

Il s'applique notamment aux objets suivants :

- outils IA ;
- agents IA ;
- frameworks IA ;
- methodes de travail ;
- workflows ;
- integrations techniques ;
- standards ;
- decisions d'usage ;
- retours d'experience.

Ce Framework ne definit pas :

- les standards transversaux du projet ;
- les templates de fichiers ;
- les schemas systeme ;
- les decisions strategiques elles-memes ;
- l'architecture generale du depot.

Les Standards definissent les regles transversales. Les Templates definissent les formats d'application. Ce Framework definit le processus a suivre.

## 3. Entrees acceptees

Les entrees acceptees sont toutes les sources pouvant contenir une information utile pour la base de connaissances.

Types d'entrees acceptes :

- source brute ;
- article externe ;
- documentation officielle ;
- video YouTube ;
- transcription YouTube ;
- livre ;
- annonce produit ;
- changelog ;
- benchmark ;
- comparatif ;
- retour d'experience ;
- experimentation personnelle ;
- note interne ;
- conversation IA ;
- decision ou observation interne.

Chaque entree doit fournir, autant que possible :

- un titre ;
- une origine ;
- une date de publication ou de consultation ;
- un type de source ;
- une reference ou URL ;
- un contexte de collecte ;
- une IA principale concernee ;
- des IA secondaires eventuelles.

Une entree sans origine claire peut etre collectee, mais elle ne peut pas etre validee directement. Elle doit rester en veille tant que son niveau de fiabilite n'est pas suffisant.

## 4. Workflow officiel

Le workflow officiel du Knowledge Processing Framework est le suivant :

```text
Source
-> Collecte
-> Qualification
-> Extraction
-> Analyse
-> Validation
-> Capitalisation
-> Archivage
-> Rapport final
```

Ce workflow est obligatoire pour toute information destinee a alimenter une fiche permanente.

Sorties possibles du workflow :

- connaissance validee et integree par differences ;
- information conservee en fiche de veille ;
- information rejetee ;
- information archivee ;
- information a surveiller.

Aucune etape ne doit permettre a une source brute de modifier directement une fiche permanente.

## 5. Description detaillee de chaque etape

### Source

Role :

Identifier l'information initiale a traiter.

Actions attendues :

- identifier la source ;
- noter son origine ;
- relever son titre ;
- relever sa date ;
- conserver sa reference ;
- identifier le contexte de decouverte.

Regles :

- Ne pas interpreter prematurement la source.
- Ne pas modifier de fiche permanente a cette etape.
- Conserver la distinction entre contenu brut et analyse.

### Collecte

Role :

Capturer les elements utiles de la source pour permettre leur traitement.

Actions attendues :

- creer une fiche de veille ou preparer son contenu ;
- resumer la source ;
- extraire les passages ou points importants ;
- conserver les references utiles ;
- indiquer la date de consultation.

Regles :

- Chaque source produit une fiche de veille.
- Les extraits de source doivent rester separes de l'analyse.
- La collecte doit rester tracable.

### Qualification

Role :

Evaluer la nature, la fiabilite et la priorite de traitement de l'information collectee.

Informations a renseigner :

- IA principale ;
- IA secondaires eventuelles ;
- type de source ;
- niveau de fiabilite ;
- priorite de traitement ;
- distinction entre fait, hypothese, marketing, speculation et retour d'experience ;
- domaine ou sujet concerne.

Regles :

- Une information non verifiee ne peut pas alimenter directement une fiche permanente.
- Les informations marketing ou speculatives restent dans la fiche de veille.
- Une source officielle n'est pas automatiquement suffisante si l'information est une annonce non encore verifiee.
- La priorite de traitement doit refleter l'impact potentiel sur la base, pas seulement l'interet de la source.

### Extraction

Role :

Extraire les informations exploitables de la fiche de veille.

Actions attendues :

- identifier les points factuels ;
- isoler les points marketing ou speculatifs ;
- identifier les impacts potentiels ;
- proposer les differences possibles pour la fiche permanente ;
- conserver les incertitudes dans la veille.

Regles :

- Les differences proposees ne sont pas encore des modifications validees.
- Les faits doivent etre separes des hypotheses.
- Les elements non verifies restent dans la fiche de veille.

### Analyse

Role :

Comparer les informations extraites avec la fiche permanente existante.

Actions attendues :

- identifier les nouveautes ;
- identifier les confirmations ;
- identifier les contradictions ;
- identifier les informations obsoletes ;
- evaluer l'impact sur la fiche permanente ;
- classer chaque difference proposee dans une des 13 sections standard.

Sections standard :

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

Regles :

- Ne jamais reecrire entierement une fiche permanente.
- Produire uniquement les differences a integrer.
- Ne pas classer une information non validee comme connaissance permanente.

### Validation

Role :

Decider si les differences proposees peuvent alimenter la fiche permanente.

Actions attendues :

- valider les differences fiables ;
- rejeter les differences non pertinentes ;
- conserver en veille les elements incertains ;
- documenter la justification ;
- dater les decisions strategiques.

Statuts possibles :

- valide ;
- rejete ;
- a surveiller ;
- archive.

Regles :

- Seules les differences validees peuvent etre capitalisees.
- Une validation doit etre explicite.
- Une contradiction doit etre signalee avant integration.
- Une decision strategique doit etre datee et justifiee.

### Capitalisation

Role :

Integrer les connaissances validees dans la fiche permanente concernee.

Actions attendues :

- preparer les differences validees ;
- identifier les sections permanentes impactees ;
- integrer uniquement les ajouts, corrections ou suppressions necessaires ;
- maintenir la lisibilite de la fiche permanente ;
- conserver la structure a 13 sections.

Regles :

- La fiche permanente n'est jamais reecrite entierement.
- Les mises a jour sont incrementales.
- Les contenus marketing, speculatifs ou non verifies sont exclus.
- Toute integration doit pouvoir etre rattachee a une source traitee.

### Archivage

Role :

Conserver la trace des elements traites lorsque le cycle actif est termine.

Actions attendues :

- archiver la fiche de veille si elle n'est plus active ;
- conserver les sources utiles ;
- conserver les justifications de validation ou de rejet ;
- indiquer les elements a surveiller si necessaire.

Regles :

- Archiver au lieu de supprimer lorsqu'une trace est utile.
- Les informations rejetees peuvent etre archivees avec justification.
- L'archive doit permettre de comprendre pourquoi une information n'a pas ete integree.

### Rapport final

Role :

Produire une synthese du traitement realise.

Actions attendues :

- resumer la source traitee ;
- indiquer le statut final ;
- lister les differences validees ;
- lister les differences rejetees ;
- lister les elements conserves en veille ;
- indiquer les sections permanentes impactees ;
- formuler la decision finale.

Regles :

- Le rapport final doit etre lisible par un humain et exploitable par un agent IA.
- Il doit distinguer clairement les faits, decisions, actions realisees et points ouverts.
- Il doit indiquer explicitement ce qui n'a pas ete integre.

## 6. Livrables produits

Le processus peut produire les livrables suivants :

- fiche de veille ;
- qualification de source ;
- differences proposees pour la fiche permanente ;
- decision de validation ;
- mise a jour incrementale de fiche permanente ;
- archive ;
- rapport final.

Livrables obligatoires :

- une fiche de veille pour chaque source ;
- un statut de decision ;
- un rapport final.

Livrables conditionnels :

- une mise a jour de fiche permanente, uniquement si des differences sont validees ;
- une archive, si la source ou la fiche de veille sort du cycle actif.

## 7. Regles obligatoires

Les regles suivantes sont non negociables :

- Une source brute ne modifie jamais une fiche permanente.
- Chaque source produit une fiche de veille.
- Seules les connaissances validees alimentent la fiche permanente.
- La fiche permanente n'est jamais reecrite entierement.
- Chaque mise a jour produit uniquement les differences a integrer.
- Les informations marketing restent dans la fiche de veille.
- Les informations speculatives restent dans la fiche de veille.
- Les informations non verifiees restent dans la fiche de veille.
- Les connaissances validees doivent etre classees dans les 13 sections standard.
- Les decisions strategiques doivent etre datees et justifiees.
- Le processus doit rester compatible avec une execution future par agents IA.

Pour les agents IA :

- produire des propositions de differences, pas des reecritures globales ;
- signaler les incertitudes ;
- ne pas inventer de source ;
- ne pas transformer une hypothese en fait ;
- respecter les Standards, Templates, Schemas et Frameworks du projet.

## 8. Cas particuliers

### Source contradictoire

Une source contradictoire avec une fiche permanente doit etre signalee. Elle ne doit pas remplacer automatiquement la connaissance existante.

Decision possible :

- valider la correction ;
- conserver la contradiction en veille ;
- demander une source complementaire ;
- classer le sujet comme a surveiller.

### Source marketing

Une source marketing peut etre collectee et resumee, mais ses affirmations doivent rester dans la fiche de veille tant qu'elles ne sont pas verifiees.

### Source non verifiable

Une source non verifiable ne peut pas alimenter directement une fiche permanente. Elle peut etre archivee ou placee en surveillance.

### Source obsolete

Une source obsolete peut servir a comprendre une evolution, mais elle ne doit pas etre integree comme connaissance actuelle sans verification.

### Source partiellement utile

Une source peut contenir a la fois des faits valides, des hypotheses et du marketing. Chaque type d'information doit etre separe.

### Plusieurs sources sur le meme sujet

Plusieurs sources convergentes peuvent renforcer la validation. Les differences proposees doivent toutefois rester synthetiques.

### Retour d'experience ou experimentation personnelle

Un retour d'experience doit etre identifie comme tel. Il peut alimenter la fiche permanente si son usage est valide, contextualise et utile.

### Information urgente mais non validee

Une information urgente mais non validee doit etre conservee en veille avec une priorite de traitement elevee. Elle ne doit pas etre capitalisee sans validation.

## 9. Criteres de qualite

Un traitement est considere comme correct si les criteres suivants sont respectes :

- la source est identifiable ;
- la fiche de veille existe ;
- les faits sont separes des hypotheses ;
- les elements marketing ou speculatifs sont isoles ;
- le niveau de fiabilite est indique ;
- la priorite de traitement est indiquee ;
- les differences proposees sont explicites ;
- les differences validees sont classees dans les 13 sections standard ;
- la fiche permanente n'est modifiee que par differences ;
- la justification de validation ou de rejet est presente ;
- le rapport final permet de comprendre le resultat du traitement.

La qualite attendue privilegie la synthese exploitable plutot que l'accumulation de notes.

## 10. Format du rapport final

Le rapport final doit utiliser le format suivant :

```markdown
# Rapport final - {{Date}} - {{Sujet}}

## Source traitee

## Statut final

## Resume du traitement

## Differences validees

## Differences rejetees

## Elements conserves en veille

## Sections permanentes impactees

## Fichiers concernes

## Actions realisees

## Decision finale

GO / NO GO / A surveiller

## Points ouverts
```

Regles :

- `GO` signifie que les differences validees peuvent etre integrees.
- `NO GO` signifie qu'aucune integration permanente ne doit etre faite.
- `A surveiller` signifie que l'information reste en veille ou en observation.
- Le rapport doit indiquer ce qui a ete integre, ce qui ne l'a pas ete et pourquoi.

## 11. Points de vigilance

Points a surveiller pendant l'execution du Framework :

- ne pas confondre annonce produit et fait valide ;
- ne pas confondre documentation officielle et validation d'usage ;
- ne pas reecrire une fiche permanente complete ;
- ne pas integrer une information sans source ;
- ne pas melanger veille et connaissance durable ;
- ne pas accumuler des details inutiles ;
- ne pas oublier le classement dans les 13 sections ;
- ne pas perdre la justification d'une decision ;
- ne pas transformer une observation personnelle en regle generale ;
- ne pas laisser un agent IA decider seul d'une integration incertaine.

En cas de doute, l'information reste dans la fiche de veille.

## 12. Statut et version

- Framework : Knowledge Processing Framework
- Version : 1.0
- Statut : Valide
- Date : 2026-06-30
- Compatibilite agents IA : oui

Documents lies :

- `PROJECT_RULES.md`
- `07_Standards/knowledge_quality_standard.md`
- `07_Standards/markdown_standard.md`
- `04_Templates/template_fiche_veille.md`
- `04_Templates/template_fiche_permanente_ia.md`
- `99_System/agents/instructions_agents.md`
