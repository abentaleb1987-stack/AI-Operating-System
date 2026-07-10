# AOS Git Rules

## Objectif

Definir les regles Git applicables au workflow automatise AOS execute par Codex.

## Cycle Git obligatoire

Apres un traitement utile, Codex execute :

```text
git status --short
git add .
git commit -m "{{message adapte}}"
git push origin main
git status --short
```

Dans un `GO AOS`, ce cycle Git fait partie des operations standards preautorisees.

Codex ne doit pas redemander confirmation pour `git status --short`, `git add`, `git commit` ou `git push origin main` lorsque ces commandes correspondent aux fichiers modifies par le workflow AOS en cours.

Cette preautorisation est une autorisation metier AOS. Elle ne peut pas supprimer une confirmation technique imposee par le mode d'execution local de Codex. Lorsque l'interface le permet, l'utilisateur peut autoriser sans redemande les familles `git status`, `git diff`, `git add`, `git commit`, `git push`, `git log` et `git rev-parse` pour ce depot.

Codex doit regrouper les operations Git standards dans une seule phase de fin de workflow et eviter de disperser plusieurs cycles `git add` / `git commit` / `git push`.

## Message de commit

Le message de commit doit etre court, explicite et adapte au sujet detecte.

Format recommande :

```text
docs(aos): {{action}} {{sujet}}
```

Exemples :

- `docs(aos): integrate Hermes source analysis`
- `docs(aos): update Codex permanent knowledge`
- `docs(aos): add MCP source watch note`
- `docs(aos): process video source batch`
- `docs(aos): integrate multi-source AI watch batch`

## Regles

- Ne pas creer de commit vide.
- Ne pas melanger plusieurs cycles de sources sans raison.
- Inclure dans le meme commit la source traitee, la fiche de veille, la fiche permanente modifiee et le deplacement vers `traitees/`.
- Verifier le statut Git avant et apres le push.
- Signaler le hash du commit dans le rapport final.
- Signaler explicitement si le push echoue.

## Regles batch

Un batch declenche par un seul `GO AOS` doit produire un seul commit global.

Codex ne doit pas creer un commit par source.

Pour un batch video simple, le message recommande est :

```text
docs(aos): process video source batch
```

Si plusieurs categories, IA, outils ou frameworks sont traites dans le meme batch, le message recommande est :

```text
docs(aos): integrate multi-source AI watch batch
```

Le cycle Git de fin de batch est :

```text
git status --short
git add .
git commit -m "{{message batch adapte}}"
git push origin main
git status --short
```

Si une erreur critique apparait pendant le batch, Codex doit arreter le traitement, ne pas creer de commit, ne pas pousser, et produire un rapport de blocage.

## Prudence

Codex ne doit pas utiliser de commande destructive.

Codex ne doit pas revert des modifications utilisateur sans demande explicite.

Les operations Git suivantes restent hors perimetre standard et necessitent une confirmation explicite :

- rollback Git ;
- `git reset --hard` ;
- `git clean` ;
- force push ;
- resolution d'un conflit Git non trivial ;
- revert de modifications utilisateur ;
- toute operation presentant un risque de perte de donnees.
