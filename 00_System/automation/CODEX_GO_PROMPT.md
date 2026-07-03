# Codex GO Prompt

## Objectif

Declencher le workflow automatise AOS complet apres validation utilisateur.

## Prompt utilisateur recommande

```text
GO AOS

Traite les sources presentes dans :
01_Collecte/sources_brutes/{{type}}/a_traiter/

Pour les videos, scanne :
01_Collecte/sources_brutes/videos/a_traiter/

Execute le workflow complet :
Source brute -> Detection IA / outil / framework -> Routage -> Fiche de veille -> Validation -> Mise a jour fiche permanente -> Deplacement source traitee -> Git commit -> Git push -> Rapport final.

Si plusieurs fichiers sont presents, traite tout le batch automatiquement, source par source, sans intervention intermediaire.

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

## Raccourci conversationnel GO RAPPORT

Commande utilisateur :

```text
GO RAPPORT
```

Variantes acceptees :

- `GO RAPPORT`
- `Go rapport`
- `go rapport`

Quand l'utilisateur ecrit `GO RAPPORT`, Codex doit lire le dernier rapport d'audit journalier AOS en mode lecture seule stricte.

Regle centrale :

- `GO RAPPORT` est une commande de lecture seule stricte.
- Toute generation de rapport est interdite dans `GO RAPPORT`.
- `GO RAPPORT` ne doit jamais executer `00_System/scripts/aos_daily_audit.py`.

Workflow obligatoire :

1. Executer `git pull origin main`.
2. Identifier le dernier rapport Markdown dans `00_System/audits/daily/`.
3. Lire le dernier rapport d'audit journalier.
4. Resumer :
   - decision d'audit ;
   - niveau de risque maximal ;
   - commit audite ;
   - alertes prioritaires Aion ;
   - alertes totales ;
   - recommandations ;
   - action attendue.
5. Executer `git status --short` final.

Contraintes obligatoires :

- Ne modifier aucun fichier.
- Ne creer aucun commit.
- Ne faire aucun push.
- Ne traiter aucune source.
- Ne modifier aucune fiche permanente.
- Ne modifier aucune fiche de veille.
- Ne generer aucun nouveau rapport.
- Ne jamais executer `00_System/scripts/aos_daily_audit.py`.
- Appliquer une lecture seule stricte apres `git pull origin main`.

Regle de conclusion :

- Si le rapport indique `GO`, conclure exactement : `Aucune action Aion requise.`
- Si le rapport indique `GO partiel`, `Audit Aion recommande`, un risque moyen ou un risque eleve, conclure exactement : `Partager ce rapport avec Aion pour arbitrage.`

## Raccourci conversationnel GO AUDIT LOCAL

Commande utilisateur :

```text
GO AUDIT LOCAL
```

Quand l'utilisateur ecrit explicitement `GO AUDIT LOCAL`, Codex peut generer manuellement un rapport d'audit local.

Workflow autorise :

1. Executer `00_System/scripts/aos_daily_audit.py --print-path`.
2. Lire le rapport genere.
3. Resumer son contenu.
4. Executer `git status --short` final.

Contraintes :

- Cette commande est distincte de `GO RAPPORT`.
- La generation locale de rapport est autorisee uniquement avec `GO AUDIT LOCAL`.
- Ne pas creer de commit sauf demande explicite separee.
- Ne pas faire de push sauf demande explicite separee.
- Ne traiter aucune source.

## Regles pour Codex

- Executer jusqu'au push GitHub si le traitement produit des modifications utiles.
- Scanner tous les fichiers presents dans les dossiers `a_traiter/`.
- Traiter les sources une par une.
- Ne pas demander d'intervention intermediaire sauf blocage critique.
- Ne pas inventer d'information.
- En cas d'incertitude, creer la fiche de veille et conserver les informations en `A surveiller`.
- Ne pas enrichir une fiche permanente avec des informations faibles.
- Ne pas creer de commit vide.
- Pour un batch, creer un seul commit global, jamais un commit par source.
- Utiliser `docs(aos): process video source batch` pour un batch video simple.
- Utiliser `docs(aos): integrate multi-source AI watch batch` si plusieurs categories ou plusieurs IA sont traitees.
- Si une source echoue sans risque critique, ne pas la deplacer vers `traitees/`, continuer les autres sources et mentionner l'echec dans le rapport consolide.
- Si une erreur critique apparait, arreter le batch, ne pas commit, ne pas push, et produire un rapport de blocage.
- Avant de deplacer une source vers `traitees/`, generer un nom lisible base sur le sujet reel detecte.
- Ne pas conserver le nom d'entree s'il est generique ou trompeur.
- Pour les videos, utiliser le format `YYYY-MM-DD_youtube_nom-chaine_sujet-video_transcript.txt`.
- Mettre le nom final en minuscules, sans accents, sans caracteres speciaux, avec tirets.
- Si deux sources produisent le meme nom final, ajouter `_01`, `_02` ou `_03` avant `_transcript.txt`.
- A la fin du batch, executer `git status --short`, `git add .`, un seul commit global, `git push origin main`, puis `git status --short`.
- Produire un rapport final consolide clair.

## Rapport consolide obligatoire

Le rapport final d'un batch doit contenir :

- nombre de sources detectees ;
- nombre de sources traitees ;
- nombre de sources echouees ;
- liste des IA principales detectees ;
- detail par source ;
- fiches de veille creees ;
- fiches permanentes modifiees ;
- sections modifiees ;
- sources deplacees ;
- nom source initial ;
- nom source traite final ;
- chemin final dans `traitees/` ;
- connaissances integrees ;
- connaissances non integrees ;
- points a surveiller consolides ;
- commit cree ;
- resultat du push ;
- resultat final de `git status --short` ;
- decision finale batch.
