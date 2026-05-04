# HoneyDrunk.Lore

The compiled research knowledge surface for HoneyDrunk Studios — a flat-file wiki maintained by OpenClaw/Honeyclaw. Humans and sourcing jobs drop raw sources in, Honeyclaw compiles and reconciles them into structured pages, and Obsidian renders the result as a navigable graph.

## How to use

The wiki has four operations. Ingest/Compile/Lint are OpenClaw/Honeyclaw-owned; Query can be used by Honeyclaw, Claude, or any other agent that reads the compiled `wiki/`. See [`AGENTS.md`](./AGENTS.md) for the full schema.

### Use Lore from Claude or another agent

Claude can still use Lore for decision-making. The important split is:

- OpenClaw/Honeyclaw owns scheduled ingestion and wiki maintenance.
- Claude consumes the compiled `wiki/`, `wiki/indexes/`, and `output/query-*.md` files as shared knowledge.
- Any recommendation based on Lore should cite the wiki/source page and state confidence or gaps.

The legacy [`CLAUDE.md`](./CLAUDE.md) file is intentionally just a pointer to `AGENTS.md` so Claude-oriented tools know where the real contract lives.

### Ingest a new source
1. Drop the source file into `raw/` (markdown, PDF, transcript, repo dump — whatever).
2. Ask Honeyclaw/OpenClaw to *"ingest the new source in `raw/`"*, or let the daily scheduled ingest run.
3. The agent reads the source, updates or creates `wiki/` pages, and adds an entry to `wiki/indexes/sources.md`.

### Daily scheduled ingest

OpenClaw runs a daily Honeyclaw ingest/compile job at **10:00 AM America/New_York** using [`tools/openclaw-lore-ingest-prompt.md`](./tools/openclaw-lore-ingest-prompt.md). It scans unprocessed `raw/` entries, compiles them into `wiki/`, crystallizes durable query outputs, rebuilds indexes, writes `output/openclaw-ingest-last-run.md`, and commits/pushes safe changes.

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
