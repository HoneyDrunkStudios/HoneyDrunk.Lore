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
