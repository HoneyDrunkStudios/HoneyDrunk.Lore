---
source: "https://www.perplexity.ai/hub/blog/self-improving-skills"
title: "Self-improving skills"
author: "Perplexity Engineering"
date_published: "2026-11-18"
date_clipped: "2026-11-23"
category: "AI / LLM Research & Tooling"
source_type: "rss"
---

Source: https://www.perplexity.ai/hub/blog/self-improving-skills

# Self-improving skills

How Perplexity Brain learns recurring procedures from experience and keeps them current.

Nov 18, 2026

AuthorsPerplexity Engineering

## Introduction

Users have workflow-specific preferences and requirements that a general-purpose model cannot know in advance. An agent needs to learn these details to adapt its work to the user, rather than requiring the user to explain the same procedure or make the same corrections in every session. Continual learning makes this possible: experience from completed tasks should inform how the agent approaches future work.

Brain, Computer’s personalized self-improvement system, enables learning through experience. It already maintains a [structured knowledge wiki](https://www.perplexity.ai/hub/blog/brain-agentic-memory-as-a-knowledge-wiki) that connects information about the user and their work to the evidence supporting it. Background agents update the wiki as new information accumulates, so the memory system improves over time.

[Agent skills](https://www.perplexity.ai/hub/blog/designing-refining-and-maintaining-agent-skills-at-perplexity) provide another way to guide agent behavior without changing the underlying model. Skills are reusable instructions that guide an agent through particular tasks. They capture requirements and supporting resources for recurring workflows that the agent would otherwise need to infer from memory or receive from the user every time, improving performance on out-of-distribution tasks. They can also include scripts for repetitive procedures or processing that can be reliably expressed in code, so the agent can simply run those scripts when they apply. The harness makes available skills discoverable and loads their instructions into context when the agent requests them. Users can also directly specify which skills to use in the prompt.

**We’re extending Brain to automatically create and update agent skills**. Brain builds on a user’s memory and session history to write and refine personal skills that capture procedures for that user’s workflows. We apply a similar approach to update built-in skills, which are available to every Perplexity user, based on aggregate patterns across all sessions.

FIG. 01An agent combines general capability with selected task context and personal experience. The underlying model uses the working context to choose what comes next, and that context changes as the task progresses. Brain supplies memory and personal skills, then uses selected session evidence for later updates, subject to checks and authorization. Personalization changes context and instructions, not model weights. Sources are selected as needed, not all loaded at once; this conceptual view simplifies update mechanisms.

We first describe our self-improvement engine shared across all skill types, and explain how it works for personal and built-in skills.

## Shared self-improvement engine

A useful skill still needs to change as new preferences emerge or experience reveals gaps in its instructions. Brain is responsible for discovering how the agent’s behavior should change the next time Computer encounters a similar task and determining how the skill should change to better achieve the desired outcome.

This improvement process forms a loop with four stages:

1. **Evidence**. Brain finds past sessions where the skill was used, especially ones where it fell short.
2. **Reflection**. An improvement agent studies that evidence and proposes updates to the skill.
3. **Verification**. Checks confirm that the proposal is well-formed and likely to improve outcomes.
4. **Activation**. The verified change is applied. Future sessions use the new version, providing evidence for the next round.

FIG. 02Brain selects past sessions where the skill was used, especially those where it fell short. An improvement agent proposes an update, and checks assess whether it is well-formed and likely to improve outcomes. Once applied, the new version is used in future sessions, providing evidence for the next round.

This loop relies on many existing capabilities built for Computer and Brain. Here, we describe the shared machinery that enables evidence and reflection. The verification and activation procedures depend on whether a change reaches one user or every Perplexity user, so we cover them in the following sections on the personal and built-in skill improvement loops.

### Evidence from past sessions

Reflection requires finding sessions where a skill was used, especially ones where there’s room for improvement. The Computer harness records signals that make this possible. When the agent loads a skill, the harness records a skill-load event that links the skill to the session. When the agent sees user frustration, broken behavior, or clear inefficiency, the agent files a short, structured diagnostic, and the harness attaches the skills in use. These are particularly useful for built-in skills, where any session could potentially be relevant, so the system needs a way to quickly narrow down the evidence pool.

Agents benefit from having access to the full record, rather than making a judgement based on the outcome or a short summary. Computer stores past sessions using provider-agnostic trajectory representations that capture messages, tool calls, reasoning, and results. We’ve also built a suite of command-line tools that agents can use to decode these trajectories and reconstruct full sessions. This enables the reflection agent to inspect specific skill loads and tool calls, identifying exact points where issues occurred or improvements could be made.

bash

`# Decode a stored trajectory into structured messages,
# including tool calls, their arguments, and their results.
python3 deserialize_trajectory.py \
 --convo-path session/convo.pb.lz4 \
 --jsonl -o session.jsonl
# Identify which skills the agent loaded and how often.
python3 list_skills_used.py session.jsonl
# Read one turn in detail, including its tool calls and results.
python3 deserialize_trajectory.py \
 --convo-path session/convo.pb.lz4 \
 --turn 3 -o turn-3.md
# Recover earlier steps preserved before a context compaction.
python3 deserialize_trajectory.py \
 --convo-path session/compactions/001/original_convo.pb.lz4 \
 --jsonl -o earlier-history.jsonl`

Example usage of Computer’s internal trajectory-inspection tools. Paths and identifiers are simplified for illustration; command names and arguments follow the implementation.

### Reflection with background agents

Brain uses a team of background agents to continuously optimize the experience for each user. For example, [Dream agents](https://www.perplexity.ai/hub/blog/brain-agentic-memory-as-a-knowledge-wiki) review accumulated experience to update the knowledge wiki. Similarly, skill improvement is powered by improvement agents that reflect on skill-use evidence to propose updates.

Each agent works in its own sandbox with a frontier model, the relevant evidence, and the current skill library, guided by plugins and skills. It decides which sessions to read, draws a concrete lesson from each, and groups lessons that call for the same reusable behavior. Because a fix for one failure can contradict another instruction or add work elsewhere, it reads the full skill before proposing an edit, and abstains when the evidence does not support one.

Improvement agents run on the same harness as Computer. We made the harness modular, so a new agent application can reuse its machinery for reasoning, tool use, and context management while defining its own instructions and capabilities through plugins. A dedicated background worker fleet lets us scale this processing independently of foreground tasks.

FIG. 03The interactive agent and the background improvement agent run on the same Computer harness. The improvement agent uses session evidence and current skills to propose a change or abstain. A proposal must pass checks specific to the skill type before a new version becomes available to future sessions.

## The personal skill improvement loop

We first describe how the shared self-improvement engine is applied to the personal improvement loop, which turns a user’s task history into new or updated personal skills. The figure below traces an example skill through the full loop, ending on the revised version.

Overview1. Current skill2. Session evidence3. Improvement agent4. Proposal checks5. Activation6. New skill

FIG. 04The personal-skill loop moves from session evidence through an improvement agent, proposal checks, and activation. Current skills also inform the improvement agent; activated changes become available to future sessions.

During a daily generation run, the improvement agent reviews the user’s recent sessions to determine changes worth making. A set of recent sessions is preloaded into the sandbox, along with skill usage data; the rest of the user’s session history can be retrieved as needed. The improvement agent also receives the catalog of existing skills. It doesn’t have access to the internet or other connectors.

Plugins and skills designed for the personal skill improvement workflow guide the reflection process, drawing on our principles about what makes a good update. The agent first analyzes full trajectories to identify a concrete lesson in each session. It then compares the lessons to the existing instructions and decides whether to update a skill, create one, or make no change. Creating a skill requires two independent occurrences of the same reusable behavior, while an update to an existing skill can be justified with a single grounded occurrence.

The agent doesn’t modify the skill directly. Instead, it produces a proposal, recording the intended changes and the supporting reasoning and evidence. Updates are scoped to one change per skill per run. Deterministic checks verify that proposals are well-formed and can be applied to the skill. Separately, an LLM judge audits sampled proposals, checking whether the evidence supports the change and whether the resulting skill provides useful instructions.

Activation turns a verified proposal into a change to the user’s skill library, so the new version can be loaded and used in future sessions. Because the harness loads an index of all available skills at the start of each session, a large library of skills can clog the context window and make it harder for the agent to find and load relevant skills. As a result, the system keeps only the most valuable skills, retiring skills that aren’t necessary to keep a small, curated library. Specifically, we enforce a per-user cap of 10 automatically created skills. At capacity, the improvement agent can still update or remove skills, but in order to add a new skill it must retire an existing skill and justify why the new skill is more useful to the user’s work.

## The built-in skill improvement loop

We also extend Brain’s continuous skill improvement framework to built-in skills. Rather than using one user’s memory and session history to improve that user’s personal skills, the built-in loop uses evidence from many users to improve the skills available to every Perplexity user. Because built-in skills can be used by anyone, the bar for changes is high; updates that inadvertently worsen performance can affect thousands of sessions. The built-in improvement agent only changes candidate versions of skills. To reach the canonical version of the skill, these updates must pass through paired replay and internal human review. Once again, we trace the full loop with an example skill and supporting evidence.

Overview1. Current skill2. Session evidence3. Improvement agent4. Paired replay5. Human review

FIG. 05Failed sessions yield a root cause and held-out failure scenarios. The improvement agent uses the root cause and clean examples to propose a revision; the scenarios are never shown to it. Paired replay compares current and revised skills on the same tests, with successful candidates proceeding to human review before approval and merging.

The built-in improvement loop uses sanitized evidence from sessions eligible for use in training. Diagnostics and failure signals are used to select relevant evidence, alongside control sessions where the skill was used without raising any flags. A sanitization pipeline strips credentials and other secrets, along with attached files and media.

A scenario-generation agent turns sanitized evidence into concrete failure scenarios. It keeps only the context necessary to understand the failure case and improve the skill; the rest of the session is rebuilt synthetically, creating a self-contained test for the verification process. Scenarios must run without connected apps or sign-in; if the original task depended on a connector, that input is replaced by synthetic files in the scenario. A separate check verifies that the skill fails on the generated scenario.

Reflection happens through a weekly revision job that turns observed failures into fixes. It looks for skill failures that recur across multiple sessions, so a single bad session doesn’t drive an edit. Each recurring failure gets a separate improvement agent run. The agent receives a description of the root-cause, along with sanitized records from successful sessions. It uses this evidence to write a candidate revision of the skill. It doesn’t receive the full failure scenarios, as those are used in evaluation.

A separate replay job uses the generated scenarios to compare the original and revised versions of the skill. An LLM judge evaluates an agent’s answers and trajectories against each scenario’s rubric. For a proposal to pass, every test scenario must pass with the revised skill, and at least one must fail with the original. Scenarios built from the control sessions are replayed as well, to confirm that nothing has stopped working. For the failure scenarios, the judge also checks that the specific failure occurred, rather than treating an unsuccessful task as evidence of the same problem.

The workflow packages the candidate changes and evaluation results into a pull request for internal human review. The changes only go into effect if an engineer approves the PR.

## Evaluations

Automatic skill improvement has significantly increased skill creation and usage. Brain wrote over 80,000 personal skills for over 20,000 users between August 1 and November 14. Additionally, more than 100,000 automatic updates were applied to over 30,000 existing personal skills between September 4 and November 14.

These skills span a broad range of domains and tasks, from verifying software to reconciling payroll to designing figures. We categorized Brain-generated skills based on the workflows they describe. Even the largest domain, software engineering, accounted for only 11% of skills; it is followed by research and briefings (10.1%), sales and operations (9.9%), and finance and investing (9.9%).

FIG. 06Among 64,230 personal skills automatically created from August 1 to November 4, software engineering accounted for the largest share (11.0%), followed by research and briefings (10.1%). The ten domains shown account for 80.3% of all skills in the sample.

We conducted an eight-week randomized test on production traffic, comparing users with automatic personal-skill improvement enabled against a control group with it disabled. 72.9% of people with skill improvement enabled got at least one new personal skill, while only 6.5% of people without it manually added a new skill. More than half of the treatment group (53%) had a personal skill loaded in a conversation they started, compared to 13% for the control group; their turns loaded a personal skill about 3.6 times as often. Among customers who got a Brain-written skill, 63% used one again in a later conversation within four weeks.

FIG. 07In an eight-week randomized production test, 72.9% of users with automatic skill improvement enabled got at least one new personal skill, compared with 6.5% of controls. A personal skill was loaded in a conversation the user started for 53% of the enabled group and 13% of controls.

Our evaluations seek to determine how these new and updated skills impact task execution and overall performance.

Results from the same randomized experiment show a decline in tool call failures and user dissatisfaction. For users with automatic skill improvement, the tool call failure rate dropped by 11% across all Computer activity. Excluding the system’s own background runs, tool calls still failed about 7% less often, suggesting that reliability improved on the user’s work. User dissatisfaction, measured as the medium/high-dissatisfaction threads per user, dropped by 7.6%. We saw no measurable change in cost or response time. These early tests demonstrate promising results, and we expect the improvements to increase over time as we refine the system and roll out self-improving skills to more users.

Offline experiments have also recorded improvements in narrower settings. In a [SkillLearnBench](https://github.com/cxcscmu/SkillLearnBench) experiment, Computer used prior task trajectories to create one personal skill for each of nine task families. Across 16 paired evaluation instances, task success increased from 43.8% without skills to 62.5% with generated skills, providing evidence that skills derived from past experience can improve performance on repeated tasks. In one built-in case study, edits to an ecommerce skill led to a 6% quality increase at 32% lower cost, with quality measured by an automated judge.

## Conclusion

Self-improving skills give Computer another way to learn from the work it does. It extends Brain to create and maintain procedural memory, improving performance on complex workflows. Automatic skill improvement has already increased skill usage, reduced tool failure rates, and lowered user dissatisfaction.

Personal skill improvement is now available to all US Max subscribers. It’s on by default for eligible users, but can be turned off. The Plugins tab shows available skills, identifies those authored by Brain, and lets users choose which skills are enabled.

Next, we’ll expand improvement to more skill classes, including user-authored skills, skills shared within projects, and organization skills. We’ll continue refining the improvement pipeline and its evaluations so that revisions lead to more reliable procedures and better results.

## Citation

BibTeX

```whitespace-pre-wrap
@online{perplexity2026SelfImprovingSkills,
  author = {{Perplexity} and Nicholas Bien and Se Won Jang and Kate Jung and Nikila Venkat and Jarrod Bryan and Claire Beamer and Jeremy Yang},
  title = {{Self-improving skills}},
  date = {2026-11-18},
  url = {https://www.perplexity.ai/hub/blog/self-improving-skills}
}
```
