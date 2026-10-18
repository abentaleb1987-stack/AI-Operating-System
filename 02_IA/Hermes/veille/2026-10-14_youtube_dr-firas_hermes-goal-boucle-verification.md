# 2026-10-14 - YouTube / Dr. Firas - Hermes Agent et la commande /goal

## 1. Identification de la source

- Titre : Hermes Agent vous donne des super-pouvoirs : voici comment les debloquer !
- Source : YouTube, Dr. Firas ; transcription collectee le 2026-10-15.
- URL de la video : absente du fichier brut.
- Type : demonstration video, doublee automatiquement.
- Date de publication indiquee : 2026-10-14.
- Source traitee : `01_Collecte/sources_brutes/videos/traitees/2026-10-14_youtube_dr-firas_hermes-agent-goal-boucle-verification_transcript.txt`.
- Documentation primaire consultee le 2026-10-18 : https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/goals.md

## 2. Qualification et statut

- IA principale : Hermes Agent.
- Domaine : execution d'objectifs persistants et verification de progression.
- Fiabilite : moyenne pour la demonstration ; elevee pour le fonctionnement documente dans le depot du projet.
- Priorite : moyenne.
- Statut du cycle : validee pour les caracteristiques documentees, archivee ; resultats de la demonstration a surveiller.

## 3. Resume synthetique

La video montre l'installation de Hermes et l'emploi de `/goal` pour continuer une tache sur plusieurs tours. Le presentateur parcourt le suivi, la pause et la reprise d'un objectif. Sa promesse selon laquelle l'agent travaille jusqu'a la reussite doit etre corrigee : la documentation prevoit aussi un verdict de blocage et une limite de tours.

## 4. Idees principales et faits validables

- `/goal <texte>` enregistre un objectif suivi sur plusieurs tours ; un modele auxiliaire juge la reponse finale de chaque tour et peut demander la continuation.
- Les verdicts documentes sont `done`, `blocked`, `continue` et `wait`. Un objectif juge irrealisable est mis en pause avec une raison.
- La limite par defaut est de 20 tours de continuation ; `/goal resume` reinitialise ce compteur. `/goal status`, `/goal pause` et `/goal clear` donnent des commandes de controle.
- L'etat de l'objectif persiste avec la session. Un nouveau message utilisateur peut reprendre la priorite sur la continuation.

## 5. Hypotheses, marketing et limites

- Hypothese a tester : la boucle peut ameliorer l'achevement de taches longues lorsque les criteres de reussite sont observables.
- Rejete : garantie de reussite ou poursuite sans limite jusqu'a atteinte de l'objectif. Le juge peut se tromper, se bloquer ou atteindre son budget.
- Les liens d'hebergement et de formation sont promotionnels ; aucune qualite de service n'est deduite de la video.
- Aucun protocole de test, taux de succes, cout complet ou trace reproductible n'est fourni.

## 6. Connaissances candidates et differences permanentes

- Integrer uniquement le fonctionnement documente de `/goal` et ses conditions d'arret dans les sections 3 et 8 de la fiche Hermes.
- Aucun cas d'usage Hermes valide pour AOS par cette seule video.

## 7. Decision et points a surveiller

- Statut final : GO partiel.
- Differences validees : commande persistante, juge, verdicts et limite de tours, recoupes par la documentation du projet.
- Elements conserves en veille : gain reel de productivite, cout par tache, fiabilite du jugement et comportement en cas d'erreur.
- Prochaine action : tester une tache AOS reversible avec criteres de succes, budget, trace et conditions d'arret explicites.
