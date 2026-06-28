# HoneyDrunk.Lore

The compiled research knowledge surface for HoneyDrunk Studios — a flat-file wiki maintained by Honeyclaw. Humans and sourcing jobs drop raw sources in, Honeyclaw compiles and reconciles them into structured pages, and Obsidian renders the result as a navigable graph.

## How to use

The wiki has four operations. Ingest/Compile/Lint are Honeyclaw-owned; Query can be used by Honeyclaw, Claude, Codex, or any other agent that reads the compiled `wiki/`. See [`AGENTS.md`](./AGENTS.md) for the full schema.

### Use Lore from Claude or another agent

Claude can still use Lore for decision-making. The important split is:

- Honeyclaw owns scheduled ingestion and wiki maintenance.
- Claude consumes the compiled `wiki/`, `wiki/indexes/`, and `output/query-*.md` files as shared knowledge.
- Any recommendation based on Lore should cite the wiki/source page and state confidence or gaps.

The legacy [`CLAUDE.md`](./CLAUDE.md) file is intentionally just a pointer to `AGENTS.md` so Claude-oriented tools know where the real contract lives.

### Ingest a new source
1. Drop the source file into `raw/` (markdown, PDF, transcript, repo dump — whatever).
2. Ask Honeyclaw to *"ingest the new source in `raw/`"*, or let the daily scheduled ingest run.
3. The agent reads the source, updates or creates `wiki/` pages, and adds an entry to `wiki/indexes/sources.md`.

### Optional Birdclaw X lane

Scheduled Lore sourcing stays website/RSS-first. Use Birdclaw only when you intentionally want to capture a targeted X/Twitter signal because the news is breaking there first, the author is a primary source, or the thread is useful enough to preserve before a canonical writeup exists.

Export the selected Birdclaw items as JSON, then convert them into normal `raw/` files:

```powershell
python tools/lore_source_birdclaw.py path\to\birdclaw-export.json
```

The converter writes `raw/YYYY-MM-DD-birdclaw-x-*.md`, dedupes by source URL/source id, marks the source as an `early-signal`, and strips secret-like values from captured text. When an official blog, changelog, docs page, transcript, or other durable written source becomes available, prefer clipping that canonical source too; keep the X capture when it remains useful as first-report, author-context, or discussion signal.

The scheduled sourcing lane runs:

```powershell
python tools/lore_source_birdclaw_recent.py --limit 25 --max-pages 1
```

That wrapper attempts a live Birdclaw refresh, refuses stale local-cache writes by default, and records health in `output/lore-birdclaw-sourcing-last-run.md`.

### Daily scheduled ingest

Honeyclaw runs a daily Lore ingest/compile job at **10:00 AM America/New_York** using [`tools/lore-ingest-prompt.md`](./tools/lore-ingest-prompt.md). It scans unprocessed `raw/` entries, compiles them into `wiki/`, crystallizes durable query outputs, rebuilds indexes, writes `output/lore-ingest-last-run.md`, and commits/pushes safe changes.

### Compile the wiki
- Say *"run a compile pass"*. The agent picks up any unprocessed `raw/` sources, consolidates reinforced claims, resolves contradictions, and rebuilds `wiki/indexes/`.

### Query the wiki
- Say *"query: <your question>"*. The agent searches `wiki/`, synthesizes an answer with citations, and files the result in `output/` as a dated markdown file. If the wiki cannot answer, the gap is logged in `wiki/indexes/gaps.md`.

### Lint the wiki
- Say *"run a lint pass"*. The agent finds orphan pages, contradictions, stale sources, and decayed claims; auto-fixes what is safe; and writes a report to `output/lint-YYYY-MM-DD.md`.

## Obsidian

The `wiki/` directory is an Obsidian vault. Open it as a vault to get graph view, backlink panels, and `[[wikilink]]` rendering. The flat-markdown layout is intentional — Obsidian needs nothing custom to work.

## Architecture context

- Node overview: `HoneyDrunk.Architecture/repos/HoneyDrunk.Lore/overview.md`
- Boundaries: `HoneyDrunk.Architecture/repos/HoneyDrunk.Lore/boundaries.md`
- Schema and operations: [`AGENTS.md`](./AGENTS.md)

The flat-file implementation is the v1. When `HoneyDrunk.Knowledge` and `HoneyDrunk.Agents` exist, the operations delegate to those Nodes — the wiki content stays where it is. See the *Conversion note* at the bottom of [`AGENTS.md`](./AGENTS.md).
