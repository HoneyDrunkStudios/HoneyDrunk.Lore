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


## 2026-10-25: Daily path puzzles require completed uniqueness proofs and versioned determinism

### Typed entities

project: Tracewise; library: kotlin.random.Random; concept: Hamiltonian path; concept: backbite move; concept: parity pruning; concept: bounded solver; concept: clue minimality.

### Claims and evidence

- The Tracewise author starts from a valid snake path and uses backbite reversals to vary a Hamiltonian path while preserving validity. A DFS counts up to two solutions with checkerboard parity, dead-end, and connectivity pruning; alternative solutions guide new clues, followed by removal attempts that retain uniqueness. confidence: 1 source, last-confirmed 2026-10-25 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-25-rss-generating-daily-path-puzzles-with-exactly-one-solution-backbite-parity-pruning-and-clue-minimization.md)
- The source explicitly treats solver node-cap exhaustion as not proven unique and adds clues. It reports same-date repeatability and a month of generation tests, with desktop JVM timings for daily boards and larger practice boards. Those tests and timings were not reproduced, and a date seed alone does not establish compatibility across future Kotlin/runtime or generator changes. confidence: 1 source, last-confirmed 2026-10-25 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-25-rss-generating-daily-path-puzzles-with-exactly-one-solution-backbite-parity-pruning-and-clue-minimization.md)

### Explicit relationships

Puzzle acceptance depends-on completed uniqueness checking; daily reconstruction uses seeded generation plus a compatible algorithm/runtime contract. This extends earlier bounded-search and save-version evidence on this page.

### Decision and quality notes

Practitioner implementation account with partial code. The removal heuristic is not proof of a globally minimum clue count, uniform random sampling, guaranteed phone latency, or unbounded-date correctness. Test unknown versus unique outcomes and pin generator, PRNG, date/time-zone, and rule versions before using shared dailies. Source-specific claims remain provisional; repeated reports and query outputs add no independent support. Open question: Which puzzle corpus verifies path validity, completed uniqueness proofs, node-cap unknown states, deterministic date/time-zone behavior across pinned runtimes, and phone latency? See [[indexes/gaps]].


## 2026-11-12: Arrow removal puzzles separate solvability from difficulty

### Typed entities

concept: arrow-removal puzzle; concept: reverse construction; concept: dependency DAG; concept: monotone removal; library: OR-Tools CP-SAT; decision: validate generated geometry. file: raw/2026-11-12-rss-how-to-generate-arrow-puzzles-7-algorithms-behind-procedural-level-gen.md.

### Claims and evidence

- The tutorial surveys reverse construction, randomized backtracking, constraint solving, dependency graphs, generate-and-test, templates and evolutionary search. Reverse construction can retain a known removal sequence only when placement checks enforce connected non-overlapping geometry and a clear exit for each newly placed arrow. confidence: 1 source, last-confirmed 2026-11-12 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-12-rss-how-to-generate-arrow-puzzles-7-algorithms-behind-procedural-level-gen.md)
- For the stated removal-only rules, removing an available arrow cannot introduce a blocker, so repeated greedy removal can verify complete clearance. A dependency graph must represent all actual geometric blockers; an abstract DAG alone does not prove that a realizable board exists. confidence: 1 source, last-confirmed 2026-11-12 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-12-rss-how-to-generate-arrow-puzzles-7-algorithms-behind-procedural-level-gen.md)
- Initial availability, dependency depth, unlock patterns and visual density are suggested difficulty proxies. The article explicitly calls for player calibration; more arrows, high fitness or a valid solution do not establish enjoyable or unique gameplay. confidence: 1 source, last-confirmed 2026-11-12 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-12-rss-how-to-generate-arrow-puzzles-7-algorithms-behind-procedural-level-gen.md)

### Explicit relationships

Generation uses constraints and reverse construction; solvability depends-on final geometry and exact removal rules. Difficulty depends-on player evidence. See [[api-testing-and-verification]].

### Decision and quality notes

Single-author instructional proposal with incomplete pseudocode and inconsistent introductory edge direction. No generator, solver or player study was executed. The monotonicity argument does not generalize to mechanics that move, rotate or introduce blockers. Source-specific claims remain provisional; recaptures and derived queries add no independent support. Open question: Which seeded arrow-puzzle corpus verifies body geometry, blocking-edge direction, full removal, generation budgets, structural duplicates and player-calibrated difficulty under the exact rules? See [[indexes/gaps]].

### Resolved source contradiction: blocking direction

Preserved source wording, paraphrased: after saying A blocks B, the introduction says B must leave before A.

- superseded-by: [geometry-derived blocking order](#2026-11-12-arrow-removal-puzzles-separate-solvability-from-difficulty); timestamp: 2026-11-12T09:05:18-05:00; reason: under the article's own clear-exit rule, if A occupies B's exit ray, A must leave before B. Prefer the explicit mechanic and later dependency-list definition over the reversed sentence. The diagram and dependency-list example also disagree, so neither is copied as a verified fixture. [captured source](../raw/2026-11-12-rss-how-to-generate-arrow-puzzles-7-algorithms-behind-procedural-level-gen.md)


## 2026-11-19: Solvable generation preserves a solution under reversible moves

### Typed entities

project: Lantern Links; concept: spanning tree; concept: growing-tree generator; concept: seed identity; concept: rotation symmetry; file: raw/2026-11-19-rss-how-we-generate-endless-always-solvable-pipe-puzzles-in-under-60-lines.md.

### Claims and evidence

- The author builds a connected N-cell/N-minus-one-edge grid tree before rotating tiles, preserving a reachable solution. The generator mixes newest-frontier and random-frontier extension rather than pure depth-first search. confidence: 1 source, last-confirmed 2026-11-19 (archived capture reviewed; no live refresh). [capture](../raw/2026-11-19-rss-how-we-generate-endless-always-solvable-pipe-puzzles-in-under-60-lines.md)
- Reproduction depends on level seed and board dimensions; restart uses a fresh time seed, and responsive shape is frozen after the first move. Par is rotations back to the chosen solution, not a proven minimum across all valid solutions. confidence: 1 source, last-confirmed 2026-11-19 (archived capture reviewed; no live refresh). [capture](../raw/2026-11-19-rss-how-we-generate-endless-always-solvable-pipe-puzzles-in-under-60-lines.md)

### Explicit relationships

Puzzle identity depends-on seed, dimensions and generator version; reversible rotations preserve solvability. See [[gamedev-production-and-community-signals]] and [[agent-evaluation-and-benchmarks]].

### Decision and quality notes

Single JavaScript devlog, not Unity implementation despite feed category. Difficulty constants and par optimality lack player/solver evidence. No game executed. Source-specific claims remain provisional; related/derived reports add no independent confirmation. Open question: Which property tests verify connectivity, reciprocal edges, border safety, rotational solvability and replay identity across viewport shapes, restarts and generator revisions? See [[indexes/gaps]].


## 2026-11-23: Verified seed catalogs preserve unresolved outcomes and rule identity

### Typed entities

concept: deterministic seed; concept: proof replay; concept: bounded solver; concept: succinct bitset; concept: select1 index; project: Solitaire Suite; file: raw/2026-11-22-web-auditing-6-76m-solitaire-deals-offline-and-packing-3-56m-verified-wins.md.

### Claims and evidence

- The game author reports auditing 6,759,994 deals across seven rulesets: 3,565,003 replay-verified wins, 122,911 exhaustive losses and 3,072,080 unresolved cases. Budget exhaustion is not a loss. Winning witnesses replay against production rules before entering the pool; manual FreeCell seed selection and one-suit Spider follow different policies. confidence: 1 source, last-confirmed 2026-11-23 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-22-web-auditing-6-76m-solitaire-deals-offline-and-packing-3-56m-verified-wins.md)
- The reported SSWDCAT1 catalog uses per-mode contiguous seed bitmaps with ranges/counts and validates length, padding and popcounts. Prefix sums over superblocks implement select1 after choosing a winner rank. The reported file is 845,092 bytes; selection is uniform within verified winners, not among all theoretically winnable deals. confidence: 1 source, last-confirmed 2026-11-23 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-22-web-auditing-6-76m-solitaire-deals-offline-and-packing-3-56m-verified-wins.md)
- Solver/rule correctness and hash-state equivalence remain prerequisites: Spider columns cannot be freely canonicalized while stock placement depends on column position. The author reports monotonic offline audit upgrades; changing generator or rules still requires catalog compatibility and replay checks. confidence: 1 source, last-confirmed 2026-11-23 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-22-web-auditing-6-76m-solitaire-deals-offline-and-packing-3-56m-verified-wins.md)

### Explicit relationships

Winning catalogs depend-on rule-bound proof replay; compact lookup uses seed bitmaps and rank selection. See [[formal-methods-and-agent-verification]] and [[unity-3d-and-realtime-vfx-patterns]].

### Decision and quality notes

Self-authored implementation account, not inspected code or a reproduced exhaustive proof. Microsecond selection and mobile shipping are author claims. The arithmetic reconciles; no deployment or game acceptance inferred. Source-specific claims remain provisional; repeated announcements, historical changelog entries and derived queries add no independent support. Open question: Which pinned rule/generator/catalog test verifies witness replay, canonicalization, malformed-file rejection, unbiased rank selection and compatibility across catalog upgrades? See [[indexes/gaps]].


## 2026-11-28: Constructive bank-shot generation preserves a replayable witness

### Typed entities

project: Carom Shot; concept: solution witness; concept: fixed spatial step; concept: aim tolerance; decision: separate solvability from difficulty; file: raw/2026-11-28-rss-always-solvable-puzzle-levels-generate-the-solution-first.md.

### Claims and evidence

- The author generates obstacles, simulates a candidate angle, and places targets along the accepted trajectory. Generation, preview and play reportedly share one fixed-step simulation; rejection rules spread targets over bounce segments and remove trivial straight shots. confidence: 1 source, last-confirmed 2026-11-28 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-28-rss-always-solvable-puzzle-levels-generate-the-solution-first.md)
- The author reports 500/500 generated boards verified in about 85 ms and sweeps 3,000 angles to estimate aim windows. Narrow one-shot windows motivated persistent hits over several shots with a one-shot bonus. These are self-reported tests, not proof of cross-platform floating-point identity or an indefinitely successful bounded generator. confidence: 1 source, last-confirmed 2026-11-28 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-28-rss-always-solvable-puzzle-levels-generate-the-solution-first.md)

### Explicit relationships

Constructive generation uses a solution witness; playable solvability depends-on replay under the same collision rules, while fairness depends-on aim tolerance and input precision. See [[realtime-game-network-protocol-design]].

### Decision and quality notes

AI-assisted developer post with disclosure retained at a high level. No game executed; bounded-attempt exhaustion, witness persistence and device behavior remain unverified. Related puzzle devlogs corroborate the design pattern, not this benchmark. Source-specific claims remain provisional; repeated captures and derived queries add no independent support. Open question: Which property/device tests replay stored solution angles under identical rules and cover generation exhaustion, bounce corners, target radius and touch aim tolerance? See [[indexes/gaps]].
