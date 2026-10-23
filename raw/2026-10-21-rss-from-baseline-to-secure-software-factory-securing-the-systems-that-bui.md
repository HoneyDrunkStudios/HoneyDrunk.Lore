---
source: "https://www.docker.com/blog/from-baseline-to-secure-software-factory-securing-the-systems-that-build-your-software"
title: "From baseline to Secure Software Factory: securing the systems that build your software"
author: "Eli Aleyner"
date_published: "2026-10-21"
date_clipped: "2026-10-21"
category: "Security & Ethical Hacking"
source_type: "rss"
---

# From baseline to Secure Software Factory: securing the systems that build your software

In July, Docker, Snyk and Keycard published [Agent Baseline](https://agentbaseline.org/), an open, vendor-neutral reference architecture that defines security outcomes for running AI agents in the enterprise. It grew out of conversations with industry leaders who want to adopt agents more broadly but need answers to three questions:

- What is operating, with what capabilities?
- Is it staying inside approved boundaries?
- Can you prove what happened and stop it?

Agent Baseline gave the industry a shared frame of reference for secure agent adoption by defining the security outcomes for safely deploying agents in organizations. Last week, we published the Secure Software Factory reference architecture, which applies those outcomes to one of the most common agentic workflows: the AI-powered software factory.

## Enter the Secure Software Factory

The Secure Software Factory was written by practitioners from Keycard, Socket, Docker, Tessl, Tracebit, Browserbase and Tailscale and shaped by conversations with security leaders at large enterprises in regulated environments such as finance and insurance.

Over the past year, many engineering teams have started building software factories: systems where agents take a request, change code, run tests and hand the result to a human for review. Teams report faster delivery, but also agents doing things nobody asked for, like escaping sandboxes, dropping databases and pushing to production without approval.

Teams need controls that limit what agents can access and do, and check their work at each step. The Secure Software Factory reference architecture shows how to apply Agent Baseline’s security outcomes across this workflow, covering:

- **The factory workflow**, from inputs through design, assembly, build and verification, with controls at each stage.
- **Architectural primitives** for identity and access, supply chain, network controls, runtime isolation and orchestration.
- **A maturity model with three levels**, so teams can start where they are and improve over time.

The paper’s central idea is that the more autonomy you give an agent, the less you can rely on it to police itself. An agent can be redirected at runtime by a prompt, a poisoned dependency or a malicious tool description. Controls have to work regardless of what the agent decides, which means they need to live in the environment it runs in. That means boundaries around credentials, tools, dependencies and network access, backed by evidence of what happened and a human accountable for the result.

This is the part of the problem Docker solves. Containers isolate applications; sandboxes isolate actors. Docker Sandboxes are isolated MicroVMs that constrain agents, deterministically.

Docker Sandboxes lets coding agents work autonomously in isolated microVM environments, locally or in the cloud, with explicit boundaries around the files, network destinations, and credentials they can access. This supports Agent Baseline’s Constrain outcome by confining agent execution and limiting its reach to what the approved task requires.

Agent Baseline is only useful if the people building the agent stack agree on it. Which is why we are proud to be among leading companies such as Snyk, Keycard, Browserbase, Tessl, Socket and Tracebit, in shaping the baseline and the reference architectures built on it.

## More companies are joining Agent Baseline

*In a software factory, context is the new code: it’s what actually gets executed. The skills you consume are part of your supply chain, and can be vulnerable, negligent or outright malicious. They need the same security controls software modules do – let’s get it right from the start!*

***Guy Podjarny, Founder and CEO, Tessl***

*“We’ve spent decades learning not to give software more access than it needs. We seem to have forgotten much of that now that the software can talk back. Agents need to reach real systems, sometimes even production. The rules haven’t changed: give them the authority to do a particular job, make that authority expire, and keep the policies and audit trail somewhere the agent can’t rewrite them. Agent Baseline gives everyone a common architecture for making that work, without every team having to figure it out from scratch.”*

***Avery Pennarun, Co-Founder & CEO, Tailscale***

*“Enterprises are handing AI agents real credentials, and some of those agents will go off-task, whether through prompt injection, a poisoned tool or a simple mistake. Agent Baseline sets the standard for keeping agents in bounds”*

***Andy Smith, Co-Founder & CEO, Tracebit***

*“Agents need the right guardrails to complete tasks on behalf of humans. This is an industry wide effort and Browserbase is proud to continue supporting initiatives like Agent Baseline”*

***Paul Klein, Founder & CEO, Browserbase***

*“Agents are already building software, and teams want them picking up work on their own. That only works if an agent’s plan can never become its permission. Agent Baseline gives everyone a shared architecture for deciding what each agent may do, task by task and outside the agent’s reach, so teams can add autonomy without starting their security model over.”*

***Ian Livingstone, Co-Founder & CEO, Keycard***

## **Get involved**

Help shape Agent Baseline and the Secure Software Factory reference architecture by putting them to work.

Read the [paper](https://agentbaseline.org/reference-architecture), open an issue on GitHub or [join the Agent Baseline Slack](https://agentbaseline.org/) to tell us where the architecture doesn’t match how you build. Implementation feedback is the most useful kind.
