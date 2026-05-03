# Lore — Sourcing Playbook

This document defines what content belongs in Lore, where to find it, and how to decide what gets clipped. It governs the sourcing stage of the Lore pipeline. It is read primarily by OpenClaw, which performs scheduled automated sourcing, and occasionally by humans for serendipitous capture.

---

## How to use this playbook

**OpenClaw — automated sourcing (every 1–2 days):** OpenClaw runs a scheduled job that walks every source listed below. For RSS-friendly sources it fetches feeds directly; for login-walled sources (X, Discord) it uses its managed Chromium browser tool with persistent cookies. Items matching the relevance criteria below land in `HoneyDrunk.Lore/raw/` as markdown.

**Web Clipper — serendipitous human capture (anytime):** When you find an article worth keeping during normal reading, hit Quick Clip (Alt+Shift+O). Output lands in `raw/` same as OpenClaw output. The downstream ingestion skill doesn't care which path produced a file.

**Your own explorations are sources too.** When a query session, debug investigation, or research thread yields something worth keeping, crystallize it — write it to `output/` and let the next compile pass pull it into `wiki/`. Treat it exactly like an external article: same relevance criteria, same compile path. This is how the wiki compounds from your own work, not just from the outside world.

> **Out of scope for this playbook:** the weekly Claude Code ingestion skill that reads `raw/` and compiles into `wiki/` is governed separately. This document only defines what gets *into* `raw/`.

---

## Categories

### 1. AI / LLM Research & Tooling
*Core to everything HoneyDrunk builds — models, agents, evals, prompting, MCP, tooling. Multi-provider by design: HoneyDrunk uses Claude, GPT, Gemini, and open models, so signal from all major labs matters.*

**What to clip:**
- Model capability announcements and benchmark results from any major lab
- Agent architecture patterns (planning, memory, tool use, multi-agent)
- Prompt engineering techniques and evals methodology
- MCP (Model Context Protocol) updates and new servers
- New AI development tools and frameworks
- LLM infrastructure and cost optimization
- Cross-provider comparisons and migration patterns

**What to skip:**
- General AI hype with no technical substance
- Product announcements with no architecture or engineering detail

**Sources — frontier labs:**
- Anthropic Research (anthropic.com/research)
- Anthropic Engineering (anthropic.com/engineering)
- OpenAI Research (openai.com/research)
- OpenAI Blog (openai.com/blog)
- Google DeepMind (deepmind.google/discover/blog)
- Google Research (research.google/blog)
- Meta AI (ai.meta.com/blog)
- Mistral AI (mistral.ai/news)

**Sources — applied + tooling:**
- Hugging Face blog (huggingface.co/blog)
- LangChain blog (blog.langchain.dev)
- Simon Willison (simonwillison.net)
- Andrej Karpathy (karpathy.ai, github.com/karpathy)
- The Batch — DeepLearning.AI (deeplearning.ai/the-batch)

**Sources — research firehose:**
- ArXiv cs.AI (arxiv.org/list/cs.AI/recent) — applied agent work only
- ArXiv cs.LG (arxiv.org/list/cs.LG/recent) — applied agent work only
- Hacker News (news.ycombinator.com) — AI/LLM posts with substantial discussion

---

### 2. Software Architecture
*Patterns that influence Grid design — distributed systems, event-driven, CQRS, domain modeling.*

**What to clip:**
- Event-driven and message-based architecture patterns
- CQRS, event sourcing, outbox patterns
- Domain-driven design and bounded contexts
- Distributed systems fundamentals (CAP, eventual consistency, sagas)
- API design and contract-first development

**What to skip:**
- Language-specific tutorials not applicable to .NET
- Opinion pieces without concrete trade-off analysis

**Sources:**
- Martin Fowler (martinfowler.com)
- ByteByteGo (bytebytego.com)
- High Scalability (highscalability.com)
- InfoQ Architecture (infoq.com/architecture-design)
- The Architecture Notes (architecturenotes.co)

---

### 3. Azure & Cloud
*Platform HoneyDrunk builds on — new services, best practices, pricing, identity.*

**What to clip:**
- Azure service announcements relevant to the Grid (Functions, Container Apps, App Config, Key Vault, Event Grid, AI services)
- Azure identity and RBAC changes
- Cost optimization strategies for Azure
- GitHub Actions + Azure integration patterns
- Cloud-native patterns (KEDA, Dapr)

**What to skip:**
- AWS/GCP content unless directly comparative to Azure
- Azure services outside the Grid current or planned scope

**Sources:**
- Azure Updates (azure.microsoft.com/updates)
- Azure DevBlogs (devblogs.microsoft.com/azure)
- Azure Architecture Center (learn.microsoft.com/azure/architecture)
- John Savill Technical Training (youtube.com/@NTFAQGuy)
- Azure Friday (learn.microsoft.com/shows/azure-friday)

---

### 4. .NET Ecosystem
*Runtime — framework updates, libraries, patterns, performance.*

**What to clip:**
- .NET release notes and preview features
- ASP.NET Core and C# language updates
- NuGet ecosystem: new libraries worth evaluating
- Performance and benchmarking
- Minimal API and middleware patterns

**What to skip:**
- Framework comparisons aimed at beginners
- Content covering stable, well-understood .NET APIs already in use

**Sources:**
- .NET Blog (devblogs.microsoft.com/dotnet)
- Andrew Lock (andrewlock.net)
- Nick Chapsas (youtube.com/@nickchapsas)
- Scott Hanselman (hanselman.com)
- .NET Weekly newsletter (dotnetweekly.com)

---

### 5. Solo Dev / Indie SaaS
*How HoneyDrunk operates as a studio — product strategy, pricing, go-to-market, sustainability.*

**What to clip:**
- Build-in-public case studies and revenue milestones
- Pricing strategy and packaging for developer tools
- Distribution and discoverability for niche SaaS
- Solo founder operating patterns
- Open source + paid tier models

**What to skip:**
- VC-funded startup content focused on growth-at-all-costs
- General entrepreneurship advice not grounded in product or technical work

**Sources:**
- Indie Hackers (indiehackers.com) — filter for SaaS and dev tools
- The Bootstrapped Founder — Arvid Kahl (thebootstrappedfounder.com)
- Pieter Levels (levels.io, twitter.com/levelsio)
- Hacker News Show HN (news.ycombinator.com/show)
- Tiny Seed blog (tinyseed.com/blog)

---

### 6. Developer Tooling & AI Coding
*Tools that improve the development workflow — Claude Code, MCP servers, IDEs, productivity.*

**What to clip:**
- Claude Code updates and new features
- MCP server releases relevant to development workflows
- IDE and editor updates (VS Code, JetBrains)
- AI-assisted coding patterns and prompting strategies
- Comparable tooling from other providers (Cursor, Aider, Codex, Gemini Code Assist) when patterns are portable

**What to skip:**
- Tool comparisons without depth
- Anything that does not directly improve the solo dev + AI agent workflow

**Sources:**
- Claude Code documentation and changelog (docs.claude.com/en/docs/claude-code)
- VS Code updates (code.visualstudio.com/updates)
- GitHub Blog (github.blog)
- Changelog podcast (changelog.com)
- The Pragmatic Engineer — Gergely Orosz (pragmaticengineer.com)

---

### 7. Game Development / Unity
*HoneyPlay sector — narrative, simulation, games powered by the Grid.*

**What to clip:**
- Unity engine updates (LTS releases, new features)
- Unity + AI integration patterns
- Procedural generation and simulation techniques
- Narrative design and interactive storytelling
- Game architecture patterns applicable to the Grid
- Indie game development workflow and tooling

**What to skip:**
- Beginner Unity tutorials
- AAA studio news with no applicable patterns

**Sources:**
- Unity Blog (unity.com/blog)
- Game Developer (gamedeveloper.com)
- r/gamedev (reddit.com/r/gamedev) — architecture and systems posts only
- Game Programming Patterns (gameprogrammingpatterns.com)
- GDC Vault (gdcvault.com) — free talks

---

### 8. DevOps & CI/CD
*Ops sector — shipping reliably, observability, deployment patterns.*

**What to clip:**
- GitHub Actions updates and new features
- Container and Docker best practices
- Observability patterns (OpenTelemetry, distributed tracing)
- DORA metrics and delivery performance
- Deployment strategies (blue/green, canary, feature flags)

**What to skip:**
- DevOps culture pieces without technical substance
- Jenkins and legacy CI content

**Sources:**
- GitHub Actions changelog (github.blog/changelog/label/actions)
- Docker blog (docker.com/blog)
- OpenTelemetry blog (opentelemetry.io/blog)
- DevOps.com (devops.com) — CI/CD and observability only
- Charity Majors (charity.wtf)

---

### 9. Workflow Automation
*Automating the solo dev operating rhythm — agents, triggers, integrations.*

**What to clip:**
- No-code and low-code automation patterns (n8n, Make, Zapier)
- Webhook-driven automation patterns
- AI agent automation case studies
- Scheduled and event-driven workflow patterns

**What to skip:**
- Enterprise RPA content
- Automation platforms with no integration path to the Grid

**Sources:**
- n8n blog (blog.n8n.io)
- Zapier blog (zapier.com/blog) — developer automation only
- Make (make.com) updates
- Hacker News (news.ycombinator.com) — automation and workflow posts

---

### 10. Emerging Technology
*Signals from adjacent fields that may influence the Grid long-term direction.*

**What to clip:**
- Robotics and embodied AI (Cyberware sector relevance)
- WebAssembly and edge computing advances
- New programming paradigms with architectural implications
- Brain-computer interfaces and HCI research

**What to skip:**
- Speculative futures without engineering substance
- Consumer technology reviews

**Sources:**
- MIT Technology Review (technologyreview.com)
- IEEE Spectrum (spectrum.ieee.org)
- Ars Technica (arstechnica.com) — deep technical dives only
- The New Stack (thenewstack.io)
- Hacker News (news.ycombinator.com) — emerging tech high-signal posts

---

### 11. Security & Ethical Hacking
*HoneyNet sector — resilience testing, digital hygiene, threat modeling.*

**What to clip:**
- Application security patterns for .NET and Azure
- OAuth2 / OIDC security considerations
- API security and secrets management best practices
- CTF write-ups with applicable defensive techniques
- Threat modeling frameworks and OWASP updates

**What to skip:**
- Malicious tooling without defensive application
- CVE announcements for technologies outside the Grid stack

**Sources:**
- OWASP (owasp.org)
- Troy Hunt (troyhunt.com)
- Scott Brady (scottbrady91.com) — .NET identity and security
- HackerOne Hacktivity (hackerone.com/hacktivity) — public disclosures
- Security Weekly (securityweekly.com)

---

### 12. Creator Economy & Marketplace
*Market sector — XP systems, gigs, payouts, marketplace dynamics.*

**What to clip:**
- Creator monetization models and platform economics
- XP and gamification system design
- Marketplace dynamics and pricing models
- Digital goods and licensing patterns

**What to skip:**
- Influencer content without product or system depth
- Speculative digital asset content

**Sources:**
- Lenny's Newsletter (lennysnewsletter.com) — product and marketplace patterns
- Hacker News (news.ycombinator.com) — marketplace and economy posts
- Stratechery (stratechery.com) — platform and marketplace analysis

---

## Sources requiring browser or audio tooling

These sources can't be fetched as simple RSS, but OpenClaw still automates them — the mechanisms differ from cats 1–12.

- **Login-walled** (X, Discord) → OpenClaw managed Chromium profile (`browser.defaultProfile = "openclaw"`). One-time login per source persists in the cookie jar; the daily job then scrapes without further auth.
- **Audio** (podcasts) → OpenClaw fetches the RSS feed, downloads new episodes, transcribes via Whisper (or equivalent), drops the transcript in `raw/` with `source: podcast` and the original audio URL in frontmatter.

Implementation specifics for both mechanisms (browser profile setup, login flows, transcription worker) live in the OpenClaw bringup packet, not here. This playbook only defines *what* gets sourced; the mechanism is OpenClaw's concern.

### X / Twitter

OpenClaw scrapes `x.com/i/lists/2050930841488904671` daily — a private list curated in the X UI. Add or remove sources directly in the list; OpenClaw picks up the change on the next run. List membership is the source of truth; this playbook does not enumerate handles.

### Discord communities

OpenClaw navigates Discord web with the managed profile and snapshots the **announcement channels only** in each server below. Help/chat noise is excluded.

- Anthropic Discord (joinable from anthropic.com) — Claude, MCP, Claude Code announcements
- OpenAI Developer Discord — API changes, model releases
- Hugging Face Discord — OSS model ecosystem
- LangChain Discord — agent framework patterns
- .NET / C# Discord (discord.gg/csharp) — language and runtime announcements

### Podcasts

OpenClaw polls the RSS feed, downloads new episodes, transcribes, and drops the transcript in `raw/` tagged `source: podcast`. The ingestion skill treats transcripts the same as articles.

- Latent Space (latent.space) — AI engineering deep dives, swyx + alessio
- Practical AI (changelog.com/practicalai) — applied AI cases
- The Pragmatic Engineer podcast (pragmaticengineer.com/podcast) — engineering leadership, dev productivity
- Acquired (acquired.fm) — strategy and business of tech, occasional infra deep dives

### What to skip

- LinkedIn — most signal here gets reposted to X or blogs; not worth automating
- TikTok / Instagram — no relevant signal for HoneyDrunk
- Real-time event streams (live conferences) — wait for the recording

---

## Relevance criteria (for agents)

When deciding whether to clip something, apply these in order:

1. **Actionable or instructive?** Can this be applied to HoneyDrunk design, architecture, or operation? If yes, clip.
2. **Durable?** Will this still matter in 6 months? Patterns and trade-off analyses usually do. Current-events opinion pieces usually do not.
3. **In scope?** Matches one of the 12 categories above? If not, skip.
4. **Deep enough?** Has technical substance, concrete examples, or case study data? Surface-level overviews are not worth compiling.

When in doubt: clip it. It is easier to lint duplicates out than to recover from missing content.

---

## Session rhythm

| Frequency | Actor | Activity |
|-----------|-------|----------|
| Every 1–2 days | OpenClaw (automated) | Walk every source in this playbook; drop qualifying items in `raw/` |
| Weekly | Claude Code ingestion skill (automated) | Compile `raw/` into `wiki/` — out of scope here, governed separately |
| Monthly, ~10 min | You | Review this playbook — add new sources, remove dead ones, refine relevance criteria |
