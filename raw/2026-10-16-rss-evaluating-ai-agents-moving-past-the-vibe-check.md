---
source: "https://developers.googleblog.com/evaluating-ai-agents-moving-past-the-vibe-check"
title: "Evaluating AI agents: moving past the vibe check"
author: "Hugo Selbie; Dani Zamora; Jesse Carah; John DeMartino"
date_published: "2026-10-15"
date_clipped: "2026-10-16"
category: "AI / LLM Research & Tooling"
source_type: "rss"
---

# Evaluating AI agents: moving past the vibe check

![evaluating-ai-agents-banner-1600x900](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/evaluating-ai-agents-banner-1600x900.original.png)

## **TL;DR**

Your agent can loop, burn tokens, or give a completely hallucinated answer and still look fine. A vibe check won't catch that. This post is the playbook behind our AI Agent Clinic episode [*How to Actually Evaluate (Any) AI Agent: Beyond the Vibe Check*](https://youtu.be/wPdoZRbvaF4), where we build an eval pipeline for a LangGraph agent in 60 minutes. Here's what's inside:

![00-tldr-at-a-glance](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/00-tldr-at-a-glance.original.png)

## **Evaluating AI agents: moving past the vibe check**

When teams start building an AI agent, testing usually looks the same. You wire up a model, hand it a few tools, run three or four prompts in a terminal, and eyeball the output. If the answer looks reasonable, you ship it.

In practice, this breaks down fast. You tweak a system prompt to fix an edge case in one workflow, and suddenly the agent stops calling a required tool in another.

Worse, agents fail differently than standard software. An agent can get stuck in a retry loop, fire off multiple tool calls, yet still return a polite, plausible-sounding final answer.

In production, that hidden failure is costly:

* It quietly spikes your cloud bill and token usage.
* It exhausts downstream API rate limits and quotas.
* It leaves users staring at a loading spinner.
* It can trigger duplicate side effects in external systems, all while looking "fine" on the surface.
* It erodes user trust, and first impressions are hard to win back.

Integrating a reliable evaluation suite into your development lifecycle can seem like extra overhead during initial prototyping, right up until modifying your system prompt causes unexpected breaking changes. The key is recognizing that evaluation is a progressive journey: any repeatable evaluation system (no matter how simple) is better than relying on ad-hoc spot checks or no system at all. You don't need an elaborate automated grading architecture on Day 0. Instead, start with simple, repeatable checks and evolve your evaluation into a more complex, automated framework as your agent's capabilities and production demands grow.

Establishing a repeatable evaluation system is made substantially easier by integrating these decisions into an evaluation framework. Transitioning beyond simple subjective checks relies on two core pillars: human oversight and targeted tools. In this article, we explore how to set up an evaluation framework using the open-source [agent-eval](https://github.com/GoogleCloudPlatform/professional-services/tree/main/tools/agent-eval) toolkit. We'll demonstrate how combining manually reviewed traces with automated verification helps detect silent regressions early in development and scales seamlessly as your agent transitions to production.

---

## **Getting started: the high-level building blocks**

### **1. Define success with critical user journeys**

Before writing test code, you need a shared vision of what a good outcome actually looks like. Anchor your tests in **critical user journeys (CUJs)** rather than abstract benchmarks.

A CUJ defines what a user expects the system to achieve, structured around their persona, goals, constraints, and verification conditions:

> *"As an operations analyst, I expect the agent to ingest a counterparty trade discrepancy email, identify the disputed transaction, verify the trade economics against our internal ledger within 30 seconds, and draft a response reverse-translating our internal trade IDs back into the broker's nomenclature without human intervention."*

Every clause in that statement becomes an evaluation point: Did the agent resolve the correct transaction ID? Did it check the ledger before drafting? Did it map internal IDs back to the external nomenclature?

![01-cuj-evaluation-points](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/01-cuj-evaluation-points.original.png)

Every clause of a CUJ becomes an evaluation point.

Defining these expectations upfront forces product stakeholders, downstream users, and engineers to agree on defining how “success” is measured.

### **2. Start with simulated users, graduate to real traffic**

You do not need six months of production logs to build your initial golden dataset. Instead, break each CUJ down into concrete **scenarios** (both happy paths and edge cases) and feed them into a **user simulator LLM** (we like [ADK user simulations](https://adk.dev/evaluate/user-sim/)). Primed with a persona and behavioral constraints (for example, an impatient analyst giving incomplete ticket numbers, or a developer asking a multi-part debugging question), the simulator mirrors the messy phrasing, typos, and multi-turn complexity of real users.

![02-adk-user-simulation-scenarios](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/02-adk-user-simulation-scenarios.original.png)

Example scenarios for ADK user simulations.

By testing your agent against a synthetic user and realistic scenarios, you can record comprehensive execution traces (including tool logs) prior to user interaction. This enables you to pinpoint and resolve any performance gaps against your release standards. As live traffic begins to flow, you can progressively replace these synthetic setups with real production traces.

### **3. Measure across the full stack**

A single top-line score will never tell you *why* an agent failed. To isolate root causes, layer four types of checks: unit tests, deterministic metrics, LLM-as-a-judge rubrics, and integration tests.

![03-four-layers-of-checks](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/03-four-layers-of-checks.original.png)

Four layers of checks, from unit tests to integration tests.

## **Four common traps to avoid**

### **Trap 1: Throwing tests out and breaking your baseline**

Setting up evaluation metrics involves trial and error, and it is tempting to delete a noisy test or swap out sample queries between runs. Every time you add or remove a test, though, you invalidate your baseline: you cannot tell if a score changed because the agent got better or because the test suite moved. Keep your golden dataset frozen while you tune a feature, change one variable at a time, and only retire a test when you are certain the underlying requirement has changed.

![07-trap1-the-suite-moved](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/07-trap1-the-suite-moved.original.png)

Deleting tests moves the baseline, not the agent.

### **Trap 2: Relying on fuzzy 1-to-5 judge scores instead of boolean checks**

LLMs are notoriously inconsistent at grading qualitative 1-to-5 scales; the boundary between a "3" and a "4" is fuzzy and often shifts from run to run.

Whenever possible, turn your judge rubrics into **boolean (pass/fail) questions** rather than open-ended rating scales. Rather than asking *"How helpful was this answer from 1 to 5?"*, ask *"Did the agent verify the account ID before calling the refund tool? (Yes/No)"*. (We like [Adaptive Rubrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview#adaptive-rubrics)*)*

### **Trap 3: Evaluating the prose while ignoring the operational bill**

A response that passes every quality check is still a production failure if it took 40 seconds, made twelve redundant tool calls, and cost sixty cents per query.

Always evaluate the whole system rather than just the final text. Track **latency, token consumption (prompt, reasoning, and completion tokens), API cost, and tool-call counts** right alongside answer quality.

### **Trap 4: Building a different eval pipeline for a different agentic framework**

Switching orchestration frameworks often forces teams to scrap and rewrite their entire testing suite. While most frameworks emit OpenTelemetry traces, they don’t use the same semantic conventions for tool calls, steps, and tokens. Standardizing your traces around open specifications like [OpenInference](https://arize.com/glossary/openinference/) solves this by decoupling evaluation from your orchestration framework. Tools like the [**agent-eval toolkit**](https://github.com/GoogleCloudPlatform/professional-services/tree/main/tools/agent-eval) support this natively, with minimal setup.

---

## **A practical Day 0 to Day 2 rollout**

You do not need to build an observability platform from scratch. You can stand up the evaluation pipeline in a couple of hours using open-source utilities like the [**agent-eval toolkit**](https://github.com/GoogleCloudPlatform/professional-services/tree/main/tools/agent-eval) which pairs OpenTelemetry trace capture with the Agent Evaluation service on the Gemini platform (formerly Vertex AI Evaluation). But building your actual evaluation strategy requires more thought.

### **Day 0: Scenarios, simulations, and the "red pen"**

Start small and stay close to the raw data:

1. Draft scenarios covering your main CUJs and run simulations through your agent.
2. Ignore aggregate scores and read the actual execution traces from top to bottom: the prompts, intermediate reasoning steps, tool arguments, and final outputs.
3. Grade the traces with a **red pen**, marking every spot where the agent hesitated, hallucinated a parameter, picked the wrong tool, or rambled.

![04-red-pen-trace-review](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/04-red-pen-trace-review.original.png)

One agent trace, graded with a red pen.

**Why the red pen matters:** Manually reading twenty traces feels slow compared to auto-generating a chart, but it saves days of wasted effort. Instead of guessing at hypothetical failure modes and writing generic rubrics that miss the mark, an hour with a red pen shows you how your system actually breaks in reality. Aggregating those notes gives you a high-signal list of the exact deterministic assertions and boolean judge checks you need to build next.

## **Day 1: Cadence, signal, and the testing framework**

Once you have that initial list of checks, tools like [**agent-eval toolkit**](https://github.com/GoogleCloudPlatform/professional-services/tree/main/tools/agent-eval) takes over the heavy lifting and standardizes execution. Helping you with things like:

* **Scaffolding and execution:** Scaffold your golden dataset and execute multi-turn scenarios against your agent over HTTP (--`base-url`) or offline.
* **Framework-agnostic trace ingestion:** Get structured OpenTelemetry traces with OpenInference conventions, whether you build with Google ADK, LangGraph, or a custom runtime.
* **Agent Evaluation integration:** Routes those traces into the Agent Evaluation service on Gemini platform to run your deterministic checks and boolean judge rubrics without bespoke API code.

Establish a regular cadence of runs with your eval pipeline:

* **Run on every change:** Whenever you adjust a prompt, swap a model, or edit a tool docstring, execute the exact same test battery and compare the delta against your baseline.

![05-agent-eval-report-metrics-over-time](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/05-agent-eval-report-metrics-over-time.original.png)

Metrics over time in the agent-eval HTML report.

* **Validate the judge against your traces:** Never trust a new LLM-as-a-judge metric blindly. Compare the automated scores against the traces you graded by hand on Day 0. If the judge gives a passing score to a trace you marked up with red ink, tighten the grading prompt until the automated signal matches your engineering judgment.

### **The tuning loop: 50 to 60 iterations of turning knobs, not rewrites**

Once your Day 1 framework is active, optimization becomes a disciplined, mechanical loop:

![06-tuning-loop-iteration](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/06-tuning-loop-iteration.original.png)

One turn of the tuning loop on a sample agent.

In a real deployment, reaching production quality often takes 50 to 60 small iterations. You are not rewriting the entire system prompt every morning; you are gradually turning individual knobs. One tweak clarifies a tool parameter description. The next adds a negative constraint. The next adjusts the JSON output schema.

For instance, upon completion of each evaluation run, the `agent-eval` framework constructs an **interactive, all-in-one HTML report**. This report aligns pass/fail boolean metrics alongside key operational metrics, including latency, token usage, API expenditure, cache utilization, and detailed tool-call execution paths. Additionally, it incorporates automated Gemini root-cause analyses for failed conversational turns, pinpointing the exact prompt directive or parameter setting that triggered the failure to guide your next adjustment.

That data replaces hunches. A prompt change might feel much smarter in manual spot-checking, only for the test battery to reveal that latency doubled and tool-call hallucinations ticked up by 15%.

The lesson for teams building agents: **small, measured changes beat big rewrites every time.**

## **Day 2: Merge gates and shared dashboards**

Once you trust the signal coming out of your eval pipeline, turn it into a permanent regression safety net:

![08-merge-gate](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/08-merge-gate.original.png)

* **CI/CD pull request gates with headless CLI:** Execute tools like agent-eval headlessly in your build pipeline (such as Cloud Build or GitHub Actions). On every pull request, it runs your golden dataset and enforces two merge rules:

1. *A global pass threshold:* The suite must meet a minimum pass bar (for example, 95% boolean success).
2. *Zero regressions on core evaluation metrics:* Even if the overall score holds steady, the build fails if any previously passing metric regresses. This prevents developers from accidentally trading a critical capability for a minor edge-case improvement.

* **Shared dashboards and centralized storage:** Configure your eval processes to export run artifacts—including raw trace JSONL, prompt hashes, model versions, latency profiles, and scorecard summaries—into a central data warehouse like BigQuery or Cloud Storage. Publishing these metrics to a shared team dashboard gives everyone visibility into accuracy, latency percentiles, and token budgets across releases.

![09-after-launch-loop](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/09-after-launch-loop.original.png)

After launch, real production traces flow back into the golden dataset.

## **See it in action**

[Link to Youtube Video](https://www.youtube.com/watch?v=wPdoZRbvaF4)
(visible only when JS is disabled)

<https://www.youtube.com/watch?v=wPdoZRbvaF4>

* **Watch the walkthrough:** Check out our companion video, [How to Actually Evaluate (Any) AI Agent: Beyond the Vibe Check](https://youtu.be/wPdoZRbvaF4), where we build this whole pipeline live on a real LangGraph agent, in 60 minutes.
* **Grab the code:** Clone the open-source [agent-eval toolkit on GitHub](https://github.com/GoogleCloudPlatform/professional-services/tree/main/tools/agent-eval) to scaffold datasets, collect traces, and generate diagnostic HTML reports out of the box.
* [The Outer Loop, Insights First: An Ambient Quality Agent That Diagnoses Your Production Agent.](https://developers.googleblog.com/the-outer-loop-insights-first-an-ambient-quality-agent-that-diagnoses-your-production-agent/)

---

## **Frequently asked questions**

### **What are the issues with manual "vibe checks" for AI agents?**

Running three or four prompts in a terminal only shows you the final text response. An agent can loop on retries, hallucinate tool parameters, burn token budgets, or trigger duplicate side effects while still returning a polite answer. Automated trace evaluation checks intermediate tool calls, state transitions, latency percentiles, and API cost alongside answer quality so silent regressions don't ship.

### **How do I evaluate an AI agent from scratch?**

Treat evaluation as a progressive rollout from Day 0 to Day 2 rather than an all-or-nothing jump. On **Day 0**, break your critical user journeys (CUJs) into a handful of test scenarios and run them through [ADK user simulations](https://adk.dev/evaluate/user-sim/). Read those first 5 to 20 execution traces with a "red pen" to see where the agent hesitates, picks the wrong tool, or rambles.

On **Day 1**, turn those red-pen notes into automated checks so you can tune one variable at a time. Once your pass rates stabilize, lock those checks into **Day 2** CI/CD pull request gates.

### **Why use boolean (pass/fail) checks instead of 1-to-5 rating scales for LLM-as-a-judge?**

LLM judges don't grade 1-to-5 scales consistently because the boundary between a "3" and a "4" shifts from run to run. With [Adaptive Rubrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview#adaptive-rubrics), you split broad quality goals into strict Yes/No questions like *"Did the agent verify the account ID before refunding?"* Pair those boolean rubrics with deterministic [computation metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/determine-eval#computation-metrics) for tool parameters and reference checks, plus trace assertions for latency and token budgets.

### **Can I use the same evaluation pipeline across LangGraph, Google ADK, and custom agent frameworks?**

Yes, if you decouple your evaluation pipeline from your agent framework by standardizing OpenTelemetry traces on [OpenInference](https://arize.com/glossary/openinference/) semantic conventions. The open-source [agent-eval toolkit](https://github.com/GoogleCloudPlatform/professional-services/tree/main/tools/agent-eval) routes those traces straight to the Agent Evaluation service on the Gemini platform (formerly Vertex AI Evaluation). You don't have to rewrite grading code when switching orchestration frameworks.

### **What happens after my agent is deployed to production?**

Once your Day 2 pipeline exports traces and scorecards to BigQuery or Cloud Storage, you can compare live traffic against your pre-production baseline. When users hit edge cases your initial scenarios missed, [ambient quality agents like The Outer Loop](https://developers.googleblog.com/the-outer-loop-insights-first-an-ambient-quality-agent-that-diagnoses-your-production-agent/) help you diagnose those failing production traces. You can then promote those real traces straight into your Day 0 golden dataset so your test suite evolves with live usage.
