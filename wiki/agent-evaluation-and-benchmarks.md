# Agent Evaluation and Benchmarks

## Decision-useful summary
Agent evaluations are no longer just model prompt tests. Current sources emphasize that the harness, tools, budget, retries, state management, scoring, and validity checks materially shape measured capability and safety. ITBench-AA adds a concrete enterprise-SRE benchmark where frontier models remain below 50%, while OpenAI's third-party evaluation playbook says reports must state the claim being tested, the harness/budget used, and checks for reward hacking, refusals, contamination, broken tasks, and sandbagging. [sources: raw/2026-05-31-rss-hugging-face-blog-itbench-aa-frontier-models-score-below-50-on-the-fir.md; raw/2026-05-31-web-openai-a-shared-playbook-for-trustworthy-third-party-evaluations.md]

## Claims
- ITBench-AA SRE evaluates agentic enterprise IT incident response over 59 Kubernetes SRE tasks, including 40 public tasks and 19 held-out tasks; each task provides alerts, events, traces, metrics, logs, and topology, and asks the model to identify the minimal independent root-cause Kubernetes entities. confidence: 1 benchmark announcement source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-hugging-face-blog-itbench-aa-frontier-models-score-below-50-on-the-fir.md]
- ITBench-AA reports frontier model scores below 50% on SRE tasks, with Claude Opus 4.7 Adaptive Reasoning Max Effort at 47%, GPT-5.5 xhigh at 46%, and Qwen3.7 Max at 42% in the source's leaderboard snapshot. confidence: 1 benchmark announcement source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-hugging-face-blog-itbench-aa-frontier-models-score-below-50-on-the-fir.md]
- ITBench-AA holds the Stirrup reference harness constant across evaluated models, with shell access to a sandboxed filesystem, a 100-turn cap, and three repeats per task; scoring uses average precision at full recall, so missing any root cause scores zero and extra false-positive entities reduce precision. confidence: 1 benchmark announcement source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-hugging-face-blog-itbench-aa-frontier-models-score-below-50-on-the-fir.md]
- ITBench-AA reports that longer trajectories do not guarantee higher accuracy: models that over-investigate may submit upstream mechanisms or co-occurring symptoms as false positives. confidence: 1 benchmark announcement source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-hugging-face-blog-itbench-aa-frontier-models-score-below-50-on-the-fir.md]
- OpenAI's third-party evaluation playbook says agentic evaluation claims usually fall into capability elicitation, safeguard performance, or controlled comparison, and the harness should match the claim rather than being treated as incidental. confidence: 1 official OpenAI source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-openai-a-shared-playbook-for-trustworthy-third-party-evaluations.md]
- OpenAI says evaluation reports should describe the tested system, harness, tools, safeguards, budget, elicitation methods, and validity checks, including reward hacking, refusals, contamination, broken problems, and sandbagging. confidence: 1 official OpenAI source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-openai-a-shared-playbook-for-trustworthy-third-party-evaluations.md]
- OpenAI argues standardized harnesses are useful for controlled comparisons, but can under-elicit capability when they omit task-specific context management, retry behavior, tools, or budget that a capable user would reasonably use. confidence: 1 official OpenAI source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-openai-a-shared-playbook-for-trustworthy-third-party-evaluations.md]
- For capability or safeguard claims, OpenAI says reports should state tokens, turns, attempts, wall-clock time, inference cost, and where possible expected cost per successful solve; scores under a budget where performance is still improving should be described as lower-bound or budget-specific evidence, not a capability ceiling. confidence: 1 official OpenAI source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-openai-a-shared-playbook-for-trustworthy-third-party-evaluations.md]

## Typed entities
- benchmark: ITBench-AA
- dataset/benchmark family: IBM ITBench
- organization: Artificial Analysis
- organization: IBM Software Innovation Lab
- harness: Stirrup reference harness
- domain: Site Reliability Engineering / SRE
- platform: Kubernetes
- model: Claude Opus 4.7
- model: GPT-5.5
- model: Qwen3.7 Max
- concept: capability elicitation
- concept: safeguard performance
- concept: controlled comparison
- concept: maximum elicitation
- concept: standardized harness
- concept: reward hacking
- concept: contamination
- concept: sandbagging
- concept: broken evaluation problem
- metric: average precision at full recall

## Explicit relationships
- Agent benchmark results depend-on the harness, tool access, state handling, retry behavior, scoring, and budget used during evaluation.
- Standardized harnesses support controlled model comparison but can contradict maximum-elicitation claims if they under-supply tools, context, or budget.
- ITBench-AA uses a fixed harness to compare models on Kubernetes root-cause analysis.
- Recall-gated precision penalizes overbroad incident diagnoses because extra submitted entities count as false positives.
- Evaluation reports use validity checks to distinguish real capability from reward hacking, memorization, refusal behavior, broken tasks, or strategic underperformance.
- [[AI Agent Harnesses]] depends-on evaluation design because harness behavior can change observed agent capability.

## HoneyDrunk implications
- Model routing should not rely on a single public benchmark score. For HoneyDrunk tasks, record the harness, tools, retries, budget, and cost per successful solve.
- For SRE/agent-ops evaluations, prefer root-cause tasks with strict false-positive penalties so agents learn to stop at the minimal supported diagnosis.
- When comparing Claude/OpenAI/Google/Qwen/local models, decide whether the goal is controlled comparison or best credible performance. Those require different harness choices.
- Any HoneyDrunk benchmark report should include refusal count, broken task count, contamination risk, and examples of reward-hacking or over-investigation if found.

## Confidence and quality notes
- Quality posture: decision-useful for evaluation design. ITBench-AA is a benchmark announcement and should be checked against the live leaderboard before current routing decisions. OpenAI's playbook is an official methodology source but reflects OpenAI's framing.
- Weak spots: leaderboard values can change; treat the 2026-05-31 snapshot as historical evidence, not a permanent ranking.
- Privacy filter: no benchmark examples with private data copied; public model and organization names retained.

## 2026-06-01 compile additions

### Claims
- Judgment Labs' Agent Judge source argues that simple LLM judges break down on long-horizon production agents because trajectories exceed context windows, stateful actions require verification against systems of record, and agent/tool behavior drifts as products change. confidence: 1 vendor/practitioner source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-agent-judge-solving-long-context-evals-for-production-agents.md]
- Agent Judge is described as an agentic evaluation harness with three capabilities: search over long trajectories, verification against tool evidence and environment state, and rubric adaptation from human labels, production outcomes, judge disagreement, and similar prior runs. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-agent-judge-solving-long-context-evals-for-production-agents.md]
- In the source's internal trajectory-level hallucination test, a refined Agent Judge rubric reports 0.86 accuracy and 0.79 F1, outperforming its initial rubric and listed LLM/coding-agent judge baselines; treat the numbers as vendor-reported internal-traffic evidence, not a general benchmark. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-agent-judge-solving-long-context-evals-for-production-agents.md]

### Typed entities
- product/pattern: Agent Judge
- concept: trajectory-level hallucination
- concept: agentic evaluation harness
- capability: search
- capability: stateful verification
- capability: rubric adaptation
- concept: Rubric Builder
- system of record: GitHub / AWS / CRM / database / MCP server

### Explicit relationships
- Agent evaluation depends-on searchable trajectories when full traces exceed a single model context window.
- Stateful verification depends-on read-only source-of-truth access to systems the evaluated agent changed or claimed to change.
- Rubric adaptation uses human and production feedback to supersede stale fixed evaluation rubrics.
- [[AI Agent Harnesses]] depends-on evaluation harnesses that can inspect tool calls, state changes, logs, and durable external evidence.

### HoneyDrunk implications
- For OpenClaw/Grid evals, store enough trace spans, tool outputs, file diffs, test results, and external state IDs to let a judge verify claims after the run.
- Do not score long-running agents only by final answer text; include evidence search and state verification in the evaluation plan.

## 2026-06-02 compile additions

### Claims
- IBM Research's agent-logic article reports ITBench-measured gains for structured agent systems over generic baselines across incident investigation, code analysis, bug remediation, and compliance modernization; because these are vendor/product claims, use them to shape eval hypotheses rather than as neutral benchmark results. confidence: 1 vendor/research source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-hugging-face-ibm-research-beyond-llms-why-scalable-enterprise-ai-adopt.md]
- Perplexity's Search as Code article reports performance and cost-performance improvements on knowledge-intensive agent benchmarks when agents can compose low-level search primitives in sandboxed code; the benchmark result depends-on Perplexity's proprietary search stack, SDK, skill design, and sandbox runtime. confidence: 1 vendor/research source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-perplexity-research-rethinking-search-as-code-generation.md]

### Typed entities
- benchmark: ITBench
- architecture: Search as Code / SaC
- SDK: Agentic Search SDK
- concept: cost-performance frontier
- concept: harness-specific benchmark result

### Explicit relationships
- Agent-evaluation outcomes depend-on harness primitives such as search SDKs, program-analysis libraries, knowledge graphs, policy systems, and sandbox runtime.
- Vendor benchmark results can generate local eval hypotheses but do not supersede HoneyDrunk task-specific benchmark evidence.

### HoneyDrunk implications
- When benchmarking Lore/OpenClaw retrieval, compare monolithic search, agent-driven grep/read, and programmable retrieval primitives under the same task/budget report.
- Record whether eval gains came from the model, the harness, the search/index layer, or deterministic validators.

## 2026-06-03 compile additions

### Claims
- MAI-Code-1-Flash was evaluated by Microsoft against Claude Haiku 4.5 on SWE-Bench Verified, SWE-Bench Pro, SWE-Bench Multilingual, Terminal Bench 2, instruction-following, and adversarial reasoning tasks using a Copilot production harness; benchmark deltas should be treated as harness-specific vendor claims. confidence: 1 Microsoft AI source, last-confirmed 2026-06-03. [source: raw/2026-06-03-web-microsoft-ai-introducing-mai-code-1-flash.md]
- Microsoft reports MAI-Code-1-Flash uses fewer solution tokens on some tasks, making cost/latency part of the evaluation claim rather than only pass rate. confidence: 1 Microsoft AI source, last-confirmed 2026-06-03. [source: raw/2026-06-03-web-microsoft-ai-introducing-mai-code-1-flash.md]
- Fowler's June 2 fragment reinforces benchmark recency risk: closed and open model rankings can shift over months, so historical public benchmarks should not be treated as permanent routing evidence. confidence: 1 Fowler fragment source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-martin-fowler-fragments-june-2.md]

### Typed entities
- model: MAI-Code-1-Flash
- comparison model: Claude Haiku 4.5
- benchmark: SWE-Bench Verified
- benchmark: SWE-Bench Pro
- benchmark: SWE-Bench Multilingual
- benchmark: Terminal Bench 2
- benchmark: IF Bench
- concept: solution-token efficiency
- concept: benchmark recency risk

### Explicit relationships
- Model evaluation depends-on pass rate, solution-token cost, latency, harness, and task mix.
- Vendor benchmark results generate local eval hypotheses but do not supersede HoneyDrunk task-specific controlled comparisons.
- Model-routing evidence decays as model families and open/closed capability gaps change.

### HoneyDrunk implications
- When comparing coding models, include token count, time-to-first-useful-output, total latency, retries, and review burden alongside pass/fail.
- Re-run small routing evals after major model releases rather than relying on benchmark snapshots older than a few months.

## 2026-06-04 compile additions

### Claims
- Microsoft ASSERT is an open-source policy-driven evaluation framework that converts organizational policies and requirements into targeted agent evaluation scenarios, with inspectable local artifacts such as specs, generated cases, outputs, judge rationale, and metrics. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-microsoft-foundry-blog-build-agents-you-can-trust-across-any-framework.md]
- Agent Control Specification (ACS) is a portable runtime control standard for deterministic checks at input, LLM, state, tool-execution, and output checkpoints; it is intended to pair with ASSERT by evaluating, applying controls, and re-running evaluations. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-microsoft-foundry-blog-build-agents-you-can-trust-across-any-framework.md]
- Foundry observability adds multi-turn evaluation, user simulation, rubric evaluation, intelligent trace sampling, trace replay/visualization, and traces-to-dataset; this reinforces evaluation as a production loop over traces rather than one-off prompt tests. confidence: 2 Microsoft Foundry sources, last-confirmed 2026-06-04. [sources: raw/2026-06-04-web-microsoft-foundry-blog-build-2026-from-observability-to-roi-for-ai-age.md; raw/2026-06-04-web-microsoft-foundry-blog-build-agents-you-can-trust-across-any-framework.md]
- Foundry's ROI for agents private preview measures task completion, time saved, and cost efficiency, making business value part of the eval/operations loop rather than a separate spreadsheet. confidence: 2 Microsoft Foundry sources, last-confirmed 2026-06-04. [sources: raw/2026-06-04-web-microsoft-foundry-blog-build-2026-from-observability-to-roi-for-ai-age.md; raw/2026-06-04-web-microsoft-foundry-blog-build-and-run-agents-at-scale-with-microsoft-fo.md]

### Typed entities
- framework: ASSERT
- specification: Agent Control Specification / ACS
- evaluator: Rubric evaluator
- feature: user simulation
- feature: multi-turn evaluation
- feature: intelligent trace sampling
- feature: trace replay and visualization
- feature: traces to dataset
- feature: ROI for agents
- concept: policy-driven evaluation
- concept: runtime control checkpoint

### Explicit relationships
- ASSERT uses policy requirements to generate targeted safety/quality evaluations.
- ACS complements ASSERT by converting identified risks into portable runtime controls.
- Multi-turn evaluation supersedes single-turn scoring when context accumulation, tone drift, contradiction, or long task completion are the failure modes.
- Trace replay and traces-to-dataset use production behavior to strengthen offline eval coverage.
- ROI measurement depends-on task completion, time saved, cost, and trace-level evidence.

### HoneyDrunk implications
- For OpenClaw evals, model the loop as policy -> generated scenarios -> controls -> re-run -> trace-backed dataset, not as ad hoc examples.
- Keep judge artifacts inspectable. A pass/fail score without generated cases, rationale, and trace links is weak evidence for agent governance.
- Include business value only after correctness and safety are measurable; ROI dashboards without trustworthy evals can optimize the wrong behavior.

## 2026-06-07 compile additions

### Claims
- EVA-Bench Data 2.0 expands the ServiceNow voice-agent benchmark to 213 scenarios across three enterprise domains: Airline CSM, ITSM, and Healthcare HRSD, with 121 tools and 35+ workflows. confidence: 1 benchmark/dataset release source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-eva-bench-data-2-0-3-domains-121-tools-213-scenarios.md]
- EVA-Bench scenarios include structured user goals, initial scenario databases, and expected final database states, with generation/validation intended to produce exactly one correct resolution path for reproducible bot-to-bot evaluation. confidence: 1 benchmark/dataset release source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-eva-bench-data-2-0-3-domains-121-tools-213-scenarios.md]
- Microsoft Agent Framework evaluation supports local checks, custom function evaluators, Foundry cloud evaluators, expected outputs/tool calls, repetitions for consistency, conversation split strategies, and workflow/sub-agent breakdowns in .NET and Python. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-evaluation.md]
- Foundry Agent Optimizer evaluates hosted agents against task criteria, generates candidate instructions/skills/model/tool-description configurations, ranks candidates by score and token cost, and promotes a chosen candidate as a versioned hosted-agent configuration. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-introducing-agent-optimizer-in-foundry-agent-service.md]

### Typed entities
- benchmark/dataset: EVA-Bench Data 2.0
- domains: Airline Customer Service Management, Enterprise IT Service Management, Healthcare HR Service Delivery
- framework: Microsoft Agent Framework evaluation
- evaluator: LocalEvaluator
- evaluator: FoundryEvals
- product: Foundry Agent Optimizer
- concept: expected final database state
- concept: expected tool calls
- concept: conversation split strategy
- concept: optimization candidate

### Explicit relationships
- Voice-agent evaluation depends-on domain-specific tools, authentication flows, unsatisfiable goals, and final-state verification, not only transcript quality.
- Agent Framework evaluation uses local deterministic checks and cloud LLM-as-judge evaluators as complementary scoring paths.
- Foundry Agent Optimizer depends-on evaluation datasets and criteria; optimization without stable evals risks improving the wrong behavior.
- Candidate prompt/skill/model/tool-description configurations supersede a baseline only after scoring against the same task set and cost report.

### HoneyDrunk implications
- For voice or support-agent experiments, prefer eval cases with tool/database final-state checks and adversarial/unsatisfiable user goals.
- When using Agent Framework, keep local smoke checks in CI and reserve Foundry/LLM judge runs for broader quality, safety, and regression evaluation.
- Treat agent optimization as an auditable release step: preserve baseline, candidate diff, score, token cost, and rollback path.

### Quality notes
- EVA-Bench is a benchmark release and should be validated against the dataset/repo before adopting its scenarios. Microsoft sources are product documentation/blog claims; preview optimizer behavior and pricing need local verification.

## 2026-06-09 compile additions

### Claims
- Kasra's vulnerable-app benchmark tested multiple LLMs against a deliberately vulnerable React Native/FastAPI/Firebase app under budget and time limits; the strongest durable signal is that security-agent evals are highly sensitive to harness, refusal policy, budget, provider limits, and whether success criteria require the agent to inspect indirect service/datastore paths. confidence: 1 practitioner eval source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-i-built-a-vulnerable-app-and-spent-1-500-seeing-if-llms-could-hack-it.md]
- The same source reports GPT-5.5 solved 7/10 runs while several other models solved fewer or refused, but the author states the eval is not scientific; treat exact model rankings as weak, non-generalizable evidence. confidence: 1 practitioner eval source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-i-built-a-vulnerable-app-and-spent-1-500-seeing-if-llms-could-hack-it.md]
- The clearbluejar FreeBSD reproduction shows detection should be measured as a rate over repeated runs: initial full-subsystem runs appeared to miss CVE-2026-4747, but reruns showed local open-weight models could identify it; the bigger issue was false-positive volume. confidence: 1 practitioner security-research source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-system-over-model-tested-reproducing-mythos-s-freebsd-find-on-local-op.md]
- Adding a reachability stage to the vulnerability-scanning pipeline reportedly pruned Gemma findings from 30 to 5 and GPT-OSS findings from 21 to 4 while preserving the target CVE, reinforcing that eval harness stages can matter more than raw model choice. confidence: 1 practitioner security-research source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-system-over-model-tested-reproducing-mythos-s-freebsd-find-on-local-op.md]
- Anthropic's chemistry benchmark compares Claude Opus 4.7/4.6/Sonnet 4.6 against ChemDraw and MestReNova on small NMR forward-prediction and inverse-elucidation tasks; Opus 4.7 was competitive or better on average, but the evaluation is small and scaffold-limited. confidence: 1 Anthropic research source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-making-claude-a-chemist.md; page: [[ai-for-science-and-chemistry]]]

### Typed entities
- benchmark target: vulnerable React Native/FastAPI/Firebase app
- model: GPT-5.5
- model: DeepSeek V4 Pro
- model: Claude Sonnet 4.6
- model: Claude Opus 4.8
- model: Gemma 4 31B
- model: GPT-OSS-20B
- vulnerability: CVE-2026-4747
- project: AISLE nano-analyzer
- stage: reachability filter
- software: ChemDraw
- software: MestReNova
- task: NMR forward prediction
- task: structure elucidation

### Explicit relationships
- Security-agent eval outcomes depend-on harness, budget, refusal policy, provider reliability, and success scoring.
- Vulnerability-scanning evals should measure solve rate, false-positive burden, and reachability evidence, not only whether one run surfaced a candidate.
- Reachability filters complement LLM triage by checking attacker-controlled inputs and call paths.
- Domain-science evals depend-on representative scaffold breadth, solvent coverage, stereochemistry/2D data scope, and expert-auditable outputs.

### HoneyDrunk implications
- For HoneyDrunk model routing, avoid adopting one-off online eval rankings. Run small repeated local evals with transcripts, budget, refusal, cost, and false-positive review time recorded.
- Add "candidate count after triage" and "human minutes to validate" to vulnerability-agent eval reports.
- For scientific or asset-domain AI claims, require domain-specific holdout tasks and expert review before treating model output as operationally reliable.

### Quality notes
- June 9 eval sources are useful for harness design. Practitioner evals are not controlled benchmarks; Anthropic chemistry eval is primary but small and scoped.

## 2026-06-10 compile additions: Fable 5, North Mini Code, and OpenEnv

### Source-backed claims
- Anthropic reports Claude Fable 5 is strongest among its models on several benchmark and customer-task examples, including long-horizon coding and vision-based game/app reconstruction; these are vendor-supplied claims requiring local validation. Source: `raw/2026-06-10-web-anthropic-claude-fable-5-and-claude-mythos-5.md`. confidence: 1 source, last-confirmed 2026-06-10.
- GitHub reports Claude Fable 5 completed equivalent Copilot work with fewer tool calls and lower token consumption than previous Opus-tier models on internal benchmarks; the changelog does not provide enough detail for procurement-grade comparison. Source: `raw/2026-06-10-web-github-changelog-claude-fable-5-is-generally-available-for-github-copilot-github-changelo.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Cohere's North Mini Code is a 30B-parameter sparse MoE coding model with 3B active parameters, released under Apache 2.0 on Hugging Face and trained for agentic software-engineering tasks. Source: `raw/2026-06-10-web-hugging-face-introducing-north-mini-code-coheres-first-model-for-developers.md`. confidence: 1 source, last-confirmed 2026-06-10.
- North Mini Code's evaluation writeup emphasizes terminal-agent harnesses, SWE-Bench/SWE-Bench-Pro deduplication, Terminal-Bench, SciCode, LiveCodeBench, multiple seeds, and task scaffolds rather than only single-turn coding prompts. Source: `raw/2026-06-10-web-hugging-face-introducing-north-mini-code-coheres-first-model-for-developers.md`. confidence: 1 source, last-confirmed 2026-06-10.
- OpenEnv is intended to make agentic RL environments reusable across harnesses, trainers, and deployment settings without standardizing the reward function itself. Source: `raw/2026-06-10-web-hugging-face-the-open-source-community-is-backing-openenv-for-agentic-rl.md`. confidence: 1 source, last-confirmed 2026-06-10.

### Typed entities
- project: Claude Fable 5
- project: North Mini Code
- project: OpenEnv
- concept: terminal-agent benchmark
- concept: agentic RL environment
- decision: HoneyDrunk local coding-agent eval suite

### Explicit relationships
- North Mini Code uses terminal-agent harnesses and verifiable repository tasks to target agentic software engineering.
- OpenEnv supports evaluation and training reuse but does not replace task design or reward validation.
- Claude Fable 5 vendor benchmarks should be tested against HoneyDrunk tasks before routing changes.

### HoneyDrunk implications
- Add Fable 5 and North Mini Code to candidate evals only with retention, cost, local-run feasibility, and task-specific quality recorded.
- Prefer eval transcripts that include tool calls, token use, refusal/fallback behavior, human validation time, and false-positive review burden.
- Track environment standardization separately from benchmark quality; OpenEnv can make harnesses portable while still requiring strong tasks.

### Quality notes
- Fable and North Mini Code claims are vendor-authored. Use them to select candidates, not to declare winners.

## 2026-06-14 compile additions: olmo-eval and hidden-state probes

### Source-backed claims
- Allen AI's olmo-eval is positioned as an evaluation workbench for active model development, not only finished-model benchmarking: it runs repeatable benchmarks across changing checkpoints and compares interventions at aggregate and per-question levels. Source: `raw/2026-06-14-web-hugging-face-blog-olmo-eval-an-evaluation-workbench-for-the-model-deve.md`. confidence: 1 Hugging Face/Allen AI source, last-confirmed 2026-06-14.
- olmo-eval separates task, suite, and harness: the task defines what is measured, the suite groups tasks, and the harness controls runtime policy such as provider, tools, scaffolding, sandboxes, and auxiliary judge models. Source: `raw/2026-06-14-web-hugging-face-blog-olmo-eval-an-evaluation-workbench-for-the-model-deve.md`. confidence: 1 source, last-confirmed 2026-06-14.
- olmo-eval reports standard error and minimum detectable effect, and supports pairwise checkpoint comparison question by question so small average-score changes can be distinguished from noise or localized regressions. Source: `raw/2026-06-14-web-hugging-face-blog-olmo-eval-an-evaluation-workbench-for-the-model-deve.md`. confidence: 1 source, last-confirmed 2026-06-14.
- James Padolsey's hidden-state probe writeup argues that some rubric-style text classification decisions already exist in an LLM's residual stream before generation; a small calibrated probe over a mid-layer final-token hidden state can replace slow prose-based LLM judging for high-volume structural classification tasks. Source: `raw/2026-06-14-rss-j11y-io-don-t-let-the-llm-speak-just-probe-it-by-james-padolsey.md`. confidence: 1 practitioner/research source, last-confirmed 2026-06-14.
- The same source notes a practical tradeoff for multi-criterion scoring: content-prefill/KV reuse is cheap when criteria are applied after content, but criteria-before-content can perform better when every content token needs to attend to a complex criterion. Source: `raw/2026-06-14-rss-j11y-io-don-t-let-the-llm-speak-just-probe-it-by-james-padolsey.md`. confidence: 1 source, last-confirmed 2026-06-14.
- The Brain Overflow security-review experiment reinforces that automated security-review evaluation should test same-session, cold-session, diff-only, and cross-commit/component-boundary conditions separately, because each exposes different blind spots. Source: `raw/2026-06-14-rss-brain-overflow-hidden-gaps-in-claude-code-security-reviews.md`. confidence: 1 practitioner experiment, last-confirmed 2026-06-14.

### Typed entities
- project: olmo-eval
- standard: OLMES
- framework: Harbor
- concept: task/suite/harness abstraction
- concept: minimum detectable effect
- concept: pairwise checkpoint comparison
- concept: hidden-state probe
- concept: residual stream
- concept: calibrated classifier
- technique: isotonic regression
- technique: KV cache reuse
- benchmark concern: review context bias

### Explicit relationships
- Evaluation workbenches depend-on separating benchmark logic from runtime policy so one benchmark can be run under baseline, tool-using, sandboxed, or judge-assisted harnesses.
- Pairwise checkpoint comparison complements aggregate score reporting by surfacing which prompts improved or regressed.
- Minimum detectable effect helps decide whether a small score delta is actionable or statistical noise.
- Hidden-state probes complement LLM-as-judge generation by reading classifier-like decisions from the forward pass without asking the model to emit prose.
- Probe accuracy depends-on prompt template, final-token seed, layer selection, calibration, and whether criterion/content interaction needs full cross-attention.
- Security-review evals depend-on reviewer context condition: same-session, cold independent, diff-only, and cross-commit review are not interchangeable.

### HoneyDrunk implications
- For OpenClaw/Grid model or prompt evals, store task, suite, harness, model, tools, sandbox, judge, and cost configuration as first-class run metadata.
- Report score deltas with standard error or minimum detectable effect before treating small improvements as routing evidence.
- For high-volume Lore/source triage, hidden-state probes or other calibrated non-generative classifiers may be worth a spike once labeled examples exist.
- Add security-review test cases that deliberately split risk across commits, tool permissions, and skill/subprocess boundaries.

### Quality notes
- olmo-eval is a concrete open-source evaluation-workbench signal, but adoption should follow a local spike. Hidden-state probe evidence is practitioner-research guidance and needs local labeled-data validation.

## 2026-06-16 compile additions: predictive data debugging as pre-training evaluation

### Source-backed claims
- Goodfire reports predictive data debugging can predict preference-training behavior before DPO by reading datasets through an interpreted model, with the captured article reporting R^2 = 0.9 against learned behavior in their experiments. Source: `raw/2026-06-16-web-goodfire-predictive-data-debugging-reveal-and-shape-what-your-model-learns-before-you-train.md`. confidence: 1 research/vendor source, last-confirmed 2026-06-16.
- The method traces predicted behavior shifts back to responsible data clusters, letting teams identify safety regressions, hallucination-inducing patterns, sycophancy clusters, and unexpected dataset artifacts before a full train/eval/retrain loop. Source: `raw/2026-06-16-web-goodfire-predictive-data-debugging-reveal-and-shape-what-your-model-learns-before-you-train.md`. confidence: 1 research/vendor source, last-confirmed 2026-06-16.
- Goodfire says some interventions can reshape data or training to preserve benchmark gains while reducing unwanted behavior, but other classes such as hallucinated links and narrow context-specific sycophancy remained only partially mitigated in the captured case studies. Source: `raw/2026-06-16-web-goodfire-predictive-data-debugging-reveal-and-shape-what-your-model-learns-before-you-train.md`. confidence: 1 research/vendor source, last-confirmed 2026-06-16.

### Typed entities
- company/platform: Goodfire Silico
- dataset: Dolci
- dataset: Tulu 3
- model family: Llama 3.1
- method: predictive data debugging
- method: direct preference optimization / DPO
- concept: concept-level data view
- concept: preference-data regression
- control: targeted data rewrite

### Explicit relationships
- Predictive data debugging complements benchmark evaluation by identifying likely training-induced behavior shifts before training.
- Data-cluster tracing links model behavior regressions back to source examples, making dataset curation part of the evaluation loop.
- Targeted data rewrites can mitigate some unwanted learned behavior but do not supersede downstream evals or manual inspection.

### HoneyDrunk implications
- If HoneyDrunk builds a preference dataset, treat it as executable behavior-shaping code: inspect, test, debug, and version it before training.
- Record which data clusters drive any local model behavior change, not just aggregate eval deltas.
- Use pre-training data-debugging results as risk triage, then confirm with held-out evals and human review.

### Quality notes
- Goodfire is both research source and product vendor. Claims are promising but should be reproduced on HoneyDrunk datasets before adoption.

## 2026-06-18 compile additions: fine-tuned trace judges and review evidence evaluation

### Source-backed claims
- LangChain/Fireworks report fine-tuning a Qwen judge model to classify "perceived error" in production traces, using multi-turn human/AI messages and labels built from model-assisted plus human review. Source: `raw/2026-06-18-web-langchain-com-building-a-100x-cheaper-trace-judge-with-fireworks.md`. confidence: 1 vendor/research blog source, last-confirmed 2026-06-18.
- In the reported experiments, a Qwen-3.5-35B LoRA SFT judge trained on `chat-langchain` reached 96.1% on that holdout and 90.8% on the separate Fleet holdout, matching or exceeding several frontier-model baselines while being described as 10-100x cheaper at scale. Source: `raw/2026-06-18-web-langchain-com-building-a-100x-cheaper-trace-judge-with-fireworks.md`. confidence: 1 vendor/research source, last-confirmed 2026-06-18.
- LangChain defines "perceived error" as user-observed assistant mistake/correction signals, not objective correctness or user happiness, and treats it as a general-purpose trace-mining signal that still may need application-specific evaluators. Source: `raw/2026-06-18-web-langchain-com-building-a-100x-cheaper-trace-judge-with-fireworks.md`. confidence: 1 source, last-confirmed 2026-06-18.
- Greptile's TREX code-review design evaluates review usefulness through artifact-backed execution rather than only textual findings, using screenshots, logs, traces, scripts, and videos to make review conclusions inspectable. Source: `raw/2026-06-18-web-greptile-com-building-trex-code-execution-and-artifact-generation-for-.md`; page: [[ai-assisted-software-practice]]. confidence: 1 vendor engineering source, last-confirmed 2026-06-18.

### Typed entities
- platform: LangSmith
- company/platform: Fireworks
- model: Qwen-3.5-35B
- method: LoRA SFT
- metric/concept: perceived error
- dataset: `chat-langchain`
- dataset: Fleet
- system: Greptile TREX
- artifact: execution trace
- artifact: screenshot/log/API trace/video

### Explicit relationships
- Trace judges complement live observability by mining every production trace for cheap, coarse signals before deeper human or application-specific evaluation.
- Perceived-error classification does not supersede objective correctness tests because it measures user correction/frustration signals.
- Fine-tuned open judges can complement frontier judges when trace volume makes per-call frontier evaluation too expensive.
- Artifact-backed review evaluation links a finding to reproducible evidence, making precision/recall assessment less dependent on prose trust.

### HoneyDrunk implications
- For OpenClaw/Grid/Lore traces, consider a small labeled "perceived error" or "operator correction" dataset before adopting any trace judge.
- Use cheap general trace classifiers for triage only; keep task-specific evals and human review for correctness-critical decisions.
- When measuring AI review quality, score whether findings include reproducible evidence, not only whether they sound plausible.

### Quality notes
- LangChain/Fireworks and Greptile are vendor-authored sources. Treat reported accuracy/cost as spike hypotheses until reproduced on HoneyDrunk traces.

## 2026-06-19 compile additions: agent-use benchmarks, production eval layers, and privacy leakage

### Source-backed claims
- Hugging Face's `agent-eval` harness evaluates whether agents can use a tool effectively by measuring match rate, median time, token use, error rate, and behavior markers across model, repository revision, task, and context tier (`bare`, `clone`, `skill`). Source: `raw/2026-06-19-web-huggingface-co-is-it-agentic-enough-benchmarking-open-models-on-your-own-tooling.md`. confidence: 1 Hugging Face source, last-confirmed 2026-06-19.
- The same source reports that adding a Transformers CLI plus Skill reduced time for large open models but increased or harmed smaller-model behavior in some settings, including a Qwen3-14B case where the Skill was mistaken for a directly callable tool. Source: `raw/2026-06-19-web-huggingface-co-is-it-agentic-enough-benchmarking-open-models-on-your-own-tooling.md`. confidence: 1 source, last-confirmed 2026-06-19.
- Thoughtworks recommends a three-layer AI-agent evaluation architecture: persona-based multi-turn simulations, functional unit evals for agents or conversations, and production observability over traces, feedback, latency, cost, retrieval quality, and failure patterns. Source: `raw/2026-06-19-web-thoughtworks-com-evaluating-ai-agents-in-production-a-practical-framework.md`. confidence: 1 Thoughtworks practice source, last-confirmed 2026-06-19.
- MosaicLeaks defines a deep-research privacy benchmark where private local facts can leak through cumulative public web-query logs; the reported base Qwen3-4B strict-chain success was 48.7% with 34.0% answer/full-information leakage, while task-only RL improved success to 59.3% but worsened leakage to 51.7%. Source: `raw/2026-06-19-web-huggingface-co-mosaicleaks-can-your-research-agent-keep-a-secret.md`; page: [[ai-coding-agent-security]]. confidence: 1 Hugging Face/ServiceNow research source, last-confirmed 2026-06-19.
- Privacy-Aware Deep Research / PA-DR combines situational task rewards with learned privacy rewards, reporting 58.7% strict-chain success and 9.9% answer/full-information leakage on the MosaicLeaks setup. Source: `raw/2026-06-19-web-huggingface-co-mosaicleaks-can-your-research-agent-keep-a-secret.md`. confidence: 1 source, last-confirmed 2026-06-19.

### Typed entities
- harness/tool: `agent-eval`
- coding agent: pi
- library: Transformers
- model: Qwen3-4B
- model: Qwen3-14B
- benchmark: MosaicLeaks
- method: Privacy-Aware Deep Research / PA-DR
- metric: strict chain success
- metric: answer/full-information leakage
- evaluation layer: persona-based testing
- evaluation layer: functional unit evals
- evaluation layer: operational observability

### Explicit relationships
- Agent-use evaluation depends-on process metrics and behavior markers, not only final-answer correctness.
- Skills can complement agent performance for strong models while contradicting smaller-model expectations when documentation looks like a callable tool.
- Production agent evaluation depends-on offline tests, multi-turn persona simulation, and live observability feeding back into the eval set.
- Deep-research privacy depends-on how public queries are constructed across a chain, not only whether private documents are excluded from final answers.
- Task-only optimization can contradict privacy goals by teaching agents to pack more private context into external queries.

### HoneyDrunk implications
- For HoneyDrunk tool and skill changes, run evals across model sizes and record whether the change reduces turns/time without increasing ambiguity or token bloat.
- Add behavior markers to local evals: CLI adoption, direct shell use, fallback to hand-written scripts, unsupported tool-call attempts, and silent failures.
- For Lore/RAG agents that mix private notes with web search, evaluate query leakage explicitly; prompt-only "do not leak" guidance is weak evidence.
- Treat production eval as a loop: traces and user/operator corrections should create new regression cases.

### Quality notes
- Hugging Face/ServiceNow and Thoughtworks sources are research/practice sources. Reported benchmark numbers are source snapshots and should be reproduced on HoneyDrunk tasks before routing or training decisions.

## 2026-06-20 compile additions: vulnerability harness evaluation metrics

### Source-backed claims
- Cloudflare's vulnerability harness measures usefulness as a filtering funnel, not speculative recall: raw candidates are validated, deduplicated, judged for production reachability, and converted into actionable findings with tests and patches. Source: `raw/2026-06-20-web-cloudflare-build-your-own-vulnerability-harness-20-minute-read.md`; page: [[ai-coding-agent-security]]. confidence: 1 Cloudflare source, last-confirmed 2026-06-20.
- The Cloudflare source reports lifetime funnel examples including 20,799 raw VDH candidates, about 12,057 surviving validation, 13,841 total findings in VVS, 5,442 deduplicated findings, and 7,245 actionable findings for engineering teams; treat these as source-reported operational metrics, not a benchmark transferable to HoneyDrunk. Source: `raw/2026-06-20-web-cloudflare-build-your-own-vulnerability-harness-20-minute-read.md`. confidence: 1 source, last-confirmed 2026-06-20.
- Cloudflare's design uses health signals such as suspiciously fast hunts, zero-finding shallow runs, coverage cells by area and attack class, held-out repository prompt tests, fail-to-pass patch tests, and different models for discovery versus validation. Source: `raw/2026-06-20-web-cloudflare-build-your-own-vulnerability-harness-20-minute-read.md`. confidence: 1 source, last-confirmed 2026-06-20.

### Typed entities
- system: Vulnerability Discovery Harness / VDH
- system: Vulnerability Validation System / VVS
- metric: validation rejection rate
- metric: high-integrity finding share
- metric: actionable finding count
- metric: area x attack-class coverage cell
- metric: shallow run
- control: held-out repository prompt test
- control: fail-to-pass regression gate

### Explicit relationships
- Vulnerability-agent evaluation depends-on candidate funnel quality, deduplication, reachability judgment, test evidence, and patch validation rather than raw finding volume.
- Different-model validation complements discovery because it reduces single-model assumption lock-in.
- Zero findings can indicate either clean code or a shallow/crashed run; harness health checks distinguish those cases.

### HoneyDrunk implications
- For HoneyDrunk security-agent evals, report raw candidates, validation survivors, duplicates, wrong-repo/low-risk findings, actionable findings, false-positive review time, and fail-to-pass patch success.
- Do not optimize for maximum findings. Optimize for verified, reproducible, reachable issues with bounded human review burden.

### Quality notes
- Cloudflare metrics are operational self-reporting. They are valuable for eval design, but not external proof of expected HoneyDrunk yield.
