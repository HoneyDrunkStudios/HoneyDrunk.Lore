---
source: "https://www.docker.com/blog/a-new-security-baseline-for-enterprise-agentic-adoption/"
title: "A new security baseline for enterprise agentic adoption"
author: "Docker Blog"
date_published: "2026-08-12"
date_clipped: "2026-08-17"
category: "Security & Ethical Hacking"
source_type: "web"
---

# A new security baseline for enterprise agentic adoption

Source: https://www.docker.com/blog/a-new-security-baseline-for-enterprise-agentic-adoption/

A new security baseline for enterprise agentic adoption
Posted Aug 12, 2026
Eli Aleyner
and
Ranti Familusi
Agent Baseline is a blueprint for AI adoption that defines six security outcomes for putting enterprise agents to work without giving them unchecked authority.
Consider this scenario: a customer-support agent receives a ticket with an attachment. Hidden inside the attachment is an instruction: query the customer database and send the results to an external address.
The agent has everything it needs to comply. It can read tickets, query internal systems, call tools, and connect to the internet. The instruction is malicious, but it looks like part of the work.
What stops the agent before customer data leaves the company?
That is the practical security problem enterprises face as agents move from experiments into daily operations. The problem is not only whether a model can recognize a malicious instruction. It is whether the systems around the model limit what the agent can reach, what authority it can use, and what actions it can take when the model gets the decision wrong.
Agents turn familiar controls into a new systems problem
Enterprises already know how to manage identities, isolate workloads, restrict networks, test software, collect logs, and respond to incidents. Those controls remain necessary.
Agents change how the controls must work together. An agent can be reprogrammed at runtime through natural-language instructions. It can choose how to pursue a goal, call tools, use delegated credentials, and spawn other agents. Its effective capabilities may change as models, prompts, tools, MCP servers, and permissions change.
A coding agent illustrates the problem. Give it a bug to fix and it may read source code and internal documentation, install packages, call an external API, delegate tasks to sub-agents, and commit a change. Each step may be reasonable on its own. The risk emerges from the combination: one runtime-programmable actor moving across systems under delegated authority, faster than a person can review every decision.
Security teams therefore need to answer three questions about every agent:
What is operating, and what can it do?
Is it staying inside approved boundaries?
If something goes wrong, can we prove what happened and stop it?
Most organizations can answer parts of these questions. Far fewer can answer them for one agent, one task, and one run across every model, tool, credential, policy decision, and downstream action
Enter the Agent Baseline: an open blueprint for building, operating and governing enterprise agents.
Agent Baseline was created by Docker, Snyk and Keycard to define the minimum security outcomes an enterprise agent deployment should meet.
The current v1.0 draft contains 35 controls across six outcomes :
Discover: Maintain an accurate record of every agent, its owner, purpose, components, dependencies, and effective access.
Constrain: Limit the agent’s runtime, data, tools, network reach, compute, and duration to what its approved purpose requires.
Authorize: Bind consequential actions to a distinct identity, task, target, scope, and period of validity.
Observe: Connect intent, identity, policy, tool use, actions, and outcomes with a stable run or trace ID.
Validate: Test the agent in the configuration and environment in which it will operate, then verify its outputs and outcomes.
Respond: Stop the agent, revoke its authority, quarantine affected components, preserve evidence, and determine impact.
We officially launched the Agent Baseline  at Black Hat 2026 , to a full house during the event Securing your AI Agent: The Road to Software Factory.  If you’re curious to hear how it went, check the video below:
Eli Aleyner, VP of Strategy, Docker
The Agent Baseline in Practice
Here is how the baseline contains the support-ticket incident:
“Discover” establishes what is at risk. The agent registry identifies the agent’s owner and purpose, the model and tools it is actually running, the database it can query, the credentials it may use, and any downstream agents it can call. This is current runtime evidence, not the configuration approved six months ago.
“Constrain” blocks the path out. The agent runs inside an isolated environment with a capability profile built for customer support. Its filesystem access is limited. Its network policy denies unapproved destinations by default. When it attempts to reach the external address, the request fails and generates evidence instead of quietly succeeding.
“Authorize” limits the value of compromised access. The agent does not carry a standing credential with broad database rights. It receives short-lived authority tied to the customer-support task, the permitted records, and the allowed action. If it delegates work, the downstream agent cannot receive more authority than the original agent held.
Together, “ Constrain” and “Authorize” make the blast radius measurable, which is far better done before an incident than during one. A compromised run reaches in three directions: what it can execute and touch on the host, what identity it can prove and use, and what it can connect to outside. Each direction has a control that shrinks it.
The blocked request and the odd query land under one run ID. That is “ Observe” : correlated evidence, so the story does not have to be pieced together from five logs a week later. And none of it was a surprise, because “ Validate” had already tested this agent against prompt injection in the configuration it actually runs in.
“Respond” contains it. The run is stopped and its active grants revoked, the evidence is preserved, and the affected customer records are scoped so the team knows exactly what the run reached. Essential tickets keep moving through an approved manual fallback while the investigation runs.
None of this depends on the model behaving. Most teams already run three or four of these controls; the usual gap is that they do not connect, so one fires in one place and the evidence lands somewhere else.
Securing organizations in the decade of agents
Agents can accomplish a wide range of tasks. A single agent can navigate seamlessly through the inner and outer loops of development, go through PRDs, write code, commit it, and ultimately push changes to production, much like a human engineer. It also has the ability to do that incredibly fast, using different tools, and creating sub-agents that work in parallel, leveraging the same tools and authentication of the original agent.
Agent governance has become a recurring requirement in our work with customers. They want the productivity of coding agents without giving those agents unchecked access to developer machines, credentials, source code, and external services.
This led to the development of Docker Sandboxes , microVM sandboxes that run AI agents securely, and Docker AI Governance , a centralized control layer for managing what AI agents can access and do across an organization. These new products, along with the existing Docker MCP Gateway and Docker Hardened Images now give organizations of all sizes an underlying infrastructure with which to manage agentic risk.
Read more about Agent Baseline:
We published Agent Baseline v1.0-draft on July 30, 2026, and presented it at Securing Your AI Agent: The Road to the Software Factory during Black Hat USA 2026. You can watch the session on demand on the link below.
The draft is open for community review until September 30, 2026. We are looking for implementation feedback, missing controls, evidence that a control is ineffective, and cases where a requirement creates disproportionate operational burden.
Download the white paper here
Visit agentbaseline.org and contribute your comment to the architecture
Agents will keep gaining access and autonomy. The standard cannot be that they behave perfectly. The standard must be that we know what they can do, enforce where they can go, trace what they did, and stop them when something goes wrong.
Partnerships
security
Partnerships
Table of contents
Related Posts
Jul 30, 2026
The Future of Agentic AI Depends on Openness and Trust. That’s Why Docker Is Joining Nvidia’s Open Secure AI Alliance.
Docker joins NVIDIA’s Open Secure AI Alliance to help build the security, governance, and trust frameworks that agentic AI systems demand.
Tushar Jain
Read now
Aug 12, 2026
Docker VMM Public Beta: A Complete Overhaul, Built for Performance
Docker VMM is now available in public beta for Mac and Windows. Learn what this means for performance, stability, and governance and how to try it yourself.
Deanna Sparks
and
Colin Hemmings
Read now
Aug 12, 2026
A new security baseline for enterprise agentic adoption
Agent Baseline is a blueprint for AI adoption that defines six security outcomes for putting enterprise agents to work without giving them unchecked authority. Consider this scenario: a customer-support agent receives a ticket with an attachment. Hidden inside the attachment is an instruction: query the customer database and send the results to an external address….
Eli Aleyner
and
Ranti Familusi
Read now
Docker Captain
Aug 5, 2026
Governance Is a Developer Experience Problem
Learn why AI governance is about more than security. Discover how trust, clear boundaries, and developer experience enable AI adoption at scale.
Karan Verma
Read now
