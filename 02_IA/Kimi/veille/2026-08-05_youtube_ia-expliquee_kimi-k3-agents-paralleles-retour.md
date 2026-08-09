# 2026-08-05 - YouTube / IA Expliquee - Kimi K3, agents paralleles et limites de coordination

## 1. Identification de la source

- Titre : Claude Fable 5 obsolete ? Mon verdict sur Kimi K3
- Source : YouTube - IA Expliquee
- Type : transcription video non officielle, test avec liens commerciaux
- Date de publication indiquee : 2026-08-05
- Date de consultation : 2026-08-09
- Fichier source traite : `01_Collecte/sources_brutes/videos/traitees/2026-08-04_youtube_ia-expliquee_kimi-k3-agents-paralleles-retour_transcript.txt`

## 2. Qualification

- IA principale : Kimi K3.
- Sujets secondaires : Kimi Work, KimiClaw, skills, contexte long, Swarm, agents paralleles et comparaison Claude.
- Fiabilite : faible a moyenne ; retour pratique detaille, mais nombreuses annonces, prix, benchmarks et comparaisons non recoupes.
- Statut : A surveiller.

## 3. Resume synthetique

La video parcourt plusieurs interfaces Kimi, les permissions fichiers, le mode plan et l'execution multi-agents. Son apport principal est un retour negatif sur la coordination parallele : des agents affectes a plusieurs couches d'une application auraient produit des variables et conventions incompatibles faute de memoire partagee suffisante. L'auteur recommande un agent unique pour le coeur du projet et une parallelisation seulement apres cadrage.

## 4. Connaissances candidates

- Ne pas accorder l'acces complet aux fichiers avant d'avoir defini permissions, interdictions et plan.
- Inspecter les prompts transmis aux sous-agents et leur contexte partage.
- Paralleliser des composants seulement si interfaces, variables, proprietaires et criteres d'integration sont explicites.
- Mesurer la consommation multi-agents, les reprises et le taux d'integration reussie.

## 5. Limites et elements rejetes

- Taille, licence, contexte, tarifs, quotas, benchmarks et positionnement face a Claude non integres.
- Les comportements destructifs et limites de memoire ne sont pas reproduits independamment.
- Les denominations de modeles et fonctions doivent etre verifiees dans la documentation primaire.

## 6. Differences permanentes

- Aucune fiche permanente creee ou modifiee : les garde-fous multi-agents sont deja couverts par Agents IA et Orchestration IA.

## 7. Decision finale

- Statut final : A surveiller.
- Point ouvert : tester Kimi sur une tache multi-couches avec contrats d'interface, traces inter-agents et mesure de cout.
