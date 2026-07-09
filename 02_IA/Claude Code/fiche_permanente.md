# Claude Code - Fiche permanente

## 1. Fiche d'identite

- Nom : Claude Code
- Type : Interface / environnement de travail pour assistance au code et workflows locaux
- Statut dans la base : En veille / En test
- Derniere mise a jour : 2026-07-01

## 2. Role principal

Claude Code est a evaluer comme interface d'execution et de maintenance de workflows de code, notamment pour des outils locaux de recherche documentaire et de gestion de connaissances.

## 3. Architecture

Elements observes dans la video Parlons IA du 2026-06-03, a confirmer par documentation officielle ou experimentation interne :

- utilisation avec une arborescence preparee ;
- presence recommandee d'un README d'installation ;
- separation possible en dossiers `agents`, `command`, `example`, `script`, `test`, `package`, `test_config` et `system_config` selon la demonstration ;
- execution controlee par tests et verification des chemins ;
- usage possible de fonctions de recherche documentaire comme WikiQuery et WikiIndex.

Elements observes dans la video Parlons IA du 2026-05-23, a confirmer :

- fichier `Claude.md` court comme cadrage projet lu au demarrage ;
- fichiers secondaires appeles seulement dans certaines situations ;
- agents specialises decrits par fichiers `.md` ;
- memoires persistantes pouvant etre placees au niveau agent ou projet ;
- skills a chargement progressif pour reduire le contexte initial ;
- hooks dans `settings.json` pour declencher ou bloquer des comportements via scripts.

## 4. Forces

- Peut aider a deployer des outils locaux lorsque les chemins, scripts et tests sont definis en amont.
- Peut servir a maintenir des workflows documentaires bases sur index, chunks et metadonnees.

## 5. Faiblesses

- Risque de surcharge du contexte si la base documentaire est injectee en entier.
- Les versions et capacites exactes citees par des videos non officielles doivent etre verifiees.

## 6. Cas d'usage valides

Aucun cas d'usage n'est encore valide par experimentation interne AOS.

## 7. Cas d'usage a eviter

- Demander a Claude Code de gerer une base Obsidian entiere sans index, chunks ni filtres.
- Lancer un deploiement sans README, chemins cibles, tests et criteres de validation.
- Considerer Obsidian comme un RAG complet sans architecture de retrieval.
- Charger un `Claude.md` trop long qui melange toutes les instructions du projet.
- Installer des hooks ou skills non audites qui peuvent agir sur fichiers, commandes ou environnement.
- Installer globalement ou activer des skills communautaires sans audit de leurs instructions, permissions, dependances et effets attendus.

## 8. Workflows recommandes

Workflow de deploiement local :

1. Preparer un README d'installation.
2. Definir le repertoire racine, les chemins sources et les chemins de sortie.
3. Fournir les scripts ou modules attendus.
4. Demarrer par un plan de verification.
5. Installer ou assembler les composants.
6. Executer les tests prevus.
7. Corriger uniquement les points detectes par les tests.

Workflow documentaire :

1. Chunker les documents.
2. Ajouter des metadonnees.
3. Construire un index principal.
4. Interroger d'abord par mots-cles, BM25 ou TF-IDF.
5. Basculer vers un agent semantique si la recherche lexicale est insuffisante.
6. Injecter seulement les chunks pertinents.

Workflow de contexte Claude Code :

1. Garder `Claude.md` court et centre sur les regles projet.
2. Deporter les details dans des fichiers secondaires.
3. Creer des agents specialises pour les taches longues ou isolees.
4. Utiliser `/compact` si le contexte reste coherent et utile.
5. Utiliser `/clear` si la conversation derive ou hallucine.
6. Mettre les controles critiques dans des hooks audites.

Workflow avec skills ou sous-agents :

1. Clarifier le besoin, les contraintes et les criteres d'acceptation avant implementation.
2. Activer uniquement les skills utiles au contexte de la tache.
3. Exiger des preuves de validation adaptees au livrable : tests, captures, logs ou comparaison visuelle.
4. Separer autant que possible la production initiale et la revue qualite pour limiter l'auto-validation.
5. Documenter les skills utilises et les conclusions de validation dans le rapport de fin de tache.

## 9. Prompts & methodes

Pour Claude Code, expliciter :

- arborescence cible ;
- fichiers a lire ou a creer ;
- commandes autorisees ;
- tests finaux ;
- criteres de reussite ;
- limites de contexte ;
- action attendue en cas d'echec.

Pour les agents Claude Code, documenter :

- contexte d'activation ;
- outils autorises et interdits ;
- nombre maximal de cycles ;
- schema d'entree/sortie ;
- memoire persistante utilisee ;
- criteres de retour a l'orchestrateur.
- preuves attendues pour valider le resultat, notamment tests, screenshots, logs ou checklist de qualite.

## 10. Integration dans mon ecosysteme

Claude Code est a tester pour construire ou maintenir :

- scripts de recherche documentaire ;
- index Markdown ;
- fonctions de retrieval local ;
- agents de query et d'indexation ;
- outils AOS limitant l'injection de contexte.

## 11. Orchestration IA

Claude Code peut intervenir comme executant technique dans une orchestration plus large, mais le routage, les criteres de validation et la decision finale doivent rester controles par le protocole AOS.

## 12. Evolutions

Points a surveiller :

- qualite d'une architecture Obsidian + index + BM25/TF-IDF sur les donnees AOS ;
- seuils `top_k`, profondeur de recherche et scores minimaux ;
- cout et precision des longues fenetres contextuelles ;
- pertinence de modeles locaux ou tiers pour les taches de retrieval.
- comportement exact de `/clear`, `/compact`, memory, skills et hooks selon les versions ;
- securite des hooks et scripts dans `settings.json` ;
- efficacite du chargement progressif des skills sur projets AOS.
- maintenance, permissions et valeur reelle des skills communautaires avant installation globale.

## 13. Decisions strategiques

Prioriser les architectures de recherche selectives plutot que l'injection massive de documents dans le contexte d'un modele.

## Historique des mises a jour

- 2026-07-01 - Ajout - Sections 1 a 13 - Source YouTube Parlons IA, batch AOS GO partiel
- 2026-07-01 - Ajout - Sections 3, 7, 8, 9, 12 - Source YouTube Parlons IA Claude Code 101, batch AOS GO partiel
- 2026-07-10 - Mise a jour - Sections 7, 8, 9, 12 - Source YouTube Melvynx skills Claude Code Codex, batch AOS GO partiel

