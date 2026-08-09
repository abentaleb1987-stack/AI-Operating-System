# 2025-10-28 - YouTube / NetworkChuck - Terminal IA, contexte local et coordination multi-outils

## 1. Identification de la source

- Titre : Vous utilisez l'IA de la mauvaise maniere (utilisez plutot ceci)
- Source : YouTube - NetworkChuck
- Type : transcription video, tutoriel non officiel avec segment sponsorise
- Date de publication indiquee : 2025-10-28
- Date de consultation : 2026-08-09
- Fichier source traite : `01_Collecte/sources_brutes/videos/traitees/2026-08-04_youtube_networkchuck_terminal-ai-context-multi-outils_transcript.txt`

## 2. Qualification

- Sujet principal : orchestration de plusieurs assistants IA en terminal autour d'un meme projet.
- Sujets secondaires : Gemini CLI, Claude Code, Codex, OpenCode, fichiers d'instructions et Git.
- Fiabilite : moyenne pour le workflow montre ; faible pour les gains chiffres et recommandations generales.
- Statut : GO partiel.

## 3. Resume synthetique

La source montre un projet conserve sur disque, accompagne de fichiers d'instructions propres aux outils et d'un rituel de cloture qui actualise l'etat avant versionnement. L'interet durable ne reside pas dans le terminal lui-meme, mais dans la possession du contexte, sa portabilite entre sessions et la prevention des divergences lorsque plusieurs assistants travaillent sur le meme depot.

## 4. Connaissances candidates

- Conserver un contexte projet canonique, local, inspectable et versionne.
- Separer instructions durables, etat courant, decisions et journal de session.
- Deriver ou lier les fichiers propres a chaque agent plutot que maintenir plusieurs copies independantes.
- Clore une session par une mise a jour explicite de l'etat, puis un controle Git.

## 5. Limites et elements rejetes

- Le gain de productivite annonce n'est pas mesure.
- Les permissions accordees aux outils de terminal ne sont pas auditees.
- La synchronisation automatique de plusieurs fichiers d'instructions peut propager une erreur ; une source canonique et une revue restent necessaires.

## 6. Differences permanentes

- Integre dans `02_IA/Orchestration IA/fiche_permanente.md`, section 8 : workflow de contexte multi-outils.

## 7. Decision finale

- Statut final : GO partiel.
- Point ouvert : tester dans AOS une source canonique avec adaptateurs ou liens par outil et controle de derive.
