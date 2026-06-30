# Hermes - Fiche permanente

## 1. Fiche d'identite

- Nom : Hermes
- Type : Agent IA / couche agentique a evaluer
- Statut dans la base : En veille / En test
- Derniere mise a jour : 2026-07-01

## 2. Role principal

Hermes est a evaluer comme agent IA oriente execution de taches, automatisation et workflows persistants.

Son role potentiel est de piloter des actions recurrentes ou semi-autonomes autour d'un backend LLM, avec supervision humaine selon le niveau de criticite.

## 3. Architecture

Elements observes dans la demonstration Vision IA du 2026-06-12, a confirmer par documentation officielle ou experimentation interne :

- installation possible sur un environnement Linux local ou sur un VPS ;
- interaction possible via terminal ;
- connexion possible a Telegram via un bot ;
- usage d'un backend LLM choisi lors de la configuration, a verifier ;
- presence observee de skills, de memoire et de taches planifiees, a confirmer.

Elements observes dans la demonstration Mike Codeur du 2026-05-28, a confirmer par documentation officielle ou experimentation interne :

- experimentation possible sur VPS Linux pour un fonctionnement persistant ;
- modes d'installation presentes : service gere, Docker et installation root, a verifier ;
- interaction via Hermes TUI observee ;
- installation d'Open WebUI comme interface de chat connectable a Hermes, a tester ;
- usage de Tailscale observe pour exposer les services sur un reseau prive ;
- dashboard Hermes observe pour sessions, modeles, logs, crons, skills, plugins et configuration ;
- presence d'une gateway/API et d'une commande d'update mentionnees dans la demonstration, a confirmer.

Elements observes dans la demonstration Parlons IA du 2026-06-26, a confirmer par documentation officielle ou experimentation interne :

- configuration du prompt systeme via un fichier `Sys.md` ;
- usage de la memoire, des skills, des outils et des providers comme composants de configuration agentique ;
- connexion possible a des outils externes via MCP, API ou OAuth selon la demonstration ;
- lancement observe de Claude Code ou Claude depuis un terminal integre a Hermes ;
- presence observee d'agents paralleles ou sous-agents dans l'interface ;
- usage de crons pour planifier une automatisation ;
- configuration observee de LM Studio comme provider local via endpoint compatible API.

## 4. Forces

## 5. Faiblesses

## 6. Cas d'usage valides

Aucun cas d'usage n'est encore valide par experimentation interne, documentation officielle fiable ou retour d'experience reproductible.

## 7. Cas d'usage a eviter

- usages critiques sans controle humain ;
- prospection automatisee sans verification des donnees ;
- usage sensible sans audit securite et confidentialite ;
- usage operationnel fonde uniquement sur une demonstration video ou une source sponsorisee ;
- exposition publique directe de Hermes, Open WebUI, dashboard, ports API, tokens ou acces Telegram sans audit securite.
- automatisation d'emails, CRM, OAuth, MCP ou donnees metier sans validation humaine, journalisation et limites d'action.

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
4. Configurer un canal de controle, par exemple Telegram, avec restriction des utilisateurs autorises.
5. Ajouter une interface optionnelle, par exemple Open WebUI, uniquement en environnement de test.
6. Restreindre l'acces reseau, par exemple via Tailscale ou solution equivalente.
7. Tester TUI, canal de communication, interface, logs, crons et dashboard.
8. Documenter les risques, tokens, ports exposes et procedures de mise a jour.

Workflow d'experimentation agentique :

1. Identifier une tache repetitive, standardisable et non critique.
2. Configurer le prompt systeme `Sys.md` avec objectif, limites, memoire, outils et formats.
3. Declarer les outils autorises, par exemple MCP, API ou provider local.
4. Tester chaque connexion en execution manuelle.
5. Verifier les sorties, les logs, les donnees lues et les donnees ecrites.
6. Ajouter une skill uniquement si la procedure devient recurrente.
7. Planifier via cron seulement apres validation manuelle.
8. Prevoir une condition d'arret et une intervention humaine pour les actions sensibles.

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
- scenarios ou les resultats peuvent etre verifies avant usage.

## 11. Orchestration IA

Hermes peut etre envisage comme couche agentique potentielle autour :

- d'un backend LLM ;
- de skills ;
- d'une memoire ;
- de canaux de communication ;
- de taches planifiees ;
- d'interfaces de controle comme TUI, Telegram, Open WebUI ou dashboard ;
- d'une couche reseau privee comme Tailscale, a confirmer.
- de connexions MCP, API ou OAuth vers des outils externes ;
- de providers multiples ou locaux, a evaluer selon cout, confidentialite et capacites ;
- d'agents paralleles ou sous-agents, a confirmer par experimentation.

Ces elements restent a confirmer avant usage strategique.

## 12. Evolutions

Cas d'usage observes a tester :

- briefing recurrent automatise ;
- recherche web structuree sous controle humain ;
- preparation de listes de leads a valider manuellement ;
- agent persistant H24 sur VPS dedie ;
- supervision de sessions, logs, modeles, crons, skills et plugins via dashboard ;
- interface conversationnelle via Open WebUI connectee a Hermes.
- configuration agentique via `Sys.md` ;
- automatisation connectee a Gmail, Airtable, Notion ou autre outil externe via MCP ;
- orchestration Hermes + Claude Code pour taches de navigation ou analyse visuelle ;
- usage de provider local via LM Studio pour tests de confidentialite.

Points a surveiller :

- statut open source et rattachement exact a Nous Research ;
- fonctionnement reel des skills ;
- nature exacte de la memoire ;
- backends officiellement supportes ;
- commandes gateway / cron ;
- modes d'installation officiellement recommandes : service gere, Docker, root ou autre ;
- fonctionnement exact de Hermes TUI, dashboard, Open WebUI et gateway/API ;
- usage de Tailscale ou alternative pour l'acces prive aux services ;
- gestion des utilisateurs, permissions, ports, logs et mises a jour ;
- fonctionnement exact de `Sys.md` et de sa relation avec la memoire, les tools et les skills ;
- fiabilite et securite des connexions MCP, API et OAuth ;
- capacites reelles de Claude Code lance depuis Hermes ;
- fonctionnement des agents paralleles ou sous-agents ;
- compatibilite et limites de LM Studio comme provider local ;
- risques lies a l'envoi automatique d'emails ou a l'ecriture dans des bases externes ;
- couts, confidentialite et conditions d'usage des providers tiers ;
- securite VPS, Telegram, tokens et acces utilisateurs ;
- confidentialite des donnees ;
- fiabilite reelle sur les taches de veille et de prospection.

## 13. Decisions strategiques

## Historique des mises a jour

- 2026-06-30 - Ajout - Sections 2, 3, 6, 7, 8, 9, 10, 11, 12 - Source YouTube Vision IA, validation humaine GO partiel
- 2026-07-01 - Mise a jour - Sections 3, 6, 7, 8, 10, 11, 12 - Source YouTube Mike Codeur, workflow AOS GO partiel
- 2026-07-01 - Mise a jour - Sections 3, 7, 8, 9, 10, 11, 12 - Source YouTube Parlons IA, workflow AOS GO partiel
