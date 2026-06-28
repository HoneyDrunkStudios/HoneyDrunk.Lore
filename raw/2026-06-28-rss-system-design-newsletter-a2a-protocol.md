---
source: "https://newsletter.systemdesign.one/p/agent-to-agent-protocol"
title: "A2A Protocol"
author: "Eric Roby"
date_published: "2026-06-26"
date_clipped: "2026-06-28"
category: "Software Architecture"
source_type: "rss"
---

# A2A Protocol

Source: https://newsletter.systemdesign.one/p/agent-to-agent-protocol

A2A Protocol - Deep Dive #158: How AI agents collaborate to solve complex tasks Eric Roby and Neo Kim Jun 26, 2026 ∙ Paid 48 8 Share Get my system design playbook for FREE on newsletter signup:
Subscribe Share this post & I’ll send you some rewards for the referrals. 
AI agents can use tools 1 today. 
Model Context Protocol ( MCP ) provides an agent with a standard way to communicate with databases, APIs, files, and external services. 
But there’s a problem MCP doesn’t solve:
What happens when you need many agents to work together? 
Onward.
Build stronger data foundations for “agentic AI” at scale Building an AI demo is EASY.
Building production-ready agentic AI systems that scale across an enterprise is extremely “difficult”.
That’s exactly what senior enterprise leaders from AWS, Prudential Insurance, Siemens, GAF, and HF Sinclair discuss in this virtual panel: how to build resilient, scalable data foundations and production-ready AI agents. 
Here’s what you’ll learn: 
Scale AI beyond the proof of concept. Build industrial-scale systems with classical and generative AI. 
Fix the data problem. Power AI with governed, high-quality data. 
Make better architecture decisions. Choose the right databases for AI applications. 
Streamline deployment. Discover, procure, and deploy AI solutions with AWS Marketplace. 
Watch the AWS panel for free right now and see how enterprise leaders are building AI systems with speed, governance, and control. 
Watch AWS Virtual Panel for FREE 
(Thanks to AWS for partnering on this post.) 
I want to introduce Eric Roby as a guest author. 
He’s a senior backend and AI engineer focused on building real-world systems and teaching developers how to do the same. He runs the YouTube channel codingwithroby , where he focuses on scalable backend architecture and integrating AI into production applications. 
Through his content and courses, he helps engineers go beyond tutorials, think in systems, and develop the skills that actually matter for senior-level roles.
Find him on:
LinkedIn 
Substack 
Here’s what’s inside this newsletter: 
Why MCP wasn’t enough. The missing coordination layer that prevents AI agents built by different vendors and frameworks from working together. 
How AI agents actually collaborate. Agent Cards, task lifecycles, delegation, streaming, discovery, and the protocol that standardizes agent-to-agent communication. 
The emerging AI interoperability stack. How A2A, MCP, RAG, AGNTCY, ACP, and AP2 fit together, and why the industry is converging around open standards. 
Where A2A breaks down in production. Latency, trust, authorization, debugging, observability, and the engineering tradeoffs you’ll face when building multi-agent systems. 
A practical guide to building with A2A. Security, Agent Card design, interoperability, production architecture, and the patterns that make agent ecosystems reliable at scale. 
Get Instant Full Access Now 
(Golden members get all letters like these!…) 
💡 Quick refresher
AI agent is a system that uses a large language model 2 ( LLM ) to reason, plan, and take actions on your behalf. It’s not just answering questions. But also calling tools, checking results, and deciding what to do next. Think of it as an LLM with hands. 
A single agent can be brilliant at one job…
They can write code, analyze data, and schedule meetings. But real work crosses domains. And you need one agent to code, one to test, and one to ship. If you stack all of this into one mega-agent, it becomes slow, expensive, and brittle.
i.e., specialization wins, just as it does on a real team…
But then, what is Agent-to-Agent ( A2A ) protocol? 
Can’t agents already communicate through normal API calls? 
The problem is every agent-to-agent integration becomes custom: one agent needs to know what another agent can do, what inputs it expects, how to authenticate, how to hand off a task, how to track status, how to pass context, and how to receive the final result.
A2A is an emerging open standard for the coordination layer…
It gives agents a shared way to advertise their capabilities, accept tasks, exchange messages, report progress, and return outputs.
i.e., A2A standardizes the workflow in which one agent delegates work to another.
Imagine A2A as the next connection layer:
TCP/IP 3 lets machines talk to each other 
HTTP lets documents link to each other
APIs let services compose into systems
MCP lets agents connect to tools
A2A does the same thing for agents
Google launched A2A in April 2025.
(They partnered with 50+ tech companies and service providers. 150+ organizations joined them later.)
To understand why A2A matters, you need to understand the pain it solves… 
Share 
AI Agent Collaboration Problem AI agents are exponentially growing…
Every team, every vendor, every platform is shipping them…but each one is a SILO.
Your customer relationship management ( CRM ) agent can’t coordinate with your internal data agent. Your coding agent can’t delegate to a testing agent built by a different team. They might all live in the same company, in the same building, on the same network… 
Yet they still can’t work together.
Framework 4 lock-in is part of the problem. 
An agent built with LangGraph can’t directly communicate with one built with CrewAI, Google’s ADK, or AutoGen. Each framework has its own internal orchestration model. While cross-framework collaboration requires custom glue code, written and maintained by you.
That's where A2A comes in.
Now let’s look at what it is… 
What A2A Actually Is Here’s a simple analogy for you: 
Think of A2A like hiring a contractor. You don’t need to know what tools are in their truck or how they manage their schedule. You hand them a job; they confirm what they can do, and then hand back the finished work. A2A is the standard contract format. This lets any contractor work with any client. They don’t need to renegotiate from scratch each time.
The Agent2Agent ( A2A ) protocol is an open standard. 
It helps AI agents find each other’s skills 5 . They can send messages, delegate tasks, and work together safely. This all happens NO matter their framework, vendor, or platform. 
Here are five design principles on which the A2A v1.0 specification is built:
Simple. Reuse existing, well-understood standards. HTTP, JSON-RPC 2.0, Server-Sent Events. No new transport layer to learn. 
Enterprise Ready. Address authentication, authorization, security, privacy, tracing, and monitoring by aligning with established enterprise practices. 
Async First. Designed for long-running tasks and human-in-the-loop interactions. Quick queries to deep research that takes hours or days. 
Modality Agnostic. Support text, audio, and video via file references, structured data, and forms, and embedded UI components. 
Opaque Execution. Agents work together by sharing their skills and information. They don’t need to reveal their internal thoughts, plans, or how their tools work. 
The last one is the most important.
A2A treats agents as autonomous, opaque entities. You don’t need to share your agent’s internals to participate in the ecosystem.
Now let’s open the hood… 
Share 
How A2A Works Under the Hood Here are the key points you should understand:
How agents connect,
What they share,
And how they communicate.
Let’s dive in!
Client-Server Model and Agent Discovery Every A2A interaction has two roles:
Client agent is the requester. It discovers remote agents, sends tasks, and coordinates the workflow. 
Remote agent is the executor. It receives and processes tasks, does the work, and returns results. 
Any agent can play both roles, depending on the workflow.
A coding agent is a client when it delegates testing to a QA agent. The same coding agent becomes a remote agent when a project manager agent asks it to write code. 
Agents discover each other through an Agent Card . 
This JSON metadata document is published by every A2A server 6 . It describes the agent’s identity, capabilities, skills, endpoint URL, supported data formats, and authentication needs. 
Agent Cards live at a standard, well-known URI: /.well-known/agent-card.json . 
The path follows RFC 8615 7 . This is the same way browsers find SSL verification files. A client agent checks another agent’s card. It does this to see what the agent can do before sending requests. 
This is like MCP’s capability negotiation 8 , but for agents instead of tools. 
Here’s what an Agent Card includes:
Name, description, version
Service endpoint URL
Supported input and output modalities, as MIME types
Skills, with IDs, descriptions, tags, and examples
Authentication requirements, aligned with OpenAPI security schemes
Supported A2A features like streaming, push notifications, and extended cards
Agents can also serve an Extended Agent Card behind authentication. 
This lets you hide sensitive skills or internal capabilities from unauthenticated discovery. i.e., public-facing summary first, full details after you prove who you are.
Tasks, Messages, and Artifacts Communication in A2A is task-oriented.
When a client agent sends a message, the remote agent creates a Task . This is the fundamental unit of work in A2A. Plus, every task has a unique ID and progresses through a defined lifecycle . 
Here are 9 possible lifecycle states:
submitted : task received by the remote agent 
working : agent is actively processing 
input-required : agent needs more information from the client 
auth-required : agent needs credentials or authorization to proceed 
completed : task finished successfully (terminal) 
failed : task could not be completed (terminal) 
canceled : task was canceled by the client (terminal) 
rejected : agent decided not to perform the task (terminal) 
unknown : state recovery scenario 
This is fundamentally different from a simple function call.
Tasks are stateful and can involve many message exchanges. They can also pause to ask the client for more information…Or pause to request authorization before doing anything destructive.
This is the kind of back-and-forth a real collaboration requires…
Messages are the units of communication between agents. Each message has a role (user or agent) and contains one or more Parts. 
Parts are the smallest content units. Text parts hold plain text. While File parts hold files or images via URI or inline bytes. And Data parts hold structured JSON. This supports rich, multimodal communication without forcing everything into text. 
Artifacts are the outputs of a task. Documents, images, structured data, or any other deliverable remote agent produces. Artifacts, like messages, consist of Parts. They can be streamed as they are created. 
Contexts group related tasks together via a contextId . This provides continuity across a series of interactions, similar to a conversation thread. 
Communication Patterns and Protocol Bindings Before we get into transport details, there are two orchestration patterns to understand: 
Centralized orchestrator . One lead agent owns the plan. It discovers specialist agents, delegates tasks, and stitches the results back together. This makes it easier to reason about and debug. The default pattern for most enterprise workflows today. This is the “tech lead delegates to ICs” model. 
Decentralized swarm . No single orchestrator. Agents find each other directly and share tasks. Each agent chooses whom to contact next based on its own judgment. More flexible. More resilient. Harder to trace. Closer to a marketplace or a team of peers. 
A2A supports both.
It’s a protocol, not an orchestration model. The protocol just defines how any two agents talk. The topology is your choice. Most real systems begin centralized. They switch to swarm patterns 9 when they can see well and have trust systems to handle complexity. 
Plus A2A supports three interaction patterns at the network level:
Synchronous request-response. Client sends a message and waits for a complete response. Good for quick tasks. 
Streaming via Server-Sent Events. Server streams incremental updates in real-time. Good for tasks where you want to show progress. 
Push notifications. Server sends async updates to a client webhook 10 . Good for long-running tasks where the client doesn’t want to hold a connection open. 
And for the actual wire protocol, A2A v1.0 supports three bindings:
JSON-RPC 2.0 11 : original and most commonly used binding. Methods include message/send, message/stream, tasks/get, tasks/cancel, and others. 
gRPC : added for high-performance scenarios. Uses Protocol Buffers for message serialization. 
HTTP REST : uses standard HTTP verbs and URL patterns like /v1/message:send and /v1/tasks/{id} . Lowers the barrier for teams that prefer REST over JSON-RPC. 
All three bindings share the same semantic model and abstract operations.
The choice of binding is a deployment decision, not a design one. As of v1.0, the protocol’s main data model is in Protocol Buffers 12 ( a2a.proto ). This file is the single source of truth. All bindings derive from this definition. 
This familiarity with existing web standards is intentional.
A2A works with your current enterprise setup. It connects easily to load balancers, API gateways, and observability tools. No new tools are needed!
Now that you understand how A2A works, the obvious question: how does it relate to MCP? 
Reminder: this is a teaser of the subscriber-only newsletter series, exclusive to my golden members. 
When you upgrade, you’ll get:
High-level architecture of real-world systems. 
Deep dive into how popular real-world systems actually work.
How real-world systems handle scale, reliability, and performance. 
Unlock Full Access Now 
Ready for the best part?
A2A vs MCP: Complementary, Not Competing Keep reading with a 7-day free trial Subscribe to The System Design Newsletter to keep reading this post and get 7 days of free access to the full post archives.
Start trial Already a paid subscriber? Sign in Previous A guest post by Eric Roby Senior Backend & AI Engineer passionate about teaching others. Subscribe to Eric
