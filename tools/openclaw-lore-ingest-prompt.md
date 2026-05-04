# OpenClaw Lore Ingest Prompt

Use this prompt for the scheduled Honeyclaw/OpenClaw Lore ingest job.

Working repo: `C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Lore`

You are Honeyclaw running the HoneyDrunk.Lore daily ingest/compile pass.

1. Change to the Lore repo.
2. Read `AGENTS.md` and follow its Ingest and Compile rules exactly.
3. Scan `raw/` for sources not represented in `wiki/indexes/sources.md`.
4. Ingest every unprocessed raw source:
   - never edit/delete files under `raw/`;
   - create/update `wiki/` pages with typed entities, claims, confidence notes, and source citations;
   - preserve superseded claims instead of overwriting them;
   - update `wiki/indexes/sources.md`, `wiki/indexes/topics.md`, and `wiki/indexes/gaps.md` as needed.
5. Crystallize useful durable facts from `output/query-*.md` when they are well-structured, cited, and not merely conversational.
6. Rebuild indexes after the compile pass.
7. Write `output/openclaw-ingest-last-run.md` with:
   - timestamp;
   - count and list of raw sources ingested;
   - wiki pages created/updated;
   - contradictions resolved;
   - gaps logged;
   - blockers, if any.
8. Commit and push safe Lore repo changes with a concise commit message. Do not push if validation or content quality is suspect; instead leave the run summary with blockers.

Stay quiet unless there is a meaningful result, blocker, or failure worth surfacing to Oleg.
