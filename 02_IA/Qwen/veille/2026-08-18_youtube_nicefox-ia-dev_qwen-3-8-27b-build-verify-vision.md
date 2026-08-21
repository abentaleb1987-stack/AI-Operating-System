# 2026-08-18 - YouTube / Nicefox IA & Dev - Qwen 3.8 27B, Build and Verify et vision

## 1. Identification de la source

- Titre source : Qwen 3.8 27B sur 16 Go de VRAM : il a resolu le bug que DeepSeek V4 Flash a rate
- Source : YouTube - Nicefox IA & Dev
- Type : transcription d'une demonstration technique non officielle
- Date de publication indiquee : 2026-08-18
- Date de consultation : 2026-08-21
- Fichier source traite : `01_Collecte/sources_brutes/videos/traitees/2026-08-18_youtube_nicefox-ia-dev_qwen-3-8-27b-build-verify-vision_transcript.txt`

## 2. Qualification

- IA / outil principal : Qwen 3.8 27B.
- Outils secondaires : OpenFox, llama.cpp et DeepSeek V4 Flash.
- Domaine : inference locale, quantification, generation de code et verification visuelle.
- Fiabilite : moyenne pour la configuration et l'observation rapportee ; faible pour toute generalisation de performance.
- Priorite : moyenne.
- Statut : A surveiller.

## 3. Resume synthetique

L'auteur execute un quant Qwen 3.8 27B sur une carte graphique de 16 Go et lui confie la generation d'un mini-jeu dans un workflow Build and Verify. La session combine generation, revue de code, tests et captures visuelles. Selon la demonstration, la vision permet au modele de diagnostiquer puis corriger un artefact graphique qui persistait avec une configuration DeepSeek V4 Flash comparee.

## 4. Faits validables

- La source publie la commande llama.cpp utilisee, avec quantification du modele et du cache KV, projection multimodale, contexte annonce de 100 000 tokens et MTP.
- Elle decrit une trajectoire complete de 46 minutes avec generation, playtests, revue de code et correction d'un desequilibre entre operations de sauvegarde et de restauration du contexte graphique.
- Elle fournit des references vers les modeles, les quants, OpenFox et llama.cpp, mais le test n'a pas ete reproduit dans AOS.

## 5. Hypotheses, marketing et limites

- Un seul mini-jeu et une seule configuration ne permettent pas de conclure a la superiorite generale de Qwen sur DeepSeek.
- Le cout du materiel, le debit, la longueur de contexte utile et les performances dependent du quant, du backend et de la plateforme.
- La correction finale peut dependre de la vision, du harness, du niveau d'effort ou de la trajectoire de session ; le test n'isole pas ces variables.
- Les noms, versions et disponibilites des modeles doivent etre confirmes par leurs publications officielles.

## 6. Differences permanentes

- Aucune modification permanente : le workflow de verification est deja documente dans `Agents IA` et les performances du modele ne sont pas reproduites.
- Connaissance candidate : pour les livrables visuels, une boucle de verification doit observer le rendu et pas uniquement le code ou les tests textuels.

## 7. Decision finale

- Statut final : A surveiller.
- Elements rejetes : comparaison generale Qwen / DeepSeek, equivalence entre materiels et extrapolation des performances a d'autres taches.
- Prochaine action : reproduire le protocole avec versions epinglees, memes prompts, memes outils, plusieurs essais et mesures de qualite, latence et memoire.
