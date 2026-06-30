# AOS Routing Rules

## Objectif

Definir comment Codex detecte le sujet d'une source brute et la route vers les bons dossiers AOS.

## Principe

Le dossier d'entree ne determine jamais le classement final.

`01_Collecte/sources_brutes/` est une zone neutre. Le classement durable se fait dans `02_IA/`.

## Detection

Codex doit analyser le contenu de la source pour identifier :

- IA principale ;
- IA secondaires ;
- outil IA ;
- framework IA ;
- type de source ;
- sujet principal ;
- sujets secondaires ;
- niveau de fiabilite ;
- statut final attendu.

## Routage vers la veille

Une fiche de veille doit etre creee dans :

```text
02_IA/{{IA ou sujet principal}}/veille/
```

Regles :

- une fiche de veille reste centree sur une IA, un outil ou un framework ;
- une source multi-sujets peut produire plusieurs fiches de veille ;
- les informations transversales doivent etre classees dans le dossier transversal approprie uniquement si elles depassent clairement une IA unique ;
- en cas d'incertitude de routage, creer la fiche de veille avec statut `A surveiller` et ne pas enrichir la fiche permanente.

## Routage des sources traitees

Apres traitement, Codex deplace la source brute vers le dossier `traitees/` correspondant a son type :

- `videos/traitees/`
- `articles/traitees/`
- `docs/traitees/`
- `tests_personnels/traitees/`

## Interdictions

- Ne pas classer une source uniquement d'apres son nom de fichier.
- Ne pas creer une nouvelle IA si un dossier existant correspond clairement.
- Ne pas fusionner plusieurs IA dans une fiche de veille unique si elles sont traitees substantiellement.
- Ne pas enrichir une fiche permanente avec une information incertaine.
