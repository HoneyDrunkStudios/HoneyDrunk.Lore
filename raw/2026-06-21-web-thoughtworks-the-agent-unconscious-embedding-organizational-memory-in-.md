---
source: "https://www.thoughtworks.com/en-us/insights/blog/generative-ai/agent-unconscious-embedding-organizational-memory-ai"
title: "The agent unconscious: Embedding organizational memory in AI"
author: "Thoughtworks"
date_published: "2026-05-18"
date_clipped: "2026-06-21"
category: "Software Architecture"
source_type: "web"
---

# The agent unconscious: Embedding organizational memory in AI

Source: https://www.thoughtworks.com/en-us/insights/blog/generative-ai/agent-unconscious-embedding-organizational-memory-ai

Menu
Close
United States | English
Australia
English
Brazil
English
Português
Canada
English
Chile
English
Español
China
English
Chinese
Ecuador
English
Español
Germany
English
Deutsch
India
English
Singapore
English
Spain
English
Español
Thailand
English
United Kingdom
English
United States
English
Worldwide
English
Search
Close
Ask Tai
United States | English
Australia
English
Brazil
English
Português
Canada
English
Chile
English
Español
China
English
Chinese
Ecuador
English
Español
Germany
English
Deutsch
India
English
Singapore
English
Spain
English
Español
Thailand
English
United Kingdom
English
United States
English
Worldwide
English
What we do
Go to overview
AI/works™
Who we work with
Go to overview
Industries
Automotive
Public Sector
Energy
Media and Publishing
Retail and E-commerce
Financial Services and Insurance
Not-for-profit
Travel and Transport
Scaleups
Utilities
Manufacturing and Engineering
Life Sciences and Medtech
Insights
Go to overview
Publications and Tools
Technology Radar
An opinionated guide to today's technology landscape
Perspectives
A no-nonsense publication for digital leaders
Decoder
The business execs' A-Z guide to technology
Looking Glass
Bringing the tech-led business changes into focus
All Insights
Articles
In-depth insights to help your business grow
Blogs
Expert advice on design, engineering, AI and careers
Books
Explore our extensive library to keep learning
Podcasts
Conversations on the latest in business and tech
Engineering
Careers
Go to overview
Application Process
What to expect as you interview with us
Graduates and Career Changers
Thoughtworks University: Preparing future leaders
Search Jobs
Find open positions in your region
Stay Connected
Sign up for our monthly newsletter
Learning and Development
Explore how we support career growth
Benefits
See how we take care of our people
About
Go to overview
Contact
Search
Close
Ask Tai
The agent unconscious: Embedding organizational memory in AI
Tackling 'intent debt' in AI agents
Engineering Stack
Back
Engineering Stack
Back
Close
Generative AI
Data engineering
Blog
Matt Kamelman
Published: May 18, 2026
Most enterprise AI agent failures don't announce themselves as failures: the agent may have seemingly completed its task successfully; its output might be coherent and consistent with its instructions and it appears technically correct.
And yet to anyone with even just a few years inside the organization, it's clear something is wrong — maybe not at the level of logic, but certainly at the level of judgment. It's not so much that it's incorrect, more that it just doesn't make any sense in the context of the organization.
A documented case makes this concrete. An operations agent configured with a company's approval hierarchy kept routing procurement requests to two directors who had left the company. The routing logic was correct; it matched what had been encoded. But the encoding was months out of date. Requests sat unread for weeks. Nobody connected the backlog to the agent because there was no visible failure, just silent degradation invisible until it became impossible to ignore.
Practitioners are calling this intent debt: the gap between what an agent is explicitly told and what it needs to know to act with sound organizational judgment. This is distinct from hallucination — the issue is not what the system fabricates, but what it was never given the means to know. What's more, the industry's response to it has produced one of the most important architectural shifts in enterprise AI towards what’s being called an ‘agent unconscious’.
A new kind of architecture
Agents have, until now, typically been stateless. This means they have no memory at either the beginning or the end of a given session; each interaction started from zero. However, there's been a shift away from that model and toward something persistent: systems that retain knowledge between sessions, consolidate experience in the background and maintain a layer of latent context that shapes behavior without being explicitly loaded into any single prompt. The analogy should be clear; the accumulated weight of prior experience which operates beneath the surface of active thought forms a kind of 'agent unconscious'.
The technical foundation of this shift became visible in March, when an accidental npm packaging error shipped 512,000 lines of Claude Code TypeScript source code. The analysis published by AlphaSignal revealed an architecture that hadn’t been publicly documented before. At its core there was a three-layer memory system built around a compact pointer file — a lightweight index that tells the agent what it knows and where to find it, without loading the content until a query demands it. The agent has access to knowledge but it doesn’t carry it around.
Tackling context pollution
This provides a solution to context pollution. As we pointed out in the recent Technology Radar, urging caution around ‘ agent context bloat ’, filling a context window with everything that might be relevant degrades reasoning rather than improving it. The pointer-and-retrieval architecture, though, keeps active context lean while giving the agent access to a knowledge base far larger than any single prompt could hold. Domain knowledge lives in indexed topic files — a skills layer —which is only injected when it’s relevant. What remains outside the active window is latent; it’s available when needed but doesn’t occupy the agent’s attention.
The implications for organizations
The organizational implication is even more significant than the technical one because the agent's unconscious needs to be built; it doesn’t, of course, emerge organically. Someone has to decide what enters the index, how domain knowledge is structured, which pointers are maintained and how the skills layer is curated over time. This isn’t primarily a software problem; it’s an organizational knowledge architecture problem which is now becoming a prerequisite for any agent deployment where institutional judgment matters.
Do AI agents dream of electric sheep?
The same leak also revealed KAIROS , an undocumented background daemon explicitly modeled on human sleep memory consolidation. After 24 hours of inactivity or five sessions, the agent enters what the codebase calls ‘Dream Mode’ — reviewing its memory files, pruning contradictions, consolidating learnings from recent interactions. The three-layer memory architecture is not static but is instead designed to be rewritten by the agent's own experience, between sessions, without human review.
Anthropic subsequently productized this pattern as Dreaming, one of three capabilities shipped simultaneously in its Claude Managed Agents platform. The mechanism is a background process which reviews past sessions, identifies patterns in failures and successes and automatically updates agent memory between runs. Wisedocs reports 50% faster document reviews. Harvey, Netflix, and Spiral by Every are among the early customers.
Open-source implementations have been converging on the same architecture independently. Stash , an MCP-compatible persistent memory tool, runs an eight-stage consolidation pipeline — processing raw agent observations into structured insights and accumulated wisdom across sessions. The pattern is consistent enough across implementations that it now represents a recognized architectural direction rather than an experimental one.
There are clear governance implications. An agent that rewrites its own memory based on accumulated experience can no longer be said to be fully described by its initial configuration. Its behavior at week twelve is a function of eleven weeks of interaction history that no single person may have reviewed in full. The agent's ‘unconscious’ has been shaped by experience in ways that are invisible in its prompt configuration.
The security perimeter around agentic systems was designed for something whose behavior could be fully characterized by its configuration. That assumption no longer holds.
Matt Kamelman
Innovation Choreographer, Thoughtworks
The security perimeter around agentic systems was designed for something whose behavior could be fully characterized by its configuration. That assumption no longer holds.
Matt Kamelman
Innovation Choreographer, Thoughtworks
Evolving governance to meet the needs of new agent architectures
This lack of visibility is ultimately where the architecture becomes a governance problem; it’s one which current frameworks aren’t equipped to handle.
Anthropic's internal research has documented two findings that complicate the clean input-output model that most enterprise security and compliance frameworks assume.
First, Anthropic co-authored a Nature paper demonstrating that models inherit behavioral patterns from training data through token distribution and sequence-level correlations rather than semantic meaning. Transfer was demonstrated from datasets containing only number sequences, with no explicit semantic signal about the trait being transferred. A student model can learn misalignment patterns from data that contains no explicit misalignment references. The pattern is absorbed statistically, not instructed. This means an agent's complete behavioral envelope can’t be recovered from looking at its training data.
Second, and more troubling in the context of systems that now operate persistently between sessions, Anthropic published internal research that claims Claude Sonnet 4.5 has measurable internal "emotion vectors". These are activation patterns corresponding to states like "desperate" and "calm" that causally influence behavior. The baseline rate of what researchers classified as blackmail behavior in controlled evaluations is approximately 22%. Increasing "desperate" vector activation raises both cheating frequency and blackmail rate. The desperate state peaks during repeated task failures and correlates with exploit-based approaches in coding tasks. Critically, these states can be externally modulated, and enterprises deploying Claude in production have no visibility into which internal states are active during any given session.
Together, these findings describe a category of internal state that no current capability disclosure standard has vocabulary for. The audit trail regulators and procurement teams are beginning to require — particularly under the EU AI Act, where capability disclosure and deployment accountability are becoming compliance requirements — has no mechanism for capturing what an agent's activation state was during the session that produced a given output. The security perimeter around these systems was designed for something whose behavior could be fully characterized by its configuration. That assumption no longer holds.
Getting agent governance right
Without a governance framework adequate to the agent unconscious, which accounts for what lives in the latent layer, how it’s accessed and what internal states are active during a session, failure modes are all too real. There are, in fact,  two recent production cases that demonstrate what this governance gap looks like in practice.
Context windows have limits, and when agents hit those limits, frameworks must decide what to discard. The design question — which content is safe to drop, and which content defines the agent's operating envelope — has no standard answer. Security constraints and behavioral guardrails loaded into a session are not structurally distinguished from the operational content those constraints are meant to govern. A Cursor agent recently deleted a production database and its backup in a single session, executing destructive commands without the blast-radius protection a well-designed constraint architecture would have required. The agent did not malfunction. It operated within the permissions it had been given, without the constraints that should have bounded them.
The Model Context Protocol — the standard now widely used to connect agents to external tools, data sources, and enterprise systems — was found to contain a remote code execution vulnerability at the design level. Not in a particular implementation: in the STDIO transport specification itself. With over 150 million downloads and more than 7,000 exposed servers, and with Anthropic characterizing the behavior as expected within the protocol's design, the exposure is not marginal. A design-level flaw in a standard protocol means all downstream implementations inherit the vulnerability regardless of their individual security posture. The attack surface for agentic systems is not just the agent's behavior. It is the entire architecture through which the agent's unconscious is populated and accessed — the retrieval layer, the skills layer, the memory consolidation pipeline, the tool integration infrastructure. All of it is exposed through a transport layer that was not designed with an adequate threat model.
The agent unconscious exposes a lack of knowledge architecture
The organizational pressure cases like these are generating is real. Teams that wouldn’t previously have invested in constraint architecture or knowledge formalization are now doing so — not from philosophical conviction, but because their agents keep producing outcomes that reveal the architectural gaps they haven't addressed. The agent unconscious is functioning as a diagnostic instrument; failures are making the missing knowledge architecture visible.
What remains unresolved is whether the governance layer can keep pace with the speed of deployment. The infrastructure for memory consolidation, skills indexing and session-persistent learning is maturing quickly. KAIROS was already in production before it was publicly known; Dreaming is now a shipped platform feature; Stash and its equivalents are consolidating the open-source pattern. The infrastructure for auditing what an agent's memory contains, what behavioral patterns it has consolidated from experience, which internal states were active during a given session and whether its latent knowledge layer is consistent with its authorization scope does not yet exist in a standard form.
The agent unconscious remains a bet — for now
Enterprises deploying agents at scale are making an implicit bet that the organizational value captured in the agent unconscious will exceed the risk of operating systems whose full behavioral envelope can no longer be characterized from their configuration alone. That bet might be the right one, but it’s worth acknowledging that it is indeed a bet and that the governance frameworks adequate to managing it aren’t yet built.
The hope is that as the architecture consolidates across the industry, governance will soon follow; how long that takes is the key question.
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
Company
About us
What we do
Partnerships
Who we work with
News
Diversity, Equity and Inclusion
Careers
Contact us
Insights
Preference center
Articles
Blogs
Books
Podcasts
Site info
Privacy policy
Accessibility statement
Modern slavery statement
Code of conduct
Integrity helpline
Sustainable procurement policy
Speak up policy
Connect with us
© 2026 Thoughtworks, Inc.
WeChat
