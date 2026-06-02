# AI-Assisted Software Practice

## Decision-useful summary
The strongest practical signal is conservative: AI increases throughput, but teams need smaller changes, guardrails, ruthless documentation, automated verification, security skepticism, explicit harness/context design, and evidence from real use. Fowler/Thoughtworks materials frame AI as a forcing function to revisit fundamentals rather than abandon them. The newer May 2026 sources sharpen that point: Simon Willison says vibe coding and agentic engineering are blurring as agents become more reliable, so usage/provenance and exercised software matter more than polished repos; a CivicSurvival case study shows nontraditional developers can ship large systems with AI only when they formalize architecture, context, analyzers, logs, audits, and live testing. [sources: raw/2026-05-03-rss-martin-fowler-fragments-april-9.md; raw/2026-05-03-rss-martin-fowler-fragments-april-14.md; raw/2026-05-03-rss-martin-fowler-fragments-april-21.md; raw/2026-05-03-rss-martin-fowler-fragments-april-29.md; raw/2026-05-06-rss-martin-fowler-fragments-may-5.md; raw/2026-05-03-rss-simonwillison-zig-ai-contribution-policy.md; raw/2026-05-07-rss-simon-willison-vibe-coding-and-agentic-engineering-are-getting-closer-.md; raw/2026-05-07-rss-dev-to-gamedev-how-i-knowing-only-if-vibecoded-civicsurvival-a-158k-li.md]

## Claims
- Fowler's May 5 fragment describes Rahul Garg's Lattice as an open-source framework/plugin that operationalizes AI-assisted programming patterns with composable skills (`atoms`, `molecules`, `refiners`) and a `.lattice/` living context layer for project standards, decisions, and review insights. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-martin-fowler-fragments-may-5.md]
- Jessica Kerr's conversation-log tooling example highlights a double feedback loop: developers change both the product being built and the tools/environment used to build it, making internal reprogrammability newly valuable with AI-speed iteration. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-martin-fowler-fragments-may-5.md]
- Willem van den Ende's local-model coding-agent setup argues that model quality is not the only axis; harness quality, skills, extensions, sandboxing, and local/open models may be good enough for daily work for some developers. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-martin-fowler-fragments-may-5.md]
- Fowler's May 5 fragment repeats the unresolved internal-quality question for agentic programming via Kent Beck's “Genie Tarpit”: AI tools can pile on complexity unless they preserve future-friendly design quality. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-martin-fowler-fragments-may-5.md]
- Prior Fowler/Thoughtworks fragments emphasize small changes, guardrails, documentation, tests/typecheckers/automated gates, security skepticism, and established engineering fundamentals as counterweights to AI speed. confidence: 5 sources, last-confirmed 2026-05-06. [sources: raw/2026-05-03-rss-martin-fowler-fragments-april-9.md; raw/2026-05-03-rss-martin-fowler-fragments-april-14.md; raw/2026-05-03-rss-martin-fowler-fragments-april-21.md; raw/2026-05-03-rss-martin-fowler-fragments-april-29.md; raw/2026-05-06-rss-martin-fowler-fragments-may-5.md]
- The Zig project has a strict anti-LLM contribution policy: no LLMs for issues, pull requests, or bug-tracker comments, including translation. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-simonwillison-zig-ai-contribution-policy.md]
- Simon Willison argues that vibe coding and responsible agentic engineering are blurring because agent reliability means even production code may no longer receive line-by-line human review; the goal should remain higher-quality production systems, not lower-quality output faster. confidence: 1 source, last-confirmed 2026-05-07. [source: raw/2026-05-07-rss-simon-willison-vibe-coding-and-agentic-engineering-are-getting-closer-.md]
- Willison says polished repos, readmes, commits, and comprehensive tests are no longer enough evidence of care because agents can generate them quickly; actual sustained use by the author or other users becomes more important provenance. confidence: 1 source, last-confirmed 2026-05-07. [source: raw/2026-05-07-rss-simon-willison-vibe-coding-and-agentic-engineering-are-getting-closer-.md]
- The CivicSurvival case study says large AI-assisted codebases need externalized memory and guardrails: project rules, RAG/navigation, custom analyzers, detailed logs, build gates, and structured audits. confidence: 1 source, last-confirmed 2026-05-07. [source: raw/2026-05-07-rss-dev-to-gamedev-how-i-knowing-only-if-vibecoded-civicsurvival-a-158k-li.md]
- CivicSurvival reports 158,583 C# lines, 31,219 TypeScript/React lines, 542 ECS systems, 369 UI components, 300+ custom Roslyn analyzers, 2,503 commits, and a custom MCP/RAG server over about three net months; treat as a self-reported case study, not an audited benchmark. confidence: 1 source, last-confirmed 2026-05-07. [source: raw/2026-05-07-rss-dev-to-gamedev-how-i-knowing-only-if-vibecoded-civicsurvival-a-158k-li.md]
- CivicSurvival's audit lesson is that “free prompt + narrow scope + correct context” found higher-yield bugs than repeated checklist prompts after known categories were exhausted, while repeated waves degraded into false positives and still could not replace live playtesting. confidence: 1 source, last-confirmed 2026-05-07. [source: raw/2026-05-07-rss-dev-to-gamedev-how-i-knowing-only-if-vibecoded-civicsurvival-a-158k-li.md]
- Google's production-agent refactor case study reinforces the same software-practice lesson from a different angle: monolithic scripts and prompt-enforced JSON should be replaced with orchestrated narrow agents, runtime schemas, dynamic RAG, traces, and framework-level retry/timeout controls. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-production-ready-ai-agents-5-lessons-from-refac.md]
- Anthropic's Opus 4.7 release claims better instruction following and literalness, which means older prompts/harnesses may need re-tuning rather than blind model substitution. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-web-anthropic-news-introducing-claude-opus-4-7.md]

## Typed entities
- person: Martin Fowler
- person: Simon Willison
- person: Rahul Garg
- person: Jessica Kerr / Jessitron
- person: Willem van den Ende
- person: Kent Beck
- project/framework: Lattice
- file/directory: `.lattice/`
- project: Zig
- project: Bun
- project/mod: CivicSurvival
- tool: Claude Code
- tool/protocol: MCP
- tool/system: CivicRAG
- analyzer type: Roslyn analyzer
- framework: Google Agent Development Kit (ADK)
- model: Claude Opus 4.7
- feature: structured outputs/Pydantic schemas
- standard/tooling: OpenTelemetry
- concept: AI-assisted coding
- concept: vibe coding
- concept: agentic engineering
- concept: agentic programming
- concept: internal reprogrammability
- concept: local/open models
- concept: coding-agent harness
- concept: externalized project memory
- concept: live usage provenance
- decision/policy: Zig anti-LLM contribution policy

## Explicit relationships
- AI-assisted coding depends-on verification gates to remain safe at higher throughput.
- Lattice uses composable skills and living project context to operationalize engineering standards for AI coding assistants.
- Local/open-model workflows depend-on harness quality, sandboxing, and custom extensions as much as raw model power.
- Internal reprogrammability is reinforced by AI-speed tooling changes because the development environment can be shaped alongside the product.
- Zig anti-LLM contribution policy contradicts the common default of accepting AI-assisted open-source submissions.
- Kent Beck's Genie Tarpit argument contradicts claims that internal quality no longer matters for agentic programming.
- vibe coding and agentic engineering converge when agent reliability reduces line-by-line human review, increasing the importance of gates, provenance, and operational use.
- CivicSurvival uses MCP/RAG, Roslyn analyzers, logs, and build gates to constrain AI-generated code.
- custom analyzers supersede recurring one-shot review findings by converting them into enforced build-time rules.
- AI audits depend-on narrow scope and evidence, but live gameplay/product testing supersedes static agent audits for experience quality.
- Prompt-only structure enforcement is superseded by runtime schemas where strict machine-readable outputs are needed.
- Model upgrades depend-on harness/prompt revalidation because stronger instruction following can change behavior.

## HoneyDrunk implications
- Keep AI coding workflows test-first and diff-small; the faster the agent, the more important the gate.
- Treat OpenClaw/Honeyclaw skills, repo instructions, and living context as first-class product surfaces; harness quality compounds.
- For any large HoneyDrunk AI-coded system, convert repeated mistakes into analyzers or automated checks instead of hoping agents remember.
- Treat “has this been used hard for days/weeks?” as a stronger trust signal than repo polish when evaluating AI-built tools.
- Explore local/open model paths for privacy-sensitive or cost-sensitive workflows, but keep sandbox/zero-trust controls regardless of model location.
- When contributing upstream, check project AI policies before using LLM-generated text or code.
- Treat model upgrades like dependency upgrades: run representative tasks, measure token/cost shifts, and adjust prompts before changing defaults.

## Confidence and quality notes
- Quality posture: decision-usable for team practice; source set is commentary-heavy and case-study-heavy, not controlled empirical measurement.
- Contradictions: Zig policy is captured as a differing governance stance, not a universal rule; local-model “good enough” is one practitioner report, not a broad benchmark.
- Weak claims: CivicSurvival metrics and audit yields are self-reported and should be treated as pattern evidence, not performance guarantees.
- Privacy filter: no private details copied; public author names and project/tool names retained.

## 2026-05-18 compile additions

### Claims
- Unmesh Joshi argues that in the LLM era the durable value of code shifts toward code as shared conceptual model and vocabulary: types, interfaces, invariants, workflows, and naming encode domain understanding for humans and LLMs. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-martin-fowler-what-is-code.md]
- Joshi names “cognitive debt” as the risk that LLMs introduce plausible vocabulary, abstractions, and structures faster than a team builds shared understanding. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-martin-fowler-what-is-code.md]
- Fowler's May 14 fragment says LLM-assisted legacy lift-and-shift may now be cheaper as a first migration step, but should not be the endpoint; teams still need user/business-outcome review after the mechanical port. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-martin-fowler-fragments-may-14.md]
- Fowler's May 14 fragment reinforces that junior-developer judgment transfer needs pairing and human review; fully automated spec/code review can block the learning that SPDD is meant to preserve. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-martin-fowler-fragments-may-14.md]
- James Pritchard's quoted position is that many product “agents” should instead be deterministic workflows with LLM function calls because known execution paths are easier to compose, debug, fail, and cost-control than autonomous conversations. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-martin-fowler-fragments-may-14.md]
- Pritchard also warns that markdown skills are often overused where architecture, clean code patterns, tests, hooks, and computational harness pieces would be more reliable. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-martin-fowler-fragments-may-14.md]

### Typed entities
- person: Unmesh Joshi
- person: James Pritchard
- person: Martin Fowler
- concept: code as shared conceptual model
- concept: cognitive debt
- concept: bounded context
- concept: ubiquitous language
- concept: lift-and-shift legacy migration
- concept: interrogatory LLM
- concept: Structured-Prompt-Driven Development / SPDD
- concept: skills overuse
- decision: prefer deterministic LLM function/workflow over runtime agent when path is known

### Explicit relationships
- Code vocabulary uses domain concepts, technical framework concepts, types, interfaces, invariants, and tests as LLM-readable harness/context.
- Cognitive debt is caused when LLM-generated abstractions outpace team understanding.
- Strong code structure supersedes prompt-only context as the primary harness for reliable coding agents.
- LLM-assisted lift-and-shift supersedes prior cost assumptions for some legacy migrations, but depends-on post-port simplification and business-outcome review.
- Deterministic workflows supersede autonomous agents when the workflow path is known.
- Pair programming uses expert/junior collaboration to transfer agentic-programming judgment.

## 2026-05-21 compile additions

### Claims
- Thoughtworks' maintainability-sensor experiment defines maintainability as making code easy and low-risk to change over time, and identifies early AI-codebase warning signs such as small adjustments touching too many files or breaking previously working behavior. confidence: 1 source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-martin-fowler-maintainability-sensors-for-coding-agents.md]
- Basic lint rules that target common AI shortcomings include maximum argument count, file length, function length, and cyclomatic complexity; the author notes these often require explicit configuration rather than relying on default ESLint presets. confidence: 1 source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-martin-fowler-maintainability-sensors-for-coding-agents.md]
- Custom lint/dependency messages can act as self-correction guidance: the sensor should explain the architectural intent and when exceptions are acceptable, not merely report a violation. confidence: 1 source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-martin-fowler-maintainability-sensors-for-coding-agents.md]
- Dependency-cruiser-style rules can enforce layer boundaries and folder structure, but import/path rules cannot fully evaluate semantic modularity. confidence: 1 source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-martin-fowler-maintainability-sensors-for-coding-agents.md]
- Raw coupling metrics alone produced noisy AI conclusions because legitimate hubs such as factories or shared schema contracts can look like high-coupling problems without domain context; coupling data is more useful for review risk triage than as standalone design authority. confidence: 1 source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-martin-fowler-maintainability-sensors-for-coding-agents.md]
- Inferential modularity reviews using strong design prompts surfaced semantic issues missed by computational sensors, including duplicate route logic, inconsistent backend-calling patterns, repeated request parameters across layers, and responsibilities hidden in surprising places. confidence: 1 source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-martin-fowler-maintainability-sensors-for-coding-agents.md]

### Typed entities
- person: Birgitta Böckeler
- organization: Thoughtworks
- tool: ESLint
- tool: Semgrep
- tool: dependency-cruiser
- tool: GitLeaks
- tool: coupling-analyser
- concept: maintainability sensor
- concept: AI modularity review
- concept: computational sensor
- concept: inferential sensor
- concept: self-correction guidance

### Explicit relationships
- Maintainability sensors use automated and inferential feedback to reduce AI-generated technical debt before human review.
- Custom lint guidance supersedes generic tool output when the goal is agent self-correction.
- Dependency rules depend-on expressible import/folder boundaries and cannot supersede semantic modularity review.
- Coupling metrics depend-on domain interpretation; legitimate architectural hubs can contradict naive “god module” findings.
- AI modularity reviews complement computational sensors by reading code semantics and tradeoffs.

### HoneyDrunk implications
- Promote recurring AI-review findings into analyzers, lint rules, dependency rules, or focused modularity-review prompts.
- Start with cheap computational gates for known AI failure modes, but reserve semantic LLM review for changed-file modularity and responsibility placement.
- Treat agent-created suppressions and threshold increases as review hotspots, not hidden debt.

## 2026-05-23 compile additions

### Claims
- Fowler's formal definition keeps “vibe coding” narrow: prompting an LLM to build/change an application while deliberately not reading the generated code; he distinguishes this from agentic programming, where developers still care about and review internal code structure. confidence: 1 source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-martin-fowler-bliki-vibe-coding.md]
- Fowler says vibe coding is best suited to disposable software, personal tools, prototypes, or limited-audience apps; broader or sensitive use raises maintainability, correctness, and security risks because the code is not inspected. confidence: 1 source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-martin-fowler-bliki-vibe-coding.md]
- Architecture Notes' “Enforce” roundup reinforces a verification gap: LLM-generated code can compile and pass tests while missing performance-critical invariants, citing a reported SQLite-vs-LLM Rust rewrite lookup gap of 0.09 ms versus 1,815.43 ms. Treat as secondary roundup evidence until the benchmark source is checked. confidence: 1 roundup source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-architecture-notes-arc-notes-weekly-105-enforce.md]

### Typed entities
- person: Martin Fowler
- person: Andrej Karpathy
- concept: vibe coding
- concept: agentic programming
- concept: verification gap
- concept: disposable software
- database: SQLite
- language: Rust

### Explicit relationships
- vibe coding contradicts agentic programming when the human stops inspecting code structure.
- Vibe-coded software depends-on limited scope and low blast radius because maintainability/correctness/security evidence is weak.
- Verification gates supersede “passes tests” as trust evidence when generated code might miss system invariants.

### HoneyDrunk implications
- Use vibe coding freely for throwaway internal prototypes, but require agentic-programming discipline for anything connected to credentials, users, data, revenue, or production workflows.
- Add performance and invariant checks to AI-code review where correctness tests alone can pass.

## 2026-05-30 compile additions

### Claims
- Fowler's May 27 fragment summarizes Ian Johnson's AI-assisted codebase restructuring: after adding characterization tests, static analysis, and architectural patterns, the human role could move from micromanaged in-the-loop review toward on-the-loop curation because gates forced better agent behavior. confidence: 1 Fowler fragment source summarizing a practitioner series, last-confirmed 2026-05-30. [source: raw/2026-05-30-rss-martin-fowler-fragments-may-27.md]
- The same fragment cites Adam Tornhill's cognitive-endurance warning: agentic coding increases decision density, so even productive agent use can be mentally expensive and should be scoped around small tasks, automation, and verification mechanisms. confidence: 1 Fowler fragment source, last-confirmed 2026-05-30. [source: raw/2026-05-30-rss-martin-fowler-fragments-may-27.md]
- Fowler's fragment argues public-to-private source closure is not an effective substitute for secure-by-design delivery, ownership, and remediation against LLM-augmented attackers. confidence: 1 Fowler fragment source citing UK GDS position, last-confirmed 2026-05-30. [source: raw/2026-05-30-rss-martin-fowler-fragments-may-27.md]
- GitHub Copilot guidance for .NET reinforces task-first delegation: chat for understanding/planning, agentic workflows for bounded change-and-verify tasks, and careful review of resulting diffs. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-rss-net-blog-doing-more-with-github-copilot-as-a-net-developer.md]

### Typed entities
- person: Martin Fowler
- person: Kent Beck
- person: Ian Johnson
- person: Adam Tornhill
- organization: UK Government Digital Service / GDS
- concept: on-the-loop human-AI collaboration
- concept: in-the-loop human-AI collaboration
- concept: characterization tests
- concept: cognitive endurance
- product: GitHub Copilot

### Explicit relationships
- Automated quality gates enable on-the-loop agent supervision by forcing behavior before human review.
- Cognitive endurance limits contradict hype around human attention over many parallel agent streams.
- Secure-by-design remediation supersedes repository closure as a response to LLM-augmented security risk.
- Copilot agentic workflows depend-on bounded tasks and reviewable diffs.

### HoneyDrunk implications
- Increase agent autonomy only where tests, static analysis, logs, and architectural rules can constrain it.
- Avoid workflows that force Oleg/Honeyclaw to context-switch across many high-stakes agent threads at once; machine parallelism is different from human attention parallelism.
- Keep source-security policy grounded in real controls, not obscurity.

## 2026-05-31 compile additions

### Claims
- Thoughtworks' VibeSec Reckoning reports two AI-assisted prototype near misses: public storage recommendations for sensitive assets and excessive service-account token permissions; both were caught by humans asking security questions. confidence: 1 Thoughtworks/Fowler source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-martin-fowler-the-vibesec-reckoning.md]
- The source argues "be secure" prompting is not equivalent to enforcement: non-negotiable rules must be codified in the development lifecycle through context files, secure templates, scanners, pre-commit/build gates, and review. confidence: 1 Thoughtworks/Fowler source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-martin-fowler-the-vibesec-reckoning.md]
- The article maps harness controls to guides/sensors and computational/inferential controls: context rules can steer the model, while linters, tests, SAST, credential scanning, infrastructure validation, dependency checks, and security review validate outputs. confidence: 1 Thoughtworks/Fowler source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-martin-fowler-the-vibesec-reckoning.md]
- The article recommends daily security intelligence feeds for CVEs, platform advisories, and AI coding tool issues so vulnerabilities are noticed near disclosure time. confidence: 1 Thoughtworks/Fowler source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-martin-fowler-the-vibesec-reckoning.md]
- OpenAI's Tax AI case study reinforces agentic software practice by turning production evidence into scoped engineering tasks: practitioner corrections are captured, grouped, converted into eval targets, and then given to Codex with traces, repo context, skills, docs, targeted evals, and regression suites. confidence: 1 official/vendor-partner source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-openai-via-tldr-ai-building-self-improving-tax-agents-with-codex.md]

### Typed entities
- concept: VibeSec
- organization: Thoughtworks
- concept: security context file
- concept: daily security intelligence feed
- control: SAST scanning
- control: credential scanning
- control: infrastructure validation
- control: secure-by-default template
- product/system: Tax AI
- product/tool: Codex
- concept: production trace
- concept: targeted eval

### Explicit relationships
- Security context files guide AI-assisted coding but depend-on computational sensors for enforcement.
- Secure-by-default templates reduce the chance that nontechnical builders accept insecure AI suggestions under deadline pressure.
- Production traces and practitioner corrections cause targeted evals, which enable scoped AI-assisted product improvements.
- Human review complements Codex-generated fixes because ambiguous corrections can reflect workflow noise or product judgment rather than a code defect.

### HoneyDrunk implications
- Create HoneyDrunk security rules as both agent context and executable gates; do not stop at markdown.
- If business/non-engineering prototypes become durable tools, require the same storage, IAM, secrets, dependency, and review gates as engineering-owned apps.
- Build improvement loops around evidence bundles: trace, expected output, actual output, source artifacts, scoped code surface, eval command, and regression suite.

## 2026-06-01 compile additions

### Claims
- Stephen Toub's dotnet/runtime report says Copilot Coding Agent created 878 PRs from 2025-05-19 through 2026-03-22, with 535 merged, 253 closed, 90 open, and a 67.9% success rate under explicit maintainer assignment; the report cautions that CCA tasks are not comparable to human PR populations. confidence: 1 Microsoft/.NET source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ten-months-with-copilot-coding-agent-in-dotnet-runtime.md]
- The same report identifies sweet spots for cloud coding agents: mechanical cleanup/removal, test additions, refactoring, and clearly described bug fixes; it flags harder areas such as native/cross-platform code, architecture-heavy work, and tests that accidentally encode existing incorrect behavior. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ten-months-with-copilot-coding-agent-in-dotnet-runtime.md]
- Warne's Claude Code reflection says AI coding shifts developer time away from typing boilerplate and toward understanding, review, testing, exploratory checks, and codebase learning; it explicitly rejects treating AI as an excuse not to understand the system. confidence: 1 practitioner source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-with-claude-less-coding-more-testing.md]
- System Design Newsletter's agent-use article frames agent delegation risk around four factors: how fast mistakes are discovered, how easy answers are to check, how much can break, and whether the result can be undone. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-how-to-get-ahead-of-99-of-software-engineers-with-ai-agents.md]

### Typed entities
- product: GitHub Copilot Coding Agent / CCA
- repository: dotnet/runtime
- product: Claude Code
- concept: task reversibility
- concept: reviewable diff
- concept: exploratory testing
- concept: AI-generated tests

### Explicit relationships
- Coding-agent success depends-on task shape, available verification, repository instructions, and human review.
- Mechanical cleanup and scoped refactoring complement cloud coding agents because success criteria are easier to search, test, and review.
- Human understanding supersedes agent output when the developer is accountable for the change.
- Agent autonomy contradicts high-blast-radius work when feedback is slow, evidence is ambiguous, or rollback is difficult.

### HoneyDrunk implications
- Prefer assigning agents small reversible tasks with clear issue descriptions, tests to run, and reviewable diffs.
- Review AI-generated tests for behavior validity; do not let agents freeze existing bugs as expected behavior.
- Keep incident diagnosis and product/architecture judgment human-owned even when agents gather evidence quickly.

## 2026-06-02 compile additions

### Claims
- Sean Goedecke's agent-vs-pipeline essay says pipelines are better when context size, GPU cost, or local-model constraints must be tightly bounded; agents are better when context gathering is uncertain, the task needs action/reaction loops, or the problem is hard enough that one-shot context assembly is unlikely to work. confidence: 1 practitioner source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-sean-goedecke-build-agents-not-pipelines.md]
- The same essay argues prompt injection and unsafe action risks exist in both pipelines and agents whenever untrusted human-generated data is fed to an LLM; tool/action constraints and human approval remain necessary in either design. confidence: 1 practitioner source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-sean-goedecke-build-agents-not-pipelines.md]
- Simon Willison's Pasted File Editor prototype was built with Codex desktop and implements a UI pattern similar to Claude's large-paste attachment behavior: long pasted text becomes an attachment instead of replacing/editor-polluting the active text area. confidence: 1 practitioner source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-simon-willison-pasted-file-editor.md]
- GameMaker's GMRT/GM-CLI release includes Claude Code in the new command-line toolchain so developers can inspect project structure, debug, manage build configuration, and use natural-language terminal workflows; GameMaker frames AI use as optional and complementary, with CLI/API/MCP/GitHub Actions surfaces available without embedded GameMaker-run AI servers. confidence: 1 Game Developer trade-press source quoting GameMaker, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-game-developer-gamemaker-incorporates-claude-code-to-enable-ai-assiste.md]

### Typed entities
- concept: pipeline
- concept: agent
- concept: prompt injection
- tool/prototype: Pasted File Editor
- product: Codex desktop
- product/tool: GameMaker GMRT
- tool: GM-CLI
- product: Claude Code
- protocol: MCP Server
- platform: GitHub Actions

### Explicit relationships
- Pipeline design uses coded control flow; agent design delegates control flow to the model plus tools.
- Action safety depends-on constrained tools and approval gates in both pipeline and agent designs.
- Attachment-aware paste handling reduces context pollution in AI-assisted editing.
- GameMaker's Claude Code integration depends-on CLI/API/MCP surfaces rather than an embedded always-on AI server.

### HoneyDrunk implications
- Pick agents only when the task shape needs iterative context discovery or action feedback; use pipelines for bounded bulk processing and local-model constraints.
- Build prompt/file UI that separates instructions from source attachments so users can inspect and remove large context chunks deliberately.
- Treat game-engine CLI/MCP integration as the enabling layer for AI-assisted workflows; do not bind the studio to an IDE-only AI path.
