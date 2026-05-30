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
