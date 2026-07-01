# Audit journalier AOS - 2026-07-01

## Resume executif

- Decision d'audit : Audit Aion recommande
- Niveau de risque maximal : eleve
- Commit audite : 802800a
- Periode auditee : Dernieres 24h ou fallback 10 commits recents
- Rapport genere le : 2026-07-01 20:29:27
- Alertes prioritaires Aion : 7
- Alertes traitees ou attenuees : 0
- Alertes totales detectees : 16

## À traiter par Aion

- eleve - `02_IA/Agents IA/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible. Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- eleve - `02_IA/Aside/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible. Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- eleve - `02_IA/ChatGPT/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible. Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- eleve - `02_IA/Claude Code/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible. Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- eleve - `02_IA/Claude/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible. Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- eleve - `02_IA/Codex/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible. Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- eleve - `02_IA/Gemini/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible. Recommandation : Verifier que le sujet est principal ou durable avant conservation.

## Alertes traitées ou déjà atténuées

- Aucune alerte traitee ou attenuee detectee.

## Periode auditee

Dernieres 24h ou fallback 10 commits recents

## Commits analyses

- `802800a` - 2026-07-01 22:24:36 +0200 - Audit - ci(aos): fix daily audit workflow history and encoding

## Classification des commits

### Knowledge batch

- Aucun commit.

### Protocol / system

- Aucun commit.

### Maintenance

- Aucun commit.

### Audit

- `802800a` - 2026-07-01 22:24:36 +0200 - ci(aos): fix daily audit workflow history and encoding

## Commits ignorés pour audit connaissance

- `802800a` - 2026-07-01 22:24:36 +0200 - Audit - ci(aos): fix daily audit workflow history and encoding

## Fichiers crees

- A .github/workflows/aos-daily-audit.yml
- A .gitkeep
- A 00_Documentation/README.md
- A 00_System/audits/daily/.gitkeep
- A 00_System/audits/daily/2026-07-01_audit-journalier-aos-calibration-final.md
- A 00_System/audits/daily/2026-07-01_audit-journalier-aos.md
- A 00_System/audits/templates/TEMPLATE_DAILY_AUDIT.md
- A 00_System/automation/AOS_DAILY_AUDIT_DESIGN.md
- A 00_System/automation/AOS_GIT_RULES.md
- A 00_System/automation/AOS_PROCESS.md
- A 00_System/automation/AOS_ROUTING_RULES.md
- A 00_System/automation/CODEX_GO_PROMPT.md
- A 00_System/automation/TEMPLATE_RAPPORT_FINAL.md
- A 00_System/automation/TEMPLATE_VEILLE.md
- A 00_System/scripts/aos_daily_audit.py
- A 01_Collecte/README.md
- A 01_Collecte/sources_brutes/articles/a_traiter/README.md
- A 01_Collecte/sources_brutes/articles/traitees/.gitkeep
- A 01_Collecte/sources_brutes/docs/a_traiter/README.md
- A 01_Collecte/sources_brutes/docs/traitees/.gitkeep
- A 01_Collecte/sources_brutes/tests_personnels/a_traiter/README.md
- A 01_Collecte/sources_brutes/tests_personnels/traitees/.gitkeep
- A 01_Collecte/sources_brutes/videos/a_traiter/README.md
- A 01_Collecte/sources_brutes/videos/traitees/.gitkeep
- A 01_Collecte/sources_brutes/videos/traitees/2026-06-27_youtube_melvynx_gpt-5-6-sol-terra-luna-availability-watch_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-06-30_youtube_melvynx_aside-ai-browser-agent-test_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-06-30_youtube_vision-ia_hermes-agent-installation-vps-telegram_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_labo-des-reseaux_gemini-3-guide_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_melvynx_claude-sonnet-5-agentic-model-evaluation_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_mike-codeur_hermes-vps-tailscale-openwebui_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_claude-code-101-agents_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_claude-code-obsidian-second-brain_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_claude-mythos-fable-agents_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_claude-opus-4-8-workflows_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_gemini-3-5-flash-agentique_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_hermes-2-claude-code-mcp-lm-studio_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_hermes-agent-business-automation_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_obsidian-notebooklm-codex-second-brain_transcript.txt
- A 02_IA/Agents IA/fiche_permanente.md
- A 02_IA/Aion/fiche_permanente.md
- A 02_IA/Aside/fiche_permanente.md
- A 02_IA/Aside/veille/2026-06-30_youtube_melvynx_aside-ai-browser-agent-test.md
- A 02_IA/ChatGPT/fiche_permanente.md
- A 02_IA/ChatGPT/veille/2026-06-27_youtube_melvynx_gpt-5-6-sol-terra-luna-availability-watch.md
- A 02_IA/Claude Code/fiche_permanente.md
- A 02_IA/Claude Code/veille/2026-07-01_youtube_parlons-ia_claude-code-101-agents.md
- A 02_IA/Claude Code/veille/2026-07-01_youtube_parlons-ia_claude-obsidian-second-brain.md
- A 02_IA/Claude/fiche_permanente.md
- A 02_IA/Claude/veille/2026-07-01_youtube_melvynx_claude-sonnet-5-agentic-model-evaluation.md
- A 02_IA/Claude/veille/2026-07-01_youtube_parlons-ia_claude-mythos-fable-agents.md
- A 02_IA/Claude/veille/2026-07-01_youtube_parlons-ia_claude-opus-4-8-workflows.md
- A 02_IA/Codex/fiche_permanente.md
- A 02_IA/Codex/veille/2026-07-01_youtube_parlons-ia_obsidian-notebooklm-codex-second-brain.md
- A 02_IA/Cursor/fiche_permanente.md
- A 02_IA/Gemini/fiche_permanente.md
- A 02_IA/Gemini/veille/2026-07-01_youtube_labo-des-reseaux_gemini-3-guide.md
- A 02_IA/Gemini/veille/2026-07-01_youtube_parlons-ia_gemini-3-5-flash-agentique.md
- A 02_IA/Hermes/fiche_permanente.md
- A 02_IA/Hermes/veille/2026-06-30_youtube_vision-ia_hermes-agent-installation-vps-telegram.md
- A 02_IA/Hermes/veille/2026-07-01_youtube_mike-codeur_hermes-vps-tailscale-openwebui.md
- A 02_IA/Hermes/veille/2026-07-01_youtube_parlons-ia_hermes-2-claude-code-mcp-lm-studio.md
- A 02_IA/Hermes/veille/2026-07-01_youtube_parlons-ia_hermes-agent-business-automation.md
- A 02_IA/Lovable/fiche_permanente.md
- A 02_IA/MCP/fiche_permanente.md
- A 02_IA/OpenRouter/fiche_permanente.md
- A 02_IA/Orchestration IA/fiche_permanente.md
- A 02_IA/Perplexity/fiche_permanente.md
- A 02_IA/README.md
- A 02_IA/TestSprite/fiche_permanente.md
- A 02_IA/TestSprite/veille/2026-06-30_youtube_melvynx_testsprite-agent-testing-workflow.md
- A 03_Frameworks/README.md
- A 03_Frameworks/knowledge_decision/README.md
- A 03_Frameworks/knowledge_organization/README.md
- A 03_Frameworks/knowledge_processing/README.md
- A 04_Templates/README.md
- A 04_Templates/template_comparatif_ia.md
- A 04_Templates/template_decision.md
- A 04_Templates/template_fiche_permanente_ia.md
- A 04_Templates/template_fiche_veille.md
- A 04_Templates/template_prompt.md
- A 04_Templates/template_retour_experience.md
- A 04_Templates/template_workflow.md
- A 05_Archives/README.md
- A 06_Scripts/README.md
- A 07_Standards/README.md
- A 07_Standards/documentation_standard.md
- A 07_Standards/git_standard.md
- A 07_Standards/knowledge_quality_standard.md
- A 07_Standards/markdown_standard.md
- A 07_Standards/naming_standard.md
- A 99_System/README.md
- A 99_System/adr/ADR-0001-architecture-frameworks-standards.md
- A 99_System/agents/instructions_agents.md
- A 99_System/git/conventions_git.md
- A 99_System/schemas/schema_fiche_permanente.md
- A 99_System/schemas/schema_fiche_veille.md
- A 99_System/schemas/schema_source.md
- A CHANGELOG.md
- A PROJECT_RULES.md
- A README.md

## Fichiers modifies

- Aucun element detecte.

## Fiches permanentes impactees

- A 02_IA/Agents IA/fiche_permanente.md
- A 02_IA/Aion/fiche_permanente.md
- A 02_IA/Aside/fiche_permanente.md
- A 02_IA/ChatGPT/fiche_permanente.md
- A 02_IA/Claude Code/fiche_permanente.md
- A 02_IA/Claude/fiche_permanente.md
- A 02_IA/Codex/fiche_permanente.md
- A 02_IA/Cursor/fiche_permanente.md
- A 02_IA/Gemini/fiche_permanente.md
- A 02_IA/Hermes/fiche_permanente.md
- A 02_IA/Lovable/fiche_permanente.md
- A 02_IA/MCP/fiche_permanente.md
- A 02_IA/OpenRouter/fiche_permanente.md
- A 02_IA/Orchestration IA/fiche_permanente.md
- A 02_IA/Perplexity/fiche_permanente.md
- A 02_IA/TestSprite/fiche_permanente.md

## Nouvelles fiches permanentes creees

- A 02_IA/Agents IA/fiche_permanente.md
- A 02_IA/Aion/fiche_permanente.md
- A 02_IA/Aside/fiche_permanente.md
- A 02_IA/ChatGPT/fiche_permanente.md
- A 02_IA/Claude Code/fiche_permanente.md
- A 02_IA/Claude/fiche_permanente.md
- A 02_IA/Codex/fiche_permanente.md
- A 02_IA/Cursor/fiche_permanente.md
- A 02_IA/Gemini/fiche_permanente.md
- A 02_IA/Hermes/fiche_permanente.md
- A 02_IA/Lovable/fiche_permanente.md
- A 02_IA/MCP/fiche_permanente.md
- A 02_IA/OpenRouter/fiche_permanente.md
- A 02_IA/Orchestration IA/fiche_permanente.md
- A 02_IA/Perplexity/fiche_permanente.md
- A 02_IA/TestSprite/fiche_permanente.md

## Fiches transversales modifiees

- Aucun element detecte.

## Fiches de veille creees

- A 02_IA/Aside/veille/2026-06-30_youtube_melvynx_aside-ai-browser-agent-test.md
- A 02_IA/ChatGPT/veille/2026-06-27_youtube_melvynx_gpt-5-6-sol-terra-luna-availability-watch.md
- A 02_IA/Claude Code/veille/2026-07-01_youtube_parlons-ia_claude-code-101-agents.md
- A 02_IA/Claude Code/veille/2026-07-01_youtube_parlons-ia_claude-obsidian-second-brain.md
- A 02_IA/Claude/veille/2026-07-01_youtube_melvynx_claude-sonnet-5-agentic-model-evaluation.md
- A 02_IA/Claude/veille/2026-07-01_youtube_parlons-ia_claude-mythos-fable-agents.md
- A 02_IA/Claude/veille/2026-07-01_youtube_parlons-ia_claude-opus-4-8-workflows.md
- A 02_IA/Codex/veille/2026-07-01_youtube_parlons-ia_obsidian-notebooklm-codex-second-brain.md
- A 02_IA/Gemini/veille/2026-07-01_youtube_labo-des-reseaux_gemini-3-guide.md
- A 02_IA/Gemini/veille/2026-07-01_youtube_parlons-ia_gemini-3-5-flash-agentique.md
- A 02_IA/Hermes/veille/2026-06-30_youtube_vision-ia_hermes-agent-installation-vps-telegram.md
- A 02_IA/Hermes/veille/2026-07-01_youtube_mike-codeur_hermes-vps-tailscale-openwebui.md
- A 02_IA/Hermes/veille/2026-07-01_youtube_parlons-ia_hermes-2-claude-code-mcp-lm-studio.md
- A 02_IA/Hermes/veille/2026-07-01_youtube_parlons-ia_hermes-agent-business-automation.md
- A 02_IA/TestSprite/veille/2026-06-30_youtube_melvynx_testsprite-agent-testing-workflow.md

## Sources traitees

- A 01_Collecte/sources_brutes/articles/traitees/.gitkeep
- A 01_Collecte/sources_brutes/docs/traitees/.gitkeep
- A 01_Collecte/sources_brutes/tests_personnels/traitees/.gitkeep
- A 01_Collecte/sources_brutes/videos/traitees/.gitkeep
- A 01_Collecte/sources_brutes/videos/traitees/2026-06-27_youtube_melvynx_gpt-5-6-sol-terra-luna-availability-watch_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-06-30_youtube_melvynx_aside-ai-browser-agent-test_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-06-30_youtube_vision-ia_hermes-agent-installation-vps-telegram_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_labo-des-reseaux_gemini-3-guide_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_melvynx_claude-sonnet-5-agentic-model-evaluation_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_mike-codeur_hermes-vps-tailscale-openwebui_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_claude-code-101-agents_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_claude-code-obsidian-second-brain_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_claude-mythos-fable-agents_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_claude-opus-4-8-workflows_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_gemini-3-5-flash-agentique_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_hermes-2-claude-code-mcp-lm-studio_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_hermes-agent-business-automation_transcript.txt
- A 01_Collecte/sources_brutes/videos/traitees/2026-07-01_youtube_parlons-ia_obsidian-notebooklm-codex-second-brain_transcript.txt

## Toutes les alertes détectées

### AUDIT-20260701-001 - creation abusive de fiche permanente

- Risque : eleve
- Fichier concerne : `02_IA/Agents IA/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-002 - creation abusive de fiche permanente

- Risque : moyen
- Fichier concerne : `02_IA/Aion/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee dans la periode auditee.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-003 - creation abusive de fiche permanente

- Risque : eleve
- Fichier concerne : `02_IA/Aside/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-004 - creation abusive de fiche permanente

- Risque : eleve
- Fichier concerne : `02_IA/ChatGPT/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-005 - creation abusive de fiche permanente

- Risque : eleve
- Fichier concerne : `02_IA/Claude Code/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-006 - creation abusive de fiche permanente

- Risque : eleve
- Fichier concerne : `02_IA/Claude/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-007 - creation abusive de fiche permanente

- Risque : eleve
- Fichier concerne : `02_IA/Codex/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-008 - creation abusive de fiche permanente

- Risque : moyen
- Fichier concerne : `02_IA/Cursor/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee dans la periode auditee.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-009 - creation abusive de fiche permanente

- Risque : eleve
- Fichier concerne : `02_IA/Gemini/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-010 - creation abusive de fiche permanente

- Risque : eleve
- Fichier concerne : `02_IA/Hermes/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-011 - creation abusive de fiche permanente

- Risque : moyen
- Fichier concerne : `02_IA/Lovable/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee dans la periode auditee.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-012 - creation abusive de fiche permanente

- Risque : moyen
- Fichier concerne : `02_IA/MCP/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee dans la periode auditee.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-013 - creation abusive de fiche permanente

- Risque : moyen
- Fichier concerne : `02_IA/OpenRouter/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee dans la periode auditee.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-014 - creation abusive de fiche permanente

- Risque : eleve
- Fichier concerne : `02_IA/Orchestration IA/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-015 - creation abusive de fiche permanente

- Risque : moyen
- Fichier concerne : `02_IA/Perplexity/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee dans la periode auditee.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

### AUDIT-20260701-016 - creation abusive de fiche permanente

- Risque : eleve
- Fichier concerne : `02_IA/TestSprite/fiche_permanente.md`
- Observation : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- Recommandation : Verifier que le sujet est principal ou durable avant conservation.
- Decision attendue : Aion / utilisateur / Codex sur demande

## Risques par categorie

### Risque faible

- Aucun risque detecte.

### Risque moyen

- `02_IA/Aion/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee dans la periode auditee.
- `02_IA/Cursor/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee dans la periode auditee.
- `02_IA/Lovable/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee dans la periode auditee.
- `02_IA/MCP/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee dans la periode auditee.
- `02_IA/OpenRouter/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee dans la periode auditee.
- `02_IA/Perplexity/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee dans la periode auditee.

### Risque eleve

- `02_IA/Agents IA/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- `02_IA/Aside/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- `02_IA/ChatGPT/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- `02_IA/Claude Code/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- `02_IA/Claude/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- `02_IA/Codex/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- `02_IA/Gemini/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- `02_IA/Hermes/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- `02_IA/Orchestration IA/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.
- `02_IA/TestSprite/fiche_permanente.md` - creation abusive de fiche permanente : Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible.

### Risque bloquant

- Aucun risque detecte.

## Recommandations

- Verifier que le sujet est principal ou durable avant conservation.

## Etat Git final

```text
(propre)
```

## Limites de l'audit

- Audit statique et heuristique.
- Ne verifie pas la veracite externe des informations.
- Ne remplace pas la decision qualitative d'Aion.
- Ne corrige aucun contenu automatiquement.
