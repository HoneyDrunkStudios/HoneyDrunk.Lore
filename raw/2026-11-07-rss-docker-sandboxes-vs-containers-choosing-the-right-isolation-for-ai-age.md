---
"source": "https://www.docker.com/blog/docker-sandboxes-vs-containers/"
"title": "Docker Sandboxes vs. Containers: Choosing the Right Isolation for AI Agents"
"author": "Srini Sekaran; Oleg Selajev"
"date_published": "2026-11-05"
"date_clipped": "2026-11-07"
"category": "DevOps & CI/CD"
"source_type": "rss"
---

# Docker Sandboxes vs. Containers: Choosing the Right Isolation for AI Agents

Source: https://www.docker.com/blog/docker-sandboxes-vs-containers/

If you’ve used Docker for a while, “Docker Sandboxes” might read as “a container with an AI agent inside.” Containers have been the unit of nearly everything Docker ships for over a decade, and a sandbox might sound like one more way to package a workload.

They’re actually different technologies. A container is an isolated process that shares the host kernel with everything else on the machine. Docker Sandboxes are [dedicated microVMs with their own Linux kernel](https://www.docker.com/products/docker-sandboxes/vs-containers/), filesystem, network, and Docker Engine, built for autonomous coding agents that need a whole development machine to work in. A sandbox can run containers, which is part of why the two are easy to conflate.

In his [WeAreDevelopers keynote](https://www.docker.com/blog/manufacturing-trust-for-ai-agents-keynote/), Docker President Mark Cavage said containers are doing exactly the job they were designed to do, but we’re asking them to do a different job.

Containers were built to isolate applications, which they still do well. But a coding agent is an actor: it makes decisions and operates on your systems the way a developer uses a laptop. It clones repositories, installs packages, starts databases, builds images, and tries again for hours. It can also act on instructions from files, web pages, and tool output that nobody reviewed.

That different job needs a different boundary, and where that boundary sits determines how far an agent’s mistake can travel. This post covers how Docker Sandboxes and containers isolate workloads, what changes beyond the kernel, what a sandbox costs you in setup, and how to pick.

> ## Key takeaways
>
> - A container is an isolated process sharing the host kernel. Docker Sandboxes are microVMs with their own kernel, filesystem, network, and Docker Engine.
> - Containers stay the right choice for packaged applications, CI jobs, and short-lived execution.
> - Docker Sandboxes fit autonomous agents that need sudo, a private Docker Engine, long-lived state, and host-enforced network and credential controls.
> - Containers can be part of an agent’s containment, and a sandbox can run them. Sandbox the agent, containerize the application it works on.

## What is a container?

A [container](https://www.docker.com/resources/what-container/?at_exp=DO105.A-DO106.B) is a process, or a group of processes, running on the host with its own view of the filesystem, process tree, and network. Linux namespaces provide that view, and cgroups meter CPU, memory, and I/O. Every container on the machine also shares the host kernel, which is why containers start quickly, pack densely, and carry so little overhead.

![Diagram of an agent running in a Linux container. The agent process, your app, and your database each run in their own container, all sharing one host kernel. A container escape lands on the host kernel, alongside every other container, with your files, credentials, network, and other processes beneath it.](https://www.docker.com/app/uploads/2026/11/docker_sandboxes-vs-containers_110226_v1_DARK-2320x1218.jpg "- docker sandboxes vs containers 110226 v1 DARK")

This design has more than a decade of tooling behind it. Compose, Kubernetes, OCI registries, image scanners, and nearly every CI system treat the container as the common primitive. If the job is to run a service, execute a code snippet, process one request, or run an evaluation and disappear, a container is usually the obvious pick, and it will stay that way.

|  |
| --- |
| ⓘ Containers share one kernel, even inside a VM. On macOS and Windows, Docker Desktop runs your Linux containers inside a virtual machine, which keeps them off your host operating system. Every container in that VM still shares its single kernel, so the isolation between one container and the next is unchanged. |

## What are Docker Sandboxes?

[Docker Sandboxes](https://docs.docker.com/ai/sandboxes/) run an AI coding agent inside a [microVM that has its own Linux kernel](https://www.docker.com/blog/benefits-of-sandbox-environments/), its own filesystem and network stack, and a private Docker Engine. The agent gets sudo inside the isolated environment. It can install packages, run services, build images, and bring up an entire Compose application without reaching the host Docker daemon, the host filesystem outside its workspace, or other sandboxes on the same machine.

![Diagram of an agent in a Docker Sandbox. The agent process, a private Docker Engine, and your app and database containers all run inside a microVM with its own guest kernel. Another agent runs in a separate microVM. A native hypervisor boundary sits between the microVMs and your machine, so a container escape lands in a disposable microVM, not on the host.](https://www.docker.com/app/uploads/2026/11/docker_sandboxes-vs-containers_110226_v1-DARK-2-2320x1218.jpg "- docker sandboxes vs containers 110226 v1 DARK 2")

Getting one running takes a single command, using sbx, the Docker Sandboxes CLI:

`sbx run claude`

That creates the sandbox and starts the agent. You can stop it, resume it, and come back to everything the agent installed until you remove the sandbox.

## Why do coding agents need a full machine?

Coding agents need a full machine because their sessions build up state over hours and they act on unvetted instructions. A container is built for a process with a known set of dependencies, and an agent’s work doesn’t fit that shape.

An agent needs the authority of a whole machine and a boundary designed for one. The capabilities that make an agent useful, such as running code, installing packages, and reaching the network, are the same ones that wear at the walls around it. An agent probes the edges of its environment because the job requires *changing* that environment.

### Agents accumulate state for hours

A coding agent’s session looks like a developer’s afternoon. It clones a repository, installs packages, starts PostgreSQL, runs migrations, builds images, launches the app with Compose, reads the logs, changes the code, and tries again. That loop can run for hours, and each step depends on what the previous one left behind.

A container is designed to be rebuilt from an image and a few explicit volumes. The packages, databases, and build output an agent creates outside those volumes are lost when the container is recreated. That’s less than ideal for a session where every step builds on the last.

|  |
| --- |
| [Box by ASCII](https://boat.dev/blog/containers-vs-vms) describes this distinction neatly: “It uses the sandbox the way a developer uses a laptop, so the sandbox has to behave like one.” |

### Agents act on untrusted instructions

The program deciding which command to run is probabilistic, and it can read instructions from many places at once, including source files, issue descriptions, web pages, package metadata, and MCP tool output. Some of that input is untrusted, and a [malicious instruction planted in a README or a tool description](https://www.docker.com/blog/coding-agent-horror-stories-the-command-you-already-approved/) can steer the agent on purpose. The code it generates may also be wrong or actively hostile.

We’ve already seen an agent that [deleted a production database](https://www.docker.com/blog/coding-agent-horror-stories-the-agent-that-deleted-production/) after misreading its task. Once the agent is [running una](https://www.docker.com/blog/what-is-yolo-mode/)[t](https://www.docker.com/blog/what-is-yolo-mode/)[tended in YOLO mode](https://www.docker.com/blog/what-is-yolo-mode/), there’s no permission prompt left to catch it. A workload with that much authority and that little predictability needs a boundary designed for it.

Put these facts together and you get the reason why we built Docker Sandboxes. An autonomous coding agent needs machine-shaped capabilities without access to everything on the developer’s machine, which comes down to four things:

1. **Containment**: a boundary the model can’t rewrite
2. **Control**: observability into what the agent is doing and the ability to stop it
3. **Choice**: the freedom to swap agents, models, and tools without rebuilding the setup
4. **Capacity**: a setup other developers can reproduce and scale past one machine.

The next sections show what each looks like, starting with containment.

## Containment: How isolation differs between containers and Docker Sandboxes

The short version is that a container’s boundary is the host kernel it shares, and Docker Sandboxes have a hypervisor boundary around a kernel the agent has to itself. That one difference decides how far a compromise can travel, and it also settles the awkward question of how an agent could get access to Docker.

This is where containers and *containment* part ways. A container can be part of containment, and often should be, but containment covers the whole environment around the agent. It starts with a boundary the model can’t rewrite, which is why Docker uses a microVM with its own kernel for autonomous agents.

### Shared kernel vs. dedicated kernel

A container’s boundary is enforced by the kernel it shares, so escaping it requires a kernel exploit or a side-channel attack. Those aren’t everyday finds. Past that bar, though, sits the entire host kernel, every other process on the machine, and [any credentials mounted alongside them](https://www.docker.com/blog/coding-agent-horror-stories-the-29-million-secret-problem/).

|  |
| --- |
| ⓘ This scenario is specific to Linux environments. On Docker Desktop (macOS and Windows), the shared kernel is the Docker Desktop VM’s kernel, not the host kernel, so an escape would land in that VM rather than the operating system. |

Docker Sandboxes give the agent its own kernel behind a hypervisor boundary. If an agent escapes its container, it lands in a disposable microVM, and the host stays out of reach. And you can delete the sandbox and start another. Each agent also gets its own microVM, so two agents running on the same machine can’t reach each other’s sandboxes either. However, the agent can still reach whatever you chose to share with it, including the workspace, allowed network destinations, MCP servers, and skills.

### The Docker socket problem

Mounting `/var/run/docker.sock` into a container is the long-standing way to give it Docker access, and it turns up in Compose setups, CI pipelines, and observability tools. It also hands the container control of the host Docker daemon, which Docker [limits to trusted users](https://docs.docker.com/engine/security/#docker-daemon-attack-surface) because it can mount host paths and start privileged containers.

An agent doesn’t need an exploit to use that. Put one in a container started with the socket mounted, and it probes its surroundings, works out that it’s in a container, and finds the hole in the configuration. In Mark’s keynote demo, that was enough for an agent to [reach a secrets file on the host](https://www.youtube.com/live/G1tT3pwbsMM?si=v-hODxDMU7pDvjPZ&t=55) with no zero-day involved.

The socket is one hole among several, and agents find them because probing their environment is part of the work. Docker-in-Docker, mounted credentials, and broad host mounts are others. Containers were built to isolate an application that behaves as configured. But an agent keeps testing that configuration, so if there’s a gap, it’s likely to find it.

### Where the microVM boundary goes

Docker Sandboxes put the missing boundary in the right place. The agent talks to a [private Docker Engine](https://docs.docker.com/ai/sandboxes/security/isolation/#docker-engine-isolation) inside the guest. It can build images, run Testcontainers, and start a whole Compose stack, and the host daemon and its socket stay outside the microVM the entire time. Containers keep doing what they do best, inside a boundary the agent can’t widen.

Let’s say you ask an agent running inside Docker Sandboxes to find a secrets file on the host. It’ll find a Docker socket, [try to use it to mount host paths and start privileged containers](https://www.youtube.com/live/G1tT3pwbsMM?si=v-hODxDMU7pDvjPZ&t=55), but won’t reach the host. A microVM can give it a much stronger trust boundary than a container. The [architecture behind Docker Sandboxes](https://www.docker.com/blog/why-microvms-the-architecture-behind-docker-sandboxes/) goes deeper on why a microVM was the right shape for this.

## Control: What you can see and stop beyond the kernel

Containment draws the boundary. *Control* is what you can see and stop inside it: what the agent is allowed to reach, and the ability to block it when it heads somewhere it shouldn’t. In a sandbox, those controls are enforced by the host, outside the agent’s reach, so the agent can’t switch them off or reason its way around them. Outbound traffic, credentials, and organization-wide policy all work this way. Control also means knowing what the agent can still touch, because a microVM can’t hide what you choose to share with it.

|  | Agent in a standard container | Agent in Docker Sandboxes |
| --- | --- | --- |
| **Kernel** | Shares the host kernel | Runs its own Linux kernel in a microVM |
| **Docker** | Needs the host socket or a nested daemon | Uses a private Docker Engine inside the microVM |
| **Workspace** | Sees the host paths you mount | Uses a direct read-write mount or an in-VM private clone |
| **Network** | Uses the container network and whatever controls its operator supplies | Sends outbound traffic through a host proxy with deny-by-default policy |
| **Credentials** | Commonly receives environment variables, files, or mounted sockets | Uses host-side credential injection for supported HTTP services |
| **State** | Usually rebuilt from an image and explicit volumes | Keeps packages, images, containers, and agent history until sbx rm |
| **Orchestration** | Fits Compose, Kubernetes, and most CI systems | Uses the sbx lifecycle and experimental environment files |

### The host enforces the controls

These controls hold because they [run outside the agent process](https://www.docker.com/blog/runtime-enforcement-not-runtime-advice/). A rule the agent can reach is a rule it can work around, so the rules that matter live on the host. Outbound traffic goes through a [host-side proxy](https://docs.docker.com/ai/sandboxes/security/) with a deny-by-default policy, which means a destination the agent wants stays blocked until someone adds it to the list. Credentials follow the same logic. For supported HTTP services, the proxy injects them into outbound requests, so the agent can use a credential without the raw value ever entering the VM.

When one developer’s setup needs to become a team standard, Docker AI Governance can move network, filesystem, and MCP policy into [organization-wide controls](https://docs.docker.com/ai/sandboxes/governance/).

### What the agent can still reach

A microVM can’t hide what you choose to share with it, so the shared parts deserve the most attention.

The **workspace** is the largest of them. It’s mounted read-write by default, so the agent can edit or delete files in your project. [Clone mode](https://docs.docker.com/ai/sandboxes/security/isolation/#clone-mode) gives the agent a private in-VM clone to work in, which protects the host working tree, though the original repository stays readable inside the sandbox.

**MCP servers** and **skills** are shared too. A local stdio MCP server runs on the host and shared agent skills use a host-side store, so the agent’s reach extends to both.

So whichever mode you pick, be sure to read the diff before you run modified code.

## Choice and capacity: What Docker Sandboxes cost you in setup

Docker Sandboxes may cost some configuration and a supported hypervisor. But Kits and environment files account for the configuration, and they’re also where you get *choice* over agents and tools and the *capacity* to reproduce a setup across a team.

### Kits and environment files

[Kits](https://docs.docker.com/ai/sandboxes/customize/) make setup repeatable by packaging tools, files, commands, network rules, credentials, and agent instructions. They’re published for different agents, tools, and IDEs, so you can swap what runs inside the sandbox without rebuilding the environment around it. An [sbxenv.yaml](https://docs.docker.com/ai/sandboxes/configuration/environment-files/) file records one project’s sandbox configuration, and committing it to the repo lets a teammate recreate the same sandbox with one command, so every developer works from the same setup. (Kits are in early access and environment files are experimental, so plan for changes to both.)

The host-enforced controls take some setup too. Network policy requires someone to decide which destinations belong in the workflow, credential mediation adds service bindings and approved domains, and clone mode adds a fetch step before changes land in the host repository.

### Hypervisor and resource requirements

Running a sandbox takes more from your machine than running a container does. It needs a supported hypervisor, which today means Apple silicon on macOS 14 or later, Windows Hypervisor Platform, or KVM on supported Ubuntu systems, and running inside another VM requires nested virtualization. The separate kernel and Docker Engine also consume more memory and disk than one additional container would.

If your machine is the limiting factor, [Docker Cloud Sandboxes](https://www.docker.com/blog/introducing-cloud-sandboxes-start-on-your-laptop-finish-in-the-cloud/) run the same microVM isolation on Docker-managed compute, and one command moves a sandbox between your laptop and the cloud. Local and cloud sandboxes keep separate secrets and network policies.

## How do you choose between a container and Docker Sandboxes?

Choose a container when you control the code and its dependencies, and choose Docker Sandboxes when the workload generates or fetches code at runtime and needs its own boundary.

| Reach for a container when | Reach for Docker Sandboxes when |
| --- | --- |
| You control the code and its dependencies | The workload generates or fetches code at runtime |
| Execution is short-lived and rebuilt from an image | The session accumulates state for hours |
| The workload doesn’t need Docker, or runs in CI that already provides it | The workload needs its own Docker Engine with no path to the host socket |
| You want maximum density and a fit with Compose or Kubernetes | You need host-enforced network and credential policy the workload can’t switch off |
| The kernel boundary is enough for the code you’re running | You want a hypervisor between the workload and your kernel |

If any of the signals below apply to your project, you should start with Docker Sandboxes.

1. The agent runs unattended, or its permission prompts are auto-approved
2. The agent needs to build images or run Compose or Testcontainers
3. The agent reads input you didn’t write, such as issues, web pages, package metadata, or MCP output
4. The agent requires API keys you don’t want inside its environment
5. The session lasts longer than a single task

Start with `sbx run claude`. Add clone mode, kits, network policy, credential mediation, and organization governance as your workflow grows.

## Sandbox the agent, containerize the application

Containers aren’t going anywhere. For services, CI jobs, and anything you package to ship, they draw the right boundary, and the ecosystem around them is the reason they’ll keep doing that work. A coding agent needs more than a container to be trusted with real work. It needs containment, meaning a boundary the model can’t rewrite, controls it can’t reason its way around, and the freedom to choose its tools and scale its setup.

Docker Sandboxes provide that containment in a microVM that can still run your containers. The boundary is also what lets the agent move faster. With it in place, you can stop approving every command and let the agent get to work.

You can have a sandbox running with one command. Start with `sbx run claude` and the [Docker Sandboxes quickstart](https://docs.docker.com/ai/sandboxes/). Once one developer’s setup needs to become a team standard, [Docker AI Governance](https://www.docker.com/products/ai-governance/) extends the same controls across your organization.

## Frequently asked questions

### Are Docker Sandboxes just containers?

No. A container is an isolated process that shares the host kernel. Docker Sandboxes are microVMs with their own kernel, filesystem, network, and Docker Engine. A sandbox can run containers, which is why the two are easy to confuse.

### Can I run Docker inside Docker Sandboxes?

Yes. Each sandbox has a private Docker Engine, so the agent can build images, run Testcontainers, and start Compose applications without the host socket or Docker-in-Docker.

### Do Docker Sandboxes replace containers?

No. Containers remain the right tool for packaged applications, CI jobs, and short-lived execution. Sandboxes add a stronger boundary for autonomous agents, and containers keep running inside them.

### What’s the difference between a container and containment?

A container isolates a workload. Containment involves the whole environment around an agent: the boundary it runs in, what it can reach, which tools it uses, and how you reproduce it. A container can be part of containment, and Docker Sandboxes add the microVM boundary an autonomous agent needs.

### What does an AI agent need from its environment?

Docker describes four requirements: containment (a boundary the model can’t rewrite), control (visibility into what the agent is doing and the ability to stop it), choice (swapping models, agents, and tools without rebuilding), and capacity (a setup other developers can reproduce and scale past one machine).

### What do I need to run Docker Sandboxes?

A supported hypervisor, which means Apple silicon on macOS 14 or later, Windows Hypervisor Platform, or KVM on supported Ubuntu systems. Running inside another VM requires nested virtualization.
