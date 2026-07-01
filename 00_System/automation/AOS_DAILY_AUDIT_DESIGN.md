# AOS Daily Audit Design

## Objectif

Ce document prepare l'architecture d'un audit journalier automatique du repository GitHub AOS.

La decision operationnelle reste :

- Codex execute.
- GitHub synchronise.
- Aion audite.

L'audit journalier doit produire chaque jour un rapport lisible, partageable et exploitable par l'utilisateur et Aion.

Le cycle cible est :

1. GitHub declenche un audit automatique a 01h00.
2. Le repository AOS est controle sans modifier les connaissances.
3. Un rapport d'audit journalier est genere.
4. L'utilisateur lit ou partage le rapport avec Aion vers 08h00.
5. Aion decide des corrections eventuelles.
6. Codex applique les corrections uniquement si l'utilisateur le demande.

## Perimetre de controle

L'audit journalier doit controler :

- coherence de classement des sources traitees ;
- presence des fiches de veille attendues ;
- presence et structure des fiches permanentes ;
- respect des regles de creation de nouvelles fiches permanentes ;
- absence de restructuration massive non justifiee des fiches permanentes majeures ;
- qualite des connaissances integrees ;
- separation entre faits valides, hypotheses, marketing et points a surveiller ;
- doublons ou quasi-doublons dans les fiches ;
- sources encore presentes dans les dossiers `a_traiter/` ;
- coherence des noms de fichiers ;
- respect des templates et standards Markdown ;
- coherence Git recente : commits, fichiers modifies et deplacements de sources.

L'audit ne doit pas :

- modifier les fiches ;
- traiter des sources ;
- deplacer des fichiers ;
- creer de commit correctif ;
- pousser de correction ;
- decider seul d'une integration permanente.

## Architecture recommandee

Architecture cible :

```text
GitHub Actions schedule 01h00
-> checkout repository
-> execution script audit AOS
-> controles statiques et heuristiques
-> generation rapport Markdown
-> publication rapport dans le repository ou en artifact
-> lecture utilisateur / analyse Aion vers 08h00
-> corrections par Codex uniquement sur demande
```

Le premier niveau d'audit doit rester deterministe et local au repository :

- lecture des fichiers Markdown ;
- verification des chemins ;
- verification des structures obligatoires ;
- detection de termes faibles ou speculatifs ;
- comparaison simple entre sources traitees, fiches de veille et fiches permanentes ;
- generation d'un rapport sans appel externe.

Un second niveau pourra etre ajoute plus tard avec un GPT connecte ou Aion, mais il ne doit pas remplacer les controles statiques.

## Role de GitHub Actions

GitHub Actions doit servir de declencheur et d'environnement d'execution reproductible.

Role attendu :

- declencher l'audit chaque jour a 01h00 ;
- executer les controles sur l'etat courant de `main` ;
- produire un rapport journalier ;
- conserver les logs d'execution ;
- exposer le rapport a l'utilisateur.

Decisions a confirmer a l'implementation :

- fuseau horaire exact du declenchement ;
- stockage du rapport comme artifact uniquement ou commit dans le repository ;
- duree de retention des artifacts ;
- notification eventuelle en cas de risque eleve.

Option recommandee pour la premiere version :

- generer un artifact GitHub Actions ;
- ne pas commit automatiquement le rapport ;
- eviter toute modification automatique du repository.

## Role eventuel d'un GPT connecte plus tard

Un GPT connecte pourra etre ajoute apres la version deterministe.

Role possible :

- lire le rapport journalier ;
- resumer les risques ;
- prioriser les corrections ;
- proposer un plan d'action ;
- aider Aion a distinguer erreur critique, dette documentaire et simple point a surveiller.

Limites obligatoires :

- le GPT ne doit pas modifier le repository directement ;
- le GPT ne doit pas valider seul une connaissance permanente ;
- le GPT doit citer les fichiers et sections concernes ;
- le GPT doit separer faits, hypotheses et recommandations ;
- les corrections doivent rester executees par Codex apres demande utilisateur.

## Dossiers de sortie des rapports

Deux options sont possibles.

### Option 1 : Artifacts GitHub Actions

Le rapport est produit dans l'environnement GitHub Actions et conserve comme artifact.

Avantages :

- aucun bruit Git ;
- pas de commit automatique ;
- simple pour une premiere version.

Limites :

- consultation moins directe depuis le repository ;
- retention limitee selon configuration GitHub.

### Option 2 : Dossier de rapports dans le repository

Dossier propose :

```text
00_System/audits/journaliers/
```

Nom de fichier propose :

```text
YYYY-MM-DD_audit-journalier-aos.md
```

Avantages :

- historique durable dans Git ;
- partage facile avec Aion ;
- comparaison simple entre audits.

Limites :

- commits automatiques a encadrer ;
- risque de bruit dans l'historique ;
- besoin d'une regle claire pour ne pas melanger audit et corrections.

Decision recommandee :

- version 1 : artifact GitHub Actions ;
- version 2 : dossier `00_System/audits/journaliers/` si l'historique des rapports devient utile.

## Regles d'audit

Regles prioritaires :

- Toute source traitee doit avoir une fiche de veille ou une justification d'exclusion.
- Une fiche permanente ne doit pas etre creee pour un outil seulement mentionne brievement.
- Une fiche permanente majeure ne doit pas etre initialisee ou restructuree largement par une source YouTube non officielle.
- Les noms de modeles, prix, benchmarks, disponibilites et capacites futures non recoupes doivent rester en veille.
- Les fiches permanentes doivent rester synthetiques et consolidees.
- Les sections principales des fiches permanentes ne doivent pas accumuler des blocs chronologiques par source.
- Les contenus marketing ou speculatifs doivent etre identifies et exclus des connaissances durables.
- Les points incertains doivent etre marques `A surveiller`.
- Les sources doivent etre renommees selon le sujet reel avant passage en `traitees/`.
- Le rapport final d'un batch doit contenir les elements obligatoires du protocole AOS.

Regles de structure :

- un seul H1 par document ;
- presence des sections standard dans les fiches de veille ;
- presence des sections standard dans les fiches permanentes ;
- liens ou chemins de sources explicites ;
- historique des mises a jour pour les fiches permanentes modifiees.

Regles Git :

- un batch `GO AOS` doit produire un seul commit global ;
- absence de commit vide ;
- coherence entre fichiers crees, fichiers modifies et sources deplacees ;
- absence de modifications hors perimetre dans un commit de traitement.

## Niveaux de risque

### Critique

Erreur pouvant corrompre la base AOS ou induire une decision durable fausse.

Exemples :

- source traitee sans fiche de veille ;
- fiche permanente majeure restructuree massivement par source faible ;
- information speculative integree comme fait valide ;
- source deplacee sans traitement detectable ;
- suppression ou reecriture large non justifiee.

### Eleve

Erreur importante mais corrigeable sans blocage immediat.

Exemples :

- mauvaise route probable vers `02_IA/` ;
- creation de fiche permanente douteuse ;
- points marketing melanges aux connaissances candidates ;
- absence de points a surveiller pour claims instables ;
- nom de source traitee peu lisible ou non conforme.

### Moyen

Dette documentaire ou incoherence locale.

Exemples :

- section de veille incomplete ;
- historique permanent insuffisamment precis ;
- duplication partielle ;
- manque de justification sur une connaissance integree.

### Faible

Amelioration de lisibilite ou hygiene documentaire.

Exemples :

- formulation a clarifier ;
- ordre de sections perfectible ;
- petite incoherence de style Markdown.

## Contenu du rapport journalier

Le rapport journalier doit contenir :

- date et heure de l'audit ;
- commit audite ;
- resultat global : `OK`, `A surveiller`, `Correction recommandee`, `Blocage critique` ;
- resume executif ;
- statistiques du repository ;
- sources en attente dans `a_traiter/` ;
- sources traitees recemment ;
- fiches de veille creees recemment ;
- fiches permanentes modifiees recemment ;
- anomalies par niveau de risque ;
- fichiers concernes avec chemins exacts ;
- justification de chaque anomalie ;
- recommandation d'action ;
- priorite proposee ;
- points a transmettre a Aion ;
- limites de l'audit ;
- checklist de verification manuelle.

Format recommande pour chaque anomalie :

```text
### AUDIT-YYYYMMDD-001 - Titre court

- Risque : Critique / Eleve / Moyen / Faible
- Fichier concerne : chemin
- Section concernee : section
- Regle violee : regle AOS
- Observation : constat factuel
- Impact : consequence probable
- Recommandation : action proposee
- Decision attendue : Aion / utilisateur / Codex sur demande
```

## Limites

L'audit journalier ne peut pas garantir seul :

- la veracite externe des informations ;
- la qualite d'un jugement strategique ;
- la detection parfaite des doublons semantiques ;
- la pertinence finale d'une integration permanente ;
- la securite d'un outil externe cite dans une source ;
- la correction de toutes les erreurs de transcription.

Les controles automatiques doivent donc etre consideres comme un filet de detection, pas comme une validation finale.

## Prochaines etapes d'implementation

Etapes recommandees :

1. Valider ce document de conception.
2. Creer un dossier de scripts d'audit si necessaire.
3. Definir le format exact du rapport Markdown.
4. Implementer une premiere version deterministe sans appel externe.
5. Ajouter un workflow GitHub Actions programme a 01h00.
6. Publier le rapport comme artifact.
7. Tester l'audit sur le repository courant.
8. Ajuster les regles de risque avec Aion.
9. Decider si les rapports doivent rester artifacts ou etre commits dans `00_System/audits/journaliers/`.
10. Etudier ensuite l'ajout d'un GPT connecte pour synthese et priorisation.

## Decision de conception

La premiere phase d'automatisation doit privilegier un audit passif, deterministe et non destructif.

Aucune correction ne doit etre appliquee automatiquement.

Aion reste responsable de l'audit qualitatif et des decisions de correction.

Codex reste responsable de l'execution des corrections uniquement apres demande explicite de l'utilisateur.
