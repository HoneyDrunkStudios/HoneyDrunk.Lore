---
source: "https://www.docker.com/blog/agentic-ai-security-docker-governance"
title: "The Trust Layer: Securing Agentic AI with Docker AI Governance"
author: "Karan Verma"
date_published: "2026-11-18"
date_clipped: "2026-11-19"
category: "Security & Ethical Hacking"
source_type: "rss"
---

# The Trust Layer: Securing Agentic AI with Docker AI Governance

Source: https://www.docker.com/blog/agentic-ai-security-docker-governance

## The Agent Trust Gap

The security problem changes once an AI agent can do more than answer a prompt. It can execute code, access files, connect to services, and call external tools. That creates a new security question for enterprises: **how do you give an agent enough freedom to be useful without giving it more access than it actually needs?**

**A model decision is not automatically an authorized action.** That distinction becomes important the moment an agent can turn a model output into an action in a real system.

The answer can’t rely only on the model. Agent behavior can vary, while security controls need to be clear and enforceable. That means putting controls around the environment where the agent runs, what it can access, which tools it can use, and what happens when a policy allows or blocks an action. For a CISO, this creates a trust gap. Approving the use of AI agents means being able to answer more than whether the model is capable: what access does the agent have, where are those boundaries enforced, and what evidence is available afterward? The goal is to let teams adopt agents without making model behavior itself the security boundary.

[Docker AI Governance](https://www.docker.com/products/ai-governance/) approaches this through three areas: **Sandbox Policies, MCP Tool Governance, and Audit + Visibility.**

Together, they address three practical questions security teams need answered: **Where can the agent operate? What can it do? And can we see what happened?**

In this article, I use “trust layer” as shorthand for the infrastructure between what an agent wants to do and what the organization actually allows it to do.

There is a related trust question too: what software artifacts are these agentic workflows building and using? Docker Hardened Images address that software supply-chain side of the problem, alongside the runtime controls discussed below.

![image3](https://www.docker.com/app/uploads/2026/11/image3.png "- image3")

*Figure 1: The three layers of Docker AI Governance: Sandbox Policies, MCP Tool Governance, and Audit + Visibility.*

## Sandbox Policies: Where Can the Agent Operate?

An agent needs enough access to get real work done. A coding agent may need to install packages, build containers, edit project files, or connect to external services. The security challenge is deciding where those actions are allowed before the agent starts taking them.

Docker Sandboxes give each agent an isolated microVM environment a lightweight virtual machine with its own Docker Engine, filesystem, and network. Docker AI Governance adds policy around that environment so security teams can control network and filesystem access centrally.

Network policies can allow or block specific domains, IP ranges, and ports. Filesystem policies control which host paths can be mounted into a sandbox and whether that access is read-only or read-write. These controls are enforced at the network proxy and filesystem mount layers rather than depending on the agent to follow an instruction.

For an organization, that means the same boundaries can follow developers across their sandboxes instead of being configured differently on every machine. Teams still get the access they need for their work, but an individual agent cannot simply expand those boundaries on its own.

A developer can check the effective boundary before starting the agent:

```
$ sbx policy check network api.anthropic.com 
Allowed: api.anthropic.com

$ sbx policy check network blocked.example.com
Denied: blocked.example.com
```

The important part is that the result comes from the active policy, not from an instruction the agent is expected to follow.

This answers the first governance question: **Where can the agent operate?**

## MCP Tool Governance: What Can the Agent Do?

Once an agent has a controlled place to run, the next question is what it should be allowed to do through external tools.

MCP (Model Context Protocol) gives agents a common way to connect to external tools, services, and capabilities, but that also expands what an agent can act on. For enterprise use, making a tool available should not automatically mean every agent can use it.

Docker AI Governance puts policy around MCP activity handled through Docker’s MCP Gateway. Administrators can control which MCP servers may be registered and what agents can do through them, including tool calls, resources, prompts, and approval requirements. These organization policies are written in Cedar, a policy language used to express authorization rules. When MCP policy enforcement is active, governed requests are denied unless a matching policy permits them. For example, a policy can permit read-only tool calls for a specific registered MCP server:

```
permit (principal, action == MCP::Action::"invokeTool", resource)
when {
  resource in MCP::Server::"example" &amp;&amp;
  resource.readOnly == true
};
```

Here, `readOnly` comes from the MCP tool’s annotations. Those annotations are supplied by the server and are advisory, so this example relies on metadata provided by that server.

This makes tool access an explicit policy decision rather than something left to each agent or developer to configure independently. A team can be given access to the tools it needs, while other servers or actions remain unavailable. Policies can also require confirmation for specific tool calls when an action needs an additional checkpoint.

One boundary is worth making clear: MCP policies apply to activity handled by Docker’s MCP Gateway. If an agent connects directly to a remote MCP server from inside a sandbox, that connection falls under the sandbox’s network policy instead.

With the environment constrained and tool access governed, we can answer the second question: **What can the agent do?**

## Audit + Visibility: Can We See What Happened?

Setting a policy is only part of the job. Security teams also need to know when that policy was applied, what action triggered it, and whether the action was allowed or denied.

Docker AI Governance records sandbox policy decisions and sandbox session events as structured [audit records](https://www.docker.com/blog/docker-ai-governance-audit-logs-now-where-your-security-team-already-works/). Each record captures details such as the principal, action, target, decision, and time. The records contain governance metadata rather than the contents of prompts or agent responses.

Audit records can be kept locally or delivered to the [cloud](https://docs.docker.com/ai/sandboxes/governance/audit/). With cloud delivery enabled, teams can search the organization-wide record, export it for further analysis, or forward events into existing SIEM (security information and event management) workflows.

Denied actions are especially useful. A team can see not only that an action failed, but that a governance rule blocked it and why. Allowed decisions matter too: they provide a record of how policy was applied while the agent was working.

Current audit coverage includes Docker Sandboxes policy decisions and sandbox session events. The same schema can support additional Docker AI sources as they become available.

That closes the third part of the governance loop: **Can we see what happened?**

## A Trusted Software Supply Chain: Docker Hardened Images

AI Governance controls access around the agent at runtime. There is a separate question that matters to the workflows those agents participate in: **what container images and software artifacts are they building, testing, or deploying?**

[Docker Hardened Images](https://docs.docker.com/dhi/) provide minimal, secure, and production-ready container images, Helm charts, and system packages maintained by Docker.

In practical terms, this gives teams evidence about what is inside an image and how that image was produced. Docker Hardened Images include signed SBOMs, VEX information, cryptographic signatures, and SLSA Build Level 3 provenance. Instead of simply trusting where an image came from, teams can inspect what is inside it and verify information about how it was built.

For organizations with additional compliance requirements, Docker also provides FIPS-enabled and STIG-ready variants through relevant DHI offerings. These capabilities sit alongside the broader DHI security and supply-chain controls rather than making any single standard the foundation by itself.

AI Governance and Docker Hardened Images solve different parts of the trust problem. Governance controls the authority an agent has while it works; DHI helps establish trust in the container artifacts that the workflow depends on.

![image1](https://www.docker.com/app/uploads/2026/11/image1.png "- image1")

*Figure 2: Docker Hardened Images combine minimal container images with signed supply-chain metadata and verifiable build provenance.*

## Putting the Three Layers Together

Consider a developer using a coding agent to investigate an issue, update a service, and use an approved internal tool along the way.

The agent begins inside a Docker Sandbox. It can work with the project and run the commands needed for the task, but its access is still bounded by policy. If it tries to reach a network destination or mount a host path that the organization has not allowed, the applicable sandbox policy can block that access.

Now suppose the agent needs an MCP tool to look up information from another service. The request goes through Docker’s MCP Gateway, where organization policy determines whether that server and tool are permitted. A routine lookup might be allowed, while a more sensitive tool call could require confirmation or remain unavailable altogether.

For governance activity currently covered by AI Governance Audit Logs, Docker records the policy decision and relevant session metadata. Security teams can see who initiated the activity, what policy-controlled action was evaluated, and whether it was allowed or denied. Those records can then feed the organization’s existing monitoring and SIEM workflow.

If that same agent builds or tests a containerized application, the software entering the workflow matters too. Docker Hardened Images provide a more verifiable software foundation for that workflow, while AI Governance controls what the agent is authorized to do at runtime.

The model is still making decisions about how to complete the task. **What changes is the authority around those decisions.** The agent can work autonomously inside the boundaries the organization has defined, while access outside those boundaries remains a policy decision.

That is the practical value of the three layers working together:

**Sandbox Policies define where the agent can operate.**

**MCP Tool Governance defines what tools it can use.**

**Audit + Visibility shows how governed activity was handled.**

Taken together, the pattern is straightforward: define the boundary, check it before the agent starts working, enforce it while the agent is running, and use the resulting audit trail to understand what happened. If a boundary needs to change, the policy changes, not the expectation that the model will simply behave differently.

## Autonomy Without Unbounded Authority

The challenge with agentic AI is not simply that agents can make decisions. It is that those decisions can now lead directly to actions.

That makes the boundary around the agent just as important as the model itself. Docker AI Governance addresses that boundary through Sandbox Policies, MCP Tool Governance, and Audit + Visibility: controlling where agents can operate, what tools they can use, and how governed activity is recorded.

Docker Hardened Images address a related supply-chain concern by helping teams work with smaller, verifiable container artifacts.

The goal is not to remove autonomy from agents. It is to make sure autonomy does not automatically come with unlimited authority.

As agents take on more real work, that distinction will matter more and more.

## Learn more

- [Why AI Agents Need Isolation](https://www.docker.com/blog/why-ai-agents-need-isolation/)
- [AI Governance Series – Part 1: Your Laptop Is the New Production Environment](https://www.docker.com/blog/your-laptop-is-the-new-production-environment/)
- [AI Governance Series – Part 2: Runtime Enforcement, Not Runtime Advice](https://www.docker.com/blog/runtime-enforcement-not-runtime-advice/)
- [AI Governance Series – Part 3: Governance Is a Developer Experience Problem](https://www.docker.com/blog/governance-is-a-developer-experience-problem/)
- [Explore Docker AI Governance](https://www.docker.com/products/ai-governance/)
- [Explore the companion GitHub repository](https://github.com/karanverma/docker-ai-governance-trust-layer)
