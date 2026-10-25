---
source: "https://dev.to/blackspectre512/generating-daily-path-puzzles-with-exactly-one-solution-backbite-parity-pruning-and-clue-374f"
title: "Generating daily path puzzles with exactly one solution (backbite, parity pruning and clue minimization)"
author: "Black"
date_published: "2026-10-25"
date_clipped: "2026-10-25"
category: "Game Development / Unity"
source_type: "rss"
---

# Generating daily path puzzles with exactly one solution (backbite, parity pruning and clue minimization)

I built a daily logic puzzle for Android called [Tracewise](https://blacksgit.github.io/tracewise/). The rules fit in one line: draw a single path through every square of the grid, passing the numbered cells in order.

The interesting part isn't the UI. It's making sure that every puzzle, three per day, forever, has **exactly one solution**, is generated on the phone in well under a second, and is the same on every phone so people can compare times. Here's how the generator works, with the Kotlin that does it.

## 1. Start from the answer

You can't sensibly place numbers first and hope a solution exists. So the generator builds the solution first: a random Hamiltonian path (a path that visits every cell once) on an n×n grid.

Random DFS with backtracking works but gets slow and biased on bigger grids. A much nicer trick is the **backbite** move:

1. Start from a boring snake path (left-to-right, then right-to-left, row by row).
2. Pick one end of the path. Pick a random grid neighbour of that end.
3. That neighbour is somewhere in the path. Connect the end to it, which makes a loop, then break the loop at the one edge that keeps it a path. In array terms, that's reversing a prefix (or suffix).

Repeat a few thousand times and the snake turns into a random-looking path, and it's always valid.

```
fun path(n: Int, rnd: Random): IntArray {
    val total = n * n
    val p = IntArray(total) { i -> val r = i / n; val k = i % n; r * n + if (r % 2 == 0) k else n - 1 - k }
    val pos = IntArray(total); for (i in p.indices) pos[p[i]] = i
    fun rev(a: Int, b: Int) {
        var i = a; var j = b
        while (i < j) { val t = p[i]; p[i] = p[j]; p[j] = t; i++; j-- }
        for (k in a..b) pos[p[k]] = k
    }
    repeat(total * 80) {
        val front = rnd.nextBoolean()
        val tip = if (front) p[0] else p[total - 1]
        val nb = neighbours(tip, n)
        val i = pos[nb[rnd.nextInt(nb.size)]]
        if (front) { if (i != 1) rev(0, i - 1) } else { if (i != total - 2) rev(i + 1, total - 1) }
    }
    return p
}
```

`kotlin.random.Random(seed)` is deterministic across platforms, so seeding it from the date gives every player the same path.

## 2. A solver that knows when to quit

To check uniqueness you need a solver that counts solutions, and stops at two. It's a plain DFS from cell 1 that only steps onto a numbered cell if it's the next number. The trick is pruning hard enough that a 7×7 with very few numbers still finishes fast.

Three prunes did almost all the work:

**Checkerboard parity.** Colour the grid like a chessboard. A path alternates colours, so from the current cell the remaining cells must split exactly: if `left` cells remain, the "other" colour needs `same + (left and 1)` of them. Keep two counters updated on every step and this check is O(1). It kills a huge share of branches.

**Dead ends.** The rest of the path runs from the current cell to the finish through every empty cell. So every empty cell except the finish needs at least two free neighbours (counting the current cell). One cell with only one way in, and the branch is dead.

**Connectivity.** A flood fill from the current cell must reach every empty cell.

```
private fun viable(c: Int, left: Int): Boolean {
    val o = free[1 - col(c)]; val same = free[col(c)]
    if (o != same + (left and 1)) return false
    for (u in 0 until total) {
        if (seen[u] || u == end) continue
        var deg = 0
        for (v in nb[u]) if (!seen[v] || v == c) deg++
        if (deg < 2) return false
    }
    // ... flood fill from c, count must equal left
}
```

There's also a node cap. If the solver hits it, the generator treats the puzzle as "not proven unique" and adds a clue. That way generation can never hang on a phone, and it never ships a puzzle it couldn't prove.

## 3. Add clues where the wrong answer goes wrong

With just the start and finish numbered, there are usually thousands of solutions. The loop:

1. Ask the solver for up to 2 solutions.
2. If it finds one that isn't ours, find the first places where that impostor path leaves the real one.
3. Put a number on the real path's cell at one of those places (or, on Hard, a wall across the impostor's step).
4. Repeat until the only solution is the real one.

Adding clues exactly where an alternative solution diverges converges in a handful of rounds instead of sprinkling numbers randomly.

## 4. Then take clues away

The first unique version usually has more numbers than it needs. So the generator walks through the numbers in random order, removes each one, and re-runs the uniqueness check. If the puzzle is still unique, the number stays gone.

That gives a minimal puzzle, which is the Hard level. Medium and Easy get two or three random numbers added back, which is a simple, surprisingly good difficulty dial.

Hard also gets a few walls that the solution never crosses. They don't change the answer, but they change how you reason about the board, and they make Hard look different at a glance.

## Numbers

On a desktop JVM a whole day's set (5×5, 6×6, 7×7) takes under 300 ms in the worst case I've seen, and an 8×8 practice board around 100 to 500 ms. On a phone it runs on a background dispatcher while the home screen draws, so the puzzles are ready before you tap.

A test generates a month of dailies and checks each one: the stored solution is a valid path, the solver finds exactly one solution, and generating the same day twice gives the same clues.

## The app

Tracewise has three dailies (Easy 5×5, Medium 6×6, Hard 7×7), streaks, spoiler-free sharing, hints that repair your line up to the next number, and endless practice up to 8×8. No ads, no account, no internet permission. It's heading to Google Play soon; the page is [blacksgit.github.io/tracewise](https://blacksgit.github.io/tracewise/).

If you like this kind of build log, I post more of them (and the things I make) on [Patreon](https://patreon.com/123black).
