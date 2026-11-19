---
source: "https://dev.to/shariar_saeikshopnil_77c/how-we-generate-endless-always-solvable-pipe-puzzles-in-under-60-lines-of-vanilla-js-19k6"
title: "How we generate endless, always-solvable pipe puzzles in under 60 lines of vanilla JS"
author: "Shariar Saeik Shopnil"
date_published: "2026-11-19"
date_clipped: "2026-11-19"
category: "Game Development / Unity"
source_type: "rss"
---

# How we generate endless, always-solvable pipe puzzles in under 60 lines of vanilla JS

Source: https://dev.to/shariar_saeikshopnil_77c/how-we-generate-endless-always-solvable-pipe-puzzles-in-under-60-lines-of-vanilla-js-19k6

Lantern Links is a pipe puzzle. A glowing core sits near the middle of a grid, every other tile holds a piece of pipe, and you rotate tiles until light reaches every lantern. We wanted levels that never run out, never need a hand-made level file, and are never unsolvable. This post walks through the generator, which is about 60 lines of plain JavaScript inside a single 71 KB `index.html` with no libraries.

A short version of the idea is in a devlog on itch. Here we go deeper into the parts that are easy to get wrong: how the tree is grown, what the seed covers, how par is counted, and how the board shape is chosen.

## The core trick: generate the answer first

Most "shuffle until solvable" approaches generate a random board and then check it. We do the opposite. We build a finished, fully lit board first, and then scramble it. If you start from a solution and only apply moves that the player can undo, the puzzle is solvable by construction. No solver is needed.

A finished board has three properties:

1. Every tile is connected to the core.
2. Every pipe end meets another pipe end (nothing points at the border or at a wall).
3. There are no loops.

A spanning tree of the grid graph has exactly these properties. It reaches every cell, it uses N-1 edges for N cells, and a connected graph with N-1 edges cannot contain a cycle. So the generator is a random spanning tree algorithm.

## Tiles as four bits

Each tile is a 4-bit mask, one bit per side:

```
const N = 1, E = 2, S = 4, W = 8;
const DIRS = [
  { bit: N, dx: 0,  dy: -1, opp: S },
  { bit: E, dx: 1,  dy: 0,  opp: W },
  { bit: S, dx: 0,  dy: 1,  opp: N },
  { bit: W, dx: -1, dy: 0,  opp: E },
];
const rotCW = m => ((m << 1) | (m >> 3)) & 15;
```

Rotating a tile clockwise moves each bit one place left, and the top bit wraps around to the bottom. That is the whole rotation function. The kind of piece falls out of the bit count: one bit is a lantern (a dead end), two opposite bits are a straight, two adjacent bits are a bend, three bits are a junction. There is no separate piece type anywhere in the code.

## Growing the tree

Carving an edge between two neighbours sets one bit on each tile: the direction bit on the tile we leave, and the opposite bit on the tile we enter. Here is the generator, trimmed only of its state handling:

```
function generate(lv, nc, nr) {
  const rnd = mulberry32(lv * 7919 + 17);
  cols = nc; rows = nr;
  const mask = new Array(cols * rows).fill(0);
  const seen = new Array(cols * rows).fill(false);
  source = Math.floor((rows - 1) / 2) * cols + Math.floor((cols - 1) / 2);
  const stack = [source];
  seen[source] = true;
  while (stack.length) {
    const pickIdx = rnd() < 0.45 ? stack.length - 1
                                 : Math.floor(rnd() * stack.length);
    const cur = stack[pickIdx];
    const x = cur % cols, y = (cur / cols) | 0;
    const opts = DIRS.filter(d => {
      const nx = x + d.dx, ny = y + d.dy;
      return nx >= 0 && ny >= 0 && nx < cols && ny < rows && !seen[ny * cols + nx];
    });
    if (!opts.length) { stack.splice(pickIdx, 1); continue; }
    const d = opts[Math.floor(rnd() * opts.length)];
    const nxt = (y + d.dy) * cols + (x + d.dx);
    mask[cur] |= d.bit;
    mask[nxt] |= d.opp;
    seen[nxt] = true;
    stack.push(nxt);
  }
  solution = mask.slice();
  return rnd;
}
```

A plain randomised depth-first search always continues from the newest cell. That makes long, snaking corridors with few branches. Picking a random cell from the frontier instead (the idea behind a randomised Prim's algorithm) gives short, bushy trees with lots of junctions. Neither feels right for this game: the first is too easy to read, the second looks like a mess of crosses.

The line that sets `pickIdx` mixes the two. With probability 0.45 we extend the newest cell (depth-first behaviour), and otherwise we extend a random cell from the stack. This is usually called the growing tree algorithm. The 0.45 is a single constant. Raising it pushes the look of the levels toward corridors, and lowering it toward bushes. Our README describes the generator as a randomised depth-first search, which is accurate for the 45 percent case only, so we are correcting that here.

A cell leaves the stack when it has no unvisited neighbours left. The loop ends when the stack is empty, and because the grid is connected, every cell has been visited by then.

```
 4 x 3 grid, X = core

 o--o--o  o
    |     |
 o--X--o--o
    |
 o--o--o--o

 12 cells, 11 edges, all connected: no loop
```

(X is the core, o is a tile, dashes and bars are carved edges. A cycle would need an edge to a cell that is already in the tree, and the generator never does that.)

## Lanterns are just leaves

Once the tree exists, lanterns need no extra step. A tile with exactly one connection is a leaf, and a leaf is a lantern, unless it is the core:

```
const degree = m => (m & 1) + ((m >> 1) & 1) + ((m >> 2) & 1) + ((m >> 3) & 1);
const isLantern = i => i !== source && degree(solution[i]) === 1;
```

We build the list of lanterns once per level from the solution mask. That is why the lantern count differs from level to level and from seed to seed: it is whatever the tree happens to produce.

## Scramble, and where par comes from

To turn the answer into a puzzle, each tile gets a random number of clockwise quarter turns, and par is the sum of the taps needed to undo them:

```
function tapsTo(m, t) {
  for (let k = 0; k < 4; k++) { if (m === t) return k; m = rotCW(m); }
  return 0;
}

function scramble(rnd) {
  tiles = solution.map(m => {
    let t = m; const r = Math.floor(rnd() * 4);
    for (let i = 0; i < r; i++) t = rotCW(t);
    return t;
  });
  if (computeLit().size === tiles.length) {          // already solved? nudge one tile
    for (let i = 0; i < tiles.length; i++) {
      if (rotCW(tiles[i]) !== tiles[i]) { tiles[i] = rotCW(tiles[i]); break; }
    }
  }
  par = tiles.reduce((s, m, i) => s + tapsTo(m, solution[i]), 0);
}
```

Three details are worth spelling out.

First, `tapsTo` returns the fewest clockwise taps that bring a tile to its target mask, which is 0 to 3. A straight pipe repeats after two turns, so for a straight it is never more than 1; a junction or bend can need up to 3.

Second, there is a guard for the unlucky case where the random rotations leave the board already solved. On a 16-tile board that is not impossible. We turn the first tile that actually changes when rotated.

Third, par is measured against the board we generated, not against a proof of the minimum. We have not shown that every board has only one solved arrangement, so a player who finds a different valid arrangement might beat par. In practice par is a good yardstick, and stars are cheap: three stars at or under par, two up to par plus half of par (rounded up), one otherwise.

## Seeded, so level 12 is level 12

`Math.random()` cannot be seeded, so we use mulberry32, a small 32-bit generator:

```
function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
```

The seed is `lv * 7919 + 17`, so the same level number grows the same tree. The same stream carries on into `scramble`, so the starting orientation is also the same. There is one catch, and it matters for the next section: the tree depends on the board's columns and rows as well as the seed. Level 12 on a 7 by 8 board is the same puzzle for everyone, but level 12 on a 6 by 10 board is a different one.

Restart is a small exception. It keeps the tree and re-scrambles with a time-based seed, so you get the same network with fresh orientations.

## Fitting the board to the screen

The old version of the game used a square board: 4 by 4 at level 1, growing one row and column every three levels, up to 10 by 10. On a phone held upright, a square board leaves most of the screen empty. So the board shape is now chosen at the start of each level from the free space:

```
function sizeFor(lv) { return Math.min(4 + Math.floor((lv - 1) / 3), 10); }

function chooseShape(lv, w, h) {
  const k = sizeFor(lv), lo = k * k, hi = Math.floor(lo * 1.5);
  let best = null;
  for (let c = 3; c <= 12; c++) for (let r = 3; r <= 12; r++) {
    if (Math.min(c, r) > 10) continue;
    const n = c * r;
    if (n < lo || n > hi) continue;
    const t = Math.min(w / c, h / r), fill = n * t * t / (w * h);
    if (!best || fill > best.fill + 0.005 || (fill > best.fill - 0.005 && n < best.n))
      best = { c, r, n, fill };
  }
  return best || { c: k, r: k };
}
```

The tile count is kept between k squared and 1.5 times k squared, so difficulty still grows with the level. Inside that range we try every columns-by-rows pair and score it by `fill`: the share of the free area covered by square tiles, where the tile side `t` is the smaller of the width and height limits. A new candidate wins if it fills clearly more space; if two shapes are within half a percent, the one with fewer tiles wins. The result is, for example, a tall 4 by 6 board on a phone and a wide 5 by 4 on a laptop.

One more rule keeps this from being annoying. While a level is untouched, resizing the window or rotating the phone re-runs `chooseShape` and rebuilds the level. After your first move the shape is frozen and the board only rescales. Otherwise the puzzle would change under your fingers.

## Checking that it is lit

Win detection is a breadth-first walk from the core. A neighbour joins the lit set only if both tiles have a bit facing each other. The level is solved when the lit set holds every tile. We use the same walk to record each tile's distance from the core, which the renderer uses to make light spread outward along the pipes after a move.

## What we would change

- A proof or a quick solver for the minimum number of moves would make par exact rather than "taps to our own answer".
- The 0.45 mix and the 1.5 tile-count ceiling are plain constants, and we have no player data on which values work best.
- Seeding by level and shape means a player on a phone and a player on a laptop see different puzzles under the same level number. That is a trade-off we accepted for the better fit.

## Try it, read it

You can play it in the browser at [webgame.fun/game/lantern-links](https://webgame.fun/game/lantern-links), with no sign-up. The whole game is one MIT-licensed file on [GitHub](https://github.com/ShahriarSaeik/lantern-links), and it is also on [itch.io](https://webgamefun.itch.io/lantern-links). Open `index.html` and search for `generate` to find the code above. If you spot a bug in the generator, or a better way to pick the shape, an issue is welcome.

We are the WebGame.fun team, a small group making free browser games: [webgame.fun](https://webgame.fun).
