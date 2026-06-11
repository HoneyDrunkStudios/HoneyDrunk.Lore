# AI Agent Harnesses

## Decision-useful summary
An agent is best treated as `model + harness`: the model supplies probabilistic reasoning, while the harness supplies state, tools, execution constraints, feedback loops, storage, orchestration, and verification. This matters for HoneyDrunk because durable agent value comes less from swapping models and more from making the runtime reliable: filesystem-backed context, safe shell/code execution, sandboxing, memory/search, continuations, lint gates, and background delegation. [source: raw/2026-05-03-web-langchain-agent-harness.md]

## Claims
- Harness engineering is the non-model layer that turns a raw LLM into a work engine by providing prompts, tools, skills/MCPs, bundled infrastructure, orchestration, hooks, and execution policy. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-web-langchain-agent-harness.md]
- Long-horizon agents need durable storage, context management, sandboxed execution, verification, memory/search, and countermeasures for context rot. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-web-langchain-agent-harness.md]
- Background/async subagents address supervisor deadlock and coordination problems by allowing delegated work to continue while the parent agent remains responsive to new information. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-web-langchain-async-subagents.md]
- OpenAI Codex CLI 0.128.0 added `/goal`, a continuation loop that keeps working until goal completion or token-budget exhaustion, apparently driven mainly by continuation and budget-limit prompt templates. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-simonwillison-codex-cli-goal.md]
- Google Agents CLI reinforces that agent harnesses now include machine-readable scaffolding, evaluation, infrastructure provisioning, deployment, and publishing commands for coding assistants, not just chat prompts. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-agents-cli-in-agent-platform-create-to-producti.md]
- Gemini API webhooks reinforce push-based completion as a harness primitive for long-running agent jobs, with signed events, idempotency headers, at-least-once delivery, and retries instead of repeated polling. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-ai-blog-reduce-friction-and-latency-for-long-running-jobs-with-.md]
- Google's ADK refactor case study reinforces production-agent harness needs: specialized subagents, executable schemas/structured outputs, dynamic retrieval, traces, retries, timeouts, and cost circuit breakers. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-production-ready-ai-agents-5-lessons-from-refac.md]
- Microsoft Agent Framework durable workflows reinforce that reliable agent harnesses need checkpointing, restart survival, distributed execution, external observability, generated HTTP/MCP entrypoints, and human-in-the-loop wait states. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-net-blog-durable-workflows-in-the-microsoft-agent-framework.md]
- The Curity/Microsoft least-privilege template reinforces that production agent harnesses should push authorization into short-lived tokens, API filters, gateways, and audit logs rather than relying on model behavior or prompt compliance. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-azure-blog-least-privilege-ai-agents-a-new-azd-template-from-curity-an.md]
- Voice-agent platforms reinforce that the harness must handle low-latency tool orchestration, partial/interrupted speech, permissions, recovery, and logging; stronger real-time models do not remove those responsibilities. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-web-the-rundown-ai-openai-closes-reasoning-gap-in-voice-agents.md]
- Dataverse's agentic-shift framing reinforces that agents need business context, relationships, rules, and process skills in addition to raw data access. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-youtube-microsoft-developer-youtube-dataverse-and-the-agentic-shift.md]
- Microsoft MCP app samples reinforce that app/client harness surfaces increasingly include reusable UI widgets, manifests/docs, previews, and cross-assistant compatibility rather than only raw tool schemas. confidence: 1 source, last-confirmed 2026-05-11. [source: raw/2026-05-11-youtube-microsoft-developer-youtube-don-t-build-mcp-apps-from-scratch-use-this.md]
- Multi-agent architecture should be chosen only when a single agent hits context, parallelism, or specialization/permission limits; otherwise extra agents add coordination, latency, token, verification, and security overhead. confidence: 1 source, last-confirmed 2026-05-12. [source: raw/2026-05-12-rss-system-design-newsletter-multi-agent-architectures-clearly-explained.md; page: [[multi-agent-architectures]]]

## Typed entities
- concept: [[AI Agent Harnesses]]
- concept: Model Context Protocol
- library/platform: LangChain Deep Agents
- library/tool: OpenAI Codex CLI
- feature: `/goal`
- feature/tool: Google Agents CLI
- feature/API: Gemini API webhooks
- framework: Google Agent Development Kit (ADK)
- framework: Microsoft Agent Framework
- protocol/security pattern: OAuth 2.0 token exchange
- model/product: GPT-Realtime-2
- platform/service: Microsoft Dataverse
- resource: MCP app samples
- concept: Business Skills
- standard/tooling: OpenTelemetry
- pattern: async subagents
- pattern: structured outputs
- file: raw/2026-05-03-web-langchain-agent-harness.md
- file: raw/2026-05-03-web-langchain-async-subagents.md
- file: raw/2026-05-03-rss-simonwillison-codex-cli-goal.md

## Explicit relationships
- [[AI Agent Harnesses]] uses tools, filesystems, sandboxes, memory/search, orchestration, and verification to make model output actionable.
- async subagents fixed supervisor deadlock and parent-agent context coordination problems described for traditional subagents.
- OpenAI Codex CLI `/goal` uses continuation prompts and budget-limit prompts to implement a Ralph-style loop.
- [[Azure MCP Server 2.0]] depends-on Model Context Protocol as one harness/tool-integration surface.
- Google Agents CLI uses eval, infrastructure, deploy, and publish commands as an agent-consumable harness surface.
- Gemini API webhooks supersede polling for supported long-running jobs.
- Production agent harnesses depend-on structured outputs, observability, and bounded retries/cost controls.
- Durable Microsoft Agent Framework workflows use checkpointing and Durable Task Scheduler to survive process restarts and coordinate distributed executors.
- Least-privilege AI agents use OAuth 2.0 token exchange, gateways, and API-side filters to constrain nondeterministic tool calls.
- Voice agents depend-on the same harness controls as text agents, plus speech-specific latency, interruption, and recovery handling.
- Business-context agents depend-on semantic relationships and process/rule descriptions, not just record retrieval.
- MCP app surfaces depend-on reusable sample patterns, UI widgets, docs, and compatibility testing across assistant clients.

## HoneyDrunk implications
- Prefer investing in runtime affordances (state, validation, background workers, resumability, audit logs) before model-specific prompt churn.
- Treat every long-running agent workflow as a harness design problem: define storage, tools, permissions, verification gate, and what happens when budget runs out.
- Prefer push/completion-event contracts for long jobs where possible; polling is a fallback, not the ideal orchestration shape.
- Treat authorization as harness infrastructure: short-lived scoped tokens, gateway audit logs, and API filters should constrain agents before prompts do.
- For voice or business-process agents, define approval/recovery paths and domain rules before exposing high-impact tools.
- Reuse sample MCP app/client patterns before custom implementation; spend custom effort on permissions, state, and verification rather than protocol boilerplate.

## Confidence and quality notes
- Quality posture: decision-usable; claims are source-cited and non-private.
- Weak spots: LangChain source is vendor-authored; validate operational patterns against local OpenClaw behavior before architecture commitments.
- Privacy filter: no credentials or unsafe PII copied from raw sources.

## 2026-05-18 compile additions

### Claims
- OpenTelemetry GenAI semantic conventions give agent harnesses standard traces, metrics, and events for model calls, token use, tool calls, retries, and optionally prompt/tool content. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-opentelemetry-blog-inside-the-llm-call-genai-observability-with-opente.md; page: [[opentelemetry-genai-observability-and-ecosystem]]]
- Fowler/Pritchard's workflow-vs-agent point reinforces that harness design should not default to autonomy: if the steps are known, compose deterministic code with bounded LLM function calls. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-martin-fowler-fragments-may-14.md]

### Typed entities
- standard: OpenTelemetry GenAI semantic conventions
- tool: Aspire Dashboard
- concept: deterministic workflow with LLM function call

### Explicit relationships
- Agent harnesses depend-on observability for debugging latency, cost, tool behavior, and retry loops.
- Deterministic LLM workflows contradict unnecessary runtime autonomy when orchestration is knowable in code.

## 2026-05-20 compile additions

### Claims
- Docker's coding-agent security writeup reinforces that the harness, not the model prompt, must enforce filesystem scope, credential reachability, network egress, and irreversible-action approvals. confidence: 1 vendor security source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md; page: [[ai-coding-agent-security]]]
- Microsoft Developer's Cowork YouTube metadata shows a narrow skill pattern: a Cowork skill accepts one GitHub contribution link, fetches metadata, and generates a formatted PowerPoint slide for a weekly “Prompt of the Week” workflow. confidence: 1 YouTube metadata source, last-confirmed 2026-05-20. [source: raw/2026-05-20-youtube-microsoft-developer-youtube-using-cowork-i-automated-my-prompt-of-the-.md]

### Typed entities
- product: Docker Sandboxes / sbx
- concept: workspace-scoped agent execution
- product: Microsoft Cowork
- artifact: PowerPoint slide
- source platform: GitHub
- pattern: single-input skill automation

### Explicit relationships
- Agent harnesses depend-on execution-layer security boundaries for destructive or external actions.
- Cowork skills use narrow inputs and tool access to automate repeatable office/content workflows.

### HoneyDrunk implications
- Prefer small, typed, single-purpose agent skills for repeatable studio operations; they are easier to permission, test, and audit than broad autonomous agents.

## 2026-05-21 compile additions

### Claims
- Docker Custom MCP Catalogs let organizations curate approved MCP servers, including Docker catalog entries, community servers, and internally built servers, then distribute them as immutable OCI artifacts through a container registry. confidence: 1 vendor source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-docker-blog-custom-mcp-catalogs-and-profiles-advancing-enterprise-mcp-.md; page: [[mcp-tool-governance-and-app-surfaces]]]
- Docker MCP Profiles define portable named groupings of MCP servers and configuration for different work modes such as coding, planning, or research; profiles can persist server options, disable unneeded tools to reduce context, connect to agent clients such as Claude Code, and be pushed/pulled as OCI artifacts. confidence: 1 vendor source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-docker-blog-custom-mcp-catalogs-and-profiles-advancing-enterprise-mcp-.md; page: [[mcp-tool-governance-and-app-surfaces]]]
- Martin Fowler/Thoughtworks maintainability-sensor guidance frames sensors as harness feedback loops for coding agents: type checks, linters, SAST, dependency rules, tests, mutation testing, secrets scans, dependency freshness, data-handling review, security review, and modularity/coupling review can run during coding, CI, scheduled review, or production. confidence: 1 source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-martin-fowler-maintainability-sensors-for-coding-agents.md; page: [[ai-assisted-software-practice]]]
- Microsoft Developer's MCP Inspector short reinforces local app-surface testing as a harness primitive: developers can launch `npx @modelcontextprotocol/inspector`, connect a local or hosted MCP server, validate raw tool calls, and interact with a React Fluent UI app widget before relying on a client integration. confidence: 1 YouTube metadata source, last-confirmed 2026-05-21. [source: raw/2026-05-21-youtube-microsoft-developer-youtube-test-your-mcp-app-ui-locally-react-fluent-.md; page: [[mcp-tool-governance-and-app-surfaces]]]

### Typed entities
- product: Docker MCP Catalog
- feature: Custom MCP Catalogs
- feature: Docker MCP Profiles
- artifact format: OCI artifact
- protocol: Model Context Protocol
- tool: MCP Inspector
- UI framework: React Fluent UI
- concept: maintainability sensor
- tool: dependency-cruiser
- tool: Semgrep
- tool: GitLeaks
- tool: mutation testing

### Explicit relationships
- MCP governance uses Custom Catalogs to separate organization-approved tool supply from individual profile composition.
- MCP Profiles depend-on cataloged servers and saved configuration to reduce context-window/tool-surface noise.
- MCP Inspector uses local server connection and widget loading to test MCP apps before client deployment.
- Coding-agent harnesses use computational and inferential sensors to provide self-correction feedback before human review.
- Maintainability sensors complement execution security: sandboxing constrains blast radius, while lint/dependency/modularity sensors constrain technical-debt drift.

### HoneyDrunk implications
- Model OpenClaw/Grid tool modes as named, minimal profiles rather than one giant always-on MCP/tool surface.
- Treat approved MCP servers as a governed catalog concern; profile-level experimentation should not bypass server provenance, secrets, and network policy.
- Add self-correction guidance to lint/dependency-rule messages where possible; raw errors are less useful to agents than errors plus the intended architectural rule.

## 2026-05-22 compile additions

### Claims
- Docker Gordon is generally available in Docker Desktop 4.74+ and the `docker ai` CLI, with access to container logs, images, Compose files, working directory context, shell/filesystem operations, Docker CLI, Docker docs/best-practices knowledge, and web access. confidence: 1 vendor source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-docker-blog-meet-gordon-docker-s-ai-agent-for-your-entire-container-wo.md]
- Gordon requires explicit user approval for shell commands, file modifications, and Docker operations, and permissions reset when the session closes; Docker also supports configurable auto-approve for trusted workflows. confidence: 1 vendor source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-docker-blog-meet-gordon-docker-s-ai-agent-for-your-entire-container-wo.md]
- Gordon's product positioning reinforces a harness split: coding assistants help with application logic while environment-aware agents handle build/run/debug/ship tasks across containers and local infrastructure. confidence: 1 vendor source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-docker-blog-meet-gordon-docker-s-ai-agent-for-your-entire-container-wo.md]
- C# caller-unsafe changes reinforce compiler-enforced harness guardrails: agent-generated .NET code can be prevented from calling unsafe APIs when the new model is enabled and `AllowUnsafeBlocks=false`. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md; page: [[csharp-memory-safety-and-unsafe-code]]]

### Typed entities
- product: Docker Gordon
- command: `docker ai`
- product: Docker Desktop 4.74+
- capability: container log inspection
- capability: Compose/workdir inspection
- capability: approval-gated shell execution
- language feature: C# caller unsafe
- project property: `AllowUnsafeBlocks`

### Explicit relationships
- Gordon depends-on Docker-local runtime context to diagnose container failures without manual context pasting.
- Approval-gated command execution complements sandbox/network/secret controls but does not supersede them.
- C# compiler unsafe gates constrain AI-generated .NET code before code review.

### HoneyDrunk implications
- Evaluate Gordon as a Docker-specific operator for container debugging, but keep broad OpenClaw actions under separate approval/sandbox policy.
- For .NET agent tooling, compiler properties are a better safety boundary than prompt instructions about avoiding unsafe APIs.

## 2026-05-23 compile additions

### Claims
- AWS's Strands Agent “CLI Creator” pattern lets a CLI create and load new commands at runtime from natural-language requests, using Amazon Bedrock/Claude Opus 4.6 for code generation, Strands Agents SDK for tool creation/loading/execution, and MCP for discovering API servers that can provide generated tools additional context. confidence: 1 vendor source, last-confirmed 2026-05-23. [source: raw/2026-05-23-rss-tldr-devops-building-self-extending-cli-tools-with-strands-agent-9-min.md]
- The self-extending CLI pattern is useful for internal platform tools with growing one-off operational needs, but it raises the same generated-code review, sandbox, provenance, and permission questions as coding agents because the application writes and executes new capabilities. confidence: 1 vendor source plus existing agent-security posture, last-confirmed 2026-05-23. [source: raw/2026-05-23-rss-tldr-devops-building-self-extending-cli-tools-with-strands-agent-9-min.md; page: [[ai-coding-agent-security]]]
- CNCF's kubectl-debug evidence-gap article says Kubernetes ephemeral container status does not preserve `lastState` or `restartCount`; a debug session's exit code/duration/target context can disappear after later pod updates, so incident workflows need external capture if debug findings matter. confidence: 1 CNCF community source, last-confirmed 2026-05-23. [source: raw/2026-05-23-rss-tldr-devops-what-kubectl-debug-doesn-t-tell-you-the-silent-evidence-ga.md]

### Typed entities
- SDK/framework: Strands Agents SDK
- service: Amazon Bedrock
- model: Claude Opus 4.6
- protocol: Model Context Protocol (MCP)
- tool: CLI Creator
- tool: kubectl debug
- Kubernetes type: EphemeralContainerStatus
- concept: self-extending CLI
- concept: debug evidence gap

### Explicit relationships
- Self-extending CLIs use agent-generated code to create new operational tools at runtime.
- MCP discovery can expand a generated tool's context and dependency surface.
- Self-extending tools depend-on sandboxing, code review, provenance logging, and scoped credentials before production use.
- `kubectl debug` depends-on external logging/audit capture for durable incident evidence because Kubernetes ephemeral containers do not retain full termination history.

### HoneyDrunk implications
- A self-extending Grid/OpenClaw CLI is attractive, but generated commands should land as reviewed code or quarantined plugins before trusted execution.
- For Kubernetes incidents, capture debug-session findings outside the pod API immediately: logs, command transcript, target container, exit code, timestamps, and operator.

## 2026-05-24 compile additions

### Claims
- Mishra's first-principles agent-training note frames agent training as a loop of prompt, model action, environment transition, reward, and gradient update; the toy example is a tldraw-style text-to-diagram agent emitting JSON `create_shape` and `connect` actions against a validating canvas. confidence: 1 source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-tldr-ai-on-building-agents-from-first-principles-15-minute-read.md]
- The example reward combines JSON validity, schema compliance, layout quality, and semantic coverage of prompt keywords, reinforcing that agent harnesses need explicit environment validators and reward/feedback design rather than vague “make it better” prompting. confidence: 1 source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-tldr-ai-on-building-agents-from-first-principles-15-minute-read.md]

### Typed entities
- person: Mishra
- concept: agent-training loop
- environment: tldraw-style validating canvas
- action schema: `create_shape`
- action schema: `connect`
- artifact format: JSON tool/action output
- concept: reward function
- concept: schema compliance

### Explicit relationships
- Agent training uses environment feedback and reward functions to turn model actions into learnable behavior.
- Structured JSON actions depend-on validators before reward scoring can be trusted.
- Reward design complements harness evaluation because both define what counts as successful agent behavior.

### HoneyDrunk implications
- For Grid/Lore agent evals, define small executable environments with typed actions, validators, and scoring before attempting broader autonomous training or self-improvement.
- Treat reward functions as product/design artifacts: validity, safety, task coverage, and aesthetics may need separate weighted checks.

## 2026-05-30 compile additions

### Claims
- OpenAI Secure MCP Tunnel reinforces private-tool connectivity as a harness primitive: supported products can call a private MCP server through an outbound `tunnel-client` without opening public ingress. confidence: 1 official vendor docs source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-openai-secure-mcp-tunnel.md; page: [[mcp-tool-governance-and-app-surfaces]]]
- Claude Code dynamic workflows make subagent fan-out a productized harness capability: Claude plans, writes orchestration scripts, runs many parallel subagents, verifies outputs, and resumes long-running work outside the conversation context. confidence: 1 official vendor source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-anthropic-introducing-dynamic-workflows-in-claude-code.md; page: [[claude-platform-2026]]]
- Microsoft Learn's orchestration guide reinforces that agent harnesses should start at the lowest complexity level that works: direct model call, single agent with tools, then multiagent orchestration only when prompt/tool/context/security limits justify it. confidence: 1 Microsoft architecture source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-microsoft-learn-ai-agent-orchestration-patterns.md; page: [[multi-agent-architectures]]]
- Azure Container Apps dynamic sessions provide a platform-managed MCP shell execution environment in preview, demonstrating that harness compute can be offered as managed ephemeral sessions rather than bespoke server code. confidence: 1 Microsoft Learn source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-microsoft-learn-tutorial-use-mcp-with-dynamic-sessions-shell.md]
- GitHub Copilot guidance for .NET developers distinguishes chat for understanding/planning/explanation from agentic workflows for bounded change/verify/update/rerun tasks; this maps directly onto harness definitions of scope, definition of done, and reviewable diffs. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-rss-net-blog-doing-more-with-github-copilot-as-a-net-developer.md]

### Typed entities
- product: OpenAI Secure MCP Tunnel
- product: Claude Code dynamic workflows
- platform: Azure Container Apps dynamic sessions
- product: GitHub Copilot
- feature: Copilot CLI
- feature: Copilot cloud coding agent
- concept: effort control
- concept: definition of done
- concept: reviewable diff
- concept: managed ephemeral shell session

### Explicit relationships
- Agent harnesses use private MCP tunnels to reach internal tools without public exposure.
- Dynamic workflows depend-on budget controls, progress persistence, subagent verification, and sandboxed execution.
- Managed shell sessions depend-on API-key or stronger authentication and should be isolated from persistent secrets.
- Chat-mode assistance complements agentic delegation; it does not supersede bounded execution tasks when changes must be made and verified.

### HoneyDrunk implications
- Treat parallel subagents as a scarce resource, not a default mode; require cost telemetry and clear synthesis criteria.
- For private tools, design connectivity, auth, and audit before exposing MCP servers to assistant clients.
- For .NET work, write agent tasks with explicit boundaries, constraints, tests to run, and stop conditions.

## 2026-05-31 compile additions

### Claims
- Hugging Face's agent glossary reinforces the working split used in Lore: the model is raw text generation, scaffolding is the behavior-defining layer of prompts/tools/context/memory, and the harness is the execution loop that calls the model, routes tool calls, handles errors, and decides when to stop. confidence: 1 source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-hugging-face-blog-harness-scaffold-and-the-ai-agent-terms-worth-gettin.md]
- The same glossary distinguishes tools, skills, and subagents: tools are actions, skills package multi-step task knowledge, and subagents are independently reasoning agents called by another agent. confidence: 1 source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-hugging-face-blog-harness-scaffold-and-the-ai-agent-terms-worth-gettin.md]
- OpenAI's Tax AI case study shows a production self-improvement loop where practitioner corrections and product traces become grouped findings, targeted evals, scoped Codex tasks, validation runs, and reviewed product changes. confidence: 1 official/vendor-partner source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-openai-via-tldr-ai-building-self-improving-tax-agents-with-codex.md]
- The Tax AI pattern depends-on bounded automation: ambiguous practitioner corrections route back to product/engineering review instead of being forced into automatic Codex fixes. confidence: 1 official/vendor-partner source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-openai-via-tldr-ai-building-self-improving-tax-agents-with-codex.md]
- Google ADK for Kotlin and ADK for Android 0.1.0 extends ADK agent harness patterns to Kotlin backends and Android on-device/hybrid agents, including session state, memory service, function tools, long-running tools, MCP tools, A2A plugins, OpenTelemetry, and a development web interface. confidence: 1 vendor source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-google-developers-blog-announcing-adk-for-kotlin-and-adk-for-android-0.md; page: [[google-agent-platform-and-gemini-api-2026]]]
- Claude Code agent view productizes multi-session agent management in the CLI: `claude agents`, left-arrow navigation, `/bg`, and `claude --bg` let users background, peek, answer, and reattach to multiple sessions. confidence: 1 vendor product source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-claude-blog-agent-view-in-claude-code.md; page: [[claude-platform-2026]]]
- OpenAI's evaluation playbook reinforces that harness design is part of the evaluation result: tools, scaffolding, state management, retries, context compaction, and budget can materially change observed capability. confidence: 1 official source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-openai-a-shared-playbook-for-trustworthy-third-party-evaluations.md; page: [[agent-evaluation-and-benchmarks]]]

### Typed entities
- concept: scaffold
- concept: harness
- concept: skill
- concept: subagent
- product/system: Tax AI
- company: Crete
- company: Thrive Holdings
- tool: Codex
- framework: ADK for Kotlin
- framework: ADK for Android
- product: Claude Code agent view
- command: `claude agents`
- command: `claude --bg`
- command: `/bg`
- page: [[agent-evaluation-and-benchmarks]]

### Explicit relationships
- Agent harnesses use scaffolding, tool routing, state, and stop conditions to turn model output into action.
- Skills complement tools by packaging reusable task knowledge, while subagents add independent reasoning and tool use.
- Self-improving agent loops depend-on production traces, expert corrections, targeted evals, scoped tasks, and human review.
- ADK for Android uses on-device Gemini Nano retrieval agents to keep private document analysis local while a cloud orchestrator handles broader reasoning.
- Agent view depends-on background session state and user-attention routing for parallel Claude Code sessions.
- Agent evaluations depend-on harness disclosure because harness choices can change measured capability.

### HoneyDrunk implications
- Keep Lore/OpenClaw vocabulary precise: do not call every prompt, tool, skill, scaffold, and orchestrator an "agent" when a narrower term is available.
- For self-improving HoneyDrunk agents, first design trace capture and eval grouping; do not ask a coding agent to improve production behavior from vague feedback.
- For parallel agents, build a queue/status surface and attention budget before increasing concurrency.
- Treat any benchmark score as harness-specific unless the report discloses tools, retries, state, and budget.

## 2026-06-01 compile additions

### Claims
- System Design Newsletter's state/memory source argues that long-running agents fail when state, memory, and consistency rules are conflated: state tracks the current workflow, memory spans tasks, and external systems remain the system of record. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ai-agents-state-memory-consistency-a-deep-dive.md]
- The same source recommends checkpointing, state versioning, rollback to the earliest affected step, scoped memory retrieval, memory lifecycle management, and "react fast with state, learn slowly with memory." confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ai-agents-state-memory-consistency-a-deep-dive.md]
- Azure Container Apps dynamic sessions provide isolated session-pool execution contexts for user-generated or third-party code, with Entra-authenticated management APIs, session identifiers, automatic allocation, cooldown destruction, optional managed identity, Azure Monitor logging, and configurable outbound network access. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-use-dynamic-sessions-in-azure-container-apps.md]
- Stephen Toub's dotnet/runtime CCA report reinforces that coding-agent harness success depends-on repo-specific instructions, accessible dependencies/build commands, task selection, and verification feedback loops; early dotnet/runtime CCA success was poor before instructions and network/build constraints were addressed. confidence: 1 Microsoft/.NET source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ten-months-with-copilot-coding-agent-in-dotnet-runtime.md]
- DigitalOcean's OpenCode integration source frames inference routing as a harness-level model-selection control: OpenAI-compatible calls can target `router:<name>` so a router chooses among models by latency, cost, and quality rather than hardcoding one provider/model. confidence: 1 vendor source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-opencode-now-supports-digitalocean-inference-router-for-intelligent-mo.md]
- Warne's Claude Code reflection and System Design Newsletter's agent-use source both reinforce human responsibility: agents are useful for code generation, tests, and codebase exploration, but humans still need to understand changes, judge review comments, own diagnosis, and set up feedback loops where errors are cheap to detect and undo. confidence: 2 commentary sources, last-confirmed 2026-06-01. [sources: raw/2026-06-01-web-with-claude-less-coding-more-testing.md; raw/2026-06-01-web-how-to-get-ahead-of-99-of-software-engineers-with-ai-agents.md]

### Typed entities
- concept: stateful agent
- concept: short-term memory
- concept: long-term memory
- concept: external memory / system of record
- framework: LangGraph
- component: SqliteSaver
- component: PostgresSaver
- platform: Azure Container Apps dynamic sessions
- role: Azure ContainerApps Session Executor
- product: GitHub Copilot Coding Agent / CCA
- tool: OpenCode
- product: DigitalOcean Inference Router
- product: Claude Code

### Explicit relationships
- Long-horizon agents depend-on durable state, checkpointing, versioning, and scoped memory retrieval.
- State updates supersede current-task behavior immediately, while long-term memory updates only after a durable preference is established.
- Systems of record supersede stored memory when live data, inventory, prices, or source-control state disagree.
- Dynamic sessions use session identifiers and session pools to provide isolated executable contexts for agent/tool workloads.
- Inference routers complement agent harnesses by moving model choice from prompt convention into provider-routing infrastructure.

### HoneyDrunk implications
- Treat OpenClaw memory as a designed subsystem: record what is current workflow state, what is durable memory, what expires, and what external source wins conflicts.
- For dynamic code/session execution, design identifier entropy, token custody, egress policy, logging, and cooldown settings before exposing sessions to agents.
- Route coding agents toward tasks with fast, reviewable feedback and reversible outputs; high-blast-radius diagnosis/deployment should keep human ownership.

## 2026-06-02 compile additions

### Claims
- IBM Research argues that scalable enterprise agents need "agent logic" in the harness layer: knowledge graphs, algorithms, program-analysis libraries, policy systems, and directed workflows that steer model behavior while reducing context and token consumption. confidence: 1 vendor/research source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-hugging-face-ibm-research-beyond-llms-why-scalable-enterprise-ai-adopt.md]
- IBM cites multiple internal/product case studies where structured harness logic outperforms LLM-only or generic ReAct baselines on app understanding, test generation, incident investigation, compliance modernization, healthcare policy enforcement, and asset maintenance; the exact numbers are vendor-reported and should be locally validated before procurement decisions. confidence: 1 vendor/research source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-hugging-face-ibm-research-beyond-llms-why-scalable-enterprise-ai-adopt.md]
- Perplexity's Search as Code architecture exposes search primitives as a Python SDK inside secure sandboxes so agents can generate task-specific retrieval, ranking, filtering, fanout, aggregation, and rendering pipelines instead of calling a monolithic search API repeatedly. confidence: 1 vendor/research source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-perplexity-research-rethinking-search-as-code-generation.md]
- Perplexity reports that filesystem-backed explicit serialization for sandbox state was more reliable than REPL-style implicit state on very long trajectories, reinforcing declarative state handoff as a long-horizon harness design pattern. confidence: 1 vendor/research source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-perplexity-research-rethinking-search-as-code-generation.md]
- Sean Goedecke's agent-vs-pipeline essay frames the control-flow tradeoff clearly: pipelines are more predictable and cost-bounded, while agents are more flexible when context gathering, action/reaction loops, or hard tasks exceed one-shot prompt assembly. confidence: 1 practitioner source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-sean-goedecke-build-agents-not-pipelines.md]
- Simon Willison's Pasted File Editor prototype shows a small harness/product-interface pattern: large clipboard pastes or dragged/opened files can be converted into file attachments while preserving the prompt/editor text, reducing accidental context pollution in AI-assisted editing workflows. confidence: 1 practitioner source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-simon-willison-pasted-file-editor.md]

### Typed entities
- concept: agent logic
- technique: program analysis
- technique: knowledge graph
- technique: policy-as-code
- product/platform: IBM watsonx Code Assistant for Z
- product/platform: IBM Instana I3
- product/platform: IBM Concert Platform
- product/platform: IBM Maximo Condition Insights
- architecture: Search as Code / SaC
- SDK: Agentic Search SDK
- runtime: secure compute sandbox
- state pattern: filesystem-backed serialization
- concept: pipeline
- concept: agentic context gathering
- tool/prototype: Pasted File Editor

### Explicit relationships
- Agent logic depends-on structured harness primitives to constrain context and decision rights before model prompting.
- Program analysis and knowledge graphs complement LLM reasoning by narrowing the search/context space.
- Search as Code uses generated code and deterministic sandbox execution to compose retrieval primitives within an agent turn.
- Explicit serialized state supersedes implicit REPL state when long trajectories require traceable intermediate artifacts.
- Pipelines supersede agents when cost, context size, and local-model constraints are strict; agents supersede pipelines when context gathering and action loops are the hard part.
- File attachments can reduce context pollution by separating durable pasted source material from the active editor prompt.

### HoneyDrunk implications
- For Lore retrieval, consider Search-as-Code style primitives only after the flat-file layer stops scaling; keep explicit serialized intermediate state over hidden REPL state for reproducibility.
- When deciding between OpenClaw agents and deterministic workflows, use task shape: strict budget/local model/simple control flow favors pipelines; uncertain context gathering and reversible exploration favors agents.
- For AI editor surfaces, prefer attachment-aware paste/file handling so long source material is inspectable, removable, and not silently mixed into the instruction text.

### Quality notes
- IBM and Perplexity results are vendor-authored and benchmark-sensitive. They are useful architecture signals, not local performance evidence.

## 2026-06-03 compile additions

### Claims
- Azure `azure-functions-skills` public preview packages Azure Functions agent skills, a `functions-copilot` agent definition, MCP configuration, hooks, and instruction files for hosts such as GitHub Copilot CLI, Claude Code, Codex CLI, and VS Code. confidence: 1 Microsoft Azure SDK Blog source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-azure-blog-introducing-azure-functions-skills-an-ai-era-workspace-for-.md]
- The Azure Functions `doctor` flow uses deterministic checks by default and opt-in semantic LLM checks for code issues such as hardcoded secrets, client-per-invocation patterns, blocking I/O, and Durable Functions nondeterminism; Microsoft recommends Tier 1-only validation on untrusted PRs and deeper checks after merge/release. confidence: 1 Microsoft source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-azure-blog-introducing-azure-functions-skills-an-ai-era-workspace-for-.md]
- n8n frames agent reliability as layered controls across model configuration, prompt structure, output schemas, tool design, guardrails, and routing logic, with capability restrictions applied before, during, and after agent execution rather than left to a single prompt. confidence: 1 n8n source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-n8n-blog-how-can-i-make-ai-agents-more-reliable-and-restrict-the-actio.md]
- DigitalOcean Serverless Inference exposes OpenAI-compatible, Anthropic-compatible, multimodal, retrieval, MCP, web-search, prompt-caching, and routing surfaces behind one API, reinforcing that model routing, built-in tools, telemetry, and billing can be provider infrastructure rather than bespoke harness code. confidence: 1 vendor source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-digitalocean-digitalocean-serverless-inference-a-deep-dive.md]
- GitHub Copilot app technical preview productizes multi-agent work management through My Work, per-session git worktrees, Agent Merge, canvases, local/cloud sandboxes, custom skills, MCP connections, scheduled tasks, Memory++/`/chronicle`, and partner agent apps. confidence: 1 GitHub product source, last-confirmed 2026-06-03. [source: raw/2026-06-03-web-github-blog-github-copilot-app-the-agent-native-desktop-experience.md]
- Fowler's June 2 fragment reinforces a human-attention constraint for parallel agents: many agents can run concurrently, but architecture judgment, conflict resolution, and final review still serialize through the human operator. confidence: 1 Fowler fragment source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-martin-fowler-fragments-june-2.md]

### Typed entities
- package/plugin: `azure-functions-skills`
- agent definition: `functions-copilot`
- command: `npx @azure/functions-skills install`
- command: `npx @azure/functions-skills doctor`
- product: GitHub Copilot app
- feature: My Work
- feature: Agent Merge
- feature: canvas
- feature: local/cloud sandbox
- feature: Memory++ / `/chronicle`
- product: DigitalOcean Serverless Inference
- feature: Inference Router
- control: structured output schema
- control: guardrail node
- concept: human attention bottleneck

### Explicit relationships
- Agent skills package procedural knowledge, hooks, MCP config, and instruction files so agent behavior can be installed and validated as workspace infrastructure.
- Deterministic validation should run before semantic LLM checks on untrusted code because LLM deep checks can execute with file-write and shell permissions.
- Agent reliability depends-on schemas, narrow tools, fixed/dynamic parameters, guardrails, and routing logic; these controls complement model choice.
- Inference routers and built-in platform tools complement local harness code by centralizing model selection, tool execution, telemetry, and billing.
- Multi-agent control centers depend-on worktree isolation, inspectable plans, sandbox policies, and human review capacity.

### HoneyDrunk implications
- Treat HoneyDrunk skills as installable, versioned workspace/runtime artifacts with validation commands, not just markdown instructions.
- For OpenClaw agent validation, separate safe deterministic checks from risky semantic/agentic checks and gate the latter by trusted event source.
- Build any parallel-agent dashboard around human review bandwidth: surface status, diffs, tests, unresolved decisions, and conflict risks before increasing concurrency.
- If evaluating DigitalOcean Serverless Inference, log router-selected models, tool use, cache hit rates, rate limits, and per-feature cost; the value is operational routing, not just endpoint compatibility.

### Quality notes
- Azure, DigitalOcean, GitHub, and n8n sources are vendor-authored and useful for architecture signals; validate preview features, pricing, and policy controls locally before standardizing.

## 2026-06-04 compile additions

### Claims
- Microsoft Foundry's Build 2026 agent platform source frames the production-agent stack as build, deploy, and operate layers: Microsoft Agent Framework for harness/framework work, Foundry Agent Service for hosted runtime and distribution, and Foundry tracing/evaluation/optimizer for operations. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-microsoft-foundry-blog-build-and-run-agents-at-scale-with-microsoft-fo.md]
- Microsoft Agent Framework stable updates include an agent harness with skills, memory, middleware, integrations with GitHub Copilot SDK and Claude Agent SDK, and multi-agent orchestration patterns such as Magentic-One. confidence: 1 Microsoft Foundry source plus 1 Agent Framework session source, last-confirmed 2026-06-04. [sources: raw/2026-06-04-web-microsoft-foundry-blog-build-and-run-agents-at-scale-with-microsoft-fo.md; raw/2026-06-04-web-microsoft-agent-framework-microsoft-agent-framework-at-build-2026.md]
- Foundry Agent Service is positioned as a framework-agnostic hosted runtime for production agents with per-session sandboxing, durable state/file access, long-running autonomous agents, routines, and Responses API / Invocations protocol support. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-microsoft-foundry-blog-build-and-run-agents-at-scale-with-microsoft-fo.md]
- Foundry Agent Service memory now distinguishes procedural memory, user memory, and session memory; procedural memory is framed as learning how to perform recurring work across runs. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-microsoft-foundry-blog-build-and-run-agents-at-scale-with-microsoft-fo.md]
- DigitalOcean's prefix-aware routing source reinforces that inference routing is a harness/runtime concern for agentic traffic: long shared prompts, tool definitions, and multi-turn context create cache-locality problems that naive load balancing wastes. confidence: 1 vendor infrastructure source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-digitalocean-the-inference-tax-how-prefix-aware-routing-eliminates-the.md; page: [[edge-ai-and-ai-infrastructure-2026]]]

### Typed entities
- platform: Microsoft Foundry
- service: Foundry Agent Service
- framework: Microsoft Agent Framework
- SDK: GitHub Copilot SDK
- SDK: Claude Agent SDK
- pattern: Magentic-One
- protocol/API: Responses API
- protocol/API: Invocations protocol
- feature: hosted agents
- feature: routines
- memory type: procedural memory
- memory type: user memory
- memory type: session memory
- concept: prefix-aware routing

### Explicit relationships
- Production agent platforms depend-on harness, runtime, distribution, observability, evaluation, security, and optimization layers rather than model calls alone.
- Foundry Agent Service uses sandboxed sessions and durable state to host long-running autonomous agents.
- Procedural memory complements user/session memory by storing task method rather than only user facts or current conversation context.
- Inference routing depends-on prompt/cache locality when agent traffic repeatedly sends shared system prompts, tool definitions, or document context.

### HoneyDrunk implications
- Keep OpenClaw/Honeyclaw architecture split into build-time skills/framework, runtime isolation/state, distribution surface, and operate/eval loops; do not let one framework choice obscure the other responsibilities.
- If testing Foundry hosted agents, validate sandbox boundaries, file durability, identity, cost, long-running routines, trace export, and rollback before production use.
- Treat procedural memory as powerful but risky: learned workflows should be inspectable, versioned, and superseded when they conflict with current repo instructions.

## 2026-06-05 compile additions

### Claims
- Hugging Face rebuilt the official `hf` CLI for both humans and coding agents, using agent-environment detection to switch output toward compact, complete, untruncated, non-ANSI agent-readable formats while preserving richer human terminal output. confidence: 1 Hugging Face source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-designing-the-hf-cli-as-an-agent-optimized-way-to-work-with-the-hub.md]
- Hugging Face reports that, on evaluated multi-step Hub tasks, agents using the `hf` CLI achieved equal-or-better success with roughly 1.3x to 1.8x fewer tokens than curl/Python SDK baselines, with larger savings on complex write/sync/copy workflows; treat quantitative results as vendor-run evals. confidence: 1 Hugging Face source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-designing-the-hf-cli-as-an-agent-optimized-way-to-work-with-the-hub.md]
- The `hf` CLI adds agent-friendly harness affordances: explicit `--format human|agent|json|quiet`, next-command hints to stderr, non-blocking fail-fast confirmation behavior, retry-safe/idempotent options, dry runs for data-moving commands, predictable resource-verb command structure, and an auto-generated `hf` skill. confidence: 1 Hugging Face source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-designing-the-hf-cli-as-an-agent-optimized-way-to-work-with-the-hub.md]
- OpenAI's Codex role-specific plugins reinforce that agent harnesses are becoming packaged distributions of apps, skills, instructions, and workflows tailored to role/task context rather than generic chat prompts. confidence: 1 OpenAI source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-codex-for-every-role-tool-and-workflow.md]
- Anthropic's Agent SDK monthly credit program separates Agent SDK/`claude -p`/Claude Code GitHub Actions usage from interactive Claude subscription limits for eligible plans starting 2026-06-15, while advising teams running shared production automation to use Claude Platform API keys for predictable pay-as-you-go billing. confidence: 1 Anthropic Help Center source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-use-the-claude-agent-sdk-with-your-claude-plan.md]

### Typed entities
- CLI: `hf`
- product/platform: Hugging Face Hub
- environment signal: `AI_AGENT`
- environment signal: `CODEX_SANDBOX`
- environment signal: `CLAUDE_CODE`
- CLI flag: `--format`
- CLI flag: `--json`
- CLI flag: `--quiet`
- CLI flag: `--dry-run`
- skill: `hf` CLI skill
- product: Codex role-specific plugins
- SDK: Claude Agent SDK
- command: `claude -p`
- integration: Claude Code GitHub Actions

### Explicit relationships
- Agent-optimized CLIs reduce harness friction by providing parseable complete output, noninteractive behavior, idempotency, and next-step hints.
- CLI skills complement predictable command trees by giving agents a compact command reference at session start.
- Role-specific plugins use apps, skills, instructions, and workflows as reusable harness packages.
- Agent SDK billing depends-on plan type and is separate from interactive subscription limits only for eligible subscription users after 2026-06-15.

### HoneyDrunk implications
- Design HoneyDrunk CLIs/tools with explicit agent mode: no prompts, structured full output, `--json`/quiet support, dry-run, idempotent retries, and next-command hints on stderr.
- Treat skills as generated/versioned command references where possible, not hand-maintained prose that drifts from the CLI.
- Use subscription Agent SDK credits only for individual experimentation or small automations; shared production HoneyDrunk automation should use explicit API billing, budgets, and service identities.

### Quality notes
- Hugging Face benchmark results are vendor-authored but methodologically useful because they grade live Hub state instead of trusting agent self-reports. Billing details are plan/date-sensitive and should be verified near use.

## 2026-06-07 compile additions

### Claims
- Reachy Mini's conversation app can now register public Hugging Face Gradio Spaces as remote MCP tools, with per-profile `tools.txt` enablement, namespaced remote tool IDs, install/list/remove commands, Hub validation, MCP endpoint probing, and no arbitrary tool code downloaded into the local app. confidence: 1 Hugging Face/Pollen Robotics source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-adding-mcp-tools-to-reachy-mini.md]
- The Reachy Mini source says prompts can encourage parallel tool calls for combined search/weather questions, but deterministic parallel orchestration should move into code when reliability matters. confidence: 1 source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-adding-mcp-tools-to-reachy-mini.md]
- Azure Functions serverless agents runtime defines agents in markdown files, app-wide defaults in `agents.config.yaml`, remote MCP servers in `mcp.json`, and can combine browser/debug chat agents, timer-triggered agents, sandboxed Python execution, dynamic session pools, and managed MCP connector tools. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-quickstart-build-serverless-agents-using-azure-functions.md]
- Foundry Agent Optimizer turns eval output into harness configuration changes by rewriting instructions, generating reusable skills, selecting model deployments, or improving local tool descriptions, with candidates injected through configuration rather than hardcoded feature branches. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-introducing-agent-optimizer-in-foundry-agent-service.md]
- GitHub enterprise-managed plugins in VS Code and Copilot CLI let enterprise administrators auto-install plugins and enforce baseline hooks and MCP configurations through `.github-private/.github/copilot/settings.json`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-enterprise-managed-plugins-in-vs-code-in-public-preview.md]

### Typed entities
- product: Reachy Mini conversation app
- platform: Hugging Face Spaces
- protocol: Model Context Protocol
- file: `tools.txt`
- file: `installed_tool_spaces.json`
- runtime: Azure Functions serverless agents runtime
- file: `agents.config.yaml`
- file: `mcp.json`
- product: Foundry Agent Optimizer
- product: GitHub Copilot enterprise-managed plugins
- file: `.github-private/.github/copilot/settings.json`

### Explicit relationships
- Reachy Mini uses profile-scoped tool enablement to keep local embodied tools and optional remote MCP tools in one registry.
- Prompt instructions complement, but do not guarantee, parallel tool orchestration.
- Azure Functions serverless agents use markdown agent definitions and Functions triggers to turn agents into deployable serverless workloads.
- Enterprise-managed plugins use centralized settings to distribute hooks, MCP configuration, skills, and agents across VS Code and Copilot CLI clients.
- Foundry Agent Optimizer uses evaluation feedback to update harness configuration rather than model weights.

### HoneyDrunk implications
- Model HoneyDrunk agent profiles after small explicit tool lists; remote tools should be opt-in per profile and namespaced to avoid collision.
- For scheduled Honeyclaw/OpenClaw-style jobs, Azure Functions serverless agents are worth a spike only if identity, sandbox, logs, connector auth, and local repo fit are validated.
- Enterprise-managed plugins are relevant to HoneyDrunk only after plugin provenance, hook behavior, MCP server trust, and default install policy are explicit.

### Quality notes
- Reachy Mini and Foundry sources are vendor/product posts. GitHub plugin management is public preview. Azure Functions quickstart is concrete but includes auth-gated Learn scaffolding in raw; promoted facts came from the readable body.

## 2026-06-08 compile additions

### Claims
- Copilot SDK GA reinforces that commercial coding-agent harnesses expose stable programmatic primitives for planning, tool invocation, file edits, streaming, multi-turn sessions, MCP, hooks, prompt-section customization, cloud/remote sessions, and OpenTelemetry tracing. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-copilot-sdk-is-now-generally-available.md; page: [[github-copilot-and-app-token-changes]]]
- Copilot CLI prompt scheduling with `/every` and `/after` treats scheduled prompt/skill execution as an in-session harness primitive, while voice input and rubber duck add input and critique subflows to the CLI experience. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-copilot-cli-improved-ui-rubber-duck-prompt-scheduling-and-voice-input.md]
- Copilot app canvases reinforce a durable work-surface pattern: agent progress, state, approvals, and verification should live in an inspectable artifact rather than only in chat transcripts. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-expanded-technical-preview-availability-for-the-github-copilot-app.md]
- VS Code's Agents window and Agent Host Protocol work reinforce multi-client/session-synchronization as a harness concern: sessions, preferences, remote state, side-by-side work, and Git flow need explicit synchronization across clients. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-github-copilot-in-visual-studio-code-may-releases.md]
- Docker Navigator's May issue frames AI agents as moving from code generation into execution in CI and local workflows, making isolation, hardened images, supply-chain response, and local model workflows part of the surrounding harness rather than separate DevOps concerns. confidence: 1 Docker newsletter source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-docker-navigator-ai-workflows-container-security-and-build-reliability.md; page: [[ai-coding-agent-security]]]

### Typed entities
- SDK: GitHub Copilot SDK
- product: GitHub Copilot CLI
- product: GitHub Copilot app
- product/surface: VS Code Agents window
- protocol: Agent Host Protocol / AHP
- feature: canvas
- feature: rubber duck
- feature: scheduled prompt
- feature: remote agent
- feature: session sync
- concept: inspectable work surface
- concept: local model workflow
- product/control: Docker Hardened Images
- product/control: Docker Sandboxes

### Explicit relationships
- Agent harnesses use stable SDK APIs, hooks, MCP, and telemetry to expose repeatable runtime behavior.
- Scheduled prompts depend-on session lifetime and should not be confused with durable external job scheduling unless persisted elsewhere.
- Canvases complement chat transcripts by preserving work state that humans can inspect, edit, approve, and verify.
- Multi-client agent work depends-on synchronized session state, Git state, remote execution state, and preferences.
- CI/local execution harnesses depend-on isolation and supply-chain controls because agents increasingly run code, not only suggest it.

### HoneyDrunk implications
- Model OpenClaw/Honeyclaw scheduled jobs as durable workflow runs with explicit persistence and audit; in-session prompt scheduling is useful but not sufficient for unattended operations.
- Build agent dashboards around structured state: plan, diff, tests, approvals, unresolved decisions, trace IDs, and artifacts.
- If embedding Copilot SDK-like runtimes, require hook-level audit, tool permission checks, and OTel traces from the start.

### Quality notes
- GitHub and Docker sources are vendor-authored. They are strong feature/ecosystem signals but need local verification around plan availability, privacy settings, sandbox behavior, and pricing.

## 2026-06-09 compile additions

### Claims
- Spotify's Honk background coding agent shows a production-scale harness pattern: Claude runs through the Anthropic Agent SDK inside Spotify's own harness on Kubernetes pods, with trusted tools and CI verification across operating systems, while Fleetshift manages target selection, scheduling, progress, and PR tracking. confidence: 1 Spotify Engineering source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-coding-is-no-longer-the-constraint-scaling-developer-experience-to-tea.md; page: [[ai-assisted-software-practice]]]
- Spotify reports Fleet Management has merged more than 2.5 million automated maintenance PRs, mostly auto-merged, and that Honk reduced a recent Java backend migration to three days for one engineer; treat the numbers as vendor/self-reported platform evidence. confidence: 1 source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-coding-is-no-longer-the-constraint-scaling-developer-experience-to-tea.md]
- LangSmith Sandboxes reinforce that code-executing agents need stateful isolated computers: filesystem, shell, package manager, network, service URLs, snapshots/forks, blueprints, auth proxy, and persistent session state behind a microVM boundary. confidence: 1 LangChain source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-give-your-agent-its-own-computer.md; page: [[ai-coding-agent-security]]]
- Microsoft Foundry Build recap says hosted agents are expected to reach GA by early July 2026 with per-session sandboxed compute, state, filesystem access, framework-agnostic deployment, Responses API and Invocations protocol support, and routines for timer/scheduled agents. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-what-s-new-in-microsoft-foundry-build-edition-microsoft-foundry-blog.md]
- Foundry Agent Service memory now distinguishes procedural, user, and session memory, with procedural memory intended to teach agents recurring work methods across runs. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-what-s-new-in-microsoft-foundry-build-edition-microsoft-foundry-blog.md]
- Datadog's unified feature-flag/product-signal source reinforces that agentic release workflows need a single correlated data model for flag exposure, traces, session replay, warehouse metrics, product funnels, and LLM eval scores; fragmented tools turn agent operation into an automated swivel-chair problem. confidence: 1 Datadog source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-how-a-unified-data-model-improves-feature-flag-rollout-decisions-datad.md; page: [[opentelemetry-genai-observability-and-ecosystem]]]

### Typed entities
- company/platform: Spotify
- agent: Honk
- orchestration system: Fleetshift / Fleet Management
- product: Backstage
- control: Soundcheck
- concept: golden state
- product: LangSmith Sandboxes
- isolation type: microVM
- feature: snapshots and forks
- feature: blueprints
- feature: service URLs
- control: auth proxy
- product: Microsoft Foundry hosted agents
- feature: routines
- protocol/API: Responses API
- protocol/API: Invocations protocol
- memory type: procedural memory
- product: Datadog Feature Flags
- product: Datadog MCP Server
- standard: OpenFeature SDK

### Explicit relationships
- Honk uses Kubernetes pods, trusted tools, CI verification, Fleetshift orchestration, and Backstage context to execute background code changes at fleet scale.
- Backstage Software Catalog and Soundcheck golden-state standards provide agent-readable ownership, documentation, and lint/standard feedback.
- LangSmith Sandboxes use microVM isolation and auth proxying to let agents execute code without inheriting production infrastructure or direct secret custody.
- Foundry hosted agents use sandboxed sessions and durable state/filesystem access to host long-running agents.
- Agentic release workflows depend-on correlated product, release, observability, warehouse, and eval data when agents are allowed to hold, continue, or modify rollouts.

### HoneyDrunk implications
- Treat OpenClaw/Honeyclaw background maintenance as a platform workflow: target selection, session scheduling, CI verification, PR tracking, owner routing, and dashboard state should be explicit.
- Build Backstage-like catalog/golden-state data for agents before expecting reliable cross-repo edits; fragmented repos reduce agent quality.
- For any agent that installs dependencies or runs generated code, prefer microVM/session isolation with injected scoped credentials over local host execution.
- For release/feature-flag agents, do not expose action tools until flag state, traces, product impact, and rollback controls are queryable from one governed surface.

### Quality notes
- Spotify, LangChain, Microsoft, and Datadog sources are vendor/platform-authored; promoted claims are operational patterns and feature signals, not procurement decisions. No secrets or private identifiers were copied.

## 2026-06-10 compile additions: composable Spaces, OpenEnv, sandboxing, Foundry routing, and decision load

### Source-backed claims
- Hugging Face Spaces can expose plain-text `agents.md` instructions that tell agents how to call a Space, including schema, request, polling, file upload, and authentication patterns; Hugging Face used this pattern to chain image generation and 3D Gaussian-splat generation Spaces into a deployed 3D Paris gallery. Source: `raw/2026-06-10-web-hugging-face-how-an-agent-built-a-3d-paris-gallery-by-chaining-two-hugging-face-space.md`. confidence: 1 source, last-confirmed 2026-06-10.
- OpenEnv is positioned as an interoperability layer for agentic reinforcement-learning environments: environments expose Gymnasium-style `reset()`, `step()`, and `state()` APIs over HTTP/WebSocket, package with Docker, and can integrate MCP as a first-class interface. Source: `raw/2026-06-10-web-hugging-face-the-open-source-community-is-backing-openenv-for-agentic-rl.md`. confidence: 1 source, last-confirmed 2026-06-10.
- OpenEnv standardizes publishing, deploying, and consuming environments, but does not prescribe reward definitions or training loops. Source: `raw/2026-06-10-web-hugging-face-the-open-source-community-is-backing-openenv-for-agentic-rl.md`. confidence: 1 source, last-confirmed 2026-06-10.
- `micropython-wasm` shows an experimental way to keep a persistent Python interpreter inside a WASM sandbox with selected host calls, memory limits, and experimental fuel-based CPU controls. Source: `raw/2026-06-10-web-simon-willison-running-python-code-in-a-sandbox-with-micropython-and-wasm.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Microsoft Foundry gateway guidance says direct model endpoint use pushes retry, circuit breaking, failover, model selection, throttling, and observability responsibilities into every client/orchestrator; a gateway can centralize those concerns but becomes its own architecture component. Source: `raw/2026-06-10-web-microsoft-learn-access-foundry-models-and-other-language-models-through-a-gateway-azure.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Microsoft's Foundry chat baseline puts the chat application layer in front of Foundry Agent Service as the user access boundary, because Foundry project roles can grant broad access to all agents in a project and the app must enforce per-user agent/conversation authorization. Source: `raw/2026-06-10-web-microsoft-learn-baseline-microsoft-foundry-chat-reference-architecture-azure-architectur.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Thoughtworks argues that AI adoption can move humans from execution into continuous evaluation, creating decision fatigue unless workflows add automated gates, upstream specs, guardrails, and exception-based human review. Source: `raw/2026-06-10-web-thoughtworks-the-paradox-of-acceleration-overcoming-ai-induced-decision-fatigue-and-b.md`. confidence: 1 source, last-confirmed 2026-06-10.

### Typed entities
- project: Hugging Face Spaces
- file: agents.md
- project: OpenEnv
- library: Gymnasium
- project: MCP
- project: micropython-wasm
- project: Microsoft Foundry Agent Service
- concept: agentic RL environment
- concept: decision fatigue
- decision: OpenClaw remote-tool and sandbox policy

### Explicit relationships
- Hugging Face Spaces `agents.md` uses plain-text tool instructions to make model-backed apps agent-callable.
- OpenEnv depends-on containerized environments, client/server APIs, and harness/trainer interoperability.
- OpenEnv uses MCP as a first-class production/simulation interface.
- `micropython-wasm` depends-on Wasmtime and selected host functions to expose controlled capabilities.
- Foundry baseline architecture depends-on an app/gateway layer for end-user authorization and progressive rollout because Foundry project RBAC is too broad for consumer-facing access.
- Automated gates reduce AI-induced decision fatigue by moving routine validation out of human review queues.

### HoneyDrunk implications
- Treat remote model Spaces as supply-chain dependencies: require provenance, auth scope, returned-artifact validation, and cost/rate limits before adding them to OpenClaw.
- Watch OpenEnv as a possible standard for reusable agent training/evaluation harnesses, but do not assume it solves rewards, benchmark leakage, or production safety.
- Keep generated-code execution in isolated sandboxes; `micropython-wasm` is a useful design reference, not a ready security boundary.
- For Foundry-style agents, prefer an application-controlled access and routing layer over direct model/project API exposure.
- Add cognitive-load metrics to agent workflows: review queue length, human validation time, rollback/rework, and exception rate.

### Quality notes
- Hugging Face, Microsoft, and Thoughtworks are platform/vendor/practice sources. The claims are durable architecture signals, but each requires local threat modeling and workload testing.

## 2026-06-11 compile additions: context engineering, outer harnesses, managed agents, and Codex controls

### Source-backed claims
- Fowler/Thoughtworks frames coding-agent context engineering as deliberate curation of reusable prompts, rules, skills, subagents, MCP servers, hooks, tools, and workspace files; more context is not automatically better because excessive context increases cost and can reduce agent effectiveness. Source: `raw/2026-06-11-web-martin-fowler-context-engineering-for-coding-agents.md`. confidence: 1 source, last-confirmed 2026-06-11.
- The same context-engineering source distinguishes who loads context: the LLM can lazy-load skills/tools, a human can invoke slash commands, and agent software can deterministically trigger hooks. Source: `raw/2026-06-11-web-martin-fowler-context-engineering-for-coding-agents.md`. confidence: 1 source, last-confirmed 2026-06-11.
- Fowler/Thoughtworks defines an outer coding-agent harness as feedforward guides plus feedback sensors; computational controls such as linters/tests/type checks are cheap and deterministic, while inferential controls such as AI review are slower, costlier, and probabilistic. Source: `raw/2026-06-11-web-martin-fowler-harness-engineering-for-coding-agent-users.md`. confidence: 1 source, last-confirmed 2026-06-11.
- Google I/O 2026 announced Antigravity 2.0, Antigravity CLI, Managed Agents in the Gemini API, and Antigravity SDK; Google positions these as agent harness surfaces with subagents, terminal sandboxing, credential masking, hardened Git policies, remote sandboxes, and self-hostable agent control. Source: `raw/2026-06-11-web-google-developers-blog-all-the-news-from-the-google-i-o-2026-developer-keynote.md`. confidence: 1 vendor source, last-confirmed 2026-06-11.
- OpenAI describes internal Codex deployment controls as managed configuration, sandbox write/network boundaries, approval policy, auto-review for some boundary-crossing actions, network allowlists, OS keyring credential storage, enterprise workspace pinning, command allow/block rules, and OpenTelemetry/compliance logs. Source: `raw/2026-06-11-web-openai-running-codex-safely-at-openai.md`. confidence: 1 official OpenAI source, last-confirmed 2026-06-11.

### Typed entities
- concept: context engineering
- concept: outer coding-agent harness
- control: feedforward guide
- control: feedback sensor
- control type: computational control
- control type: inferential control
- product: Google Antigravity 2.0
- CLI: Antigravity CLI
- SDK: Antigravity SDK
- feature: Gemini API Managed Agents
- product: OpenAI Codex
- control: managed network policy
- control: auto-review mode
- standard: OpenTelemetry

### Explicit relationships
- Context engineering uses rules, skills, MCP servers, subagents, hooks, and workspace files to shape model behavior.
- Outer harnesses use feedforward controls to steer agents before action and feedback sensors to let agents self-correct after action.
- Computational sensors complement inferential review because deterministic checks can run earlier and more often.
- Google Antigravity Managed Agents use remote sandboxing and harness provisioning to reduce local infrastructure setup.
- Codex safety depends-on sandbox policy, approval policy, network policy, credential custody, and agent-native telemetry, not prompt instructions alone.

### HoneyDrunk implications
- Keep OpenClaw/Honeyclaw context small and task-scoped: always-on AGENTS guidance, lazy-loaded skills, profile-specific tools, and deterministic hooks should be separate levers.
- Improve repeated agent failures by adding either a guide or a sensor; do not rely on humans remembering to re-explain recurring constraints.
- For coding agents, log policy decisions and tool actions in addition to process/file changes so security review can explain agent intent.

### Quality notes
- Fowler/Thoughtworks sources are practice guidance. Google and OpenAI sources are vendor/platform-authored. Promoted claims are durable harness patterns, not procurement decisions.
