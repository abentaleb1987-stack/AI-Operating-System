# 2026-08-01 - YouTube / Projets IA - RAG : retrieval, reranking et boucle corrective

## 1. Identification de la source

- Titre : RAG explique simplement : la technique derriere les IA qui marchent
- Source : YouTube - Projets IA
- Type : transcription video pedagogique non officielle
- Date de publication indiquee : 2026-05-14
- Date de consultation : 2026-08-01
- Fichier source traite : `01_Collecte/sources_brutes/videos/traitees/2026-08-01_youtube_projets-ia_rag-retrieval-reranking-correctif_transcript.txt`

## 2. Qualification

- Sujet principal : architecture Retrieval-Augmented Generation (RAG).
- Sujets secondaires : chunking, embeddings, index vectoriel, recherche KNN, reranking, multi-query, HyDE et RAG correctif.
- Fiabilite : moyenne a elevee pour les principes generiques ; source pedagogique non primaire et simplifications techniques presentes.
- Statut : GO partiel.

## 3. Resume synthetique

La source decompose un RAG en indexation des documents, recherche des passages pertinents et generation ancree dans ces passages. Elle explique que la qualite depend du decoupage, de la coherence de l'espace d'embeddings et du retrieval. Pour depasser un RAG lineaire fragile, elle propose de reformuler les requetes, recuperer un ensemble large de candidats, les reranker, verifier la pertinence et l'ancrage de la reponse, puis boucler de maniere bornee en cas d'insuffisance.

## 4. Faits et connaissances candidates

- Preserver les frontieres semantiques, metadonnees et references lors du chunking ; l'overlap doit etre calibre et non applique aveuglement.
- Documents et requetes doivent etre projetes dans un espace d'embeddings compatible.
- Le retrieval initial rapide peut etre complete par un reranking plus precis sur un sous-ensemble de candidats.
- Une reponse doit etre verifiee contre les passages recuperes et refuser de conclure lorsque les preuves sont insuffisantes.
- Les boucles de reformulation et de retrieval doivent avoir des limites d'iteration et conserver leurs journaux.

## 5. Limites et elements non integres

- Les tailles de chunks, nombres de dimensions, valeurs de `k` et bases citees sont des exemples, pas des standards universels.
- L'interpretation geometrique simplifiee de la similarite cosinus et l'affirmation que toutes les entreprises utilisent le meme schema ne sont pas retenues.
- HyDE, multi-query, cross-encoders et RAG correctif doivent etre compares sur un corpus et des questions AOS avant adoption.

## 6. Differences permanentes

- Fiche modifiee : `02_IA/Agents IA/fiche_permanente.md`.
- Sections : 3 Architecture, 8 Workflows recommandes, 12 Evolutions et historique.
- Differences integrees : pipeline RAG auditable, retrieval large puis reranking, verification d'ancrage et boucle corrective bornee.

## 7. Decision finale

- Statut final : GO partiel.
- Point ouvert : constituer un jeu d'evaluation AOS avec questions, passages attendus, citations, latence, cout et taux de refus correct.
