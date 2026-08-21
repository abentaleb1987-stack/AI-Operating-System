# 2026-08-20 - YouTube / Alejavi Rivera - DeepSeek Harness, plugins et modeles locaux

## 1. Identification de la source

- Titre source : DeepSeek vient de bouleverser le monde de l'IA ! Ils ont lance leur framework gratuitement
- Source : YouTube - Alejavi Rivera
- Reference produit fournie : `https://deepseek.com/harness/en/`
- Type : transcription d'une presentation et demonstration non officielle, doublee automatiquement
- Date de publication indiquee : 2026-08-20
- Date de consultation : 2026-08-21
- Fichier source traite : `01_Collecte/sources_brutes/videos/traitees/2026-08-20_youtube_alejavi-rivera_deepseek-harness-plugins-modeles-locaux_transcript.txt`

## 2. Qualification

- IA / outil principal : DeepSeek Harness.
- Outils secondaires : DeepSeek V4, Ollama, fournisseurs compatibles, plugins, agents personnalises et GLM.
- Domaine : runtime agentique, extensibilite, permissions, tracabilite et portabilite de modeles.
- Fiabilite : moyenne pour les manipulations montrees ; faible pour les prix, performances et annonces de modeles.
- Priorite : moyenne, car une fiche permanente DeepSeek Harness existe deja.
- Statut : GO partiel par confirmation, sans nouvelle integration permanente.

## 3. Resume synthetique

La video installe DeepSeek Harness, configure un espace de travail et une cle API, puis montre plusieurs cas : operations sur fichiers, creation d'une application, generation de plugins, creation d'un agent d'audit et connexion de fournisseurs ou modeles locaux via Ollama. L'auteur insiste sur l'architecture plugin et la visibilite de la trajectoire. Les dernieres parties melangent demonstrations, promotion d'un outil sponsorise et annonces recentes de modeles.

## 4. Faits validables

- La demonstration retrouve les caracteristiques deja documentees dans AOS : execution locale de l'interface, architecture plugin, espaces de travail et trajectoire visible.
- Elle montre des niveaux d'acces a un dossier ainsi que des actions sur fichiers, ce qui confirme l'importance d'un test du moindre privilege.
- Elle montre la creation de plugins et d'agents personnalises, sans audit du code genere ni de leur isolation.
- Elle illustre la selection de fournisseurs et de modeles locaux, mais la compatibilite exacte depend de la version du Harness et des adaptateurs.

## 5. Hypotheses, marketing et limites

- Les affirmations de gratuite, d'usage illimite, de cout, de vitesse, de classement et de compatibilite universelle ne sont pas reproduites.
- Le nombre d'etoiles GitHub, les versions DeepSeek V4/V5, Qwen et GLM ainsi que leurs performances sont instables.
- Les applications, plugins et correctifs d'audit sont des demonstrations ponctuelles et non des validations de robustesse ou de securite.
- Topview MCP et les formations de l'auteur font l'objet de passages promotionnels.
- Le doublage automatique et les erreurs de transcription rendent certains noms et commandes ambigus.

## 6. Differences permanentes

- Aucune nouvelle modification : `02_IA/DeepSeek/fiche_permanente.md` documente deja l'architecture plugin, le statut de preview, les permissions, la portabilite et le workflow d'evaluation isolee.
- La source renforce les points a tester sur les permissions de dossier, la provenance des plugins et les adaptateurs de modeles.

## 7. Decision finale

- Statut final : GO partiel par confirmation.
- Elements rejetes : claims de prix, gratuit, performance, compatibilite, securite et annonces de modeles.
- Prochaine action : conserver le protocole existant avec version epinglee, environnement jetable, permissions minimales, plugins audites et comparaison reproductible des adaptateurs.
