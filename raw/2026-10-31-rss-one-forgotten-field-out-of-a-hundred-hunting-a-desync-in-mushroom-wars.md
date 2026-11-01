---
source: "https://dev.to/chromealex/one-forgotten-field-out-of-a-hundred-hunting-a-desync-in-mushroom-wars-2-427"
title: "One Forgotten Field Out of a Hundred: Hunting a Desync in Mushroom Wars 2"
author: "Alex Silaev"
date_published: "2026-10-31"
date_clipped: "2026-10-31"
category: "Game Development / Unity"
source_type: "rss"
---

# One Forgotten Field Out of a Hundred: Hunting a Desync in Mushroom Wars 2

Some bugs are invisible to the compiler, slip past gameplay tests, and can't be reproduced by hand. In a networked game with rollback, the classic example is a field someone forgot to copy. Here's how we found one in Mushroom Wars 2, and how we made sure this kind of bug can't happen again.

## How our rollback works

Mushroom Wars 2 is an RTS where every player runs the same deterministic simulation and only inputs travel over the network. To avoid waiting for other players' commands, the client simulates ahead using a prediction. Before predicting, it saves a snapshot of the world. When the other players' inputs arrive, the client restores the snapshot and re-simulates those ticks with the correct data.

Snapshots were taken with a `CopyFrom` method on every state class, and each method listed its fields by hand. A unit has around a hundred of them. One day someone added a new field and forgot to add it to the unit's `CopyFrom`.

## Why this bug is nearly invisible

As long as no rollback happens, the field lives its own life and the game behaves correctly. It only breaks when a rollback lands on a moment where that field matters. After the snapshot is restored, one client still holds the value from the discarded prediction, while another holds the correct one. The simulations diverge even though the inputs are identical.

For us it looked like this: on one client a player captured a building, while on the other client the same building stayed neutral. Reproducing that by hand is almost impossible, because you need a rollback on exactly the tick where the forgotten field changes.

## How we found it: hashes

Clients send state hashes to the server, and the share of matches with mismatching hashes is one of our permanent metrics. There is always some background level of desyncs, but at some point the rate went above normal. That was the signal: a new source of divergence had appeared, and it had to be somewhere in code that touches simulation state.

Without that metric, a rare desync would have looked like a handful of odd player reports that nobody could reproduce.

## Step 1: a test that finds the forgotten field

Before touching the code, I asked an AI model to write a test. It finds every class in the project that has a `CopyFrom` method, fills a source object with random values, copies it, and compares every field, private ones included. It's a mechanical task that is easy to verify by eye, which is exactly where AI does well.

```
public class CopyFromTests {

    private static IEnumerable<System.Type> CopyableTypes() {
        return typeof(Unit).Assembly.GetTypes()
            .Where(t => t.IsClass == true && t.IsAbstract == false && t.GetMethod("CopyFrom", new[] { t }) != null);
    }

    [TestCaseSource(nameof(CopyableTypes))]
    public void CopyFromCopiesEveryField(System.Type type) {
        var source = System.Activator.CreateInstance(type);
        var target = System.Activator.CreateInstance(type);
        TestData.FillRandom(source, seed: 42);
        type.GetMethod("CopyFrom", new[] { type }).Invoke(target, new[] { source });
        var flags = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;
        foreach (var field in type.GetFields(flags)) {
            var equal = TestData.DeepEquals(field.GetValue(source), field.GetValue(target));
            Assert.IsTrue(equal, $"{type.Name}.{field.Name} was not copied");
        }
    }

}
```

`TestData.FillRandom` and `TestData.DeepEquals` are recursive helpers that walk into nested structs, lists and arrays. One subtlety: `GetFields` doesn't return private fields declared in base classes, so the real test collects fields by walking up the `BaseType` chain.

A test like this catches a forgotten field on its first run instead of a hundred matches later.

## Step 2: make the mistake impossible

A test is a safety net, but it's better when the mistake simply can't be made. I moved all of the unit's blittable fields into a single struct. Assigning a struct copies it in full, so `CopyFrom` shrank to one line for the data plus manual copying of a few reference fields:

```
public struct UnitData {
    public int ownerId;
    public int health;
    public float captureProgress;
    // ...and about a hundred more blittable fields
}

public class Unit {

    public UnitData data;
    public List<int> path = new List<int>();

    public void CopyFrom(Unit other) {
        this.data = other.data;
        this.path.Clear();
        this.path.AddRange(other.path);
    }

}
```

The field names here are illustrative. The point is that a hundred lines of assignments became one. A new field added to the struct is copied automatically, so there's no way to forget it anymore.

## The result

This class of bugs is gone. The compiler copies the fields inside the struct, and the test guards the few reference fields that are still copied by hand. It runs on every change and immediately names the class and the field that was missed.

What I took away from this:

- **Listing fields by hand in copy, compare or serialization code is a time bomb.** The more fields there are, the more certain it is that one of them will eventually be forgotten.
- **Keep simulation state in blittable structs.** Copying, hashing and serialization then become operations on a single block of memory. My ECS framework [ME.BECS](https://github.com/chromealex/ME.BECS) is built on this idea: the whole world state there is one block of memory.
- **Compare state hashes between clients every few ticks.** Then you see a desync on the tick it happened, not when a player complains.
- **Tests for mechanical invariants like "the copy equals the original" are a great job for AI.** They're easy to review and pay off a lot.

---

*I'm Alex Silaev, CTO at Zillion Whales, the studio behind Mushroom Wars 2, and I've been building games in Unity for more than 15 years. This is one of the production stories from my book on Unity performance, memory and architecture (currently in Russian). More of my work: [GitHub](https://github.com/chromealex), [chromealex.com](https://chromealex.com).*
