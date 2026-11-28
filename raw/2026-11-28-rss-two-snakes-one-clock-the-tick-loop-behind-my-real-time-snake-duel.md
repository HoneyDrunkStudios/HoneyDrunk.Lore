---
source: "https://dev.to/mympgames/two-snakes-one-clock-the-tick-loop-behind-my-real-time-snake-duel-5803"
title: "Two snakes, one clock: the tick loop behind my real-time Snake Duel"
author: "My MP Games"
date_published: "2026-11-28"
date_clipped: "2026-11-28"
category: "Game Development / Unity"
source_type: "rss"
secondary_categories: ["Software Architecture"]
---

# Two snakes, one clock: the tick loop behind my real-time Snake Duel

Most of the games on mympgames.com are turn-based. Chess, Ludo, Battleship and the rest let the server sit there until somebody moves. Snake Duel doesn't work like that. Two snakes share a 24×18 grid, both move on every tick, and the whole match is over in less than a minute. It was the first game on the site where I couldn't just wait for input. The server had to keep its own time.

This post covers how it works: the tick loop, the order collisions get checked in, and a few small decisions that keep it fair. The game module is about 190 lines of plain JavaScript and has no dependencies.

## The server owns the clock

Every real-time game on the site exports the same few functions: `createState`, `onAction`, `tick` and `publicState`. Snake Duel also exports `getTickMs`. The room server runs a self-rescheduling `setTimeout` loop. I didn't use `setInterval`, and the reason is speed ramping, which I'll get to below.

```
const step = () => {
  if (room.status !== 'playing' || !room.state) return;
  if (hasBots(room)) runBotNow(room);
  game.tick(room.state);
  if (room.state.winner != null) {
    room.status = 'finished';
    stopTick(room);
    emitRoom(room);
    return;
  }
  emitState(room, { volatile: true });
  room.tickTimer = setTimeout(step, game.getTickMs(room.state));
};
```

Clients don't simulate anything. They send directions and draw whatever state comes back. That rules out a lot of problems: nobody can speed-hack, nobody can teleport, and the two players never disagree about whether a head touched a body. The cost is that every move takes a round trip. I'll come back to that in the tradeoffs.

## Input is a single slot, not a queue

A keypress doesn't move the snake. It only records what the snake should do on the next tick:

```
function onAction(state, playerIndex, action) {
  const snake = state.snakes[playerIndex];
  const nd = { up: [0, -1], down: [0, 1], left: [-1, 0], right: [1, 0] }[action.dir];
  if (!nd) return { ok: false, error: 'Bad dir' };
  // no reverse into current travel direction
  if (nd[0] === -snake.dir[0] && nd[1] === -snake.dir[1]) {
    return { ok: true, silent: true };
  }
  snake.nextDir = nd;
  return { ok: true, silent: true };
}
```

There are two details worth pointing out.

The reversal check compares against `dir`, the direction the snake actually moved last tick, and not against `nextDir`. This blocks a classic snake bug. Say you're moving right and quickly press up, then left. If I checked against `nextDir`, "left" would pass because the pending direction is "up", and on the next tick your snake would turn straight back into its own neck. Because I check against `dir`, "left" gets rejected and "up" stays queued.

The second detail is the `silent: true` flag. A direction change doesn't trigger a broadcast. The room handler sees that the game is real-time and leaves the broadcast to the next tick. If someone mashes the arrow keys, that costs nothing on the network.

The downside is that I only keep one slot. Two valid turns inside one tick, like up then right, collapse to the last one. Some snake games queue two or three inputs so quick corner turns feel crisp. I went with the simpler model, and at the opening pace of 200ms per tick it's rarely noticeable.

## One tick, in a strict order

Most of the game's rules come down to the order things happen inside `tick()`:

1. Commit each living snake's `nextDir` into `dir`.
2. Work out both next head positions.
3. Check for a head-on collision.
4. Check heads against bodies.
5. Move the survivors and handle food.
6. Decide the winner.

The board edges don't kill you. Heads wrap around to the opposite side:

```
function wrap(n, max) {
  return ((n % max) + max) % max;
}
const next = [wrap(hx + snake.dir[0], W), wrap(hy + snake.dir[1], H)];
```

The double modulo is there because JavaScript's `%` keeps the sign, so `-1 % 24` gives `-1` and not `23`. I chose wrapping because on a small two-player board, wall deaths mostly end rounds before the two snakes have even met. Wrapping keeps the fight about the other snake.

### Collisions are computed before anyone moves

Both snakes are judged against the board as it stood at the start of the tick:

```
// head-on: both die
if (h0 && h1 && h0[0] === h1[0] && h0[1] === h1[1]) {
  state.snakes[0].alive = false;
  state.snakes[1].alive = false;
}

for (let i = 0; i < 2; i++) {
  const [nx, ny] = nextHeads[i];
  for (let j = 0; j < 2; j++) {
    const other = state.snakes[j];
    if (!other.alive && j !== i) continue;
    other.body.forEach(([x, y], k) => {
      if (j === i && k === other.body.length - 1) return; // own tail is moving away
      if (x === nx && y === ny) snake.alive = false;
    });
  }
}
```

Because nobody moves until both snakes have been checked, player 1 never gets an advantage just from being processed first. A few things fall out of this structure:

- **Same target cell.** Both heads land on one cell, so both snakes die.
- **Swapping heads.** If the snakes are nose to nose and both move forward, each new head lands on the other's current head. That's part of a body, so both die too. Head-on is always mutual.
- **Chasing your own tail.** The last segment of your own body is skipped, because it's about to move out of the way. You can follow your own tail in a tight loop. You can't follow the opponent's tail, because the check doesn't make that exception for them.
- **A dead snake isn't an obstacle.** Once the opponent has died, their body stops counting, which is why the `!other.alive` skip is there.

### Growth is "unshift, then maybe pop"

```
const ate = head[0] === state.food[0] && head[1] === state.food[1];
snake.body.unshift(head);
if (ate) {
  snake.score += 1;
  state.food = spawnFood(state.snakes);
} else {
  snake.body.pop();
}
```

Every snake gains a new head on every tick. If it didn't eat, the tail comes off. That's the whole growth mechanic. Food spawns by trying up to 200 random cells, skipping any that a living snake occupies, and falling back to the center of the board. On a 432-cell grid with two snakes on it, the random tries find a free cell almost every time.

## Who wins

```
if (!a0 && !a1) {
  if (s0.score > s1.score) state.winner = 0;
  else if (s1.score > s0.score) state.winner = 1;
  else state.winner = -1; // draw
} else if (!a0) state.winner = 1;
else if (!a1) state.winner = 0;
```

The last snake alive wins. If both die on the same tick, say from a head-on crash or both hitting bodies at once, the one that ate more food takes it. If the scores are also equal, it's a draw. I like this tiebreak because it rewards the player who played well up to the crash, and it means a kamikaze head-on doesn't automatically erase a lead.

## Getting faster as it goes

`getTickMs` starts at 200ms. Every food either snake eats takes 14ms off, and every 12 ticks takes another 3ms. The floor is 60ms. This is why the loop reschedules itself: each tick asks for the next delay based on the current state. The current tick length is also sent in `publicState`, so the client always knows the pace.

## The bot

Solo players get a greedy bot. For each direction other than reversing, it works out the next cell. It gives a huge penalty to anything that hits a body or goes off the edge (it doesn't take advantage of wrapping), and otherwise picks the move with the shortest Manhattan distance to the food. It doesn't look ahead, so you can trap it. That's on purpose: it's an opponent you can beat, not a solver.

## Tradeoffs I accepted

- **Latency vs. authority.** A turn takes effect on the first tick after the server receives it. On a bad connection you feel that. In exchange, both players always see the same result.
- **Full snapshots, volatile delivery.** Every tick sends the entire public state: two bodies, the food, scores and the tick length. On a grid this small that's still a small payload. It goes out as a Socket.IO `volatile` emit, so a client that's falling behind drops frames and catches up, instead of stacking up old ones. Deltas would use less bandwidth, but snapshots can't drift out of sync.
- **Rendering.** The client is a canvas that redraws the full grid on every state update. Heads get a smaller inset so you can tell which end is which.

The game is free and runs in the browser with no sign-up. You can play it against a friend or the bot at <https://mympgames.com/play/snake-duel>, and the rest of the 60+ multiplayer games are at <https://mympgames.com>.
