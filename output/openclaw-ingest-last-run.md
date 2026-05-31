# OpenClaw Lore ingest run - 2026-05-31

- Timestamp: 2026-05-31 10:00 America/New_York / 2026-05-31 14:00 UTC
- Operator: Honeyclaw / OpenClaw scheduled ingest

## Raw sources ingested: 15

1. `raw/2026-05-31-rss-azure-blog-azure-mcp-server-now-available-as-an-mcp-bundle-mcpb.md` - Azure MCP Server MCP Bundle packaging.
2. `raw/2026-05-31-rss-azure-blog-write-azd-hooks-in-python-javascript-typescript-or-net.md` - multi-language `azd` hooks.
3. `raw/2026-05-31-rss-dev-to-gamedev-building-a-data-driven-ability-combat-system.md` - data-driven ability/combat architecture.
4. `raw/2026-05-31-rss-docker-blog-comparing-different-approaches-to-sandboxing.md` - sandboxing strategy comparison for agents.
5. `raw/2026-05-31-rss-docker-blog-the-untrusted-autonomous-workload-how-ai-coding-agents-res.md` - Docker Sandboxes autonomous-agent threat model.
6. `raw/2026-05-31-rss-google-developers-blog-announcing-adk-for-kotlin-and-adk-for-android-0.md` - Google ADK for Kotlin/Android 0.1.0.
7. `raw/2026-05-31-rss-hugging-face-blog-harness-scaffold-and-the-ai-agent-terms-worth-gettin.md` - agent vocabulary: model, scaffold, harness, tools, skills, subagents.
8. `raw/2026-05-31-rss-hugging-face-blog-itbench-aa-frontier-models-score-below-50-on-the-fir.md` - ITBench-AA SRE benchmark.
9. `raw/2026-05-31-rss-martin-fowler-the-vibesec-reckoning.md` - AI-assisted prototype security controls.
10. `raw/2026-05-31-rss-openai-via-tldr-ai-building-self-improving-tax-agents-with-codex.md` - Tax AI self-improvement loop with Codex.
11. `raw/2026-05-31-rss-opentelemetry-blog-how-skyscanner-scales-opentelemetry-managing-collec.md` - Skyscanner OpenTelemetry collector operations.
12. `raw/2026-05-31-rss-realtimevfx-baking-animated-maya-procedural-shaders-into-texture-seque.md` - Maya procedural shader baking to texture sequences.
13. `raw/2026-05-31-web-anthropic-engineering-how-we-contain-claude-across-products.md` - Anthropic Claude containment engineering.
14. `raw/2026-05-31-web-claude-blog-agent-view-in-claude-code.md` - Claude Code agent view.
15. `raw/2026-05-31-web-openai-a-shared-playbook-for-trustworthy-third-party-evaluations.md` - OpenAI third-party evaluation methodology.

## Wiki pages created/updated

- Created: `wiki/agent-evaluation-and-benchmarks.md`.
- Updated: `wiki/ai-agent-harnesses.md`, `wiki/ai-assisted-software-practice.md`, `wiki/ai-coding-agent-security.md`, `wiki/azure-agent-automation-and-identity.md`, `wiki/claude-platform-2026.md`, `wiki/gamedev-production-and-community-signals.md`, `wiki/google-agent-platform-and-gemini-api-2026.md`, `wiki/mcp-tool-governance-and-app-surfaces.md`, `wiki/opentelemetry-genai-observability-and-ecosystem.md`, `wiki/technical-art-community-and-talent-signals.md`, `wiki/unity-3d-and-realtime-vfx-patterns.md`.
- Updated indexes: `wiki/indexes/sources.md`, `wiki/indexes/topics.md`, `wiki/indexes/gaps.md`.

## Crystallization from `output/query-*.md`

- Reviewed existing query outputs by filename and current wiki coverage. No new durable query facts required crystallization in this pass; recent query facts were already represented by prior wiki compile additions.
- Non-query `output/signal-review-*.md` files were not crystallized because the Compile contract only names `query-*.md` outputs for this step.

## Contradictions / supersession

- No direct contradictions required resolution.
- Added reinforced posture that agent benchmark scores are harness- and budget-specific; this limits over-reading older model-ranking notes without superseding them.
- Added reinforced posture that environment containment is the primary blast-radius boundary for coding agents; prompt/security-context rules are useful guidance but do not supersede deterministic gates.

## Gaps logged

- HoneyDrunk model-routing eval design: controlled comparison versus maximum elicitation and required harness/budget metadata.
- SRE/agent-ops benchmark design with strict root-cause false-positive penalties.
- Post-agent shared-workspace checks for host-executed artifacts.
- AI security context file plus deterministic sensor rollout.
- Azure MCP `.mcpb` provenance and least-privilege approval policy.
- Google ADK Android hybrid-agent prototype candidates and local-data boundaries.
- Data-driven ability/combat schema and telemetry taxonomy.
- OpenTelemetry collector/base-image standardization.
- Maya procedural shader baking validation for stylized asset interchange.

## Quality posture

- Decision-usefulness: strong for official OpenAI, Anthropic, Microsoft/Azure, Google, OpenTelemetry, and Docker platform-control sources; useful for methodology and vocabulary.
- Weak claims: ITBench-AA leaderboard values are a 2026-05-31 snapshot and should be checked against the live leaderboard before routing decisions; Docker and Anthropic sources are vendor-authored; RealtimeVFX and DEV.to game sources require local validation.
- Privacy/safety filtering: no secrets, credentials, private network addresses, exploit payloads, or unsafe PII copied into wiki pages. Public comments embedded in Hugging Face captures were not promoted except for high-level MCP vocabulary signal.
- Source citations: all promoted claims cite immutable raw filenames.
- Decision-usefulness notes: strongest new decisions are around evaluation reporting discipline, agent containment review, MCP bundle governance, and OTel standardization.

## Blockers

- None for content quality or validation. Safe to commit/push ingest changes.
