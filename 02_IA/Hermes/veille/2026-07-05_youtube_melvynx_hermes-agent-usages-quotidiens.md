# 2026-07-05 - YouTube Melvynx - Hermes Agent usages quotidiens

> Regle : une fiche de veille correspond a une source unique. Elle ne modifie jamais directement une fiche permanente.

## 1. Identification de la source

- Titre : Hermes Agent : 10 VRAIS usages quotidiens que je fais avec mon Agent IA
- Source : YouTube - Melvynx
- URL ou reference : transcript local initial `2026-07-05_youtube_codex_workflow_aos_01.txt`
- Fichier source traite : `01_Collecte/sources_brutes/videos/traitees/2026-07-05_youtube_melvynx_hermes-agent-usages-quotidiens_transcript.txt`
- Type de source : Video YouTube / transcription / retour d'experience personnel
- Date de publication : 2026-04-30
- Date de consultation : 2026-07-05
- Auteur ou organisation : Melvynx
- Contexte de collecte : Batch GO AOS depuis `videos/a_traiter/`.

## 2. Qualification

- IA principale : Hermes
- IA secondaires : OpenClaw, Claude Code, ChatGPT, Claude
- Domaine : Agent autonome, automatisation personnelle, skills, memoire, crons, outils externes
- Niveau de fiabilite : Moyen faible
- Priorite : Moyenne
- Statut de traitement : Traitee

## 3. Statut du cycle de traitement

- Statut : A surveiller
- Etape actuelle : Fiche de veille creee ; integration permanente limitee aux principes prudents
- Prochaine action : Tester uniquement sur donnees non sensibles et avec validation humaine

## 4. Resume synthetique

La source presente Hermes comme agent autonome connecte a un ordinateur, a Telegram, a des APIs, a des outils metier et a des fichiers de memoire. L'auteur decrit des usages personnels : emails et remboursements, facturation, gestion de sponsors, support client, recherche de voyages, creation de contenu, suivi de donnees personnelles, analyse business, crons recurrents et creation de skills.

La valeur durable pour AOS n'est pas la validation des cas d'usage, mais le pattern operationnel : un agent persistant devient utile lorsqu'il dispose d'outils, de memoire, de procedures reutilisables et de canaux de supervision. Le risque durable est symetrique : plus l'agent dispose d'acces larges, plus les garde-fous, journaux, validations humaines et limites d'action deviennent obligatoires.

## 5. Idees principales

- Hermes est presente comme une couche agentique capable d'agir sur un environnement informatique complet.
- L'agent peut utiliser des APIs, CLIs, emails, bases de donnees, fichiers et canaux de chat.
- Les taches recurrentes peuvent etre transformees en skills reutilisables.
- Les crons et digests permettent de transformer l'agent en assistant persistant.
- Les actions sensibles doivent rester supervisees, notamment emails, remboursements, acces clients, donnees de sante et donnees financieres.

## 6. Faits validables

- La source montre des exemples d'automatisation via Telegram et outils externes.
- La source mentionne la creation de skills par l'agent apres execution d'une tache.
- La source montre une interface Hermes avec projets, crons, modeles, dashboard et skills.
- La source mentionne l'utilisation de Claude Code pour connecter ou preparer certains outils.
- La source contient des commentaires utilisateurs soulevant des questions de securite, d'acces et de prompt injection.

## 7. Hypotheses

- Hermes pourrait etre teste comme assistant persistant pour taches recurrentes non critiques si chaque outil est limite, journalise et reversible.
- La creation de skills peut reduire la friction sur les procedures repetees, mais doit etre auditee pour eviter l'accumulation de skills inutiles ou dangereux.
- Les digests quotidiens et crons peuvent etre utiles pour AOS si le perimetre de donnees reste controle.

## 8. Elements marketing ou speculatifs

- Les affirmations de fiabilite quasi parfaite ne sont pas reproductibles dans AOS.
- Les claims sur GPT 5.4, fenetres de contexte et couts ne sont pas verifiables depuis cette seule source.
- Les usages lies a la formation, aux sponsors et a la promotion de contenus ne doivent pas etre integres comme connaissances durables.
- Les exemples de donnees personnelles et medicales ne constituent pas une recommandation d'usage.

## 9. Limites de la source

- Source non officielle, personnelle et promotionnelle.
- Transcription bruitee avec erreurs d'encodage et noms d'outils deformes.
- Les resultats annonces ne sont pas accompagnes de protocole de test.
- Les acces donnes a l'agent sont tres larges et ne constituent pas un modele de securite.
- Les commentaires utilisateurs signalent des risques non resolus : acces open bar, email personnel, cout API, prompt injection.

## 10. Connaissances candidates

- Hermes : ajouter un workflow d'automatisation supervisee pour connecter outils, skills, crons et validation humaine.
- Hermes : renforcer les points a surveiller sur prompt injection, permissions, scopes OAuth/API, skills inutiles et donnees sensibles.
- Hermes : conserver les cas observes comme hypotheses a tester, pas comme cas d'usage valides.

## 11. Differences proposees pour la fiche permanente

### Section concernee : 7. Cas d'usage a eviter

- Ajout propose : eviter les agents avec acces larges a emails, donnees clients, finances, sante ou bases de production sans cloisonnement, logs et validation humaine.
- Correction proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : La source montre que la valeur operationnelle vient de l'acces aux outils, mais ce meme acces augmente fortement le risque.

### Section concernee : 8. Workflows recommandes

- Ajout propose : workflow d'automatisation supervisee avec choix de tache non critique, scopes minimaux, validation manuelle, logs, skill auditee et cron seulement apres stabilisation.
- Correction proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : Les exemples recurrentes de la source sont utiles uniquement si transformes en protocole controle.

### Section concernee : 12. Evolutions

- Ajout propose : surveiller les skills auto-creees, crons, digests, acces email/API/BDD, prompt injection et donnees sensibles.
- Correction proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : Ces points determinent si Hermes peut etre teste sans risque excessif.

## 12. Decision de validation

- Statut : GO partiel
- Justification : Les patterns d'architecture agentique sont utiles ; les cas d'usage restent non valides et doivent etre testes en environnement borne.
- Sections permanentes impactees : Hermes sections 7, 8, 12 et historique
- Validation humaine requise : Non

## 13. Elements rejetes

- Validation des automatisations email, remboursement, sponsor, sante ou finance comme cas d'usage AOS - Justification : absence de test interne et risques eleves.
- Claims de fiabilite et performance - Justification : non reproductible.
- Donnees de cout et modeles cites - Justification : source non officielle et informations instables.

## 14. Elements a surveiller

- Prompt injection via emails, pages web ou donnees lues par l'agent.
- Scopes OAuth/API trop larges.
- Skills auto-creees non auditees.
- Crons agissant sans supervision.
- Donnees personnelles, medicales, financieres ou clients.
- Cout API et derive d'execution sur taches longues.

## 15. Rapport final

- Statut final : GO partiel
- Differences validees : workflow d'automatisation supervisee ; renforcement des risques d'acces et skills
- Differences rejetees : validation des cas d'usage sensibles, claims de fiabilite, marketing
- Elements conserves en veille : usages Hermes quotidiens, crons, dashboard, skills, digests, donnees personnelles
- Fichiers concernes : `02_IA/Hermes/fiche_permanente.md`
- Actions realisees : fiche de veille creee, integration permanente ciblee
- Decision finale : GO partiel
- Points ouverts : test interne avec donnees non sensibles et scopes limites

