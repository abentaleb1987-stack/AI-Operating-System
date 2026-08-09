# 2026-05-20 - YouTube / NetworkChuck - Hermes : memoire, skills et exploitation sur VPS

## 1. Identification de la source

- Titre : Vous devez utiliser Hermes DES MAINTENANT !! (adieu OpenClaw !!)
- Source : YouTube - NetworkChuck
- Type : transcription video non officielle, retour d'usage sponsorise
- Date de publication indiquee : 2026-05-20
- Date de consultation : 2026-08-09
- Fichier source traite : `01_Collecte/sources_brutes/videos/traitees/2026-08-04_youtube_networkchuck_hermes-memoire-skills-vps_transcript.txt`

## 2. Qualification

- IA principale : Hermes Agent.
- Sujets secondaires : VPS, Telegram, Honcho, memoire persistante, auto-creation de skills, Home Assistant et UniFi.
- Fiabilite : moyenne pour le retour d'usage ; faible pour les comparaisons de fiabilite et promesses d'auto-amelioration.
- Statut : A surveiller.

## 3. Resume synthetique

La source decrit l'installation de Hermes sur un VPS, le choix d'un provider, un canal Telegram et deux niveaux de memoire. Elle montre aussi un agent qui transforme des procedures repetees en skills et execute des taches d'administration. Le temoignage est utile pour reperer les composants a tester, mais ne constitue ni un audit de securite ni une validation de production.

## 4. Connaissances candidates

- Separer memoire de travail, resume de session et memoire longue inspectable.
- Ne transformer une procedure en skill qu'apres stabilisation, relecture et limitation des permissions.
- Isoler les integrations d'infrastructure et conserver logs, inventaire des acces et mecanisme d'arret.
- Evaluer la fiabilite sur un corpus de taches avec taux d'erreur et reprises, pas sur un temoignage.

## 5. Limites et elements rejetes

- Cout VPS, coupons, qualite comparee a OpenClaw et fiabilite dite absolue non retenus.
- Le fonctionnement exact d'Honcho, du curateur et de la regle de compression memoire reste a confirmer.
- Les demonstrations Home Assistant et UniFi exposent un risque eleve si les droits ne sont pas bornes.

## 6. Differences permanentes

- Aucune difference integree : memoire, VPS, skills, permissions, logs et supervision sont deja couverts par la fiche Hermes.

## 7. Decision finale

- Statut final : A surveiller.
- Point ouvert : tester la memoire et la creation de skills en environnement isole avec traces et permissions minimales.
