---
"source": "https://newsletter.systemdesign.one/p/llm-evaluation-and-guardrails"
"title": "AI Evals, Guardrails & Security - A Deep Dive"
"author": "Neo Kim"
"date_published": "2026-09-19"
"date_clipped": "2026-10-05"
"category": "Security & Ethical Hacking"
"source_type": "rss"
---

# AI Evals, Guardrails & Security - A Deep Dive

[Share this letter](https://newsletter.systemdesign.one/p/llm-evaluation-and-guardrails/?action=share)& I’ll send you some rewards for the referrals.

Getting an AI system to work takes about ten minutes with a model API.

Yet knowing whether it still works after the next prompt change, model update, and/or retrieval tweak[1](https://newsletter.systemdesign.one#footnote-1) takes months of engineering that most teams never do. A chat assistant has no built-in way to detect that its answers got worse. A RAG pipeline cannot tell you that fixing one edge case broke five others. An agent cannot stop a poisoned document from steering its next action.

The system runs… But whether it runs “correctly” is a separate question.

That question has 4 parts:

*Can you measure quality repeatably before deployment?**Can you stop a bad request before it reaches the model?**Can you reconstruct what happened when something goes wrong?**Can you prove system meets the obligations*[2](https://newsletter.systemdesign.one#footnote-2)*your deployment carries?*

Evaluation, guardrails, security & observability each handle one of those parts.

Onward.

**§**

#### I’m happy to partner with [Inngest](https://inngest.link/jtH41MP) on this newsletter.

[Inngest](https://inngest.link/jtH41MP)

A few weeks back, I wrote a deep dive on how to build AI agents that can recover from failures without starting over.

[Read my guide to durable AI agents →](https://newsletter.systemdesign.one/p/durable-ai-agents)

Agents, like all of us, often need to recover from failure. But they shouldn’t start from scratch.

Inngest’s durable execution checkpoints your agents every step of the way.

So your agents can pick up where they left off and avoid doubling up on token & compute spend.

[Inngest](https://inngest.link/jtH41MP) offers a generous free tier and a sleek local dev server for testing.

**§**

I want to introduce [Louis-François Bouchard](https://louisbouchard.substack.com/) as a guest author.

He’s a best-selling author ([Building LLMs for Production](https://amzn.to/4bqYU9b)), the co-founder of [Towards AI](https://academy.towardsai.net/?ref=1f9b29), and the creator of the YouTube Channel, [What’s AI](https://www.youtube.com/@whatsai?sub_confirmation=1), where he helps people understand AI and learn how to apply it in the real world. Through his development work with clients, content, teaching, AI training programs, and the new Mentorship program at [Towards AI Academy](https://academy.towardsai.net/?ref=1f9b29), Louis focuses on making AI practical for builders, engineers, and curious learners alike.

At Towards AI, he and his team train AI engineers through courses and mentorship built for every stage, from beginner to advanced. That educational mission and the real-world experience building for his clients are exactly why I wanted him in this newsletter series.

**§**

**Here’s what you’ll find inside this newsletter:**

**Why an AI system working is different from knowing it still works.**The trust layer around your application, and how evaluation, guardrails, security, and observability work together.**How to measure AI quality before shipping a change.**Golden test sets, grader hierarchies, LLM-as-Judge, regression testing, and the metrics that change across RAG, tools, agents, and multimodal systems.**How to protect an AI system while it is running.**Input and output guardrails, tool permissions, prompt-injection defenses, data poisoning, agent security, and red teaming.**What you need to record when something goes wrong.**End-to-end traces, safe logging, drift detection, alerts, and the feedback loop that turns production failures into future regression tests.**How to build an evaluation process around your own failures.**Error analysis, failure taxonomies, metric stacks, validity gates, and controlled experiments for deciding whether a prompt, model, or retrieval change is ready to ship.

**§**

## Why You Cannot Skip This Layer

You can ship without evaluation, guardrails, or tracing…

But you *lose* the ability to tell whether the system still works once its prompts, models, data & users start changing…

Here are five properties of these systems that make that guarantee *impossible* without a dedicated infrastructure:

**The system is non-deterministic.**The same input produces different outputs on different runs, so an exact assertion cannot distinguish a valid rephrasing from a regression.**Its mistakes look like correct answers.**A wrong answer arrives as fluently as a right one. Surface quality does not indicate correctness.**Its regressions are silent.**A prompt change that fixes one case can break five others. Without a repeatable suite, this trade gets never reported.**Its inputs are not all trustworthy.**Instructions can arrive inside a retrieved document, a fetched web page, or a tool result and steer the model. There is no complete fix, only layered mitigation.**Its legal exposure depends on deployment.**Duties attach to personal data, generated media, and high-risk decisions based on how the system gets used, not which model powers it.

How much of this layer to *build* depends on what the “system” decides, not on how many people use it.

An internal meeting-note helper would need a small test set & basic tracing. Yet an internal hiring screen needs much stronger controls, because a wrong answer affects someone’s career.

**§**

## Target System Design

The trust layer has four components, each handling a different stage of the system lifecycle:

**Evaluation**grades the system before deployment, answering whether the current version is good enough to ship.**Guardrails**check every request & response at runtime.**Observability**records what happened in production & feeds failures back into the evaluation set.**Security**cuts across all three & defends against external attackers.

For these four to work together, the system needs a golden test set, repeatable offline grading, runtime checks[3](https://newsletter.systemdesign.one#footnote-3) with explicit latency budgets, and end-to-end traces that include guardrail decisions.

The evaluation pipeline also runs in CI, so a quality regression blocks the merge in the same way a failing test does…

This newsletter covers the architecture and how to use it…

All four components assume you can already tell a good answer from a bad one.

**§**

## Part 1: Evaluation

Different AI systems need different metrics.

A RAG system needs retrieval and faithfulness checks, while an agent needs tool-use and outcome checks.

A trust layer brings these metrics into one repeatable evaluation stack that answers one question:* is the system still good after the latest change?*

### Why Evaluation Has No Assert Statement

In software testing, a correct output is a known value.

In an AI system, *“is this answer good?”* depends on who is asking and which standard applies. The same answer can be correct by one rubric[4](https://newsletter.systemdesign.one#footnote-4) and unhelpful by another, so evaluation cannot be reduced to an equality check.

The way through is to match the grader to the question, a principle we’ll call the **grader hierarchy**:

When a correct answer exists, use a deterministic check: Does the JSON parse against the schema? Does the tool call carry valid arguments? Does the code run? Does the response come back under the latency cap?

Where quality is subjective, use a rubric or an LLM grader.

Where the stakes are high, use human review.


The organizing rule across all three is to use the “cheapest” grader that catches the *failure* you care about.

### From Vibe Checks to Numbers

**Vibe checking** is the informal starting point: *try prompts, read outputs, form an impression.*

It’s useful for discovering failures, but an impression cannot compare versions and/or isolate which change moved the result.

Public benchmarks help you choose a starting model… But they cannot tell you how well it would perform in your specific domain or edge cases.

A LinkedIn bot[5](https://newsletter.systemdesign.one#footnote-5) could correctly tell someone they were a terrible fit for a job. But the user needed to know which skills they lacked & how to improve. A correct answer is still a BAD answer if it does not help the user.

The numbers therefore have to come from a test set built around your own product.

### Golden Test Sets That Stay Honest

A golden test set gives you a fixed collection of cases for evaluating your AI system.

Start with 20 to 50 cases from real failures, then grow the set to around 50 to 100.

Also split the cases into three groups:

**In-scope:**Questions the system should answer.**Out-of-scope:**Questions the system should refuse.**Adversarial:**Questions designed to break the system.

You can start with synthetic cases generated from your own data.

Then replace them with real user queries as you collect production traffic, with a domain expert defining the expected behavior for each case.

Each test case should include the input, expected behavior and/or key points to check, supporting evidence, and prompt & data versions. Review each case for outdated assumptions and broken references before treating it as ground truth.

Plus a golden test set needs maintenance:

**Refresh stale cases:**Add failures & queries from production as the product changes.**Keep a holdout set:**If you repeatedly tune prompts against the same tests, you can overfit to them. Keep some cases hidden from the tuning process.

Think of the holdout set as the *final exam*: you practice with one set of problems, then test yourself on questions you have not seen before.

### Offline and Online Evaluation

Running the golden set before deployment is **offline evaluation**.

Every version answers the same questions under the same conditions, so the numbers are comparable across versions.

**Online evaluation** measures the live system on real traffic, using A/B tests, thumbs up & down, regeneration rate, and citation clicks.

Each catches what the other misses:

Offline catches regressions

*before*users see them, but only on the questions you thought to include.Online catches the cases your test set never imagined, but only

*after*real users have hit them.

Production systems run both…

Some online signals need no grader, since a click, a thumbs-down, or a regeneration is the judgment itself. Offline scoring of anything subjective still runs through an LLM grader, and the grader needs calibrating before its scores mean anything.

### LLM-as-Judge, Calibrated

A large language model (**LLM**)-as-Judge uses a model to grade AI outputs against a written rubric. To make those grades useful, choose a clear grading format.

For most evaluations:

**Use pass/fail:**Define one clear criterion for each check. Numeric scores such as 1 to 5 are harder to calibrate because the boundary between scores could be unclear.**Generate the critique first:**Ask the judge to explain its assessment before returning the verdict. This reduces the chance the explanation simply justifies a verdict chosen first.**Use pairwise grading for subjective comparisons:**When pass/ fail is too restrictive, ask the judge to compare two answers rather than assign an absolute score.**Grade outcomes for multi-step tasks:**Check each required subgoal separately. Inspect the agent’s trajectory only when a subgoal fails. Different paths could still produce equally valid results.

So choose the format that produces the *strongest* agreement with your human evaluations.

Three biases need active mitigation:

**Position bias:**The judge favors the answer it reads first. So swap the answer order across runs & average the results.**Self-preference:**A model favors outputs that match its own writing style. So use a different model family for the judge than the model you evaluate.**Verbosity bias:**Longer answers score higher than equally good shorter answers. So include length-matched pairs in your calibration set.

Calibration is not optional…

Before you trust the judge, run it on 30 to 50 human-labeled examples. Compare its verdicts with the human labels & compute agreement. Keep the judge blind to which system version produced each output.

Use one portion of the labeled examples to shape the rubric, then validate it on a held-out portion. Thirty to fifty labels are enough to start using the judge, but not enough to treat its scores as ground truth[6](https://newsletter.systemdesign.one#footnote-6).

Pick the *cheapest* model that passes calibration.

For a judge, consistency matters more than raw capability. Judge inference is cheap; collecting reliable human labels is the real cost.

### Metric Stack

The metrics you need depend on the components inside your system.

Each component adds its own evaluation layer, so you measure only what applies.

A single model call forms the base layer… Measure:

**Correctness:**Did the model produce the right answer?**Format compliance:**Did the output follow the required structure?

Retrieval-augmented generation (**RAG**) adds retrieval metrics:

**Hit rate:**Did at least one relevant chunk appear in the top K retrieved results?**Mean Reciprocal Rank**(**MRR**)**:**How high did the first relevant result rank? Higher positions receive higher scores.**Context precision:**How much of the retrieved context was relevant?**Context recall:**How much of the relevant information did retrieval find?**Faithfulness:**Did the answer stay supported by the retrieved context?**Response relevance:**Did the answer address the user’s question?

These metrics show whether RAG retrieved the right information, ranked it well, and used it to produce a relevant, supported answer.

**Tool use** adds another check: *did the model call the correct tool with the correct arguments?* This is a “deterministic” check, so it belongs in the cheapest tier of the grader hierarchy.

**Agents** need outcome-first evaluation… So grade the state the agent left behind:

*Did the refund get issued?**Did the file get written?**Did the test pass?*

Path-based grading penalizes valid alternative solutions and marks down agents that still reach the correct outcome[7](https://newsletter.systemdesign.one#footnote-7).

Also use trajectory metrics to diagnose failures:

**Step efficiency:**How many steps did the agent need?**Loop detection:**Did the agent repeat the same actions without making progress?**Tokens per task:**How many tokens did the agent spend to complete the task?

These metrics help explain a *bad* outcome…Yet they should not serve as release gates.

**Media generation**adds prompt adherence, identity preservation, artifact rates, and unsafe content rates[8](https://newsletter.systemdesign.one#footnote-8).**Voice systems**add first-audio latency & interruption success.

The rule of thumb: start with the base evaluation layer, then add metrics for each component your system uses.


### Evaluation as CI

The metric stack defines what to measure.

Continuous integration (**CI**) determines *when* to measure it.

Run the evaluation suite like unit tests:

Change the prompt/model.

Run the same evaluation suite.

Generate a scorecard.

Block the merge if critical scores fall below your release thresholds.


Use two evaluation suites for different goals:

**Regression suite:**Contains cases the system already handles correctly. Its pass rate should stay near 100%. A failed case = new version broke something the previous version handled correctly.**Capability suite:**Contains hard cases near limits of the system’s current abilities. Its pass rate should stay below 100%, so the suite continues to expose weaknesses & measure improvements.

As the system improves, more capability tests pass.

Anthropic calls the point where nearly all tests pass **eval saturation**. Once a suite approaches this ceiling, add harder tasks so the evaluation continues to reveal meaningful differences between system versions.

Two rules keep the evaluation gate reliable:

#### 1. Build most test cases from observed failures

Twenty cases from real production traces often represent actual system risks better than 100 hypothetical questions written in advance.

Yet there are 2 exceptions:

**Adversarial cases:**Tests designed to expose attacks/unsafe behavior.**Compliance cases:**Tests for requirements the system must follow.

Include these before an incident occurs… Waiting for a real security and/or compliance failure is too late…

#### 2. Run each evaluation suite three to five times per change

Model outputs vary between runs, so a two-point drop in one run could be sampling noise.

Block a release when the drop persists across repeated runs rather than reacting to a single fluctuation…

Also repeated runs produce 2 useful *reliability* metrics:

**pass@k:**At least one of*k*attempts must succeed. Use this when a person reviews the result, and retries are acceptable.**pass^k**[9](https://newsletter.systemdesign.one#footnote-9)**:**All*k*attempts must succeed. τ-bench, Sierra’s benchmark for customer-service agent tasks, introduced this metric. Use it when an agent acts without supervision.

If an unsupervised agent fails *10% of the time*, the probability of at least one failure across eight tasks is roughly *57%*.

A strong single-run score could therefore hide inconsistencies that make “unsupervised” deployment *unreliable*…

The evaluation harness measures performance on cases you anticipated & tested.

*Guardrails* cover another part of the problem by checking every input & output at runtime…

**§**

**Reminder: this is a teaser of the subscriber-only newsletter series, exclusive to my golden members.**

When you upgrade, you’ll get:

**Simple breakdown of real-world architectures**Frameworks you can plug into your work or business

**Proven systems behind ChatGPT, Perplexity, and Copilot**

*Ready for the best part?*
