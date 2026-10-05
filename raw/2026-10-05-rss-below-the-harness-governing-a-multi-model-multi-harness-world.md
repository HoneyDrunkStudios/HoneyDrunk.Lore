---
"source": "https://www.docker.com/blog/below-the-harness-governing-a-multi-model-multi-harness-world"
"title": "Below the Harness: Governing a Multi-Model, Multi-Harness World"
"author": "Srini Sekaran"
"date_published": "2026-09-29"
"date_clipped": "2026-10-05"
"category": "Security & Ethical Hacking"
"source_type": "rss"
---

# Below the Harness: Governing a Multi-Model, Multi-Harness World

*We believe the future is a multi-model, multi-harness world. And we think it needs a new trust model.*

In 1988, Norm Hardy described a [problem](https://css.csail.mit.edu/6.858/2015/readings/confused-deputy.html) that had been quietly breaking systems for years: the confused deputy. A program that takes action using its permissions instead of yours.

Today, every AI agent is that deputy. It inherits your authority: Your credentials, your repo access, your ability to call APIs. But its behavior is probabilistic. It might be acting on an instruction found in its environment, on a step it invented, or on a confident wrong answer.

The industry didn’t fix the confused deputy problem by making the deputy itself more careful. They fixed it by moving its authority a layer away. Forty years on, that’s still the answer.

## Everyone is converging on the same future

Three facts are pushing the industry toward the same conclusion.

**Agents are expensive loops.**An agent takes many steps, and you pay for every token of every one. We all can agree that it makes no economic sense to call the latest frontier model for simple tasks.**The leader of frontier capability changes often.**We’re all aware that the top model of the day (and its vendor) changes every couple of months.**Your workflows may need custom models.**Many teams are recognizing that intelligence is commodifying and the differentiator is custom models, derived from custom context.

As a result, all of us are quickly ending up with a portfolio of multiple models across multiple harnesses.

A similar convergence is happening one layer up. Developers pick certain tools for the right task, the way they always have. For example, perhaps Claude Code for long refactors, Codex for daily work, Hermes for quick scripts.

It’s reasonable to expect the future of work to be multi-model and multi-harness.

## Which makes trust the defining question

A lot of agents work the same way.

They read material that is often out of our control: support tickets, web pages, documentation, and code written by strangers. But they act with authority you granted: your credentials, repo access, production APIs, and the open internet. And they usually do both from a developer’s laptop, outside typical security guardrails like VPCs and IAM.

Private data and the ability to act autonomously, together, is what makes an agent worth deploying. Your deputy needs the ability to execute in order to be useful. Which means the interesting question is no longer which model is best. It’s what happens when one of these deputies is wrong, or manipulated.

## Per-harness guardrails break down

The obvious answer is that each harness ships its own guardrails. Many do. But relied on as your security boundary, they fail in three ways.

**The agent talks past them.**Guardrails inside the harness are enforced in the same loop the agent is running. Deny it a git push and it reaches for the API. Deny the API and it opens a gist. Deny the gist and it tucks the data into a channel you trust and never inspect. Researchers showed last year that a single[malicious issue filed in a public GitHub repo](https://www.docker.com/blog/mcp-horror-stories-github-prompt-injection/)could steer a coding agent into reading a company’s private repositories and publishing the contents in a pull request the agent opened itself. Nothing was hacked since every step used the agent’s own legitimate access, through a channel everyone trusts. A boundary the agent can negotiate with is not a boundary.**The rails move without you.**Most harness’s isolation models are closed source and ship on their vendor’s schedule. The major coding agents have each revised their default sandbox and approval behavior several times in the past year alone. Updates to sandboxing models should be treated as a security event. Multiply this by ten harnesses and your security posture is, at any moment, whatever is the patchwork of your half dozen vendors’ measures.**The rails don’t cover the fleet.**The custom agent your platform team built has exactly the guardrails your platform team wrote. The agent inside your support SaaS has whatever its vendor chose, and most expose no isolation controls to you at all. Every new harness means building or auditing governance again, from scratch, differently. You end up with a dozen implementations that drift apart, each blind to the others’ traffic, with no single place to set a rule and no single record to understand why something went wrong.

Safety cannot depend on the agent making the right decision, or on someone else’s release schedule.

## A layer below

So here is what we believe. The future is multi-model and multi-agent. And given that future, we believe every organization will need a layer below: a runtime layer, *below the harness*, that all of them run on top of.

The reasoning is straightforward. Strip away the model, the vendor, and the framework, and an agent has two ways to affect anything. It runs code, which touches files and opens network connections. Or it calls a tool, which acts on a system. Everything an agent does travels one of those paths. And both paths cross the same surface: the runtime, where processes execute, credentials get used, and requests leave the machine. Every agent passes through it, no matter which model powers it, which vendor shipped it, or whether you built it yourself. That makes it the one place where rules you define can be enforced across all your agents. It is also the same fix as 1988, applied to today’s deputy: the authority sits a layer away.

Put enforcement there and each of the three failure scenarios we spoke about flips around.

**Your agents can’t talk past themselves.** The boundary for an agent sits outside the loop the agent is running, so it holds steady no matter if the model is with you, hallucinating, or compromised. A hard neutral boundary at the runtime is more effective than a prompt-level boundary the agent creates for itself.

**The rails stop moving randomly.** Policy is yours, written once, covering execution, tool calls, credentials, and spend. Now, a model or agent vendor making an update won’t randomly change your security posture.

**The rails cover your whole fleet.** A policy you write up will apply to every harness. And every action, by all your agents, lands in one record: what ran, what it touched, which rule decided.

This is what lets you be nuanced about agents. Without a boundary below your harnesses, you have three bad options: block agents completely, allow all of them and hope for the best, or wedge a manual approval into every step and give up the productivity you wanted.

A boundary at the runtime gives you a fourth option. When consequences are bounded even if an agent goes off the rails, you can start granting it true autonomy, which is the goal.

We expect models to keep changing and new harnesses to land in all of our toolkits. That part is healthy. The boundary underneath them is the part that should hold steady.

Curious what this looks like in practice? [Book 20 minutes with us](https://www.docker.com/products/ai-governance/demo/) to see how Docker AI Governance keeps that boundary steady across your fleet.

*At We Are Developers in San Jose, Tushar Jain, Docker’s CTO, will talk more about this world: multiple models, multiple harnesses, and a single runtime under it all.*
