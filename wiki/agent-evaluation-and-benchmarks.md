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
