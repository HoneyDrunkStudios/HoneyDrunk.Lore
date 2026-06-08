---
source: "https://80.lv/articles/technical-artist-on-building-tools-pipelines-and-blending-art-with-engineering"
title: "Technical Artist on Building Tools, Pipelines, and Blending Art with Engineering"
author: "80 Level"
date_published: "2026-05-20"
date_clipped: "2026-06-08"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Technical Artist on Building Tools, Pipelines, and Blending Art with Engineering

Source: https://80.lv/articles/technical-artist-on-building-tools-pipelines-and-blending-art-with-engineering

# Technical Artist on Building Tools, Pipelines, and Blending Art with Engineering

Ryan Amos joined us to talk about how it has been for him to work on different projects, the problems with production pipelines, building tools that can make the work easier, the connection between art and engineering, and his thoughts about technical art and its evolution.

**You've worked across AAA, AA, mobile, and simulation projects for many years. How has your approach to technical art evolved across such a wide range of platforms and production environments?**

Early in my career, I was already looking for ways to save time and make workflows more predictable and harder to break. Even when I was focused on environment art, I was constantly building small tools or processes to remove friction.

Over time, that evolved into thinking more in terms of systems. Working across mobile and simulation especially forces you to respect constraints (memory, performance, iteration time), and that discipline carries into AAA, where scale amplifies every problem.

Now my approach is centered around building workflows that prevent issues rather than reacting to them. If something breaks repeatedly, that's usually a pipeline problem, not an artist problem.

**Your career consistently focuses on building tools and pipelines. What do you see as the most common inefficiencies in production pipelines today, and how do you typically approach solving them?**

The biggest inefficiencies are a lack of visibility and poor structure. Teams often don't know something is wrong until it's already affecting performance or stability. On top of that, weak project organization (inconsistent naming, messy folder structures, and a lack of useful documentation) compounds those problems over time.

- I focus on addressing both sides
- Pushing validation and feedback earlier in the pipeline
- Establishing clear naming conventions and folder structures
- Creating documentation that's actually useful, maintained, and easy to access

If knowledge only exists mentally, it becomes a liability. When someone leaves, that knowledge leaves with them. Getting structure right early pays huge dividends later. It keeps teams aligned, surfaces issues faster, and makes complex tasks repeatable instead of fragile.

**You've worked extensively in Unreal Engine, including helping studios transition from proprietary engines. What are the biggest challenges teams face during that transition, and how can technical artists smooth that process?**

The biggest challenge is mindset, not technology. Teams often try to recreate their proprietary engine inside Unreal Engine instead of adapting to how the engine is designed to work. That usually creates unnecessary complexity. Another challenge is that things don't usually map cleanly 1:1. Asset structures, workflows, and systems all behave differently.

While I've spent the last several years working heavily in Unreal Engine, I've also worked extensively in Unity earlier in my career. Across both, the underlying concepts are very similar. They're just exposed differently. I've found it helps to give teams a clear mental and visual map of what equates to what, so they can form those connections more quickly.

Technical artists can smooth the process by:

- Translating workflows into engine-native approaches
- Establishing standards early
- Building bridge tools where needed

The goal is to reduce friction quickly so teams can focus on making content, not fighting the engine.

**Lighting has been a key area of your work. How do you approach building lighting pipelines that balance artistic intent with strict performance and memory budgets?**

It starts with defining constraints early and making them visible. Lighting can become unpredictable without clear guidelines around light usage, shadowing, and material response. I focus on establishing those baselines along with reusable setups and ensuring that lighting artists have a good mental model of associated costs. Once the cost is clearly defined, it allows them to be much more intentional and accurate with how they create their work.

Lighting is also one of the areas I enjoy most, so I try to stay hands-on with teams. Working directly with lighting artists builds ownership, creates mentorship opportunities, and helps ensure we're aligning with art direction while staying within budget. When constraints are clear, artists can make informed decisions, and that's when you can really push quality without breaking performance.

**You've worked with tools like Unreal Insights and PIX for profiling. How do you translate data from those tools into actionable changes for artists and designers?**

Raw profiling data isn't very useful to most artists. It's too abstract. The key is translating that data into something visual and actionable. In the past, I've built automated performance telemetry systems that gather metrics on a cadence, then worked with teams to generate frame reports that turn that data into graphs, trends, and clear targets.

Instead of saying "this frame is expensive," it becomes:

- What specifically is causing the cost
- Where it exists in the content
- What can be done to fix it

That makes it easier for artists and designers to understand, and also makes it much easier to communicate status to directors and stakeholders.

**How important is automation in modern game development, and where do you see teams underutilizing it?**

Automation is critical, and still heavily underutilized. A lot of teams default to manual work simply because it's what they know. There's often an assumption that "a tool couldn't do this," when in reality, it usually can. I spend a lot of time talking directly with artists to understand what parts of their workflow are tedious or frustrating, then building tools to remove that pain.

That's where automation has the most impact:

- Repetitive setup tasks
- Validation and cleanup
- Performance checks during development

There's nothing better than solving a problem people didn't realize was solvable. You get a lot of "I didn't know you could do that" reactions, which is usually a good sign you're focusing on the right problems.

**As someone who bridges art and engineering, how do you ensure tools remain artist-friendly while still being technically robust and scalable?**

It comes down to separating interface from complexity. The underlying system can be as robust and scalable as it needs to be, but the user-facing side should be simple and intuitive. I try to build tools with inherent documentation (clear naming, tooltips, and predictable behavior). Good documentation still matters, but ideally, the tool shouldn't require much explanation to use.

I also iterate closely with artists. If something feels confusing or slows them down, it gets simplified. The more intuitive a tool is, the more likely it is to actually be used. Unused tools don't provide any value. I've also found that artists, designers, and engineers greatly enjoy tools being collated into places that make them easy to find/use. My go-to in this regard is custom menus built right into the editor.

**Looking ahead, how do you see the role of Technical Artists evolving, especially with increasing complexity in engines, pipelines, and real-time rendering?**

Technical Artists are becoming more central to production, especially at the pipeline level. There's still room for specialists (lighting, rendering, VFX, animation), but there's a growing need for people who think in terms of the bigger picture: pipeline structure, workflow efficiency, and scalability.

A lot of teams are still losing time to manual or overly complex processes that could be streamlined significantly. Having someone focused on that space becomes a force multiplier for the entire team. That's the area I enjoy most: helping teams operate more clearly, more efficiently, and with fewer bottlenecks.

**Finally, any behind-the-scenes, work-in-progress, or breakdown-style pieces and productions you could share would be awesome for our audience to take a look at.**

Most of my work happens behind the scenes in tools and pipeline development, so it doesn't always translate into traditional visual breakdowns. That said, one example I like to share is a Steam updater tool I built that automates deployment and validation workflows. More importantly, it effectively amortizes the cost of constant Steam branch switching, which ends up saving a significant amount of time when iterating fixes and pushing updates to live environments. It takes something that's usually disruptive and turns it into a predictable, low-friction part of the workflow.

More broadly, that kind of thinking is what led me to start Damascus Interactive. After years in production, I realized most teams don't struggle because of a lack of talent. They struggle because of friction. Poor pipeline structure, unclear workflows, missing tools, or systems that don't scale. Those problems compound over time and quietly drain productivity.

The idea behind the studio is to address that directly:

- Identify where teams are losing time or fighting their tools
- Build targeted solutions that remove that friction
- Leave behind systems that continue to provide value long after the work is done

A big part of the philosophy is that it's not just about helping teams ship faster. It's about helping them build stronger foundations. Tools, pipelines, and workflows should make development more predictable, not more chaotic. That's also why the approach is very production-focused and collaborative. It starts with understanding how a team actually works, then building solutions that fit into that reality rather than forcing something overly complex or theoretical.

I've started sharing some of that work publicly, including code examples and tooling approaches, to give people insight into how I think about solving these kinds of problems.

[Ryan Amos](https://www.linkedin.com/in/ryanmamos/), Senior/Lead Technical Artist

#### Interview conducted by [David Jagneaux](https://www.linkedin.com/in/davidjagneaux/)

[Partner with 80 Level](https://80level.typeform.com/to/B8udrWL5)
