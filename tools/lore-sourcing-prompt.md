# Lore Scheduled Sourcing Prompt

You are Honeyclaw running the scheduled Lore sourcing pass for HoneyDrunk.Lore.

Repo: `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Lore`

Goal: source high-signal public/RSS/web items from `sourcing-playbook.md` and save qualifying content into `raw/` as markdown. Do **not** compile `raw/` into `wiki/`; the separate ingest agent owns that.

## Required workflow

1. Read `sourcing-playbook.md` fully enough to understand categories, sources, and relevance criteria.
2. Read `wiki/indexes/sources.md` and inspect existing `raw/*.md` frontmatter to build a dedupe set of known source URLs.
3. Run `python tools/lore_source_birdclaw_recent.py --limit 25 --max-pages 1` before public sourcing so the daily signal review has a fresh X-lane status. If live Birdclaw refresh is blocked, keep going with public sourcing; the script records the blocker in `output/lore-birdclaw-sourcing-last-run.md`. Do not use local-only Birdclaw cache for writes unless the operator explicitly asks for `--allow-local-cache`.
4. Source only public website/RSS/web-accessible written sources that fetch and extract cleanly. Do not source Discord, podcasts, or YouTube by default. Prefer official feeds, blogs, docs, changelogs, support/help-center articles, and indexed announcement pages.
5. Prefer fresh, durable, actionable items relevant to HoneyDrunk: AI/LLM tooling, .NET, Azure, architecture, CI/CD, indie SaaS/devtool strategy, and agent automation.
6. Cap each run at 15 saved public web/RSS items unless the user explicitly asks for a larger harvest. Quality beats volume, but avoid single-vendor monoculture.
7. For each candidate, apply the playbook relevance criteria in order: actionable/instructive, durable, in scope, deep enough. When enough candidates exist, select at least 2 items from each major interest area before filling remaining slots by priority: AI/LLM tooling, .NET, Azure/cloud, DevOps/GitHub/CI, security, game dev, architecture, and technical art/creator tools.
8. Fetch full readable content when possible. If a source cannot be fetched cleanly, skip it rather than saving a stub.
9. Save qualifying items to `raw/` using this filename format:
   `YYYY-MM-DD-source_type-slug.md`
   Examples: `2026-05-04-rss-dotnet-aspire-update.md`, `2026-05-04-web-simonwillison-agent-pattern.md`
10. Every saved file must include frontmatter:

```yaml
---
source: "<original URL>"
title: "<original title>"
author: "<author if available, otherwise unknown>"
date_published: "<YYYY-MM-DD if available, otherwise unknown>"
date_clipped: "<today YYYY-MM-DD>"
category: "<matched playbook category>"
source_type: "rss|web|clipper|birdclaw-x"
---
```

Then include the extracted article/content body in markdown.

11. Deduplicate strictly: skip any URL already present in existing `raw/*.md` frontmatter or `wiki/indexes/sources.md`.
12. Reliability: if one source fails, continue. Do not abort the whole run.
13. At the end, write/update `output/lore-sourcing-last-run.md` with a short summary: timestamp, saved count, skipped duplicate count, failed sources, filenames written, and whether `output/lore-birdclaw-sourcing-last-run.md` reported a Birdclaw blocker.
14. If no qualifying items are found, update the summary and exit cleanly.

## Good default source strategy

Use a mix of:
- Direct feed/page fetches from the playbook where URLs are obvious.
- Web search scoped to the playbook sources when feed discovery is weak.
- Official/vendor public written sources first. Priority order: .NET/Azure/GitHub/TLDR first, then high-signal AI newsletters such as The Rundown AI and AINews/smol.ai, then Anthropic/OpenAI/Hugging Face/Google official blogs/docs/support pages as relevant.
- Recent queries like: `site:devblogs.microsoft.com/dotnet .NET release`, `site:devblogs.microsoft.com/azure-sdk Azure SDK`, `site:github.blog/changelog actions`, `site:tldr.tech AI developer tooling`, `site:therundown.ai/p AI agents`, `site:news.smol.ai AI agents`, `site:anthropic.com/news Claude`, `site:anthropic.com/engineering Claude Code`, `site:support.claude.com Claude Agent SDK`, `site:support.claude.com Claude Code usage`, `site:developers.googleblog.com Gemini API`, `site:blog.google/products/gemini Gemini`, `site:azure.microsoft.com/updates container apps`, `site:martinfowler.com architecture`.

Do not run browser-backed sourcing or audio/video metadata sourcing by default. If a non-website surface points at an important item, find and clip the canonical written website source instead. Birdclaw/X capture is allowed through `tools/lore_source_birdclaw_recent.py` because it records live-sync health and refuses stale local-cache writes by default.
