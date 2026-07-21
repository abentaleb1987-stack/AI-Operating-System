# MCP - Fiche permanente

## 1. Fiche d'identite

- Nom : Model Context Protocol (MCP)
- Type : Protocole d'integration entre applications IA et outils ou donnees externes
- Statut dans la base : En veille / En test
- Derniere mise a jour : 2026-07-21

## 2. Role principal

MCP fournit une interface standardisee pour qu'une application hote puisse decouvrir et utiliser des capacites externes sans les reimplementer pour chaque modele ou outil.

## 3. Architecture

- Separation entre application hote, client MCP et serveur MCP.
- Capacites exposees sous forme de tools, resources et prompts.
- Echanges structures, couramment via JSON-RPC, avec une phase de decouverte des capacites.
- Les transports et details d'implementation doivent etre verifies dans la specification officielle avant choix technique.

## 4. Forces

- Reduit le couplage entre une application IA et chaque integration externe.
- Rend les capacites et leurs schemas plus explicites pour l'orchestrateur.

## 5. Faiblesses

- Un serveur MCP et ses outils elargissent le perimetre de permissions d'un agent.
- Une description ou une source non fiable peut influencer les actions proposees par l'agent.

## 6. Cas d'usage valides

Aucun cas d'usage n'est encore valide par experimentation interne AOS.

## 7. Cas d'usage a eviter

- Connecter un serveur non audite a des fichiers, secrets ou systemes de production.
- Autoriser une action a effet externe sans confirmation, journalisation et perimetre de droits minimal.

## 8. Workflows recommandes

1. Identifier le besoin et la source de donnees ou l'outil a connecter.
2. Lire la specification et la documentation du serveur concerne.
3. Limiter les permissions et tester sur un environnement isole.
4. Verifier les appels, sorties et effets externes avant extension du perimetre.

## 9. Prompts & methodes

- Declarer les outils autorises, les donnees accessibles et les actions interdites.
- Demander une validation explicite avant toute action externe sensible.

## 10. Integration dans mon ecosysteme

MCP peut etre evalue comme couche d'integration pour des outils AOS, sous reserve d'audit des serveurs, de permissions minimales et de traces d'execution.

## 11. Orchestration IA

L'orchestrateur doit conserver la responsabilite de choisir les outils, d'appliquer les permissions et de verifier les effets des appels MCP.

## 12. Evolutions

- Evolution de la specification et des transports officiels.
- Maturite des pratiques de securite, d'authentification et de journalisation des serveurs MCP.

## 13. Decisions strategiques

Ne connecter dans AOS que des serveurs MCP documentes, audites et limites au moindre privilege.

## Historique des mises a jour

- 2026-07-21 - Initialisation - Sections 1 a 13 - Source YouTube Projets IA MCP et specification officielle citee, batch AOS GO partiel
