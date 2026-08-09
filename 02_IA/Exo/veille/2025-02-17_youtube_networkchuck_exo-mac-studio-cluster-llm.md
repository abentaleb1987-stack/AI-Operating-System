# 2025-02-17 - YouTube / NetworkChuck - Exo et cluster Mac Studio pour LLM local

## 1. Identification de la source

- Titre : J'ai construit un supercalculateur IA avec 5 Mac Studios
- Source : YouTube - NetworkChuck
- Type : transcription video, demonstration technique non officielle avec sponsor
- Date de publication indiquee : 2025-02-17
- Date de consultation : 2026-08-09
- Fichier source traite : `01_Collecte/sources_brutes/videos/traitees/2026-08-04_youtube_networkchuck_exo-cluster-mac-studio-llm_transcript.txt`

## 2. Qualification

- Outil principal : Exo.
- Sujets secondaires : Llama 3.1 405B, quantification, memoire unifiee Apple et inference distribuee.
- Fiabilite : moyenne pour l'experience montree ; faible pour les comparaisons de cout et performance.
- Statut : A surveiller.

## 3. Resume synthetique

La video assemble cinq Mac Studio avec Exo afin de repartir un modele trop volumineux pour une seule machine. Elle distingue utilement capacite memoire et vitesse : distribuer les couches peut rendre un grand modele executable sans necessairement accelerer une requete, le reseau et le passage sequentiel entre noeuds devenant des limites majeures.

## 4. Connaissances candidates

- Evaluer separement la capacite a charger un modele, la latence, le debit multi-requetes et la consommation.
- La memoire cumulee d'un cluster ne garantit pas une acceleration lineaire.
- La quantification reduit les besoins memoire au prix d'un compromis de precision a mesurer.
- Les interconnexions doivent etre comparees dans des unites coherentes et testees en conditions reelles.

## 5. Limites et elements rejetes

- Configuration beta, protocole incomplet et absence de benchmark reproductible.
- Prix, equivalences avec serveurs GPU et qualite du modele quantifie non integres.
- La demonstration ne valide pas Exo pour un usage AOS en production.

## 6. Differences permanentes

- Aucune fiche permanente creee : l'outil et ses limites doivent d'abord etre verifies par documentation primaire et test local.

## 7. Decision finale

- Statut final : A surveiller.
- Point ouvert : mesurer modele, quantification, topologie, latence, debit, memoire et consommation sur un protocole stable.
