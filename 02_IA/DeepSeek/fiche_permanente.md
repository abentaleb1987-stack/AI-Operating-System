# DeepSeek / DeepSeek Harness - Fiche permanente

## 1. Fiche d'identite

- Nom : DeepSeek / DeepSeek Harness
- Type : famille de modeles et runtime open source pour agents IA
- Editeur ou origine : DeepSeek AI
- Site officiel : `https://deepseek.com/`
- Depot officiel Harness : `https://github.com/deepseek-ai/deepseek-harness`
- Statut dans la base : En veille / En test
- Niveau de maturite du Harness : Developer preview
- Derniere mise a jour : 2026-08-19

## 2. Role principal

DeepSeek Harness est a evaluer comme couche d'execution et de composition d'agents, distincte du modele de raisonnement. Il assemble les composants necessaires pour donner au modele des outils, un contexte, des permissions, des sessions et une boucle d'action.

## 3. Architecture

Elements confirmes par le depot officiel :

- projet open source sous licence MIT ;
- architecture ou les composants sont concus comme des plugins ;
- utilisation de Cordis comme socle de composition ;
- interface web locale lancee par le CLI `dsh` ;
- projet encore en developer preview avec changements incompatibles annonces.

La separation a retenir pour l'evaluation AOS est : modele de raisonnement, harness d'orchestration, puis environnement d'execution et services accessibles.

## 4. Forces

- Modularite permettant d'evaluer ou de remplacer des composants sans confondre le modele avec toute la couche agentique.
- Code et licence permettant l'inspection du runtime.
- Potentiel de tracabilite des sessions, appels d'outils et permissions a confirmer par test interne.

## 5. Faiblesses

- Preview instable avec risque explicite de rupture de compatibilite.
- Surface d'audit importante lorsque outils, permissions, boucles, interfaces et dependances deviennent extensibles.
- Maturite, isolation et maintenabilite non validees dans AOS.

## 6. Cas d'usage valides

Aucun cas d'usage n'est encore valide par experimentation interne AOS.

## 7. Cas d'usage a eviter

- Deploiement en production sur une version non epinglee.
- Installation de plugins non audites ou execution avec des permissions larges.
- Utilisation sur secrets, donnees sensibles ou depots critiques sans isolation verifiee.
- Conclusion sur la qualite d'un modele a partir du seul comportement du harness.

## 8. Workflows recommandes

Workflow d'evaluation AOS :

1. Epingler une version ou un commit du projet.
2. Utiliser un depot jetable sans secret et un environnement isole.
3. Inventorier les plugins, dependances, outils, acces reseau et permissions actifs.
4. Definir un jeu de taches et des criteres identiques pour chaque modele ou configuration comparee.
5. Conserver les logs, appels d'outils, diffs, erreurs, couts et temps de reprise.
6. Tester les refus, limites de permission, interruption, reprise et retrait d'un plugin.
7. Ne promouvoir un usage qu'apres revue humaine et reproduction du test.

## 9. Prompts & methodes

- Separer les criteres portant sur le modele de ceux portant sur le harness.
- Declarer explicitement outils autorises, chemins, permissions, preuves de succes et conditions d'arret.
- Exiger un rapport de trajectoire et un diff final avant validation.

## 10. Integration dans mon ecosysteme

DeepSeek Harness peut etre teste comme banc d'evaluation de runtimes et de modeles, sans remplacer les workflows AOS existants tant que sa stabilite, sa securite et sa maintenance ne sont pas mesurees.

## 11. Orchestration IA

Son architecture plugin peut servir a etudier la portabilite des modeles, outils et boucles d'agents. L'orchestrateur AOS doit toutefois conserver le routage, les controles critiques et la decision finale.

## 12. Evolutions

Points a surveiller :

- stabilisation des API et apparition de versions publiees ;
- qualite de l'isolation fichiers, reseau et processus ;
- exhaustivite et export des trajectoires de session ;
- securite, provenance et compatibilite des plugins ;
- portabilite reelle entre fournisseurs de modeles ;
- cout de maintenance lors des changements incompatibles.

## 13. Decisions strategiques

- 2026-08-19 - Autoriser une evaluation isolee de DeepSeek Harness ; ne pas l'adopter en production tant que la preview, les permissions, l'isolation et la maintenance ne sont pas validees par un test AOS reproductible.

## Historique des mises a jour

- 2026-08-19 - Creation - Sections 1 a 13 - Depot officiel DeepSeek Harness et deux sources YouTube de demonstration, batch AOS GO partiel.
