# OpenClaw Lore ingest run - 2026-06-07

- Timestamp: 2026-06-07 10:10 America/New_York / 2026-06-07 14:10 UTC
- Operator: Honeyclaw / OpenClaw scheduled ingest

## Raw sources ingested: 15

- raw/2026-06-07-web-eva-bench-data-2-0-3-domains-121-tools-213-scenarios.md
- raw/2026-06-07-web-nemotron-3-5-content-safety-customizable-multimodal-safety-for-global-.md
- raw/2026-06-07-web-adding-mcp-tools-to-reachy-mini.md
- raw/2026-06-07-web-quickstart-build-serverless-agents-using-azure-functions.md
- raw/2026-06-07-web-evaluation.md
- raw/2026-06-07-web-ai-tool-calling-net.md
- raw/2026-06-07-web-workflow-oriented-multi-agent-patterns.md
- raw/2026-06-07-web-orchestrator-and-subagent-multi-agent-patterns.md
- raw/2026-06-07-web-introducing-agent-optimizer-in-foundry-agent-service.md
- raw/2026-06-07-web-announcing-foundry-managed-compute-run-open-models-in-microsoft-foundr.md
- raw/2026-06-07-web-enterprise-managed-plugins-in-vs-code-in-public-preview.md
- raw/2026-06-07-web-codeql-2-25-6-adds-swift-6-3-2-support-and-improves-c-coverage.md
- raw/2026-06-07-web-fix-with-copilot-for-failing-actions-now-in-pro-pro-and-max.md
- raw/2026-06-07-web-what-is-sandbox-security.md
- raw/2026-06-07-web-basic-concepts-unity-pipeline-automation.md

## Wiki pages created/updated

- Created: none.
- Updated:
  - wiki/agent-evaluation-and-benchmarks.md
  - wiki/ai-agent-harnesses.md
  - wiki/ai-coding-agent-security.md
  - wiki/azure-agent-automation-and-identity.md
  - wiki/edge-ai-and-ai-infrastructure-2026.md
  - wiki/github-actions-platform-operations.md
  - wiki/github-copilot-and-app-token-changes.md
  - wiki/mcp-tool-governance-and-app-surfaces.md
  - wiki/microsoft-dotnet-ai-stack.md
  - wiki/multi-agent-architectures.md
  - wiki/unity-3d-and-realtime-vfx-patterns.md
  - wiki/voice-agent-platforms-2026.md
- Indexes rebuilt/updated:
  - wiki/indexes/sources.md
  - wiki/indexes/topics.md
  - wiki/indexes/gaps.md

## Crystallization from `output/query-*.md`

- Reviewed query-output inventory. The unrepresented query files through 2026-05-23 are older daily signal summaries.
- No additional crystallization was performed because the durable facts in those query outputs are already reflected in the cited wiki pages, and the remaining material is redundant extraction-quality commentary rather than new durable facts.

## Contradictions / supersession

- No contradictions required resolution.
- No existing claims were superseded. New sources mostly reinforced existing posture around agent evaluation, tool governance, sandbox security, Copilot automation, Foundry/Azure agent infrastructure, and Unity pipeline automation.

## Gaps logged

- Which HoneyDrunk voice/support-agent scenarios should become reproducible eval cases with tool calls, authentication, unsatisfiable goals, and final-state checks?
- Should HoneyDrunk pilot Azure Functions serverless agents for scheduled OpenClaw/Honeyclaw jobs, and what connector consent, function-key, dynamic-session, managed-identity, logging, and cost policy is required?
- Should HoneyDrunk evaluate Foundry Managed Compute for open-weight/custom models, and what comparison set should include direct Azure GPU VMs, local inference, DigitalOcean, and existing API providers?
- What organization policy should govern enterprise-managed Copilot plugins in VS Code/Copilot CLI, including auto-install, hooks, MCP configs, provenance, and rollback?
- Which CI failure classes are safe for one-click Fix with Copilot, and what branch, billing-owner, tool, sandbox, and review requirements should constrain it?

## Quality posture

- Decision-usefulness: good. All promoted claims cite immutable raw files and were mapped to existing canonical wiki pages rather than creating duplicate pages.
- Weak claims: Microsoft/GitHub/Docker/NVIDIA/Unity product and benchmark claims remain vendor-authored. Preview features, pricing, region/plan availability, benchmark transfer, and production controls require local validation before adoption.
- Privacy/safety filtering: no raw secrets, tokens, malware indicators, or runnable exploit procedures were copied into wiki content. Safety/security sources were summarized at control and decision level.
- Source-quality notes: Microsoft Learn raw captures included auth/scaffolding boilerplate, but readable body content was sufficient for durable claims. The Nemotron source was retained as scouting evidence and not treated as production safety proof.
- Decision-usefulness notes: strongest actionable signals are eval final-state design from EVA-Bench, serverless agent/dynamic-session policy questions, Foundry Managed Compute as an open-model hosting candidate, Copilot plugin/CI repair governance, and sandbox-tier discipline for OpenClaw/Honeyclaw.

## Validation

- Raw source coverage check passed: every file under `raw/` except `.gitkeep` is represented in `wiki/indexes/sources.md`.
- Source-to-wiki citation check passed: every 2026-06-07 raw source appears in at least one non-index wiki page.
- Non-raw staged diff check passed. Full staged `git diff --check` reports trailing whitespace inside newly added `raw/` source captures; those files were left unchanged because `raw/` is immutable source evidence.
- Topic and gap indexes updated with 2026-06-07 additions.

## Blockers

- None. Validation passed; safe to commit and push the ingest/compile changes.
