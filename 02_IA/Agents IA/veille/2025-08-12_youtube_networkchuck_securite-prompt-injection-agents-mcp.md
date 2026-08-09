# 2025-08-12 - YouTube / NetworkChuck - Securite agentique, prompt injection et MCP

## 1. Identification de la source

- Titre : Pirater l'IA est TROP FACILE (cela devrait etre illegal)
- Source : YouTube - NetworkChuck, entretien avec Jason Haddix
- Type : transcription video, entretien pedagogique sponsorise
- Date de publication indiquee : 2025-08-12
- Date de consultation : 2026-08-09
- Fichier source traite : `01_Collecte/sources_brutes/videos/traitees/2026-08-04_youtube_networkchuck_securite-prompt-injection-agents-mcp_transcript.txt`

## 2. Qualification

- Sujet principal : securite des applications et agents IA.
- Sujets secondaires : jailbreak, exfiltration, contenus encodes, appels d'outils, MCP et red teaming.
- Fiabilite : moyenne ; intervenant specialise et demonstrations utiles, sans protocole complet ni sources primaires pour tous les incidents cites.
- Statut : GO partiel.

## 3. Resume synthetique

L'entretien distingue le contournement conversationnel d'une compromission applicative capable d'exfiltrer des donnees ou d'abuser d'outils. Les exemples illustrent les injections directes et indirectes, les contenus encodes et les liens malveillants. La defense proposee combine controles web classiques, validation des entrees et sorties, moindre privilege, journalisation et limitation du rayon d'impact.

## 4. Connaissances candidates

- Cartographier toutes les entrees non fiables et les chemins entre contenu, modele, donnees et outils.
- Tester les injections indirectes dans documents, pages, logs, liens et sorties de connecteurs.
- Appliquer le moindre privilege aux scopes, secrets, fichiers et actions.
- Ne pas substituer un filtre IA aux controles applicatifs, a l'autorisation et a la supervision.

## 5. Limites et elements rejetes

- Les cas Salesforce, Slack et fuite de prompt sont presentes sans dossier technique complet.
- Un pare-feu IA ne garantit pas a lui seul la resistance aux injections.
- L'usage offensif doit rester strictement autorise, isole et documente.

## 6. Differences permanentes

- Integre dans `02_IA/Agents IA/fiche_permanente.md`, section 8 : workflow de securite agentique.

## 7. Decision finale

- Statut final : GO partiel.
- Point ouvert : construire un jeu de tests AOS couvrant injection indirecte, exfiltration, abus d'outils et confinement.
