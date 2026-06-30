# AOS Git Rules

## Objectif

Definir les regles Git applicables au workflow automatise AOS execute par Codex.

## Cycle Git obligatoire

Apres un traitement utile, Codex execute :

```text
git status --short
git add .
git commit -m "{{message adapte}}"
git push
git status --short
```

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

## Regles

- Ne pas creer de commit vide.
- Ne pas melanger plusieurs cycles de sources sans raison.
- Inclure dans le meme commit la source traitee, la fiche de veille, la fiche permanente modifiee et le deplacement vers `traitees/`.
- Verifier le statut Git avant et apres le push.
- Signaler le hash du commit dans le rapport final.
- Signaler explicitement si le push echoue.

## Prudence

Codex ne doit pas utiliser de commande destructive.

Codex ne doit pas revert des modifications utilisateur sans demande explicite.
