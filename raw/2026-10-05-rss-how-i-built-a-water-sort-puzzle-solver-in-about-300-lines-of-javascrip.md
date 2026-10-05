---
"source": "https://dev.to/kang_wang_375088cb68739bf/how-i-built-a-water-sort-puzzle-solver-in-about-300-lines-of-javascript-5edi"
"title": "How I built a water sort puzzle solver in about 300 lines of JavaScript"
"author": "kang wang"
"date_published": "2026-10-05"
"date_clipped": "2026-10-05"
"category": "Game Development / Unity"
"source_type": "rss"
---

# How I built a water sort puzzle solver in about 300 lines of JavaScript

Water sort puzzles (also sold as color sort, ball sort or "potion" games) look trivial: a few tubes of stacked colors, pour until every tube holds one color. Then you hit level 140 with two empty tubes, nine colors, and no idea what to do next.

I make a small water sort game for the browser, and I wanted a "hint" that is always right. That turned into a standalone solver: you type in a stuck level and get the moves back, step by step. It is free to use at [chaoschemy.com/tools/water-sort-solver](https://chaoschemy.com/tools/water-sort-solver/), and the core is open source (MIT, no dependencies): [github.com/convee/water-sort-solver](https://github.com/convee/water-sort-solver).

This post walks through how it works: the rules as code, the search, and how it proves that a level has no solution.

##
[
](https://dev.to#1-the-rules-as-code)
1. The rules, as code

A shelf is an array of tubes. Each tube is an array of color indexes from the bottom up, so the last element is the top layer:


```
const tubes = [[0, 1, 0, 1], [1, 0, 1, 0], [], []]; // 4 layers per tube
```


Most mobile games share the same pour rule: you pour the top run of one color onto the same color or into an empty tube, as much of it as fits. I keep the rule as a function that says *why* a pour is not allowed, because the online tool shows that reason to the player:


```
function pourBlock(tubes, from, to, capacity) {
const source = tubes[from], target = tubes[to];
if (from === to) return 'same';
if (!source.length) return 'empty';
if (isSealed(source, capacity)) return 'sealed'; // full and one color: done
if (target.length >= capacity) return 'full';
if (target.length && top(target) !== top(source)) return 'mismatch';
return null; // legal
}
// A legal pour moves the whole top run, or as much of it as fits.
const pourAmount = (tubes, from, to, capacity) =>
pourBlock(tubes, from, to, capacity) ? 0
: Math.min(topRun(tubes[from]), capacity - tubes[to].length);
```


`applyPour`

copies the shelf and moves that many layers. Everything else is built on these three functions.

##
[
](https://dev.to#2-treat-tube-order-as-irrelevant)
2. Treat tube order as irrelevant

Two shelves that differ only in the order of their tubes are the same puzzle. If the search treats them as different states, it explores the same position many times. So the "seen" set uses a canonical key with the tubes sorted:


```
const canonical = (tubes) => tubes.map((t) => t.join('.')).sort().join('|');
```


Without it, every reordering of the same tubes counts as a new state, and a shelf with 10 tubes has up to 10! orderings. It is the cheapest optimization in the whole solver.

##
[
](https://dev.to#3-prune-moves-that-never-help)
3. Prune moves that never help

Some legal pours are pointless:

- pouring out of a sealed tube (it is already done);
- pouring a tube that holds only one color into an empty tube (you just move the problem);
- trying every empty tube as a target, when they are all the same: only the first empty tube is tried.

```
function searchMoves(tubes, capacity) {
const moves = [];
const firstEmpty = tubes.findIndex((t) => !t.length);
for (let from = 0; from < tubes.length; from++) {
const source = tubes[from];
if (!source.length || isSealed(source, capacity)) continue;
const uniform = topRun(source) === source.length;
for (let to = 0; to < tubes.length; to++) {
if (!tubes[to].length && (to !== firstEmpty || uniform)) continue;
if (!pourBlock(tubes, from, to, capacity)) moves.push([from, to]);
}
}
return moves;
}
```


##
[
](https://dev.to#4-a-heuristic-count-the-mess)
4. A heuristic: count the mess

The search needs a guess of "how far from solved" a shelf is. Mine counts two kinds of mess:

- color breaks inside a tube (each place where two different colors touch);
- colors spread over several tubes (a color in 3 tubes adds 2).

```
function estimate(tubes) {
let breaks = 0;
const seen = new Map();
for (const tube of tubes) {
for (let i = 1; i < tube.length; i++) if (tube[i] !== tube[i - 1]) breaks++;
for (const color of new Set(tube)) seen.set(color, (seen.get(color) || 0) + 1);
}
for (const count of seen.values()) breaks += count - 1;
return breaks;
}
```


A solved shelf scores 0. It is not admissible (one pour can fix more than one break), so it does not guarantee shortest solutions, but it points the search in the right direction fast.

##
[
](https://dev.to#5-weighted-bestfirst-search-with-a-budget)
5. Weighted best-first search with a budget

The main search is weighted A*: priority `f = g + w * h`

, where `g`

is pours so far and `h`

is the estimate above. With `w = 2`

the search prefers shelves that look tidy over shelves that are cheap to reach, which finds a solution quickly instead of the shortest one. A plain binary heap holds the open list, and a node budget keeps it from running forever:


```
function guidedSearch(start, { capacity, limit = 40000, weight = 2 } = {}) {
const open = new Heap(), seen = new Set([canonical(start)]);
open.push({ tubes: start, g: 0, f: weight * estimate(start), parent: null, move: null });
let expanded = 0;
while (open.size && expanded < limit) {
const node = open.pop(); expanded++;
if (isSolved(node.tubes, capacity)) return pathTo(node);
for (const [from, to] of searchMoves(node.tubes, capacity)) {
const tubes = applyPour(node.tubes, from, to, capacity);
const key = canonical(tubes);
if (seen.has(key)) continue;
seen.add(key);
const g = node.g + 1;
open.push({ tubes, g, f: g + weight * estimate(tubes), parent: node, move: [from, to] });
}
}
return null; // nothing within the budget
}
```


If that finds nothing, the solver tries once more with a larger budget (400,000 shelves) and a greedier weight (`w = 4`

).

How fast is it? On random solvable shelves with two empty tubes (40 shelves per size, Node 22 on a small Linux server):

| Shelf | Median time | Slowest | Median solution |
|---|---|---|---|
| 5 colors, 3 layers | 0.1 ms | under 1 ms | 11 pours |
| 5 colors, 4 layers | 0.3 ms | 1 ms | 16 pours |
| 8 colors, 4 layers | 0.4 ms | 2 ms | 26 pours |
| 12 colors, 4 layers | 1.5 ms | 26 ms | 41 pours |
| 7 colors, 5 layers | 0.4 ms | 1 ms | 29 pours |

The price of `w = 2`

: on 30 small shelves (4 colors), the guided path was longer than the true shortest one in 19 cases, usually by one or two pours. For a hint button that is fine. Players care that the next move is right, not that the route is optimal.

##
[
](https://dev.to#6-proving-a-level-is-impossible)
6. Proving a level is impossible

Typed-in levels are sometimes wrong (one layer misread), and some shelves really have no solution. "No solution found" is not a useful answer; "this level cannot be solved" is.

So when the guided search gives up, the solver runs a plain breadth-first search over every reachable shelf, with no pruning, and a cap of 300,000 states. If the queue empties before it finds a sorted shelf, the level is proven impossible. If the cap is hit first, the answer is honestly "unknown".


```
function exhaustiveSearch(start, { capacity, cap = 300000 } = {}) {
const parents = new Map([[shelfKey(start), null]]);
let frontier = [start];
while (frontier.length) {
const next = [];
for (const tubes of frontier) {
if (isSolved(tubes, capacity)) return { status: 'solved', path: rebuild(parents, tubes) };
for (let from = 0; from < tubes.length; from++) {
for (let to = 0; to < tubes.length; to++) {
const poured = applyPour(tubes, from, to, capacity);
if (!poured) continue;
const key = shelfKey(poured);
if (parents.has(key)) continue;
if (parents.size >= cap) return { status: 'unknown' };
parents.set(key, { key: shelfKey(tubes), move: [from, to] });
next.push(poured);
}
}
}
frontier = next;
}
return { status: 'impossible' };
}
```


This is cheaper than it sounds. With only one empty tube, very few pours are legal at each step, so the reachable space stays small. On 90 random shelves with one empty tube (4 to 6 colors, 4 layers), 64 were impossible, and each proof took 6 ms or less.

Before any search, a validator checks the obvious mistakes and says exactly what is wrong ("Blue has 3 layers: add 1 more", "Tube 4 holds more than 4 layers"). Most "impossible" levels people type in are really one of these.

##
[
](https://dev.to#7-share-links)
7. Share links

A level fits in a short URL hash, so people can send a stuck level to a friend or bookmark it. Each tube is written bottom to top as letters (`a`

is the first color), empty tubes are `0`

, and the prefix is the tube capacity:


```
c4-abab-baba-0-0
```


Paste that after `#`

on the solver page and the level loads ready to solve: [chaoschemy.com/tools/water-sort-solver/#c4-abab-baba-0-0](https://chaoschemy.com/tools/water-sort-solver/#c4-abab-baba-0-0).

##
[
](https://dev.to#try-it)
Try it

- Online, with a tube editor and step-by-step replay:
[chaoschemy.com/tools/water-sort-solver](https://chaoschemy.com/tools/water-sort-solver/) - Source (MIT, one file, no dependencies, runs in the browser or Node):
[github.com/convee/water-sort-solver](https://github.com/convee/water-sort-solver) - The game it was written for, with a daily shelf:
[Potion Sort](https://chaoschemy.com/games/potion-sort/)

If you know a level layout it struggles with, I'd like to see it: open an issue with the share link.

*Disclosure: I'm a solo developer, and the code was written with AI coding tools.*
