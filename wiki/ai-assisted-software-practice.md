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
