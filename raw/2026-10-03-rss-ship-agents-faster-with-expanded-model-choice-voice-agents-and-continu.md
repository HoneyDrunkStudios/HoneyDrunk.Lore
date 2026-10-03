---
"source": "https://azure.microsoft.com/en-us/blog/ship-agents-faster-with-expanded-model-choice-voice-agents-and-continuous-optimization/"
"title": "Ship agents faster with expanded model choice, voice agents, and continuous\
  \ optimization"
"author": "Tina Schuchman"
"date_published": "2026-09-24"
"date_clipped": "2026-10-03"
"category": "Azure & Cloud"
"source_type": "rss"
"capture_method": "full-readable-extraction"
---

# Ship agents faster with expanded model choice, voice agents, and continuous optimization

The best model for your business will keep changing. Adopting it should move your business forward, not send your team back to rebuild the architecture around it. As models advance, organizations need the freedom to choose the right model for each workload, and an agent foundation that can evolve with those choices.

[Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) provides that model—and harness—agnostic foundation for building and running agents. Teams can adopt better models as they emerge while preserving their investments in the enterprise systems, knowledge, tools, and controls that make agents useful to their business.

Adopting a newer model is only the starting point. Foundry helps teams continuously improve their agents, using production traces to evaluate and refine instructions, skills, tools, and model choice against quality, latency, and cost. That’s the **hill-climbing** approach: observe, evaluate, optimize, validate, and repeat—with people in control

Today, we’re advancing that foundation to help teams build and continuously improve agents that deliver business value:

**Choose from a broader range of models**as frontier AI advances.**Build voice experiences and support long-running work**on the same agent foundation.**Equip agents with knowledge and tools**that help them discover and apply the right capabilities.**Turn production insights into continuous improvement**across agent quality, latency, and cost.

These advances help teams spend less time assembling infrastructure and more time building.

One customer putting these capabilities together is [Fashable](https://www.fashable.ai/), which uses Foundry’s models, agents, knowledge, and tools to help fashion brands turn trends and ideas into clothing designs, virtual try-on experiences, and campaign imagery. By connecting these workflows with the existing brands’ systems, Fashable reports cutting the time to develop new fashion products from months to weeks, with one customer reducing its budget for physical samples by 60%.

## Choose and evaluate frontier AI models in Microsoft Foundry

Frontier AI is advancing rapidly across providers. New capabilities are arriving in days, not months, and this week captures that momentum: the full **GPT-6 family from OpenAI****, including GPT-6 Sol and GPT-6 Luna, and **[ Claude Opus 5.5 from Anthropic](https://aka.ms/ClaudeOpus5.5) are now available in Microsoft Foundry. What makes this moment important is not any single model. It is the pace and breadth of innovation happening across the frontier at the same time.

For developers and enterprises, model choice is no longer a decision you make at the start of a project. It is becoming a continuous advantage. The best model for a coding agent today may not be the best model for research, customer service, or high-volume inference, and the right answer will keep changing as new models arrive. **Microsoft Foundry is built for that reality.**

Foundry brings together models from leading AI providers in an open platform where teams can evaluate them against their own data and workloads, compare tradeoffs across quality, latency, and cost, and put the right models into production without rebuilding their AI strategy around a single provider. The arrival of the GPT-6 family and Claude Opus 5.5 expands that choice, giving teams more models to evaluate for their specific workloads alongside the broader portfolio already available in Foundry.

## Build and operate voice agents with Foundry Agent Service

Voice is rapidly becoming a major way people interact with AI agents. Yet many voice experiences are still built by layering speech onto agents designed for text, requiring separate speech, orchestration, monitoring, and deployment components. With [ voice agents in Foundry Agent Service](https://aka.ms/VoicefirstagentsSept2026), voice becomes a native part of the agent foundation—built, deployed, observed, evaluated, and optimized through the same platform, API, and SDK as the rest of your Foundry agents.

Voice agents, now in public preview, are a new agent type supporting both prompt and hosted agents. Choose from industry-leading voice models— GPT Realtime, Azure Realtime, MAI and more—to balance latency, reasoning depth, and cost for each scenario, or bring your own. Models, tools, and deployment paths are designed for spoken interaction from the start: expressive voices, natural turn-taking, and graceful recovery when someone interrupts, across 80+ languages and 140+ locales. Teams that want a distinct identity can fine-tune custom speech for domain vocabulary, create a custom voice, or add a photo or video avatar for unique brand identity. Developers can reuse the tools, enterprise knowledge, and governance configured for their other Foundry agents, then deploy to web channels, Microsoft Teams, Teams Phone, and Twilio-based inbound and outbound telephony experiences.

The developer workflow extends across the tools teams already use:

**AZD AI**provides a repeatable, source-controlled workflow for configuring and deploying voice agents.**Foundry Toolkit in Visual Studio Code**(*coming soon*) enables developers to create, run, speak with, and debug voice agents without leaving their development environment.**Voice-agent observability**brings tracing, monitoring, transcripts, and voice-native evaluation to spoken interactions.

At Fashable, our mission is to make advanced AI accessible to brands and manufacturers of all sizes, regardless of their technical maturity. As we introduce new agentic capabilities, voice becomes an important part of that journey, enabling interactions that feel more natural, conversational, and accessible. People don’t think in prompts, they think in conversations, and using voice agents in Foundry with MAI-Voice helps bridge that gap.

—Orlando Ribas Fernandes, CEO, Fashable

## Build resilient hosted agents for long-running tasks

Real enterprise work does not always finish within a single request. A research task may span many sources, a report may require several tools and processing stages, and an agent may need to wait for external systems or human approval. [ Long-running resilience in Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/long-running-agent-resilience), now in public preview, lets the work of hosted agents continue after a request disconnects and recover when its hosting process stops unexpectedly.

Microsoft Agent Framework complements these capabilities with framework-level workflow state and checkpointing. When a resilient background workflow is interrupted, Agent Framework can resume from its latest durable checkpoint while Foundry preserves the hosted response.

Microsoft Agent Framework also adds Agent Channel for messaging integrations, AG-UI support for interactive applications, CodeAct and Hyperlight containers for isolated code execution, and episodic procedural memory to reuse successful task patterns. [Read more](https://aka.ms/MAFSept2026) about the latest updates in Microsoft Agent Framework.

To build and deploy these long-running agents, developers can use the Foundry Toolkit for Visual Studio Code, which supports hosted agents and Microsoft Agent Framework. The new [ Foundry dev pack](https://aka.ms/DevpackSept2026) simplifies onboarding by bringing the Foundry developer toolchain together in one installer.

## Give agents only what they need, when they need it

Enterprise agents don’t need every document, tool, and procedure in every interaction. Loading everything upfront adds latency and cost, and can make behavior harder to predict. Agents should be able to find and use the resources they need as the work unfolds.

give agents on-demand access to tools and reusable procedures, with opt-in discovery and tool-level guardrails. Teams can make capabilities available without loading them into every call. Toolboxes are already generally available for hosted agents and are now expanding to prompt agents in public preview.[Toolboxes](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/toolbox?pivots=vscode), now generally available, lets agents find the right tool without loading the full catalog of tool definitions upfront. In an[Tool search](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/tool-search?pivots=python)in Toolboxes[internal evaluation](https://commandline.microsoft.com/tool-search-toolboxes-foundry/)using a[public benchmark](https://arxiv.org/abs/2503.01763)of more than 44,000 tools and 7,000 queries, tool search reduced input-token consumption by more than 60% for a 50-tool toolbox and by over 97% for a 1,000-tool toolbox. These results are compared with a prompt-cached baseline that loads the full tool catalog upfront., now generally available, lets agents call other agents, including other Foundry agents, through an open, standardized protocol. Teams can connect agents without building custom point-to-point integrations, while centralized credentials and policy enforcement help maintain security and governance as those systems grow.**Agent-to-Agent (A2A)**, now generally available, let teams run automated agents on a schedule, after a delay, or in response to an event. Teams no longer need to build their own schedulers, queues, and identity plumbing just to start an agent at the right time.[Routines](https://devblogs.microsoft.com/foundry/from-chatbots-to-automated-assistants-routines-in-microsoft-foundry-are-now-generally-available/)in Foundry Agent Service

Together, these capabilities help teams reduce unnecessary context and custom infrastructure, with more control over what agents can access and when they run.

## Turn production evidence into continuous improvement

Getting an agent into production is just the beginning. As real users put it to work, teams need to understand what’s driving quality, latency, and cost, and which changes will improve performance without introducing regressions. That has often meant piecing together traces, dashboards, and ad hoc tests. Foundry brings those steps into a continuous improvement loop, helping teams turn production insights into measurable improvements: observe, understand, evaluate, optimize, validate, and repeat.

[Insights in Foundry](https://aka.ms/ObservabilitySept2026), now in public preview, helps teams understand what is happening in production. It analyzes production traces to surface recurring issues and ones teams didn’t know to look for. For each issue, it gathers the supporting evidence, points to the likely cause, and recommends what to do next, so teams know where to focus before a small problem becomes a widespread one.

[Rubric evaluator](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rubric-evaluators), generally available later this month, helps teams define what good looks like once they know what to fix. It turns an agent’s prompts, traces, and requirements into clear success criteria that can be measured consistently.[Synthetic and traces](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/traces-to-dataset?tabs=python)to dataset generation, generally available later this month, builds the evaluation data to match those criteria. Traces to dataset generation draws on real production traffic, so tests reflect the scenarios customers actually encounter, including the ones Foundry insights flagged.[Agent optimizer](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-optimizer-overview)in Foundry Agent Service, generally available later this month, puts those evaluations, datasets, and constraints to work. It tests changes across instructions, tools, skills, and model choice, and shows which changes actually improve results before anything ships.

Together, these capabilities close the loop from production back to production. The improved agent returns to real traffic, where Foundry insights keep watching for what comes next, and each pass builds on the last so agents keep getting better the longer they run.

Agent optimizer in Foundry Agent Service turns evaluation insights into actionable datasets and optimization, reducing the manual effort of finding and fixing performance issues. That systematic loop aligns directly with NTT DATA’s AgentOps with Harness approach—a core element of our Smart AI Agent® concept—together moving agents from proof of concept to trusted production at scale.

—Takashi Okamoto, AI Technology Strategist, Global AI Office, NTT DATA Group Corporation

## Govern AI agents with identity, lifecycle, and network controls

As agents take on more work, organizations need to manage them as enterprise assets, with identities, owners, policies, lifecycle controls, and evidence of what they did.

**Foundry agents now honor governance operations originating in Microsoft Entra and Agent 365. **Actions such as blocking, disabling, deleting, restoring, or assigning a new owner are enforced by the Foundry runtime rather than recorded only in a directory.

[Network egress controls](https://aka.ms/EgresscontrolsSept2026) govern the outbound destinations a hosted agent can access. Teams can define allow and deny rules, modify outbound headers, or redirect requests before traffic leaves the Foundry-managed sandbox. An audit mode enables teams to evaluate policies before enforcement, with each decision emitted to Azure Application insights.

Coming soon in October, Microsoft Foundry is expanding its integration with Azure API Management with preview support for the new **AI Gateway tier**, helping organizations bring centralized governance into the Foundry developer experience. With this integration, organizations can adopt a **hub-and-spoke approach** where platform teams centrally govern model access through AI Gateway and make approved models available to developers through **Admin Connected Models**. Developers can then use these governed models across familiar Foundry experiences for model discovery, experimentation, agent development, and evaluation. Developers will also be able to connect to models across other resources or outside of Foundry directly from the playground. Existing Foundry integration with traditional Azure API Management tiers will remain supported.

Governing agents as enterprise assets also means proving they meet the organization’s safety and policy requirements. The new [open-source run-assert-eval Skill](https://aka.ms/ASSERT-ACS-Clarity-Sept2026) brings that verification into a single workflow.

It runs three of Microsoft’s open-source tools in sequence:

[Clarity](https://github.com/microsoft/clarity-agent)surfaces risks developers may have missed.

[ASSERT](https://github.com/microsoft/ASSERT)turns requirements into measurable evaluations.

[Agent Control Specification (ACS)](https://github.com/microsoft/agent-governance-toolkit/tree/main/policy-engine)applies targeted runtime controls where an agent falls short.

The Skill then re-runs the evaluation to confirm the agent improved without restricting legitimate behavior, giving teams evidence that each policy is working as intended.

## Get started with Microsoft Foundry

The latest capabilities in Microsoft Foundry give developers a flexible path from a simple prompt to a production agent, without requiring teams to assemble disconnected development tools, runtimes, gateways, schedulers, and governance controls.

**Start building:**Head to[ai.azure.com](https://ai.azure.com/)to build your next agent in Microsoft Foundry. Choose a model, define the agent’s instructions, and connect the knowledge and tools it needs.**Learn with the community:**Join[Model Mondays](https://aka.ms/model-mondays)and[Foundry Fridays](https://aka.ms/model-mondays/discord)for demos and practical guidance. Next up:[Agent Optimizer and insights in Foundry Session](https://discord.com/events/1113626258182504448/1542207383823196290/1553096245248000000)**Join us at Microsoft Ignite:**Visit[Microsoft Ignite](https://ignite.microsoft.com/)to explore sessions on AI and agents and opportunities to connect with experts.
