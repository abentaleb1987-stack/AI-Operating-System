# TestSprite - Fiche permanente

## 1. Fiche d'identite

- Nom : TestSprite
- Type : Outil de test automatise et verification agentique a evaluer
- Statut dans la base : En veille
- Derniere mise a jour : 2026-07-01

## 2. Role principal

TestSprite est a evaluer comme outil de verification de workflows applicatifs modifies ou crees par agents IA, avec preuves visuelles, logs d'etapes et execution sur environnements cibles.

## 3. Architecture

Elements observes dans un segment sponsorise Melvynx du 2026-06-30, a confirmer :

- configuration par cle API ;
- commande de setup projet ;
- creation de scenarios de test depuis un agent de code ;
- execution sur environnement cible ;
- preuves par screenshots ou video ;
- inspection des etapes pour debogage.

## 4. Forces

- Peut repondre au besoin de verification des changements produits par agents IA.
- Les preuves visuelles peuvent aider a auditer un workflow UI.
- Les comptes de test et environnements separes sont compatibles avec une approche prudente.

## 5. Faiblesses

- Source initiale sponsorisee, donc aucune validation operationnelle.
- Risque de faux sentiment de securite si la "correctness" n'est pas definie par criteres explicites.
- Necessite une revue securite avant usage avec credentials ou environnements reels.

## 6. Cas d'usage valides

Aucun cas d'usage n'est encore valide par experimentation interne AOS.

## 7. Cas d'usage a eviter

- Lancer TestSprite sur production sans compte de test ni limites.
- Donner des credentials sensibles a un agent de test non audite.
- Remplacer les tests unitaires, integration ou E2E existants par une verification IA non controlee.

## 8. Workflows recommandes

Workflow de qualification :

1. Lire la documentation officielle.
2. Creer un environnement de test isole.
3. Fournir un compte de test a droits limites.
4. Definir le workflow et les criteres de succes.
5. Collecter screenshots, video et logs.
6. Comparer avec une verification manuelle.
7. Decider seulement apres plusieurs executions reproductibles.

## 9. Prompts & methodes

Pour tester avec un agent :

- decrire le workflow utilisateur ;
- definir l'etat initial ;
- definir les donnees de test ;
- interdire les actions hors scope ;
- exiger preuves visuelles et logs ;
- demander un diagnostic par etape en cas d'echec.

## 10. Integration dans mon ecosysteme

TestSprite n'est pas integre dans AOS. Il reste une piste de veille pour verifier les livrables produits par agents IA.

## 11. Orchestration IA

TestSprite pourrait jouer un role de validateur externe dans une orchestration IA, mais uniquement si ses actions, credentials, environnements et criteres d'acceptation sont bornes.

## 12. Evolutions

Points a surveiller :

- documentation officielle et modele de securite ;
- integrations avec agents de code ;
- qualite des preuves visuelles ;
- taux de faux positifs et faux negatifs ;
- cout d'execution sur workflows recurrents.

## 13. Decisions strategiques

Ne pas adopter TestSprite sur la base d'un segment sponsorise. L'outil doit etre recoupe, teste en environnement isole et compare aux tests E2E existants.

## Historique des mises a jour

- 2026-07-01 - Ajout - Sections 1 a 13 - Source YouTube Melvynx TestSprite, batch AOS GO partiel
