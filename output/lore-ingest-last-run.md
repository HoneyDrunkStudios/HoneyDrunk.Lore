# Lore Ingest Last Run

Timestamp: 2026-09-10T16:18:00-04:00

## Raw sources ingested

Count: 15

- `raw/2026-09-10-rss-github-changelog-actions-control-github-actions-cache-access-with-cach.md`
- `raw/2026-09-10-rss-net-blog-announcing-net-11-release-candidate-1.md`
- `raw/2026-09-10-rss-net-blog-use-c-unions-and-closed-hierarchies-in-asp-net-core.md`
- `raw/2026-09-10-rss-system-design-newsletter-if-you-want-to-get-started-with-claude-code-r.md`
- `raw/2026-09-10-rss-tech-artists-org-array-attributes-in-maya-python-api-2-mpxnode.md`
- `raw/2026-09-10-rss-thoughtworks-insights-how-to-talk-with-ai.md`
- `raw/2026-09-10-rss-tldr-ai-connections-managed-credentials-and-per-caller-identity-for-ma.md`
- `raw/2026-09-10-rss-tldr-ai-inside-the-megakernel-serving-engine-for-north-mini-code-22-mi.md`
- `raw/2026-09-10-rss-tldr-infosec-gtig-ai-threat-tracker-from-prompting-to-autonomy-the-evo.md`
- `raw/2026-09-10-rss-tldr-infosec-sage-github-repo.md`
- `raw/2026-09-10-rss-unity-blog-drakkenridge-building-an-open-world-adventure-for-mobile-vr.md`
- `raw/2026-09-10-rss-unity-blog-official-unity-plugin-for-claude-code.md`
- `raw/2026-09-10-web-microsoft-command-line-pyrit-democratizing-ai-red-teaming-through-open.md`
- `raw/2026-09-10-web-microsoft-command-line-stop-restricting-the-agent-start-restricting-it.md`
- `raw/2026-09-10-web-microsoft-command-line-your-agent-s-guardrails-have-a-bypass.md`

## Wiki pages created/updated

Created:
- None.

Updated:
- `wiki/github-actions-platform-operations.md`
- `wiki/dotnet-runtime-and-mobile-2026.md`
- `wiki/microsoft-dotnet-ai-stack.md`
- `wiki/ai-agent-identity-and-workload-auth.md`
- `wiki/azure-agent-automation-and-identity.md`
- `wiki/ai-coding-agent-security.md`
- `wiki/agent-evaluation-and-benchmarks.md`
- `wiki/ai-agent-harnesses.md`
- `wiki/edge-ai-and-ai-infrastructure-2026.md`
- `wiki/mcp-tool-governance-and-app-surfaces.md`
- `wiki/ai-assisted-software-practice.md`
- `wiki/unity-3d-and-realtime-vfx-patterns.md`
- `wiki/gamedev-production-and-community-signals.md`
- `wiki/technical-art-community-and-talent-signals.md`
- `wiki/indexes/sources.md`
- `wiki/indexes/topics.md`
- `wiki/indexes/gaps.md`
- `output/lore-ingest-last-run.md`

Related sourcing receipts selected for this commit after review:
- `output/lore-sourcing-last-run.md`
- `output/lore-birdclaw-sourcing-last-run.md`
- `output/signal-review-2026-09-10.md`

## Contradictions resolved

- None. New sources reinforced existing governance, .NET, Unity, and agent-security themes without superseding prior wiki claims.

## Gaps logged

Count: 9

- GitHub Actions workflows that should explicitly set `cache-mode`.
- .NET APIs that should trial C# 15 unions or closed hierarchies.
- Managed-agent credential ownership and OAuth policy.
- Agent hook host implementation and fail-closed proof.
- AI coding-assistant plugin, MCP, package-manager, hidden-config, and CI-cache safety mediation.
- PyRIT/RAMPART red-team scenario, scorer, and coverage design.
- Cohere-style decode megakernel benchmark relevance.
- Unity Claude Code plugin trial workflow and rollback rules.
- Minimal Maya MPxNode array compound attribute reproduction.

## Crystallization from output/query-*.md

- Reviewed the current `output/query-*.md` inventory posture from the prior compile state.
- No additional `query-*.md` artifacts were promoted in this pass; durable cited facts from older query outputs are already represented in wiki pages.
- `output/signal-review-2026-09-10.md` was retained as a sourcing review receipt, not treated as a `query-*` crystallization source.

## Blockers

- Birdclaw live sync remains unavailable in the sourcing receipt: `xurl` is not installed/local mode is active and the Bird command is unavailable.
- External sourcing replaced two transient candidates before ingest; the committed raw batch is the stabilized 15-file source list recorded above.
- Pre-existing unrelated worktree changes remain outside this ingest commit: `.obsidian/graph.json`, older signal-review outputs, and `tools/lore_source_public.py`.

## Quality posture

- Pages rewritten/flagged: no full rewrites; 14 existing concept pages received dated sections with typed entities, explicit relationships, claims, confidence notes, and source citations.
- Weak claims: Cohere benchmark claims, Unity performance/plugin claims, Sage/PyRIT README claims, and the partial Claude Code tutorial are marked as needing local validation before operational adoption.
- Privacy redactions: unsafe operational prompt/exploit details from the GTIG threat report were not promoted; only defensive themes and control implications were captured.
- Decision-usefulness: the pass promotes concrete follow-up decisions around cache permissions, agent credentials, hooks, PyRIT evaluation, .NET 11/C# 15 contracts, Unity plugin trials, and mobile-VR performance measurement.

## Validation

- Read `AGENTS.md` and followed the Ingest/Compile contract.
- Compared current files under `raw/` against `wiki/indexes/sources.md` and ingested every unrepresented 2026-09-10 source.
- Rebuilt `wiki/indexes/sources.md`, `wiki/indexes/topics.md`, and `wiki/indexes/gaps.md` with the 2026-09-10 additions.
- Preserved `raw/` immutability; no files under `raw/` were edited.
- Per publishing rules, completed an explicit staged-diff code-review pass before commit/push; no blockers were found in promoted wiki/output content.
