---
source: "https://dev.to/chromealex/how-the-bot-in-mushroom-wars-2-works-forecasting-openings-and-honest-difficulty-154m"
title: "How the Bot in Mushroom Wars 2 Works: Forecasting, Openings and Honest Difficulty"
author: "Alex Silaev"
date_published: "2026-10-31"
date_clipped: "2026-10-31"
category: "Game Development / Unity"
source_type: "rss"
---

# How the Bot in Mushroom Wars 2 Works: Forecasting, Openings and Honest Difficulty

Writing a bot that always wins is not the hard part of making an RTS. Writing a bot that's fun to play against is much harder. I've lost count of how many bots I've written. Here's what the bot in Mushroom Wars 2 is built on, what we had to teach it by hand, and how we tune difficulty so players don't feel the bot is throwing the game.

## The core function: "how many will there be in T seconds"

Our bots are built on weights, an approach in the spirit of Utility AI. But weights alone don't get you far if the bot only looks at the current state.

An example. The map has enemy buildings with 50, 10 and 70 units. The bot has 100 units in its building and has to decide where to send them, and whether to send them at all. For simplicity, assume captures trade units one for one. The distances to the targets are 30, 60 and 80.

A human looks at this and thinks: I have 100, they have 50, easy. But every building produces units. So the most important method, and one of the first worth writing, is "how many will there be after some time." It's a universal tool, not just for units in buildings. Say an enemy regenerates HP and is running away from you. From your speed and theirs, you can work out when you'll catch them and how much HP they'll have regained by then. Maybe the chase isn't worth it. Or the other way round: with your damage output, maybe you can finish them off in time.

Most of the bot's decisions rest on this function. Plug it into Utility AI scoring and the bot immediately looks smarter, because it starts predicting: "I'm not going there."

## How the bot picks a target

Back to the map. By the time our units cover 30 meters, the target building will have, say, 60 units. We can still take that: 100 against 60 leaves 40. Great? No.

As soon as we send units, the enemy sees where we're heading and can reinforce the target from nearby buildings. So there's a radius within which we account for the support the target can receive. To those 60 we add the 10 from one neighbor and the 70 from another, but not in full: we account for distance and how many of them can arrive in time. Now we're at, say, 110. Meanwhile, about 10 seconds pass, during which our own building produces another 20.

We add it all up and check whether we win. It can turn out that attacking here makes no sense, and it's better to go for buildings that are farther away but have no nearby point that could wipe us out after our attack. The bot picks what to defend and how to carry out attacks the same way.

The forecasting function is called hundreds of times per decision: for every target, every possible reinforcement, every attack source. So it should be pure and cheap. Here's a sketch for the "production plus reinforcements within a radius" mechanic:

```
public struct Building {
    public float2 pos;
    public float units;
    public float productionPerSec;
    public float capacity;    // limit after which production stops
    public int owner;
}

public static class Forecast {
    public static float UnitsAt(in Building b, float t)
        => math.min(b.units + b.productionPerSec * t, math.max(b.units, b.capacity));

    // How many defenders the target will have when the attack arrives.
    public static float DefendersOnArrival(in NativeArray<Building> all, int target,
                                           float arrivalTime, float unitSpeed,
                                           float supportRadius, float supportShare) {
        var tgt = all[target];
        float total = UnitsAt(tgt, arrivalTime);
        for (int i = 0; i < all.Length; ++i) {
            if (i == target || all[i].owner != tgt.owner) continue;
            float dist = math.distance(all[i].pos, tgt.pos);
            if (dist > supportRadius) continue;
            // The enemy only reacts once it sees our units leave,
            // and only helps if it arrives before we do.
            float travel = dist / unitSpeed;
            if (travel > arrivalTime) continue;
            total += UnitsAt(all[i], arrivalTime - travel) * supportShare;
        }
        return total;
    }
}
```

`supportShare` is your assumption about what fraction of a garrison the opponent will actually send to defend. Against a human, 0.5 to 0.7 is more reasonable than 1, and at high difficulty you can learn from replays how often players really reinforce. The resulting value is normalized and fed into the target's utility score along with the building's value and the risk of a counterattack.

Some games with similar mechanics have bots that reason like this: I have 100, there are 10 next door, so attack. And the bot just keeps feeding units away. In our game, many factors affect whether an attack succeeds. For example, a successful attack grants a kind of morale bonus that affects later attacks and defense. All of that has to be taken into account too.

## Openings: what the bot couldn't learn on its own

We taught the bot to attack and defend, and it all worked. But it couldn't play the start of a match as efficiently as a human. At the beginning the map is empty, surrounded by neutral buildings that don't defend themselves; you just capture them. The bot captured everything, but much more slowly than a top player who has studied every map. And the start of a match shapes everything that follows.

So we recorded openings for it. We literally wrote down the initial moves in several variants, and at the start of a match the bot picks one at random. It develops like a player, and once it holds half the map it switches to its regular logic.

There's nothing wrong with openings, and they're useful in many genres, shooters included. You spawn at a specific location and almost always do one of a few standard things. After that comes micro, which any of the classic algorithms can handle. The key is to keep several variants and choose randomly, otherwise the bot becomes predictable.

## Neural networks: two attempts

The first story isn't mine; a developer I know told it to me. In chess-like games, bots have a problem: they're either too strong or too dumb. Search many plies ahead and the bot is unbeatable. Search only a few, and a strong player calculates three moves ahead and humiliates it. That's exactly what happened to them: a good chess player showed up and tore the bot apart. The developer took a simple perceptron, three layers if I remember right, and fed it a few dozen games from a database. The network's output was a heatmap over the board's squares, and those coefficients were added to the evaluation in the main search algorithm. Even with shallow search, the bot started changing its strategy. It worked, but didn't ship, because of the computational cost of the search itself rather than the network.

My own attempt was in Mushroom Wars. I tried to teach the bot to use skills optimally, and we have a lot of them: speeding up units, burning units in an area, quickly moving units from one building to another, and so on. The bot uses skills at a basic level, and the rules are simple: for example, burning makes sense if the enemy has more units within a radius than some threshold. But when to use them was a big problem. We tried training a network on replays, weren't happy with the results, and dropped it. Most likely we just didn't train enough: there are a million parameters, and it all needs careful tuning.

Between a hard-coded rule and a neural network there are middle-ground options that usually get results faster:

- **Utility AI with forecasting.** Evaluate not "how many enemies are in the radius right now" but "how much value will I destroy or save," using the same "what happens in T" function, and compare that with the cost of the cooldown.
- **Mini-simulation.** If the game rules are deterministic (and in an RTS with lockstep networking they have to be anyway), you can run the simulation a few seconds ahead with and without the ability and compare the outcomes. It's expensive, so candidates are first filtered by simple rules and only the 2 or 3 best are simulated.
- **For chess-like bots,** instead of limiting search depth, it works well to pick not the best move but a random one among moves whose evaluation is within a set margin of the best. That margin is your difficulty knob.

## Making the bot more human

People often ask whether we try to make the bot's behavior more human. Especially in games where everything is easy to compute, like billiards, where the bot wrecks anyone the moment it gets a turn.

Yes, we do. We started by teaching the bot to evaluate mid-match whether it's worth playing to the end: how much territory it holds, how much the enemy has, and so on. The bot has ways to end a match, for example building towers and then surrendering.

In general, every bot probably starts the same way: you write the strongest bot you can. When it becomes uncomfortable to play against, you start handing it difficulty levels, which means making it weaker. The simplest way to weaken a bot in an RTS is a "thinking" delay. The bot starts to fumble: it sent units, should send support, and it's already too late. Things stop adding up, and the difficulty drops.

A couple of details that make such a delay feel natural:

- **The delay shouldn't be a constant.** Draw it from a distribution that resembles human reaction time, for example log-normal with a mean of 300 to 600 ms on easy levels. Apply it not only to reactions but also to how often the bot reconsiders its decisions. Then the bot makes mistakes "like a human": not the same way every time, but occasionally.
- **Degrade perception, not decisions.** A bot that sees worse or notices threats later looks natural. A bot that deliberately picks a worse option reads to players as "the bot is letting me win."

The easiest way to make a bot harder is to give it more at the start or tweak its coefficients: 10% faster production, faster units, more units at the start. But we only do that in the single-player campaign, where players are prepared for the bot to hold half the map from the beginning.

In multiplayer, early on we have bots that teach the player how to play. We gradually make them harder and then release the player to real people. Those bots play fair, one on one, with no handicaps, and the openings exist precisely so they behave like players.

## Synchronized attacks

Here's what we did at the highest difficulty level. Say the bot holds three buildings and wants to attack a fourth. It doesn't send everyone at once. It first sends units from the farthest building; when they reach a certain line, it sends from the next one, then from the third. The whole crowd hits the target at the same moment. It's effective, it looks great, and players love doing it themselves.

Technically it's just planning backwards from the end: compute each group's travel time `t_i = dist_i / speed`, take the maximum `T`, and send group `i` with a delay of `T - t_i`.

## Summary

Whatever you build on, whether FSM, Behaviour Tree, Utility AI or GOAP, two things work on top of it. A forecasting function, "what will happen in T," that makes the bot smarter. And an honest answer to the question of whether it's fun to play against.

---

*I'm Alex Silaev, CTO at Zillion Whales, the studio behind Mushroom Wars 2, and I've been building games in Unity for more than 15 years. This article is adapted from the game AI chapter of my book on Unity performance, memory and architecture, available in English on [Boosty](https://boosty.to/chromealex). More of my work: [GitHub](https://github.com/chromealex), [chromealex.com](https://chromealex.com).*
