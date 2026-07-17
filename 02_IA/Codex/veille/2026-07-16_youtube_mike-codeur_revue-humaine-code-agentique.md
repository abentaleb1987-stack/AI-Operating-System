# 2026-07-16 - YouTube Mike Codeur - Revue humaine du code agentique

> Regle : une fiche de veille correspond a une source unique et ne modifie jamais directement une fiche permanente.

## 1. Identification de la source

- Titre : Le metier de developpeur n'existe plus (c'est le PDG de Mistral qui le dit)
- Source : YouTube - Mike Codeur
- Fichier source : `01_Collecte/sources_brutes/videos/traitees/2026-07-16_youtube_mike-codeur_revue-humaine-code-agentique_transcript.txt`
- Type de source : Video / transcription YouTube
- Date de publication : 2026-07-16
- Date de consultation : 2026-07-17
- Contexte de collecte : Source presente dans `videos/a_traiter/` lors du GO AOS.

## 2. Qualification

- IA principale : Codex
- IA secondaires : Claude Code, agents de revue, outils de CI
- Domaine : Workflow de developpement assiste par agents et revue humaine
- Niveau de fiabilite : Moyen pour le retour d'experience, faible pour les affirmations generales et les etudes citees
- Priorite : Moyenne
- Statut de traitement : Traitee

## 3. Resume synthetique

La video defend un workflow dans lequel des agents produisent une proposition de changement, executent tests et controles automatiques, puis soumettent une pull request a une revue humaine ciblee. Elle recommande que l'humain concentre son attention sur les zones sensibles : authentification, paiement, donnees sensibles et architecture.

La source signale aussi le risque de deleguer sans comprehension suffisante. Pour AOS, cela conforte les controles deja documentes : ne pas assimiler un test passant a une validation complete et exiger une revue proportionnee au risque.

## 4. Faits validables

- La transcription decrit une organisation en phases : recherche, plan, execution, revue et livraison.
- Elle recommande des controles automatiques avant une revue humaine ciblee.
- Elle identifie les zones a risque eleve qui meritent une revue humaine explicite.

## 5. Hypotheses et elements non integres

- Les predictions sur la disparition du metier de developpeur sont des opinions editoriales.
- Les chiffres et conclusions attribues a des etudes ne sont pas integres sans acces aux publications primaires et a leur methode.
- Une pull request avec tests et lint valides ne prouve pas a elle seule la securite, la maintenabilite ou l'adequation au besoin.

## 6. Differences proposees pour la fiche permanente

### Sections concernees : Codex / Workflows recommandes et Prompts & methodes

- Ajout propose : Aucun.
- Justification : la fiche permanente demande deja des preuves objectives, des tests, des logs ou diffs controles, ainsi qu'une verification humaine. La source ne fournit pas de nouvel element suffisamment specifique et verifie.

## 7. Decision de validation

- Statut : A surveiller
- Justification : workflow coherent avec les garde-fous AOS existants, mais source YouTube non officielle sans protocole ni mesure reproductible.
- Sections permanentes impactees : Aucune
- Validation humaine requise : Non

## 8. Elements a surveiller

- Efficacite comparee des controles automatiques et de la revue humaine ciblee sur un depot de test AOS.
- Maintien des competences de diagnostic et de revue lorsque les agents prennent en charge une part croissante de l'execution.

## 9. Rapport final

- Statut final : A surveiller
- Differences validees : Aucune nouvelle difference permanente.
- Elements conserves en veille : revue humaine ciblee, controles automatiques et risque de surconfiance dans les sorties agentiques.
- Actions realisees : Analyse, qualification, creation de la fiche de veille et archivage de la transcription.
- Decision finale : A surveiller.
