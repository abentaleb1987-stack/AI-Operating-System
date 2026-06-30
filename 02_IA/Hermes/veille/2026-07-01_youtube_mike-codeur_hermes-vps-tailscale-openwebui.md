# 2026-07-01 - YouTube Mike Codeur - Hermes VPS Tailscale Open WebUI

> Regle : une fiche de veille correspond a une source unique et ne modifie jamais directement une fiche permanente.

## 1. Identification de la source

- Titre : Tu dois utiliser Hermes IMMEDIATEMENT ! (Adieu OpenClaw !!)
- Source : YouTube - Mike Codeur
- Fichier source : `01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_mike-codeur_hermes-vps-tailscale-openwebui_transcript.txt`
- Type de source : Video / transcription YouTube / tutoriel / demonstration sponsorisee
- Date de publication : 2026-05-28
- Date de consultation : 2026-07-01
- Contexte de collecte : Source deposee dans `videos/a_traiter/` pour execution du workflow automatise AOS.

## 2. Detection et routage

- IA principale / outil / framework : Hermes
- IA secondaires : OpenClaw, Claude Code, Open WebUI, Tailscale, Telegram, OpenAI
- Dossier de veille cible : `02_IA/Hermes/veille/`
- Dossier source traitee cible : `01_Collecte/sources_brutes/videos/traitees/`
- Niveau de fiabilite : Moyen
- Priorite : Haute

## 3. Resume synthetique

La source presente une installation technique de Hermes sur un VPS, avec un angle pratique : rendre l'agent disponible en continu, le connecter a un modele LLM, configurer Telegram, installer Open WebUI, securiser l'acces avec Tailscale et utiliser le dashboard Hermes pour superviser sessions, modeles, logs, crons, skills et plugins.

La video apporte des informations utiles pour l'architecture d'experimentation Hermes, mais elle reste une demonstration non officielle et sponsorisee. Les points observes doivent donc etre classes comme elements a tester ou a surveiller, et non comme connaissances definitivement validees.

## 4. Faits validables

- La source montre une installation de Hermes sur un VPS Linux.
- La source presente plusieurs modes d'installation : service gere, Docker et installation root selon la demonstration.
- La source montre une configuration avec acces SSH, creation d'utilisateur et installation Hermes.
- La source montre une configuration de Telegram pour communiquer avec Hermes.
- La source montre une configuration de modele via OpenAI dans la demonstration.
- La source montre une utilisation via Hermes TUI.
- La source montre l'installation d'Open WebUI comme interface de chat connectable a Hermes.
- La source montre l'usage de Tailscale pour acceder aux services via un reseau prive.
- La source montre un dashboard Hermes avec sessions, modeles, logs, crons, skills, plugins et configuration.
- La source mentionne des crons pour des taches recurrentes et une commande d'update Hermes.

## 5. Hypotheses

- Hermes pourrait etre pertinent comme agent persistant H24 lorsqu'il est installe sur un VPS dedie.
- Tailscale pourrait reduire l'exposition publique des interfaces Hermes et Open WebUI si la configuration est correctement maitrisee.
- Open WebUI pourrait fournir une interface plus confortable pour certains usages conversationnels, mais son integration exacte avec Hermes doit etre testee.
- Le dashboard Hermes pourrait faciliter la supervision de sessions, logs, skills et taches planifiees.
- Les modes d'installation geres ou Docker pourraient simplifier la prise en main, mais leurs limites et risques doivent etre verifies.

## 6. Elements marketing ou speculatifs

- Le titre affirme qu'il faut utiliser Hermes immediatement.
- La video compare Hermes a OpenClaw avec un angle promotionnel.
- La source presente Hermes comme pouvant remplacer de nombreux SaaS, sans validation economique reproductible.
- La source contient une sponsorisation Hostinger, un code promotionnel et des recommandations commerciales.
- Certaines affirmations sur l'auto-amelioration, les skills et la superiorite d'Hermes doivent etre recoupees.

## 7. Limites de la source

- La source est une video tutorielle sponsorisee, pas une documentation officielle Hermes.
- La transcription contient du bruit YouTube, des commentaires, recommandations et erreurs d'encodage.
- Les commandes et noms techniques peuvent etre deformes par la transcription.
- La demonstration ne constitue pas un audit de securite.
- Les couts, offres VPS et options d'installation peuvent changer.
- Les integrations Open WebUI, Telegram, Tailscale et dashboard doivent etre testees avant usage operationnel.

## 8. Connaissances candidates

- Section 3. Architecture : Hermes peut etre experimente sur VPS Linux pour un fonctionnement persistant.
- Section 3. Architecture : la demonstration observe plusieurs couches possibles autour d'Hermes : TUI, Telegram, Open WebUI, dashboard, Tailscale, gateway/API et backend LLM.
- Section 7. Cas d'usage a eviter : eviter l'exposition publique directe des interfaces Hermes, Open WebUI ou dashboard sans audit securite.
- Section 8. Workflows recommandes : ajouter un workflow d'experimentation VPS securisee avec utilisateur dedie, backend LLM, canal de communication, interface optionnelle, Tailscale et tests manuels.
- Section 10. Integration dans mon ecosysteme : Hermes est a tester comme agent persistant de veille, d'automatisation et de supervision via dashboard.
- Section 11. Orchestration IA : Hermes peut etre evalue comme couche agentique autour d'un backend LLM, d'interfaces de controle, de canaux de communication, de crons, de skills et d'un reseau prive.
- Section 12. Evolutions : surveiller les modes d'installation, Tailscale, Open WebUI, dashboard, gateway/API, gestion des users, logs, plugins, crons et updates.

## 9. Differences proposees

### Section concernee : 3. Architecture

- Ajout propose : documenter prudemment l'architecture observee VPS + Hermes TUI + Telegram + Open WebUI + Tailscale + dashboard + backend LLM.
- Modification proposee : completer les elements deja observes dans la source Vision IA sans valider officiellement les integrations.
- Suppression proposee : Aucune.
- Justification : La source montre une sequence technique plus complete que la premiere veille Hermes.

### Section concernee : 6. Cas d'usage valides

- Ajout propose : Aucun.
- Modification proposee : indiquer qu'aucun cas d'usage Hermes n'est encore valide par experimentation interne, documentation officielle fiable ou retour reproductible.
- Suppression proposee : retirer le statut "valide par demonstration" des cas issus de videos non officielles.
- Justification : Le protocole AOS reserve les cas d'usage valides aux usages confirmes par experimentation interne, documentation officielle fiable ou retour reproductible.

### Section concernee : 7. Cas d'usage a eviter

- Ajout propose : eviter toute exposition publique directe des interfaces Hermes, Open WebUI, dashboard, ports API, tokens ou acces Telegram sans audit securite.
- Modification proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : La source insiste sur la securisation reseau, mais ne remplace pas un audit.

### Section concernee : 8. Workflows recommandes

- Ajout propose : ajouter un workflow d'experimentation VPS securisee.
- Modification proposee : completer le workflow minimal existant avec utilisateur dedie, acces prive, interface optionnelle et tests de bout en bout.
- Suppression proposee : Aucune.
- Justification : La source fournit une sequence d'installation et de verification exploitable comme hypothese de workflow.

### Section concernee : 10. Integration dans mon ecosysteme

- Ajout propose : evaluer Hermes pour agent persistant H24, veille recurrente, automatisations simples et supervision via dashboard.
- Modification proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : Ces usages restent a tester, mais sont pertinents pour l'ecosysteme AOS.

### Section concernee : 11. Orchestration IA

- Ajout propose : positionner Hermes comme couche agentique potentielle reliant backend LLM, TUI, Telegram, Open WebUI, dashboard, crons, skills, plugins et reseau prive.
- Modification proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : La video montre plusieurs briques d'orchestration autour d'Hermes.

### Section concernee : 12. Evolutions

- Ajout propose : ajouter les cas observes a tester et les points a surveiller issus de cette source.
- Modification proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : La source est utile pour orienter l'experimentation, mais pas suffisante pour validation permanente forte.

## 10. Validation

- Statut : GO partiel / A surveiller
- Validation humaine requise : Non, execution automatique AOS apres GO utilisateur.
- Justification : La source apporte une valeur technique pour l'architecture d'experimentation Hermes, mais elle est non officielle et sponsorisee. Les informations sont integrees uniquement comme observations prudentes, hypotheses de workflow et points a surveiller.

## 11. Rapport final de traitement

- Differences integrees : Sections 3, 6, 7, 8, 10, 11, 12 et historique Hermes.
- Differences non integrees : marketing, sponsorisation Hostinger, promesses de remplacement de SaaS, comparaison forte avec OpenClaw, validation officielle des modes d'installation et de securite.
- Points a surveiller : modes d'installation, Open WebUI, Tailscale, dashboard, gateway/API, crons, skills, plugins, update Hermes, separation utilisateur, securite VPS, tokens Telegram et confidentialite.
- Source deplacee vers : `01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_mike-codeur_hermes-vps-tailscale-openwebui_transcript.txt`
- Fichiers modifies : `02_IA/Hermes/fiche_permanente.md`
