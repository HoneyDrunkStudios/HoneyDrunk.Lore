---
source: "https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/"
title: "Announcing the Agentic Resource Discovery specification"
author: "unknown"
date_published: "2026-06-17"
date_clipped: "2026-06-19"
category: "AI / LLM Research & Tooling"
source_type: "web"
---
# Announcing the Agentic Resource Discovery specification

JUNE 17, 2026

Agents are becoming participants in a much larger ecosystem. They increasingly rely on tools, skills, and other agents distributed across teams, organizations, and platforms.

For this ecosystem to scale, agents need reliable answers to three questions: **Where does the right capability live? Which capability should I actually use? And how do I verify it’s safe to connect to?**

Today, there is no standard way to answer those questions across organizations.

That’s why we’re announcing **Agentic Resource Discovery (ARD)**, an open specification for publishing, discovering, and verifying AI capabilities across the web. Developed with partners across the industry, ARD allows tools and services to be securely shared and connected, regardless of their underlying framework, protocol, or provider.

Consider an operations agent investigating a live production incident. To resolve the issue, it might need to query observability systems, search engineering documentation, review deployment history, open support tickets, and maybe even consult specialized troubleshooting agents.

While many platforms already feature custom registries to manage these capabilities, they remain fragmented and siloed within specific ecosystems. This lack of interoperability prevents agents from easily communicating across different tools. What’s missing is a standard way for agents to discover capabilities across organizational boundaries and establish trust in what they find.

ARD provides that layer. It standardizes how capabilities are published under an organization's own domain name and indexed across federated registries, enabling any agent to dynamically find the right resources for the job. From there, ARD steps out of the way – handing off the verifiable trust metadata so the agent can establish a direct, secure connection using the tool's native protocol.

This architecture relies on two primitives: **catalogs** and **registries**.

**Catalogs:**To make resources discoverable, an organization publishes a catalog describing its available capabilities. Because these catalogs are hosted directly under the organization’s own domain, ownership of that domain serves as the cryptographic foundation for identity and trust.**Registries:**Registries act as search engines for the agentic web. They crawl published catalogs, index their contents, and make them searchable. When an agent submits a discovery request, a registry returns matching capabilities along with the metadata required to verify the publisher and establish trust before connecting.

The video below demonstrates an ARD client discovering and executing new capabilities entirely at runtime. Watch for these four key phases in the terminal window:

**Publishing the catalog:**The provider hosts an ai-catalog.json file at a well-known path on its domain. The catalog describes the provider's available capabilities, which can include things like MCP servers, A2A agents, OpenAPI tools, or even other nested catalogs.**Discovery and resolution**: When a client agent needs a capability, it can either query an ARD registry using a plain-language intent (which can actively crawl and index these catalogs), or it can completely bypass search and directly fetch a catalog from a known partner's domain.**Cryptographic verification:**For production environments, the discovery layer allows publishers to attach verifiable trust metadata. Whether found via search or direct fetch, this enables the client agent or registry to actively confirm the publisher's true cryptographic identity before connecting to the endpoint.**Direct runtime connection:**The client agent dynamically loads the selected capability, interacts with it using its native protocol or API, and returns the result to the user.

Just as the open web democratized information, ARD democratizes AI resource discovery. Google Cloud supports this with Agent Registry in Gemini Enterprise Agent Platform – the enterprise-grade product that delivers on this vision and forms part of this global federated network.

Agent Registry ensures enterprises can trust, govern, and operationalize that promise at scale. It provides fully hosted support for searching, discovering, and hosting agentic resources, including agents, skills, MCP servers and other tools. Additionally, it allows users to onboard these capabilities directly onto Agent Registry, and it will soon support authenticated publisher onboarding.

Importantly, Agent Registry plays a central role in enterprise governance. This includes assigning globally unique namespaced URNs, enforcing agentic egress policies, and pinning tools and specifications. It also handles secure resource management using Agent Identity to verify the trust manifest – ARD’s cryptographic layer for proving agent authenticity and meeting enterprise compliance standards like HIPAA.

Native support for ARD will be available in Agent Platform in the coming months, allowing organizations to securely connect their internal registries to the broader network.

The ARD specification is available now. To get involved:

**Publish your first catalog:**Follow the quickstart guide to host an`ai-catalog.json`

file on your domain and make your services discoverable in minutes.**Read the specification:**Check out the specification, including full schemas, federation model, trust architecture, and reference implementations.**Join the community:**Contribute implementations, propose schema updates, and participate in the evolution of ARD by visiting our GitHub repository.

The agent ecosystem works best when it is decentralized and open. ARD is our contribution to keeping it that way. We’d love your feedback – and your catalog!

The Agentic Resource Discovery specification is licensed under Apache 2.0 and is built upon the foundational AI Catalog data model. We are grateful to the AI Catalog Working Group under the Linux Foundation, as well as the launch partners who helped shape the specification and reference implementations.
