# Cursor - Fiche permanente

## 1. Fiche d'identite

- Nom : Cursor
- Type : IDE assiste par IA / environnement de developpement agentique
- Statut dans la base : En veille / En test
- Derniere mise a jour : 2026-07-08

## 2. Role principal

Cursor est a evaluer comme environnement de production logicielle assiste par IA, combinant edition de code, agents, choix de modeles, outils projet et consommation de quotas.

Dans AOS, son interet principal est la generation et la modification de projets avec controle du cout, de la qualite, de la robustesse et de la maintenabilite.

## 3. Architecture

- Cursor expose plusieurs modes ou modeles de travail, dont un modele proprietaire appele Composer selon les sources observees.
- Les modeles peuvent avoir des profils de cout, vitesse, qualite visuelle, raisonnement et consommation de tokens tres differents.
- Les tests en IDE doivent etre evalues sur un repository reel, avec contexte, fichiers, dependances, serveur local, erreurs et validations visibles.
- Les MCP ou integrations projet peuvent influencer les recommandations d'architecture du modele ; leur presence doit etre documentee lors d'un benchmark.

## 4. Forces

- Peut accelerer la generation de prototypes, pages, jeux simples, composants et plans techniques.
- Permet de comparer plusieurs modeles sur un meme environnement de developpement.
- Les modeles moins couteux peuvent etre suffisants pour des iterations courtes si le cadrage est strict et les tests rapides.

## 5. Faiblesses

- Le meilleur resultat visible ne correspond pas toujours au meilleur rapport cout / valeur.
- Les modeles premium peuvent consommer fortement les quotas sur des taches longues, des plans et des corrections successives.
- Les benchmarks video ou communautaires sont sensibles aux prompts, assets, contexte projet, versions, quotas et preferences subjectives.
- Les modeles rapides ou economiques peuvent produire des livrables moins finis, moins robustes ou moins attentifs aux details de contexte.

## 6. Cas d'usage valides

Aucun cas d'usage n'est encore valide par experimentation interne AOS.

## 7. Cas d'usage a eviter

- Choisir un modele uniquement sur une demonstration non officielle.
- Lancer une construction large avec un modele premium sans budget, criteres d'arret et verification intermediaire.
- Confondre cout nominal par token, consommation de quota Cursor et cout complet par tache terminee.

## 8. Workflows recommandes

Workflow de comparaison de modeles dans Cursor :

1. Definir une tache representative AOS avec criteres d'acceptation.
2. Lancer chaque modele sur le meme contexte et les memes assets.
3. Mesurer tokens, temps, cout ou pourcentage de quota consomme.
4. Evaluer resultat visible, bugs, robustesse, respect des consignes, maintenabilite et besoin de reprises.
5. Calculer le cout par livrable acceptable, pas seulement le cout par prompt.
6. Reserver le modele premium aux taches ou son gain marginal est visible, utile et reproductible.

Workflow de selection pragmatique :

1. Utiliser un modele economique ou rapide pour exploration, prototype et modifications bornees.
2. Monter vers un modele plus fort pour architecture critique, debogage difficile, UX exigeante ou revue finale.
3. Revenir a un modele moins couteux pour les iterations mecaniques apres stabilisation du plan.

## 9. Prompts & methodes

- Preciser la feature, le niveau de finition attendu, les contraintes techniques, les fichiers concernes et les tests disponibles.
- Demander un plan avant build lorsque la tache peut exploser en scope, cout ou complexite.
- Exiger une verification locale du rendu, des erreurs et des tests lorsque le livrable est applicatif.
- Pour les prototypes visuels, fournir assets et criteres de design plutot que laisser le modele inventer toute la direction.

## 10. Integration dans mon ecosysteme

Cursor est a tester pour :

- prototypes applicatifs rapides ;
- modifications de code avec contexte projet ;
- comparaison de modeles de code selon cout et qualite ;
- generation de plans techniques avant implementation ;
- workflows ou le controle humain reste dans l'IDE.

## 11. Orchestration IA

Cursor peut servir de surface d'execution code dans une orchestration plus large, mais ne doit pas etre confondu avec l'orchestrateur strategique AOS.

Les decisions de modele doivent etre externalisees dans des regles de routage : modele economique pour iteration, modele premium pour arbitrage complexe, revue ou finition critique.

## 12. Evolutions

Points a surveiller :

- evolution officielle de Composer, de ses versions et de son pricing ;
- ecart reel entre Composer, modeles Anthropic, OpenAI et autres modeles dans Cursor ;
- impact des quotas mensuels sur les workflows longs ;
- qualite des plans d'architecture selon presence de MCP, contexte projet et stack deja installee ;
- robustesse des livrables UI : responsive, chargement, layout shifts, accessibilite, erreurs runtime ;
- cout complet d'un livrable acceptable incluant prompts, corrections, recherches, rebuilds et revue humaine.

## 13. Decisions strategiques

Ne pas adopter un modele Cursor comme choix par defaut sans benchmark AOS comparant qualite, cout complet, robustesse et reproductibilite.

Le modele le plus cher doit etre reserve aux taches ou son gain marginal compense clairement le cout et les quotas consommes.

## Historique des mises a jour

- 2026-07-08 - Ajout - Sections 1 a 13 - Source YouTube DevArt Composer 2.5 vs Claude Opus, batch AOS GO partiel
