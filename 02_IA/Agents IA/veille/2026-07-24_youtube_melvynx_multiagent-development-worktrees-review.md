# 2026-07-24 - YouTube / Melvynx - Développement multi-agent, worktrees et revue

## 1. Identification de la source

- Titre : Lancer 10+ agents en même temps : mes méthodes pour ONE-SHOT tout
- Type : vidéo YouTube non officielle ; consultation le 2026-07-25.
- Fichier source : `01_Collecte/sources_brutes/videos/a_traiter/2026-07-24_youtube_codex_workflow_AOS_01.txt`

## 2. Détection et routage

- Sujet principal : agents de développement et orchestration multi-agent.
- IA secondaires : Codex, Claude, ChatGPT et Cursor cités comme outils.
- Fiabilité : moyenne ; retour d'expérience individuel.

## 3. Résumé synthétique

La vidéo décrit un mode de travail avec plusieurs agents en parallèle. Elle distingue les tâches à faible risque des environnements professionnels, où la capacité de revue et de validation demeure un facteur limitant. Elle présente les worktrees comme une isolation à réserver aux travaux importants et persistants, et propose un cycle exploration, planification, exécution, revue puis vérification. Les vérifications automatisées, y compris visuelles, sont présentées comme un moyen de rendre le parallélisme plus contrôlable.

## 4. Faits validables

- La parallélisation augmente le besoin de contrôle des changements et de tests reproductibles.
- Un worktree isole les modifications, mais son usage implique ensuite une stratégie explicite d'intégration.

## 5. Hypothèses et limites

- Les seuils d'agents simultanés et le niveau de revue nécessaire dépendent du contexte ; ils ne sont pas établis par la source.
- Les recommandations reposent sur un retour d'expérience et non sur une évaluation comparative contrôlée.

## 6. Validation

- Statut : GO partiel.
- Différences intégrées : aucune fiche permanente modifiée ; les principes recoupent les règles AOS existantes.
- Point à surveiller : mesurer les coûts, conflits et taux de défaut avant d'augmenter le parallélisme.
