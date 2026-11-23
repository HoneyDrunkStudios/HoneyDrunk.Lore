---
source: "https://solitaire.nnoff.net/updates/update-d5efff91-dbc.html"
title: "Auditing 6.76M Solitaire Deals Offline and Packing 3.56M Verified Wins into 825 KB"
author: "Oleg Neyman"
date_published: "2026-11-22"
date_clipped: "2026-11-22"
category: "Game Development / Unity"
source_type: "web"
discovered_via: "https://dev.to/oleg_neyman_17c7d8d5296c3/auditing-676m-solitaire-deals-offline-and-packing-356m-wins-into-825-kb-38ce"
---

# Auditing 6.76M Solitaire Deals Offline and Packing 3.56M Verified Wins into 825 KB

Why we refused to run a solver on players' phones, how a two-tier .NET audit proved 3,565,003 winning deals and 122,911 impossible ones across seven Solitaire modes, and how a 1-bit-per-seed succinct bitset packs the entire catalog into 845,092 bytes with microsecond uniform random selection.

![Chart of 6.76 million audited Solitaire deals across seven modes alongside the 845,092-byte SSWDCAT1 succinct bitset binary layout and select1 lookup pipeline](https://solitaire.nnoff.net/media/2c8f93a86cc63ebef13197065b99c3cf1153d5574760c2a1c93aeabef78af8be.png)

If you shuffle a standard 52-card deck completely at random in Klondike or 4-suit Spider, a large fraction of deals are mathematically unwinnable before the player touches a single card. Shipping pure random shuffles frustrates players who play cleanly and still hit a brick wall. On the other hand, running a search solver on a phone at deal time burns battery, spikes frame times on budget Android devices, and tempts developers into faking "winning" deals with rigged, repetitive layouts.

We wanted a third option for Solitaire: Klondike & Spider: keep the exact deterministic integer-seed deal generators untouched, audit millions of candidate seeds offline with proof-carrying replay against the real game rules, and pack every verified winner into a compact read-only bitset that picks uniformly in microseconds.

1. Scope and Exact 7-Mode Audit Results

Random winning-deal selection covers seven distinct rule sets, audited across fixed contiguous seed ranges (6,759,994 total candidate deals, 0 unexamined):
- FreeCell (#1 to #1,000,000): 978,019 verified wins (97.80%), 1 proven loss (#33986), 21,980 unresolved
- Spider 2-Suit (899,999 seeds, #100,000 to #999,998): 850,635 verified wins (94.52%), 0 proven losses, 49,364 unresolved
- Klondike Draw 1 Unlimited (989,999 seeds, #10,000 to #999,998): 602,609 verified wins (60.87%), 273 proven losses, 387,117 unresolved
- Spider 4-Suit (899,999 seeds, #100,000 to #999,998): 505,079 verified wins (56.12%), 0 proven losses, 394,920 unresolved
- Klondike Draw 3 Unlimited (989,999 seeds, #10,000 to #999,998): 410,233 verified wins (41.44%), 41,354 proven losses, 538,412 unresolved
- Klondike Draw 3 Limited, 3 passes (989,999 seeds): 157,382 verified wins (15.90%), 63,914 proven losses, 768,703 unresolved
- Klondike Draw 1 Limited, 1 pass (989,999 seeds): 61,046 verified wins (6.17%), 17,369 proven losses, 911,584 unresolved

Across all seven modes, the audit verified 3,565,003 winning deals (52.74%), proved 122,911 deals impossible by exhausting their reachable state graphs, and left 3,072,080 deals unresolved and conservatively excluded from the random pool.

A few details in that table immediately jump out. First, Klondike Draw 1 with 1 pass has far fewer proven wins (6.17%) than Draw 3 with 3 passes (15.90%): a single sweep through the 24-card stock leaves almost no way to recover cards blocked early, whereas three passes of Draw 3 unlock many more orderings. Second, Spider shows 0 proven losses because a 104-card Spider state graph is vastly wider than a 4,096-state exact budget, and our pipeline strictly refuses to label budget exhaustion a loss. Third, 1-suit Spider stays standard random because our deterministic smart deal generator is already overwhelmingly solvable there, and FreeCell keeps manual deal-number selection (#1 to #1,000,000) untouched so players can still dial up any exact deal — including #33986 if they want to verify a proven dead end themselves.

2. Two-Tier Solving and Zero-Trust Proof Replay

Every candidate seed goes through a two-tier offline .NET pipeline (Tools/WinningDeals) built directly against the production SolitaireSuite.Core rule library:
- Tier 1 (Mode-specific fast solvers): Klondike runs a depth-360 DFS (4,000 work budget) over compact integer-array columns with bitmask stock tracking, 192-bit position hashes, and forced safe auto-moves matching the in-game hint engine. Spider runs a depth-320 beam search (90,000 work budget, beam width 8 to 90) bucketed by remaining stock waves on byte-packed boards with 64-bit hashes. FreeCell runs a best-first priority-queue search (5,000 work budget) with a 16-bit 0xDDDD foundation encoding and presenter-matched safe auto-promotions.
- Tier 2 (Exact legal state-graph search): Any seed not solved in Tier 1 enters ExactDealSolver (node cap: 4,096 states for Klondike and Spider, 16,384 states for FreeCell). It traverses the live GameStateModel and IGameRule graph directly using reversible Execute and Undo commands.

Two state-key details turned out to be essential in ExactDealSolver. First, symmetry canonicalization sorts interchangeable tableau columns, foundations, and free cells lexicographically in the visited-state key — with one crucial exception: Spider tableau columns are NOT reordered while stock remains non-empty, because future Spider stock waves deal cards by physical column index. Second, when stock passes are unlimited, the pass counter collapses to zero in the state key so cycling back to an identical board collapses cleanly instead of spinning forever. Crucially, hitting the node cap can only return Unknown; only complete exhaustion of the reachable graph proves Lost.

Most importantly, we do not trust solver shortcuts blindly. Every winning record written to the ledger carries a 64-bit FNV-1a deck fingerprint and the full move-by-move witness string. When exporting the catalog, EmitVerifiedAudit replays all 3,565,003 witnesses from scratch through the real game rules (KlondikeRule, SpiderRule, FreeCellRule) and verifies CheckWinCondition. If a solver ever made an illegal move or drifted from the shuffler, export fails hard.

3. Fault-Tolerant Shards and Measured Solver Optimizations

Auditing 6.76 million deals across multi-hour runs requires crash safety and clean resumption. The ledger stores 26,411 fixed 256-seed gzipped TSV shards (WinningDealAudit2 format), each guarded by a per-batch .lock lease and atomic temp-file swap. Every shard stamps the solver assembly ModuleVersionId and .NET runtime version. Indices step through the seed range using a coprime stride (104,729) so partial runs sample uniformly across the entire range, and re-running with a larger exact node limit is strictly monotonic: already-proven wins and losses are skipped and can never be downgraded.

Before running the wide 4,096-state exact pass, profiling showed ExactDealSolver spending heavy time in GC from per-state canonical key construction and temporary move-pack allocations. Replacing those hot-path allocations with reusable per-search buffers (StringBuilder, char[104] column scratch buffer, PileKey[] sort buffer, and cached CardModel[][] pack buffers) delivered measurable wins across our 7-mode benchmark fixture:
- At 4,096-node limit (1,744 hard candidates): median total dropped from 32.309 s to 26.473 s (1.22x faster), and managed allocations fell 38.3% from 82,383.5 MiB (80.5 GiB) down to 50,805.2 MiB (49.6 GiB).
- At 16,384-node limit (424 hard candidates): median total dropped from 33.300 s to 29.310 s (1.14x faster), with allocations down 35.6% (79,029.3 MiB to 50,862.0 MiB).
- Parallel shard scaling (958 previously-unknown Klondike Draw 1 Limited deals): wall time dropped from 54.71 s on 1 worker to 18.39 s on 4 workers (2.98x speedup).

4. Packing 3,565,003 Deals into 845,092 Bytes (1.90 Bits per Winner)

Once all winning witnesses pass replay, the intermediate generated C# seed array weighs 32,161,864 bytes (30.7 MiB). Even storing 3,565,003 winning seeds as raw 32-bit integers would cost 14,260,012 bytes (13.6 MiB) inside the mobile APK.

Because each mode audits a dense contiguous interval, flipping the representation from a list of integers to a 1-bit-per-seed bitmap collapses the catalog dramatically. Our binary asset (WinningDealsVerified.bytes) uses a dead-simple format:
- 8-byte magic header: SSWDCAT1
- 7 sections, each starting with 12 bytes of little-endian Int32 metadata (firstSeed, seedCount, winnerCount)
- Followed immediately by ceil(seedCount / 8) raw bitmap bytes, where bit i is 1 if and only if (firstSeed + i) has a verified winning witness

Total exact size: 8 + 84 + 845,000 = 845,092 bytes (~825 KB). That is 16.9x smaller than a raw int32 array and averages 1.90 bits per verified winning deal.

At runtime, PackedWinningDealCatalog.TryParse validates the magic bytes, exact file length, expected ranges, zeroed trailing padding bits in each section's final byte, and exact popcount equality against winnerCount. During that single linear pass, it builds a succinct select1 index: a cumulative prefix-sum array (BlockTotals) over 256-byte superblocks. Across all seven modes combined, that index is only 3,312 Int32 values — 13,248 bytes (~12.9 KiB) of RAM.

To pick a uniformly random winning deal with zero bias among the verified pool, the game draws rank = Random.Range(0, winnerCount) and runs Select(mode, rank):
1. Binary search BlockTotals (at most 490 superblocks, <= 9 comparisons) to locate the 256-byte superblock containing that rank.
2. Scan at most 256 bytes linearly using a 256-entry BitsPerByte popcount lookup table.
3. Scan at most 8 bits in the target byte and return firstSeed + byteIndex \* 8 + bit.

The game then feeds that ordinary integer seed into its normal deterministic shuffler. Deal startup takes microseconds, uses zero solver CPU on the player's phone, and preserves exact replayability if a player taps Restart.

5. Honest Tradeoffs and Selection Bias

There is one important nuance worth stating plainly: because 3,072,080 deals hit our bounded search caps and were excluded conservatively rather than solved exhaustively, the current verified pool is not a mathematically uniform sample of all theoretically winnable deals. In tight modes like 1-pass Klondike (6.17% proven), deals requiring unusually deep backtracks are underrepresented compared to deals solvable within our solver budgets.

We accepted that tradeoff intentionally. Players get a strict, proof-carrying guarantee that every random deal in all seven audited modes has at least one legal winning route, without paying battery or latency costs on mobile. And because the runtime catalog loader already checks for a drop-in upgraded file before falling back to the verified snapshot, and our 26,411 audit shards upgrade monotonically, deeper offline passes can expand the catalog later without touching a single line of gameplay code.

This catalog ships today in Solitaire: Klondike & Spider on Android (available via the link in the header above), with full offline play and the exact same deterministic seed engines described here.
