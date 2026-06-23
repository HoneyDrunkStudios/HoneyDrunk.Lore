# OpenClaw Lore Ingest - Last Run

Timestamp: 2026-06-23T13:16:30.6336226-04:00
Mode: ingest/compile

## Raw sources ingested

Count: 15

- raw/2026-06-23-rss-architecture-notes-arc-notes-weekly-104-telluride.md
- raw/2026-06-23-rss-architecture-notes-arc-notes-weekly-106-arrowhead.md
- raw/2026-06-23-rss-azure-blog-azure-sdk-release-may-2026.md
- raw/2026-06-23-rss-game-developer-how-a-12-year-wait-made-alien-isolation-2-a-better-sequ.md
- raw/2026-06-23-rss-polycount-learning-blender-and-texturing.md
- raw/2026-06-23-rss-tech-artists-org-free-tool-materialist-a-material-manager-shelf-for-ma.md
- raw/2026-06-23-rss-tldr-ai-knowledge-agents-beat-frontier-models-with-better-structure-18.md
- raw/2026-06-23-rss-tldr-ai-openai-launches-new-security-tools-and-updates-gpt-5-5-cyber-2.md
- raw/2026-06-23-rss-tldr-ai-sakana-fugu-3-minute-read.md
- raw/2026-06-23-rss-tldr-ai-the-text-in-claude-code-s-extended-thinking-output-is-not-auth.md
- raw/2026-06-23-rss-tldr-devops-codebase-memory-mcp-github-repo.md
- raw/2026-06-23-rss-tldr-devops-jcode-github-repo.md
- raw/2026-06-23-rss-tldr-infosec-a-public-sentry-key-is-all-it-takes-to-hijack-claude-code.md
- raw/2026-06-23-rss-tldr-infosec-making-secret-scanning-more-trustworthy-reducing-false-po.md
- raw/2026-06-23-rss-unity-blog-how-playrix-is-growing-township-with-unity-ads-d28-iap-roas.md

## Wiki pages created/updated

Created:

- None

Updated:

- wiki/agent-evaluation-and-benchmarks.md
- wiki/ai-agent-harnesses.md
- wiki/ai-assisted-software-practice.md
- wiki/ai-coding-agent-security.md
- wiki/azure-agent-automation-and-identity.md
- wiki/azure-sdk-for-rust.md
- wiki/browser-snapshot-source-quality.md
- wiki/gamedev-production-and-community-signals.md
- wiki/indexes/gaps.md
- wiki/indexes/sources.md
- wiki/indexes/topics.md
- wiki/llm-wiki-and-knowledge-formats.md
- wiki/mcp-tool-governance-and-app-surfaces.md
- wiki/microsoft-dotnet-ai-stack.md
- wiki/technical-art-community-and-talent-signals.md
- wiki/unity-3d-and-realtime-vfx-patterns.md

## Contradictions resolved

- None. The June 23 batch strengthened existing claims around agent harnesses, MCP governance, agent security, knowledge-agent formats, Azure SDK/agent retrieval, technical art, Unity UA, and game production without superseding prior wiki claims.

## Gaps logged

Count: 7

- HoneyDrunk externally influenced telemetry/issue/log MCP integrations and tool-output-to-command gates.
- codebase-memory-mcp and Jcode approved-tool review criteria.
- Agent audit trail requirements when model "thinking" summaries are not reasoning logs.
- Lore/OpenClaw knowledge-agent retrieval benchmark design.
- Azure AI Search knowledge-base and Agent Server preview spike criteria.
- DCC/material tool repository, license, security, and workflow review.
- Mobile UA metrics for Unity Ads/Vector/D28-style ROAS evaluation.

## Crystallization

- Existing `output/query-*.md` files were checked against the current query output set. No new well-structured, cited query output requiring crystallization was found, and no query-derived facts were promoted in this pass.

## Blockers

- None for maintained wiki quality.
- Several sources were qualified for source quality: Architecture Notes items were older than the sourcing date, Game Developer and Polycount captures had substantial boilerplate, and Sakana Fugu came through ThreadReader/social capture.
- Existing local changes outside this ingest scope were left untouched and should be reviewed separately before any broader publish decision: `.obsidian/graph.json`, `README.md`, `output/openclaw-sourcing-last-run.md`, `sourcing-playbook.md`, sourcing prompt/tool files, `tools/openclaw_lore_source_birdclaw.py`, and untracked `output/signal-review-2026-06-19.md` / `output/signal-review-2026-06-20.md` / `output/signal-review-2026-06-21.md` / `output/signal-review-2026-06-22.md`.

## Quality posture

- Pages include source citations, confidence notes, typed entities, explicit relationship language, HoneyDrunk implications, and source-quality notes where relevant.
- Vendor/product/social/secondary sources are marked as product, platform, social, or secondary evidence and require local validation before implementation, procurement, routing, security, or operational changes.
- Security-sensitive sources were summarized at control, policy, validation, telemetry, and audit level. No secrets, credentials, tokens, unsafe PII, exploit payloads, or reusable bypass instructions were copied into wiki pages.
- Raw files were treated as immutable and were not edited.
- Decision-usefulness is strong for externally influenced MCP/tool-output risk, approved-tool criteria, knowledge-agent retrieval eval design, Azure managed-retrieval scouting, and agent audit logging. Technical-art, Unity UA, Fugu, and secondary OpenAI cyber items remain scouting signals pending primary-source or local validation.
