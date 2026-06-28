---
source: "https://www.docker.com/blog/whats-next-for-mcp-security/"
title: "What’s Next for MCP Security?"
author: "Jim Clark and Justin Cormack"
date_published: "2025-05-06"
date_clipped: "2026-06-28"
category: "Security & Ethical Hacking"
source_type: "web"
---

# What’s Next for MCP Security?

Source: https://www.docker.com/blog/whats-next-for-mcp-security/

Securing Model Context Protocol: Safer Agentic AI with Containers
Posted May 6, 2025
Jim Clark 
and
Justin Cormack 
Model Context Protocol (MCP) tools remain primarily in the hands of early adopters, but broader adoption is accelerating. Alongside this growth, MCP security concerns are becoming more urgent. By increasing agent autonomy, MCP tools introduce new risks related to misalignment between agent behavior and user expectations and uncontrolled execution. These systems also present a novel attack surface, creating new software supply chain threats. As a result, MCP adoption raises critical questions about trust, isolation, and runtime control before these systems are integrated into production environments.
Where MCP tools fall short on security 
Most of us first experimented with MCP tools by configuring files like the one shown below. This workflow is fast, flexible, and productive, ideal for early experimentation. But it also comes with trade-offs. MCP servers are pulled directly from the internet, executed on the host machine, and configured with sensitive credentials passed as plaintext environment variables. It has been like setting off fireworks in your living room: it’s thrilling, but it’s not very safe.
{
"mcpServers": {
"command": "npx",
"args": [
"-y",
"@org/mcp-server",
"--user", "me"
],
"env": {
"SECRET_API_KEY": "YOUR_API_KEY_HERE"
}
}
}
As MCP tools move closer to production use, they force us to confront a set of foundational questions:
Can we trust the MCP server? 
Can we guarantee the right software is installed on the host? Without that baseline, reproducibility and reliability fall apart. How do we verify the provenance and integrity of the MCP server itself? If we can’t trace where it came from or confirm what it contains, we can’t trust it to run safely. Even if it runs, how do we know it hasn’t been tampered with — either before it reached us or while it’s executing?
Are we managing secrets and access securely? 
Secret management also becomes a pressing concern. Environment variables are convenient, but they’re not secure. We need ways to safely inject sensitive data into only the runtimes permitted to read it and nowhere else. The same goes for access control. As teams scale up their use of MCP tools, it becomes essential to define which agents are allowed to talk to which servers and ensure those rules are enforced at runtime.
Figure 1: Discussions on not storing secrets in.env on Reddit . Credit: amirshk 
How do we detect threats early?  
And then there’s the question of detection. Are we equipped to recognize the kinds of threats that are emerging around MCP tools? From prompt injection to malicious server responses, new attack vectors are already appearing. Without purpose-built tooling and clear security standards, we risk walking into these threats blind. Some recent threat patterns include:
MCP Rug Pull – A malicious MCP server can perform a “rug pull” by altering a tool’s description after it’s been approved by the user. 
MCP Shadowing – A malicious server injects a tool description that alters the agent’s behavior toward a trusted service or tool.  
Tool Poisoning – Malicious instructions in MCP tool descriptions, hidden from users but readable by AI models. 
What’s clear is that the practices that worked for early-stage experimentation won’t scale safely. As adoption grows, the need for secure, standardized mechanisms to package, verify, and run MCP servers becomes critical. Without them, the very autonomy that makes MCP tools powerful could also make them dangerous.
Why Containers for MCP servers 
Developers quickly realized that the same container technology used to deliver cloud-native applications is also a natural fit for safely powering agentic systems. Containers aren’t just about packaging, they give us a controlled runtime environment where we can add guardrails and build a safer path toward adopting MCP servers.
Making MCP servers portable and secure  
Most of us are familiar with how containers are used to move software around, providing runtime consistency and easy distribution. Containers also provide a strong layer of isolation between workloads, helping prevent one application from interfering with another or with the host system. This isolation limits the blast radius of a compromise and makes it easier to enforce least-privilege access. In addition, containers can provide us with verification of both provenance and integrity. This continues to be one of the important lessons from software supply chain security. Together, these properties help mitigate the risks of running untrusted MCP servers directly on the host.
As a first step, we can use what we already know about cloud native delivery and simply distribute the MCP servers in a container. 
{
"mcpServers": {
"mcpserver": {
"command": "docker",
"args": [
"run", "-i", "--rm",
"org/mcpserver:latest",
"--user", "me"
],
"env": {
"SECRET_API_KEY": "YOUR_API_KEY_HERE"
}
}
}
}
But containerizing the server is only half the story. Developers still would need to specify arguments for the MCP server runtime and secrets. If those arguments are misconfigured, or worse, intentionally altered, they could expose sensitive data or make the server unsafe to run. 
In the next section, we’ll cover key design considerations, guardrails, and best practices for mitigating these risks.
Designing secure containerized architectures for MCP servers and clients 
Containers provide a solid foundation for securely running MCP servers, but they’re just the beginning. It’s important to consider additional guardrails and designs, such as how to handle secrets, defend against threats, and manage tool selection and authorization as the number of MCP servers and clients increases. 
Secure secrets handling 
When these servers require runtime configuration secrets, container-based solutions must provide a secure interface for users to supply that data. Sensitive information like credentials, API keys, or OAuth access tokens should then be injected into only the authorized container runtimes. As with cloud-native deployments, secrets remain isolated and scoped to the workloads that need them, reducing the risk of accidental exposure or misuse.
Defenses against new MCP threats 
Many of the emerging threats in the MCP ecosystem involve malicious servers attempting to trick agents and MCP servers into taking actions that conflict with the user’s intent. These attacks often begin with poisoned data flowing from the server to the client.
To mitigate this, it’s recommended to route all MCP client traffic through a single connection endpoint, a MCP Gateway, or a proxy built on top of containers. Think of MCP servers like passengers at an airport: by establishing one centralized security checkpoint (the Gateway), you ensure that everyone is screened before boarding the plane (the MCP client). This Gateway becomes the critical interface where threats like MCP Rug Pull Attacks, MCP Shadowing, and Tool Poisoning can be detected early and stopped. Mitigations include:
MCP Rug Pull : Prevents a server from changing its tool description after user consent. Clients must re-authorize if a new version is introduced. 
MCP Shadowing : Detects agent sessions with access to sets of tools with semantically close descriptions, or outright conflicts. 
Tool Poisoning : Uses heuristics or signature-based scanning to detect suspicious patterns in tool metadata, such as manipulative prompts or misleading capabilities, that are common in poisoning attacks. 
Managing MCP server selection and authorization 
As agentic systems evolve, it’s important to distinguish between two separate decisions: which MCP servers are trusted across an environment, and which are actually needed by a specific agent. The first defines a trusted perimeter, determining which servers can be used. The second is about intent and scope — deciding which servers should be used by a given client.
With the number of available MCP servers expected to grow rapidly, most agents will only require a small, curated subset. Managing this calls for clear policies around trust, selective exposure, and strict runtime controls. Ideally, these decisions should be enforced through platforms that already support container-based distribution, with built-in capabilities for storing, managing, and securely sharing workloads, along with the necessary guardrails to limit unintended access.
MCP security best practices 
As the MCP spec evolves, we are already seeing helpful additions such as tool-level annotations like readOnlyHint and destructiveHint.  A readOnlyHint can direct the runtime to mount file systems in read-only mode, minimizing the risk of unintentional changes. Networking hints can isolate an MCP from the internet entirely or restrict outbound connections to a limited set of routes. Declaring these annotations in your tool’s metadata is strongly recommended. They can be enforced at container runtime and help drive adoption — users are more likely to trust and run tools with clearly defined boundaries.
We’re starting by focusing on developer productivity. But making these guardrails easy to adopt and test means they won’t get in the way, and that’s a critical step toward building safer, more resilient agentic systems by default.
How Docker helps   
Containers offer a natural way to package and isolate MCP tools, making them easier and safer to run. Docker extends this further with its latest MCP Catalog and Toolkit , streamlining how trusted tools are discovered, shared, and executed.
While many developers know that Docker provides an API for containerized workloads, the Docker MCP Toolkit builds on that by enabling MCP clients to securely connect to any trusted server listed in your MCP Catalog. This creates a controlled interface between agents and tools, with the familiar benefits of container-based delivery: portability, consistency, and isolation.
Figure 2: Docker MCP Catalog and Toolkit securely connects MCP servers to clients by running them in containers 
The MCP Catalog, a part of Docker Hub, helps manage the growing ecosystem of tools by letting you identify trusted MCP servers while still giving you the flexibility to configure your MCP clients. Developers can not only decide which servers to make available to any agent, but also scope specific servers to their agents. The MCP Toolkit simplifies this further by exposing any set of trusted MCP servers through a single, unified connection, the MCP Gateway. 
Developers stay in control, defining how secrets are stored and which MCP servers are authorized to access them. Each server is referenced by a URL that points to a fully configured, ready-to-run Docker container. Since the runtime handles both content and configuration, agents interact only with MCP runtimes that are reproducible, verifiable, and self-contained.   These runtimes are tamper-resistant, isolated, and constrained to access only the resources explicitly granted by the user. Since all MCP messages pass through one gateway, the MCP Toolkit offers a single enforcement point for detecting threats before they become visible to the MCP client. 
Going back to the earlier example, our configuration is now a single connection to the Catalog with an allowed set of configured MCP server containers. MCP client sees a managed view of configured MCP servers over STDIO. The result: MCP clients have a safe connection to the MCP ecosystem!
{
"mcpServers": {
"mcpserver": {
"command": "docker",
"args": [
"run", "-i", "--rm",
"alpine/socat", "STDIO", "TCP:host.docker.internal:8811"
],
}
}
}
Summary 
We’re at a pivotal point in the evolution of MCP tool adoption. The ecosystem is expanding rapidly, and while it remains developer-led, more users are exploring ways to safely extend their agentic systems. Containers are proving to be the ideal delivery model for MCP tools — providing isolation, reproducibility, and security with minimal friction.
Docker’s MCP Catalog and Toolkit build on this foundation, offering a lightweight way to share and run trusted MCP servers. By packaging tools as containers, we can introduce guardrails without disrupting how users already consume MCP from their existing clients. The Catalog is compatible with any MCP client today, making it easy to get started without vendor lock-in.
Our goal is to support this fast-moving space by making MCP adoption as safe and seamless as possible, without getting in the way of innovation. We’re excited to keep working with the community to make MCP adoption not just easy and productive, but secure by default.
Learn more 
Check out the MCP Catalog and Toolkit product launch blog   
Get started with Docker MCP Catalog and Toolkit 
Join the webinar for a live technical walkthrough. 
Visit our MCP webpage   
Subscribe to the Docker Navigator Newsletter . 
New to Docker? Create an account .  
Have questions? The Docker community is here to help . 
About the Authors
Jim Clark
Principal Software Engineer, Docker
Justin Cormack
CTO, Docker
Open source, cloud, technology, NetBSD, unikernels, work @docker
AI/ML 
Docker 
MCP 
Products 
Table of contents 
Related Posts
May 12, 2026 
Docker AI Governance: Unlock Agent Autonomy, Safely
Introducing Docker AI Governance: centralized control over how agents execute, what they can reach on the network, which credentials they can use, and which MCP tools they can call, so every developer in your company can run AI agents safely, wherever they work. Your laptop is the new prod Agents are the biggest productivity unlock…
Srini Sekaran 
Read now 
Jun 26, 2026 
What Does EU AI Act Compliance Require?
Learn what EU AI Act compliance requires at each risk tier, key deadlines through 2027, and how engineering teams can operationalize AI governance.
Dan Stelzer 
and
Monique Altman 
Read now 
Jun 25, 2026 
How to Generate an SBOM for Container Workflows
Learn when, where, and how to generate SBOMs for container images. Covers build-time vs. post-build approaches, quality criteria, and CI/CD integration.
Aditya Tripathi 
Read now 
Jun 25, 2026 
EU Cyber Resilience Act: Overview, Requirements, and Timelines
Learn what the EU Cyber Resilience Act requires, including SBOM mandates, vulnerability reporting, and compliance deadlines for container teams.
Dan Stelzer 
and
Monique Altman 
Read now
