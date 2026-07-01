# Aside - Fiche permanente

## 1. Fiche d'identite

- Nom : Aside
- Type : Navigateur avec assistant IA et fonctions agentiques a evaluer
- Statut dans la base : En veille
- Derniere mise a jour : 2026-07-01

## 2. Role principal

Aside est a evaluer comme navigateur agentique capable d'assister la navigation, de piloter des tabs et de tenter des actions web sous controle utilisateur.

## 3. Architecture

Elements observes dans la video Melvynx du 2026-06-30, a confirmer par documentation officielle :

- interface de navigation avec sidebar et chat IA ;
- modes ou options local/cloud ;
- connexion possible a des comptes ou abonnements existants ;
- integration possible avec un password manager ;
- mecanisme de confirmation finale pour certaines actions sensibles.

## 4. Forces

- Peut centraliser navigation, chat IA et tabs dans une meme interface.
- Peut rendre visibles certaines actions d'agent dans le navigateur.
- Peut etre utile pour explorer les limites des agents web grand public.

## 5. Faiblesses

- Lenteur observee sur workflows authentifies dans la source.
- Fragilite possible lors des connexions, OTP et reprises de controle.
- Risque eleve si l'agent accede a emails, comptes, achats ou secrets sans limites claires.

## 6. Cas d'usage valides

Aucun cas d'usage n'est encore valide par experimentation interne AOS.

## 7. Cas d'usage a eviter

- Utiliser Aside sur des donnees sensibles sans confirmation humaine explicite.
- Laisser l'agent agir sur emails, achats, formulaires ou comptes sans logs et limites.
- Connecter un password manager avant audit du modele de securite.
- Remplacer une automatisation directe fiable par un agent navigateur non teste.

## 8. Workflows recommandes

Workflow de test prudent :

1. Utiliser un profil de test separe.
2. Desactiver les comptes sensibles.
3. Choisir une tache courte, reversible et non critique.
4. Activer confirmation finale pour toute action externe.
5. Mesurer temps, succes, reprise de controle et traces.
6. Ne pas conserver l'outil si le workflow echoue sans diagnostic clair.

## 9. Prompts & methodes

Pour un navigateur agentique, specifier :

- site cible ;
- action attendue ;
- interdictions ;
- criteres d'arret ;
- besoin de confirmation avant soumission, achat, suppression ou envoi ;
- format du rapport d'execution.

## 10. Integration dans mon ecosysteme

Aside n'est pas integre dans AOS. Il reste un outil de veille sur les interfaces navigateur-agent.

## 11. Orchestration IA

Aside peut etre considere comme un agent d'execution web uniquement si un orchestrateur externe ou l'utilisateur conserve la validation finale et les limites d'action.

## 12. Evolutions

Points a surveiller :

- maturite des agents navigateur ;
- securite des connexions et password managers ;
- qualite des logs d'action ;
- latence sur workflows web ;
- mode local/cloud et confidentialite.

## 13. Decisions strategiques

Ne pas utiliser Aside pour des workflows AOS sensibles tant qu'un test interne, un audit de securite et une documentation claire des permissions ne sont pas disponibles.

## Historique des mises a jour

- 2026-07-01 - Ajout - Sections 1 a 13 - Source YouTube Melvynx Aside, batch AOS GO partiel
