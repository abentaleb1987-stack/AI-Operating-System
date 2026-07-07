# Hermes - Fiche permanente

## 1. Fiche d'identite

- Nom : Hermes
- Type : Agent IA / couche agentique a evaluer
- Statut dans la base : En veille / En test
- Derniere mise a jour : 2026-07-06

## 2. Role principal

Hermes est a evaluer comme agent IA oriente execution de taches, automatisation et workflows persistants.

Son role potentiel est de piloter des actions recurrentes ou semi-autonomes autour d'un backend LLM, avec supervision humaine selon le niveau de criticite.

## 3. Architecture

Architecture consolidee a confirmer par documentation officielle ou experimentation interne :

- Hermes est a traiter comme une couche agentique autour d'un backend LLM choisi, plutot que comme un modele IA autonome.
- L'installation semble possible sur environnement Linux local ou VPS ; les modes exacts recommandes restent a verifier.
- Les interactions observees incluent terminal, Hermes TUI, Telegram, dashboard et interface type Open WebUI, selon configuration.
- Les composants structurants a verifier sont : prompt systeme ou soul, memoire, sessions, skills, crons, logs, plugins, hooks et gateway/API.
- Hermes peut potentiellement se connecter a des outils externes via MCP, API ou OAuth ; ces connexions doivent etre testees une par une.
- Hermes semble pouvoir utiliser plusieurs providers, y compris providers externes ou locaux ; le choix doit tenir compte du cout, de la confidentialite, des capacites et de la criticite.
- LM Studio peut etre teste comme provider local potentiel pour Hermes via un endpoint HTTP et une cle API, avec verification stricte de l'acces reseau, de CORS, des logs, de la confidentialite et de la charge memoire.
- Hermes WebUI peut etre teste avec un provider alternatif comme Ollama via une configuration controlee ; les modeles, limites, couts, donnees envoyees et conditions d'usage doivent etre verifies avant integration operationnelle.
- Les workflows avances peuvent impliquer orchestrateur, agents specialises, agents de controle et agents paralleles ; cette architecture reste a valider experimentalement.
- L'exposition reseau et les canaux de controle doivent etre limites et audites, notamment pour VPS, Tailscale, Telegram, Open WebUI, dashboard, tokens et ports.

## 4. Forces

## 5. Faiblesses

## 6. Cas d'usage valides

Aucun cas d'usage n'est encore valide par experimentation interne, documentation officielle fiable ou retour d'experience reproductible.

## 7. Cas d'usage a eviter

- usages critiques sans controle humain ;
- prospection automatisee sans verification des donnees ;
- usage sensible sans audit securite et confidentialite ;
- usage operationnel fonde uniquement sur une demonstration video ou une source sponsorisee ;
- exposition publique directe de Hermes, Open WebUI, dashboard, ports API, tokens ou acces Telegram sans audit securite ;
- automatisation d'emails, CRM, OAuth, MCP ou donnees metier sans validation humaine, journalisation et limites d'action ;
- taches fiscales, juridiques, administratives ou financieres sans validation humaine finale, sources officielles et audit de conformite.
- agent persistant avec acces larges a emails, donnees clients, bases de production, comptes financiers, informations medicales ou fichiers personnels sans cloisonnement, scopes minimaux, logs et validation humaine.

## 8. Workflows recommandes

Workflow minimal d'experimentation :

1. Installer Hermes sur un environnement dedie.
2. Connecter un backend LLM.
3. Configurer un canal de communication.
4. Definir une tache simple.
5. Tester manuellement.
6. Ajuster prompt, frequence, format de sortie et garde-fous.

Workflow d'experimentation VPS securisee :

1. Preparer un VPS dedie et un utilisateur non root lorsque c'est possible.
2. Installer Hermes avec le mode choisi.
3. Configurer le backend LLM et verifier le cout d'usage.
4. Pour un provider alternatif, verifier les limites reelles, la confidentialite, les logs, les donnees envoyees et le comportement de facturation avant tout usage recurrent.
5. Configurer un canal de controle, par exemple Telegram, avec restriction des utilisateurs autorises.
6. Ajouter une interface optionnelle, par exemple Open WebUI, uniquement en environnement de test.
7. Restreindre l'acces reseau, par exemple via Tailscale ou solution equivalente.
8. Tester TUI, canal de communication, interface, logs, crons et dashboard.
9. Documenter les risques, tokens, ports exposes et procedures de mise a jour.

Workflow d'experimentation agentique :

1. Identifier une tache repetitive, standardisable et non critique.
2. Configurer le prompt systeme `Sys.md` avec objectif, limites, memoire, outils et formats.
3. Declarer les outils autorises, par exemple MCP, API ou provider local.
4. Tester chaque connexion en execution manuelle.
5. Verifier les sorties, les logs, les donnees lues et les donnees ecrites.
6. Ajouter une skill uniquement si la procedure devient recurrente.
7. Planifier via cron seulement apres validation manuelle.
8. Prevoir une condition d'arret et une intervention humaine pour les actions sensibles.

Workflow de test provider local LM Studio :

1. Installer LM Studio et charger un modele local adapte a la VRAM disponible.
2. Activer le serveur local uniquement dans un environnement controle.
3. Generer une cle API et limiter l'acces reseau au strict necessaire.
4. Configurer Hermes avec le provider LM Studio, l'endpoint HTTP et le modele detecte.
5. Tester une tache simple et non sensible avec journalisation.
6. Verifier latence, qualite, erreurs, saturation memoire, logs et donnees exposees.
7. Comparer le resultat a un provider distant avant tout usage operationnel.
8. Desactiver l'exposition reseau si elle n'est pas indispensable.

Workflow d'automatisation supervisee :

1. Choisir une tache recurrente non critique et reversible.
2. Donner uniquement les acces minimaux necessaires a l'agent.
3. Executer la procedure manuellement une premiere fois avec journalisation.
4. Transformer la procedure en skill seulement si elle est stable et relue.
5. Ajouter une validation humaine avant tout email, paiement, remboursement, modification client ou ecriture en base.
6. Activer un cron seulement apres plusieurs executions controlees.
7. Revoir regulierement les skills, permissions, logs, couts et erreurs.

Workflow de conception multi-agents :

1. Decomposer le processus en sous-taches distinctes.
2. Identifier les agents specialises necessaires.
3. Definir un orchestrateur et ses criteres de routage.
4. Ajouter un agent de controle pour les taches sensibles.
5. Tester chaque bloc separement avec donnees non critiques.
6. Verifier les sorties avec sources officielles ou donnees de reference.
7. Paralleliser uniquement les blocs independants.
8. Conserver une validation humaine finale pour tout impact externe.

## 9. Prompts & methodes

Pour les taches recurrentes, preciser :

- domaine cible ;
- frequence ;
- format de sortie ;
- exclusions ;
- criteres de qualite ;
- canal de livraison ;
- mecanisme anti-doublon si necessaire.

Pour le prompt systeme Hermes, preciser :

- objectif operationnel ;
- outils autorises et outils interdits ;
- emplacement et role de la memoire ;
- sources de donnees autorisees ;
- formats de sortie ;
- schemas de decision ;
- conditions d'intervention humaine ;
- garde-fous de securite, confidentialite et cout.

Pour les workflows multi-agents, preciser :

- role de l'orchestrateur ;
- role de chaque agent specialise ;
- criteres de controle independant ;
- provider ou modele autorise par sous-tache ;
- sources officielles ou donnees de reference ;
- assets, templates et regles metier ;
- actions autorisees et actions interdites ;
- journalisation et procedure de reprise.

## 10. Integration dans mon ecosysteme

Hermes est a tester prudemment pour :

- veille automatisee ;
- automatisations simples ;
- taches recurrentes ;
- agent persistant sur VPS dedie ;
- supervision via dashboard ;
- experimentation d'interfaces de controle comme TUI, Telegram ou Open WebUI ;
- automatisations connectees a des outils externes via MCP, API ou OAuth ;
- tests de providers locaux via LM Studio pour scenarios sensibles ;
- workflows administratifs, email ou CRM en mode supervise ;
- prototypage de systemes multi-agents avec agents de controle ;
- scenarios ou les resultats peuvent etre verifies avant usage.

## 11. Orchestration IA

Hermes peut etre envisage comme couche d'orchestration agentique a tester autour :

- d'un ou plusieurs backends LLM ;
- de providers externes ou locaux choisis selon cout, confidentialite, capacites et criticite ;
- d'une memoire, de sessions, de skills et de taches planifiees ;
- de canaux et interfaces de controle comme terminal, TUI, Telegram, Open WebUI ou dashboard ;
- de connexions MCP, API ou OAuth vers des outils externes ;
- d'une couche reseau privee ou controlee pour limiter l'exposition des services ;
- d'un orchestrateur, d'agents specialises et d'agents de controle pour les workflows sensibles ;
- d'agents paralleles uniquement lorsque les sous-taches sont independantes et verifiables.

Ces elements restent a confirmer avant usage strategique.

## 12. Evolutions

Cas d'usage observes a tester :

- briefing recurrent automatise ;
- recherche web structuree sous controle humain ;
- preparation de listes de leads a valider manuellement ;
- agent persistant sur environnement dedie ou VPS ;
- supervision via dashboard des sessions, logs, modeles, crons, skills et plugins ;
- interface conversationnelle ou de controle via Open WebUI, TUI, Telegram ou outil equivalent ;
- configuration agentique via prompt systeme, memoire, tools, skills et providers ;
- automatisations connectees a des outils externes via MCP, API ou OAuth ;
- orchestration avec Claude Code ou autre outil specialise pour les taches non couvertes par Hermes seul ;
- usage de provider local pour scenarios sensibles ou tests de confidentialite ;
- workflow multi-agents avec orchestrateur, agents specialises et agents de controle ;
- automatisation email, CRM, administrative ou financiere uniquement sur donnees de test ou en mode supervise.
- assistant persistant pour digests, suivis recurrents, support interne, preparation de contenus, recherche d'informations et analyse de donnees uniquement avec acces limites et validation humaine.

Points a surveiller :

- statut open source et rattachement exact a Nous Research ;
- fonctionnement reel des skills, de la memoire, des sessions, hooks, plugins et logs ;
- backends officiellement supportes ;
- commandes gateway / cron ;
- modes d'installation officiellement recommandes : service gere, Docker, root ou autre ;
- fonctionnement exact de Hermes TUI, dashboard, Open WebUI et gateway/API ;
- usage de Tailscale ou alternative pour l'acces prive aux services ;
- gestion des utilisateurs, permissions, ports, logs et mises a jour ;
- fonctionnement exact du prompt systeme ou soul et de sa relation avec la memoire, les tools et les skills ;
- fiabilite et securite des connexions MCP, API et OAuth ;
- capacites reelles de Claude Code lance depuis Hermes ;
- fonctionnement des agents paralleles ou sous-agents ;
- compatibilite et limites de LM Studio comme provider local ;
- securite de LM Studio utilise comme endpoint local pour Hermes, notamment cle API, CORS, acces LAN, logs et saturation memoire ;
- qualite reelle des modeles locaux quantises et des modeles de raisonnement locaux dans Hermes ;
- statut et fiabilite des modeles annonces comme distilles ou optimises a partir de Claude Fable ;
- risques lies a l'envoi automatique d'emails ou a l'ecriture dans des bases externes ;
- couts, confidentialite et conditions d'usage des providers tiers ;
- robustesse du spawning et de l'orchestration multi-agents ;
- fiabilite des agents de controle independants ;
- risques juridiques, fiscaux, administratifs et financiers des workflows sensibles ;
- criteres de choix des providers par criticite, cout, confidentialite et capacites ;
- Ollama comme provider potentiel pour Hermes WebUI, y compris modeles cloud, limites Pro, cout reel, confidentialite, reseau Docker partage et configuration provider personnalise ;
- securite VPS, Telegram, tokens et acces utilisateurs ;
- confidentialite des donnees ;
- fiabilite reelle sur les taches de veille et de prospection.
- securite face aux prompt injections issues d'emails, pages web, commentaires ou documents lus par l'agent ;
- proliferation de skills auto-creees, skills inutiles ou skills non auditees ;
- controle des crons, digests et taches recurrentes qui agissent sans supervision continue ;
- gestion des scopes API/OAuth et des droits sur emails, CRM, paiement, bases de donnees, fichiers personnels et donnees sensibles ;
- cout complet des taches longues incluant recherches, retries, erreurs et generation de skills.

## 13. Decisions strategiques

## Historique des mises a jour

- 2026-06-30 - Ajout - Sections 2, 3, 6, 7, 8, 9, 10, 11, 12 - Source YouTube Vision IA, validation humaine GO partiel
- 2026-07-01 - Mise a jour - Sections 3, 6, 7, 8, 10, 11, 12 - Source YouTube Mike Codeur, workflow AOS GO partiel
- 2026-07-01 - Mise a jour - Sections 3, 7, 8, 9, 10, 11, 12 - Source YouTube Parlons IA, workflow AOS GO partiel
- 2026-07-01 - Mise a jour - Sections 3, 7, 8, 9, 10, 11, 12 - Source YouTube Parlons IA business automation, workflow AOS GO partiel
- 2026-07-01 - Consolidation - Sections 3, 11, 12 - Synthese permanente Hermes apres audit Aion
- 2026-07-03 - Mise a jour - Sections 3, 8, 12 - Source YouTube Dr. Firas Hermes WebUI Ollama Kimi VPS, workflow AOS GO partiel
- 2026-07-06 - Mise a jour - Sections 7, 8, 12 - Source YouTube Melvynx Hermes usages quotidiens, batch AOS GO partiel
- 2026-07-07 - Mise a jour - Sections 3, 8, 12 - Source YouTube Parlons IA Hermes LM Studio modeles Fable locaux, batch AOS GO partiel
