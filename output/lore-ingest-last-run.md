# Lore Ingest - Last Run

Timestamp: 2026-06-28T10:06:13.2031414-04:00
Mode: ingest/compile

## Raw sources ingested

Count: 15

- `raw/2026-06-28-rss-80-level-developing-valheim-style-creature-collection-mmo-adventure.md`
- `raw/2026-06-28-rss-80-level-miris-built-a-car-configurator-without-pixel-streaming.md`
- `raw/2026-06-28-rss-80-level-setting-up-vegetation-for-alien-planet-in-3d.md`
- `raw/2026-06-28-rss-azure-sdk-blog-azure-developer-cli-azd.md`
- `raw/2026-06-28-rss-azure-sdk-blog-azure-functions-mcp-extension-what-s-new-at-build-2026.md`
- `raw/2026-06-28-rss-docker-blog-eu-cyber-resilience-act-cra-overview.md`
- `raw/2026-06-28-rss-docker-blog-sbom-generation-for-container-workflows.md`
- `raw/2026-06-28-rss-github-changelog-actions-actions-steps-can-now-be-run-in-parallel.md`
- `raw/2026-06-28-rss-github-changelog-actions-more-control-over-your-github-hosted-runners.md`
- `raw/2026-06-28-rss-hugging-face-blog-run-a-vllm-server-on-hf-jobs-in-one-command.md`
- `raw/2026-06-28-rss-simon-willison-what-happened-after-2-000-people-tried-to-hack-my-ai-as.md`
- `raw/2026-06-28-rss-system-design-newsletter-a2a-protocol.md`
- `raw/2026-06-28-rss-thoughtworks-insights-build-an-ai-knowledge-fabric-for-your-organizati.md`
- `raw/2026-06-28-web-docker-blog-what-s-next-for-mcp-security.md`
- `raw/2026-06-28-web-owasp-genai-security-project-ai-security-solutions-landscape-for-agent.md`

## Wiki pages created/updated

Created:

- `wiki/container-supply-chain-and-compliance.md`

Updated:

- `wiki/ai-coding-agent-security.md`
- `wiki/azure-agent-automation-and-identity.md`
- `wiki/edge-ai-and-ai-infrastructure-2026.md`
- `wiki/gamedev-production-and-community-signals.md`
- `wiki/github-actions-platform-operations.md`
- `wiki/indexes/gaps.md`
- `wiki/indexes/sources.md`
- `wiki/indexes/topics.md`
- `wiki/llm-wiki-and-knowledge-formats.md`
- `wiki/mcp-tool-governance-and-app-surfaces.md`
- `wiki/multi-agent-architectures.md`
- `wiki/technical-art-community-and-talent-signals.md`
- `wiki/web-3d-runtime-tradeoffs.md`

## Contradictions resolved

- None. New sources reinforced or extended existing claims; no newer source contradicted a prior wiki claim strongly enough to supersede it.

## Gaps logged

Count: 9

- CRA applicability and missing container compliance evidence for HoneyDrunk products.
- Build-time SBOM attestation and generator-pinning coverage.
- Safe adoption criteria for GitHub Actions parallel steps.
- Hosted runner group/default-label policy for HoneyDrunk workflows.
- Azure Functions MCP hosting suitability and auth/schema requirements.
- MCP gateway/catalog evaluation for tool-metadata and secret-scope threats.
- HF Jobs model-serving benchmark criteria.
- A2A handoff candidates and primary spec/SDK evidence needs.
- Adaptive WebXR/spatial-streaming validation criteria.

## Crystallization

- Existing `output/query-*.md` files were checked. No new query output required promotion in this pass.
- Signal-review outputs are not `query-*.md` crystallization inputs under the current Compile rule and were left as episodic reporting artifacts.

## Blockers

- No content-quality blocker for the 15-source compile.
- The worktree already contained unrelated or pre-existing scheduled-job changes before this pass, including Lore/OpenClaw rename work, sourcing tool changes, signal-review outputs, and `.obsidian/graph.json`. They were not reverted.
- Some pre-existing sourcing-tool deletions/renames need final review before a safe all-repo commit/push decision.

## Quality posture

- Raw files were treated as immutable and were not edited.
- Claims were added with source links, confidence notes, typed entities, explicit relationships, and HoneyDrunk implications.
- Low-detail or vendor-promotional captures were marked as weak/watchlist evidence rather than promoted to strong operational truth.
- No secrets, credentials, tokens, unsafe PII, exploit payloads, or reusable bypass instructions were copied into wiki content.
- Privacy redactions: none required beyond summarizing security mechanics at control level.
- Decision-usefulness is good for scouting and backlog shaping; legal/compliance conclusions, vendor benchmark claims, MCP gateway adoption, A2A adoption, and HF Jobs usage still require local validation or primary-spec review before implementation.
