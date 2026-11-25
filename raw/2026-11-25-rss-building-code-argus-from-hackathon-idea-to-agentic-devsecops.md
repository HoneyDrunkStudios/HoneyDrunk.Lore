---
source: "https://www.thoughtworks.com/insights/blog/generative-ai/building-code-argus-hackathon-to-agentic-devsecops"
title: "Building Code Argus: From hackathon idea to agentic DevSecOps"
author: "Sarath Kumar; Divyansha Jain; Surya Borusu"
date_published: "2026-11-25"
date_clipped: "2026-11-25"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Building Code Argus: From hackathon idea to agentic DevSecOps

*Developed during AI/works™ Innovation Hackathon (2026), Code Argus is an experiment in making DevSecOps workflows more intelligent, connected and reliable. We spoke to the three-person team behind it about what they built, the challenges they encountered and what they learned.*

### Tell us about the challenges you were facing. What had you noticed? What were you experiencing?

We kept hitting the same three recurring DevSecOps time-sinks. First, production incidents: an alert fires, an engineer gets woken up and the first hour is spent re-deriving context that already exists buried in logs, stack traces and code. Second, inconsistent reviews: engineering standards (SOLID, test coverage, security baselines) get applied unevenly across hundreds of PRs a week, depending on who happens to review. Third, silent technical debt: memory leaks, dead code and vulnerable dependencies accumulate for weeks before anyone notices.

The tools we already had, such as SonarQube, Snyk and GitHub Copilot each solve a slice, but none of them reason across code, tickets, runtime signals and engineering standards as one connected workflow. SonarQube finds the issue, Copilot writes the line, but nothing connects an alert to the responsible code path, to its blast radius, to the team's own standards and to a safe, tested fix. All the context an engineer needs exists; it's just scattered across five different tools. Closing that gap is what Code Argus is built for.

How did you arrive at your solution? Were there any other tools or products that you looked to for inspiration?

CI tools already detect issues correctly, so reasoning is the bottleneck. What's missing is the layer that connects a finding to the code, its blast radius, the project's standards and a validated fix. So we made a deep code knowledge base the core differentiator and kept the agent layer thin and deliberate.

For inspiration, we drew on Anthropic's "Building effective agents" (small, composable agents over a controllable state graph: why we picked LangGraph over chattier frameworks like CrewAI/AutoGen), Microsoft AutoGen's multi-agent patterns, Sourcegraph Cody's write-ups on hybrid code retrieval and Neo4j's GraphRAG work. GitHub Copilot Autofix/Workspace was a positioning reference: those are PR-scoped assistants, whereas we wanted something that lives inside the pipeline itself, a container invoked as a GitHub Action, inheriting the sandbox, ephemeral credentials and toolchain CI already provides, with zero idle cost and a one-line adoption story.

We also arrived at the current shape by iterating: we replaced Qdrant with pgvector (one less service, same quality at our scale), and after feedback from the Hackathon judges at the end of Round 1, we added a skill layer: versioned per-flow playbooks with least-privilege tool access. We deliberately rejected the Claude Agent SDK so that we could stay provider-agnostic via LiteLLM.

Were there any particularly challenging parts of the process? Any failures or errors that you had to overcome?

Plenty, but a few stand out because of what they taught us:

**Silent data loss in the graph:**Our TypeScript cross-file CALLS edges were being silently dropped. When a caller's file was indexed before the callee's, the Cypher MATCH found no node and the edge just vanished. The fix was two-pass indexing: upsert all symbols first, edges second, plus filtering external library calls so the graph stays clean.

** **

**A hard runtime failure in embeddings:**Our original model (jina-embeddings-v2-base-code) used HuggingFace custom code that imports a function removed in transformers 5.x. This was a crash, not a preference, so we switched to BAAI/bge-base-en-v1.5 (same 768 dimensions, Apache-2.0, no remote code).

**Hallucinated fixes from thin evidence:**An early demo fed the Fix agent a fictional stack trace, and it dutifully invented an entire payment_gateway.py out of nothing. The lesson that evidence must be real led us to plant a genuine bug instead (a one-token change that keeps all 932 tests green, exactly the kind of defect that walks past CI into production).

**Gates that always said green:**An internal review found our test/scan gates were stubs, and routing never inspected results. We wired the real runners and moved deterministic gates ahead of the Critic LLM call, so a red build loops back to Fix without spending tokens.

**Going cross-vendor for the Critic:**Our first Gemini model string returned a real Google 404 ("no longer available to new users"), and the next hit free-tier rate limits. We settled on Google's gemini-flash-latest alias after live verification.

Each failure ended up strengthening a design principle: real evidence, computed (not asserted) safety claims and deterministic code where determinism matters.

Explain the importance of the knowledge base. Why Neo4j? And how does it work?

The knowledge base is the differentiator. It lets the agents reason about your code instead of guessing. It answers four questions with provenance: structurally ("who calls this function?", which gives the blast radius), semantically ("which code looks like this stack trace?"), from memory ("have we seen this incident before, and how was it fixed?") and from governance ("which of our standards apply here?"). Every retrieved chunk carries its file, line range, relevance score and why it was surfaced, so agents cite evidence rather than assert guesses.

**Why Neo4j:** the questions that matter most are relationship questions. "What breaks if I change this function?" is a graph traversal: match all callers of this symbol and their callers' context. Vector search is great at finding similar text, but it can't reliably enumerate every caller of a function; a graph does that exactly, and Neo4j gives us mature, expressive Cypher pattern matching, variable-length traversals and a clear ops path (self-hosted in Docker Compose today, managed tiers later, with Memgraph noted as a drop-in alternative for license-sensitive organizations).

**How it works: **Tree-sitter parses Python and TypeScript into symbols, call edges and import edges. A two-pass indexer upserts symbols into Neo4j first, then resolves edges against the whole-repo symbol map (dropping external library calls so the graph stays clean), and simultaneously embeds each symbol's source (768-dim vectors) into Postgres/pgvector. One component, the Code Analyst, is the single door: agents send a typed query, and it routes to graph, vector or both (hybrid), merges and deduplicates, and returns one structured RetrievalResult with chunks, blast radius, past incidents and a standards excerpt. No agent touches the databases directly, which also means the storage backends can change without touching a single agent.

You describe it as deterministic by design. Can you explain how you made things deterministic and why this is important?

The principle is that the LLM proposes and deterministic code disposes. An LLM call is spent only where genuine reasoning is required.

Concretely: the orchestrator is pure code, not an LLM. It routes by inspecting typed state (tests green? scan safe? iterations under the bound?) and makes zero LLM calls. The hero flow has exactly four LLM calls (Triage diagnoses, Fix proposes a patch, Critic reviews it on a different model, Reviewer writes the PR body). Everything else is deterministic: git operations, build/test/scan execution, event routing (GitHub's event types select the scenario, with no classifier model), dedup, prioritization and story selection. The safety gates run before the Critic. A failing test or an unsafe scan delta loops straight back to Fix without spending an LLM call, and the fix loop is bounded (at most three iterations, then it defers to a Jira story instead of opening a broken PR). No new vulnerabilities" is computed, not asserted: a delta SARIF (baseline vs post-fix scan) proves it.

Why it matters: every LLM call adds cost, latency and a failure surface. Deterministic code is reproducible, auditable and testable. For a system that opens pull requests on real codebases, predictability is the trust story. It's also the cost story: a full incident-to-PR run lands around $0.12 because the expensive model is only touched for reasoning, never for mechanics.

Does working with Code Argus change how you work? Are there any technical overheads or other risks that you had to be aware of?

Does working with Code Argus change how you work? Are there any technical overheads or other risks that you had to be aware of?

It changes the shape of the work: engineers approve instead of debug. The 3am incident becomes a morning PR review, with the full reasoning trace (every LLM call, tool call and token cost visible in Langfuse) attached. And incident knowledge compounds: every diagnosis and resolution is stored as a past incident, so the context leaves the run, not the on-call.

The overheads are real but bounded: adopting repos declare a small .argus/ contract (config for build/test/scan commands and a standards.md ruleset, the one setup step); you operate a small persistent tier (Neo4j and Postgres), which is why incremental indexing matters (a one-line change shouldn't cost a 30-minute re-index); each fix pays a double build/test (inner gate and outer CI gate, accepted as defense-in-depth); and LLM spend per run is capped by a budget.

The risks are the reasons for several design choices. Hallucinated fixes that pass tests: mitigated by an independent Critic on a different vendor's model, the delta-SARIF proof, a bounded loop and mandatory human merge. Prompt injection from external text: inputs are scanned, and the PR Reviewer's dynamic tool loop is injection-guarded. PII leakage: Presidio redaction on runtime/log data entering prompts (source stays intact; an agent can't reason over a censored diff). Over-privileged agents: least privilege is enforced in code. The toolset handed to each role physically cannot call what its role doesn't allow (Triage can't patch; the Reviewer can't push). And duplicate outputs on retries: idempotent branch/PR/Jira operations plus advisory locks. We also dogfood it: it has opened real PRs on our own repository, which keeps the risk conversation honest.

How did you decide on the scope of the project (i.e., what it would and wouldn’t do)?

The governing principle was "defer scope, never fake substance": a feature that isn't built is honestly absent (an explicit NotImplementedError, or simply not wired), never a facade that looks done. That's enforced by a repo check that bans fakes and stubs from production code, and it's what let us build in parallel as a three-person team without anyone shipping a stage-prop the others would build on.

The hackathon had two judged rounds. In Round 1, teams submitted their idea along with an architecture and a demo video. In Round 2, the shortlisted teams got judges’ feedback and then built out their projects. For Round 1 we deliberately scoped a single hero flow, production triage-to-PR, and built it end to end. The other flows existed only on the architecture diagram, because one flow that works flawlessly beats four that half-work. In Round 2 those flows were built, one per workstream, and each had an explicit LLM-call budget: the LLM is used only for reasoning, while detection, routing and dedup stay deterministic.

The "wouldn't do" list was as deliberate as the features: no hosted service (the pipeline is the runtime); the LLM never executes git or scan operations: it emits artifacts and deterministic helpers execute them; agents never merge (a human is in the loop by design); scheduled scans file deduplicated Jira stories rather than opening unsolicited PRs (a human labels a story Ready-for-build, and only then does the autonomous flow fix it; unsolicited PRs are a higher-risk default than tickets); Python and TypeScript only, documented as a known limitation. Scope could also widen with evidence: the scheduled scan originally budgeted one LLM call, and building it revealed that a scan which only relays other tools' findings does zero reasoning of its own, so we added a standards-judge call, a deliberate, logged widening rather than scope creep.

**What’s next for the project?**

The main direction is making the knowledge base three-dimensional: today, runtime signals (Datadog/CloudWatch/Sentry metrics like memory, CPU, error rates) only trigger triage after something breaks. The plan is to ingest them into the KB as a third retrieval dimension alongside graph and vector, so a scheduled run can correlate "memory spike in order_service" with "which functions in create_order hold long-lived references?" and propose a proactive fix before an alert ever fires.

Near term, closing the autonomy loop: when PR review flags findings on a PR the autonomous flow itself opened, have the flow read that feedback and run another bounded fix attempt before surfacing to a human, so that Review → AutoDev-fixes-comments → re-review runs as one unit.

Beyond that: cross-repo reasoning (SCIP edges over the shared, repo-partitioned graph, the org-scale differentiator, so a change in one service can show its blast radius in its callers in another repo); more languages, which the parser protocol makes a one-line registration (Go and Java are the natural next); auto-detecting build/test commands so .argus/ onboarding shrinks further; and continued hardening: expanding the retrieval-quality eval harness, fingerprint stability across large line shifts and per-ecosystem dependency evidence beyond Python. The architecture was built so each of these lands behind an existing seam (the Code Analyst interface, the parser protocol, the skill layer) rather than requiring a redesign.

* *

* *

*Code Argus is still evolving, with plans to extend its knowledge base to runtime signals and support reasoning across repositories. The project offers an interesting look at how agentic AI can work within existing engineering workflows while keeping humans in control.*

Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.
