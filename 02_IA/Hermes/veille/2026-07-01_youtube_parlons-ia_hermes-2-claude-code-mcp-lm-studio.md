# 2026-07-01 - YouTube Parlons IA - Hermes 2 Claude Code MCP LM Studio

> Regle : une fiche de veille correspond a une source unique et ne modifie jamais directement une fiche permanente.

## 1. Identification de la source

- Titre : J'ai teste Hermes 2.0 avec Claude Code : Le resultat est fou !
- Source : YouTube - Parlons IA
- Fichier source : `01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_hermes-2-claude-code-mcp-lm-studio_transcript.txt`
- Type de source : Video / transcription YouTube / tutoriel / demonstration promotionnelle
- Date de publication : 2026-06-26
- Date de consultation : 2026-07-01
- Contexte de collecte : Source deposee dans `videos/a_traiter/` pour execution du workflow automatise AOS.

## 2. Detection et routage

- IA principale / outil / framework : Hermes
- IA secondaires : Claude Code, Claude, GLM, ChatGPT, MiniMax, Ollama, LM Studio, Airtable, Notion, Gmail, MCP
- Dossier de veille cible : `02_IA/Hermes/veille/`
- Dossier source traitee cible : `01_Collecte/sources_brutes/videos/traitees/`
- Niveau de fiabilite : Moyen
- Priorite : Haute

## 3. Resume synthetique

La source presente Hermes comme une couche agentique a configurer finement plutot qu'un outil pret a produire du travail des l'installation. La video insiste sur le role du prompt systeme `Sys.md`, la memoire, les skills, les outils MCP, les providers LLM, les agents paralleles, les automatisations planifiees et l'usage possible de modeles locaux via LM Studio.

Elle propose aussi de completer Hermes avec Claude Code pour certaines taches de navigation ou d'analyse visuelle, puis illustre une automatisation autour de Gmail et Airtable. Ces elements sont utiles pour orienter l'experimentation Hermes, mais la source reste une video non officielle avec contenu promotionnel, affirmations fortes sur les modeles et recommandations de formation. Les informations doivent rester prudentes et classees comme observations a tester.

## 4. Faits validables

- La source presente une interface Hermes permettant d'ouvrir un terminal et de lancer Claude depuis Hermes selon la demonstration.
- La source affirme que Hermes seul n'a pas la meme capacite de controle navigateur ou d'analyse visuelle que Claude dans l'exemple montre.
- La source montre une configuration du fichier `Sys.md` comme prompt systeme Hermes.
- La source indique que `Sys.md` peut decrire ou trouver la memoire, les skills, les outils et les comportements attendus.
- La source presente la memoire Hermes comme un element a configurer explicitement.
- La source presente les MCP comme moyen de connecter Hermes a des outils externes.
- La source montre des connexions MCP par cle API ou OAuth selon les outils.
- La source illustre des connexions avec Airtable, Notion et Gmail.
- La source montre une logique d'automatisation : collecter des emails, extraire des variables, normaliser les donnees et alimenter Airtable.
- La source mentionne des agents paralleles ou sous-agents visibles dans l'interface.
- La source mentionne des crons pour executer une automatisation a frequence definie.
- La source presente les skills comme des instructions structurees, chargees pour des taches precises.
- La source indique que Hermes peut utiliser differents providers LLM.
- La source presente une configuration de LM Studio comme provider local via endpoint compatible API.

## 5. Hypotheses

- Hermes pourrait devenir plus utile si son prompt systeme est configure comme une specification operationnelle compacte.
- La combinaison Hermes + Claude Code pourrait compenser certaines limites de navigation ou d'analyse visuelle, a tester.
- Les MCP pourraient rendre Hermes pertinent pour des workflows metier connectes a des outils externes.
- Une architecture avec providers multiples pourrait aider a choisir entre cout, confidentialite, vitesse et capacites.
- LM Studio pourrait etre utile pour des tests locaux lorsque la confidentialite prime sur la performance ou la simplicite.
- Les skills Hermes pourraient formaliser des procedures reutilisables si elles sont versionnees et auditees.

## 6. Elements marketing ou speculatifs

- Formulations de type "1000 fois plus puissant", "resultat fou" ou "IA la plus puissante".
- Promesses liees a une formation payante ou gratuite associee.
- Affirmations fortes sur des modeles, versions ou couts sans recoupement officiel.
- Comparaisons de prix, tokens ou performances entre providers sans protocole reproductible.
- Promesses d'automatisation business complete sans validation operationnelle independante.

## 7. Limites de la source

- La source est une video de demonstration non officielle avec contenu promotionnel.
- Les noms de modeles, versions et fournisseurs peuvent etre deformes ou instables.
- Les integrations MCP, OAuth, Gmail, Airtable, Notion et LM Studio doivent etre verifiees techniquement.
- L'envoi automatique d'emails et la manipulation de donnees metier presentent des risques de securite et de gouvernance.
- Les affirmations sur la confidentialite des providers doivent etre recoupees dans les politiques officielles.
- La demonstration ne constitue pas un benchmark ni un audit de securite.
- Les commandes et chemins peuvent varier selon l'installation Hermes.

## 8. Connaissances candidates

- Section 3. Architecture : Hermes peut etre observe comme wrapper agentique configurable via `Sys.md`, memoire, skills, outils, providers et MCP.
- Section 3. Architecture : la source observe une interaction entre Hermes et Claude Code via terminal integre.
- Section 3. Architecture : la source observe des connexions MCP vers des outils externes via API ou OAuth.
- Section 7. Cas d'usage a eviter : eviter les automatisations qui envoient des emails ou modifient des bases sans validation humaine et garde-fous.
- Section 8. Workflows recommandes : ajouter un workflow d'experimentation pour configurer `Sys.md`, tester MCP, executer un run manuel, puis planifier seulement apres validation.
- Section 9. Prompts & methodes : traiter le prompt systeme comme une specification compacte incluant memoire, outils autorises, criteres, templates, decisions et limites.
- Section 10. Integration dans mon ecosysteme : Hermes est a tester pour automatisations reliees a Gmail, Airtable, Notion ou bases de connaissance, sous controle humain.
- Section 11. Orchestration IA : Hermes peut etre evalue comme couche reliant providers LLM, Claude Code, MCP, skills, agents paralleles, crons et modele local.
- Section 12. Evolutions : surveiller `Sys.md`, MCP, providers, LM Studio, Claude Code dans Hermes, agents paralleles, crons et skills.

## 9. Differences proposees

### Section concernee : 3. Architecture

- Ajout propose : ajouter les elements observes autour de `Sys.md`, memoire, skills, MCP, providers, terminal Claude Code, agents paralleles et LM Studio local.
- Modification proposee : Aucune reecriture globale.
- Suppression proposee : Aucune.
- Justification : La source detaille une couche de configuration interne moins presente dans les sources precedentes.

### Section concernee : 7. Cas d'usage a eviter

- Ajout propose : eviter les automatisations d'email, CRM, OAuth, MCP ou donnees metier sans validation humaine, journalisation et limites d'action.
- Modification proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : La source montre des automatisations actives qui peuvent produire des effets externes.

### Section concernee : 8. Workflows recommandes

- Ajout propose : workflow d'experimentation configuration agentique : configurer `Sys.md`, declarer outils/memoire/skills, tester un MCP en run manuel, valider les sorties, puis seulement planifier.
- Modification proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : La source insiste sur le fait qu'Hermes doit etre configure avant automatisation.

### Section concernee : 9. Prompts & methodes

- Ajout propose : preciser les composants d'un prompt systeme Hermes : objectif, outils autorises, memoire, sources, formats, schemas de decision, garde-fous et conditions d'intervention humaine.
- Modification proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : La source presente `Sys.md` comme element structurant.

### Section concernee : 10. Integration dans mon ecosysteme

- Ajout propose : evaluer Hermes pour automatisations connectees a des outils externes via MCP, notamment bases, emails et connaissances personnelles, sans action critique automatique.
- Modification proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : Le besoin AOS porte sur capitalisation et orchestration prudente.

### Section concernee : 11. Orchestration IA

- Ajout propose : documenter Hermes comme couche orchestrant backend LLM, Claude Code, providers, MCP, skills, memoire, agents paralleles, crons et modele local.
- Modification proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : La source decrit Hermes comme wrapper et architecture agentique.

### Section concernee : 12. Evolutions

- Ajout propose : ajouter les points observes a tester et les elements a recouper.
- Modification proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : La source n'est pas officielle et doit rester a surveiller.

## 10. Validation

- Statut : GO partiel / A surveiller
- Validation humaine requise : Non, execution automatique AOS apres GO utilisateur.
- Justification : La source apporte des hypotheses techniques utiles pour structurer les tests Hermes, mais elle ne suffit pas a valider officiellement les capacites, couts, providers, securite ou integrations.

## 11. Rapport final de traitement

- Differences integrees : Sections 3, 7, 8, 9, 10, 11, 12 et historique Hermes.
- Differences non integrees : promesses marketing, comparaisons de puissance, couts fournisseurs, versions non recoupees de modeles, automatisation business sans garde-fous.
- Points a surveiller : `Sys.md`, memoire, skills, MCP, OAuth/API, Claude Code dans Hermes, providers, LM Studio, agents paralleles, crons, envoi email, Airtable, Notion, Gmail, confidentialite et couts.
- Source deplacee vers : `01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_hermes-2-claude-code-mcp-lm-studio_transcript.txt`
- Fichiers modifies : `02_IA/Hermes/fiche_permanente.md`
