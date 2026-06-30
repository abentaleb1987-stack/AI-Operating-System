# Codex GO Prompt

## Objectif

Declencher le workflow automatise AOS complet apres validation utilisateur.

## Prompt utilisateur recommande

```text
GO AOS

Traite les sources presentes dans :
01_Collecte/sources_brutes/{{type}}/a_traiter/

Execute le workflow complet :
Source brute -> Detection IA / outil / framework -> Routage -> Fiche de veille -> Validation -> Mise a jour fiche permanente -> Deplacement source traitee -> Git commit -> Git push -> Rapport final.

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
- Ne pas inventer d'information.
- En cas d'incertitude, creer la fiche de veille et conserver les informations en `A surveiller`.
- Ne pas enrichir une fiche permanente avec des informations faibles.
- Ne pas creer de commit vide.
- Produire un rapport final clair.
