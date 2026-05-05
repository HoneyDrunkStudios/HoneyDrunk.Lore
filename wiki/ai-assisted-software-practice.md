# AI-Assisted Software Practice

## Decision-useful summary
The strongest practical signal is conservative: AI increases throughput, but teams need smaller changes, guardrails, ruthless documentation, automated verification, and security skepticism. Fowler/Thoughtworks materials frame AI as a forcing function to revisit fundamentals rather than abandon them. Zig's anti-LLM contribution policy is a useful counterexample: open-source projects may reject AI-generated issues/PRs/comments for review-quality and trust reasons. [sources: raw/2026-05-03-rss-martin-fowler-fragments-april-9.md; raw/2026-05-03-rss-martin-fowler-fragments-april-14.md; raw/2026-05-03-rss-martin-fowler-fragments-april-21.md; raw/2026-05-03-rss-martin-fowler-fragments-april-29.md; raw/2026-05-03-rss-simonwillison-zig-ai-contribution-policy.md]

## Claims
- Martin Fowler highlighted AI-native software work as comparable to earlier industry shifts and connected it to agile/TDD, unhealthy metrics, and developer adaptation. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-martin-fowler-fragments-april-14.md]
- Thoughtworks Technology Radar volume 34 was described as AI-dominated, but with renewed emphasis on pair programming, zero-trust architecture, mutation testing, DORA metrics, clean code, deliberate design, testability, and accessibility. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-martin-fowler-fragments-april-21.md]
- Fowler's April 29 fragment summarizes AI-coding guidance: keep changes small, build guardrails, document ruthlessly, and verify with tests/typecheckers/automated gates or human judgment where it matters. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-martin-fowler-fragments-april-29.md]
- Fowler's April 9 fragment foregrounds Simon Willison's concern that AI-assisted programming contains a security risk that teams must actively manage. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-martin-fowler-fragments-april-9.md]
- The Zig project has a strict anti-LLM contribution policy: no LLMs for issues, pull requests, or bug-tracker comments, including translation. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-simonwillison-zig-ai-contribution-policy.md]

## Typed entities
- person: Martin Fowler
- person: Simon Willison
- person: Chris Parsons
- organization/project: Thoughtworks Technology Radar
- project: Zig
- project: Bun
- concept: AI-assisted coding
- concept: TDD
- concept: DORA metrics
- concept: zero-trust architecture
- decision/policy: Zig anti-LLM contribution policy

## Explicit relationships
- AI-assisted coding depends-on verification gates to remain safe at higher throughput.
- Thoughtworks Technology Radar reinforces established engineering practices as counterweights to AI speed.
- Zig anti-LLM contribution policy contradicts the common default of accepting AI-assisted open-source submissions.
- Bun uses AI assistance internally but depends-on a Zig fork partly because upstream Zig policy rejects LLM-aided contributions.

## HoneyDrunk implications
- Keep AI coding workflows test-first and diff-small; the faster the agent, the more important the gate.
- When contributing upstream, check project AI policies before using LLM-generated text or code.

## Confidence and quality notes
- Quality posture: decision-usable for team practice; source set is commentary-heavy, not empirical measurement.
- Contradictions: no contradiction to resolve; Zig policy is captured as a differing governance stance, not a universal rule.
- Privacy filter: no private details copied.
