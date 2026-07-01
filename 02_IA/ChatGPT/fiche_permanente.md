# ChatGPT - Fiche permanente

## 1. Fiche d'identite

- Nom : ChatGPT / GPT
- Type : Assistant IA et famille de modeles a evaluer
- Statut dans la base : En veille
- Derniere mise a jour : 2026-07-01

## 2. Role principal

ChatGPT est a evaluer comme interface et moteur de modeles GPT pour assistance, code, recherche, synthese et orchestration sous controle utilisateur.

## 3. Architecture

Elements a confirmer par documentation officielle avant integration durable :

- interface conversationnelle ;
- acces a plusieurs modeles ou modes selon abonnement et disponibilite ;
- fonctions possibles d'outils, recherche, code ou agents selon contexte ;
- system cards et restrictions d'usage a lire pour les modeles sensibles.

## 4. Forces

- Peut servir de modele generaliste fort lorsque la qualite, la vitesse et la disponibilite sont au rendez-vous.
- Peut reduire le besoin d'orchestration complexe si un modele unique resout correctement la tache.

## 5. Faiblesses

- Disponibilite, limites, noms de modeles et conditions d'acces peuvent changer rapidement.
- Les claims de performance issus de videos, tweets ou benchmarks isoles ne doivent pas etre integres sans recoupement.

## 6. Cas d'usage valides

Aucun cas d'usage n'est encore valide par experimentation interne AOS.

## 7. Cas d'usage a eviter

- Choisir un modele uniquement sur la base d'une annonce non officielle ou d'un benchmark isole.
- Integrer des donnees sensibles sans verifier confidentialite, politique de donnees et mode d'execution.

## 8. Workflows recommandes

Workflow de veille modele :

1. Identifier le modele et sa disponibilite officielle.
2. Lire la documentation et la system card.
3. Verifier cout, limites, region et conditions d'acces.
4. Tester sur une tache AOS reproductible.
5. Comparer qualite, temps, cout et taux de retry.
6. Integrer seulement les resultats stables.

## 9. Prompts & methodes

Pour ChatGPT/GPT, expliciter :

- objectif ;
- sources autorisees ;
- niveau de verification attendu ;
- format de sortie ;
- incertitudes a conserver en veille ;
- interdictions sur donnees sensibles.

## 10. Integration dans mon ecosysteme

ChatGPT peut etre utilise dans AOS pour assistance generale, analyse de sources, generation de syntheses et comparaison de workflows, sous reserve de verification et de tracabilite.

## 11. Orchestration IA

ChatGPT/GPT peut jouer un role de modele principal ou de sous-agent selon le cout, la disponibilite, la qualite attendue et les permissions disponibles.

## 12. Evolutions

Points a surveiller :

- disponibilite officielle des nouveaux modeles ;
- system cards, evaluations de securite et restrictions ;
- cout par tache complete, pas seulement prix par token ;
- strategie multi-fournisseurs si l'acces aux meilleurs modeles devient instable ;
- comparaison avec modeles open-weight ou routeurs multi-modeles.

## 13. Decisions strategiques

Ne pas integrer dans AOS des noms, benchmarks ou performances de modeles GPT non confirmes par sources officielles ou tests internes reproductibles.

## Historique des mises a jour

- 2026-07-01 - Ajout - Sections 1 a 13 - Source YouTube Melvynx GPT 5.6, batch AOS GO partiel
