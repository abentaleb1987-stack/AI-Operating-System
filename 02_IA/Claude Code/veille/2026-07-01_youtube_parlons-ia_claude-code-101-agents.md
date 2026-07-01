# 2026-07-01 - YouTube Parlons IA - Claude Code 101 et architecture d'agents

> Regle : une fiche de veille correspond a une source unique et ne modifie jamais directement une fiche permanente.

## 1. Identification de la source

- Titre : Claude Code : obtenez le diplome officiel pour etre embauche !
- Source : YouTube - Parlons IA
- Fichier source : `01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_codex_workflow_aos_04.txt`
- Type de source : Video / transcription YouTube
- Date de publication : 2026-05-23
- Date de consultation : 2026-07-01
- Contexte de collecte : Batch GO AOS depuis `videos/a_traiter/`.

## 2. Detection et routage

- IA principale / outil / framework : Claude Code
- IA secondaires : Claude, Agents IA, MCP, skills
- Dossier de veille cible : `02_IA/Claude Code/veille/`
- Dossier source traitee cible : `01_Collecte/sources_brutes/videos/traitees/`
- Niveau de fiabilite : Moyen
- Priorite : Haute

## 3. Resume synthetique

La source decrit Claude Code comme un environnement agentique qui doit etre structure avec des fichiers de contexte courts, des agents specialises, des outils autorises, des memoires persistantes et des hooks pour rendre certains comportements deterministes. Le point durable est la distinction entre un prompt global trop charge et une architecture modulaire de fichiers, agents, skills et memoires.

La video insiste sur l'importance de `Claude.md`, des fichiers secondaires, de la commande `/compact` pour conserver une coherence utile, de `/clear` lorsque la conversation derive, et des hooks dans `settings.json` pour bloquer ou declencher des comportements sensibles. Les mentions de diplome/certification et d'employabilite restent marketing et ne sont pas integrees comme connaissance durable.

## 4. Faits validables

- La source distingue chatbot simple et systeme agentique capable de collecter du contexte, prendre des decisions, agir et verifier.
- La source recommande de garder `Claude.md` compact et oriente projet, plutot que long et role-based.
- La source decrit des agents sous forme de fichiers `.md` avec version, description, modele, effort, outils, contexte d'activation, variables et schemas d'entree/sortie.
- La source presente les sous-agents comme moyen de deleguer et recuperer des donnees sans saturer la fenetre principale.
- La source distingue memoires chargees en continu et skills a chargement progressif.
- La source presente les hooks comme scripts de controle dans `settings.json` pour rendre certains comportements deterministes.
- La source cite `/clear` et `/compact` comme strategies differentes selon la qualite du contexte courant.

## 5. Hypotheses

- AOS pourrait utiliser le modele `Claude.md` court + fichiers secondaires + agents specialises pour limiter la surcharge d'instructions.
- Les hooks peuvent servir a securiser des commandes sensibles dans les workflows locaux.
- Les skills doivent etre privilegiees lorsque le chargement progressif reduit le contexte initial.

## 6. Elements marketing ou speculatifs

- Promesse d'employabilite liee a un diplome.
- Claims de reconnaissance par les entreprises.
- Promotions de formation, offres et liens.
- Commentaires YouTube et anecdotes non verifiables.

## 7. Limites de la source

- Source video non officielle et partiellement promotionnelle.
- Les details exacts de certification doivent etre verifies sur source officielle.
- Les comportements de `/clear`, `/compact`, memory, skills et hooks peuvent varier selon version.
- Les architectures de fichiers doivent etre testees dans AOS avant validation.

## 8. Connaissances candidates

- Claude Code - Section 3. Architecture : ajouter `Claude.md`, agents `.md`, memory, skills, hooks et settings.
- Claude Code - Section 8. Workflows recommandes : utiliser `/compact` pour conserver un contexte utile, `/clear` en cas de derive.
- Claude Code - Section 7. Cas d'usage a eviter : prompt global de plusieurs dizaines de pages, agent unique surcharge, hooks non audites.
- Agents IA - Section 3. Architecture : formaliser outils autorises/interdits, cycles, schema d'entree/sortie et contexte d'activation.

## 9. Differences proposees

### Section concernee : Claude Code / Architecture

- Ajout propose : decrire `Claude.md` comme couche courte de cadrage projet, completee par agents, skills, memoires et hooks.
- Modification proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : La source apporte une structure plus precise que la fiche actuelle.

### Section concernee : Agents IA / Architecture

- Ajout propose : inclure activation, outils, cycles, schemas entree/sortie et memoire persistante dans les fiches d'agents.
- Modification proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : Ces elements rendent un agent plus auditables et limite les derives.

## 10. Validation

- Statut : GO partiel / A surveiller
- Validation humaine requise : Non
- Justification : Architecture utile ; claims de certification et emploi rejetes comme marketing.

## 11. Rapport final de traitement

- Differences integrees : Architecture Claude Code, hooks, skills, memory, agents `.md`, clear/compact prudent.
- Differences non integrees : Certification, employabilite, promesses commerciales, commentaires.
- Points a surveiller : Documentation officielle Claude Code, securite des hooks, cout du contexte, comportement exact de memory/skills.
- Source deplacee vers : `01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_codex_workflow_aos_04.txt`
- Fichiers modifies : `02_IA/Claude Code/fiche_permanente.md`, `02_IA/Agents IA/fiche_permanente.md`, `02_IA/Orchestration IA/fiche_permanente.md`
