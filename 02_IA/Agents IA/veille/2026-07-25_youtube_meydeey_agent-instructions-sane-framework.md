# 2026-07-25 - YouTube / Meydeey - Accumulation d'instructions et framework S.A.N.E.

## 1. Identification de la source

- Titre : Tes règles SABOTENT Claude Code, Codex et Gemini
- Publication indiquée : 2026-07-16 ; vidéo non officielle.
- Fichier source : `01_Collecte/sources_brutes/videos/a_traiter/2026-07-25_youtube_codex_workflow_AOS_07.txt`

## 2. Détection et routage

- Sujet principal : conception d'instructions pour agents ; Claude Code, Codex et Gemini sont des exemples.
- Fiabilité : moyenne ; framework et seuils proposés par l'auteur.

## 3. Résumé synthétique

La source soutient que l'ajout successif de règles, exceptions et négations peut dégrader l'exécution d'un agent. Elle propose le framework S.A.N.E. pour examiner l'utilité de chaque instruction et recommande de retirer les règles qui ne changent pas une décision observable. L'enjeu avancé est de réduire la charge de configuration et de conserver des instructions actionnables.

## 4. Faits validables

- Chaque instruction devrait avoir une intention, un déclencheur et un résultat vérifiable.
- Les instructions doivent être révisées à partir de cas d'échec et d'évaluations, non accumulées sans contrôle.

## 5. Limites

- Le seuil de complexité et le framework S.A.N.E. ne sont pas validés scientifiquement par cette vidéo.

## 6. Validation

- Statut : GO partiel.
- Différences intégrées : aucune ; le dépôt applique déjà une documentation ciblée et des contrôles de workflow.
- Point à surveiller : auditer périodiquement les règles locales contre des scénarios réels.
