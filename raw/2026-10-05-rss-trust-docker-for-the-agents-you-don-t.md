---
"source": "https://www.docker.com/blog/docker-cloud-sandboxes-wearedevelopers-recap"
"title": "Trust Docker for the agents you don’t"
"author": "Jin Kim"
"date_published": "2026-10-01"
"date_clipped": "2026-10-05"
"category": "DevOps & CI/CD"
"source_type": "rss"
---

# Trust Docker for the agents you don’t

*Cloud Sandboxes, open Kits, and a developer community building the next generation of AI software*

**Docker Cloud Sandboxes are here.** At WeAreDevelopers World Congress North America, we launched a way for developers to start agent work in a safe way on their laptop, move to the same microVM environment on Docker-managed cloud compute, and bring the results back. Longer tasks can keep running, even after you close your laptop.

That launch reflects a bigger ambition. We want developers to be able to give agents useful work with confidence in the systems around them. That means a place for the agent to run, clear limits on what it can access, and a way to inspect what happened. It also means keeping the freedom to choose the agent and model that fit the job.

We brought that message to San Jose with Cloud Sandboxes, the open Sandbox Kit specification, and a commitment to bring the spec to the Cloud Native Computing Foundation (CNCF). Three mainstage talks explored what trust requires in practice. Four workshops gave developers time with the tools. Across the Docker Pavilion and booth, customers, partners, and community members brought their own experience and questions into the discussion.

A year after [announcing our partnership to bring WeAreDevelopers to North America](https://www.docker.com/blog/wearedevelopers-docker-unveils-the-future-of-agentic-apps/), it was exciting to join [more than 10,000 developers, AI builders, and technology leaders at the inaugural event](https://www.wearedevelopers.com/company/media/wearedevelopers-world-congress-brings-the-whos-who-of-the-software-industry-to-san-jose-in-its-north-america-debut), September 23-25. Here is what we shared, and where developers can get started.

**Introducing Docker Cloud Sandboxes**

An agent working through a large refactor or migration may need more time than you want to keep a laptop open. Running several tasks at once can put pressure on local resources, too. [Cloud Sandboxes](https://www.docker.com/blog/introducing-cloud-sandboxes-start-on-your-laptop-finish-in-the-cloud/) gives those tasks somewhere else to run.

Each sandbox is an isolated microVM, a small virtual machine with its own kernel and Docker daemon. The agent can install dependencies, build applications, and run containers inside that environment. With Cloud Sandboxes, Docker supplies the compute, and developers use `sbx`

, the same command-line tool they use for local sandboxes.

The workflow starts wherever the developer needs it to. Begin locally, move the sandbox’s filesystem to the cloud for a longer run, and bring it back when it is time to review the results. The same reusable agent packages, called Kits, work in both environments. Local and cloud credentials and policies are configured separately, so the access granted in each environment remains an explicit decision.

Cloud Sandboxes are [available now](https://agentic-platform.docker.com/), with compute billed by the second. For developers, that opens up a useful choice: keep interactive work on the laptop and give longer agent tasks their own capacity. It makes the move from local experimentation to sustained agent work a practical part of the development workflow.

**The foundation for trusting agents with more work**

In his [opening keynote](https://www.youtube.com/watch?v=G1tT3pwbsMM), Docker President and COO Mark Cavage explained why giving agents more freedom also requires a stronger foundation. He described four requirements for an agent factory: containment, control, choice, and capacity. Teams need to know where agents can act, see and stop their activity, choose their models and tools, and run work beyond a single laptop.

The keynote included a clear example of what can go wrong. An agent running in a container with the host Docker socket mounted found a way to read a secret on the host. It had not discovered a new vulnerability. It was using access the configuration had given it.

[Docker Sandboxes](https://www.docker.com/products/docker-sandboxes/) puts a microVM boundary around the agent. In a subsequent demonstration, the same attempt to reach the host through the Docker socket failed inside the sandbox. Containers still do the job of packaging and running applications; the sandbox gives the agent building those applications an execution boundary of its own.

This is what we mean by **trust Docker for the agents you don’t**. The infrastructure enforces the boundary, even when an agent chooses an unexpected course of action. Developers can decide how much access to grant and retain responsibility for the work that ships.

Cavage also addressed the limits of those controls. Blocking an unapproved network destination is different from recognizing that an otherwise permitted email is going to the wrong customer. Narrow permissions, such as allowing an agent to read and draft messages without letting it send them, remain an essential part of using agents responsibly. There is still work to do on whether an action matches the user’s intent, and we should be clear about that.

**Open Kits for environments teams can share**

Once an agent has a place to run, the next question is what belongs in that environment. Which tools does it need? Which services may it reach? What credentials and storage should be available?

The new [Docker Sandbox Kit specification](https://www.docker.com/blog/docker-sandbox-kit-spec/) puts those requirements in an artifact teams can share and review. A Kit is an OCI image containing the agent and its tools, together with declarations of the access it needs. It works with familiar image tooling: teams can build, push, pull, scan, and pin it by digest.

That makes an environment easier to reproduce, and it makes changes to its requested permissions visible. If a Kit asks for another network destination or credential, reviewers can see that change alongside the rest of the package. The runtime decides which requests to grant and enforces the resulting policy outside the agent.

We [published the specification under Apache 2.0 and committed to bringing it to the CNCF](https://www.linux.com/featured/docker-commits-to-bringing-the-sandbox-kit-spec-to-the-cncf/) for neutral governance. Docker Sandboxes is the first runtime to implement it. Opening the format gives other runtimes a specification they can adopt and developers a common way to describe an agent environment.

Nous Research joined Cavage onstage with [Hermes](https://github.com/NousResearch/hermes-agent), its open-source agent, as a launch partner. Packaging an independently developed agent as a Kit demonstrated the choice we want developers to have: use the agent that fits the work, with an environment and controls the team can understand.

**Governing agents across the organization**

[Docker CTO Tushar Jain’s keynote, “Govern the Runtime, Not the Agent,”](https://www.youtube.com/watch?v=Oc-DrLQWimc) took the discussion to the team level. Organizations use different models and agent tools. Governing each tool separately makes it harder to maintain a consistent policy and see the full picture of agent activity.

Tushar made the case for a common runtime layer that can govern execution, tools, credentials, permissions, and spend. His demo supplied a concrete example: an agent’s request to delete a GitHub repository was blocked by a default-deny rule and returned HTTP 403. Enforcement came from the runtime. In the Q&A, he described team-specific policies that can give a finance user and a developer different access to the same agent, while acknowledging that agent identity remains an open industry challenge.

Docker CISO Mark Lechner connected those ideas to security in his keynote, [“One Boundary for the Agentic Era”](https://www.youtube.com/watch?v=7lR9SUdMHPQ). His talk connected those runtime controls to the software supply chain. An agent consumes dependencies and tools, then creates code that a team has to review and ship. Lechner showed how a Kit manifest describes the agent’s requested access, and how a proxy can use a credential without exposing the raw API key inside the sandbox.

Managing those capabilities as code gives security teams something concrete to review. They can inspect the environment an agent receives and compare its permissions with the activity recorded during a task. Across the three talks, the common goal was to make greater agent autonomy something teams can govern.

**Building with our customers, partners, and community**

The Docker Pavilion kept the discussion going across Thursday and Friday, with customers, partners, and Docker engineers sharing how these ideas apply to real systems. A [field-notes panel](https://www.wearedevelopers.com/world-congress-north-america/agenda/schedule) compared lessons from rolling out sandboxed agents to thousands of developers. Our engineers took questions about Sandboxes and AI Governance. A panel with Spectro Cloud and J.P. Morgan Payments asked what it takes to own how AI is deployed and governed, beyond simply consuming more tokens.

The [customer and partner sessions](https://www.docker.com/blog/wearedevelopers-partner-customer-sessions-2026/) covered several parts of the agent workflow:

• **Running real workloads.** Spectro Cloud showed repeatable agent workloads at the edge. J.P. Morgan Payments brought a two-container payments example that starts with `docker compose up`

. ClickHouse showed what changes when a database starts from a hardened image, and BAND demonstrated separately sandboxed agents exchanging work.

• **Controlling access and investigating activity.** Palo Alto Networks connected agent audit records to investigation, while Datadog followed a security incident from detection to response. Prediction Guard demonstrated model-call controls alongside execution isolation, and Snyk showed how to inspect work inside a sandbox. GitGuardian, Mend, and Merge covered secrets, runtime guardrails, and third-party integrations.

• **Providing context and reviewing results.** Box, Cognee, and SurrealDB explored giving agents useful knowledge and memory with visible limits. Chainloop brought signed records to the review process, and Sonar showed how to verify generated code.

These sessions showed how the sandbox fits into a wider system of tools for running agents, protecting their access, and checking their work.

Eli Aleyner and Kelsey Hightower also sat down for a fireside chat at the Pavilion, bringing the cloud-native community into the program alongside customers, partners, and Docker engineers. The [platform](https://www.wearedevelopers.com/world-congress-north-america/special-events/scaling-agentic-ai) and [security](https://www.wearedevelopers.com/world-congress-north-america/special-events/agentic-ai-safety) roundtables gave smaller groups space to compare what they were seeing in their own organizations.

**Four workshops to get hands-on**

On Wednesday, September 23, our [stage and workshop program](https://www.wearedevelopers.com/world-congress-north-america/agenda/schedule) gave developers time to work with the tools themselves. All four workshops connected the larger message to practical development tasks:

• **Dan Ndombe** introduced Docker’s `sbx`

command for running agents in isolated sandboxes, then worked through network rules, tools connected through Model Context Protocol (MCP), and packaging agent workflows with Kits.

• **Michael Irwin** built an AI-ready developer environment with Kits and `sbxenv`

files, which describe a set of sandbox environments as configuration.

• **Oleg Šelajev** connected Sandboxes, MCP, and the infrastructure beneath agent workflows in a hands-on agentic platform workshop.

• **Ajeet Raina** focused on Docker Hardened Images and supply chain security when agents write the code.

The shorter talks connected those pieces to ordinary development work. Michael showed how to make an agent environment work across machines. Ajeet and Docker Captain Kristiyan Velkov covered Docker tools developers may have missed, including Testcontainers and Scout. Other sessions examined giving an agent its own machine and verifying the components agents put into a software build.

**Demos and conversations at the Docker booth**

There was plenty to explore at the Docker booth, where a steady stream of visitors could see the tools working and talk with the team. In the coding factory demo, an agent worked on a Next.js app inside its own microVM, built and served the application, and encountered a network destination blocked by organization policy. The audit view recorded the policy decision, letting visitors follow the agent’s work and see where a rule had been enforced. The demonstration connected the infrastructure controls to a familiar result: a working application developers could inspect.

The booth also hosted **Sandbox Royale**, an AI game challenge that invited visitors to connect agents through Model Context Protocol (MCP) and compete in a shared virtual town. Agents negotiated, traded fictional assets, and navigated a trust dilemma in fifteen-minute games with a live leaderboard. It was a lively way to explore how agents behave when they interact with other agents and untrusted input.

The steady booth traffic, demonstrations, and conversations gave our team opportunities to hear directly from developers about the work they want agents to take on.

**Build with us**

We came to WeAreDevelopers with a clear direction for Docker’s work in AI: make agents easier to run, make their access visible and controllable, and give developers the tools to build with them on their own terms. Cloud Sandboxes and the open Kit specification are concrete steps in that direction.

The conference gave us the chance to put that work in front of developers alongside the partners and community helping shape it. Thank you to everyone who spent time with us in San Jose. We are looking forward to seeing what you build next.

[Try Docker Cloud Sandboxes](https://www.docker.com/blog/introducing-cloud-sandboxes-start-on-your-laptop-finish-in-the-cloud/), [start locally with Docker Sandboxes](https://www.docker.com/products/docker-sandboxes/), or [explore and contribute to the Sandbox Kit specification](https://github.com/docker/sandbox-kit-spec).
