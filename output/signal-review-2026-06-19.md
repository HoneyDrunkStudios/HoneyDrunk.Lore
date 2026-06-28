# Lore Signal Review - 2026-06-19

## Executive verdict

- Alert Oleg: yes
- Reason: New GitHub workflow-admission and checkout-safety signals apply directly to active HoneyHub/NovOutbox PR-review workflows before the HoneyHub public-release checkpoint.

## Consider now

- GitHub privileged-workflow trigger audit before HoneyHub public-release work hardens
  - Why it matters: GitHub added workflow execution protections for actor/event admission and is changing `actions/checkout` behavior around privileged fork-PR contexts on a July 2026 timeline. A read-only check found `pull_request_target` Grid Review Request workflows in both active-lane repos; HoneyHub's caller does not locally guard to same-repo PRs, while NovOutbox does. The shared reusable workflow appears to check out the base repository and use PR metadata/API calls rather than untrusted head code, so this is not an observed exploit, but it is exactly the kind of privileged trigger surface the new controls target.
  - HoneyDrunk surface: HoneyHub current focus #1/#2 public launch and release readiness; NovOutbox current focus #6-#9 first commercial trial scaffolding and beta substrate; Grid Review Request workflows in `HoneyDrunk.HoneyHub`, `HoneyDrunk.NovOutbox`, and reusable workflow `HoneyDrunk.Actions/.github/workflows/job-review-request.yml`.
  - Suggested question for Oleg: Before HoneyHub's public release path gets more outside PR traffic, should privileged review-request workflows be put behind GitHub workflow execution protections in evaluate mode and checked for fork/head checkout bypasses, or is the current base-checkout plus local worker admission model sufficient for now?
  - Source/wiki: `wiki/github-actions-platform-operations.md`; `wiki/ai-coding-agent-security.md`; `raw/2026-06-19-web-github-blog-control-who-and-what-triggers-github-actions-workflows.md`; `raw/2026-06-19-web-github-blog-safer-pull-request-target-defaults-for-github-actions-checkout.md`

## Spike candidates

- NovOutbox usage-metering and billing correctness checklist
  - Why it might matter: The new reusable-SaaS-plumbing source is low-authority founder/community evidence, but its specific failure modes match NovOutbox's first-beta dependency cut: idempotent usage recording, concurrent counters, quota enforcement, retries, overages, and Stripe reconciliation are easy to get subtly wrong.
  - Smallest useful spike: Draft a one-page test checklist for NovOutbox first-beta metering/billing boundaries, limited to idempotency keys, replay behavior, quota enforcement, tenant isolation, and reconciliation evidence.
  - Source/wiki: `wiki/creator-business-models.md`; `raw/2026-06-19-web-indiehackers-com-i-rebuilt-the-same-saas-plumbing-four-times-so-i-built-the-thing-i-wi.md`

- Lore/OpenClaw research-query leakage smoke test
  - Why it might matter: MosaicLeaks reframes deep-research privacy as cumulative public-query leakage, not only final-answer leakage. This matters if Lore/OpenClaw ever mixes private repo notes or Architecture context into web-search tasks.
  - Smallest useful spike: Run one synthetic Lore query with private-looking but fake facts and inspect emitted web/search terms for leakage before changing any scheduled job behavior.
  - Source/wiki: `wiki/agent-evaluation-and-benchmarks.md`; `wiki/ai-coding-agent-security.md`; `raw/2026-06-19-web-huggingface-co-mosaicleaks-can-your-research-agent-keep-a-secret.md`

## Watch

- Agent discovery and tool governance specs
  - Why to watch: ARD, A2A, and Microsoft AGT reinforce cataloged, policy-governed agent/tool discovery. This is aligned with HoneyHub's agent-discovery work, but the specs are vendor/platform signals and should not interrupt the current release checklist unless HoneyHub needs external agent-resource publication or .NET MCP governance soon.
  - Source/wiki: `wiki/mcp-tool-governance-and-app-surfaces.md`; `wiki/google-agent-platform-and-gemini-api-2026.md`; `wiki/microsoft-dotnet-ai-stack.md`

- Agent-use and production-eval frameworks
  - Why to watch: Hugging Face `agent-eval` and Thoughtworks production-eval layers are relevant to HoneyHub/Evals, especially model-size sensitivity and regression cases from operator feedback, but they are practice-shaping rather than an immediate launch blocker.
  - Source/wiki: `wiki/agent-evaluation-and-benchmarks.md`; `wiki/ai-assisted-software-practice.md`

- Azure SRE Agent networking and ACA code interpreter sessions
  - Why to watch: The egress/session-isolation details are useful if HoneyDrunk evaluates hosted agent execution, but no active focus item requires Azure SRE Agent or ACA code interpreter adoption now.
  - Source/wiki: `wiki/azure-agent-automation-and-identity.md`; `wiki/mcp-tool-governance-and-app-surfaces.md`

## No action / archived only

- Docker Content Trust retirement is important platform news, but the active-lane scan did not identify a concrete DCT dependency before timeout/noise; preserve it for a later org-wide Docker signing inventory.
- Copilot code review root `AGENTS.md` support reinforces the existing decision to treat repo instructions as runtime policy; no separate action beyond maintaining accurate `AGENTS.md` files.
- Copilot modernization assessment source is useful for future migration work, but HoneyDrunk's current focus is product delivery, not legacy .NET modernization.
- Environment-art co-development structure is good production guidance for future game/world work, but it does not materially change the Curiosities Phase 0 content spike.

## Review notes

- Files reviewed: `output/openclaw-ingest-last-run.md`; `output/openclaw-sourcing-last-run.md`; `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Architecture\initiatives\current-focus.md`; `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Architecture\constitution\charter.md`; `wiki/indexes/sources.md`; `wiki/indexes/topics.md`; `wiki/github-actions-platform-operations.md`; `wiki/ai-coding-agent-security.md`; `wiki/mcp-tool-governance-and-app-surfaces.md`; `wiki/google-agent-platform-and-gemini-api-2026.md`; `wiki/agent-evaluation-and-benchmarks.md`; `wiki/creator-business-models.md`; `wiki/azure-agent-automation-and-identity.md`; `wiki/microsoft-dotnet-ai-stack.md`; `wiki/ai-assisted-software-practice.md`; `wiki/technical-art-community-and-talent-signals.md`; `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.HoneyHub\.github\workflows\grid-review-request.yml`; `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.HoneyHub\.github\workflows\pr.yml`; `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.NovOutbox\.github\workflows\pr-review.yml`; `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.NovOutbox\.github\workflows\nightly-security.yml`; `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Actions\.github\workflows\job-review-request.yml`; `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Actions\.github\workflows\nightly-security.yml`
- Blockers: `rg` is unavailable in this shell, so PowerShell search was used. Existing unrelated local changes were left untouched: `.obsidian/graph.json` and `tools/openclaw-lore-signal-review-prompt.md`. Docker/DCT active-lane scan hit noisy dependency folders and timed out, so DCT was not promoted beyond archived/watch posture.
