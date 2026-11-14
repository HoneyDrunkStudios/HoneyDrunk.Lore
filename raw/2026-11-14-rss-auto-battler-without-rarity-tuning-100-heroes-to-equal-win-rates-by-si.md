---
source: "https://dev.to/antgamesai/auto-battler-without-rarity-tuning-100-heroes-to-equal-win-rates-by-simulation-2dmg"
title: "Auto battler without rarity: tuning 100 heroes to equal win rates by simulation"
author: "Ant Games"
date_published: "2026-11-14"
date_clipped: "2026-11-14"
category: "Game Development / Unity"
source_type: "rss"
---

# Auto battler without rarity: tuning 100 heroes to equal win rates by simulation

Most auto battlers sell their balance problem as a feature: rare heroes are stronger, so you pull for them. We wanted the opposite, so we built one with no rarity at all. [Ant Games (antgames.ai)](https://antgames.ai/) makes free browser games (our own site: no ads, no purchases, no sign-up), and EQUAL HEROES ARENA has a hundred heroes in ten factions that all cost the same, never level up, and are supposed to win about as often as each other.

"Supposed to" is the hard part. You can't get there by feel with a hundred heroes and a thousand skills, so the numbers come from simulation. This post is how that works, with real snippets from the game's repository and numbers I re-measured while writing it.

A disclosure first: the game and its balance tooling were made with AI agents, on Ant Games' production line (the project was handed to the line as a finished base; agents audited and keep working on it). The game itself is fully in Chinese inside (title 同阶英雄竞技场); its page on our site is in English and Chinese: [English](https://antgames.ai/play/equal-heroes-arena/), [中文](https://antgames.ai/zh/play/equal-heroes-arena/). Everything below is plain JavaScript you can read in the repo's `tools/` folder.

[![EQUAL HEROES ARENA](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F5wtozj9r9se5ee318f5j.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F5wtozj9r9se5ee318f5j.jpg)

## The idea: one budget, one dial

Every hero is built from the same role template (a tank has 1200 HP and 78 ATK, an assassin 700 HP and 128 ATK) and ten skills whose power is priced by a points budget (`js/core/budget.js`, where 1.0 is one basic attack). Authoring by budget gets you into the right neighbourhood, but not the right house.

So each hero gets exactly one balancing number, a **dial**. It is not a grade and the player never sees or changes it. It multiplies HP, ATK and DEF, and also the stat-independent numbers in the kit (shield size, heal percent, buff values), so one number moves everything the hero does:

```
HA.retune = function () {
  for (var n = 0; n < HA.HEROES.length; n++) {
    var h = HA.HEROES[n], t = HA.TUNING && HA.TUNING[h.id], f = (t && t.mult) || 1;
    var slots = dialled[h.id] || (dialled[h.id] = dialSlots(h));
    for (var i = 0; i < slots.length; i++) {
      var s = slots[i], sign = s.v < 0 ? -1 : 1;
      var v = Math.round(Math.abs(s.v) * f / s.q) * s.q;   // authored value, scaled, snapped to its step
      v = Math.min(s.max, Math.max(s.min, v));            // never past the stat's own limits
      s.o[s.k] = sign * Math.round(v * 1000) / 1000;
    }
  }
};
```

Every call starts from the authored numbers, so the tuner can call it thousands of times with different dials. Because skill text in the game is generated from those numbers, the tooltip always says what the retuned skill really does.

## Step 1: make "a fair test" precise

"Win rate" depends entirely on who the hero fights alongside. The tuner uses a sampler of random but sensible teams: a front line, usually a support, and no more than two of any back-line role.

```
plan.push(rng() < 0.8 ? 'tank' : 'fighter');
plan.push(rng() < 0.7 ? (plan[0] === 'tank' ? 'fighter' : 'tank') : null);
let needSupport = rng() < 0.75;
// ...fill the rest from ['assassin','mage','ranger','support'], at most 2 of any
```

Two such teams fight with every hero on its standard build, and each hero's wins are credited to every hero on the winning team. Battles are fully deterministic given a seed (a small mulberry-style generator, `HA.makeRng`), so every number below can be reproduced.

## Step 2: pick the build before you tune the power

A hero brings 6 of its 10 skills (4 actions, 2 passives), so "the hero" is really a family of builds. If you tune power against a bad build you'll boost a hero to compensate for a mistake. So the tool first finds each hero's standard build by greedy search plus single swaps, scored in 1,200 fixed scenarios (random allies, random foes, fixed seeds):

```
// greedy from nothing: which skill helps most next?
for (let step = 0; step < H.LOADOUT_SIZE; step++) { /* try every legal slot, keep the best */ }
// then single swaps until none helps (greedy picks can block a better pair)
for (let round = 0; round < 5; round++) { /* swap one skill; stop when the gain is under 0.002 */ }
```

The score of a scenario is half win/loss and half the HP fraction left, which is much less noisy than win/loss alone. The search also records each skill's value: what you lose by dropping it.

## Step 3: tune the dials by feedback

The core loop is almost embarrassingly simple. Measure every hero's win rate, then nudge its dial against the error:

```
for (const id of ids) mult[id] *= Math.exp(-gain * (m.wr[id] - 0.5));
normalise();   // keep the geometric mean of all dials at 1, bounded to 0.45..2.0
```

The exponential keeps dials positive and symmetric; `normalise()` stops the whole roster drifting stronger together. The tool runs a few coarse passes, re-finds builds, then fine passes: 120,000 battles per pass across worker processes (the header comment quotes about 30,000 battles a second on a 32-thread machine).

## Step 4: equal win rate isn't enough

This is the part I think is worth stealing. If every hero wins 50% of random teams, you can still have a game where nobody picks half of them. A hero can be average in random teams and useless in the best teams, or be in every winning team. So the tuner measures a second thing: for every hero, **search for the best team that contains it** (start from winners of an open self-play league, swap the hero into each seat, mutate, keep the best) and play those hundred teams against the league's best. That number is `top`. Each meta round then combines three readings into one dial update:

```
mult[id] *= Math.exp(-g * (G_TOP * (vS[i] - target)       // best team with this hero vs the league
                         + G_PICK * overPicked(uS[i])      // how many top line-ups field it
                         + G_RATE * (m.wr[id] - 0.5)));    // random-team win rate
```

with `G_RATE = 0.6, G_TOP = 0.5, G_PICK = 0.06`. A hero that is strong only next to certain partners ends up with a lower dial: weak alone, strong in its combo. The best team found for each hero then joins the league, so line-ups the league never reached by itself get their chance to take over. The full run is 30 meta rounds; the shipped table records 35.2 million battles.

## What it produced

The output is a generated file, `js/data/tuning.js`, one line per hero (this is the real first row):

```
wisp: { mult: 1.144, wr: 0.529, top: 0.758, order: ['p3','u2','p2','a3','a1','a2','p1','a4','u1','p4'], val: { ... } },
```

I re-measured it with the game's own sampler and the real engine, 400,000 battles each way, one process (`scripts/article3-measure.cjs` in our SEO folder; about three minutes each):

|  | as authored (every dial 1.0) | shipped tuning |
| --- | --- | --- |
| lowest hero | 30.4% (mycorax) | 42.7% (sylvara) |
| highest hero | 71.4% (morwyn) | 55.3% (nettle) |
| standard deviation | 8.01 points | 3.19 points |
| heroes outside 45-55% | 49 | 12 |
| average battle | 9.03 rounds, 14.9% sudden death | 8.24 rounds, 10.5% sudden death |

The dials that did it run from 0.638 to 1.416. The stored `top` values range from 60.9% to 86.1%: even the weakest hero's best team beats the league's best teams 60.9% of the time here, and no hero's best team falls under 45%.

## Where it falls short

I'd rather tell you than have you find it. Three honest limits, all from our own audit (`docs/audits/balance.md`, 400,000 battles, written by an Opus-class agent that was told to mend nothing):

- **"Equal" means a band of about plus or minus 6 points, not 50.0%.** Twelve heroes sit outside 45-55%; none is outside 40-60. The audit noted the tool could narrow this with a higher `G_RATE` or more passes. We have not.
- **Balancing heroes did not balance the ladder.** The rating numbers shown on the rival ladder (library line-ups) are on the wrong scale between 1400 and 2600: 400 points apart wins about 57%, where the rating formula says 91%. Fixing the hero dials never touched that, because it's a different mechanism (how rivals get rated).
- **Combos add nothing at equal rating** (50.0% in 200 matched pairs). They are already priced into the rating, so tuning combos up on that reading would have been a mistake.

One thing it cleared: with the same line-ups on both sides, side A won 50.3% over 50,000 battles.

## What I would reuse

1. **One dial per entity, applied everywhere the entity's numbers live.** Scaling only HP and ATK misses shields, heals and buffs.
2. **Fix the builds first.** Otherwise the dial absorbs a bad build.
3. **Feedback in log space with a normaliser.** Ten lines, and a few passes settle it.
4. **Measure two things: random-team win rate and best-team strength.** The second one is what keeps a hero from being fair on paper and pointless in practice.
5. **Write the audit that contradicts you.** Ours caught the rating scale, which the hero numbers could never have shown.

To see the result, the game is free and runs in one page: [EQUAL HEROES ARENA](https://antgames.ai/play/equal-heroes-arena/) ([中文页面](https://antgames.ai/zh/play/equal-heroes-arena/)), or the [Ant Games home page](https://antgames.ai/) for the other games. The interface is in Chinese.
