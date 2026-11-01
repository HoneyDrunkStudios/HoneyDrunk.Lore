---
source: "https://dev.to/chromealex/ten-years-of-rollback-netcode-in-a-cross-platform-rts-without-fixed-point-2c71"
title: "Ten Years of Rollback Netcode in a Cross-Platform RTS, Without Fixed-Point"
author: "Alex Silaev"
date_published: "2026-10-31"
date_clipped: "2026-11-01"
category: "Game Development / Unity"
source_type: "rss"
---

# Ten Years of Rollback Netcode in a Cross-Platform RTS, Without Fixed-Point

Source: https://dev.to/chromealex/ten-years-of-rollback-netcode-in-a-cross-platform-rts-without-fixed-point-2c71

Mushroom Wars 2 is a real-time strategy game with thousands of units on screen. It has been live for about ten years, on Switch, PlayStation, Xbox, PC, iOS and Android, and at various points all of those platforms played against each other on the same servers. The netcode is deterministic lockstep with rollback. The simulation runs on plain `float`. There is no fixed-point math in it.

That last part usually starts an argument, so here is how the whole thing works, what actually breaks determinism in practice, and the one bug that taught me the most.

## The setup: thin server, fat clients

There are a few classic multiplayer architectures: the server simulates and clients render, one client is the master, or every client simulates the same thing. RTS games and fighting games use the last one. Every client runs the full simulation, and only player inputs travel over the network. The server doesn't run game logic at all. It relays packets, and does a few small things like deciding the winner.

That makes the server absurdly cheap. In this setup a $50 server holds around 10,000 connected players. Traffic doesn't depend on the number of units either, which is the only reason thousands of units are possible at all.

Logic runs in fixed ticks. We use 33 ms, so 30 ticks per second. Classic PC RTS games used much longer network turns, around 200 ms in Age of Empires. Rendering and animation run at whatever frame rate the device can do; only the logic is tied to ticks.

## Why rollback, and why StarCraft doesn't need it

Pure lockstep waits: a client doesn't compute tick N until it has every player's input for tick N. On PC that's fine. PC RTS games simply show "waiting for player" when someone lags, and the simulation only ever moves forward.

On mobile that doesn't work. Pings are high and jumpy, matches last three to five minutes, and nobody wants to stare at a waiting screen. So we do what fighting games do.

A client applies its own command immediately, so the game feels offline. The packet goes to the server, which forwards it to everyone else. When another client receives "player 1 did X at tick 1" while it is already at tick 5, it restores a saved snapshot from before tick 1, applies the input, and re-simulates ticks 1 to 5. Visual jumps are smoothed by interpolation, or not smoothed at all if units are slow enough that nobody notices.

Snapshots are taken every 10 to 20 ticks. Fighting games snapshot every tick, because they roll back two or three ticks constantly. We roll back further but less often.

Here is the skeleton. The state of the world is a set of flat arrays of structs, copied wholesale:

```
public sealed class RollbackSimulation {
    private const int SnapshotInterval = 10;
    private const int HistoryTicks = 600; // 20 seconds at 30 ticks per second

    private WorldState current;
    private readonly Dictionary<int, WorldState> snapshots = new Dictionary<int, WorldState>();
    private readonly SortedDictionary<int, List<PlayerInput>> inputs = new SortedDictionary<int, List<PlayerInput>>();
    private int tick;
    private int dirtyFromTick = int.MaxValue;

    public void AddInput(PlayerInput input) {
        if (input.tick <= this.tick - HistoryTicks) return; // too old: this is already a desync
        if (this.inputs.TryGetValue(input.tick, out var list) == false) this.inputs[input.tick] = list = new List<PlayerInput>();
        list.Add(input);
        list.Sort(PlayerInput.Comparer); // order within a tick: by playerId, then by seq
        if (input.tick < this.tick) this.dirtyFromTick = Math.Min(this.dirtyFromTick, input.tick);
    }

    public void Advance(int targetTick) {
        if (this.dirtyFromTick != int.MaxValue) {
            var restoreTick = this.dirtyFromTick - this.dirtyFromTick % SnapshotInterval;
            this.current.CopyFrom(this.snapshots[restoreTick]);
            this.tick = restoreTick;
            this.dirtyFromTick = int.MaxValue;
        }
        while (this.tick < targetTick) {
            if (this.tick % SnapshotInterval == 0) this.SaveSnapshot(this.tick);
            this.inputs.TryGetValue(this.tick, out var list);
            this.current.Step(list); // deterministic logic step
            ++this.tick;
        }
    }

    private void SaveSnapshot(int t) {
        if (this.snapshots.TryGetValue(t, out var s) == false) this.snapshots[t] = s = new WorldState();
        s.CopyFrom(this.current);
        this.snapshots.Remove(t - HistoryTicks);
    }
}
```

Enter fullscreen mode

Exit fullscreen mode

Two details in there matter more than they look.

The `Sort` inside a tick. If two players send commands for the same tick, every client must apply them in the same order. Packet arrival order is different on every client, so it can't be used. Sort by player id, then by sequence number.

The cost of `CopyFrom`. Re-simulating 10 to 20 ticks inside one frame is routine, so copying the world has to be close to a `memcpy`. If a snapshot means walking a thousand objects and allocating, rollback will kill any phone. On our weakest supported devices a logic tick takes about 6 ms out of the 33 ms budget, which leaves room to catch up two or three ticks per frame after a spike.

Free bonus: replays cost nothing. A match is just its inputs. You are always replaying a recording; it just happens to arrive over the network.

## Who wins when two players do the same thing

Say there's one free spot left to build on, and two players click it 33 ms apart. Each one sees their own building first. Then player 2 receives player 1's packet, rolls back to tick 1, applies "player 1 builds here", reaches its own command at tick 2, and the command is now invalid. It stays in the history, it just doesn't do anything. Player 1 does the mirror image: rolls back, keeps their building, skips player 2's command.

Packet arrival order doesn't matter, only the ticks written in the packets. Once all packets have arrived, every client has exactly the same world.

## Floats are deterministic. Mostly.

Here's the part people object to. IEEE 754 defines rounding for basic operations, so the same sequence of additions, multiplications and divisions produces the same bits on compliant hardware. If 10 / 100 comes out as 0.0999999 instead of 0.1, that's fine. What matters is that every client gets the same 0.0999999.

In practice, divergence comes from three places:

1. **The compiler.** Clients built by the same toolchain with the same settings agree. Build two clients differently and they can diverge. Fused multiply-add is the classic culprit: `a * b + c` with one rounding instead of two gives different low bits.
2. **Math libraries.** `sin`, `cos`, `pow` and friends are implemented differently on different platforms. Don't call engine or OS transcendental functions in simulation code. Write your own from basic operations.
3. **A small tail of weird hardware.** We saw divergence on roughly 1% of some Android devices from a few vendors. There are tens of thousands of device models out there, and you can't fix all of them. You can put those players in rooms with each other.

The real modern problem is vectorizing compilers. Unity's Burst, for example, may fuse operations into FMA, reorder them in fast-math modes, or use approximate instructions like `rsqrt` depending on the target CPU. As far as I know, its deterministic float mode was announced but never actually shipped. If you use Burst for simulation, you will probably end up needing something other than float.

On a recent project we went the textbook route and built fixed-point math so everything could go through Burst. Then we took it out again, and performance went up by about 40%. Fixed-point isn't free: every multiply needs a widening and a shift, and `Sqrt`, `Sin` and `Atan2` become hand-written tables or iterations that eat exactly the time you were trying to save.

What I'd recommend today is neither general fixed-point nor float, but plain integers with a unit chosen per quantity. You know the ranges of your own data. If speed never exceeds 100 m/s and a tick never exceeds a second, millimeters and milliseconds are enough:

```
public struct Movement {
    public int positionMm;     // position in millimeters
    public int speedMmPerSec;  // at most 100,000 (100 m/s)

    // deltaMs is at most 1000
    public void Tick(int deltaMs) {
        // 100,000 × 1000 = 10^8, fits in int
        this.positionMm += this.speedMmPerSec * deltaMs / 1000;
    }
}
```

Enter fullscreen mode

Exit fullscreen mode

Integer math is identical on every CPU and costs nothing extra. Division truncates, which can lose precision for very slow objects, but it truncates the same way everywhere, so determinism is safe.

## What actually causes desyncs

In ten years, floats were never our main problem. These were:

* `System.Random` or `UnityEngine.Random` in logic. Randomness must be part of the world state, seeded, and rolled back with it.
* Iterating a `Dictionary` or `HashSet`. Order is not guaranteed.
* `GetHashCode()` on strings and objects. In .NET Core it is randomized per process.
* The engine's physics. PhysX is not deterministic across machines.
* Unstable sorts with equal keys. Always add a secondary key like the entity id.
* Anything that touches `deltaTime`.

And one more category that no rule catches.

## The forgotten field

Our snapshots used to be taken by `CopyFrom` methods written by hand, one per state class. A unit had about a hundred fields. Someone added a new one and forgot to copy it.

Nothing broke. Without a rollback, the field lives its normal life and the game is correct. It only breaks when a rollback lands exactly on a tick where that field matters: one client restores the snapshot and keeps the stale value from the discarded prediction, another client has the correct one. In our case, a building got captured on one client and stayed neutral on the other. Reproducing that by hand is close to impossible.

We caught it with hashes. Clients periodically hash the world state for a tick that is already confirmed (all inputs received) and send it to the server. The share of matches with mismatched hashes is a permanent metric for us. There is always some background noise from the hardware tail above, but one day the rate went up. That meant a new source of divergence, somewhere in code that touches simulation state.

The fix came in two steps. First, a reflection test that finds every type with a `CopyFrom`, fills an instance with random values, copies it, and compares every field, including private ones in base classes. It catches a forgotten field on the first run instead of a hundred matches later. Second, all blittable fields of a unit moved into one struct, so the copy became a single assignment. A new field can't be forgotten anymore, because the compiler copies it.

## Hashes, cheaters, and the 1v1 problem

The same hashes handle cheating. If three clients report hash A and one reports hash B, the odd one out is told to roll back further and re-simulate. A transient glitch fixes itself. A modified client keeps producing B and eventually gets removed from the room. Nobody else notices anything.

In one-on-one games you can't tell who is right with two votes. For that, the server can run a headless client fed with all the match inputs. It renders nothing and re-simulates the whole match almost instantly; whoever it agrees with wins. It's also the best debugging tool we have for real desyncs.

Two practical notes on the hash itself. Don't use `GetHashCode()`. Walk the raw bytes of the state in a fixed order with something simple like FNV-1a, and zero your structs on creation, because padding bytes can contain garbage and break the hash for identical data. And only hash ticks for which all inputs are confirmed, or you'll chase "desyncs" that disappear after the next rollback.

## A self-check worth stealing

The cheapest determinism test we have doesn't need a network. In the editor, a debug mode rolls back one tick on every tick, re-simulates it, and compares the hash. Any state that isn't fully captured by snapshots, any hidden dependency on time or order, shows up immediately, long before a real match.

## Takeaways

* Rollback lets a lockstep game feel offline on bad mobile connections, at the cost of re-simulating ticks. Make snapshots a memory copy, or don't do it.
* Floats can be deterministic in production across consoles, PC and phones, if you control the compiler and stay away from platform math libraries and vectorizing fast-math. Fixed-point is a real cost, not a free safety net.
* Most desyncs come from randomness, iteration order, hashing and hand-written copy code, not from floating point.
* Hash confirmed ticks, track the desync rate as a metric, and keep a headless client on the server for disputes.

---

*I'm Alex Silaev, CTO at Zillion Whales, the studio behind Mushroom Wars 2. This article is based on the networking chapter of my book on Unity performance, memory and architecture, available in English on [Patreon](https://www.patreon.com/chromealex/posts/book-everything-173962820) and [Boosty](https://boosty.to/chromealex/posts/7d456477-1b06-460d-8cc7-5f8defad2dcb). The determinism ideas here also drive [ME.BECS](https://github.com/chromealex/ME.BECS), my open-source deterministic ECS framework for Unity.*
