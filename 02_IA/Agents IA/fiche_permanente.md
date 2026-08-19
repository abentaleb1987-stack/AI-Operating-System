# Agents IA - Fiche permanente

## 1. Fiche d'identite

- Nom : Agents IA
- Type : Systeme logiciel combinant modele IA, instructions, outils, memoire, workflow et controles
- Statut dans la base : En veille / En structuration
- Derniere mise a jour : 2026-08-19

## 2. Role principal

Un agent IA sert a transformer un modele generatif en executant de taches controlees, capable d'utiliser des outils, de suivre un workflow, de respecter des criteres d'acceptation et de produire des sorties auditables.

## 3. Architecture

Architecture minimale a retenir :

- kernel ou noyau de comportement ;
- objectif et livrable attendu ;
- workflow explicite ;
- memoire ou contexte gere ;
- outils autorises ;
- logs ;
- criteres de decision ;
- criteres d'acceptation ;
- conditions d'arret ;
- mecanisme de validation ou de demande d'aide.

Une architecture plus avancee peut inclure :

- orchestrateur principal ;
- sous-agents specialises ;
- fan-out pour taches paralleles ;
- recherche lexicale avant retrieval semantique ;
- Human-in-the-Loop pour les cas incertains ou sensibles.

La capacite de verification doit progresser avant le nombre d'agents. Pour une execution parallele, chaque chantier doit disposer d'un environnement de travail isole, d'une preuve de succes reproductible et d'un chemin d'integration explicite.

Pour un agent specialise, documenter aussi :

- contexte d'activation ;
- outils autorises et interdits ;
- nombre maximal de cycles ;
- schema d'entree/sortie ;
- memoire persistante ;
- criteres de retour vers l'orchestrateur.

Une boucle de travail agentique doit documenter :

- objectif de la boucle ;
- outils autorises ;
- test ou critere de verification ;
- diagnostic en cas d'echec ;
- preuve de succes attendue ;
- limite de cycles ou condition d'arret.

Pour un pipeline RAG auditable, documenter aussi :

- preparation des documents, frontieres de chunks, overlap, metadonnees et references ;
- modele ou espace d'embeddings compatible entre documents et requetes ;
- retrieval initial, nombre de candidats et filtres appliques ;
- reranking eventuel sur un sous-ensemble limite ;
- passages effectivement injectes au modele et citations attendues ;
- verification d'ancrage, comportement si les preuves sont insuffisantes et limite de correction.

## 4. Forces

- Peut automatiser des workflows repetables lorsque les entrees, outils et criteres sont controles.
- Peut reduire le temps de traitement par decomposition et parallelisation.
- Peut rendre les sorties plus auditables que des conversations libres.

## 5. Faiblesses

- Devient instable si les objectifs, outils ou criteres sont implicites.
- Peut deriver si les logs, limites et conditions d'arret sont absents.
- Peut saturer le contexte si les sources sont injectees sans selection.
- Les garde-fous externes au modele peuvent etre affaiblis par une configuration incoherente, une expiration manuelle oubliee, un traitement incomplet des flux ou modalites, ou une exemption propagee a un perimetre trop large.

## 6. Cas d'usage valides

Aucun cas d'usage n'est encore valide par experimentation interne AOS.

## 7. Cas d'usage a eviter

- Agent autonome sans verification humaine sur donnees ou actions sensibles.
- Prompt vague transforme en pretendu agent.
- Injection massive de documents sans index ni selection.
- Usage d'outils externes sans permissions, limites et logs.
- Skill ou hook non audite capable de piloter navigateur, fichiers, commandes ou variables d'environnement.
- Workflow long ou couteux lance sans limite de cycles, console de suivi ou criteres d'arret.
- Boucle recursive lancee sans preuve de succes mesurable ni comportement defini en cas d'incertitude.

## 8. Workflows recommandes

Workflow de conception :

1. Definir l'objectif.
2. Declarer les donnees d'entree.
3. Identifier les outils autorises.
4. Ecrire le workflow.
5. Ajouter criteres de validation et conditions d'arret.
6. Prevoir logs et erreurs.
7. Tester en sequence.
8. Paralleliser uniquement les etapes independantes.
9. Demander une precision utilisateur lorsque les criteres de verification ne sont pas objectivables.

Workflow documentaire :

1. Preparer chunks et metadonnees.
2. Interroger d'abord les index.
3. Utiliser BM25, TF-IDF ou grep pour les recherches rapides.
4. Basculer vers un agent semantique si necessaire.
5. Injecter uniquement les extraits pertinents.

Workflow RAG prudent :

1. Nettoyer les documents, preserver leur structure et joindre metadonnees et references.
2. Decouper selon les frontieres semantiques et calibrer l'overlap sur un jeu d'evaluation.
3. Indexer les chunks dans un espace d'embeddings coherent avec celui des requetes.
4. Recuperer un ensemble de candidats par recherche lexicale, vectorielle ou hybride.
5. Reranker les candidats lorsque la precision du premier retrieval est insuffisante.
6. Injecter uniquement les passages retenus et exiger une reponse ancree et sourcable.
7. Reformuler et relancer le retrieval de maniere bornee si les preuves sont faibles ; sinon refuser de conclure.
8. Mesurer rappel, precision, ancrage, citations, latence, cout et taux de refus correct.

Workflow de decisions persistantes :

1. Consigner les decisions importantes dans un ADR avec contexte, decision, options ecartees et consequences.
2. Relier l'ADR au besoin produit et aux livrables concernes.
3. Rendre les ADR consultables au demarrage d'une nouvelle session ou lors d'un changement d'agent.
4. Mettre a jour le statut d'une decision lorsque son contexte devient caduc.

Workflow de securite agentique :

1. Cartographier les entrees non fiables, donnees sensibles, outils, connecteurs et chemins d'exfiltration possibles.
2. Appliquer le moindre privilege aux fichiers, secrets, API, scopes et actions accessibles a l'agent.
3. Tester les injections directes et indirectes, y compris les contenus encodes, liens, documents et sorties d'outils.
4. Valider et filtrer les entrees comme les sorties, tout en conservant les controles classiques de la couche applicative.
5. Journaliser les appels d'outils et alertes, puis verifier qu'une compromission reste contenue dans un rayon limite.
6. Exiger une approbation humaine pour toute action sensible, irreversible ou susceptible d'exposer des donnees.
7. Deployer d'abord sur un perimetre limite avec controles renforces et observer les traces avant extension.
8. Automatiser l'expiration des acces temporaires et limiter les exemptions a des utilisateurs ou roles explicites.
9. Lier programmatiquement versions, seuils et configurations afin d'eviter les copies manuelles incoherentes.
10. Tester les chemins complets, y compris les fins de flux, images et autres modalites, puis surveiller les regressions.
11. Conserver une revue humaine ou externe independante pour les conclusions de risque ; l'auto-revue par le modele reste une preuve complementaire.

Workflow de passage d'une supervision continue a une revue par resultats :

1. Stabiliser les conventions, commandes et zones protegees dans un contrat projet versionne.
2. Construire une commande de verification reproductible combinant selon le livrable tests, compilation, lint et controles de bout en bout.
3. Isoler chaque tache parallele dans une copie de travail ou un bac a sable distinct.
4. Faire relire le resultat par un agent ou une session qui n'a pas produit la modification.
5. Presenter a l'humain le diff, les preuves de verification et le rapport de revue, tout en conservant une approbation manuelle pour les actions sensibles.
6. Augmenter progressivement le parallelisme seulement si le debit de revue et le taux de defaut restent maitrises.

## 9. Prompts & methodes

Eviter les prompts de role vagues.

Preferer des instructions structurees comme un contrat d'entree :

- contexte ;
- variables ;
- contraintes ;
- outils ;
- format de sortie ;
- criteres d'acceptation ;
- boucle de controle ;
- action en cas d'erreur.

## 10. Integration dans mon ecosysteme

Les agents IA sont a utiliser dans AOS pour :

- traiter des sources ;
- router des connaissances ;
- interroger des bases documentaires ;
- produire des fiches ;
- assister des workflows repetables ;
- maintenir des controles de qualite.

## 11. Orchestration IA

Un systeme multi-agents doit garder un orchestrateur responsable du routage, de la priorisation, du controle des deviations, de l'agregation des resultats et de la decision finale.

## 12. Evolutions

Points a surveiller :

- robustesse des agents face aux longues sequences ;
- gestion du cout des appels d'outils ;
- securite contre prompt injection ;
- qualite des logs et formats auditables ;
- performance des recherches hybrides lexicales + semantiques.
- chargement progressif des skills par rapport aux memories chargees en continu ;
- hooks deterministes pour bloquer les actions sensibles ;
- suivi de workflow des agents longs.
- reutilisation d'assets, scripts et procedures audites pour transformer les apprentissages en blocs operationnels plutot qu'en memoire implicite.
- qualite et maintien d'un registre de decisions (ADR) pour limiter la re-proposition d'options deja ecartees.
- valeur reelle du multi-query, de HyDE, des rerankers et des boucles RAG correctives sur un corpus AOS evalue.
- debit de verification, taux de defaut et charge de revue lorsque le nombre d'agents paralleles augmente ; la consommation de tokens ne doit pas devenir un objectif de performance.
- derive operationnelle des garde-fous : configuration, expiration d'acces, couverture des modalites, portee des exemptions et qualite de la detection de regression.

## 13. Decisions strategiques

Traiter un agent IA comme un systeme logiciel, pas comme un simple prompt. Aucun agent ne doit etre considere fiable sans workflow, outils bornes, criteres de validation, logs et verification.

## Historique des mises a jour

- 2026-07-01 - Ajout - Sections 1 a 13 - Sources YouTube Parlons IA, batch AOS GO partiel
- 2026-07-01 - Ajout - Sections 3, 7, 12 - Sources YouTube Parlons IA Claude Code / Codex, batch AOS GO partiel
- 2026-07-04 - Mise a jour - Sections 3, 7, 8, 12 - Source YouTube Parlons IA Claude Fable loop engineering, batch AOS GO partiel
- 2026-07-21 - Mise a jour - Sections 8, 12 - Source YouTube Mike Codeur ADR et memoire agentique, batch AOS GO partiel
- 2026-08-01 - Mise a jour - Sections 3, 8, 12 - Source YouTube Projets IA RAG, batch AOS GO partiel
- 2026-08-09 - Mise a jour - Section 8 - Source YouTube NetworkChuck, defense en profondeur des applications agentiques, batch AOS GO partiel
- 2026-08-19 - Mise a jour - Sections 3, 8 et 12 - Source YouTube IA et Strategie, supervision par resultats et boucle de verification, batch AOS GO partiel
- 2026-08-19 - Mise a jour - Sections 5, 8 et 12 - Rapport de risque officiel Anthropic, incidents de controles et deploiement progressif, batch AOS GO partiel
