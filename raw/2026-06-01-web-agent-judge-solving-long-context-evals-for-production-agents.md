---
source: "https://www.judgmentlabs.ai/blogs/agent-judge-solving-long-context-evaluations"
title: "Agent Judge: Solving Long-Context Evals for Production Agents"
author: "Rishi Gujjar, Andrew Li"
date_published: "2026-05-27"
date_clipped: "2026-06-01"
category: "AI / LLM Research & Tooling"
source_type: "web"
---

# Agent Judge: Solving Long-Context Evals for Production Agents

Source: https://www.judgmentlabs.ai/blogs/agent-judge-solving-long-context-evaluations

Agent Judge: Solving Long-Context Evals for Production Agents Why production agent evals need agentic judges that can search, verify, and adapt.
Rishi Gujjar , Andrew Li · May 27, 2026 · 8 min read Moving Away From Simple LLM Judges 
Most teams evaluate agent trajectories with a simple LLM judge approach: give the judge the user query, final agent output, perhaps some metadata, and a rubric. Then, ask whether the agent behaved as intended.
As the industry moves toward long-horizon agents that autonomously perform tasks end-to-end, LLM judges fail to consistently produce accurate evals. For instance, a sales agent may research leads, update a CRM, send an email, and book a meeting before it returns a final message. Or a coding agent may edit dozens of files, update an AWS config, and open a GitHub PR.
In both cases, a basic LLM judge breaks down: it cannot fit the full agent trajectory into its context window, and it cannot verify stateful changes against source-of-truth systems such as Google Calendar, a CRM, AWS, or GitHub. As a result, the effectiveness of automated evals falls apart. Agent failures slip through undetected, customer dissatisfaction persists, and teams default back to manual review of agent trajectories.
LLM judges break down on long-horizon agents for three reasons:
Long trajectories. Long-horizon agents can span hundreds of tool calls across databases, services, documents, and other systems. Coding agents like Codex and Claude Code can run for long horizons because they compact context as they work. That lets their trajectories extend into millions of tokens, far beyond what an LLM judge can fit into a single context window. 
LLM Judges can only read a small window of a long trajectory Most of the trajectory falls outside what the judge can read. What the Judge Misses Input Rest of trajectory Output LLM Context Window Long-horizon agent trajectories can exceed what an LLM judge can hold in context. Pasting the whole trace into one prompt may fail outright; truncating or slicing it leaves important parts unread. 
Stateful actions. Production agents do more than generate text. They query databases, call APIs, update records, send messages, and trigger workflows. A background sales agent might update the status of your leads, and the evaluator has to look into the CRM to verify that the change was reflected. 
Only Agent Judge can reach the systems that hold the truth. LLM Judges only see the trajectory. Agent Judge inspects the systems where production state lives. LLM Judge GitHub AWS IAM Secrets Manager CloudWatch Agent Judge GitHub AWS IAM Secrets Manager CloudWatch An LLM Judge only sees the trajectory, not the corresponding environment, so stateful changes go unverified. Agent Judge queries the same systems the agent acted on and checks whether the action actually happened. 
Changing behavior. Models, tools, and user workflows evolve as AI systems improve. An evaluation rubric that worked last month may go stale, miss new failure modes, over-penalize improved behavior, or keep looking for evidence in the wrong place. In production, the rubric has to evolve with the distribution of your queries and changes to your agents so the evaluator stays accurate and useful. 
The rubric stays still. The agent does not. A fixed rubric defines a tolerance band. Production behavior drifts out of it. Week 1 Week 10 Rubric Behavior Changes to the underlying models, tools, and user workflows change how the agent behaves. A fixed rubric keeps grading against old criteria, so the judge stops catching relevant new failure modes. 
Evaluations are no longer a judgment of the final answer. It is an investigation of the entire trajectory. The evaluator has to inspect what the agent saw, did, changed, and relied on.
Agent Judge 
We designed Agent Judge as an agentic evaluation harness to handle these three failure modes through three distinct capabilities: Search, Verification, and Adaptation.
Search: handles long trajectories by making them navigable, so buried evidence can be found without manual trace review. 
Verification: handles stateful actions by checking tool evidence and environment state, so the eval checks the effect of agent actions. 
Adaptation: handles dynamic human and agent behavior by comparing evaluations against human feedback and production signals across many production trajectories, so rubrics can evolve as the agent, tools, and product change. 
Agent Judge runs as a multi-agent system: reader agents inspect targeted evidence, spawned worker agents split the search or verification work, and forked agents pursue new questions raised by the first pass.
Search 
In long trajectories, failure modes are subtle and rarely live in one place. Mistakes can originate from an early retrieval result, a failed retry, a later tool call, or the final answer. Evaluating these cases often requires multi-hop reasoning: one search surfaces a clue, that clue raises a new question, and the evaluator has to follow the chain.
Agent Judge turns long-horizon trajectories into a queryable object. Messages, tool calls, retrieved documents, database responses, logs, retries, and state changes all become navigable evidence, not just context to jam into a single prompt.
Pull only the slices that matter Agent Judge picks the turns that decide the outcome — the rest stays out of context. Coding agent trajectory read grep edit read read bash read bash read test test read git msg edit bash git Evidence Agent Judge searches across the trajectory for evidence relevant to the rubric. The rest of the trajectory stays out of the worker agent context. 
Agent Judge searches across two planes: within the current trajectory and across prior trajectories. It can spend more compute where the case is ambiguous or complex: reading targeted slices of evidence, spawning worker agents to inspect specific parts of the run, or forking follow-up searches when the first search surfaces new information.
Within a trajectory: Worker agents inspect specific turns, tool-call chains, retrieved records, logs, or state changes. One worker might track which record the agent used, while another checks whether a later answer depended on stale or incorrect evidence. 
Example 
Across trajectories: Other workers can search similar runs, prior labels, previous judge disagreements, or repeated failure patterns to understand whether the current case matches something the system has seen before. 
Example 
The coordinator collects the relevant spans, tool calls, and state changes, then combines them into an evaluation or launches follow-up searches if the evidence is incomplete.
Verification 
Agent Judge verifies that the environment state matches the agent's claimed actions. Did the agent update the correct record? Did the API call succeed? Did the generated PR modify the right files? Did the workflow actually trigger?
On recorded or live runs, Agent Judge inspects captured tool evidence such as API responses, database results, logs, update confirmations, retrieved records, and GitHub events. When the underlying system exposes durable evidence, such as audit logs, event streams, timestamps, or versioned records, Agent Judge can also verify stateful actions against read-only source-of-truth systems like databases, service APIs, GitHub, ticketing systems, or MCP servers.
Claimed actions, checked against the source of truth Agent Judge lines up each claim with the recorded state and flags where the two diverge. Agent claims Source of truth Edited auth File change Ran tests Test run Opened PR Pull request Bug fixed Final claim Diff present Repository Tests ran CI system PR #1247 open GitHub 1 test failing Not fixed Agent Judge aligns each claimed action with the system’s recorded state. Three match; the final “bug fixed” claim diverges — CI still shows a failing test. 
Agent Judge evaluates stateful work directly: not whether the agent described the right action, but whether the action actually happened.
Adaptation 
Agent Judge adapts through Rubric Builder, a feedback loop that turns evaluated trajectories and human-in-the-loop signals into improvements for the next rubric version. The goal is to make sure human feedback is reflected in the criteria future evaluations use.
Rubric updates are concrete: add a missing criterion, tighten vague language using examples, reduce a recurring false positive or false negative, or tell the judge which evidence to inspect more carefully.
The loop repeats. Agent Judge reruns the updated rubric until Rubric Builder exhausts its search for improvements:
Evaluation: Agent Judge evaluates difficult or high-signal cases using the current rubric. 
Calibration check: The evaluations are compared against feedback signals such as human-expert labels, pairwise preferences, production outcomes, environment checks, judge disagreement, or similar runs with different outcomes. 
Rubric refinement: An analysis agent reviews patterns across the gaps, not just isolated errors, and proposes a focused rubric change. 
Iteration: The refined rubric is fed back into Agent Judge, and the process repeats as more production data comes in. 
The rubric converges, pass by pass Each rerun makes a focused change to the rubric. Accuracy climbs, then settles as the gains run out. Accuracy Rubric refinement pass Added CI test check Tightened wording Removed false-positive rule Gains exhausted Across successive refinement passes — each a focused change to the rubric — Agent Judge’s accuracy rises and then plateaus as Rubric Builder exhausts its search for improvements. 
Over time, the rubric becomes a living, versioned evaluation artifact: tested against production trajectories, updated from feedback, and grown alongside your agents instead of rewritten by hand each time behavior shifts.
Evaluating on Internal Traffic 
We tested Agent Judge against coding agents and LLM judges on trajectory-level hallucination detection using internal production traffic. We define trajectory-level hallucination as an unsupported claim or action relative to the trajectory, tool evidence, or source-of-truth environment state.
Human experts labeled each trajectory for hallucination. We evaluated the labeled set with coding-agent harnesses, LLM judges, Agent Judge with the initial rubric, and Agent Judge after Rubric Builder refinement.
Method Setup Accuracy Recall Precision F1 Agent Judge, Refined Rubric Custom agentic evaluation harness with Rubric Builder 0.86 0.88 0.71 0.79 Agent Judge, Initial Rubric Custom agentic evaluation harness with initial rubric 0.76 0.80 0.58 0.67 Claude Code Claude Opus 4.6 in coding-agent harness with rg and jq 0.73 0.53 0.56 0.54 Codex GPT-5.4 in coding-agent harness with rg and jq 0.69 0.63 0.49 0.55 GPT-5.4 LLM Judge LLM judge over trajectory and rubric 0.74 0.80 0.54 0.65 GPT-5.4-mini LLM Judge LLM judge over trajectory and rubric 0.65 0.51 0.43 0.47 
After five refinement iterations, Agent Judge with Rubric Builder improves accuracy, recall, precision, and F1 over the initial rubric.
To measure hard cases, we used a five-judge LLM ensemble as a difficulty baseline. We compare that baseline against Agent Judge with the initial rubric and Agent Judge after Rubric Builder refinement.
Accuracy by Difficulty Decile Higher deciles are harder under the trajectory difficulty heuristic. 100 80 60 40 20 0 1 2 3 4 5 6 7 8 9 10 Difficulty Decile Accuracy (%) Agent Judge w/ Rubric Builder Agent Judge, initial rubric 5x LLM Judge Ensemble GPT-5.4 LLM Judge Claude Code Codex Accuracy by difficulty decile. Agent Judge with Rubric Builder stays strongest in the hard tail, while the five-judge LLM ensemble baseline drops sharply as trajectory difficulty increases. 
Across difficulty deciles, Agent Judge with Rubric Builder matches or beats the baselines in most deciles, while the five-judge LLM ensemble consistency degrades sharply as difficulty increases.
Long-horizon agent evals should be done by agents with dynamic rubrics, not fixed LLM judge prompts. High-quality evals need access to the full trajectory context, the environment state the agent changed, and the feedback needed to adapt as production behavior evolves.
What's Next 
The next step is failure diagnosis. As Agent Judge evaluates more trajectories, it should not only assign scores; it should analyze why failures happen, identify the code paths, tools, prompts, or workflows involved, and surface the changes most likely to improve the agent.
Agent Judge turns evals into a production improvement loop: better judges produce better failure analysis, better failure analysis produces better rubrics and training examples, and the same loop can eventually propose targeted changes back into codebases, tools, prompts, and workflows.
Subscribe to our newsletter
Get new posts delivered to your inbox.
