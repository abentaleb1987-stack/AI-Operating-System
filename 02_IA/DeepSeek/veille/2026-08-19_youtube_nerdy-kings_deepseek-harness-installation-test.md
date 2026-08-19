# 2026-08-19 - YouTube / Nerdy Kings - DeepSeek Harness, installation et test

## 1. Identification de la source

- Titre source : DeepSeek Harness : La Fin de Claude Code ? (Installation + Test)
- Source : YouTube - Nerdy Kings
- Reference officielle recoupee : `https://github.com/deepseek-ai/deepseek-harness`
- Type : transcription d'une video de presentation et demonstration non officielle
- Date de publication indiquee : 2026-08-19
- Date de consultation : 2026-08-19
- Fichier source traite : `01_Collecte/sources_brutes/videos/traitees/2026-08-19_youtube_nerdy-kings_deepseek-harness-installation-test_transcript.txt`

## 2. Qualification

- IA / outil principal : DeepSeek Harness.
- Outils secondaires : Cordis, Node.js et Claude Code comme point de comparaison.
- Domaine : runtime d'agents, plugins, permissions, sessions, outils et developpement assiste.
- Fiabilite : elevee pour les caracteristiques recoupees dans le depot officiel ; moyenne pour la demonstration et les comparaisons.
- Priorite : haute.
- Statut : GO partiel.

## 3. Resume synthetique

La video distingue le modele du harness qui gere contexte, outils, permissions, sessions et boucle agentique. DeepSeek Harness applique une architecture ou les composants sont des plugins, appuyee sur Cordis. La demonstration installe l'interface web, parcourt plusieurs modes et cree un plugin visuel en Creator Mode. L'auteur conclut que le projet offre plus de controle qu'un produit integre, mais ne remplace pas encore un outil mature.

## 4. Faits validables

- Le depot officiel presente DeepSeek Harness comme un agent harness open source developpe par DeepSeek AI.
- L'architecture « everything is a plugin » et l'usage de Cordis sont confirmes par le README officiel.
- Le projet est distribue sous licence MIT.
- Le depot officiel le classe en developer preview et avertit de changements incompatibles.
- L'interface web peut etre lancee avec `npx @deepseek-ai/dsh web` selon le README officiel.

## 5. Hypotheses, marketing et limites

- La creation reussie d'un plugin d'horloge est une demonstration, pas un test de robustesse.
- Les modes, limites de sandbox et comportements de securite doivent etre controles sur la version exacte testee.
- La comparaison avec Claude Code ne constitue pas un benchmark reproductible.
- Une architecture tres extensible agrandit aussi la surface d'audit des plugins, permissions et dependances.

## 6. Differences permanentes

- Creation de `02_IA/DeepSeek/fiche_permanente.md` avec l'identite du projet, son architecture plugin, son statut de preview et un workflow d'evaluation prudent.
- Aucun cas d'usage valide n'est ajoute avant experimentation interne AOS.

## 7. Decision finale

- Statut final : GO partiel.
- Elements rejetes : affirmation de remplacement de Claude Code, niveau de securite et benefices de performance non mesures.
- Prochaine action : tester une version epinglee sur un depot jetable avec plugins audites, preuves de verification et journal des permissions.
