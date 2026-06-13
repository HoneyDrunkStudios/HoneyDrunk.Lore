---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-azure-container-apps-sandboxes-secure-infrastructure-for-agentic-wor/4524131"
title: "Introducing Azure Container Apps Sandboxes: Secure Infrastructure for Agentic Workloads | Microsoft Community Hub"
author: "unknown"
date_published: "2026-06-02"
date_clipped: "2026-06-12"
category: "Azure & Cloud"
source_type: "web"
---

11 MIN READ

# Introducing Azure Container Apps Sandboxes: Secure Infrastructure for Agentic Workloads

[vyomnagrani](/users/vyomnagrani/1396352)

Microsoft

Jun 02, 2026

Today we are announcing the public preview of **Azure Container Apps Sandboxes** - a new first-class resource type that gives you fast, secure, ephemeral compute environments with built-in suspend and resume. This is the underlying infrastructure on which products like [Cloud sandboxes in GitHub Copilot](https://docs.github.com/copilot/concepts/about-github-sandbox?utm_source=mike-hulmes-build-blog-github-sandbox-docs-cta&utm_medium=blog&utm_campaign=msbuild-2026), [Foundry Hosted Agents](https://aka.ms/HostedAgents-blog), and [Azure Container Apps Express](https://aka.ms/aca/express/launch-blog) are built, you now have the opportunity to build your solutions leveraging this infrastructure.

Azure Container Apps Sandboxes unlocks two massive opportunities. For platform developers and ISVs, sandboxes give you the same isolated compute fabric that powers many Microsoft products. You get the building blocks to create your own multi-tenant platform on proven, enterprise-scale infrastructure. For AI agents, sandboxes become a self-configurable tool that lets agents extend their own capabilities on the fly. An agent can spin up a fresh sandbox in milliseconds and use it to execute untrusted code, compile source, test HTTP requests against a live app, launch a browser session, or tackle whatever needs a quick and scalable infrastructure.

On one side it empowers humans to build platforms, on the other it empowers agents to build their own capabilities. Both get enterprise-grade isolation, instant startup, and snapshot-based persistence out of the box.

We'll walk through the resource model, sandbox lifecycle, the features that set Sandboxes apart - like snapshots, lifecycle policies, network egress controls, volumes, and managed identities - and show you how to get started with the portal and CLI.

# What Are Container Apps Sandboxes?

Container Apps Sandboxes are secure, isolated compute environments that start in sub-second time, scale to thousands, and cost nothing when idle. Each sandbox runs in its own hardware-isolated microVM boundary - fully separated from the host, the platform, and every other sandbox. You bring your own Open Container Initiative (OCI) image, and Sandboxes handle the rest: provisioning from prewarmed pools, strong multi-tenant isolation, and snapshot-based suspend/resume that preserves full memory and disk state across sessions.

There are many ways Sandboxes can help you build your next project - here are a few:

- Your own build & test systems - wire a Sandbox into your CI/CD flow to run builds while your laptop stays cool.
- Agents that can run anything safely - an agent spawns a sandbox, executes work inside it, and returns the output with no agent host privileges required.
- Agent swarms - decompose a research question, spawn N sandbox workers in parallel (each pinned to its own image and egress policy), and synthesize the result.

Early access customers are already unlocking significant benefits by leveraging Azure Container Apps Sandboxes.

> *"With Azure Container Apps sandboxes, SitecoreAI can safely enable agents to take real action. The combination of multi-tenant isolation, rapid scale-out, and full automation allows Sitecore to run long-lived, autonomous agents that securely execute code, manage workflows, and interact with enterprise systems within secure, governed environments.*
>
> *With this foundation, we can build agents that do real work: assembling content, personalizing experiences, and optimizing campaigns in production. Agents that operate continuously, learn from results, and improve over time, so our customers get better outcomes without giving up control."*
>
> - Mo Cherif, VP of AI and Innovation, [Sitecore](https://www.sitecore.com/)

> *"We got early access to Azure Container Apps Sandboxes, and got the first prototype integrated with Atlas AI in hours, and it's already shaping a new Atlas AI capability that we plan to launch in preview in Q3.*
>
> *It gives every Atlas AI agent a safe, sandboxed workspace (file system, terminal, code execution) on a customer's live data in Cognite Data Fusion. The value: Industrial process, reliability, and production engineers spend days and weeks on questions like "which wells are underperforming and why?" These questions are tractable but expensive, so they are asked rarely and decisions are made on gut feel. With this, an agent pulls the data, runs the analysis, cross-references maintenance and inspection records, and returns a cited draft in minutes. Sandboxes make it practical: Aligned feature set, per-customer isolation, pause/resume across multi-day investigations, scale-to-zero economics."*
>
> - Kelvin Sundli, Product manager, Atlas AI, [Cognite](https://www.cognite.com/)

## Resource Model: Sandbox Groups and Sandboxes

The top-level ARM resource is *Microsoft.App/SandboxGroups*. A Sandbox Group is the management boundary for a collection of sandboxes that share configuration - think of it like a Container Apps Environment, but purpose-built for sandboxes.

When you create a Sandbox Group, you specify:

- **Subscription**, **Resource Group**, and **Region**
- **Sandbox defaults** (optional): default CPU, memory, disk, max sandbox count, and default idle timeout
- **Networking**: optionally deploy into a custom VNet with a dedicated subnet for private networking
- **Identity**: System or user assigned Entra identity.

Individual sandboxes are created within a Sandbox Group. Each sandbox has its own source (disk image or snapshot), resource tier, lifecycle policy, network egress policy, environment variables, ports, volumes, and connections.

## Sandbox Lifecycle

Sandboxes have a well-defined lifecycle with the following states:

|  |  |
| --- | --- |
| **State** | **Description** |
| **Creating** | Provisioning the sandbox from a disk image or snapshot |
| **Running** | Actively executing - backed by a live microVM |
| **Idle** | System-suspended after inactivity; can auto-resume on the next request |
| **Suspended** | Full state (memory + disk) preserved as a snapshot; no compute costs |
| **Resuming** | Restoring from a suspended or idle state - sub-second for most workloads |
| **Stopped** | User-initiated stop; can be resumed |
| **Stopping** | Graceful shutdown in progress |
| **Deleting** | Teardown in progress |

The key insight here is the distinction between **Idle** and **Suspended**. When a sandbox goes idle (e.g., no traffic for a configured timeout), the system can automatically suspend it and capture a snapshot. When a new request arrives, the sandbox resumes transparently. This gives you scale-to-zero economics with stateful compute - something that wasn't possible before without significant custom engineering.

## Disk Images: Bring Your Own Container

Sandboxes boot from **Disk Images** - Open Container Initiative (OCI) images converted into an optimized root filesystem format. You point to any OCI image (public or private registry), and the platform builds a bootable disk image from it.

You can start with public, pre-built images maintained by the platform (for example, Ubuntu base images), or bring your own private images. For private registries, you can authenticate with username/token or use a **user-assigned managed identity** for Azure Container Registry (ACR) – integrated with Azure as you expect.

## Snapshots: Full-State Persistence

Snapshots capture the complete state of a running sandbox - memory, disk, and all running processes. When you resume a sandbox from a snapshot, every process, open file handle, and in-memory data structure is restored exactly as it was.

A snapshot captures the full state of a running sandbox: memory pages, disk, processes. Two ways to make one - automatically on suspend, or manually on demand. Three things they're great for:

- Checkpointing mid-task so a long-running agent can resume exactly where it left off
- Cloning an environment that's already warm - dependencies installed, caches populated, services running
- Shipping a "ready-to-go" state that resumes in sub-second instead of cold-booting

Snapshots are **free during the preview**, after which they will be stored as Azure Blob Storage at [standard rates](https://azure.microsoft.com/pricing/details/storage/blobs/). Each snapshot records the source sandbox, resource allocation (CPU, memory, disk), and container metadata - so what you get back is exactly what you snapshotted.

## Resource Tiers

Every sandbox is assigned to a resource tier that determines its CPU, memory, and disk allocation:

|  |  |  |  |
| --- | --- | --- | --- |
| **Tier** | **CPU** | **Memory** | **Disk** |
| **XS** | 0.25 vCPU | 0.5 GB | 5 GB |
| **S** | 0.5 vCPU | 1 GB | 10 GB |
| **M** (default) | 1vCPU | 2 GB | 20 GB |
| **L** | 2 vCPU | 4 GB | 40 GB |
| **XL** | 4 vCPU | 8 GB | 80 GB |

When creating a sandbox from a snapshot, the resource tier is inherited from the snapshot and cannot be changed - this ensures the restored environment has the exact resources it was running with when the snapshot was taken.

## Lifecycle Policies: Auto-Suspend and Auto-Delete

Every sandbox can be configured with lifecycle policies that automate state transitions and cleanup:

**Auto-Suspend**

- **Idle timeout**: How long a sandbox can sit idle before being suspended (configurable: 1m, 2m, 5m, 10m, 30m, 60m)
- **Suspend mode**:
  - **Disk + Memory** (default): Full snapshot including memory state - resume picks up exactly where you left off, with all processes and in-memory data intact.
  - **Disk**: Only the disk is preserved; the VM restarts fresh on resume. Useful when you only need file persistence, not process continuity.

**Auto-Delete**

- Automatically delete sandboxes after a configurable number of days of inactivity
- Prevents accumulation of abandoned sandboxes that consume snapshot storage

These lifecycle policies are what make Sandboxes economically viable at scale. A platform serving thousands of tenants can configure aggressive idle timeouts (say, 60 seconds) with Memory suspend mode, and each tenant's sandbox disappears from the billing meter almost immediately - but resumes in sub-second time the moment they return.

## Network Egress Policy

For scenarios involving untrusted code - AI agents executing LLM-generated scripts, multi-tenant SaaS with user-submitted workloads - controlling outbound network access is critical. Sandboxes provide a per-sandbox Network Egress Policy:

- **Default action**: Allow or Deny all outbound traffic
- **Host rules**: Domain-pattern rules (e.g., \*.github.com → Allow) to permit specific destinations
- **Custom CIDR rules**: Network-level rules for IP ranges (e.g., 10.0.0.0/8 → Deny)
- **Skip egress proxy**: Option to bypass the egress proxy entirely when custom VNet routing handles policy enforcement

This means you can run a sandbox in a **deny-by-default** posture and allowlist only the specific endpoints it needs (your API server, a package registry, etc.) - without setting up NSGs or firewall appliances.

## Managed Volumes: Persistent and Shared Storage

Sandboxes support two types of mountable volumes, both managed by Microsoft:

|  |  |  |
| --- | --- | --- |
| **Volume Type** | **Backed By** | **Best For** |
| **Managed Azure Blob** | Azure Blob Storage | Shared data across sandboxes, file uploads/downloads, persistent artifacts |
| **Managed Data Disk** | Azure Disk Storage | High-performance storage for databases, build caches, large working sets - only available to one sandbox at a time |

Blob volumes come with a built-in file explorer in the portal - you can browse, upload, download, create folders, and drag-and-drop files directly. Data Disk volumes provide dedicated block storage with configurable sizes.

## Secrets and Identity

**Secrets**

Sandbox Groups support key-value secrets scoped to the group. Secrets can be created, edited, and referenced by sandboxes within the group. These secrets can be used in egress policies to modify requests with transform or header-injection rules, without exposing the secrets to code running inside the sandbox.

**Managed Identity**

Sandbox Groups support both system-assigned and user-assigned managed identities, with full RBAC role assignment management. This means your sandboxes can authenticate to Azure services (Key Vault, Storage, Cosmos DB, etc.) without managing credentials - the same identity model you use everywhere else in Azure.

## MCP Connectors and Triggers

ACA Sandboxes now supports managed connectors through the Model Context Protocol (MCP), giving sandboxes access to external APIs - including Microsoft 365, Salesforce, ServiceNow, GitHub, and 1,400+ other systems - without managing credentials directly. Attach a Connector Gateway to your sandbox group, and every sandbox in the group can call external APIs through a standardized MCP interface at runtime. Pair connectors with triggers to build event-driven automation: route an Outlook email to a sandbox that triages it with an AI agent, or react to a SharePoint file upload by extracting and processing the document  all without writing glue code. Triggers can fire a shell command inside a sandbox or invoke an HTTP endpoint the sandbox exposes, so your automation shapes fit naturally around your workload.

The integration is built on the new Connector Namespace service (az *connector-namespace),* the same runtime behind Logic Apps and Power Platform connectors, now available as a programmable layer for sandboxes. See the [end-to-end samples](https://github.com/Azure-Samples/azure-container-apps-sandboxes) for runnable azd up-deployable examples covering email triage and document automation scenarios.

## The Portal Experience

Azure Container Apps Sandboxes are only available in the new [Azure Container Apps portal](https://sandboxes.azure.com/) that provides a rich, IDE-like experience for working with sandboxes.

**Creating a Sandbox**

The portal offers multiple creation paths:

- **Standard Sandbox** - full configuration control over source, resources, lifecycle, networking, and volumes
- **GitHub Copilot Sandbox -** preset, Copilot CLI ready to go, GitHub credentials can be wired through the Access Token before the sandbox is created
- **Claude Sandbox** - Claude CLI pre-installed, ready for agentic coding inside the sandbox

**Using Coding Agents (Copilot CLI / Claude Code)**

If you live inside Copilot CLI or Claude Code, you don't need to learn a new CLI. Install the azure-sandbox skill once and your agent picks up the right skills:

```
# GitHub Copilot CLI # Add as a plugin marketplace /plugin marketplace add microsoft/azure-container-apps # Install all skills /plugin install sandboxes@Azure-Container-Apps # Claude Code claude plugin add microsoft/azure-container-apps
```

The skill runs prerequisite checks silently (*az --version, az account show, node --version, aca --version*), prompts only if something's missing, and maps natural-language asks to the right aca commands. Bundled runbooks cover Copilot CLI BYOK (bring your own Azure OpenAI key), the deploy-a-web-app walkthrough, and shell setup.

**Sandbox Detail Page**

Once your sandbox is running, the detail page gives you immediate access to the sandbox terminal and additional details, such as -

- **Network Audit** - real-time egress traffic log showing allowed and denied requests
- **Monitor** - live CPU, memory, disk, and network utilization charts
- **Connectors** - attached connections with an "Add" action
- **Volumes** - mounted volumes with an "Add" action
- **Log Stream** - streaming container logs
- **Processes** - running process list inside the sandbox
- **Files** - file explorer to browse the sandbox filesystem

The toolbar actions let you manage the state of the sandbox - **Resume** or **Stop**. In the Ellipsis menu (⁝) you can find additional settings to manage network **Egress Policy** and **ingress** (Add port), take a **Snapshot** of the sandbox, **Commit** (save disk state as a new disk image), set **Lifecycle Policy** or permanently Delete the sandbox. Finally, you can see additional **Details** in a side panel.

## Getting Started with the CLI and Python SDK

All sandbox and sandbox-group operations go through the *aca* CLI. There are no *az containerapp sandbox* commands, *- az* is only used for *az login*, *az account show*, and resource-group management.

**Install (CLI)**

```
# Mac, Linux
curl -fsSL https://aka.ms/aca-cli-install | sh

# Windows
irm https://aka.ms/aca-cli-install-ps | iex
```

Run *aca --help* to get started.

**Install (Python SDK)**

```
pip install azure-containerapps-sandbox
```

For more details, quick start and examples on ACA CLI and Python SDK, please go to <https://sandboxes.azure.com>

# Evolution from Dynamic Sessions

If you've used [Azure Container Apps Dynamic Sessions](https://learn.microsoft.com/en-us/azure/container-apps/sessions), Sandboxes are the next evolution of that capability. Everything Sessions can do, Sandboxes can do - and significantly more:

|  |  |  |
| --- | --- | --- |
| **Capability** | **Dynamic Sessions** | **Sandboxes** |
| Sub-second startup | ✓ | ✓ |
| Strong isolation | ✓ | ✓ |
| Custom container images | ✓ | ✓ |
| Custom VNet integration | ✓ (Partial) | ✓ |
| Suspend/resume with Memory and Disk snapshots | - | ✓ |
| Lifecycle policies (auto-suspend, auto-delete) | - | ✓ |
| Network egress policy (per-sandbox) | - | ✓ |
| Persistent managed volumes (Blob, Data Disk) | - | ✓ |
| Managed identity (system + user-assigned) | - | ✓ |
| Secrets management | - | ✓ |
| Configurable resource tiers | - | ✓ |
| Direct access to sandbox in Portal experience | - | ✓ |

We will continue to support Dynamic Sessions, but all new investment goes into Sandboxes. If you're building new workloads on isolated ephemeral compute, start with Sandboxes.

## How It All Fits Together

ACA Sandboxes is a platform primitive. It's the foundation on which multiple Microsoft products are already built - including ACA Express, Cloud sandboxes in GitHub Copilot, and Foundry Hosted Agents. When you build on Sandboxes, you're building on the same infrastructure that powers Microsoft's own portfolio.

This is the evolution of what we shared with [Project Legion](https://aka.ms/aca/project-legion-blog) in 2024. Legion described the internal infrastructure; Sandboxes exposes it as a customer-facing primitive that you can use directly.

# What's Next

• Deeper Azure integrations - first-class connectivity with Azure networking, identity, storage, and AI services

• Enhanced SDK and CLI - richer programmatic experiences for managing sandboxes at scale

• More Microsoft services built on Sandboxes - this is just the beginning

# Get Started Today

• **Portal**: <https://sandboxes.azure.com/>

• **Documentation**: [Azure Container Apps Sandboxes](https://aka.ms/aca/sandbox)

• **Pricing**: [Azure Container Apps Pricing](https://azure.microsoft.com/pricing/details/container-apps/) (per-second vCPU/memory billing, scale-to-zero, snapshots at Blob Storage rates)

We'd love to hear your feedback. You can ask questions, or file issues on the [Azure Container Apps GitHub](https://github.com/microsoft/azure-container-apps) (prefix with [Sandbox] for Sandboxes-specific issues).

Updated Jun 02, 2026

Version 1.0

[azure container apps](/tag/azure%20container%20apps?nodeId=board%3AAppsonAzureBlog)

[azure paas](/tag/azure%20paas?nodeId=board%3AAppsonAzureBlog)

[best practices](/tag/best%20practices?nodeId=board%3AAppsonAzureBlog)

[cloud native](/tag/cloud%20native?nodeId=board%3AAppsonAzureBlog)

[containers](/tag/containers?nodeId=board%3AAppsonAzureBlog)

[microservices](/tag/microservices?nodeId=board%3AAppsonAzureBlog)

[modern apps](/tag/modern%20apps?nodeId=board%3AAppsonAzureBlog)

[python](/tag/python?nodeId=board%3AAppsonAzureBlog)

[serverless](/tag/serverless?nodeId=board%3AAppsonAzureBlog)

[web apps](/tag/web%20apps?nodeId=board%3AAppsonAzureBlog)

Comment

[vyomnagrani](/users/vyomnagrani/1396352)

Microsoft

Joined May 20, 2022

Send Message

[View Profile](/users/vyomnagrani/1396352)

[Apps on Azure Blog](/category/azure/blog/appsonazureblog)

Follow this blog board to get notified when there's new activity
