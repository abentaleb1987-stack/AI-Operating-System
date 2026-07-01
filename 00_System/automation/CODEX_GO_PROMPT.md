# Codex GO Prompt

## Objectif

Declencher le workflow automatise AOS complet apres validation utilisateur.

## Prompt utilisateur recommande

```text
GO AOS

Traite les sources presentes dans :
01_Collecte/sources_brutes/{{type}}/a_traiter/

Pour les videos, scanne :
01_Collecte/sources_brutes/videos/a_traiter/

Execute le workflow complet :
Source brute -> Detection IA / outil / framework -> Routage -> Fiche de veille -> Validation -> Mise a jour fiche permanente -> Deplacement source traitee -> Git commit -> Git push -> Rapport final.

Si plusieurs fichiers sont presents, traite tout le batch automatiquement, source par source, sans intervention intermediaire.

Respecte :
- 00_System/automation/AOS_PROCESS.md
- 00_System/automation/AOS_ROUTING_RULES.md
- 00_System/automation/AOS_GIT_RULES.md
- les Frameworks AOS
- les Standards AOS
- les Templates AOS

Ne demande pas d'intervention intermediaire sauf blocage critique.
Termine par le rapport final complet.
```

## Regles pour Codex

- Executer jusqu'au push GitHub si le traitement produit des modifications utiles.
- Scanner tous les fichiers presents dans les dossiers `a_traiter/`.
- Traiter les sources une par une.
- Ne pas demander d'intervention intermediaire sauf blocage critique.
- Ne pas inventer d'information.
- En cas d'incertitude, creer la fiche de veille et conserver les informations en `A surveiller`.
- Ne pas enrichir une fiche permanente avec des informations faibles.
- Ne pas creer de commit vide.
- Pour un batch, creer un seul commit global, jamais un commit par source.
- Utiliser `docs(aos): process video source batch` pour un batch video simple.
- Utiliser `docs(aos): integrate multi-source AI watch batch` si plusieurs categories ou plusieurs IA sont traitees.
- Si une source echoue sans risque critique, ne pas la deplacer vers `traitees/`, continuer les autres sources et mentionner l'echec dans le rapport consolide.
- Si une erreur critique apparait, arreter le batch, ne pas commit, ne pas push, et produire un rapport de blocage.
- A la fin du batch, executer `git status --short`, `git add .`, un seul commit global, `git push origin main`, puis `git status --short`.
- Produire un rapport final consolide clair.

## Rapport consolide obligatoire

Le rapport final d'un batch doit contenir :

- nombre de sources detectees ;
- nombre de sources traitees ;
- nombre de sources echouees ;
- liste des IA principales detectees ;
- detail par source ;
- fiches de veille creees ;
- fiches permanentes modifiees ;
- sections modifiees ;
- sources deplacees ;
- connaissances integrees ;
- connaissances non integrees ;
- points a surveiller consolides ;
- commit cree ;
- resultat du push ;
- resultat final de `git status --short` ;
- decision finale batch.
