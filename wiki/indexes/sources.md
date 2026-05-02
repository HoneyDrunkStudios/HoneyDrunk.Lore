# Sources

Auto-maintained by the Ingest and Compile operations. Every file added to `raw/` gets an entry here once it has been ingested.

## Entry format

```
- [<source-title>](../../raw/<filename>) — <one-line summary> — ingested YYYY-MM-DD
```

Per-source authority is not tracked here; it is judged at contradiction-resolution time inside Compile (recency, authority, supporting count). Per-claim reinforcement (`confidence: N sources, last-confirmed YYYY-MM-DD`) lives on the claim inside `wiki/` pages, not in this index.

## Sources

_None yet. Drop a file in `raw/` and run an ingest pass._
