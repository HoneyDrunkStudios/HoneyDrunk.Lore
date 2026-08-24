---
source: "https://www.docker.com/blog/ai-agent-security-systems-problem"
title: "17,600 Actions: Agent Security Is a Systems Problem"
author: "Mark Cavage"
date_published: "2026-08-18"
date_clipped: "2026-08-24"
category: "DevOps & CI/CD"
source_type: "rss"
---

# 17,600 Actions: Agent Security Is a Systems Problem

Source: https://www.docker.com/blog/ai-agent-security-systems-problem

*Everyone has been talking about the OpenAI/Hugging Face incident, and I was initially skeptical that Docker had much to add. After several weeks of customer conversations, I think we do. The useful lesson is not that an AI agent escaped a sandbox. It is what 17,600 actions expose about security systems designed for human tempo.*

Hugging Face reconstructed approximately 17,600 attacker actions across a four-and-a-half-day campaign in July, including roughly two and a half days inside its infrastructure.

Put thirty seconds of human review against each action and you get 147 hours of work. Hugging Face grouped those actions into roughly 6,280 clusters; review only those and you still get more than 52 hours. Either way, manual approval and ordinary alert triage were never plausible primary controls for this workload.

This was not a fundamentally new category of attack. If you have any background in incident response, the sequence is familiar: exploit a reachable service, obtain code execution, collect credentials, escalate privilege, and cross the next trust boundary.

What was different was the rate, persistence, and ability to carry authority and state across short-lived environments. The agent could fail, rebuild its tooling, recover its communications channels, and continue from another environment without starting the campaign over. The useful mental model is a capable attacker fused with a fuzzer: it can reason about each result and keep probing without fatigue. That is the AI part of the story.

This is not a commentary on model alignment, and I will offer no opinion here on which model or agent framework you or your organization should use. The security question is familiar: what authority should be given to a workload that can execute code, hold credentials, reach the network, and continue testing paths long after a human would have stopped?

## What happened

OpenAI was running internal cyber-capability evaluations against a benchmark called ExploitGym, which tasks agents with finding and exploiting vulnerabilities. The evaluation used reduced refusal behavior and none of the production-grade classifiers a deployed model would normally have.

The agents did not have direct internet access. They were allowed to install packages through an internally hosted package-registry cache. The agents found a previously unknown vulnerability in that permitted service and used it to reach the open internet.

The permitted service was the escape path. That’s the important point in the incident.

From there, the agents escalated privilege inside OpenAI’s research environment, reached a user-hosted CyberGym-style code-execution harness running on an external sandbox, and obtained root inside that harness. The sandbox platform itself was not compromised. Having apparently worked out that Hugging Face might host the benchmark’s reference answers, the agents went after Hugging Face directly, assessing that cheating was the fastest path to a passing score.

Hugging Face’s reconstruction documents local-file disclosure, code execution through a template engine, cloud metadata access, Kubernetes privilege escalation, exposure of a production secret containing 136 keys, access to the corporate network through a stolen credential, and limited write access to source control. It found no evidence that public models, datasets, packages, or released software were modified, and the customer content accessed was limited to a handful of benchmark-related datasets. That is a good outcome relative to what was possible. It is not evidence that the attack path was harmless.

The individual weaknesses were familiar: an unsafe processing path, accessible cloud metadata, broad privileges, long-lived credentials, and a shared administrative identity. A capable human attacker could have chained them, too. The difference was the volume of paths tested, the speed with which a failed path was replaced, and the amount of evidence defenders had to interpret while the campaign continued.

If you want the full blow-by-blow, Hugging Face published a detailed technical writeup and interactive replay. Both are worth reading.

## The controls this requires

That arithmetic, not the novelty of the attack, is what changes the operating model. A human cannot sit in the control loop for thousands of actions at machine speed.

There are also two related threat models to account for.

In the first, the agent discovers and exploits a path on its own, as the agents did in this incident. In the second, an external party redirects the agent through a poisoned tool, compromised dependency, malicious document, prompt injection, or attacker-controlled data. In that case, the agent becomes the attack vector.

The same authority is dangerous in either case. The controls therefore have to govern what enters the environment, which capabilities the agent receives, and what happens when its behavior leaves the expected boundary.

What can go wrong | Control required |
|---|---|
| Untrusted content attempts to change the agent’s instructions | Treat external content as data, never authority; preserve provenance and trust boundaries; do not allow retrieved content to modify policy or grant capabilities |
| A tool, package, image, or MCP server is poisoned | Strict allowlisting; pin versions and digests; verify signatures and provenance; require SBOMs; scan and review updates before promotion |
| External data becomes executable input | Use structured and typed tool interfaces; validate and escape arguments; prohibit unsafe shell interpolation and other paths from data to command execution; run commands inside a sandbox and constrain which commands can be invoked |
| A permitted service becomes an escape path | Expose the narrowest operation-specific interface; scope access by task and destination; monitor permitted paths for behavior that diverges from their purpose |
| The workload reaches ambient credentials or control-plane services | Remove ambient credentials; use short-lived, task-scoped workload identity; block metadata and control-plane endpoints the task does not require |
| The workload exceeds its intended execution boundary | Use a hardened isolation boundary; reject privileged workloads, host filesystem mounts, raw device access, and unrestricted host sockets unless explicitly required |
| State or authority persists beyond replacement of the worker | Govern durable write paths; separate read from write authority; correlate identity and activity across runs |
| The agent, or an attacker acting through it, crosses into another system | Require explicit authorization for external and destructive actions; scope credentials to the target operation; make write paths observable and revocable |
| Thousands of individually plausible actions hide behavior that has diverged from the task | Evaluate sequences and bursts against policy and expected behavior; correlate activity across tools and systems; contain at machine speed |

The point is not to put human approval in front of every action. That defeats much of the value of using agents and eventually produces approval fatigue. Routine and reversible actions should have very little friction. More sensitive, external, destructive, or unusual actions should receive stronger scrutiny.

Review and sanitization still matter, particularly for packages, tools, and paths where external data could become a command. But sanitization alone is not a reliable answer to prompt injection. Natural-language content is too ambiguous for us to assume we can always identify and remove the malicious part. The stronger boundary is architectural: untrusted content must not be able to grant itself authority, change policy, or create capabilities the agent did not already have.

Done well, governance is not what limits agent autonomy. It is what makes it possible to safely give agents more of it.

## Where Docker fits today, and where we do not

We are proud to be founding authors of the Agent Baseline. We worked with other industry experts to distill the problem into six outcomes: Discover, Constrain, Authorize, Observe, Validate, and Respond.

If Docker Sandboxes sit in one specific bucket, it’s “Constrain,” but really, we believe they’re foundational, and where you would instrument or implement all six. They give each agent a dedicated microVM and enforceable boundaries around local compute, filesystem access, and network reach, as well as providing the base (and thus ground truth) layer to observe. That is a real and useful layer.

Docker AI Governance addresses parts of Authorize and Observe by giving organizations a centralized way to define and enforce controls around agent environments, including network and filesystem policies and access to MCP servers and tools.

Together, Sandboxes and AI Governance provide a meaningful part of the answer today: a hardened execution environment and centralized policy enforcement around it. They do not repair a vulnerable service the agent is authorized to contact, narrow a credential issued by another system, or replace the customer’s own security architecture. No vendor, Docker included, can claim its technology would have made this particular incident a non-event.

But a deterministic enforcement boundary is still necessary. It gives an organization one place to apply least capability and least privilege, and one place to observe what the agent was actually allowed to do. If an agent is using a package registry as an egress proxy rather than a package registry, that’s the kind of divergence the telemetry needs to help surface, especially when viewed across a sequence of requests rather than one request at a time.

The broader problem remains difficult. The useful unit of observation is not always one tool call. It may be a burst of activity, a target, a protocol, a credential, or a pattern visible only across systems. A package request can be normal. Repeatedly probing the service behind it, discovering credentials, and using them to reach another system should change the assessment.

That’s the agent-security challenge beyond basic containment. We need to constrain authority, but also observe activity at the right granularity, recognize when it deserves more scrutiny, and respond at the same tempo as the agent. For all of us, Docker included, there is still substantial work ahead across observation, validation, and response.

## The operational tradeoff

Security, capability, and autonomy all matter, and they will always be in tension. Said differently, none of this is free.

Short-lived credentials expire during long-running tasks. Narrow egress policies break legitimate package installation. Admission controls reject tools developers assumed they could run. Cross-system detection costs money and produces false positives. A write approval inserted at the wrong point can eliminate most of the productivity the agent was supposed to provide.

Teams will be tempted to loosen each control until the agent works again. That is understandable. The failure mode created by a strict policy is immediate and visible; the failure mode created by excessive authority remains invisible until an incident.

The answer is not to remove the controls or ask a human to approve everything. It is to make friction proportional to consequence, test the failure modes, measure the operational cost, and weigh it against the risk and potential blast radius.

## How I work

I use agents every day, and I assume that a sufficiently capable agent will eventually try something I did not anticipate (perhaps on a daily basis…).

For the most part, I do not run one general-purpose agent with access to everything. I use task-focused agents, each packaged as a separate kit, built on free Docker Hardened Images and run in Docker Sandboxes.

Each kit starts with a specific job, then receives only the software, network access, files, credentials, and external capabilities required for that job.

In most cases, the agent has very few restrictions inside its sandbox. That is intentional. What matters is that god mode inside the sandbox does not become god mode over my laptop, my credentials, or every service I can reach.

I do a lot of desk research. Those agents can access the open internet. They’re not useful if they can’t. But their image has no compilers, package manager, general-purpose network debugging tools, or development toolchain, and it runs with deliberately limited system permissions. They can retrieve and analyze public information, but have very little machinery with which to turn something they encounter into an exploit or act on another system. They have no reason to hold my source code or production credentials.

My production coding agent has a much richer environment. It runs pi, can use multiple models, compile code, run tests, and use the tools required for real engineering work. Its network access is restricted to an explicit allow list of services I use, including Docker, GitHub, Snowflake, and Cloudflare. It does not receive arbitrary internet access or arbitrary tools simply because a coding task occasionally needs the network.

My home kit can interact with an Arduino, but it does not receive direct access to the host or the device. A host-side MCP server brokers the allowed operations. The agent can request a defined Arduino capability through that interface; it cannot turn that permission into general access to every device connected to the machine.

My development kit is where I experiment. It runs with balanced network access, but no ambient host secrets and no unrestricted access to host files. When it needs Google Workspace, Snowflake, or another host service, host-side daemons broker those calls. The agent sees the capability I have chosen to expose, not the underlying credential or the rest of the service. Those brokers can enforce which operations are allowed and which are blocked.

These are deliberately different environments. The research agent would be poor at production coding. The coding agent cannot reach every site the research agent can. The home agent cannot turn an Arduino operation into arbitrary host access. The development agent can query a service without possessing the credential that authorizes the query.

That constraint is the feature.

## Conclusion: Security at agent speed

The OpenAI/Hugging Face incident was not the failure of a single boundary. It was a chain of reasonable-seeming permissions and familiar weaknesses that became something very different when an agent could test thousands of paths, preserve state across runs, and carry authority from one system into the next.

We will not anticipate every vulnerability an agent might find or every way it might combine the access we give it. The architecture cannot depend on perfect agent behavior, perfect software, or a human noticing every dangerous action in time.

So, the starting point is still least capability and least privilege: give an agent the narrowest interface, credentials, tools, and network access its task requires. Put those controls at a deterministic enforcement boundary. Make the resulting activity observable, not only as isolated requests, but as sequences and patterns across systems. When the behavior leaves the expected envelope, containment has to happen at agent speed.

Docker Sandboxes and Docker AI Governance provide important parts of that architecture today: hardened execution boundaries and centrally enforced policy around them. They do not secure every service an agent is permitted to contact, and they do not eliminate the need for an organization to decide what authority each agent should have. The broader work across Discover, Constrain, Authorize, Observe, Validate, and Respond is why we helped create the Agent Baseline in the first place.

The goal is not to build an agent that never tries the wrong thing. The goal is to build a system where trying the wrong thing does not give it the keys to everything else.
