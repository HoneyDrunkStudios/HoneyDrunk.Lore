---
source: "https://www.thoughtworks.com/insights/blog/generative-ai/how-to-implement-effective-review-gates-for-ai-assisted-development"
title: "How to implement effective review gates for AI-assisted development | Thoughtworks"
author: "Vineet Desai"
date_published: "2026-04-21"
date_clipped: "2026-06-04"
category: "Software Architecture"
source_type: "web"
---

# How to implement effective review gates for AI-assisted development | Thoughtworks

Source: https://www.thoughtworks.com/insights/blog/generative-ai/how-to-implement-effective-review-gates-for-ai-assisted-development

How to implement effective review gates for AI-assisted development
Engineering Stack 
Back 
Engineering Stack 
Back 
Close 
Generative AI
Blog
Summarize with AI
Woops! Something went wrong and we're unable to generate a response at the moment. Please try again later.
Disclaimer: AI-generated summaries may contain errors, omissions, or misinterpretations. For the full context please read the content below. 
By 
Vineet Desai 
Published: April 21, 2026 
AI coding assistants can significantly increase development speed . However, ensuring we can trust their outputs is a key challenge. Common difficulties include reviewing large, unmanageable diffs, losing context across coding sessions and dealing with partially functional code resulting from the AI changing focus mid-task.
So, I wanted to find a workflow that would tackle some of those risks and will:
Reduce the cognitive load of reviewing AI generated code.
Allow me to walk away from a session and pick up later without re-explaining context to AI assistant
Keep the codebase stable so the AI can't silently drift.
I tested this by building tiny-event-bus — a type-safe, zero dependency event bus built using GitHub Copilot with Claude Opus 4.6. The workflow has three parts: milestones that break work into small reviewable chunks, review gates at two frequencies and a living context file for AI project memory across sessions. In this blog post I’ll explain more about those milestones and why I think they’re important in AI-assisted software development. 
Development planning with AI assistance 
I spent the first session not writing code but just describing what I wanted and the AI proposed a plan: tech stack, package structure, milestone breakdown. Once agreed, the AI drafted AGENTS.md and MILESTONES.md in plan mode, reviewed and iterated by me before any code was written. AGENTS.md is a compact context file under 200 lines, updated after every milestone so fresh sessions start with current context.
Milestones keep code reviews small 
The AI can produce a 40-file diff in minutes. Milestones fix this by breaking every feature into chunks small enough to review in one sitting. Each milestone leaves the codebase compilable, tested and documented.
Every feature starts in plan mode and the AI proposes a breakdown. Specifically, it looks at which layers it touches, how many milestones and in what order. Ordering comes from dependency analysis, not rigid sequencing and we iterate until it makes sense. The AI then updates MILESTONES.md with the agreed milestones, each one marked "not started". Finally, I review the plan before implementation begins.
"A feature is never one milestone."  
Take the ability to subscribe to all events on the bus — the onAny event listener. Its implementation became four milestones:
Core implementation — add the onAny feature to the event bus.
A React hook — a wrapper that ties the listener to the react component lifecycle.
Demo update — wire it into the example app.
End-to-end verification and docs update — this will prove the API works end to end and make it discoverable.
After the first milestone, the core works and all tests pass. The React hook doesn't exist yet, but nothing is broken. You could push and come back later.
Take another example of the monorepo migration to support feature extensions to the event bus via a plugin architecture. It became five milestones:
Scaffold the workspace structure.
Extract the core package.
Extract the React plugin.
Full workspace verification.
Migrate the example app to workspace dependencies.
Contrast this with the AI doing the entire migration in one shot: a 40-file diff where you're checking peer dependency declarations while also verifying import paths. That review will be miserable! Reviewing in small chunks, though, is easy because you actually read and think about it. Milestones turn code review from an audit into a conversation.
Review gates catch drift early 
Review gates keep each milestone honest. I frame these as gates rather than loops because the defining characteristic isn't the repetition, but the fact that the AI must stop and await explicit permission to proceed. This ensures that nothing is integrated into the codebase without passing through human review.
This is a deliberate contrast with fully autonomous approaches like the Ralph Loop, where the AI runs in a continuous cycle - code, test, fix, repeat - with minimal human intervention. While the Ralph Loop prioritizes velocity, it creates obstacles for human oversight due to the rapid generation of massive code volumes. This speed can lead to the compounding of incorrect assumptions. Gates trade speed for control, and is still dramatically faster than writing everything yourself.
There are two review gates, operating at different frequencies. The inner gate fires after every individual test which is also the smallest reviewable unit and catches a wrong assumption before it propagates. The outer gate fires at milestone boundaries and checks whether the completed feature fits the bigger picture and whether the codebase is in a stable state to hand off or continue later.
The inner gate 
The project follows test-driven development (TDD). The inner gate fires after every red-green-refactor cycle. The AI writes one failing test, implements just enough to pass, then stops for review. This prevents AI from front-loading assumptions.
Without the inner gate, the AI writes tests based on a misunderstanding and implements against them, resulting in a coherent but wrong feature. The inner gate catches this drift early and also builds human confidence in the code.
The outer gate 
The outer gate fires at milestone boundaries. The AI runs mechanical checks like the test suite, linting, build, doc updates. My review is the human layer wherein I verify the design, review updates to config files, review project structure, catch what automation misses. After any milestone, AGENTS.md and MILESTONES.md are updated and they tell the AI where you left off. This is what makes “pause and resume” work.
This helps in breaking down the reviews in small chunks, rollback to any previous checkpoint safely and keep documents up to date so that a new session can start after logical completion.
The entire workflow for a feature development looks something like this
Do you need both ? 
The inner gate is a review point within a milestone. The outer gate is a milestone boundary that is stable enough to push. 
Could you skip inner gates? It depends. Outer gates alone keep reviews small and give stable pause points. But you catch wrong assumptions at the milestone end instead of after one test. Inner gates also make outer gate reviews faster because you've already reviewed each test, so the outer gate becomes mostly a design check. 
For mature codebases, skipping inner gates is reasonable. For greenfield work, they earned their keep.
Friction 
The AI writes correct implementations immediately instead of minimal code, weakening TDD. The refactor step is even weaker. After turning a test green, the AI almost never spontaneously opts to review if a refactor is required. Either the code is already clean enough, or there's a real refactoring opportunity that the AI doesn't notice. You have to often spot those yourself and nudge it.
It doesn't reliably follow rules in the context file. AI models follow instructions probabilistically, not deterministically.
Updating docs with AI is a recurring fight. Sometimes the AI will mark a milestone done and move on without touching the other docs unless you explicitly ask. Even when it does, it'll update some docs but forget to update others.
AGENTS.md rules are conventions with no automated enforcement.
Caution — it’s addictive! 
The loop is very satisfying. When implementation friction drops so low, the bottleneck shifts to your energy and judgment and both degrade with fatigue. Gates work less well when you're tired and just want to check the box and see the next feature come alive.
Takeaway 
AI can write code faster than you can review it. This workflow solves it with constraints:
Milestones that keep reviews small.
Inner gates that catch drift one test at a time.
Outer gates that leave the codebase stable at every checkpoint.
Living context file for project memory across sessions.
The AI is fast and tireless but has no taste and judgment. Your job shifts from writing code to designing constraints and reviewing output. You become the architect, senior dev and the QA simultaneously.
Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.
Related content 
Technology Radar | Guide to technology landscape
Learn more 
Engineering effectiveness 
Unleashing potential: The business benefits of AI-first software engineering
Learn more 
Generative AI 
AI isn't just a coding partner — it can be a deployment partner, too
Learn more 
View more 
View less 
Engineering excellence. Unlocked. 
Explore now
