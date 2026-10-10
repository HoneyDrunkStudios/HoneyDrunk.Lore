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


## 2026-09-30: Cross-Platform Save Systems: Cloud Sync Done Right

### Typed entities

project: Unity; concept: save schema; concept: atomic write; concept: cloud sync; concept: conflict resolution.

### Claims and evidence

The [captured source](../raw/2026-09-30-rss-unity-offline-cloud-save-layering.md) records the following attributed summary:

The article separates a Unity save system into a plain C# data model, local persistence, and a replaceable cloud-sync provider. It recommends schema versions, device metadata, atomic writes, rollback copies, and offline-first operation. Multi-device divergence and schema upgrades require explicit conflict and migration behavior, rather than merely uploading serialized state.

### Capture interpretation for HoneyDrunk

For HoneyDrunk, test interrupted writes, divergent offline progress, old save versions, and platform-service failures. The article also proposes local encryption; this capture does not treat client-side encryption as proof of authoritative progression or protection from a player controlling the device.

confidence: 1 source, last-confirmed 2026-09-30 (archived attributed summary reviewed; no live refresh).

### Explicit relationships

Cloud save uses replaceable sync over local persistence; cross-device restoration depends-on conflict and migration contracts.

### Decision and quality notes

Single authored source; source observations and capture recommendations remain provisional. No HoneyDrunk implementation or independently verified outcome is established. Older publication dates remain as recorded in the capture; the confirmation date means archival review. Related reports and derived queries add no independent support. Open question: Which interrupted-write, divergent offline progress, old-schema, and service-failure tests qualify HoneyDrunk game saves? See [[indexes/gaps]].


## 2026-10-04: Puzzle variation preserves a verified baseline

### Typed entities

project: Meowdoku; concept: verified puzzle bank; concept: geometric symmetry; concept: deterministic level selection.

### Claims and evidence

The author derives levels from a preverified bank through rotations/reflections of regions and solutions. Pure level selection lets the server reconstruct boards and validate submitted answers without trusting client board state. Banks are fetched on demand with bounded client preloading. The claimed 913 times eight count is nominal: the capture does not prove all transformed boards are unique or that every bank size visits every index/transform pair. confidence: 1 source, last-confirmed 2026-10-04 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-04-rss-how-913-puzzles-became-7-304-levels-procedural-variation-on-a-precompu.md)

### Explicit relationships

Puzzle validity depends-on verified baseline content and matching transformations; server validation uses deterministic reconstruction.

### Decision and quality notes

Single authored source; source-specific claims remain provisional. Related reports and derived queries add no independent confirmation. No HoneyDrunk integration or independently reproduced outcome is established. Open question: Do HoneyDrunk puzzle tests cover symmetry duplicates, index/transform coverage, bank versioning, complete rules, and cache bounds? See [[indexes/gaps]].


## 2026-10-05: Puzzle search must distinguish budget exhaustion from impossibility

### Typed entities

project: water-sort-solver; concept: weighted best-first search; concept: state canonicalization; concept: exhaustive search.

### Claims and evidence

- The author describes sorting tube representations to collapse symmetric states, pruning redundant moves, and a weighted search with a non-admissible heuristic and bounded retries. The method seeks useful hints, without guaranteeing shortest paths. confidence: 1 source, last-confirmed 2026-10-05 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-05-rss-how-i-built-a-water-sort-puzzle-solver-in-about-300-lines-of-javascrip.md)
- After guided search fails, the reported solver uses breadth-first exploration and returns impossible only if the reachable queue is exhausted; reaching its state cap returns unknown. Input validation checks color counts and tube capacity before search. confidence: 1 source, last-confirmed 2026-10-05 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-05-rss-how-i-built-a-water-sort-puzzle-solver-in-about-300-lines-of-javascrip.md)

### Explicit relationships

Hint search uses canonicalized states; impossibility depends-on exhaustive coverage of the implemented rules.

### Decision and quality notes

Single author demo, disclosed AI-assisted code; linked repository and timings were not reproduced. The purported unpruned fallback still uses applyPour with the earlier sealed-tube rule, so completeness must be established for the exact game rules before treating impossibility as proof. Source-specific claims remain provisional; related reports and derived queries add no independent confirmation. Open question: Do HoneyDrunk puzzle tests prove pruning/canonicalization validity, replayable hints, and impossible-versus-unknown semantics under the actual rules? See [[indexes/gaps]].


## 2026-10-10: Echo Weaver separates loop state from durable player knowledge

### Typed entities

project: Echo Weaver; project: Moonlight Kids; project: Unity 6; concept: loop reset; concept: streamed ownership; decision: separate run state and remembered knowledge.

### Claims and evidence

In Unity's developer interview, Echo Weaver retains run-specific string-keyed state in memory while chunks stream, discards its lightweight essentials scene and run dictionary at reset, and serializes remembered knowledge across loops. Static geometry remains loaded. Recreating door interaction components fixed reset UI state; moving carryable objects out of chunk ownership fixed disappearing or duplicated items. Persistent scene ownership is not by itself a cross-loop save guarantee. confidence: 1 source, last-confirmed 2026-10-10 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-08-rss-echo-weaver-building-a-time-loop-metroidbrainia-in-unity-6.md)

### Explicit relationships

Loop resets use explicit state lifetimes; streamed inventory integrity depends-on ownership outside unloadable chunks. See [[unity-3d-and-realtime-vfx-patterns]].

### Decision and quality notes

Developer production account relayed by Unity, not independently inspected code. A time loop still requires state persistence within each run. Validate disk writes, version migration, carry/reset behavior, and stable keys locally. Source-specific claims remain provisional; derived queries add no independent support. Open question: Which streamed-item ownership, door/UI reset, in-loop reload, cross-loop knowledge, interrupted-save, and migration tests qualify HoneyDrunk game persistence? See [[indexes/gaps]].
