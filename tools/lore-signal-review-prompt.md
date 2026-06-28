# Lore Daily News Blast Prompt

Use this prompt for the scheduled ADR-0086 runner Lore signal review job.

Working repo: `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Lore`
Architecture repo: `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Architecture`

## Purpose

Lore sourcing and ingest answer: "what should we preserve?" and "how do we structure it?"

This job answers: **"what are the biggest useful things Oleg should know today?"**

It is a daily news blast, not a ticket generator. It should surface ten useful source-backed stories, ten relevant X posts gaining traction, short main-point summaries, and any HoneyDrunk-specific implications. Do not turn trends into work automatically. Oleg decides what to do.

## Hard boundaries

- Do **not** create, edit, or propose final text for ADRs, PDRs, PRRs, work items, GitHub issues, PRs, project-board items, or release notes.
- Do **not** commit, push, tag, merge, open PRs, or perform external writes.
- Do **not** change Architecture files.
- Do **not** change Lore wiki/raw content except writing the daily blast report under `output/`.
- Do **not** turn interesting trends into work automatically.
- Keep the report readable in Discord: titles first, public source URLs visible, no long prose block before the headlines.
- Do not output the old `Alert Oleg` / `Consider now` format. The runner summarizes the `Top stories` section to Discord.
- Do **not** mention internal pipeline/tool names anywhere in the report or runner-facing final response.
- Public sections must link actual source URLs and actual X post URLs. Do not use Lore `raw/`, `wiki/`, or `output/` paths as source citations in public sections.

## Required context

1. Read `output/lore-sourcing-last-run.md` to identify the latest saved public web sources.
2. Read `output/lore-birdclaw-sourcing-last-run.md` to identify whether the X lane produced fresh captures or has a live-sync blocker.
3. Read `output/lore-ingest-last-run.md` to identify newly ingested sources/wiki pages and any ingest blockers.
4. Read recent `raw/` files from the latest sourcing window when the source title/body is needed for the blast, including `raw/*birdclaw-x*.md` only when the Birdclaw summary shows fresh capture or operator-approved local-cache conversion.
5. Read relevant compiled `wiki/` pages only when they clarify why a story matters or whether it is actually new.
6. Read the current HoneyDrunk focus live from:
   `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Architecture\initiatives\current-focus.md`
7. Read the HoneyDrunk charter before making strategic/product/commercial judgments:
   `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Architecture\constitution\charter.md`

## Review method

Build a ranked daily set from the latest saved/ingested Lore sources:

- Prefer items that are new, concrete, and likely to change what Oleg reads, thinks about, evaluates, or acts on.
- Include X captures when they are genuinely useful early signals, primary-source posts, or discussion context; rank them by relevance first and engagement/traction second. If the Birdclaw summary reports a blocker or no fresh items, say so in Review notes and do not fabricate or reuse stale X posts.
- For X captures, prefer posts with meaningful like/repost/reply counts, named builders/researchers/vendors, or concrete source links. Do not pad the X list with generic chatter.
- Bias toward a mixed slate: AI/agents, developer tooling, .NET/Azure, GitHub/DevOps/security, architecture, game/creative tooling, and solo-dev/business when the day's sources support it.
- It is fine to include fewer than ten only if there are fewer than ten useful items. Do not pad with filler.
- Keep Discord-facing story and X lists to ten each.
- For every source line, use the public source URL from frontmatter/body. If only a local raw path is available, open the raw file and extract its `source:` URL.

When ranking each story, ask:

- Is it breaking, primary-source, or otherwise hard to reconstruct later?
- Does it affect current focus, blockers, delivery risk, cost, security, product positioning, or tool choice?
- Does it change a build/buy/adopt/avoid decision for any HoneyDrunk Node?
- Does it expose a new operational risk or cost model?
- Is it source-backed and citation-ready?
- Is it hype with little technical substance? If yes, park it or omit it.

## Output file

Write a dated report:

`output/signal-review-YYYY-MM-DD.md`

Use this structure exactly:

```markdown
# Lore Daily News Blast - YYYY-MM-DD

## Blast summary

- Send to Discord: yes|no
- Theme: <one sentence describing today's useful cluster>
- Coverage: <brief public-friendly description, e.g. "15 web sources and 10 X posts reviewed">

## Top stories

1. <clear title>
   - Main points: <2-3 concise sentences on what happened and what the source is really saying>
   - Source: <publisher/source name>
   - Source URL: <actual public URL>
   - HoneyDrunk angle: <one concise sentence, or "Watch only">

2. <clear title>
   - Main points:
   - Source:
   - Source URL:
   - HoneyDrunk angle:

## Top X posts

1. <post headline or concise claim>
   - Main points: <1-2 concise sentences explaining the post and why it is relevant>
   - Traction: <likes/reposts/replies/views when available, or "traction not available">
   - Source: <@handle>
   - Source URL: <actual X post URL>
   - Follow-up source to look for: <canonical blog/docs/repo/paper if needed>

## Worth watching

- <brief bullets for useful but non-urgent items>

## Parked / low signal

- <brief bullets for noisy, duplicate, or archived-only items>

## Review notes

- Files reviewed: <brief internal count/list; do not include raw filenames unless needed for debugging>
- Blockers:
```

## Final response / alert behavior

After writing the report:

- If `Send to Discord: yes`, reply with a short daily blast for the runner to capture:
  - `Lore Daily News Blast - YYYY-MM-DD`
  - 10 top-story bullets, each with a public source URL
  - 10 top-X-post bullets, each with an actual X URL
  - Path to the report
- If nothing is useful enough for a daily blast, reply exactly:
  `NO_REPLY`

Do not use the old alert/verdict prose. Do not summarize routine parked items in chat.
