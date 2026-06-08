# Lore Signal Review - 2026-06-05

## Executive verdict

- Alert Oleg: yes
- Reason: Two new Lore signals touch active HoneyDrunk execution risk: public HTTP/2 exposure during Notify/Pulse deployment, and policy boundaries for GitHub Copilot cloud-agent API/scheduled automations before HoneyHub/OpenClaw dispatch decisions harden.

## Consider now

- HTTP/2 termination inventory before Notify/Pulse and Notify Cloud exposure
  - Why it matters: Newly ingested primary research describes an HTTP/2 memory-exhaustion class where default HTTP/2 configurations may need decoded-header-size limits, header-field-count limits, stalled-stream bounds, and worker/container memory caps. This is directly relevant to any public ingress path for Notify/Pulse dev deployment and later Notify Cloud.
  - HoneyDrunk surface: Current focus #2 Deploy Notify + Pulse to dev; #7 Notify Cloud multi-tenant scaffolding kickoff slice.
  - Suggested question for Oleg: Do the HoneyDrunk ingress paths that can speak or terminate HTTP/2 have known version/config coverage for header-count, cookie-crumb, stalled-stream, and memory-cap controls before public or tenant-facing use?
  - Source/wiki: `wiki/ai-coding-agent-security.md`; `raw/2026-06-05-web-codex-discovered-a-hidden-http-2-bomb.md`

- Agent automation policy before using Copilot cloud-agent API or scheduled automations
  - Why it matters: GitHub now exposes Copilot cloud-agent tasks through a REST API and scheduled/event automations, while Docker's agent-security overview reinforces that prompts and approval prompts are not durable controls. HoneyDrunk already runs scheduled agent jobs and has an active HoneyHub agent-dispatch ADR follow-up pending, so this can affect build/buy/adopt/avoid boundaries.
  - HoneyDrunk surface: Current focus #3 ADR-0043 backlog generation; #6 PDR-0009 HoneyHub agent-dispatch service ADR; OpenClaw/Honeyclaw scheduled jobs.
  - Suggested question for Oleg: Should Copilot cloud-agent API/scheduled automations be allowed only as an experiment behind repo scope, tool allowlist, spend owner, sandbox/default-off policy, branch/PR behavior, and human review requirements, or excluded from the first HoneyHub dispatch design?
  - Source/wiki: `wiki/github-copilot-and-app-token-changes.md`; `wiki/ai-coding-agent-security.md`; `raw/2026-06-05-web-agent-tasks-rest-api-now-available-for-copilot-pro-pro-and-max.md`; `raw/2026-06-05-web-schedule-and-automate-tasks-with-copilot-cloud-agent.md`; `raw/2026-06-05-web-cloud-and-local-sandboxes-for-github-copilot-now-in-public-preview.md`; `raw/2026-06-05-web-how-to-secure-ai-agents-a-practical-overview.md`

## Spike candidates

- Agent-optimized HoneyDrunk CLI/tool contract
  - Why it might matter: Hugging Face's `hf` CLI redesign gives a concrete pattern for agent-friendly tools: explicit agent/json/quiet formats, no blocking prompts, dry-run support, idempotent retries, full untruncated output, and next-command hints. This is relevant to future HoneyHub/OpenClaw tool surfaces, but it is not urgent enough to interrupt current ranked work.
  - Smallest useful spike: Pick one existing HoneyDrunk command/tool used by agents and compare it against the `hf` pattern for output format, prompt behavior, dry-run/idempotency, and machine-readable errors.
  - Source/wiki: `wiki/ai-agent-harnesses.md`; `raw/2026-06-05-web-designing-the-hf-cli-as-an-agent-optimized-way-to-work-with-the-hub.md`

## Watch

- Foundry IQ / Fabric IQ / HorizonDB managed knowledge stack
  - Why to watch: Microsoft is packaging governed retrieval, MCP exposure, serverless retrieval economics, Fabric knowledge graphs, and AI-application data planes. This may matter if flat-file Lore stops scaling, but the charter and current Lore contract favor lightweight local files until scale or retrieval quality forces a change.
  - Source/wiki: `wiki/azure-agent-automation-and-identity.md`; `wiki/edge-ai-and-ai-infrastructure-2026.md`; `wiki/mcp-tool-governance-and-app-surfaces.md`

- Codex role plugins and Codex Sites
  - Why to watch: Generated shared workspaces and role-specific plugins are relevant to future Grid/HoneyHub dashboards, but preview availability, permissions, source citation behavior, hosting boundaries, and data retention are not established for HoneyDrunk use.
  - Source/wiki: `wiki/ai-assisted-software-practice.md`; `wiki/generative-ui-and-a2ui.md`

- Blender 5.2 LTS beta and Real Fake Interiors
  - Why to watch: Useful technical-art and Unity optimization signals for future asset/prototype work, but not connected to the active HoneyDrunk focus list.
  - Source/wiki: `wiki/technical-art-community-and-talent-signals.md`; `wiki/unity-3d-and-realtime-vfx-patterns.md`

## No action / archived only

- Carson Gross "code is cheaper" essay reinforces existing HoneyDrunk practice: small diffs, human understanding, simplification, and review gates.
- Claude Agent SDK monthly credits affect billing hygiene, but the actionable policy is already clear: personal credits for experiments, service-owned API billing for shared automation.
- .NET Native AOT Node-API addons are worth preserving for future VS Code/Node tooling, but no active HoneyDrunk Node currently needs this native bridge.
- Docker software supply-chain overview reinforces existing action-pinning, SBOM/provenance, image-signing, and deploy-verification themes; no new immediate work beyond the agent/security policy question above.

## Review notes

- Files reviewed: `output/openclaw-ingest-last-run.md`; `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Architecture\initiatives\current-focus.md`; `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Architecture\constitution\charter.md`; `wiki/ai-agent-harnesses.md`; `wiki/ai-assisted-software-practice.md`; `wiki/ai-coding-agent-security.md`; `wiki/azure-agent-automation-and-identity.md`; `wiki/claude-platform-2026.md`; `wiki/dotnet-runtime-and-mobile-2026.md`; `wiki/edge-ai-and-ai-infrastructure-2026.md`; `wiki/generative-ui-and-a2ui.md`; `wiki/github-copilot-and-app-token-changes.md`; `wiki/mcp-tool-governance-and-app-surfaces.md`; `wiki/technical-art-community-and-talent-signals.md`; `wiki/unity-3d-and-realtime-vfx-patterns.md`
- Blockers: None.
