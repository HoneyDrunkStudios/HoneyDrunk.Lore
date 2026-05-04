# Audit Trail

Scheduled and large Lore operations should leave concise audit/run summaries in `output/`, especially `output/openclaw-ingest-last-run.md`.

Track:

- operation timestamp and operator/runtime;
- raw sources ingested;
- wiki pages created or updated;
- contradictions resolved or superseded;
- privacy redactions;
- low-quality pages or claims flagged;
- gaps added;
- commit hash, if changes were pushed.

This keeps Lore decision-usable for Honeyclaw, Claude, and future agents.