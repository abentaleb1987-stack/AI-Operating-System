# 2026-08-22 - YouTube / Meydeey - DeepSeek Harness, modes, permissions et trajectoires

> Regle : une fiche de veille correspond a une source unique. Elle ne modifie jamais directement une fiche permanente.

## 1. Identification de la source

- Titre : DeepSeek Harness... surpuissant
- Source : YouTube - Meydeey | Automatisation IA
- URL ou reference : transcription locale fournie dans le batch AOS
- Type de source : Video / transcription YouTube
- Date de publication : 2026-08-22
- Date de consultation : 2026-08-22
- Auteur ou organisation : Meydeey | Automatisation IA
- Contexte de collecte : Source presente dans `videos/a_traiter/` lors du GO AOS.
- Fichier source traite : `01_Collecte/sources_brutes/videos/traitees/2026-08-22_youtube_meydeey_deepseek-harness-modes-permissions-trajectoires_transcript.txt`

## 2. Qualification

- IA ou outil principal : DeepSeek Harness
- IA secondaires : modeles DeepSeek, Claude, Codex et modeles servis par des fournisseurs externes
- Composants secondaires : Cordis, plugins, presets d'agents, trajectoires et logs JSONL
- Domaine : runtime agentique composable, permissions, observabilite et portabilite des modeles
- Niveau de fiabilite : Moyen pour les manipulations montrees ; faible pour les chiffres, compatibilites, couts, performances et projections
- Priorite : Moyenne, car une fiche permanente DeepSeek Harness et des veilles recentes couvrent deja l'architecture principale
- Statut de traitement : Traitee

## 3. Statut du cycle de traitement

- Statut : A surveiller
- Etape actuelle : Qualification, analyse, comparaison avec l'existant et archivage termines
- Prochaine action : Reproduire l'incident de suppression et verifier les permissions, l'export des trajectoires et les modes sur une version epinglee dans un depot jetable

## 4. Resume synthetique

La video presente DeepSeek Harness comme une couche agentique modulaire separee du modele. Elle parcourt quatre presets annonces, les niveaux d'acces aux workspaces, la configuration de fournisseurs, les plugins et la vue de trajectoire. Plusieurs petits projets sont generes afin d'illustrer l'ecriture de fichiers, l'ouverture d'un navigateur, les travaux en arriere-plan et l'export de logs de session.

L'apport le plus important pour AOS est un avertissement de securite : l'auteur rapporte qu'un fichier a ete supprime alors que son instruction en langage naturel n'accordait pas clairement cette action. Cet incident n'est pas reproduit ni documente techniquement, mais il justifie de tester les frontieres de permission imposees par le runtime et le systeme, sans traiter le prompt comme un controle d'acces.

## 5. Idees principales

- Le modele, le harness, les outils, les permissions et l'environnement d'execution doivent etre evalues comme des couches distinctes.
- Les presets standard, PTC, minimal et creator sont presentes comme des assemblages differents d'outils et de comportements.
- Une trajectoire de session peut aider a inspecter les prompts, appels d'outils, tours, durees et boucles anormales.
- La possibilite de changer de fournisseur ou de modele ne garantit ni compatibilite fonctionnelle ni equivalence de qualite.
- Les limites de fichier doivent etre imposees et testees hors du langage naturel lorsque des actions destructives sont possibles.

## 6. Faits validables dans la source

- La demonstration affiche des niveaux d'acces lecture, ecriture dans le workspace et acces complet.
- Elle montre une vue de trajectoire contenant plusieurs roles et appels d'outils, ainsi qu'un export annonce de logs de session en JSONL.
- Elle montre des presets standard, PTC, minimal et creator, et une configuration de fournisseurs ou de plugins.
- Plusieurs workspaces sont utilises pour generer des projets et lancer des serveurs locaux.
- L'auteur rapporte un test anterieur ou un fichier a ete supprime malgre une autorisation formulee de facon ambigue ; aucune trace reproductible de l'incident n'est fournie.

## 7. Hypotheses

- Des trajectoires exportables pourraient faciliter l'audit de sessions si elles sont completes, stables et reliees aux diffs produits.
- Des presets specialises pourraient reduire la surface d'outils par tache s'ils appliquent effectivement le moindre privilege.
- Un modele local combine a un runtime local pourrait reduire certains transferts de donnees, sous reserve d'un audit du reseau, des dependances et des outils actifs.

## 8. Elements marketing ou speculatifs

- Les nombres d'etoiles, de forks, de versions, de plugins et de modeles disponibles.
- Les affirmations de gratuite, d'absence de limitation, de souverainete complete et de compatibilite avec n'importe quel modele.
- Les noms, disponibilites, prix et performances des modeles cites.
- Les promesses de creer des agents, outils ou infrastructures d'entreprise rapidement et de remplacer des produits integres.
- Les extrapolations sur un marche futur de harness specialises.

## 9. Limites de la source

- Video non officielle sans version ou commit exact du Harness, inventaire de dependances ni configuration complete.
- L'incident de suppression est rapporte oralement sans logs, permissions exactes, fichier test ni procedure de reproduction.
- Les applications generees sont jugees visuellement sans batterie de tests, audit de securite ou comparaison controlee.
- Plusieurs modes, providers et plugins sont parcourus mais pas testes en profondeur.
- La transcription contient des erreurs d'encodage et de nombreux noms de produits ambigus.

## 10. Connaissances candidates

- Securite : ne jamais utiliser une consigne en langage naturel comme frontiere de permission pour l'ecriture ou la suppression.
- Evaluation : enregistrer la version, le preset, le modele, les plugins, les permissions et les acces reseau de chaque essai.
- Observabilite : relier les trajectoires et logs exportes aux fichiers modifies, tests, erreurs et couts.
- Specialisation : reduire les outils d'un preset au besoin reel avant d'augmenter son autonomie.

## 11. Differences proposees pour la fiche permanente

### Sections concernees : Aucune

- Ajout propose : Aucun.
- Correction proposee : Aucune.
- Suppression proposee : Aucune.
- Justification : la fiche permanente DeepSeek documente deja l'architecture plugin, la preview instable, le moindre privilege, l'audit des outils, le test des refus et l'export de trajectoires a confirmer. L'incident de suppression renforce ces controles, mais son absence de preuve reproductible ne justifie pas une nouvelle difference permanente.

## 12. Decision de validation

- Statut : A surveiller
- Justification : la source confirme plusieurs points deja capitalises et fournit un signal de risque utile, sans preuve suffisante pour valider les compatibilites, la securite ou les performances.
- Sections permanentes impactees : Aucune
- Validation humaine requise : Non

## 13. Elements rejetes

- Compatibilite universelle des modeles et fournisseurs - Justification : elle depend des adaptateurs, protocoles, outils et versions.
- Souverainete garantie par une installation locale - Justification : le modele, les outils, les recherches et les dependances peuvent encore communiquer avec des services distants.
- Robustesse deduite des projets generes - Justification : aucune verification reproductible n'est fournie.
- Prompt comme controle d'acces suffisant - Justification : l'incident rapporte montre precisement que cette limite doit etre imposee par des mecanismes externes.

## 14. Elements a surveiller

- Reproduction de la suppression non autorisee - Condition de revision : test isole avec matrice lecture/ecriture/suppression et journaux complets.
- Exhaustivite de l'export JSONL - Condition de revision : comparaison entre trajectoire, appels d'outils, processus, acces reseau et diff Git.
- Semantique reelle des quatre presets - Condition de revision : inventaire versionne des outils, permissions, limites et conditions d'arret de chacun.
- Portabilite entre fournisseurs - Condition de revision : jeu de taches identique, versions epinglees et mesure des erreurs, couts et reprises.
- Isolation d'un modele et d'un runtime locaux - Condition de revision : observation reseau et audit des dependances sur environnement jetable.

## 15. Rapport final

- Statut final : A surveiller
- Differences validees : Aucune nouvelle difference permanente ; confirmation des controles deja presents.
- Differences rejetees : compatibilite universelle, souverainete automatique, performances et robustesse non mesurees.
- Elements conserves en veille : incident de suppression, presets, niveaux d'acces, trajectoires, export JSONL et providers.
- Fichiers concernes : cette fiche de veille et la transcription archivee.
- Actions realisees : analyse, qualification, comparaison avec la fiche permanente et les veilles recentes, creation de la fiche et archivage de la transcription.
- Decision finale : A surveiller.
- Points ouverts : permissions destructives, exhaustivite des logs, semantique des presets, portabilite et isolation reseau.
