# 2026-07-21 - YouTube Projets IA - GPU et inference LLM

## Identification et qualification

- Titre : Pourquoi l'IA tourne sur des GPU et pas des CPU
- Source : YouTube, transcription collectee le 2026-07-21
- IA principale : Agents IA (infrastructure de calcul)
- Domaine : Materiel et performance d'inference
- Niveau de fiabilite : Moyen (vulgarisation citant NVIDIA et litterature)
- Statut : Traitee - A surveiller

## Resume synthetique

La video oppose le parallelisme massif et la bande passante memoire des GPU a la faible parallelisation des CPU pour les calculs de reseaux neuronaux. Elle distingue aussi le prefill, souvent limite par le calcul, de la generation token par token, souvent sensible a la bande passante memoire. Les chiffres et caracteristiques de materiel sont dependants des modeles et doivent etre verifies avant dimensionnement.

## Elements conserves en veille

- Pour un LLM, le cout et la latence dependent du calcul, de la memoire et de la bande passante, pas seulement du nombre de coeurs.
- Le choix d'infrastructure doit etre evalue sur une charge representative incluant prefill et generation.
- Les specifications et performances annoncees ne sont pas integrees sans documentation officielle et mesure interne.
