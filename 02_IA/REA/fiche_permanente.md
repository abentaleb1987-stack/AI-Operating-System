# REA - Fiche permanente

## 1. Fiche d'identite

- Nom : REA (Reverse Engineer Anything)
- Type : outil local d'investigation logicielle pour agents
- Projet : https://github.com/morluto/rea
- Statut dans la base : En veille / A tester
- Derniere mise a jour : 2026-10-15

## 2. Role principal

REA aide un agent a examiner le comportement ou les artefacts d'un logiciel, a relier ses constats a des preuves, puis a guider l'implementation d'une fonction adaptee a un autre projet.

## 3. Architecture

- Interface CLI et MCP, accompagnee d'un skill de routage.
- Fournisseurs d'analyse selon la plateforme et le type d'artefact ; les capacites disponibles dependent des outils installes et des limites propres a chaque fournisseur.
- Resultats d'investigation et enregistrements de preuves reutilisables.

## 4. Forces

- Separe observation, inference et implementation lorsqu'un agent documente les preuves de son analyse.
- Peut guider une investigation plus ciblee que la simple recreation d'une interface de memoire.

## 5. Faiblesses

- Ne recupere pas de facon garantie le code source original et ne clone pas automatiquement une application.
- Les resultats dependent de l'acces autorise a la cible, du fournisseur d'analyse, des interactions observees et de leur verification.
- L'installation et les integrations agentiques exigent un examen des permissions et des donnees traitees.

## 6. Cas d'usage valides

Aucun usage n'a encore ete valide par experimentation interne AOS.

## 7. Cas d'usage a eviter

- Conclure qu'un prototype d'interface equivaut au logiciel etudie.
- Inspecter des donnees ou services tiers sans droits et cadre d'utilisation verifies.
- Reutiliser automatiquement code, marque, visuels ou donnees captures sans examen approprie.

## 8. Workflows recommandes

1. Definir une fonction et une cible dont l'analyse est autorisee.
2. Lister les comportements accessibles et les outils necessaires.
3. Consigner les observations, les preuves et les zones inconnues.
4. Implementer une solution propre au besoin et au contexte du projet.
5. Tester la fonction produite et examiner ses risques avant usage.

## 9. Prompts & methodes

Demander a l'agent de distinguer ce qu'il a observe, ce qu'il deduit et ce qu'il n'a pas pu verifier.

## 10. Integration dans mon ecosysteme

REA est un candidat a un test isole dans AOS si un besoin d'analyse logicielle precis apparait. Aucune installation ou integration AOS n'a ete effectuee.

## 11. Orchestration IA

L'agent de developpement conduit l'investigation et l'implementation ; REA fournit les moyens d'inspection et les preuves associees.

## 12. Evolutions

- Suivre la maturite des fournisseurs d'analyse selon les plateformes.
- Mesurer l'apport de l'outil face a un agent seul sur un protocole reproductible.

## 13. Decisions strategiques

- 2026-10-15 - Classer REA en veille et demander une evaluation ciblee avant adoption. La demonstration video ne suffit pas a valider un gain general.

## Historique des mises a jour

- 2026-10-15 - Creation - Sections 1 a 13 - Video Simon De Lima du 2026-10-14 et documentation du projet REA.
