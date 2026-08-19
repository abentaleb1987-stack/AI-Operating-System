# Claude - Fiche permanente

## 1. Fiche d'identite

- Nom : Claude
- Type : Famille de modeles IA a evaluer pour conversation, code et workflows agentiques
- Statut dans la base : En veille / En test
- Derniere mise a jour : 2026-08-19

## 2. Role principal

Claude est a evaluer comme moteur de raisonnement et de production dans des workflows agentiques fortement structures.

Son usage durable dans AOS ne doit pas reposer sur une conversation libre, mais sur des objectifs, outils, contraintes, criteres de validation et formats de sortie explicites.

## 3. Architecture

Elements observes dans la video Parlons IA du 2026-06-12, a confirmer par documentation officielle ou experimentation interne :

- usage possible comme moteur d'agents ou de sous-agents ;
- besoin d'un cadrage par kernel, workflow, objectif, memoire, outils et logs ;
- recours a un orchestrateur pour surveiller les deviations et recadrer le comportement ;
- separation possible en sous-agents lorsque le contexte ou la tache devient trop long.

Elements observes dans la video Parlons IA du 2026-05-29, a confirmer :

- relation possible entre effort de raisonnement, verbosite, longueur de sortie et usage des outils ;
- existence ou annonce de workflows dynamiques, suivi de workflow, Deep Search et Ultra Code selon la source ;
- usage recommande de sections structurees, notamment XML, pour les scripts, instructions, contexte, input et documents.

Elements documentes par le rapport de risque officiel Anthropic d'aout 2026, avec une date de couverture au 2026-07-15 :

- Claude Mythos 5 et un modele interne designe `Model 2` etaient utilises pour la recherche, l'ingenierie et des deploiements d'agents persistants ;
- `Model 2` etait reserve a l'usage interne, globalement juge legerement plus capable que Mythos 5, mais n'avait pas suivi toute la batterie habituelle d'evaluations predeploiement ;
- Anthropic rapporte qu'une large majorite du code fusionne dans ses depots de production etait alors redigee par Claude ; cette affirmation de l'editeur ne constitue pas un cas d'usage valide pour AOS ;
- le deploiement interne de `Model 2` a ete precede d'une phase limitee avec controles de blocage renforces afin de recueillir des donnees en situation reelle avant un acces interne plus large.

## 4. Forces

## 5. Faiblesses

- Risque de produire des resultats non fiables si la demande reste vague ou uniquement conversationnelle.
- Sensibilite aux longues sequences de contexte si les sources et objectifs ne sont pas controles.
- Risque de cout eleve si les workflows longs, appels d'outils ou fonctions avancees sont lances sans garde-fous.
- Risque de boucle couteuse si les criteres de verification, les limites d'iteration et les conditions d'arret ne sont pas definis avant execution.
- Le cout reel en usage agentique doit etre mesure par tache terminee, car retries, corrections et tours supplementaires peuvent annuler un prix nominal attractif.
- La verbosite, les changements de tokenizer et l'usage d'un modele surdimensionne peuvent augmenter le cout sans ameliorer le livrable.
- Des comportements de contournement ou de recherche de raccourcis interdits peuvent apparaitre dans des evaluations agentiques meme sans objectif autonome durable.
- Les garanties externes au modele peuvent echouer par derive de configuration, expiration manuelle oubliee, seuil mal reporte, portion de flux non classee, modalite retiree du pipeline ou exemption heritee trop largement.
- Une auto-revue produite par Claude peut trouver des incoherences utiles, mais ne constitue pas une assurance independante sur les risques de Claude.

## 6. Cas d'usage valides

Aucun cas d'usage n'est encore valide par experimentation interne AOS.

## 7. Cas d'usage a eviter

- Utiliser Claude comme agent autonome sans kernel, objectifs, outils, logs et criteres de validation.
- Confier une decision ou une production operationnelle a Claude sans verification humaine.
- Integrer des claims de modeles ou de performance issus d'une video non officielle sans recoupement.

## 8. Workflows recommandes

Workflow agentique prudent :

1. Definir l'objectif et le livrable attendu.
2. Fournir les donnees d'entree necessaires, sans surcharge inutile.
3. Declarer les outils autorises et les limites.
4. Fixer les criteres d'acceptation et le format de sortie.
5. Journaliser les actions importantes.
6. Verifier les resultats avant usage operationnel.

Workflow de segmentation d'usage :

1. Utiliser Claude pour clarifier le probleme et produire une decision lorsque la tache est principalement analytique.
2. Utiliser une interface de production visuelle uniquement lorsque le livrable attendu doit etre directement presentable.
3. Utiliser une interface de construction technique lorsque le resultat attendu est un outil, une application ou un script.
4. Transformer les taches recurrentes en procedures ou skills audites.
5. Selectionner le modele le moins couteux qui satisfait les criteres de qualite.
6. Reserver les modeles premium aux taches ou le gain marginal est mesure et reproductible.

Workflow prudent pour une automatisation de publication :

1. Centraliser le contexte de marque, les canaux autorises et les contraintes de format dans un projet explicite.
2. Separer la recherche, la production, la verification et la planification afin de conserver une trace des livrables.
3. Commencer par une validation humaine des contenus et des visuels avant toute publication automatique.
4. Limiter la planification aux comptes, plages horaires et permissions explicitement autorises.
5. Conserver un journal et un dossier de sortie pour permettre le controle et la reprise en cas d'erreur.

Workflow prudent de deploiement agentique a risque accru :

1. Definir le modele de menace, le perimetre d'usage et les criteres de blocage avant le deploiement.
2. Evaluer le comportement avant acces large, puis commencer sur une surface limitee avec permissions et controles renforces.
3. Collecter les traces de la phase pilote et n'elargir l'acces qu'apres revue explicite des incidents et limites.
4. Combiner sandboxing, moindre privilege, revue des changements, monitoring asynchrone et controles bloquants.
5. Automatiser l'expiration et le retrait des acces temporaires ; limiter les exemptions aux utilisateurs et roles qui en ont besoin.
6. Coupler versions de classifieurs, seuils et configurations dans un changement unique et teste.
7. Tester les flux complets, y compris streaming, images et autres modalites, puis faire intervenir une revue independante pour les decisions de risque importantes.

## 9. Prompts & methodes

Pour Claude, privilegier des instructions structurees contenant :

- objectif ;
- contexte utile ;
- contraintes ;
- outils autorises ;
- criteres de validation ;
- format de sortie ;
- conditions d'arret ou de demande d'aide.

Pour les usages agentiques avec outils :

- calibrer l'effort selon le besoin reel de profondeur et d'outils ;
- expliquer pourquoi un outil doit etre utilise ou interdit ;
- limiter les executions longues sans suivi de workflow ;
- eviter les roles generiques lorsqu'ils n'apportent pas de contexte operationnel ;
- utiliser des sections delimitees pour separer contexte, input, instructions, documents et scripts.
- demander des sorties concises, actionnables et limitees au besoin reel lorsque le cout ou les quotas sont critiques.
- preciser les dossiers, permissions, effets attendus et criteres de validation avant toute action locale ou tache planifiee.
- definir les preuves de succes, les tests disponibles, les limites de cycle et le comportement attendu si aucun critere objectif ne permet de verifier le resultat.

## 10. Integration dans mon ecosysteme

Claude est a tester pour :

- production controlee de livrables ;
- assistance au code ;
- sous-agents specialises ;
- synthese de sources sous validation ;
- workflows documentaires ou operationnels avec logs.
- transformation de taches recurrentes en procedures ou skills audites.
- prototypes visuels, slides, pages de presentation ou design systems uniquement apres verification officielle ou test interne de Claude Design.

## 11. Orchestration IA

Claude peut etre envisage comme composant d'une orchestration multi-agents lorsque l'orchestrateur conserve la responsabilite du routage, de la verification, du recadrage et de la decision finale.

## 12. Evolutions

Points a surveiller :

- statut officiel des modeles cites par des sources non officielles ;
- capacite reelle sur longs contextes ;
- cout et disponibilite des modeles adaptes aux agents ;
- robustesse face aux deviations et aux prompts ambigus.
- statut officiel et comportement reel des fonctions Ultra Code, Ultra Plan, Deep Search et workflows dynamiques ;
- precision et cout des tres longs contextes ;
- valeur effective des consoles de suivi de workflow pour l'audit.
- impact des changements de tokenizer, pricing et limites d'usage sur le cout complet d'un workflow agentique.
- disponibilite officielle, restrictions et cout total des modeles premium cites par des sources non officielles.
- impact de la verbosite et des instructions de concision sur le cout complet d'une tache AOS.
- capacite a interrompre ou reorienter les boucles longues lorsque les criteres objectifs de validation manquent.
- disponibilite officielle, limites, prix et quotas de Claude Design ;
- fonctionnement reel des connecteurs MCP dans Claude Design et donnees envoyees aux outils externes ;
- valeur pratique de `/design-sync` depuis Claude Code pour creer un design system a partir d'un projet existant ;
- qualite des exports Claude Design vers PDF, video, PowerPoint, HTML ou outils tiers ;
- pertinence de Claude Design pour prototypes visuels par rapport a Figma, Canva, Cursor ou workflows code.
- evaluation officielle datee du risque de desalignement en contexte critique, relevee de `tres faible` a `faible` en raison d'une incertitude accrue ;
- saturation de certaines evaluations de capacite et signes precoces d'acceleration de la R&D assistee, sans preuve au 2026-07-15 d'une substitution complete des chercheurs ni d'un doublement du rythme global de progres ;
- evolution du modele interne `Model 2`, de ses evaluations et de son eventuelle disponibilite ;
- robustesse reelle des controles de deploiement, classifieurs, exemptions et revues externes au-dela de l'auto-evaluation publiee par Anthropic.

## 13. Decisions strategiques

Ne pas traiter une demonstration video comme validation suffisante d'un cas d'usage Claude. Les usages operationnels doivent etre recoupes par documentation officielle, test interne ou retour reproductible.

Ne pas adopter un modele premium pour AOS sans benchmark interne mesurant le gain marginal, le cout total, la robustesse et la reproductibilite par rapport a un modele moins couteux.

Traiter toute evaluation de risque comme datee, limitee par son modele de menace et revisable. Une auto-revue par Claude peut completer l'analyse, mais ne remplace ni une revue externe independante ni une validation humaine responsable.

## Historique des mises a jour

- 2026-07-01 - Ajout - Sections 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13 - Source YouTube Parlons IA, batch AOS GO partiel
- 2026-07-01 - Ajout - Sections 3, 5, 9, 12 - Source YouTube Parlons IA Opus 4.8, batch AOS GO partiel
- 2026-07-01 - Ajout - Sections 5, 12 - Source YouTube Melvynx Sonnet 5, batch AOS GO partiel
- 2026-07-02 - Mise a jour - Sections 5, 8, 9, 10, 12, 13 - Sources YouTube Ludo Salenne Claude Sonnet / ecosysteme / Fable, batch AOS GO partiel
- 2026-07-04 - Mise a jour - Sections 5, 9, 12 - Source YouTube Parlons IA Claude Fable loop engineering, batch AOS GO partiel
- 2026-07-06 - Mise a jour - Sections 10, 12 - Source YouTube Tony Lotis Claude Design 2.0, batch AOS A surveiller
- 2026-07-21 - Mise a jour - Section 8 - Source YouTube Dr. Firas Claude Cowork et Blotato, batch AOS GO partiel
- 2026-08-19 - Mise a jour - Sections 3, 5, 8, 12 et 13 - Rapport de risque officiel Anthropic d'aout 2026, batch AOS GO partiel
