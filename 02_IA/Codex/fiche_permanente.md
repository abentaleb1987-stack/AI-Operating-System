# Codex - Fiche permanente

## 1. Fiche d'identite

- Nom : Codex
- Type : Agent de developpement et d'automatisation documentaire a evaluer
- Statut dans la base : En veille / En test
- Derniere mise a jour : 2026-07-01

## 2. Role principal

Codex est a evaluer comme orchestrateur technique capable de modifier des fichiers, automatiser des workflows locaux, structurer des bases documentaires et produire des livrables audites.

## 3. Architecture

Elements observes dans la video Parlons IA du 2026-05-19, a confirmer par experimentation interne :

- usage possible dans un pipeline de second brain avec Obsidian et NotebookLM ;
- automatisation possible via skills ou scripts ;
- interaction navigateur possible via Chrome/Playwright selon la demonstration ;
- importance d'une preparation documentaire avant ingestion dans un outil de recherche.

## 4. Forces

- Peut aider a construire des pipelines locaux de preparation, transformation et routage documentaire.
- Peut orchestrer des outils differents si les permissions, chemins et sorties sont explicites.

## 5. Faiblesses

- Risque de securite si des skills ou scripts non audites pilotent navigateur, fichiers ou variables d'environnement.
- Risque d'hallucination ou de mauvaise restitution si les donnees sources sont brutes, mal OCRisees ou non structurees.

## 6. Cas d'usage valides

Aucun cas d'usage n'est encore valide par experimentation interne AOS.

## 7. Cas d'usage a eviter

- Import direct de PDF ou sources brutes non nettoyees dans une base de connaissances.
- Execution de skills externes non auditees.
- Automatisation navigateur sans journalisation, limites et verification humaine.
- Traitement de donnees sensibles dans NotebookLM ou tout outil externe sans verification de confidentialite.
- Installation globale ou activation automatique de plugins communautaires sans lecture des instructions, verification des permissions et test sur un perimetre limite.

## 8. Workflows recommandes

Workflow second brain prudent :

1. Extraire la source brute.
2. Nettoyer le texte.
3. Preserver la structure des tableaux et sections.
4. Ajouter metadonnees.
5. Decouper en chunks.
6. Decrire les images et leur position.
7. Conserver les references et citations.
8. Importer seulement des donnees structurees dans l'outil de recherche.
9. Automatiser l'interrogation uniquement avec une skill auditee.
10. Verifier les reponses et sources avant integration.

Workflow avec skills ou plugins :

1. Lire les instructions du skill ou plugin avant activation.
2. Verifier le contexte d'activation, les outils autorises et les effets possibles sur les fichiers.
3. Limiter l'usage aux taches ou le skill apporte une verification ou une methode explicite.
4. Demander des preuves objectives de resultat : tests, logs, captures ou diff controle.
5. Consigner les validations et les limites restantes dans le rapport final.

## 9. Prompts & methodes

Pour Codex, expliciter :

- source a lire ;
- transformation attendue ;
- format cible ;
- criteres de qualite documentaire ;
- limites de securite ;
- outils autorises ;
- statut attendu en cas d'incertitude.
- criteres d'acceptation et preuves attendues lorsque des skills, sous-agents ou validations visuelles sont utilises.

## 10. Integration dans mon ecosysteme

Codex peut etre utilise dans AOS pour :

- traiter des sources brutes ;
- creer des fiches de veille ;
- enrichir prudemment des fiches permanentes ;
- maintenir des pipelines de preparation documentaire ;
- auditer les changements Git ;
- automatiser des workflows locaux sous controle utilisateur.

## 11. Orchestration IA

Codex peut jouer le role d'orchestrateur executant lorsqu'il dispose d'un protocole clair, d'un acces fichiers controle, de criteres de validation et d'un rapport final auditable.

## 12. Evolutions

Points a surveiller :

- integration avec NotebookLM, Obsidian ou outils de recherche externe ;
- securite des skills et extensions navigateur ;
- qualite OCR et preservation des tableaux/images ;
- confidentialite des donnees envoyees vers services tiers ;
- usage de Playwright ou navigateur automatise dans des workflows documentaires.
- securite, maintenance et valeur effective des skills ou plugins communautaires dans les workflows Codex.

## 13. Decisions strategiques

Ne pas automatiser un second brain sans pipeline de qualite documentaire. La priorite AOS est de transformer les sources brutes en donnees structurees, sourcables et verifiables avant toute recherche ou integration.

## Historique des mises a jour

- 2026-07-01 - Ajout - Sections 1 a 13 - Source YouTube Parlons IA Obsidian NotebookLM Codex, batch AOS GO partiel
- 2026-07-10 - Mise a jour - Sections 7, 8, 9, 12 - Source YouTube Melvynx skills Claude Code Codex, batch AOS GO partiel

