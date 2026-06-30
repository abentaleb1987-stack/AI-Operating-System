# ADR-0001 - Architecture des Frameworks et des Standards

## Statut

Valide

## Date

2026-06-30

## Contexte

Le projet AI Operating System - BDD IA n'est pas une simple base documentaire.

Il est concu comme un projet logiciel versionne, auditable et evolutif, destine a capitaliser les connaissances sur l'intelligence artificielle et a soutenir une strategie d'orchestration IA.

Les premieres reflexions ont montre un risque de multiplication excessive des Frameworks :

- Knowledge Validation Framework
- Knowledge Capitalization Framework
- Knowledge Comparison Framework
- Knowledge Orchestration Framework

Cette granularite risque de rendre le systeme difficile a maintenir et de creer de la confusion sur le role de chaque Framework.

Une distinction claire est donc necessaire entre :

- les Frameworks, qui definissent les processus de travail ;
- les Standards, qui definissent les regles transversales.

## Decision

Le projet adopte une architecture fondee sur deux familles distinctes :

```text
Standards = regles transversales
Frameworks = processus operationnels
```

## Standards

Les Standards definissent les regles applicables a l'ensemble du projet.

Ils repondent a la question :

```text
Quelles regles doivent etre respectees ?
```

Exemples :

- regles de nommage ;
- format Markdown ;
- conventions Git ;
- structure des fiches ;
- vocabulaire metier ;
- regles de documentation ;
- regles de qualite ;
- regles de securite ou de confidentialite.

Les Standards sont transversaux. Ils s'appliquent aux Frameworks, aux Templates, aux fiches IA, aux scripts et aux agents.

## Frameworks

Les Frameworks definissent les methodes de travail.

Ils repondent a la question :

```text
Comment executer un processus ?
```

Le projet limite volontairement les Frameworks principaux a trois responsabilites majeures.

### Knowledge Processing Framework

Responsabilite : transformer une source d'information en connaissance exploitable.

Perimetre :

- collecte ;
- qualification ;
- extraction ;
- analyse ;
- validation ;
- capitalisation ;
- archivage ;
- rapport final.

### Knowledge Organization Framework

Responsabilite : organiser, maintenir et faire evoluer la base de connaissances.

Perimetre :

- classement ;
- consolidation ;
- deduplication ;
- evolution des fiches ;
- gestion des versions ;
- archivage ;
- migration progressive du format standard.

### Knowledge Decision Framework

Responsabilite : exploiter la base de connaissances pour produire des decisions.

Perimetre :

- comparaison d'IA ;
- choix d'outil selon un besoin ;
- arbitrage technique ;
- recommandations d'orchestration ;
- decisions GO / NO GO / A surveiller ;
- priorisation strategique.

## Architecture cible

```text
AI Operating System

├── Instructions
│   └── Regles globales du projet
│
├── Standards
│   └── Regles transversales
│
├── Frameworks
│   └── Processus operationnels
│
├── Templates
│   └── Formats reutilisables
│
├── IA
│   └── Connaissance permanente et veille par IA
│
├── Collecte
│   └── Sources entrantes
│
├── Archives
│   └── Historique et elements traites
│
├── Scripts
│   └── Automatisations futures
│
└── System
    └── Agents, schemas, ADR et conventions techniques
```

## Regles d'architecture

### Regle 1 - Un Framework = une responsabilite principale

Un Framework ne doit pas melanger plusieurs missions.

Le Knowledge Processing Framework traite une source. Il ne definit pas les conventions de nommage. Il ne decide pas seul de la strategie d'orchestration.

### Regle 2 - Un Standard = une regle transversale

Un Standard doit pouvoir s'appliquer a plusieurs parties du projet.

Un Naming Standard s'applique aux fichiers, dossiers, templates, fiches de veille, scripts et futurs agents.

### Regle 3 - Les modules internes ne deviennent pas automatiquement des Frameworks

La validation, la capitalisation, la comparaison ou l'orchestration peuvent etre des etapes internes d'un Framework.

Elles ne doivent devenir des Frameworks autonomes que si leur complexite justifie une responsabilite independante.

### Regle 4 - Les Frameworks utilisent les Standards

Les Standards sont la couche normative. Les Frameworks doivent les respecter.

Exemple : le Knowledge Processing Framework doit respecter le Naming Standard, le Markdown Standard, le Git Standard et le Knowledge Quality Standard.

### Regle 5 - Les Templates implementent les Standards et les Frameworks

Les Templates ne definissent pas la methode. Ils appliquent une methode deja validee.

Exemple : le template de fiche de veille applique le Knowledge Processing Framework.

### Regle 6 - Les agents executent, ils ne redefinissent pas l'architecture

Codex, Hermes, Claude Code ou tout autre agent IA doivent respecter :

- les Instructions ;
- les ADR ;
- les Standards ;
- les Frameworks ;
- les Templates.

Ils ne doivent pas inventer une nouvelle structure sans validation.

## Consequences

Cette decision permet de :

- limiter la proliferation des Frameworks ;
- clarifier le role de chaque type de document ;
- faciliter la maintenance ;
- rendre le projet plus lisible pour Codex et les futurs agents ;
- preparer une automatisation propre ;
- traiter l'AI Operating System comme un vrai projet logiciel.

## Impact sur l'arborescence

```text
03_Frameworks/
├── README.md
├── knowledge_processing/
├── knowledge_organization/
└── knowledge_decision/

07_Standards/
├── README.md
├── naming_standard.md
├── markdown_standard.md
├── git_standard.md
├── knowledge_quality_standard.md
└── documentation_standard.md

99_System/
├── adr/
│   └── ADR-0001-architecture-frameworks-standards.md
├── agents/
├── schemas/
└── git/
```

## Decision finale

Le projet adopte officiellement la separation suivante :

```text
Instructions = contrat global du projet
Standards = regles transversales
Frameworks = processus operationnels
Templates = formats d'application
IA = connaissances capitalisees
Scripts = automatisation
System = gouvernance technique
```

Cette architecture devient la reference pour toutes les futures evolutions de l'AI Operating System.

