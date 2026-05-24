# OpenClaw Lore Signal Review Prompt

Use this prompt for the scheduled Honeyclaw/OpenClaw Lore signal review job.

Working repo: `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Lore`
Architecture repo: `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Architecture`

## Purpose

Lore sourcing and ingest answer: "what should we preserve?" and "how do we structure it?"

This review answers: **"does any newly ingested Lore materially apply to HoneyDrunk, and should Oleg consider it?"**

This is an alerting/recommendation layer only. It must not mutate HoneyDrunk strategy artifacts.

## Hard boundaries

- Do **not** create, edit, or propose final text for ADRs, PDRs, PRRs, issue packets, GitHub issues, PRs, project-board items, or release notes.
- Do **not** commit, push, tag, merge, open PRs, or perform external writes.
- Do **not** change Architecture files.
- Do **not** change Lore wiki/raw content except writing the review report under `output/`.
- Do **not** turn interesting trends into work automatically. Oleg decides.
- Keep alerts sparse. If nothing is genuinely worth Oleg's attention, stay quiet.

## Required context

1. Read `output/openclaw-ingest-last-run.md` to identify newly ingested sources/wiki pages and any ingest blockers.
2. Read the current HoneyDrunk focus live from:
   `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Architecture\initiatives\current-focus.md`
3. Read the HoneyDrunk charter before making strategic/product/commercial judgments:
   `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Architecture\constitution\charter.md`
4. Read only the Lore wiki/raw/output files needed to understand the new signals. Prefer compiled `wiki/` pages and source indexes over raw unless raw detail is necessary.

## Review method

For each newly ingested or materially changed source/page, classify it:

- **Consider now** — materially relevant to active HoneyDrunk focus or near-term execution; Oleg should decide whether to act.
- **Spike candidate** — promising, but needs a small investigation before it should influence work.
- **Watch** — strategically relevant trend, but no near-term action.
- **No action** — preserved in Lore, but not worth attention now.

Bias toward **No action** unless there is a concrete HoneyDrunk implication.

When evaluating relevance, ask:

- Does this affect current focus, blockers, delivery risk, cost, security, or product positioning?
- Does it change a build/buy/adopt/avoid decision for any HoneyDrunk Node?
- Does it expose a new operational risk or cost model we should account for?
- Does it create a low-risk adoption opportunity?
- Is it charter-aligned, or is it venture/hype framing that should be ignored?

## Output file

Write a dated report:

`output/signal-review-YYYY-MM-DD.md`

Use this structure:

```markdown
# Lore Signal Review - YYYY-MM-DD

## Executive verdict

- Alert Oleg: yes|no
- Reason: <one sentence>

## Consider now

- <item or "None">
  - Why it matters:
  - HoneyDrunk surface:
  - Suggested question for Oleg:
  - Source/wiki:

## Spike candidates

- <item or "None">
  - Why it might matter:
  - Smallest useful spike:
  - Source/wiki:

## Watch

- <item or "None">
  - Why to watch:
  - Source/wiki:

## No action / archived only

- <brief bullets for notable reviewed items>

## Review notes

- Files reviewed:
- Blockers:
```

## Final response / alert behavior

After writing the report:

- If **Consider now** or a high-value **Spike candidate** is present, reply to Oleg with a short alert:
  - 1-line verdict
  - 1-3 bullets max
  - Path to the report
- If there is no meaningful alert, reply exactly:
  `NO_REPLY`

Do not summarize routine Watch/No action items in chat.
