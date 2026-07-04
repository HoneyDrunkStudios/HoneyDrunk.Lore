# Lore Ingest - Last Run

Timestamp: 2026-07-04T10:10:25.5169554-04:00
Mode: ingest/compile

## Raw sources ingested

Count: 15

- `raw/2026-07-04-web-agent-assisted-sglang-development-an-initial-exploration.md`
- `raw/2026-07-04-web-bliki-future-of-software-development.md`
- `raw/2026-07-04-web-browser-tools-for-github-copilot-in-vs-code-are-generally-available-github-cha.md`
- `raw/2026-07-04-web-build-agentic-full-stack-apps-with-genkit.md`
- `raw/2026-07-04-web-contextforge.md`
- `raw/2026-07-04-web-copilot-cli-no-longer-needs-a-personal-access-token-in-github-actions-github-c.md`
- `raw/2026-07-04-web-hand-tracking-in-unity-xr-hand-capture-simulation.md`
- `raw/2026-07-04-web-more-details-on-fable-5-s-cyber-safeguards-and-our-jailbreak-framework.md`
- `raw/2026-07-04-web-net-8-and-net-9-will-reach-end-of-support-on-november-10-2026-net-blog.md`
- `raw/2026-07-04-web-packaging-and-package-identity-for-net-apps-with-winapp-cli-on-windows-net-blo.md`
- `raw/2026-07-04-web-phantom-squatting-ai-hallucinated-domains-as-a-software-supply-chain-vector.md`
- `raw/2026-07-04-web-soatok-s-informal-guide-to-threat-models-dhole-moments.md`
- `raw/2026-07-04-web-unity-adds-xr-glasses-support-for-android.md`
- `raw/2026-07-04-web-vulnerability-and-malware-checks-in-uv.md`
- `raw/2026-07-04-web-why-we-built-adk-2-0.md`

## Wiki pages created/updated

Created:

- None.

Updated:

- `wiki/ai-agent-harnesses.md`
- `wiki/ai-assisted-software-practice.md`
- `wiki/ai-coding-agent-security.md`
- `wiki/claude-platform-2026.md`
- `wiki/dotnet-runtime-and-mobile-2026.md`
- `wiki/github-actions-platform-operations.md`
- `wiki/github-copilot-and-app-token-changes.md`
- `wiki/google-agent-platform-and-gemini-api-2026.md`
- `wiki/indexes/audit.md`
- `wiki/indexes/gaps.md`
- `wiki/indexes/sources.md`
- `wiki/indexes/topics.md`
- `wiki/mcp-tool-governance-and-app-surfaces.md`
- `wiki/post-quantum-security-and-cryptography.md`
- `wiki/unity-3d-and-realtime-vfx-patterns.md`

## Contradictions resolved

- Fable 5 availability: the 2026-07-04 Anthropic source says Fable 5 has been redeployed and is available globally, superseding the earlier 2026-06-12 suspension for current availability. The prior suspension remains preserved as model-access volatility history.

## Gaps logged

Count: 8

- LLM-suggested domain and URL trust in HoneyDrunk agent/developer workflows.
- `uv audit` and `UV_MALWARE_CHECK=1` pilot criteria for Python projects.
- Lightweight threat-model template requirements for agent execution and PR review.
- ContextForge or equivalent MCP/A2A gateway evaluation gates.
- GitHub Copilot browser-tool allowed/denied domain and sensitive-permission policy.
- Copilot CLI `GITHUB_TOKEN` Actions jobs, `copilot-requests: write`, session limits, and org billing controls.
- .NET 8/9 upgrade inventory and WinApp CLI package identity candidates.
- Unity Android XR glasses/headset validation spike for hands-first interactions.

## Crystallization

- Existing `output/query-*.md` files were checked. No query output required promotion in this pass.
- Signal-review outputs remain episodic reporting artifacts; no new durable facts were crystallized from them in this compile.

## Blockers

- No content-quality blocker for the 15-source compile.
- The worktree already contained pre-existing scheduled-job changes before this pass: `.obsidian/graph.json`, `output/lore-birdclaw-sourcing-last-run.md`, `output/lore-sourcing-last-run.md`, `output/signal-review-2026-06-28.md`, and `output/signal-review-2026-07-03.md`. They were not reverted.
- The 2026-07-04 raw sources were untracked at run start and are part of the intended ingest commit.

## Quality posture

- Raw files were treated as immutable and were not edited.
- Claims were added with source links, confidence notes, typed entities, explicit relationships, HoneyDrunk implications, and quality caveats.
- Security sources were summarized at control/policy level. No exploit payloads, credentials, tokens, unsafe PII, unredacted phishing domains, or reusable bypass steps were copied into wiki pages.
- The Fable 5 availability contradiction was resolved with supersession language instead of overwriting the earlier history.
- Vendor/project sources were treated as product or scouting evidence requiring tenant/local validation before operational adoption.
- Decision-usefulness is good for backlog shaping, threat modeling, platform upgrade planning, and source discovery. ContextForge adoption, uv enforcement, Copilot browser policy, Copilot CLI billing controls, .NET upgrades, and Unity Android XR adoption still require local validation before implementation.
