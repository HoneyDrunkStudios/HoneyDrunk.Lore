---
source: "https://aplusgamesstudio.com/blog/game-economy-design"
title: "Game economy design: currencies, sources and sinks"
author: "A Plus Games Studio"
date_published: "2026-11-11"
date_clipped: "2026-11-16"
category: "Game Development / Unity"
source_type: "rss"
discovered_via: "https://dev.to/aplusgamesstudio/game-economy-design-currencies-sources-and-sinks-2g80"
---

# Game economy design: currencies, sources and sinks

## The short answer

**A game economy is made of currencies, the sources that create them, the sinks that remove them and the rates between the two. Design it by deciding how long progression should take, listing every source and sink, modelling a typical player's daily earnings and spending in a spreadsheet, and then tuning with real data after launch. The goal is a player who always has something worth saving for and is usually a little short of it.**

## The building blocks

| Element | Meaning | Examples |
| --- | --- | --- |
| Currency | A resource the game counts | Coins, gems, energy, tickets, experience |
| Source | Anything that adds currency | Level rewards, quests, daily login, ads, purchases |
| Sink | Anything that removes currency | Upgrades, items, crafting, entry fees, repairs |
| Rate | How fast sources and sinks run | Coins per minute, cost per upgrade level |
| Store of value | What players accumulate | Characters, buildings, cosmetics, levels |

If sources outrun sinks, currency piles up and loses meaning. If sinks outrun sources, players stall and leave. Balance is the whole job.

## Common currencies

- **Soft currency.** Earned by playing and spent on routine progress. Plentiful.
- **Hard currency.** Bought with money and given out in small amounts. Spent on premium items and shortcuts.
- **Energy or lives.** Limits session length and creates return points.
- **Event currency.** Earned and spent inside a limited-time event, which stops events disturbing the main economy.
- **Experience.** A measure of progress that cannot be spent.

Start with as few as possible. Each extra currency is another thing to explain and another conversion to balance. Many successful games work with two.

## Step 1: define the progression

Before numbers, decide the shape of the journey.

- How long should it take to reach the end of the launch content: two weeks, two months?
- How many sessions a day do you expect, and how long is each?
- What should a player unlock in the first session, the first day, the first week?
- How much faster should a paying player progress?

These time targets turn into every number that follows. See [level design principles](https://aplusgamesstudio.com/blog/level-design-principles) for pacing content alongside the economy.

## Step 2: list sources and sinks

Write every way currency enters and leaves. For each, note whether it is repeatable, capped per day or one-time. Check that:

- Every currency has at least one strong, repeatable sink.
- Late-game players still have sinks that scale.
- No source is unlimited without a matching sink.
- Rewards for skill and rewards for time are both present.

## Step 3: model it in a spreadsheet

Build a simple simulation of a typical player.

1. Estimate earnings per session from each source.
2. Multiply by sessions per day.
3. List the cost of each upgrade or unlock in order.
4. Calculate the day on which each becomes affordable.
5. Compare with your time targets and adjust.

Do this for at least three profiles: a casual player, an engaged player and a payer. Visual modelling tools exist for more complex systems, but a spreadsheet is enough for most games and forces you to state assumptions.

## Step 4: cost and reward curves

Costs usually rise faster than rewards so that each step takes a little longer than the last.

| Curve | Behaviour | Use |
| --- | --- | --- |
| Linear | Each level costs a fixed amount more | Short progressions |
| Polynomial | Costs grow steadily faster | Mid-length progressions |
| Exponential | Costs multiply each level | Idle games and long progressions |

Pair the cost curve with a reward curve that grows more slowly. The ratio between them sets how long each step takes. Idle games depend on this pairing, as covered in [idle game development cost](https://aplusgamesstudio.com/blog/idle-game-development-cost).

## Step 5: pricing real money

- **Anchor the value of hard currency** in time saved or content gained, and keep it consistent.
- **Offer several pack sizes,** with better value at higher prices.
- **Include a low-priced first offer.** The first purchase is the hardest.
- **Use bundles and passes** for clear value. See [battle pass design](https://aplusgamesstudio.com/blog/battle-pass-design).
- **Check regional pricing.** The stores provide local price tiers.
- **Avoid pay-to-win** in competitive games. Selling power damages fairness and long-term retention.

Purchases must be implemented safely, as described in [in-app purchase implementation](https://aplusgamesstudio.com/blog/in-app-purchase-implementation-guide). Ads are also a source and need the same care. See [rewarded ads design](https://aplusgamesstudio.com/blog/rewarded-ads-design).

## Step 6: control inflation

Over time, veteran players accumulate currency. Without control, prices lose meaning and new content is bought instantly.

- Add sinks that scale with wealth: upgrades with rising costs, cosmetics, prestige systems.
- Use percentage-based costs such as taxes or fees in player trading.
- Introduce new tiers of content with new costs.
- Keep event rewards in event currencies.
- Cap storage or daily earnings from repeatable sources.
- Avoid one-off giveaways large enough to flood the economy.

## Step 7: tune with data

No spreadsheet survives contact with players. Track every earn and spend with its source and sink, then watch:

- Average balance by player level. A rising curve means inflation.
- Where players stall for lack of currency.
- Which sinks are used and which are ignored.
- How long real progression takes against your targets.
- Conversion and revenue by offer.

Use remote configuration so values can be changed without an app update, and test changes on a portion of players first. See [game analytics events to track](https://aplusgamesstudio.com/blog/game-analytics-events-to-track) and [mobile game KPIs](https://aplusgamesstudio.com/blog/mobile-game-kpis).

## Player trading and multiplayer economies

When players can trade or sell items to each other, the economy becomes a market with prices you do not set. That brings real-money trading, bots and fraud. It needs monitoring, transaction fees as sinks and anti-fraud work. Most games should not allow free trading unless it is central to the design. Blockchain-based economies add legal and store-policy questions, discussed in [NFT and blockchain game basics](https://aplusgamesstudio.com/blog/nft-blockchain-game-development-basics).

## Premium games have economies too

A paid game without purchases still has an economy: gold, experience, crafting materials and shop prices decide pacing and whether choices feel meaningful. The same method applies, with fun and pacing as the only goals. See [RPG game development cost](https://aplusgamesstudio.com/blog/rpg-game-development-cost).

## Ethics and rules

- Be clear about what purchases give.
- Disclose odds for randomized items, which stores require and some countries regulate.
- Protect children from pressure to spend. See [rules for kids games](https://aplusgamesstudio.com/blog/kids-game-app-store-rules).
- Do not engineer frustration solely to sell the cure. Players notice, and reviews say so.

Economies built on trust last longer and earn more over time.

## Common mistakes

1. Too many currencies.
2. Generous launch rewards that cannot be sustained.
3. No late-game sinks.
4. Numbers hard-coded in the app.
5. Balancing by feel without a model.
6. Copying another game's prices without its content volume.
7. Ignoring the casual player profile.

## Getting help

We design economies, build the models and tune them through soft launch for mobile and PC games. Packages are on [the offer page](https://aplusgamesstudio.com/offer), and our page on [how to earn from games](https://aplusgamesstudio.com/how-to-earn-from-games) compares revenue models.

**Sources:** [Wikipedia: Virtual economy](https://en.wikipedia.org/wiki/Virtual_economy) · [Wikipedia: Game balance](https://en.wikipedia.org/wiki/Game_balance) · [Machinations](https://machinations.io/). Checked November 11, 2026.

Related: [Mobile game development](https://aplusgamesstudio.com/mobile-game-development) · [How to earn from games](https://aplusgamesstudio.com/how-to-earn-from-games) · [Get a quote](https://aplusgamesstudio.com/offer)

FAQ

## Quick answers ❓

What is a game economy?

It is the system of currencies, the sources that give them, the sinks that take them and the rates between, which together control pacing, progression and monetization.

What are sources and sinks in game design?

Sources add currency to the player, such as level rewards and daily bonuses. Sinks remove it, such as upgrades, items and entry fees.

How many currencies should a game have?

As few as possible. Many free-to-play games work with a soft currency earned by playing and a hard currency bought with money, plus temporary event currencies.

How do you stop inflation in a game economy?

With sinks that scale with wealth, new content tiers, percentage-based fees, event currencies kept separate and caps on repeatable sources.

How is a game economy balanced?

By modelling a typical player's earnings and spending in a spreadsheet against time targets, then tuning with analytics and remote configuration after launch.

## Related guides

[Battle pass design →](https://aplusgamesstudio.com/blog/battle-pass-design)
[Mobile game monetization: ads vs IAP →](https://aplusgamesstudio.com/blog/mobile-game-monetization-ads-vs-iap)
