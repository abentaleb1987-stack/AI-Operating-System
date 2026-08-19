# 2026-08 - Anthropic - Risk Report August 2026

## 1. Identification de la source

- Titre : Risk Report: August 2026
- Source : Anthropic, rapport officiel public partiellement expurge
- Fichier source : `01_Collecte/sources_brutes/docs/traitees/2026-08_anthropic_risk-report-august-2026.pdf`
- Type : documentation officielle, 186 pages
- Date de publication : aout 2026
- Date de couverture : 2026-07-15
- Date de consultation : 2026-08-19
- Contexte de collecte : validation des annonces sur les modeles internes, les risques agentiques et les garde-fous Anthropic.

## 2. Detection et routage

- IA principale : Claude / Anthropic.
- Sujet secondaire transversal : securite et gouvernance des agents IA.
- Dossier de veille cible : `02_IA/Claude/veille/`.
- Dossier source traitee cible : `01_Collecte/sources_brutes/docs/traitees/`.
- Niveau de fiabilite : eleve pour les politiques, incidents et evaluations declares par Anthropic ; moyen pour l'estimation globale du risque, qui reste une auto-evaluation partiellement expurgee.
- Priorite : haute.

## 3. Resume synthetique

Le rapport analyse trois familles de risques : desalignement en contexte critique, automatisation de la R&D et facilitation de la production d'armes chimiques ou biologiques. Anthropic classe chacun de ces risques au niveau faible a la date de couverture, tout en signalant une incertitude accrue. Le risque de desalignement est releve de tres faible a faible ; les evaluations de R&D montrent des signes d'acceleration mais pas de substitution complete des chercheurs ni de doublement du rythme global ; les risques chimiques et biologiques restent faibles mais non negligeables ou fortement incertains selon le scenario.

Le rapport documente aussi l'usage interne intensif de Claude, le deploiement progressif d'un modele interne plus capable, des mecanismes de monitoring et plusieurs incidents limites mais instructifs de configuration, controle d'acces et couverture de classifieurs.

## 4. Faits validables

- `Model 2` est decrit comme un modele interne non deploye a l'exterieur, globalement legerement plus capable que Claude Mythos 5, sans batterie complete d'evaluations predeploiement au moment couvert.
- Claude Mythos 5 et `Model 2` sont utilises pour la recherche, l'ingenierie et des agents persistants ; Anthropic affirme que Claude redige une large majorite du code fusionne dans ses depots de production.
- Anthropic ne considere pas que ses modeles remplacent l'ensemble de ses chercheurs ni qu'ils aient double son rythme global de progres au 2026-07-15.
- Le deploiement interne de `Model 2` a commence sur des surfaces limitees avec controles renforces avant extension.
- Les controles cites comprennent evaluations comportementales, monitoring, sandboxing, revue de code, classifieurs bloquants, controle des acces et securite des poids.
- Les incidents publies incluent expiration manuelle oubliee, blocage desactive sur une surface, seuil de classifieur mal reporte, fin de flux partiellement non classee, image retiree d'un etage du pipeline et exemption etendue a trop de sieges.
- Une auto-revue par Claude Mythos 5 a identifie des limites et conduit a ajouter des reserves, tout en declarant elle-meme son absence d'independance.

## 5. Hypotheses et elements a surveiller

- Le rapport juge plausible que l'automatisation de la R&D devienne une preoccupation majeure dans les 6 a 12 mois ; cette projection n'est pas integree comme fait durable.
- Les estimations de risque sont qualitatives, dependantes des modeles de menace et susceptibles d'evoluer rapidement.
- La robustesse future des controles depend de la progression relative des capacites d'attaque, de monitoring et d'evasion.

## 6. Limites de la source

- Le rapport est une auto-evaluation Anthropic et certaines parties sont expurgees pour securite ou sensibilite commerciale.
- La date de couverture precede la publication et ne represente pas necessairement l'etat courant apres le 2026-07-15.
- Plusieurs conclusions reposent sur des evaluations internes, parfois saturees ou incompletes.
- L'auto-revue de Claude est une source d'assurance supplementaire, pas une revue externe independante.

## 7. Connaissances candidates et differences integrees

- Claude, sections 3 et 12 : usage interne, `Model 2`, evaluation datee des risques et limites des mesures de capacite.
- Claude, sections 5 et 8 : contournements agentiques, derive operationnelle des garde-fous et workflow de deploiement progressif.
- Claude, section 13 : evaluation de risque revisable et auto-revue non independante.
- Agents IA, sections 5, 8 et 12 : expiration automatique, portee minimale des exemptions, couplage configuration-seuil, tests multimodaux et revue independante.

## 8. Validation

- Statut : GO partiel.
- Validation humaine requise : non pour les differences prudentes integrees ; oui avant toute decision de deploiement a risque eleve.
- Differences non integrees : calendrier previsionnel, details expurges, chiffres de benchmarks, extrapolations de capacites et evaluation absolue du risque hors du contexte Anthropic.
- Point a surveiller : prochaine version du rapport, revues externes, incidents de garde-fous et evolution des seuils RSP.

## 9. Rapport final de traitement

- Fiches permanentes modifiees : `02_IA/Claude/fiche_permanente.md` et `02_IA/Agents IA/fiche_permanente.md`.
- Source deplacee vers : `01_Collecte/sources_brutes/docs/traitees/2026-08_anthropic_risk-report-august-2026.pdf`.
- Decision finale : GO partiel.
