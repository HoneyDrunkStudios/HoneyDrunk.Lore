---
source: "https://unity.com/blog/ai-vibe-coding-vs-buying-managed-infrastructure"
title: "Real-time 3D with Unity Industry: What to vibe code with Unity CLI and when to rely on the foundational infrastructure"
author: "unknown"
date_published: "2026-11-23"
date_clipped: "2026-11-24"
category: "Game Development / Unity"
source_type: "rss"
---

# Real-time 3D with Unity Industry: What to vibe code with Unity CLI and when to rely on the foundational infrastructure

Source: https://unity.com/blog/ai-vibe-coding-vs-buying-managed-infrastructure

[Blog](https://unity.com/blog)

# Real-time 3D with Unity Industry: What to vibe code with Unity CLI and when to rely on the foundational infrastructure

Nov 23, 2026|15 Min

[CLI](https://unity.com/blog?topics=CLI)

[CLI](https://unity.com/blog?topics=CLI)

![](https://mip.web.unity.com/img/4pUvuYg0gyB2bkIhoO5QHLkxTu_NMTSO2B5d9UajfaE/w:1568/h:941/r:52,0,1568,941/q:75/f:avif/aHR0cHM6Ly9jZG4uc2FuaXR5LmlvL2ltYWdlcy9mdXZiampscC9wcm9kdWN0aW9uL2U0N2QxYjdlODJkZmE5NzJjNjAzMWI5N2Q3ZjcyMWZjMDQzMWVkODYtMTY3MXg5NDEucG5n.avif)

For many tasks, large language models (LLMs) now write code that's stable and fast enough to prototype and even ship with. The "citizen developer" idea we've been promising each other since the low-code days has arrived, because you can now describe what you want and get working software and automation back.

So, does every person and every company now build their own flows, wired exactly to their own needs – a new standard with strong ROI? Or will it result in teams inheriting a tangled mess of code nobody fully understands, with the need to invent job titles to cope with it: robot administrator, vibe-code solution architect, prompt janitor?

Many companies are facing these questions daily: what do we build ourselves, and when do we buy traditional SaaS (software-as-a-service)? In this piece, we explore this new dilemma and share our current perspective. For Unity teams [building industrial 3D workflows](https://unity.com/products/unity-industry), the practical question is: where should AI accelerate the functionality and features on top – the surface the user interacts with – and where do you rely on managed Unity infrastructure for the foundation?

## Key takeaways

- Vibe coding is strongest for the functionality and features you add on top of Unity work. This is where [Unity CLI](https://unity.com/resources/a-beginners-guide-to-unity-cli-and-the-pipeline-package) (command line interface) and agentic AI, together with [Unity Industry](https://unity.com/campaign/unity-industry-product-walkthrough-demos), help teams take action inside the Unity Editor: with prototyping, UI, custom Editor tools, and the C# scripts that connect all the logic for animation, audio, non-player character (NPC) behavior, and more.
- Buy the foundation for load-bearing work: [proprietary CAD import, asset management](https://unity.com/resources/cad-to-real-time-3d-pipeline), security, versioning, compliance, and multi-user workflows. Unity’s managed tools provide the governed infrastructure underneath.
- AI can speed up creation, but production systems still need testing, maintenance, access control, and long-term ownership.
- The best approach is to combine the two. Run on a managed foundation, then build the interfaces and flows on top that match how your team actually works, whether that is automation, sharing, or optimization.

## AI and Unity CLI take Unity’s well-known extensibility into the future

We launched our new [Command Line Interface](https://www.youtube.com/watch?v=DgNrgZeJOxQ&t=1s) (CLI), which gives an LLM a streamlined interface to key commands, runtime execution, and an Eval command that runs C# directly in the Unity Editor with no domain reload.

Unity has always been flexible and built for many kinds of work, with C# as the connective layer. In the past, this meant a developer had to set up both the application logic and the tools other team members needed to work independently. The CLI speeds up iteration for both: it works with common AI agents and CI/build systems, and can reach the runtime. Developers get a faster, more stable interface for work such as building tests and CI/CD setups. Designers and technical artists can prototype more quickly, spawning prefabs, assembling scene logic, blocking out environments, setting up navigation, or building tools such as an audio manager or spline-based animation.

None of this required us to rebuild the engine around AI. Unity has been extensible for years, with open APIs, a scripting layer, a deep package ecosystem, and C# as the extension point for nearly everything. Compared with more monolithic software, that architecture leaves a large surface an agent can operate through, and the Eval command in the CLI makes it directly reachable.

The practical result is that you can largely prompt your way through project setup, scene creation, performance work, asset creation, and test runs inside the [Unity Editor.](https://unity.com/products/unity-engine) But the Editor and the full [Industry suite](https://unity.com/products/unity-industry) are paid software, with subscriptions that grow at scale. So if an agent can now reach almost any part of Unity, the tempting question is: why not build more of the ecosystem yourself, your own asset manager, transform toolkit, or flow automation, and save on the subscriptions?

## First, let's agree on what the terms mean

This piece is about where vibe coding enhances the experience and where it adds more noise than value. Two quick definitions first:

**Vibe coding** describes prompting an LLM in plain language to write the game code and set up the game systems and features. You don't read every line; you steer by results. It’s fast and useful for prototypes and small tools. (Andrej Karpathy coined the term, and has since drawn the same line we draw here, toward what he calls [agentic engineering](https://www.youtube.com/watch?v=96jN2OCOfLs).)

**Agentic AI** goes further. Instead of handing back code, the model takes actions itself, runs scripts, edits files, chains steps toward a goal. The Unity CLI supports this pattern, so you can plan and execute tasks while working on something else.

## What you can vibe, and what you can't

Modern real-time 3D software has many parts, and some are a great fit for vibe coding, [like the UI](https://www.youtube.com/watch?v=SwuGB3quO2k), and the binding between the front end and the back end. The Unity ecosystem in particular is driven heavily by a layer on top, the Editor scripts and custom functionality you add yourself, and that upper layer is where vibe coding is most effective.

The parts underneath are a different story: getting 3D data in, optimizing it, and versioning, security and user roles. And then there's everything that comes with running software many people depend on at scale: service-level agreements (SLAs), bug reporting and fixes, upgrades, and a whole software lifecycle to maintain. In short, the load-bearing structure.

For shorthand: let’s call the upper layer the **surface** and the load-bearing layer the **foundation**. Concretely, the surface is what you build on top: your scenes, UI, scripts, the custom Editor tools you add, and the scripts you run to [automate your CAD-to-3D asset pipeline](https://unity.com/blog/automating-3d-production-pipelines-with-unity). The foundation is everything Unity provides underneath, not just [Unity Asset Transformer,](https://unity.com/products/unity-asset-transformer) [Unity Asset Manager](https://unity.com/products/asset-manager) and pipeline automation, but the engine itself: rendering, physics, audio, animation, multiplatform support, the compiler, camera systems, the recorder, and the hundred-plus other packages and systems that together make up the Editor.

AI performs well on the surface. But can it build the foundation too?

## Unity Industry ecosystem

![A flow chart suggesting where you can use agentic workflows and where to rely on foundational infrastructure ](https://mip.web.unity.com/img/7f_Q_8zGCKd-eQlT2o0ZlRcV-6m9IkpsOhNNV97IrFQ/w:3000/h:2460/q:75/f:avif/aHR0cHM6Ly9jZG4uc2FuaXR5LmlvL2ltYWdlcy9mdXZiampscC9wcm9kdWN0aW9uL2YzZWQ2ZGQxYjY1YTk5YTI1MTFkMDZmNTczMzYyYWI2MTBiOGI2YTMtMzAwMHgyNDYwLnBuZw.avif)

## Where vibe coding shines: the surface

Why does AI do well on the surface? Because a model performs best where there is a large body of online public material, like there is for Unity content: reference UIs, code samples, and forum threads. That is a function of training data rather than luck, and it is what makes the surface the right place to let a model run.

Let’s look at two examples of vibe coding inside the Unity Editor.

### Example of vibe coding in the Unity Industry Ecosystem

#### A car cluster from a moodboard

Drop reference images into the agent, describe the intent, and you can vibe code a working HMI cluster in uGUI with speed, battery level, and a link between the two dials, then refine from there. In our own test, built with an LLM agent connected to the Editor, work that previously would have taken days or weeks, relying on a static prototype and several rounds between a designer and a developer, came together in a few hours in a single working session.  
**Learn more:** [Automotive HMI sample for embedded-style hardware](https://unity.com/blog/unity-industry-hmi-template-for-embedded-systems)

![](https://mip.web.unity.com/img/ff0STH75AMTjmmNLXJO27inAGDl38mVh88u4OqiafeY/w:2000/h:324/q:75/f:avif/aHR0cHM6Ly9jZG4uc2FuaXR5LmlvL2ltYWdlcy9mdXZiampscC9wcm9kdWN0aW9uLzVlZWE0MWZlNWVkOWNmNjZkMzYzNWU0ZmJhNTZmNzBmMDRmMGYwYmItMjAwMHgzMjQucG5n.avif)

Connect an LLM agent to Unity and the agent can act inside the Editor through the CLI: create scenes and GameObjects, set component values, write and edit C# scripts, read the console, and trigger Editor actions, all from plain-language prompts.

#### Add new functionality and control UI.

In this example, a [digital twin](https://unity.com/campaign/xr-for-industry) application simulates robot behaviors, with a UI displaying telemetry, placement, and overall health for an entire distribution center. Individual robot and camera controls, however, are missing. With a few prompts and a set of design guidelines, vibe coding adds that functionality and a matching UI, giving users more direct control over individual robots.

![](https://mip.web.unity.com/img/ydbuEpXT2rIRwaV4gJiILb84WvFWkUv0jwcT82FoD7w/w:2000/h:324/q:75/f:avif/aHR0cHM6Ly9jZG4uc2FuaXR5LmlvL2ltYWdlcy9mdXZiampscC9wcm9kdWN0aW9uLzc5ODc0NjczNTY0YjhmZmQ4ZGQ5OTQwN2RhYzVhODIwYzkxZTJjYWItMjAwMHgzMjQucG5n.avif)

The generated logic checks the runtime platform: when it detects a touch device, it automatically enables the on-screen touch controls: the **MOVE** (WASD) and **ORBIT** pads and the **AUTO / MANUAL** switch.

Also see how we are improving this workflow:

![Prototyping UI Toolkit with Unity CLI](https://img.youtube.com/vi/SwuGB3quO2k/hqdefault.jpg)

#### Integrating AI connectors into a pipeline automation workflow

Using vibe coding,we can build custom scripts and features quickly enough to stand up a new automated pipeline. We built a flow that sends a 2D image to Unity Asset Manager, which automatically triggers a hand-off to a third-party 3D generator. Once the 3D asset is created it passes back to Unity Asset Manager, ready to deploy in [Unity Studio](https://unity.com/products/unity-studio), the Unity Editor, or any companion 3D application. Writing these scripts with an agent makes the setup faster and more accessible to less technical users.

![The AI-driven pipeline automation example](https://mip.web.unity.com/img/ip3SzxgLQ6Db8Kw3tkSV0ZU79s3SFzTKr4H9lpjkmKM/w:3420/h:1217/q:75/f:avif/aHR0cHM6Ly9jZG4uc2FuaXR5LmlvL2ltYWdlcy9mdXZiampscC9wcm9kdWN0aW9uLzQ4ZmI5YzI1MGRlYjM1MTYxMjEyM2FiODlkMGNmMmM2ZTVkZmRiMzctMzQyMHgxMjE3LnBuZw.avif)

## Where it stops being worth it

Vibe coding something for yourself, or for prototyping, works well: a tool to speed up your own pipeline, a script to optimize a step. Hosting it locally for one or two people is fine too. The economics change when it’s a commercial application that has to serve a team: security, access permissions, multiple users, reliable hosting, and the critical infrastructure. That is not where the code is hard. It is where the *ownership* is.

Many software engineers draw the same line from the engineering side: AI gets you most of the way to a working app fast, but the last stretch, the part that makes it production-ready, becomes hard without deep engineering knowledge. The release process, hidden maintenance costs, fixes that introduce new bugs, and the security holes that show up the moment something real is at stake. The conclusion is that AI coding tools are powerful, but production software still requires accountability, craft, review, testing, security, and collaboration.

Take a concrete case: a local asset manager with versioning for heavy 3D models. The UI and the simple logic are easy to prototype. But map out the rest, such as the storage, versioning, access control, and the hardware to run it, and the argument strengthens for choosing a proven asset manager solution. Also keep in mind that the software you buy also uses AI behind the scenes, which makes their products better and evolve faster. And it is built by a dedicated team of specialists, at a scale and with an infrastructure that a single engineer working on the side typically cannot match. Both get faster with AI, so the real question is where to split: what you write code for yourself, and what you get from the product you buy.

![](https://mip.web.unity.com/img/hYlm-8kq5_A6bmBxdg4ooiDWnTM4Ti1a2BKWDKFAxUQ/w:1320/h:720/q:75/f:avif/aHR0cHM6Ly9jZG4uc2FuaXR5LmlvL2ltYWdlcy9mdXZiampscC9wcm9kdWN0aW9uL2VmN2ZlNmUyM2EwODQyMjgzM2YyMGEzNWRkYjBkOTY0M2Y4NjNiZDAtMTMyMHg3MjAucG5n.avif)

For illustrative purposes only, not based on actual numbers.

## Remember: What you build has to be maintained

Code is written once and maintained for years. The moment something breaks, or you push a fix, someone has to understand what the AI actually wrote, so the change doesn't quietly break something else. This is sometimes referred to as the [comprehension debt](https://addyosmani.com/blog/comprehension-debt/): the burden a codebase carries when no engineer fully understands the logic the AI generated. And it compounds: if the issues do not get cleaned up, they accumulate.

Over time this will most likely improve. Agents will increasingly write their own tests and run release-acceptance checks before deployment, and the people prompting them will get better at setting guardrails. But standing that up is a new capability in its own right, and it needs a team to own it. In automating the primary work, you inherit the operational burden around it. That infrastructure, the test suites, the release gates, and the people accountable for keeping updates safe, is exactly what a managed platform provides. It is also what a subscription covers: the underlying cost of running the software reliably.

Usage-based AI costs are another variable to plan for when AI-built tooling becomes critical infrastructure. If an AI-built setup and its upkeep become critical infrastructure, you take on exposure to the cost of the underlying models. As the market shifts, so can your bill, and you may have limited ability to cap it.

## The part AI cannot reliably learn: proprietary CAD

There is one part of this that is not about discipline or maintenance. It is about what the model can realistically know.

Vibe coding works well when the problem space is public, documented, and abundant in training data: glTF, OBJ, JSON, REST, Python, Unity APIs, and similar open workflows.

Proprietary industrial CAD data is different. Native formats like CATIA, NX, Creo, and SolidWorks are not openly documented in the same way, so the source knowledge needed to interpret them correctly is not reliably available to the model. That makes errors more likely, especially in areas like tessellation, hierarchy, metadata, or assembly positioning.

AI can still help around the workflow, automation, UI, and integrations. But the core translation of proprietary CAD data depends on specialized, maintained interoperability technology, access to closed formats, and years of accumulated expertise.

## The thing you don't want to own yourself: security

For many enterprise customers, the biggest concern is not speed. It is trust: security, access permissions, data handling, and auditability.

This is also where a home-built or AI-generated pipeline can quickly become risky. Secrets end up in logs. Access control is added too late. Multi-user permissions are improvised instead of designed. And once real customer data, production assets, or proprietary CAD files are involved, “good enough” will not cut it.

This is where buying flips from cost to advantage. With enterprise SaaS, you are not only buying features. Enterprise platforms help provide tested security practices, access controls, and documentation customers can review. Unity’s security and compliance materials, including relevant SOC 2 reports for in-scope services, are available through the [Unity Trust Center,](https://trust.unity.com/certifications) with official reports available by request where applicable.

## Why Unity is strong foundation in the AI era

AI integration is important to the Unity architecture, and it is not an afterthought. This matters for a practical reason: our long-standing API-first approach, open APIs, scripting capabilities, and package ecosystem mean external agents and AI models can connect without custom plumbing. The [Unity CLI](https://docs.unity.com/en-us/unity-cli) works with the LLM you choose, and documented APIs across our SDKs let you build custom tools on top of the platform. That architecture is why vibe coding fits Unity well: you get a stable foundation, and the freedom to build surface features on it.

The result is a vetted, governed foundation that meets AI at well-defined integration points, so you can build your own features on top without touching the core infrastructure underneath.

## A high-level guide for what to vibe and what to avoid

When you are unsure where a task falls on that spectrum, ask two questions. Is this a one-off job, a prototype, or a low-risk change such as a UI update? Or does it handle confidential material and customer data, or require broad user access and role controls? If it is temporary and low-risk, try vibe coding it. If it touches production data, credentials, or systems other people depend on, rely on the foundation and govern it properly.

**Task**

One-off scripts (rename, sort, convert a batch of files)

**Vibe it?**

**Yes**

**Why**

Runs once, nothing depends on it, and you can discard it afterward

Custom Editor tools (e.g. a material replacer tool or gameobject merger

**Vibe it?**

**Yes**

**Why**

Solves your own concrete need, you own the result

Viewer / UI work, prototypes, proof-of-concepts

**Vibe it?**

**Yes**

**Why**

AI does well here, so you can test several directions quickly. Shifting the look and feel or adding interactivity is fast enough to prove a concept and gather feedback early.

Glue between two systems you control, with you in the loop

**Vibe it?**

**Maybe**

**Why**

Acceptable for occasional, ad hoc use; once it needs to run unattended, stability matters far more, and reviewing AI output can take longer than doing the work by hand

Reading proprietary CAD formats (CATIA, NX, Creo, SolidWorks…)

**Vibe it?**

**No**

**Why**

Not openly documented at the level needed for reliable translation, so the model has little reliable information to work from

Secrets, tokens, access control

**Vibe it?**

**No**

**Why**

One gap leaks across the whole org.

Production-grade CAD conversion / tessellation

**Vibe it?**

**No**

**Why**

The hard edge cases are exactly where quick solutions break.

Versioning tools and asset management

**Vibe it?**

**No**

**Why**

A solved problem; rebuilding it reinvents what already works

Anything touching customer data, compliance, or private cloud

**Vibe it?**

**No**

**Why**

The wrong place to improvise; Managed platforms provide controls that help support your compliance program

**Task**

**Vibe it?**

**Why**

One-off scripts (rename, sort, convert a batch of files)

**Yes**

Runs once, nothing depends on it, and you can discard it afterward

Custom Editor tools (e.g. a material replacer tool or gameobject merger

**Yes**

Solves your own concrete need, you own the result

Viewer / UI work, prototypes, proof-of-concepts

**Yes**

AI does well here, so you can test several directions quickly. Shifting the look and feel or adding interactivity is fast enough to prove a concept and gather feedback early.

Glue between two systems you control, with you in the loop

**Maybe**

Acceptable for occasional, ad hoc use; once it needs to run unattended, stability matters far more, and reviewing AI output can take longer than doing the work by hand

Reading proprietary CAD formats (CATIA, NX, Creo, SolidWorks…)

**No**

Not openly documented at the level needed for reliable translation, so the model has little reliable information to work from

Secrets, tokens, access control

**No**

One gap leaks across the whole org.

Production-grade CAD conversion / tessellation

**No**

The hard edge cases are exactly where quick solutions break.

Versioning tools and asset management

**No**

A solved problem; rebuilding it reinvents what already works

Anything touching customer data, compliance, or private cloud

**No**

The wrong place to improvise; Managed platforms provide controls that help support your compliance program

## So: vibe or buy?

If it is temporary, personal, or on the surface, a script, a tool, a UI, a prototype, vibe it. The model has seen a great many examples of that work and you will be done faster. If it reads a closed CAD format, holds a credential, or has to still work in two years when the person who prompted it has moved on, buy it. Not because AI cannot write the code; it usually can. But somebody has to own it, and be responsible for its long-term stability and maintenance.

So, should you vibe or buy? We have outlined when to choose each, but the more useful answer is that you combine them. Let a managed foundation carry the load-bearing work, and keep the flexibility to build custom use cases on top with vibe coding. Vibe code the surface, the UI, prototypes, and one-off tools; buy the foundation for the essentials such as data handling and security. AI on its own is fast, but it has nothing underneath it to guarantee the result, and a foundation on its own still leaves the last mile of your workflow unbuilt. Together, the foundation gives you something to check the AI’s output against, and the AI makes building on that foundation considerably quicker. The ability to prototype and build on the **surface** has changed how quickly our projects move, without changing what we rely on underneath.
