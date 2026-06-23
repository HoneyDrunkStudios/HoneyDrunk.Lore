---
source: "https://architecturenotes.co/p/arc-notes-weekly-106-arrowhead"
title: "Arc Notes Weekly #106: Arrowhead"
author: "Architecture Notes"
date_published: "Sun, 15 Mar 2026 17:52:15 GMT"
date_clipped: "2026-06-23"
category: "Software Architecture"
source_type: "rss"
---

# Arc Notes Weekly #106: Arrowhead

Source: https://architecturenotes.co/p/arc-notes-weekly-106-arrowhead

Architecture Notes Weekly Arc Notes Weekly #106: Arrowhead This week, Amazon tightened review after a nearly six-hour retail outage and a 13-hour AWS incident tied to AI-written code, while Stripe's 11-task benchmark showed Claude Opus 4.5 hitting 92% on task Mahdi Yusuf Mar 15, 2026 7 Share This week, Amazon tightened review after a nearly six-hour retail outage and a 13-hour AWS incident tied to AI-written code, while Stripe’s 11-task benchmark showed Claude Opus 4.5 hitting 92% on full-stack integrations. Plus, Bassim Eledath mapped 8 levels of agentic engineering, Manuel Schipper ran 4-8 coding agents with tmux, and Agent Safehouse brought deny-first sandboxing to macOS.
Enjoy this week's round-up!
— Mahdi Yusuf ( @myusuf3 ) or LinkedIn 
👋🏾 You are reading Architecture Notes - Your Sunday newsletter, which curates best system design and architecture news from around the web. We would appreciate you sharing it with like-minded people. 
Articles 
Amazon Tightens Review of AI-Written Code After Retail and AWS Outages 
Amazon told engineers it has seen a recent trend of high-blast-radius incidents involving Gen-AI assisted changes, and junior and mid-level staff will now need senior sign-off on AI-assisted code changes. The move follows a nearly six-hour retail outage this month and earlier AWS incidents, including a 13-hour disruption tied to the Kiro coding tool, offering a revealing look at how one tech giant is trying to put guardrails around AI coding.
How The New York Times is Scaling Unit Test Coverage using AI tools 
The New York Times used AI tools, under strict human review, to generate unit tests across six web projects, raising average coverage from 28% to 83% and cutting work by an estimated 70%. It matters because stronger test coverage helps a fast-moving newsroom ship changes more safely, and the article offers concrete guardrails - like read-only coverage reports and a hard rule not to edit source code - that show where AI helps and where it still needs supervision. 
Why Good Communicators Start With the Point, Not the Backstory 
Steve Huynh argues that most people explain ideas bottom-up even though listeners process them top-down, and offers three fixes: BLUF, just-in-time context, and a top-down bridge. Using technical debt examples like an authentication module tied to six services and a proposed six-week cleanup, he shows how clearer structure helps people make decisions faster and reveals why saying less can make complex ideas land b
The 8 Levels Of Agentic Engineering, From Copilot To Autonomous Agent Teams 
Bassim Eledath maps AI-assisted software work across eight levels, from tab-complete and IDE chat to context engineering, MCP-powered skills, harnesses with automated feedback loops, and background agents that can raise PRs while you sleep. The framework explains why strong model benchmarks often fail to translate into team productivity, and why the real leverage may come from better tooling, review flows, and coordination before fully autonomous agent teams arrive. 
Why Organizations Get the Results They Are Designed For 
Mike Fisher argues that recurring outcomes are usually products of system design, not individual failure, drawing on Deming and Conway’s Law to show how structure shapes behavior. Using Amazon’s two-pizza teams and API-driven services alongside Boeing’s 737 MAX, MCAS, and the 346 deaths in the 2018 and 2019 crashes, he shows why leaders must redesign incentives, communication, and authority if they want different results - and why surface fixes rarely hold. 
Why “Managing Up” Fails and What Effective Communication Looks Like 
Rands argues that “managing up” is often a euphemism for selectively shaping a boss’s perception, and says the real job is bi-directional communication plus strong lateral relationships across people, projects, and politics. He offers a practical rule set - report unexpected developments immediately, from missed milestones to any mention of HR or Legal - because managers operate with a wider context, and the overlooked half of your information often sits with peers, not just your boss.
Architecture Notes — System Design & Software Development is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
Subscribe How To Design And Sustain Sub-100 ms APIs At Scale 
This InfoQ article argues that sub-100 ms APIs come from explicit latency budgets across the request path - for example, 10 ms at the edge, 5 ms at the gateway, 30 ms for service logic, and 40 ms for data access - plus patterns like async fan-out, multi-level caching, and circuit breakers. It matters because latency compounds across services and quietly erodes user experience and revenue, and the piece usefully shows how architecture and team practices work together to keep speed from regressing over time.
16 Principles For Working With AI Coding Agents Without Losing Control 
Yoav Aviram distills a year of daily work with coding agents into 16 principles, arguing that code is becoming cheap while the real constraints shift to feedback loops, supervision, security, and shipping. With examples like rebuilding a CMS four times in three months and migrating four WordPress blogs to Hetzner in 15 minutes, he sketches how software work changes when agents can build fast but still fail in subtle ways.
Projects cmux 
Cmux is an open source macOS terminal built on Ghostty that adds vertical tabs and notifications aimed at AI coding agents, with 6.6k GitHub stars, 1,491 commits, and recent work on Claude Code status hooks and duplicate-notification suppression. That makes it more than a terminal skin: it is trying to solve the messy workflow around long-running agent sessions, and the recent implementation details hint at how serious the integration is.
tui-studio 
TUI Studio is an open source GitHub project with 657 stars and 132 commits that lets developers visually build terminal user interfaces, including per-screen theming, Bubble Tea-style tabs, and an enhanced color picker. It matters because it could speed up TUI prototyping without hand-coding every layout detail, and the recent additions hint at how far visual tooling for terminal apps can go. 
agent safehouse 
Agent Safehouse is an open source macOS tool that uses sandbox-exec, composable policy profiles, and a deny-first model to limit what coding agents like Claude, Codex, and Amp can read or write. It matters because it adds practical least-privilege controls without breaking normal developer workflows, and the project already shows traction with 1.3k GitHub stars and a latest release of v0.3.1. 
Why Looking Stupid Can Be a Real Advantage in Creative Work 
Sharif Shameem argues that creative progress often depends on being willing to publish bad ideas first, drawing on examples from Nobel winners who stop taking small swings, a Whole Foods cake brainstorm with his friend Aadil, and even evolution’s many failed mutations before jellyfish. It matters because fear of embarrassment can turn better, more experienced people into cautious non-creators, and his simple reframing - share something at all, not something perfect - is a useful test for anyone stuck hesitating.
7 Share Previous
