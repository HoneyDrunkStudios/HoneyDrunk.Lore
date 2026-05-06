# AI-Assisted Software Practice

## Decision-useful summary
The strongest practical signal is conservative: AI increases throughput, but teams need smaller changes, guardrails, ruthless documentation, automated verification, security skepticism, and explicit harness/context design. Fowler/Thoughtworks materials frame AI as a forcing function to revisit fundamentals rather than abandon them. The May 5 Fowler fragment adds durable signals: Lattice-style composable skills and living project context, the double feedback loop of adapting both product and dev environment, and local/open models becoming good-enough for some coding-agent workflows when paired with high-quality harnesses and sandboxing. Zig's anti-LLM contribution policy is a useful counterexample: open-source projects may reject AI-generated issues/PRs/comments for review-quality and trust reasons. [sources: raw/2026-05-03-rss-martin-fowler-fragments-april-9.md; raw/2026-05-03-rss-martin-fowler-fragments-april-14.md; raw/2026-05-03-rss-martin-fowler-fragments-april-21.md; raw/2026-05-03-rss-martin-fowler-fragments-april-29.md; raw/2026-05-06-rss-martin-fowler-fragments-may-5.md; raw/2026-05-03-rss-simonwillison-zig-ai-contribution-policy.md]

## Claims
- Fowler's May 5 fragment describes Rahul Garg's Lattice as an open-source framework/plugin that operationalizes AI-assisted programming patterns with composable skills (`atoms`, `molecules`, `refiners`) and a `.lattice/` living context layer for project standards, decisions, and review insights. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-martin-fowler-fragments-may-5.md]
- Jessica Kerr's conversation-log tooling example highlights a double feedback loop: developers change both the product being built and the tools/environment used to build it, making internal reprogrammability newly valuable with AI-speed iteration. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-martin-fowler-fragments-may-5.md]
- Willem van den Ende's local-model coding-agent setup argues that model quality is not the only axis; harness quality, skills, extensions, sandboxing, and local/open models may be good enough for daily work for some developers. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-martin-fowler-fragments-may-5.md]
- Fowler's May 5 fragment repeats the unresolved internal-quality question for agentic programming via Kent Beck's “Genie Tarpit”: AI tools can pile on complexity unless they preserve future-friendly design quality. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-martin-fowler-fragments-may-5.md]
- Prior Fowler/Thoughtworks fragments emphasize small changes, guardrails, documentation, tests/typecheckers/automated gates, security skepticism, and established engineering fundamentals as counterweights to AI speed. confidence: 5 sources, last-confirmed 2026-05-06. [sources: raw/2026-05-03-rss-martin-fowler-fragments-april-9.md; raw/2026-05-03-rss-martin-fowler-fragments-april-14.md; raw/2026-05-03-rss-martin-fowler-fragments-april-21.md; raw/2026-05-03-rss-martin-fowler-fragments-april-29.md; raw/2026-05-06-rss-martin-fowler-fragments-may-5.md]
- The Zig project has a strict anti-LLM contribution policy: no LLMs for issues, pull requests, or bug-tracker comments, including translation. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-simonwillison-zig-ai-contribution-policy.md]

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
- concept: AI-assisted coding
- concept: agentic programming
- concept: internal reprogrammability
- concept: local/open models
- concept: coding-agent harness
- concept: zero-trust architecture
- decision/policy: Zig anti-LLM contribution policy

## Explicit relationships
- AI-assisted coding depends-on verification gates to remain safe at higher throughput.
- Lattice uses composable skills and living project context to operationalize engineering standards for AI coding assistants.
- Local/open-model workflows depend-on harness quality, sandboxing, and custom extensions as much as raw model power.
- Internal reprogrammability is reinforced by AI-speed tooling changes because the development environment can be shaped alongside the product.
- Zig anti-LLM contribution policy contradicts the common default of accepting AI-assisted open-source submissions.
- Kent Beck's Genie Tarpit argument contradicts claims that internal quality no longer matters for agentic programming.

## HoneyDrunk implications
- Keep AI coding workflows test-first and diff-small; the faster the agent, the more important the gate.
- Treat OpenClaw/Honeyclaw skills, repo instructions, and living context as first-class product surfaces; harness quality compounds.
- Explore local/open model paths for privacy-sensitive or cost-sensitive workflows, but keep sandbox/zero-trust controls regardless of model location.
- When contributing upstream, check project AI policies before using LLM-generated text or code.

## Confidence and quality notes
- Quality posture: decision-usable for team practice; source set is commentary-heavy, not empirical measurement.
- Contradictions: Zig policy is captured as a differing governance stance, not a universal rule; local-model “good enough” is one practitioner report, not a broad benchmark.
- Privacy filter: no private details copied; defamatory allegation example from the source is summarized only at high level here and not recorded as a claim about the individual.
