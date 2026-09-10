---
source: "https://www.thoughtworks.com/insights/blog/generative-ai/how-to-talk-with-ai"
title: "How to talk with AI?"
author: "Javier López Fernández"
date_published: "2026-09-08"
date_clipped: "2026-09-10"
category: "Software Architecture"
source_type: "rss"
---

# How to talk with AI?

Source: https://www.thoughtworks.com/insights/blog/generative-ai/how-to-talk-with-ai

How to talk with AI?
Not to write better prompts, but to build a better understanding of intent between humans and AI
Blogs
Back
Blogs
Back
Close
Generative AI
Blog
By
Javier López Fernández
Published: September 08, 2026
We are currently suffering from a bizarre industry-wide obsession: prompt engineering.
Every week, a new “prompt wizard” posts a cheat sheet claiming that if you frame your request with the right magic incantations “Act as a Senior Principal Architect with 20 years of experience...” the AI will suddenly emit flawless, production-ready software.
This is not software engineering. This is spell-casting.
The fundamental flaw of the prompt engineering Illusion is simple: natural language is ambiguous, and LLMs (large language models) are non-deterministic black boxes. You can spend hours tweaking a five-paragraph prose prompt, but reading the AI’s polite, conversational reply tells you absolutely nothing about how it has interpreted the request about your codebase or your user’s problem.
The real challenge of AI-assisted development isn’t forcing a model to generate syntax. It is uncovering intention: exposing the AI’s internal blueprint before it touches a single line of production code.
The asymmetric dialogue: We speak prose, the AI responds in contracts
As humans, natural language is our natural superpower. It is effortless, expressive and fast for us to express intent, critique ideas and refine direction in plain English. For the AI, however, natural language responses are a fog of polite, statistical text that masks what the model actually plans to build.
This reveals the ideal asymmetric dialogue for AI-driven engineering: We speak to the AI in natural language, but the AI must respond to us in formal languages.
We shouldn’t want the AI to answer with long, conversational paragraphs explaining its philosophy. We need the AI to answer with concrete, unyielding artifacts: a snippet of code, a focused architectural diagram, a type definition or a failing test assertion.
By forcing the machine to speak in formal structures while we guide it with natural language, we establish a crystal-clear communication boundary:
The AI makes its interpretation visible: Formal artifacts make hidden assumptions much harder to conceal.
The human gets a visible anchor: Instead of critiquing abstract ideas, you use plain English to give surgical feedback directly on the visible code or diagram (“This interface leaks domain logic into the persistence layer,” or “This test scenario misses the refund boundary condition”).
This asymmetry plays directly to both strengths: human expressive intuition guiding machine-driven formal precision.
Even with formal artifacts, our human cognitive capacity is strictly limited. We cannot perform a meaningful mental model check on an AI that dumps a proposed change spanning fifty files, three complex diagrams and hundreds of lines of code. When the batch size explodes, our ability to spot logical errors drops significantly.
To make this asymmetric loop work, we must drastically shrink the batch size of every interaction and iterate through problems incrementally.
We must demand that the AI responds in micro-increments: a single test assertion, a five-line interface definition or a tiny structural diagram. By keeping the batch size small, we keep human cognitive load near zero, spot misunderstandings instantly and maintain complete control over the evolving architecture.
Uncovering intention through tiny, visible artifacts
Instead of asking the AI to guess what you want from a mega-prompt, force the machine to expose how it has interpreted the request in tiny, digestible increments.
We need to limit the batch size of every planned step to something a human brain can evaluate in seconds: one test assertion (perhaps two), a tiny schema change, a single interface definition.
Once the AI generates this small, visible artifact, the workflow transforms completely:
The AI exposes its intent: You see its proposed logic in hard syntax that cannot hide behind vague English prose or massive multi-file pull requests.
The human leverages natural language on concrete code: You no longer need to write a master-class prompt from scratch. You point directly at the tiny, visible artifact and give surgical feedback (“This assertion misses the boundary case when the balance hits zero”).
Cognitive load remains near zero: Because the increment is micro-sized, you process it effortlessly without losing context.
The aim is to inspect each artifact closely enough to correct the AI’s direction early and reduce the ambiguity inherent in natural language.
Why end-of-line code reviews are dead
This micro-batch approach challenges the traditional end-of-process pull request model.
In this model trunk-based development and continuous code reviews in micro-steps make much more sense.
Waiting for the AI to generate a huge feature and conducting a “code review at the end” is an obsolete anti-pattern. By the time fifty files have been generated, you are no longer reviewing logic; you are just rubber-stamping syntax you don’t fully comprehend.
Instead, human engineering must shift into the live, continuous development loop. Being present at every tiny step serves a dual purpose:
You align the machine: You ensure the AI truly understands the problem’s hidden domain rules before it builds on top of bad assumptions.
You learn the solution as it evolves: By co-designing micro-increments, you build a deep mental context of the system. You don’t just ship software faster, you actually understand what you shipped.
Imagine a continuous checkpoint. The AI presents a micro-blueprint: a single failing test or a five-line type definition representing the next incremental step. You inspect it, offer quick natural language feedback on that specific visible code, lock in the intent and let the AI fulfill that micro-contract. Repeat.
The three-step intentional dialogue
To move past prompt engineering, establish a low-cognitive-load loop focused on exposing, inspecting and refining intent in micro-batches:
Step 1: Exposing the micro-blueprint (intent check)
Feed the AI the user problem and formal acceptance criteria (using specification by example). Instruct the AI: “Do not write feature implementation yet. Show me your intended next step as a tiny, visible contract with just one failing test or interface signature.”
Step 2: Surgical human feedback on visible code
Leverage your natural human strength. Inspect the micro-artifact. Use quick, conversational feedback to critique the visible code (“Reuse this domain entity instead of inventing a new DTO here”). The AI adjusts the plan instantly with relatively little rework.
Step 3: Micro-execution & co-learning
The AI implements the minimal logic to satisfy the tiny contract. Because you were present during the creation of this small step, you fully understand the code, reduce knowledge debt and guide the system toward clean, maintainable architecture.
Automated feedback: Letting fitness functions do the talking
While natural language is ideal for human critique, manually reviewing every micro-increment can still create friction. To keep velocity high without sacrificing rigor, we must delegate the primary feedback loop to automated mechanisms: hooks and fitness functions.
When an AI proposes a formal artifact, a code change, a test or a schema modification, we shouldn’t rely solely on manual inspection. Instead, we plug the AI directly into deterministic feedback loops within our development environment:
Compiler & type checks: Catching structural mismatches and type violations instantly.
Linters & architectural rules: Enforcing code style, layer boundaries and dependency constraints automatically.
Automated test runners: Verifying whether the proposed logic satisfies existing invariants or makes new assertions pass.
Fitness functions: Running architectural assertions that measure coupling, complexity metrics or security boundaries.
Crucially, these hooks must respond in formal, unambiguous language.
When a git hook or test runner fails, it shouldn’t send the AI a vague summary. It must feed the AI exact stack traces, compiler errors and failed assertion diffs. This provides the LLM with a zero-ambiguity feedback loop: the machine generates a formal proposal, the automated fitness function evaluates it against deterministic rules and the AI corrects its own trajectory before the human even looks at the result.
By placing automated formal checks at the gate, we free human judgment for what matters most: evaluating high-level domain intent and guiding architectural design.
The latency trap: Engineering low-latency feedback loops
There is a catch to relying on automated hooks and continuous iteration: waiting on slow feedback loops will destroy your developer velocity.
If every micro-step requires running a 10-minute test suite, waiting for a full monolithic build to compile or watching an LLM churn through thousands of tokens, you will spend half your day staring at progress bars. That isn't a flow state; it’s paralysis.
A core responsibility of modern software engineering is driving down feedback latency. If we want AI agents to iterate continuously against automated hooks, we must engineer our systems and test strategies so that feedback happens feedback happens as quickly as practical rather than requiring long-running cycles:
Optimizing the test pyramid: Pushing test coverage down from slow, brittle end-to-end UI tests to lightning-fast, isolated unit tests. If a business rule can be verified in a domain unit test, never force the AI loop to wait on an integrated browser or a heavy database container.
Selective test execution: Configuring test runners and git hooks to execute only the scoped tests relevant to the changed module or impacted boundary, rather than running the entire repository on every micro-commit.
Decoupled deployment units: Breaking large, tightly-coupled systems into modular components or smaller deployment units so compilation targets remain small and hyper-focused.
Optimizing the AI feedback loop is fundamental Lean engineering: shrink the batch size, eliminate waiting time and protect the team’s flow state. If your AI pipeline is slow, don’t write bigger prompts to avoid running it: fix your architecture and test distribution so the feedback loop becomes instantaneous.
Stop being a prompt wizard, start being a contract validator
The future of software engineering with AI has nothing to do with memorizing prompt hacks, master-class templates or magic natural language tricks.
Prompting in a vacuum leads to hallucinated architectures, unreviewable code and complete loss of human context. The real power of AI-assisted engineering emerges when we speak in natural language to demand tiny, formal artifacts in return: giving us concrete code and diagrams to critique, learn from and validate.
Stop trying to write the perfect prompt to guess what the AI will do. Stop thinking that the solution is big design upfront . It’s not. It never was.
Speak in prose, demand formal artifacts in return, keep the batch size small and build the software together.
Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.
More insights
Generative AI
From specification to production: Building enterprise software with agentic AI
Learn more
Generative AI
Why generative AI won't create 10x developers
Learn more
Legacy modernization
The agentic frontier: Modernizing commodities trading through AI ecosystems
Learn more
Explore a snapshot of today's tech landscape
Read Tech Radar
