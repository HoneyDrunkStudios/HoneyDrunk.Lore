# OpenClaw Lore ingest run - 2026-06-02

- Timestamp: 2026-06-02 10:07 America/New_York / 2026-06-02 14:07 UTC
- Operator: Honeyclaw / OpenClaw scheduled ingest

## Raw sources ingested: 15

1. `raw/2026-06-02-rss-google-developers-blog-supercharge-your-integration-workflow-with-the-.md` - Google Pay & Wallet Developer MCP server.
2. `raw/2026-06-02-rss-hackread-fake-anthropic-sites-deliver-fileless-infostealer-to-claude-c.md` - fake Claude Code installer / ClickFix-style infostealer reporting.
3. `raw/2026-06-02-rss-hugging-face-ibm-research-beyond-llms-why-scalable-enterprise-ai-adopt.md` - IBM Research agent-logic case studies.
4. `raw/2026-06-02-rss-lohitya-pushkar-thewhiteh4t-llmreaper-dom-based-ai-conversation-exfilt.md` - LLMReaper browser-extension AI conversation exfiltration PoC.
5. `raw/2026-06-02-rss-microsoft-tech-community-hardening-openclaw-on-aks-mitigating-containe.md` - OpenClaw on AKS with Kata microVM isolation.
6. `raw/2026-06-02-rss-microsoft-tech-community-how-acr-artifact-cache-handles-multi-arch-ima.md` - ACR Artifact Cache multi-architecture image and webhook behavior.
7. `raw/2026-06-02-rss-perplexity-research-rethinking-search-as-code-generation.md` - Perplexity Search as Code architecture.
8. `raw/2026-06-02-rss-sean-goedecke-build-agents-not-pipelines.md` - agent-vs-pipeline engineering tradeoffs.
9. `raw/2026-06-02-rss-simon-willison-pasted-file-editor.md` - attachment-aware pasted file editor prototype.
10. `raw/2026-06-02-rss-slack-engineering-slack-ai-the-path-to-multi-cloud.md` - Slack AI multi-cloud LLM routing architecture.
11. `raw/2026-06-02-web-adobe-developer-adobe-photoshop-api-firefly-services.md` - Adobe Photoshop API v2 / Firefly Services.
12. `raw/2026-06-02-web-game-developer-gamemaker-incorporates-claude-code-to-enable-ai-assiste.md` - GameMaker GMRT/GM-CLI with optional Claude Code workflows.
13. `raw/2026-06-02-web-github-changelog-codeql-2-25-5-improves-query-accuracy-for-github-acti.md` - CodeQL 2.25.5 GitHub Actions query improvements.
14. `raw/2026-06-02-web-github-changelog-copilot-usage-metrics-api-adds-cohorts-for-ai-adoptio.md` - Copilot usage metrics adoption cohorts.
15. `raw/2026-06-02-web-github-changelog-updates-to-github-copilot-billing-and-plans.md` - Copilot usage-based billing, budgets, and code-review runner controls.

## Wiki pages created/updated

- Created: `wiki/creative-automation-and-firefly-services.md`.
- Updated: `wiki/agent-evaluation-and-benchmarks.md`, `wiki/ai-agent-harnesses.md`, `wiki/ai-assisted-software-practice.md`, `wiki/ai-coding-agent-security.md`, `wiki/azure-agent-automation-and-identity.md`, `wiki/browser-snapshot-source-quality.md`, `wiki/edge-ai-and-ai-infrastructure-2026.md`, `wiki/gamedev-production-and-community-signals.md`, `wiki/github-actions-platform-operations.md`, `wiki/github-copilot-and-app-token-changes.md`, `wiki/mcp-tool-governance-and-app-surfaces.md`, `wiki/technical-art-community-and-talent-signals.md`.
- Updated indexes: `wiki/indexes/sources.md`, `wiki/indexes/topics.md`, `wiki/indexes/gaps.md`.

## Crystallization from `output/query-*.md`

- Reviewed the existing `output/query-*.md` set by current wiki/source-index coverage. No new durable query facts required crystallization in this pass.
- Non-query `output/signal-review-*.md` files remain review artifacts and were not crystallized under the current Compile contract.

## Contradictions / supersession

- No direct contradictions required supersession.
- Reinforced existing positions that coding-agent security depends on execution-layer controls, browser/extension posture is part of AI data safety, agent benchmark results are harness-specific, and model/provider routing needs cost/latency/quality telemetry.

## Gaps logged

- Browser extension/profile policy for sensitive AI chat and coding-agent web use.
- OpenClaw execution-isolation choice across local microVMs, AKS Kata, Azure dynamic sessions, or hybrid approaches.
- Copilot budgets, default code-review runners, and adoption-cohort reporting before broad Copilot code-review use.
- Better body-boundary extraction for Microsoft Tech Community, Hackread, and Game Developer captures.
- A small Lore retrieval benchmark before adding BM25/vector/graph or Search-as-Code-style infrastructure.
- Photoshop API v1 migration check before Adobe's 2026-07-31 end-of-life date.

## Quality posture

- Decision-usefulness: strongest for GitHub Copilot billing/API changes, CodeQL/GitHub Actions detection changes, ACR Artifact Cache behavior, Adobe API v2 migration date, Slack multi-cloud routing lessons, and browser-extension AI-chat exfiltration controls.
- Weak claims: IBM/Perplexity/Slack benchmark and routing metrics are vendor-authored; GameMaker AI workflow is trade-press reporting; Hackread campaign details are secondary reporting. These are useful signals but need local validation or primary security reports before high-stakes decisions.
- Privacy/safety filtering: malware domains, IPs, command strings, keys, and similar indicators were not copied into wiki pages. Security content was summarized at behavior/control level.
- Source quality: Microsoft Tech Community, Hackread, and Game Developer captures contained duplicate/navigation scaffolding but had recoverable article body facts. This was logged as a source-quality gap.
- Source citations: all promoted claims cite immutable raw filenames.

## Blockers

- None for content quality or validation. Safe to commit/push ingest changes if repository checks pass.
- Validation note: full `git diff --check` reports trailing whitespace inside immutable `raw/` captures; non-raw staged diff check passed, and raw files were not rewritten.
