---
source: https://dev.to/focss/how-913-puzzles-became-7304-levels-procedural-variation-on-a-precomputed-puzzle-bank-31d2
title: 'How 913 Puzzles Became 7,304 Levels: Procedural Variation on a Precomputed
  Puzzle Bank'
author: Focss
date_published: '2026-10-04'
date_clipped: '2026-10-04'
category: Game Development / Unity
source_type: rss
capture_method: full-readable-extraction
---

# How 913 Puzzles Became 7,304 Levels: Procedural Variation on a Precomputed Puzzle Bank

Source: https://dev.to/focss/how-913-puzzles-became-7304-levels-procedural-variation-on-a-precomputed-puzzle-bank-31d2

Meowdoku ships over a hundred levels and keeps growing. Every one of them has to be provably solvable. This is a Star Battle-style puzzle, so a malformed board is a dead end the player can't solve.

You can either generate levels at runtime with a solver or hand-author them. Neither works well in practice. Runtime generation puts a backtracking search on the critical path of a player tapping "Next." Hand-authoring doesn't scale past a few dozen boards.

What we ended up doing: **store a finite bank of verified puzzles, and derive variation from geometry instead of content.**

## The data shape

A bank is a JSON dictionary of difficulty tiers. Each entry is small: a region map and a solution.


```
{
"1": [
{
"seed": 7,
"regionMap": [[3,3,0,3],[1,3,3,3],[3,3,2,2],[3,3,3,2]],
"solution": [2,0,3,1],
"r": 1,
"steps": 4
}
]
}
```


`regionMap[r][c]`

is the color-region index of each cell. `solution`

is stored compactly: **one column index per row**, not a 2D grid. Since the rules guarantee exactly one cat per row, `solution[r] = c`

fully describes the answer in `n`

numbers instead of `n²`

.

That's compact for storage, but it doesn't give you a shape you can rotate. You can't rotate an array of row indices; the shape isn't there.

## Picking a level is a pure function

Level selection depends only on the level number, which is what lets the server reproduce the same board:


```
const index = (levelNum - 1) % rawList.length;
const transform = ((levelNum - 1) * 3) % 8; // 4 rotations × 2 reflections
```


`index`

walks the bank; `transform`

picks one of eight symmetries of a square: four rotations, optionally mirrored. Because rotation and reflection preserve the puzzle's constraints, a solved puzzle stays solved under any transform. So the player doesn't see "the same puzzle again," they see a different board that happens to share a skeleton.

Multiplying that out: the 6×6 bank holds 913 entries, which becomes 7,304 distinct boards.

## The transform, and the shape problem

The transform itself has one awkward step:


```
export function transformPuzzle(regionMap: number[][], solution: number[], transform: number) {
const size = regionMap.length;
if (transform === 0) return { regionMap, solution };
// The stored solution is row → col, which isn't a rotatable shape.
// Rebuild it as a 2D boolean grid first.
const catGrid = Array.from({ length: size }, () => Array(size).fill(false));
for (let r = 0; r < size; r++) catGrid[r][solution[r]] = true;
let newMap = regionMap.map(row => [...row]);
let newCats = catGrid.map(row => [...row]);
for (let step = 0; step < transform % 4; step++) {
const rotatedMap = Array.from({ length: size }, () => Array(size).fill(0));
const rotatedCats = Array.from({ length: size }, () => Array(size).fill(false));
for (let r = 0; r < size; r++) {
for (let c = 0; c < size; c++) {
rotatedMap[c][size - 1 - r] = newMap[r][c]; // 90° clockwise
rotatedCats[c][size - 1 - r] = newCats[r][c];
}
}
newMap = rotatedMap;
newCats = rotatedCats;
}
if (transform >= 4) { // then mirror horizontally
for (let r = 0; r < size; r++) { newMap[r].reverse(); newCats[r].reverse(); }
}
// Collapse the boolean grid back into the compact row → col form
const newSolution = new Array(size).fill(-1);
for (let r = 0; r < size; r++) {
for (let c = 0; c < size; c++) if (newCats[r][c]) { newSolution[r] = c; break; }
}
return { regionMap: newMap, solution: newSolution };
}
```


One thing to remember: **compact storage formats and geometric operations rarely mix.** Expanding to a 2D grid, doing both operations there, and collapsing back at the end is clearer and less bug-prone than trying to shortcut the conversion.

## The same function runs on the server

The server can compute the exact board the client is playing, because level selection is pure. It loads the same bank file, caches it in memory, and re-runs the rules to validate a claimed solution:


```
// src/lib/serverLevelValidator.ts
for (const cat of cats) {
if (rowSet.has(cat.r)) return { valid: false, reason: `Multiple cats in row ${cat.r}` };
if (colSet.has(cat.c)) return { valid: false, reason: `Multiple cats in col ${cat.c}` };
const region = regionMap[cat.r][cat.c];
if (regionSet.has(region)) return { valid: false, reason: `Multiple cats in region ${region}` };
rowSet.add(cat.r); colSet.add(cat.c); regionSet.add(region);
}
```


So the server can derive the board from the level number alone. No board state has to be transmitted, stored, or trusted. The same property also powers the daily challenge, which hashes the UTC date string into an `(index, transform)`

pair so every player worldwide gets an identical puzzle with zero server-side scheduling.

## What it costs

There are trade-offs:

-
**Bank size.**The level data is ~67 MB of JSON across 34 files. That's a significant payload, which is why banks are split by grid size and variant type, fetched on demand, and served with`Cache-Control: immutable`

. -
**Memory.**A client-side`Map`

cache holds preloaded levels, and we keep it bounded by only preloading the next five levels. On the server, the same cache is fine because the working set is a handful of files. -
**A solver you still trust.**The bank is the thing you verified once. If a bad puzzle ever gets in, transforms will faithfully replicate it eight ways.

## The takeaway

Precomputing correctness once and varying the geometry is what made this scale. The bank stays small, and the player still sees a new board every level.

Play it here: [https://meowdokuguide.com/online](https://meowdokuguide.com/online)

## Top comments (0)
