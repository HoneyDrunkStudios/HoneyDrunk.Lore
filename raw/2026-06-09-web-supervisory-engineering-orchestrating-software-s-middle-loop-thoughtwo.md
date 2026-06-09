---
source: "https://www.thoughtworks.com/en-ca/insights/blog/agile-engineering-practices/supervisory-engineering-orchestrating-software-middle-loop"
title: "Supervisory engineering: Orchestrating software’s ‘middle loop’ | Thoughtworks Canada"
author: "Richard Gall"
date_published: "2026-06-03"
date_clipped: "2026-06-09"
category: "Software Architecture"
source_type: "web"
---

# Supervisory engineering: Orchestrating software’s ‘middle loop’ | Thoughtworks Canada

Source: https://www.thoughtworks.com/en-ca/insights/blog/agile-engineering-practices/supervisory-engineering-orchestrating-software-middle-loop

Supervisory engineering
Orchestrating software’s ‘middle loop’ 
Blogs 
Back 
Blogs 
Back 
Close 
Agile engineering practices
Generative AI
Blog
By 
Richard Gall 
Published: June 03, 2026 
For decades, software development was neatly organized into two core rhythms: the inner loop and outer loop. The inner loop largely happened in your IDE: writing functions, running local tests, fixing syntax. The outer loop, meanwhile, was everything that happened after you typed `git push`: code reviews, CI/CD pipelines, staging environments and deployment.
But things have changed. Generative AI and autonomous coding agents have broken this two-loop mental model. Agents are now able to churn out a hundred lines of syntactically perfect code in a matter of seconds. The bottleneck is no longer around how fast we can type or implement code, it's about how fast we can verify.
This change is nothing less than a brand-new layer in software development: the middle loop. What’s more, this middle loop requires a new approach to software; one we’re calling supervisory engineering .
What is the 'middle loop'? 
To understand the middle loop, we need to look at how software engineering is being structurally re-architected as a result of AI .
Historically, software development was a binary model: you wrote code (inner loop) and then you deployed it (outer loop). The middle loop can be understood as a new operational layer that has been forced into existence by the volume and speed of AI-generated code. It’s the phase where human judgment rubs up against machine execution.
To see why the middle loop is distinct, contrast it with the traditional two:
The inner loop. Historically, this was a human engineer typing, compiling and fixing syntax errors locally. Today, AI agents are taking over much of this work: an agent can spin up a local environment, write functions and iterate until the code compiles.
The outer loop. This is the realm of DevOps and platform engineering — CI/CD pipelines, automated security scanning, containerization and pushing to production.
The middle loop. This new layer is triggered the moment an AI agent proposes a solution. In the middle loop, the human engineer evaluates whether the agent actually solved the right problem, ensures the code doesn't introduce architectural drift and orchestrates how multiple agent-created components fit together.
The middle loop in practice: Supervisory engineering 
In the middle loop you aren't writing code from scratch. You’re supervising a system. However, the word supervisory shouldn’t be taken to mean that developers have little to do other than watch over systems and correct things if they go wrong. There is, in fact, lots of things they still need to do.
Aligning intent and setting constrains 
Before an agent builds, the supervisor needs to establish the necessary parameters in which it can do so. This involves feeding the agent precise architectural constraints, API specifications and style guides. Prompting an agent to build something is easy; getting it to build the right thing in the right way is another matter; it requires the knowledge and experience of a software engineer in this new supervisory role. 
Multi-agent synthesis 
Modern AI workflows don't just rely on one LLM. One agent might write frontend components, another refactors the backend API and a third generates database migrations. The middle loop is where the engineer must synthesize these parallel work streams. You ensure Agent A’s output cleanly integrates with Agent B’s output without breaking the overall system architecture.
Differential and behavioral review 
In a traditional code review, you look at a pull request (PR) written by a peer to catch logic flaws. In the middle loop, you’re reviewing a massive wall of code generated in seconds. Your review shifts from checking how the code was written to verifying what the code does. This involves running behavior-driven tests, checking for hidden hallucinatory bugs and ensuring the agent didn't take bizarre shortcuts to make a test pass.
Gatekeeping and guardrails 
The middle loop should be treated as a kind of filter stage, one that needs to be passed before anything touches your CI/CD pipeline. It’s where you apply automated policy-as-code, run targeted integration testing and make the high-stakes executive decision: is this machine-generated code safe enough to merge into our core repository? 
The three pillars of supervisory engineering 
Another way to understand supervisory engineering is through the prism of three key pillars: directing, evaluating and correcting. Together these underline the overall shift that is taking place in software engineering as engineers get to grips with the middle loop.
Directing. This goes way beyond basic prompting. It involves breaking a massive system architecture down into "agent-sized" chunks, managing context windows and explicitly codifying engineering standards so an agent doesn't hallucinate its own design patterns.
Evaluating. This is the hard part. It requires deep system context to read highly plausible, beautifully indented code and instantly ask: ‘Did this catch the edge cases under heavy load? Is it using a deprecated API? Is this just confident nonsense?’
Correcting. Stitching together three different codebases generated by three different agents working in parallel, maintaining architectural coherence and ensuring the systems mesh seamlessly.
Beyond those three pillars, perhaps the most important thing to remember is this: you used to slow down while writing code; now, you have to force yourself to slow down while reading, questioning and auditing it.
The skill that scales 
The surface area of engineering responsibility hasn't shrunk; it has expanded. The industry no longer requires you to be a walking syntax dictionary. Instead, it values:
Strong mental models of system architecture. 
Mechanical sympathy/sensitivity to how your software functions. 
The ability to delegate and orchestrate complex tasks rather than manually implementing them. 
Junior developers may need to adapt and even bypass the traditional "syntax-mastery" phase to learn the art of rigorous evaluation (although that remains open to question). Senior engineers who have spent decades debugging systems should, though, already possess the exact intuition needed to act as effective supervisors.
The future of software engineering isn't human vs. machine; it's human judgment managing machine velocity.  Welcome, then, to the middle loop; it’s time to put your expertise and experience to work and supervise. 
Generative AI 
Why context engineering is like teaching AI to skip stones
Learn more 
Generative AI 
GitHub Copilot and me: The evolution of my partnership with a coding assistant
Learn more 
Generative AI 
Harness engineering and agent feedback: Exploring AI coding sensors
Learn more 
View more 
View less 
Explore a snapshot of today's tech landscape 
Read Technology Radar
