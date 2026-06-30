# Knowledge Decision Framework

## 1. Objectif du Framework

Le Knowledge Decision Framework definit le processus officiel pour exploiter la base de connaissances du projet AI Operating System - BDD IA afin de produire des decisions fiables, justifiees et tracables.

Il repond a la question : comment utiliser les fiches permanentes, les veilles, les Standards et les Frameworks pour choisir, comparer, arbitrer et orchestrer les IA selon un besoin concret ?

Objectifs principaux :

- transformer un besoin concret en decision exploitable ;
- choisir une IA selon un besoin ;
- comparer plusieurs IA ;
- arbitrer entre outils proches ;
- produire une decision `GO`, `NO GO` ou `A surveiller` ;
- recommander une orchestration IA lorsque cela est utile ;
- expliciter les risques, limites et conditions de validite ;
- conserver la trace des connaissances utilisees.

Regles principales :

- Les decisions doivent s'appuyer sur les connaissances validees.
- Les fiches permanentes sont la source de verite.
- La veille peut servir uniquement de signal faible ou d'element a surveiller.
- Les decisions doivent etre justifiees.
- Les risques et limites doivent etre explicites.
- Les arbitrages doivent rester pragmatiques.
- Un agent IA peut proposer une decision, mais il ne peut pas imposer une decision strategique.

## 2. Perimetre

Ce Framework couvre l'exploitation de la base de connaissances pour produire des decisions d'usage, de comparaison, d'arbitrage et d'orchestration IA.

Il s'applique notamment a :

- choix d'une IA selon un besoin ;
- comparaison entre plusieurs IA ;
- arbitrage entre outils proches ;
- decision `GO`, `NO GO` ou `A surveiller` ;
- recommandation d'orchestration IA ;
- analyse des risques ;
- prise en compte des projets de l'ecosysteme ;
- justification des decisions ;
- tracabilite des sources et connaissances utilisees.

Ce Framework ne definit pas :

- le traitement d'une source brute, qui releve du Knowledge Processing Framework ;
- l'organisation et la maintenance de la base, qui relevent du Knowledge Organization Framework ;
- les regles transversales, qui relevent des Standards ;
- les formats de fichiers, qui relevent des Templates ;
- les decisions strategiques elles-memes sans validation humaine.

Les Standards definissent les regles transversales. Les Frameworks definissent les processus. Les Templates appliquent les formats. Les agents IA executent les consignes validees.

## 3. Entrees utilisees

Les entrees utilisees par ce Framework sont les elements de connaissance deja presents dans la base.

Entrees principales :

- fiches permanentes IA ;
- sections des fiches permanentes ;
- decisions existantes ;
- workflows recommandes ;
- prompts et methodes ;
- integrations documentees ;
- Standards applicables ;
- Frameworks applicables ;
- Templates applicables.

Entrees secondaires :

- fiches de veille ;
- sources archivees ;
- anciennes decisions ;
- retours d'experience ;
- elements a surveiller.

Regles :

- Les fiches permanentes sont la source de verite.
- Les connaissances validees priment sur les informations de veille.
- Une fiche de veille ne peut pas fonder seule une decision strategique.
- Les informations de veille doivent etre signalees comme signaux faibles.
- Les archives peuvent eclairer l'historique, mais elles ne remplacent pas la connaissance actuelle.
- Les sources utilisees doivent rester tracables.

## 4. Types de decisions

Le Framework peut produire plusieurs types de decisions.

Types principaux :

- choix d'une IA principale ;
- choix d'une IA secondaire ;
- comparaison entre plusieurs IA ;
- arbitrage entre outils proches ;
- recommandation d'orchestration IA ;
- decision d'integration ;
- decision d'experimentation ;
- decision de maintien, abandon ou surveillance ;
- decision `GO`, `NO GO` ou `A surveiller`.

Regles :

- Le type de decision doit etre explicite.
- Une recommandation n'est pas automatiquement une validation strategique.
- Une decision peut etre temporaire si le contexte est instable.
- Une decision d'experimentation doit etre distinguee d'une decision d'adoption durable.
- Une decision doit pouvoir etre relue et revisee.

## 5. Workflow decisionnel

Le workflow officiel du Knowledge Decision Framework est le suivant :

```text
Besoin
-> Qualification du besoin
-> Identification du contexte
-> Selection des IA candidates
-> Collecte des connaissances validees
-> Evaluation selon criteres
-> Comparaison
-> Analyse des risques
-> Arbitrage
-> Recommandation
-> Decision finale
-> Tracabilite et justification
```

Ce workflow est obligatoire pour toute decision destinee a orienter un choix d'IA, une comparaison, une integration ou une orchestration.

Sorties possibles :

- recommandation argumentee ;
- decision `GO` ;
- decision `NO GO` ;
- decision `A surveiller` ;
- proposition d'experimentation ;
- proposition d'orchestration ;
- demande de clarification du besoin ;
- demande de connaissances complementaires.

Regles :

- Ne pas commencer par l'outil prefere.
- Le besoin guide la selection.
- Les connaissances validees guident l'arbitrage.
- Les incertitudes doivent etre conservees dans la decision.
- La decision finale doit etre lisible, actionnable et revisable.

## 6. Qualification du besoin

La qualification du besoin transforme une demande generale en besoin decisionnel clair.

Informations a renseigner :

- objectif recherche ;
- besoin metier ou operationnel ;
- type de tache ;
- contexte d'usage ;
- projet concerne ;
- utilisateurs ou agents concernes ;
- contraintes techniques ;
- contraintes humaines ;
- contraintes de cout, temps ou maintenance ;
- niveau de criticite ;
- frequence d'usage ;
- besoin d'automatisation ;
- criteres de succes.

Regles :

- Le besoin metier ou operationnel prime toujours sur la preference pour un outil IA.
- Une decision sans besoin qualifie est fragile.
- Le besoin doit etre formule avant la comparaison.
- Les contraintes du projet doivent etre explicites.
- Si le besoin est trop vague, la sortie correcte est une demande de clarification.
- Ne pas transformer une preference personnelle en critere objectif.

## 7. Selection des IA candidates

La selection des IA candidates identifie les outils pertinents a evaluer pour le besoin qualifie.

Categories possibles :

- IA directement adaptees au besoin ;
- IA proches ou alternatives ;
- IA deja integrees dans l'ecosysteme ;
- IA pertinentes pour une orchestration ;
- IA a exclure ;
- IA a surveiller.

Actions attendues :

- consulter les fiches permanentes pertinentes ;
- identifier les IA dont les cas d'usage valides correspondent au besoin ;
- identifier les IA dont les limites connues bloquent le besoin ;
- limiter la comparaison aux candidates utiles ;
- signaler les candidates fondees seulement sur des signaux faibles.

Regles :

- La selection doit s'appuyer sur les fiches permanentes.
- Ne pas comparer toutes les IA par defaut.
- Une IA exclue doit l'etre avec justification.
- Une IA en veille peut etre candidate uniquement avec un statut prudent.
- Une IA ne doit pas etre retenue uniquement parce qu'elle est recente ou populaire.

## 8. Criteres d'evaluation

Les criteres d'evaluation permettent de comparer les IA candidates selon le besoin.

Criteres possibles :

- adequation au besoin ;
- qualite de sortie ;
- fiabilite ;
- maturite ;
- facilite d'integration ;
- cout ou effort d'usage ;
- rapidite de mise en oeuvre ;
- maintenabilite ;
- compatibilite avec l'ecosysteme ;
- potentiel d'orchestration ;
- risques ;
- limites connues ;
- dependance externe ;
- besoin de supervision humaine.

Regles :

- Les criteres doivent etre adaptes au besoin.
- Tous les criteres ne pesent pas forcement le meme poids.
- Les limites doivent etre evaluees autant que les forces.
- Les criteres doivent rester pragmatiques.
- Un critere non documente doit etre signale comme incertain.
- Les criteres doivent pouvoir etre relies aux fiches permanentes ou aux connaissances validees.

## 9. Comparaison et scoring

La comparaison structure l'evaluation des candidates. Le scoring peut aider l'arbitrage, mais il ne remplace pas le jugement.

Formats possibles :

- comparaison qualitative ;
- tableau comparatif ;
- score simple ;
- score pondere ;
- classement par adequation au besoin ;
- synthese forces / limites / risques.

Regles :

- Un score doit etre justifie.
- Ne pas creer de precision artificielle.
- Le scoring aide l'arbitrage, il ne remplace pas la decision.
- Une IA peut etre pertinente pour un besoin et non pertinente pour un autre.
- Les faits valides doivent etre distingues des signaux faibles.
- Une absence d'information doit etre signalee, pas compensee par une supposition.

## 10. Analyse des risques

L'analyse des risques rend visibles les limites avant la recommandation.

Types de risques :

- risque technique ;
- risque de fiabilite ;
- risque de qualite de sortie ;
- risque d'integration ;
- risque de cout ou dependance ;
- risque de maintenance ;
- risque de securite ou confidentialite ;
- risque d'obsolescence ;
- risque lie a une information incertaine ;
- risque strategique.

Actions attendues :

- identifier les risques principaux ;
- distinguer risque valide et risque suppose ;
- evaluer l'impact sur le besoin ;
- indiquer les conditions de reduction du risque ;
- signaler les risques bloquants.

Regles :

- Une decision sans risques explicites est incomplete.
- Les risques doivent etre contextualises.
- Un risque eleve peut mener a `A surveiller` ou `NO GO`.
- Les risques non verifies doivent rester signales comme hypotheses.
- La recommandation doit tenir compte des risques, pas seulement des forces.

## 11. Arbitrage et recommandation

L'arbitrage transforme la comparaison et l'analyse des risques en recommandation claire.

Elements attendus :

- option recommandee ;
- alternatives acceptables ;
- options rejetees ;
- raisons principales ;
- compromis acceptes ;
- conditions de validite ;
- limites de la recommandation.

Regles :

- L'arbitrage doit etre pragmatique.
- La meilleure IA abstraite n'est pas forcement le meilleur choix pour le projet.
- Les compromis doivent etre explicites.
- Une recommandation doit etre comprehensible sans relire toute la comparaison.
- Une recommandation incertaine doit mener a `A surveiller` ou a une experimentation limitee.
- Une recommandation strategique doit rester soumise a validation humaine.

## 12. Decision GO / NO GO / A surveiller

La decision finale stabilise le resultat de l'arbitrage.

Statuts possibles :

- `GO` : l'option est recommandee pour le besoin qualifie.
- `NO GO` : l'option n'est pas recommandee pour le besoin qualifie.
- `A surveiller` : l'option presente un potentiel, mais les informations ou garanties sont insuffisantes.

Format obligatoire :

```markdown
Decision :
Justification :
Risques :
Conditions :
Prochaine action :
```

Regles :

- `GO` doit etre justifie par des connaissances validees.
- `NO GO` doit expliquer les raisons du rejet.
- `A surveiller` ne doit pas etre presente comme une validation.
- Une decision doit etre datee lorsqu'elle est materialisee dans un fichier de decision.
- Une decision peut etre revisee si la base de connaissances evolue.
- Les conditions de revision doivent etre explicites lorsque le contexte est instable.

## 13. Orchestration IA

L'orchestration IA consiste a recommander une combinaison d'IA lorsque plusieurs outils apportent une valeur complementaire.

Elements a definir :

- IA principale ;
- IA secondaires ;
- role de chaque IA ;
- sequence de travail ;
- entrees et sorties attendues ;
- points de controle humain ;
- limites de l'orchestration ;
- conditions d'usage ;
- risques de complexite.

Regles :

- L'orchestration la plus simple qui repond correctement au besoin doit etre preferee.
- L'orchestration doit repondre a un besoin reel.
- Ne pas complexifier si une IA seule suffit.
- Chaque IA doit avoir un role clair.
- Les dependances entre IA doivent etre explicites.
- Les points de controle humain doivent etre indiques pour les usages critiques.
- Une orchestration experimentale doit etre signalee comme telle.

## 14. Integration dans mon ecosysteme

Une decision doit tenir compte des projets, outils, workflows et contraintes deja presents dans l'ecosysteme.

Elements a analyser :

- projet concerne ;
- outils deja utilises ;
- workflows existants ;
- contraintes d'environnement ;
- niveau d'integration requis ;
- effort d'adoption ;
- impacts sur les pratiques existantes ;
- maintenance future ;
- compatibilite avec les Standards et Frameworks du projet.

Regles :

- Une decision doit etre adaptee a l'ecosysteme reel.
- Ne pas recommander un outil isole de son contexte d'usage.
- L'integration doit rester maintenable.
- Une solution deja integree peut etre preferee si elle repond correctement au besoin.
- Les decisions durables peuvent alimenter les fiches permanentes apres validation.

## 15. Tracabilite et justification

La tracabilite rend la decision auditable, revisable et exploitable dans le temps.

Elements a indiquer :

- besoin qualifie ;
- fiches permanentes consultees ;
- sections utilisees ;
- decisions existantes consultees ;
- workflows ou integrations utilises ;
- Standards ou Frameworks mobilises ;
- veilles utilisees comme signaux faibles ;
- criteres appliques ;
- raisons de l'arbitrage ;
- risques identifies ;
- limites ;
- date de decision ;
- points ouverts.

Regles :

- Une decision doit indiquer sur quoi elle s'appuie.
- Les sources incertaines doivent etre distinguees des connaissances validees.
- Les justifications doivent etre synthetiques mais suffisantes.
- La tracabilite doit permettre une revision future.
- Une decision sans justification ne doit pas etre consideree comme stable.

## 16. Compatibilite agents IA

Ce Framework doit pouvoir etre execute par Codex, Hermes, Claude Code ou tout autre agent IA autorise.

Comportements attendus :

- lire les instructions, ADR, Standards, Frameworks et Templates applicables ;
- lire les fiches permanentes pertinentes ;
- identifier les candidates ;
- qualifier le besoin si possible ;
- proposer une grille de comparaison ;
- distinguer connaissances validees et signaux faibles ;
- signaler les informations manquantes ;
- signaler les risques ;
- produire une recommandation argumentee ;
- distinguer proposition et decision validee ;
- demander validation humaine si la decision est strategique.

Limites :

- un agent IA peut proposer une decision, mais il ne peut pas imposer une decision strategique ;
- un agent IA ne doit pas inventer d'information ;
- un agent IA ne doit pas transformer une veille en connaissance validee ;
- un agent IA ne doit pas masquer les incertitudes ;
- un agent IA ne doit pas redefinir l'architecture ;
- un agent IA ne doit pas remplacer la validation humaine lorsque celle-ci est requise.

Regles :

- Les agents IA executent les regles, ils ne redefinissent pas l'architecture.
- Les propositions doivent respecter ADR-0001, les Standards, les Templates et les Frameworks existants.
- Les incertitudes doivent etre explicites.
- Une recommandation produite par agent doit rester revisable.

## 17. Criteres de qualite

Une decision est consideree comme correcte si les criteres suivants sont respectes :

- le besoin est clairement qualifie ;
- le contexte projet est explicite ;
- les candidates sont pertinentes ;
- les fiches permanentes ont ete utilisees comme source de verite ;
- les informations de veille sont signalees comme signaux faibles ;
- les criteres d'evaluation sont explicites ;
- la comparaison est comprehensible ;
- les scores eventuels sont justifies ;
- les risques et limites sont documentes ;
- l'arbitrage est pragmatique ;
- le statut `GO`, `NO GO` ou `A surveiller` est clair ;
- la justification est suffisante ;
- la tracabilite permet une revision future ;
- le role des agents IA reste limite a la proposition sauf validation humaine.

La qualite attendue privilegie une decision actionnable, justifiee et revisable plutot qu'une comparaison exhaustive.

## 18. Points de vigilance

Points a surveiller pendant l'execution du Framework :

- ne pas choisir une IA par preference personnelle ;
- ne pas partir de l'outil avant le besoin ;
- ne pas surponderer une annonce recente ;
- ne pas confondre veille et connaissance validee ;
- ne pas produire un score sans justification ;
- ne pas ignorer les risques ;
- ne pas recommander une orchestration trop complexe ;
- ne pas imposer une decision strategique par agent IA ;
- ne pas oublier le contexte projet ;
- ne pas transformer une experimentation en adoption durable ;
- ne pas presenter `A surveiller` comme un `GO`.

En cas de doute :

- qualifier le besoin avant de comparer ;
- utiliser `A surveiller` si l'information est insuffisante ;
- signaler les contradictions avant arbitrage ;
- demander validation humaine pour les decisions strategiques ;
- revenir au Knowledge Processing Framework si une source doit etre traitee ;
- revenir au Knowledge Organization Framework si la base doit etre consolidee avant decision.

## 19. Statut et version

- Framework : Knowledge Decision Framework
- Version : 1.0
- Statut : Valide
- Date : 2026-06-30
- Compatibilite agents IA : oui

Documents lies :

- `PROJECT_RULES.md`
- `03_Frameworks/knowledge_processing/README.md`
- `03_Frameworks/knowledge_organization/README.md`
- `04_Templates/template_decision.md`
- `04_Templates/template_comparatif_ia.md`
- `07_Standards/git_standard.md`
- `07_Standards/knowledge_quality_standard.md`
- `07_Standards/markdown_standard.md`
- `07_Standards/naming_standard.md`
- `99_System/adr/ADR-0001-architecture-frameworks-standards.md`
- `99_System/agents/instructions_agents.md`
