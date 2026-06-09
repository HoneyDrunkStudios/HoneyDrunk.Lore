---
source: "https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-build-2026/"
title: "What's new in Microsoft Foundry | Build Edition | Microsoft Foundry Blog"
author: "Nick Brady"
date_published: "2026-06-02"
date_clipped: "2026-06-09"
category: "Azure & Cloud"
source_type: "web"
---

# What's new in Microsoft Foundry | Build Edition | Microsoft Foundry Blog

Source: https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-build-2026/

TL;DR 
At Build 2026, Microsoft Foundry added more of the platform pieces developers need for production agents: runtime, tools, memory, grounding, models, observability, and governance. This recap highlights what shipped, what is in preview, and where to start.
Agent development got faster: Microsoft Agent Framework adds stable orchestration building blocks, and Foundry Toolkit for VS Code is now generally available. 
Production agent hosting matured: hosted agents are expected to reach general availability by early July 2026, with sandboxed sessions, state, filesystem access, and framework flexibility. 
Agents can connect to more tools and channels: Toolboxes in Foundry is in public preview, Voice Live adds real-time voice paths, and Foundry agents can publish to Microsoft Teams and Microsoft 365 Copilot, planned for general availability in June 2026. 
Agent memory expanded: Memory in Foundry Agent Service , in public preview, now includes procedural, user, and session memory. 
Foundry IQ became a broader knowledge plane: serverless retrieval, new knowledge sources, knowledge bases, Web IQ, security updates, and agentic retrieval improvements reduce custom retrieval-augmented generation (RAG) plumbing. 
Model and compute options expanded: new MAI models, Fireworks AI on Foundry, Managed Compute, fine-tuning, and Frontier Tuning give developers more choices for inference, training, and customization. 
Trust, evaluation, and observability moved closer to the development loop: ASSERT, Agent Control Specification (ACS), Guided Guardrail Setup, Rubric, tracing, Agent Optimizer, and Agent ROI help teams evaluate, govern, and improve agents. 
Start here: what to try first 
If you only have time to try one thing, start with the row that matches your current build problem:
If you are building… 
Start with… 
Why it matters 
A production agent runtime 
Hosted agents in Foundry Agent Service 
Managed sandboxed sessions, state, filesystem access, and framework flexibility 
An agent with many tools 
Toolboxes in Foundry 
One governed endpoint for tools, skills, Model Context Protocol (MCP) clients, and enterprise data 
An enterprise knowledge experience 
Foundry IQ knowledge bases 
SLA-backed retrieval and MCP access without custom indexing glue 
A real-time voice agent 
Voice Live 
Speech recognition, text-to-speech, turn detection, interruption handling, and avatars in one API 
Agent safety and evaluation workflows 
ASSERT , ACS , and Rubric 
Policy-driven evaluations, deterministic runtime controls, and generated scoring criteria 
Model experimentation or custom inference 
Fireworks AI on Foundry , MAI models, and Managed Compute 
More model options through Azure endpoints with enterprise controls 
Explore the Build news 
Developer tools and SDKs 
The updates in Microsoft Agent Framework give developers more stable building blocks for agent applications:
Agent harness with skills, memory, and middleware , now in stable release. 
Integrations with GitHub Copilot SDK and Claude Agent SDK , now in stable release. 
Multi-agent orchestration patterns including Magentic-One , now in stable release. 
File system tools, memory tools, and the deep research agent , now in public preview. 
Foundry Toolkit for VS Code is now generally available. Use it to create agents from templates or with GitHub Copilot, debug runs locally with trace visualization, connect to Toolboxes, and deploy to Foundry Agent Service from VS Code.
Try this next: Open Foundry Toolkit in VS Code, create an agent from a template, and run it locally before deploying it to Foundry Agent Service.
Watch: Build smarter AI systems in Foundry as models and costs evolve for model selection, benchmarking, and developer workflow guidance in Microsoft Foundry.
Agents 
Build 2026 adds more of the pieces developers need to move agents from prototypes to production:
Capability 
Status 
Use when… 
Hosted agents 
Expected general availability by early July 2026 
You need managed runtime, sandboxing, state, durable filesystem access, and framework flexibility 
Routines 
Public preview 
You want an agent to run on a timer or schedule, such as overnight issue triage or daily reporting 
Toolboxes 
Public preview 
You need one managed endpoint for tools, skills, MCP clients, and governance 
Voice Live prompt agents 
Generally available 
You want the fastest path to a real-time voice experience 
Hosted voice agents 
Public preview 
You want your own runtime or orchestration framework connected to Voice Live 
Memory 
Public preview 
You want agents to retain procedural, user, or session context 
Teams and Microsoft 365 Copilot publishing 
Planned for general availability in June 2026 
You want users to access your Foundry agent where they already work 
Deploy production agents with hosted agents and routines 
Hosted agents in Foundry Agent Service , expected to reach general availability by early July 2026, provide a managed runtime for production agents. Every session runs in its own sandbox with dedicated compute, memory, and filesystem access.
The runtime is framework-agnostic, so agents built with Microsoft Agent Framework, GitHub Copilot SDK, LangGraph, or other software development kits (SDKs) can be deployed without rewrites. Two protocols are supported:
Responses API for OpenAI-compatible stateful interactions. 
Invocations protocol for schema-free, pass-through scenarios where you control the request and response format. 
Hosted agents now support long-running autonomous agents like OpenClaw and Hermes with durable state and filesystem access, and routines , in public preview, for running any agent on a timer or schedule.
Try this next: Explore the sample code with Microsoft Agent Framework , then deploy an agent to hosted agents.
Watch: From prototype to production: build and run agents at scale for the hosted-agent runtime story.
Toolboxes and skills 
Toolboxes in Foundry , in public preview, gives your agent a single managed endpoint for every tool type. Configure tools once, point any MCP client at one URL, and let Foundry handle auth, lifecycle, and governance.
Skills , in preview, are now first-class: versioned in a project-scoped catalog and discoverable as MCP resources by any agent in the project. Tool search , also in preview, helps select the right tools per task instead of surfacing every tool to the model.
Toolbox also connects to Microsoft IQ, including Work IQ in preview, Fabric IQ in preview with Fabric data agent, Ontology, and semantic models, and Foundry IQ , so agents can tap enterprise data without custom plumbing.
Try this next: Create a Toolbox, connect it to an MCP-compatible client, and test the Microsoft Agent Framework and Toolbox sample .
Watch: Turn your agents into action: Connect tools, APIs, and documents for tool, API, and Toolbox patterns.
Voice Live 
Voice Live unifies speech recognition, text-to-speech, turn detection, interruption handling, avatars, and other real-time conversational features into a single API.
For teams building with prompt agents, Voice Live is now generally available as the fastest path to adding real-time voice experiences. Existing agent capabilities, including tool calling, knowledge, memory, guardrails, and enterprise integrations, can now use low-latency speech interactions.
For teams that need full control over runtime and orchestration, hosted agents with Voice Live are available in public preview. Developers can use Microsoft Agent Framework, LangChain, or a custom stack, host on Foundry Agent Service, and connect directly to Voice Live.
Try this next: Use Voice Live with a prompt agent if you want the shortest path to voice, or pair hosted agents with Voice Live if you need custom orchestration.
Memory 
Memory in Foundry Agent Service , in public preview, now includes three types:
Procedural memory , new at Build in public preview, helps agents learn how to do the work across runs, not just what was said . Early Tau-bench results show +7–14% absolute success-rate gains at near-baseline cost . 
User memory remembers preferences and facts across sessions, such as “user is allergic to dairy.” 
Session memory maintains context within a conversation thread. 
Try this next: Enable memory on a test agent and compare task success, tool calls, and token use across repeated runs.
Publish agents where people work 
With publishing to Microsoft Teams and Microsoft 365 Copilot , planned for general availability in June 2026, any Foundry agent can be deployed directly into the tools employees already use, with identity, permissions, and policy flowing through automatically.
Try this next: Publish a low-risk internal agent to Teams, validate permissions, and then expand to Microsoft 365 Copilot.
Knowledge and grounding 
Grounding an agent in enterprise knowledge usually means building a retrieval-augmented generation (RAG) pipeline from scratch: chunking, indexing, retrieval, and a different integration for every data source.
Foundry IQ replaces that with a dedicated knowledge layer behind your Foundry agents. It unifies Work IQ, Fabric IQ, Azure SQL, File Search, and MCP sources behind one service-level agreement (SLA)-backed retrieval endpoint. Foundry IQ is available today and is wired into Toolboxes in Foundry, so agents can tap enterprise data without custom plumbing.
Foundry IQ update 
Status 
Developer action 
Foundry IQ Serverless 
Public preview 
Create a Foundry IQ resource or review the SKU documentation 
New knowledge sources 
Public preview 
Ground agents across Work IQ, Fabric IQ, File Search, Azure SQL, and MCP with a multi-source knowledge base; start with the cookbook 
Microsoft Web IQ in Foundry IQ 
Limited access 
Use live web, licensed publisher, and marketplace data when your agent needs fresh external context 
Foundry IQ knowledge bases 
Generally available 
Create an SLA-backed knowledge base and query it with the quickstart 
Agentic retrieval quality improvements 
Available 
Compare answer quality, latency, and token use with the agentic retrieval quickstart 
Security updates 
Public preview 
Test encryption, permission sync, and sensitivity-label governance with the security cookbook 
Data pipeline updates 
Public preview 
Use layout-aware ingestion, image serving, and broader SharePoint indexing when documents include more than raw text 
When your agent needs the live web, Web IQ provides sub-200 ms web grounding with zero data retention. It surfaces browse, news, web, video, and image results and is available today for select Azure customers.
Both Foundry IQ and Web IQ roll up into Microsoft IQ, the generally available intelligence layer for connecting work data, business data, and agent knowledge.
Explore Foundry IQ updates 
Watch: Foundry IQ: Fuel agents with enterprise knowledge and agentic retrieval and Build context-aware agents: From data to decisions for the grounding and IQ deep dive.
Models and compute 
New MAI models in Microsoft Foundry 
Microsoft’s MAI model family expands in Microsoft Foundry with four first-party models entering public preview at Build:
MAI-Thinking-1 , a mid-weight large language model for chat and reasoning. 
MAI-Image-2.5 , an updated image generator with image-to-image editing. 
MAI-Transcribe-2 , a speech-to-text model with speaker diarization and content biasing. 
MAI-Voice-2 , a multilingual text-to-speech model with voice cloning. 
Together, they cover the four core generative modalities: text, image, transcription, and voice.
Action: Try the new models in the Foundry catalog.
Read the announcement 
Fireworks AI on Foundry 
Fireworks AI on Microsoft Foundry is now generally available, bringing open-model inference through a single Azure endpoint with enterprise SLAs, zero-setup onboarding, no separate infrastructure, and no separate contracts.
Fireworks AI on Foundry provides day-zero access, low latency, high throughput, and support for custom-weight models. It is validated for enterprise use with provisioned throughput unit (PTU) Data Zone support and SOC 2 readiness, governed by the same access controls and audit logging as the rest of Foundry.
Action: Spin up a Fireworks endpoint from the Foundry catalog and benchmark latency, quality, and throughput against your current setup.
Explore Fireworks AI on Foundry 
Managed Compute in Foundry Models 
Use Managed Compute in Foundry Models when regional GPU capacity is the bottleneck and you want Foundry to route workloads globally without managing infrastructure.
Capacity: route around regional GPU constraints without managing infrastructure. 
Fine-tuning: spin up flexible compute for bespoke model training. 
Operations: reduce infrastructure management for model workloads. 
Action: Try Managed Compute for a workload that currently depends on capacity in one region.
Fine-tuning and Frontier Tuning 
Fine-tuning in Foundry delivers higher-quality results than prompt engineering alone, broader example coverage, token savings, and lower-latency requests on smaller models. Frontier Tuning is more than 10x more cost-efficient than GPT-5.5 on tasks like producing technical Microsoft documentation.
Action: Try the new developer tier for fine-tuning: no hosting fees, just experiment.
Watch: Post-Training and Deploying Open Source Reasoning Models in Foundry , Turn foundation models into production AI on Microsoft Foundry , and Orchestrate special agents with NVIDIA Nemotron models on Foundry for model customization and open-model deployment patterns.
Trust, observability, and security 
Build also introduced new ways to evaluate, control, and improve agents across the development lifecycle:
Capability 
Status 
Use when… 
ASSERT 
Open source 
You want to turn written policies into executable agent evaluations 
Agent Control Specification 
Open source 
You need deterministic controls at input, model, state, tool, and output checkpoints 
Guided Guardrail Setup 
Public preview 
You want recommended guardrails based on your agent’s audience, data, and use case 
Rubric evaluator 
Public preview 
You want generated, weighted quality criteria for an agent-specific scorecard 
Tracing and evaluations for any framework 
Public preview 
You need observability for agents built on LangChain, Semantic Kernel, or custom frameworks 
Agent Optimizer 
Coming soon in public preview 
You want production traces to feed ranked, reviewable improvement suggestions 
Agent ROI 
Private preview 
You need to connect agent performance to business impact 
Watch: Observe and control agents across any framework with open source tools , From observability to ROI for AI agents on any framework , and Build secure and enterprise-ready agents with Agent 365 for the trust, observability, and governance track.
ASSERT: open-source policy-driven agent evaluation 
ASSERT is Microsoft’s new framework for policy-driven agent evaluation, built on a proven Microsoft Research approach. ASSERT converts your policies into concrete, measurable evaluations, systematically generates targeted evaluation scenarios, and surfaces safety and quality defects before they reach production.
ASSERT is open source and works across LangChain, CrewAI, LightLLM, OpenAI, and more.
Resources:
ASSERT: Written intent as executable evaluations 
ASSERT on GitHub 
Action: Clone the ASSERT GitHub repository and run it against your agent’s policies.
Read the responsible AI announcement 
Agent Control Specification: an open standard 
Agent Control Specification (ACS) is an open industry specification for placing deterministic safety and security controls at five checkpoints in an agent’s lifecycle: input, large language model (LLM), state, tool execution, and output.
ACS is expressed as a portable YAML contract: versionable, auditable, and framework-agnostic. Reference implementations are available for major platforms, and the partner ecosystem at launch includes Infosys, KPMG, IBM, Aviatrix, BigSpin, and CrewAI.
Resources:
Agent Control Specification runtime governance 
Agent Control Specification 
Agent Governance Toolkit GitHub repository 
Action: Review the Agent Control Specification , then use the Agent Governance Toolkit to apply controls at checkpoints.
Read the responsible AI announcement 
Guided Guardrail Setup in Foundry Agent Builder 
Guided Guardrail Setup in Foundry Agent Builder is in public preview. A short questionnaire about your agent’s audience, data access, and use case surfaces the risks relevant to your scenario and recommends the right controls, such as personally identifiable information (PII) filters, jailbreak protection, and task adherence, with no security expertise required.
Action: Run the Guided Guardrail Setup wizard on your next agent.
Rubric evaluator 
Rubric is a new evaluator type in Microsoft Foundry, in public preview, that auto-generates evaluation criteria based on your agent’s specific context. It creates custom quality criteria from your agent definition and use case, supports weighted dimensions for aggregate scoring, and runs alongside existing safety and quality evaluators for a unified scorecard. It also feeds directly into Agent Optimizer.
Action: Generate a Rubric for your agent and replace your static benchmarks.
Read the responsible AI announcement 
Tracing, evaluations, optimization, and ROI 
Tracing and evaluations for any agent framework , in public preview, brings Foundry’s production-grade tracing and evaluations to agents built on LangChain, Semantic Kernel, or any custom framework, so no team has to choose between its stack and observability.
Agent Optimizer in Foundry Agent Service , coming soon in public preview, runs Foundry’s full evaluation suite directly within Foundry AI Operations Service and feeds results into Foundry Optimizer, closing the loop from production signal to ranked, reviewable improvements.
ROI for agents in Foundry , in private preview, measures the real business impact of your agents, including task completion rates, time saved, and cost efficiency, giving stakeholders the data they need to justify investment and prioritize what to improve.
Read the responsible AI announcement 
Resources and community 
Foundry docs: Start with the Microsoft Foundry documentation . 
Microsoft Build: Catch up on Foundry sessions in the Microsoft Build session catalog . 
Discord: Join the Foundry Discord . 
GitHub Discussions: Ask questions in the forum . 
RSS: Subscribe to get this digest monthly. 
Model catalog: Browse models in Microsoft Foundry . 
Explore the Build news
