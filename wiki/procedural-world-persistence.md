# Procedural World Persistence

Canonical concept page for generation baselines, saved progress, and cross-version restoration. Evidence and decision limits are recorded below.


## 2026-09-28: Generation recipes and saved progress have distinct compatibility contracts

### Typed entities

person: Krishna Soni; concept: world seed; concept: generator version; concept: baseline-plus-delta persistence; concept: stable entity identifier; concept: save migration.

### Claims and evidence

- Soni proposes storing the seed and generator/content versions separately from changed entities and quest state. A reproducible initial world is not a saved world with player changes; saved random-generator state alone does not preserve inventory or player-built objects. confidence: 1 source, last-confirmed 2026-09-28 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-28-rss-procedural-world-save-state-contract.md)
- A version label requires compatible generation, migration, or enough stored state to restore the world. Stable entity identifiers support applying deltas after an update. The article proposes tests for repeatable generation, progress after reload, fresh-world behavior, and generator changes, and recommends persisting accepted model-generated content when continuity matters. confidence: 1 source, last-confirmed 2026-09-28 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-28-rss-procedural-world-save-state-contract.md)

### Explicit relationships

World reconstruction uses a generation baseline and saved changes; cross-version restoration depends-on stable identities and an explicit compatibility strategy. See [[distributed-systems-patterns]] and [[ai-assisted-game-development-pipelines]].

### Decision and quality notes

Practitioner design proposal, not a demonstrated production persistence system. The source supports acceptance criteria, not a ready-to-adopt schema or evidence that a seed/version tuple guarantees restoration. Source-specific claims remain provisional single-source evidence; related accounts and derived queries add no independent confirmation. Open question: Which baseline, entity identifiers, saved deltas, accepted generated content, and migration tests preserve HoneyDrunk world progress across reloads and generator/content updates? See [[indexes/gaps]].
