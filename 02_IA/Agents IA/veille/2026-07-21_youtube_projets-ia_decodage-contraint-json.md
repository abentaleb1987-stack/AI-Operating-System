# 2026-07-21 - YouTube Projets IA - Decodage contraint et JSON structure

> Regle : une fiche de veille correspond a une source unique et ne modifie jamais directement une fiche permanente.

## 1. Identification de la source

- Titre : Comment FORCER une IA a produire du JSON valide a 100 % (pas 95 %)
- Source : YouTube - Projets IA
- Fichier source : `01_Collecte/sources_brutes/videos/traitees/2026-07-21_youtube_projets-ia_decodage-contraint-json_transcript.txt`
- Type de source : Video / transcription YouTube
- Date de publication : 2026-07-02
- Date de consultation : 2026-07-22
- Contexte de collecte : Source presente dans `videos/a_traiter/` lors du GO AOS.

## 2. Detection et routage

- IA principale / outil / framework : Agents IA
- IA secondaires : OpenAI Structured Outputs, Anthropic tool use, Outlines, llama.cpp
- Domaine : Sorties structurees et contraintes de generation
- Dossier de veille cible : `02_IA/Agents IA/veille/`
- Niveau de fiabilite : Moyen (vulgarisation citant des documentations et outils externes)
- Priorite : Moyenne

## 3. Resume synthetique

La video distingue l'instruction par prompt d'une contrainte appliquee pendant le decodage. Elle presente le masquage des tokens incompatibles avec un schema ou une grammaire comme un moyen de reduire les sorties syntaxiquement invalides. Elle cite notamment les schemas JSON, les grammaires GBNF et Outlines.

## 4. Faits validables

- La source decrit une generation autoregressive choisissant un token a chaque etape.
- Elle presente les sorties structurees comme une contrainte de format distincte des seules instructions de prompt.
- Elle cite OpenAI, Anthropic, Outlines et llama.cpp comme pistes a verifier dans leurs documentations respectives.

## 5. Hypotheses

- Un schema de sortie et une validation applicative peuvent reduire les reprises dans un workflow agentique.
- Le niveau de garantie depend de l'implementation, du schema et de l'API ou moteur selectionne.

## 6. Elements marketing ou speculatifs

- L'affirmation d'une validite JSON a 100 % est conditionnelle a l'implementation et n'est pas validee ici par test AOS.

## 7. Limites de la source

- Video non officielle et transcription automatique imparfaite.
- Aucun protocole de test, aucun schema cible ni comparaison reproductible ne sont fournis.
- La validite syntaxique ne garantit ni la justesse semantique ni la securite d'une action outil.

## 8. Connaissances candidates

- Agents IA - Prompts & methodes : distinguer contrat de sortie, validation et contenu genere.

## 9. Differences proposees

### Section concernee : Agents IA / Prompts & methodes

- Ajout propose : Aucun.
- Modification proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : la fiche permanente exige deja un schema d'entree/sortie, des criteres d'acceptation et des verifications ; la source ne fournit pas de preuve reproductible supplementaire.

## 10. Validation

- Statut : A surveiller
- Validation humaine requise : Non
- Justification : conserver la distinction entre contrainte de format et validation de fond ; verifier la documentation officielle et tester sur un cas AOS borne avant integration.

## 11. Rapport final de traitement

- Differences integrees : Aucune difference permanente.
- Differences non integrees : Garantie absolue de validite et details d'implementation non verifies.
- Points a surveiller : compatibilite des schemas, validation semantique et gestion d'erreurs dans les outils retenus.
- Source deplacee vers : `01_Collecte/sources_brutes/videos/traitees/2026-07-21_youtube_projets-ia_decodage-contraint-json_transcript.txt`
- Fichiers modifies : cette fiche de veille et la source archivee.

