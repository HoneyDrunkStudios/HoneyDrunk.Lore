---
source: "https://dev.to/idlecultivation/four-rounds-of-review-on-my-own-work-and-what-each-caught-ki2"
title: "Four rounds of review on my own work, and what each caught"
author: "IdleCultivation"
date_published: "2026-10-18"
date_clipped: "2026-10-18"
category: "Game Development / Unity"
source_type: "rss"
---

# Four rounds of review on my own work, and what each caught

Development covered **4 Sep 2026 to 6 Sep 2026** (commit dates).

Working alone means nobody hands your change back. Review is not something that happens to you, it is something you schedule, and if you schedule it badly it turns into rereading your own diff and nodding.

[![Myriad Immortal Sect, the game this devlog is about. Play it free in the browser](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F5ry5ba73ahswb860ofof.png)](https://idlecultivation.com/immortal-sect?src=devto)

Over the last few weeks I have settled into running several rounds on anything non trivial, and this stretch produced enough data to say what each round is actually for.

## Round one finds the obvious, and that is not the point

The first pass catches the things you already half knew: the case you did not handle, the message you left in developer language, the value you meant to make configurable.

If review stopped there it would still be worth doing, and it would also be roughly what a careful person catches while writing. The rounds that pay for themselves are the later ones, and what they find is a different category entirely.

## The valuable category is damage you just caused

The single most productive rule I have: after applying a batch of fixes, review the batch, not the original problem.

One night this week that produced seven separate issues, all introduced by that same evening's fixes. Not regressions in old code. New problems created by the repairs, in the hour after they were written, by someone who was concentrating.

The sharpest one: a fix I had recorded as landed had not landed at all. The edit was matching a piece of text that an earlier reformatting had changed, so it quietly applied nothing, and the commit message went on describing behaviour that did not exist. Everything downstream then reasoned from that description. A later round only caught it because the reviewer went to the running code instead of reading the note.

Another was two thresholds that were supposed to be the same number and were not. One value decided when a cooldown was considered finished, another decided when the button lit up. They differed slightly, so when a cooldown hit zero, roughly half the buttons stayed dim, which reads to a player as an input that did not register. Those duties are how a disciple climbs towards an [Elder's Seal](https://idlecultivation.com/article/entity-artifact-elder-seal-elder-s-seal-artifact-guide), one rank at a time.

[![Mission Hall board where duties and their buttons wait on cooldowns](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fsiseqtmp3arlv2ehwpk2.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fsiseqtmp3arlv2ehwpk2.jpg)

## Change the reader, not just the day

The thing that makes a later round productive is that the reader is different. The same person, on the same day, with the same idea of how the change works, finds the same things they found the first time.

I get this by varying who reads: a different model with different habits, or myself after enough time to have lost the mental model. A reviewer who has to reconstruct how it works will question things the author never thought to state, and the questions are the value. Half of what these rounds turn up starts as "why does this compare against that?" rather than as a found defect.

## Silent no-ops are the recurring shape

Almost everything the later rounds catch fails quietly. The fix that did not apply. The two thresholds that nearly matched. A configuration override read before the thing it overrides exists, so the override never takes. A guard whose suite was already failing for an unrelated reason, so the checking process skipped the whole file and nobody saw the guard go dark.

[![Profile settings screen whose options should take effect the moment they change](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Flw0l4sgk3netn05slpmx.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Flw0l4sgk3netn05slpmx.jpg)

None of these produce an error. All of them produce a system that behaves slightly differently from every description of it, including the ones you wrote yourself an hour ago.

If I had to compress the whole practice into one habit, it would be this: before you believe a fix, look at the running thing rather than the record of the change. The record is a claim about the past. The behaviour is the only evidence. What they pay is counted in [Contribution Tokens](https://idlecultivation.com/article/entity-material-contribution-token-contribution-token-material-guide), which is why a dim button matters.

Sect duties are waiting: [take one on in your browser](https://idlecultivation.com/immortal-sect?src=devto). Older posts are collected at [Cultivation Game](https://idlecultivation.com/).

[![Myriad Immortal Sect, the game this devlog is about. Play it free in the browser](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F5ry5ba73ahswb860ofof.png)](https://idlecultivation.com/immortal-sect?src=devto)
