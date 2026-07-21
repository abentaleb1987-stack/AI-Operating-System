# 2026-07-21 - YouTube Mike Codeur - ADR et memoire agentique

## Identification et qualification

- Titre : Ton agent IA oublie tout : la solution des devs : les ADR
- Source : YouTube, transcription collectee le 2026-07-21
- IA principale : Agents IA
- Domaine : Documentation de decisions et continuite inter-session
- Niveau de fiabilite : Moyen (retour de praticien, sans demonstration reproductible fournie)
- Statut : Traitee - GO partiel

## Resume synthetique

La video propose d'utiliser des Architecture Decision Records, elargis ici en "Any Decision Records", pour conserver le contexte de decisions dans les projets assistes par agents. Le code montre le resultat courant mais pas toujours les contraintes, options ecartees et raisons du choix. Un registre consultable avant une nouvelle session peut limiter la re-proposition de solutions deja abandonnees.

## Faits et connaissances candidates

- Un ADR peut documenter le contexte, la decision, les options ecartees et les consequences.
- La persistance des decisions complete PRD, user stories et code dans un workflow agentique.
- Le benefice affirme pour les agents doit etre valide par un test AOS : consultation effective des ADR et reduction des reprises de decision.

## Decision de validation

- Valide : workflow de decisions persistantes dans la fiche Agents IA.
- A surveiller : format exact, automatisation de consultation et efficacite reelle dans AOS.
- Rejete : toute promesse implicite qu'un ADR seul rend un agent fiable.
