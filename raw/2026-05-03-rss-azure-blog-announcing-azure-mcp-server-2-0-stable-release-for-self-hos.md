---
source: "https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/"
title: "Announcing Azure MCP Server 2.0 Stable Release for Self-Hosted Agentic Cloud Automation"
author: "Azure Blog"
date_published: "Fri, 10 Apr 2026 17:16:10 +0000"
date_clipped: "2026-05-03"
category: "Azure & Cloud"
source_type: "rss"
---

# Announcing Azure MCP Server 2.0 Stable Release for Self-Hosted Agentic Cloud Automation

Source: https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/

We’re excited to announce the stable release of Azure MCP Server 2.0, a significant milestone for building secure and flexible agentic workflows on Azure. Azure MCP Server is open-source software that implements the Model Context Protocol specification and enables AI agents and developer tools to interact with Azure resources through a consistent, standardized tool interface.
Azure MCP currently contains 276 MCP tools across 57 Azure services, enabling end-to-end scenarios that span provisioning, deployment, monitoring, and operational diagnostics within AI-assisted experiences. The defining advancement in 2.0 is the self-hosted, remote MCP server support. Azure MCP server can now run as a remote MCP server, so you can deploy it exactly where your team builds and operates.
What is Azure MCP Server? 
Azure MCP Server is an MCP-compliant server that exposes Azure capabilities as structured, discoverable tools that agents can select and invoke. It’s designed to integrate into modern developer workflows and can be used flexibly across local development on IDEs, tool integrations, and centralized deployments, including operation as a self-hosted remote MCP server for team and enterprise scenarios, which is the primary focus of the 2.0 release.
This flexibility lets you start small on a single machine and scale to centrally managed deployments with consistent policy, security controls, and configuration.
Key updates in Azure MCP Server 2.0 
Azure MCP Server 2.0 represents a focused set of improvements that make the platform more suitable for shared deployments, stronger governance, and daily engineering workflows.
Self-hosted remote MCP server 
Azure MCP Server 2.0 is designed for remote hosting. It strengthens HTTP-based transport to support authentication scenarios and safer operational behaviors in remote mode. This enables teams to deploy Azure MCP as a centrally managed internal service and apply consistent configuration and governance.
Remote Azure MCP also supports multiple authentication approaches so you can align access with your environment and security model. For example, you can use managed identity when running alongside Microsoft Foundry . Alternatively, use an On-Behalf-Of (OBO) flow , also known as OpenID Connect delegation, to securely call Azure APIs using the signed-in user context.
Common scenarios include:
Providing shared Azure MCP access to developers and internal agent systems 
Operating Azure MCP within enterprise network and policy boundaries 
Centrally managing configuration such as tenant context, subscription defaults, and telemetry policies 
Integrating MCP-powered workflows into CI/CD and automation pipelines 
Security hardening and operational safeguards 
Security and operational safety are central design priorities in 2.0. The release includes stronger validation and safeguards intended to reduce risk in both local development and remote hosting scenarios. These improvements span endpoint validation, protections against common injection patterns for query-oriented tools, and tighter isolation controls for development environments.
Collectively, these changes are intended to make Azure MCP safer to run locally and more appropriate to host as a remote shared service.
Client compatibility and distribution options 
Azure MCP Server 2.0 continues to support a broad range of development environments and agent platforms, whether you’re working inside an IDE, interacting through a CLI, or running a standalone server. The release also expands distribution options to improve portability and simplify onboarding across MCP-compatible tools.
Performance and reliability improvements 
Azure MCP Server 2.0 includes practical upgrades that improve reliability and responsiveness in day-to-day usage, particularly in scenarios that depend on multiple MCP toolsets. Container distribution updates also reduce image size and support more efficient deployment in containerized environments.
Sovereign cloud readiness 
Azure MCP Server can be configured for sovereign cloud environments such as Azure US Government and Azure operated by 21Vianet Cloud (Azure in China), enabling use in regulated deployments that require sovereign endpoints and stronger boundary controls. This capability complements the 2.0 emphasis on self-hosting by allowing teams to deploy Azure MCP close to their required cloud environment and compliance posture.
Under the hood 
Azure MCP continues to evolve its tool ecosystem to improve usability and agent selection accuracy through clearer tool descriptions, more consistent validation logic, and consolidation of redundant operations where it improves discoverability. The intent is to provide a practical code-to-cloud operational interface that works consistently across a wide range of Azure scenarios without requiring service-specific integration patterns.
Get started and choose your experience 
GitHub Repo 
Docker Image 
Create an Issue 
Choose your experience 
Use Azure MCP as an IDE extension in the following tools for an integrated developer workflow:
Visual Studio Code 
Visual Studio 
IntelliJ 
Eclipse 
Cursor 
Use it with agent tools such as GitHub Copilot CLI and Claude Code for command-line agentic scenarios. 
Run it as a standalone local server when you want a simple, self-contained setup. 
Self-host it as a remote MCP server when you need shared access, centralized configuration, and enterprise-ready controls, which is the key capability introduced in 2.0. 
Thank you! 
Azure MCP Server 2.0 reflects continued collaboration with partners and the broader developer community. Thank you for the feedback, contributions, and real-world scenarios that shaped this release. We’re looking forward to what you build with 2.0, especially as more teams adopt self-hosted MCP servers to bring agentic workflows closer to their systems, policies, and day-to-day engineering practices.
