# OpenClaw Lore Ingest — Last Run

Timestamp: 2026-05-21T09:00:00Z
Operator: Honeyclaw / OpenClaw scheduled ingest

## Raw sources ingested: 8

- raw/2026-05-21-rss-docker-blog-custom-mcp-catalogs-and-profiles-advancing-enterprise-mcp-.md
- raw/2026-05-21-rss-godot-engine-maintenance-release-godot-4-6-3.md
- raw/2026-05-21-rss-martin-fowler-maintainability-sensors-for-coding-agents.md
- raw/2026-05-21-rss-tldr-ai-gemini-3-5-flash-karpathy-joins-anthropic-openai-guaranteed-ca.md
- raw/2026-05-21-rss-tldr-devops-claude-agents-eks-backups-ai-ci-costs.md
- raw/2026-05-21-rss-unity-blog-accelerate-3d-workflows-new-collaboration-and-export-tools-.md
- raw/2026-05-21-web-the-rundown-ai-gemini-s-busy-agentic-day-at-google-i-o.md
- raw/2026-05-21-youtube-microsoft-developer-youtube-test-your-mcp-app-ui-locally-react-fluent-.md

## Wiki pages created/updated

Created:
- wiki/mcp-tool-governance-and-app-surfaces.md

Updated:
- wiki/ai-agent-harnesses.md
- wiki/ai-assisted-software-practice.md
- wiki/browser-snapshot-source-quality.md
- wiki/godot-2026-mobile-and-4-7-cycle.md
- wiki/microsoft-dotnet-ai-stack.md
- wiki/unity-3d-and-realtime-vfx-patterns.md
- wiki/indexes/sources.md
- wiki/indexes/topics.md
- wiki/indexes/gaps.md

## Crystallization from output/query-*.md

- No new durable query output needed crystallization beyond facts already represented by prior compile passes. Latest uncrystallized signal for this run came from new raw sources.

## Contradictions / supersession

- Godot 4.6.3 stable supersedes Godot 4.6.3 RC 2 and Godot 4.6.2 for stable 4.6-line upgrade guidance. Prior RC detail remains preserved as historical release-candidate signal.
- TLDR AI/DevOps title-level claims were not promoted because raw bodies contained sponsor copy; source-quality entries explicitly contradict using those titles as evidence.
- Rundown AI Google I/O/Gemini title/body claims were not promoted because inspected raw lacked decision-grade body text and contained public client config/site scaffolding.

## Gaps logged

- TLDR AI/DevOps extraction still needs body/sponsor separation.
- Rundown AI extraction still needs article-body recovery plus public config stripping.
- HoneyDrunk should decide whether to define approved MCP catalogs and task-specific MCP profiles.
- HoneyDrunk should choose first repositories/rules for coding-agent maintainability sensors.
- HoneyDrunk should validate Unity Studio-to-Editor Export on representative scenes before relying on it.

## Privacy filtering

- Redacted/omitted Rundown AI public client configuration values (Sentry DSNs, Stripe publishable key, VAPID key, Turnstile/site app config) from wiki pages.
- Omitted non-decision-relevant personal Docker Hub namespace/example identity from Docker MCP examples.
- Raw files were not edited or deleted.

## Quality posture

- Decision-useful pages updated with typed entities, explicit relationships, source citations, confidence notes, and HoneyDrunk implications.
- Weak/vendor claims flagged: Docker and Unity sources are vendor-authored; Microsoft item is YouTube metadata; local validation is required before standardization.
- No blockers. Safe to commit/push.
