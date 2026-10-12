---
source: "https://www.thoughtworks.com/insights/articles/context-challenge-ai-agents"
title: "Why context is the real bottleneck for AI agents"
author: "Gaurav Patole"
date_published: "2026-10-01"
date_clipped: "2026-10-12"
category: "Software Architecture"
source_type: "rss"
---

# Why context is the real bottleneck for AI agents

## The missing link in autonomous decision-making

Your AI agent can have access to the right data, produce a perfectly plausible answer and still make a terrible decision. This is the emerging risk of agentic AI: the context problem.

As your organization delegates more complex work to autonomous systems, the growing challenge is whether your agent understands what that information means inside your business: which definition applies, which exception matters, whose judgment to trust and when a rule should be broken. Put simply, context is the knowledge that makes AI trustworthy.

While the technology to store context – semantic layers, ontologies and repositories – already exists and is maturing at a great pace, the real challenge lies in extracting, encoding and verifying it. Context spans multiple dimensions, from technical context (schemas, databases and pipelines) to policy-level context (governance rules and compliance policies). But the most elusive layer is business context. This is the organizational secret sauce: the unwritten tribal knowledge, informal definitions and on-the-ground logic that employees – like a financial analyst interpreting market metrics – rely on daily to drive value.

[Decades of underinvestment in data foundations](https://www.thoughtworks.com/perspectives/edition39-agentic-ready-data-strategy) mean most organizations have failed to put these knowledge layers into practice. The result is employees losing trust in the very tools built for them, reverting instead to unwritten tribal knowledge or asking a colleague to double-check a sales figure before hitting publish.

Capturing business context for agentic systems requires organizations to embrace a new operating model. This is already top-of-mind for most leaders: in [Thoughtworks’ recent global survey](https://www.thoughtworks.com/insights/reports/global-cio-survey-2026) of 3,200 CIOs, 89% of them agreed that they are now more responsible for redesigning workforce workflows and labor models than for managing core IT infrastructure. True agentic readiness requires employees to evolve from passive “data consumers” into active “context providers”. Evolving this capability needs to be a collective effort across the entire data value chain – engaging leadership, system owners, data engineers, business users and end consumers.

## The high stakes of “half-truths”

The danger of clean but context-poor data is that it presents AI agents with “half-truths”. Unlike hallucinated errors that are obvious to the human eye, half-truths blend accurate facts with subtle context gaps. When key context is missing, an AI agent connects the dots using pure logic – coming up with a plan that looks great on paper, but leads to real-world disaster in practice.

Take the case of [PocketOS](https://www.theguardian.com/technology/2026/apr/29/claude-ai-deletes-firm-database). An AI coding agent was working on a routine task in a test environment when it encountered a permission error. To “fix” the problem, it found a valid API token and used it to issue a wipe command to clear the blocker. However, what the agent didn’t know was that the token held blanket access to live systems. In just nine seconds, it deleted the company’s production database and all its backups.

However, simply inserting a “human-in-the-loop” doesn’t solve the problem. Because half-truths produce outputs that look completely rational on the surface, catching the flaw requires people who genuinely understand the business context; someone who knows the hidden insights and tricks-of-the-trade that were never written down. Without that tacit knowledge, human oversight becomes a rubber stamp, leaving systems exposed to automated mistakes.

## Why tribal knowledge gets locked away

Failing to give agents proper context carries high stakes. Yet capturing tribal knowledge remains notoriously difficult because the primary obstacles are cultural rather than technical. Human behavior, political dynamics and organizational silos all cause institutional knowledge to be either guarded or permanently lost.

Among these barriers is a clear incentive problem. Domain experts are asked to give away the very knowledge that makes them indispensable while hearing leadership announce that AI will “streamline” the workforce. The result is predictable: employees withhold information out of a rational fear of self-obsolescence.

Knowledge can also be withheld by design. Internal competition can lead business units to treat context as leverage, prompting teams within the same organization to isolate their insights from one another. In other cases, knowledge hoarding can be a legal or ethical obligation – such as when delivery teams working with competing clients must maintain strict confidentiality boundaries.

Capturing context also fails when it becomes an administrative burden. Companies often rely on brute force – mandating exhaustive forms, schema mapping and manual logs – which turn a valuable curation exercise into a low-priority chore. Without a seamless way to capture context in real time, decades of unwritten knowledge, edge-case solutions and legacy context can simply walk about the door when senior employees retire or leave.

Decades of IT outsourcing work have also left businesses wondering about the expertise needed to build, learn and scale context internally. As a result, when teams are tasked with feeding AI systems or reviewing their outputs, they often lack the unwritten, operational context required to guide these systems.

Finally, some expertise is inherently difficult to document. In hyper-specialized domains – such as oncology or stock market trading – knowledge is largely tacit and intuitive. Even though medical guidelines or financial frameworks are widely available, these professionals make critical decisions based on experience and deep pattern recognition honed over decades, making their knowledge difficult to extract and encode.

## The challenges of verifying context

Giving AI agents the right context is only half the battle. Organizations face another hurdle: verifying that captured context is factually correct, up to date and aligned across systems.

Data silos force different teams to maintain duplicate records, creating competing versions of “truths”. This is a common “Excel trap”, where departments rely on isolated spreadsheets as their ultimate authority. When these sources contradict one another, an agent has no way to verify which source holds the correct facts.

Different business units can also operate on conflicting definitions. For example, Finance and Sales may define an “active customer” or “net revenue” in completely different ways. Without a single owner to own these definitions, AI agents cannot determine which department’s rules or definitions to trust.

This verification challenge is worsened by the absence of a unified context layer. As organizations operate across multi-cloud and multi-vendor ecosystems, context naturally gets locked inside these vendor environments. For instance, context defined in Databricks stays within Databricks, while context stored in Salesforce gets isolated within the CRM. Because these systems lack a shared context layer, data cannot be cross-referenced or verified in real-time as it flows across the business.

## The solution: context lifecycle management

Context needs an accountable owner in the same way production data products do. Achieving this requires moving away from static, one-time documentation projects toward a continuous context management capability – one that establishes end-to-end governance, traces lineage, assigns ownership and continually updates context as business realities change.

Moving to this new operating model does not require a multi-year, enterprise overhaul. Success comes from starting small, focusing on specific business goals and executing across three foundational pillars: people, processes and technology.

### Start with the outcome and work backwards

Start with a specific business outcome you want the agent to achieve and work backward to map the exact context required. For example, if you are building an AI agent for financial reporting, limit your scope to the data, definitions and workflows that a specific agent needs to execute its task.

### People: ownership and adoption

### 

* **Assign clear ownership:** Establish clear department-level accountability for business definitions and context verification rather than defaulting to IT. For instance, business line owners must own business context, while compliance, legal and security teams own policy-level context.
* **Build psychological safety:** Reframe the AI narrative to address job security concerns. Position agents not as a workforce replacement but as “eager interns” shadowing domain experts. Employees need to guide and train the AI with their knowledge so it can better support their daily work.

### Processes: lineage, data products and streamlined workflows

### 

* **Ensure end-to-end traceability:** Establish clear lineage for every agent decision. When an agent produces a wrong decision, teams must be able to trace the output directly back to the exact context source, allowing them to correct it immediately.
* **Build agent-ready data products:** Prepare your data so that it’s safe for AI agents to interact with. Data products solve specific business needs and are built with the same discipline applied to product engineering: start from the job to be done, work back to the data that serves it and package it into well-governed, safely managed assets for AI agents – read more on getting your [data ready for agentic AI](https://martinfowler.com/articles/making-data-ready-for-agentic-ai.html).
* **Streamline curation workflows:** Instead of extracting knowledge as a one-off exercise, embed it directly into daily operations. Traditional means like table-column level descriptions, business glossaries and wiki pages that require manual input aren’t scalable with the increasing number of AI agents within an enterprise. One idea is to enable features like conversational AI agents where employees interact naturally with the agent to answer questions like “what was the customer’s issue?” and “how did you solve it?”. The conversational AI feeds this context back into the core context layer automatically, capturing on-the-ground knowledge with minimal friction.

### Technology: semantic layers

### 

* **Invest in semantic and ontology tooling:** Context stays consistent only when business definitions live in one governed place rather than being recreated inside every tool that needs them. The capability to aim for is a shared semantic layer: business definitions, entity relationships and the logic behind key measures, captured once as a governed and reusable asset, and ported through open interfaces so that analytics, applications and agents all resolve to the same meaning rather than inventing their own. Several categories of tooling are converging on this such as data catalogs, semantic layers and lakehouse metadata platforms (Databricks Unity Catalog Semantics, Collibra, Atlan, etc.), though they are still maturing to become an enterprise-wide reality.

A word of caution, though: a semantic layer is the foundation, not the finished house. This tooling makes context available and consistent; it does not, on its own, make it correct. It can hold a definition of "active customer," but it cannot decide which of four competing definitions is the right one, or notice when that meaning quietly drifts. That still takes people. So treat the investment as the technical backbone of your context strategy, essential but only as valuable as the human ownership and curation you build around it.

## The context advantage

An organization today might deploy a single agent. Soon, it will run hundreds or even thousands simultaneously executing complex workflows – making the context problem a choice between multiplying business value or compounding costly real-world failures.

To prepare for this reality, organizations need to embrace a new operating model that treats context not as an administrative chore, but as a living operational asset. By starting with targeted business outcomes, building psychological safety and embedding context lifecycle management into everyday processes, organizations can break down data silos and mitigate the risk of automated errors.

Ultimately, the winners in the agentic era will be those who can systematically transform institutional knowledge into a single, verifiable source of truth – creating a reliable foundation for autonomous agents to act on.
