# Lore Signal Review - 2026-05-30

## Executive verdict

- Alert Oleg: yes
- Reason: Claude Code dynamic workflows materially affect the active PR-review and cost-governance decisions because they introduce high-budget parallel subagents before HoneyDrunk has accepted the related cost ceiling and reviewer policy.

## Consider now

- Claude Code dynamic workflows should be treated as a cost/security policy surface before use on important HoneyDrunk repos.
  - Why it matters: Anthropic's new dynamic workflows can run tens to hundreds of parallel subagents, save progress, verify outputs, and resume long-running work; that is useful for large repo tasks but can multiply token spend, review burden, and sandbox risk.
  - HoneyDrunk surface: Current focus #2 ADR-0079 Multi-Perspective PR Review Stack, #14 ADR-0052 Cost Governance, #1 ADR-0086 Pull-Based Local Worker, and the charter's disciplined solo-operator/AI-multiplier model.
  - Suggested question for Oleg: Should dynamic workflows be disallowed by default until ADR-0079/ADR-0052 define budget, sandbox, approval, and verification limits for multi-subagent review or coding runs?
  - Source/wiki: `wiki/claude-platform-2026.md`; `wiki/multi-agent-architectures.md`; `wiki/ai-agent-harnesses.md`; `wiki/ai-assisted-software-practice.md`; raw sources `raw/2026-05-30-web-anthropic-introducing-dynamic-workflows-in-claude-code.md`, `raw/2026-05-30-web-anthropic-introducing-claude-opus-4-8.md`, `raw/2026-05-30-web-microsoft-learn-ai-agent-orchestration-patterns.md`, `raw/2026-05-30-rss-martin-fowler-fragments-may-27.md`.

## Spike candidates

- Private MCP connectivity choice: OpenAI Secure MCP Tunnel vs Azure dynamic shell sessions vs self-managed/local runner networking.
  - Why it might matter: HoneyDrunk is actively moving toward local pull-based workers and home-server agent infrastructure; newly ingested sources show multiple private-tool connectivity paths with different trust, audit, key, preview-stability, and network-ingress tradeoffs.
  - Smallest useful spike: Compare one private MCP use case across OpenAI tunnel, Azure dynamic sessions, and the existing local-worker/home-server approach by auth model, logs, Windows/dev ergonomics, cost, and secret handling. Do not pick a default from vendor docs alone.
  - Source/wiki: `wiki/mcp-tool-governance-and-app-surfaces.md`; `wiki/azure-agent-automation-and-identity.md`; `wiki/ai-agent-harnesses.md`; raw sources `raw/2026-05-30-web-openai-secure-mcp-tunnel.md`, `raw/2026-05-30-web-microsoft-learn-tutorial-use-mcp-with-dynamic-sessions-shell.md`.

- GitHub Code Quality and PR coverage preview may be a low-risk CI governance experiment.
  - Why it might matter: GitHub now exposes Code Quality setup APIs and PR coverage upload with narrow `code-quality:write` permission, which overlaps current integration-CI, PR-review, and repository-governance work.
  - Smallest useful spike: Pick one non-critical C# repo with existing Cobertura output, verify permission requirements, preview behavior, and whether it adds signal beyond existing CI/Sonar plans.
  - Source/wiki: `wiki/github-actions-platform-operations.md`; `wiki/ai-coding-agent-security.md`; raw sources `raw/2026-05-30-web-github-changelog-github-code-quality-repository-enablement-api.md`, `raw/2026-05-30-web-github-changelog-code-coverage-on-pull-requests-is-now-in-public-previ.md`.

- GitHub secret-scanning bypass reporting and Dependabot/code-scanning OIDC private registries are worth checking against credential-inventory work.
  - Why it might matter: ADR-0083/ADR-0084 are focused on external SaaS credentials and alert routing; GitHub added API filtering for bypassed secret-scanning alerts and expanded OIDC private-registry support that can reduce static registry secrets.
  - Smallest useful spike: Inventory whether HoneyDrunk has GitHub Advanced Security secret-scanning bypasses or supported private registries; if yes, decide whether these become alert/report inputs. If no, archive the signal.
  - Source/wiki: `wiki/ai-coding-agent-security.md`; raw sources `raw/2026-05-30-web-github-changelog-filter-secret-scanning-approval-requests-by-sort-orde.md`, `raw/2026-05-30-web-github-changelog-expanded-oidc-support-for-dependabot-and-code-scannin.md`.

## Watch

- Unity render pipeline strategy confirms URP as the default for new Unity prototypes and Built-In Render Pipeline deprecation planning.
  - Why to watch: Relevant to future game/technical-art prototypes, but no active current-focus item depends on Unity render-pipeline choice.
  - Source/wiki: `wiki/unity-3d-and-realtime-vfx-patterns.md`; `wiki/technical-art-community-and-talent-signals.md`; raw source `raw/2026-05-30-web-unity-render-pipelines-strategy-for-2026.md`.

- Game camera systems and realtime protocol design are durable prototype architecture references, not current alerts.
  - Why to watch: Useful if a character-led, cinematic, spectator, or multiplayer prototype enters active planning.
  - Source/wiki: `wiki/game-camera-systems.md`; `wiki/realtime-game-network-protocol-design.md`; `wiki/gamedev-production-and-community-signals.md`; raw sources `raw/2026-05-30-web-80-level-how-black-eye-2-0-is-rethinking-how-video-game-camera-systems.md`, `raw/2026-05-30-web-jkm-dev-how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dial-up.md`.

## No action / archived only

- GitHub Copilot/.NET task-surface guidance reinforces existing bounded-agent practice; no distinct HoneyDrunk decision needed beyond the dynamic-workflow and CI-cost items above.
- .NET MAUI Material 3 is relevant only if a MAUI Android prototype is active; no current-focus trigger.
- Claude Opus 4.8 model upgrade is worth normal benchmark discipline but does not require routing changes from Lore alone.
- Fowler May 27 AI-practice notes reinforce existing HoneyDrunk posture: increase autonomy only behind tests, static analysis, logs, and architectural gates.
- Black Eye 2.0, RuneScape protocol design, and Unity URP items are preserved for future game/prototype decisions.

## Review notes

- Files reviewed: `output/openclaw-ingest-last-run.md`; `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Architecture\initiatives\current-focus.md`; `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Architecture\constitution\charter.md`; `wiki/ai-agent-harnesses.md`; `wiki/ai-coding-agent-security.md`; `wiki/azure-agent-automation-and-identity.md`; `wiki/mcp-tool-governance-and-app-surfaces.md`; `wiki/github-actions-platform-operations.md`; `wiki/claude-platform-2026.md`; `wiki/multi-agent-architectures.md`; `wiki/github-copilot-and-app-token-changes.md`; `wiki/dotnet-runtime-and-mobile-2026.md`; `wiki/microsoft-dotnet-ai-stack.md`; `wiki/ai-assisted-software-practice.md`; `wiki/gamedev-production-and-community-signals.md`; `wiki/unity-3d-and-realtime-vfx-patterns.md`; `wiki/realtime-game-network-protocol-design.md`; `wiki/game-camera-systems.md`; `wiki/technical-art-community-and-talent-signals.md`; `wiki/indexes/gaps.md`; `wiki/indexes/sources.md`.
- Blockers: None. Raw detail was not needed beyond compiled wiki/source-index coverage for this review.
