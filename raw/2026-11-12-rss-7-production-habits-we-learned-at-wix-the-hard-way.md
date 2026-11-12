---
source: "https://www.wix.engineering/post/7-production-habits-we-learned-at-wix-the-hard-way"
title: "7 Production Habits We Learned at Wix. The Hard Way"
author: "Guy Nahum"
date_published: "2026-11-10"
date_clipped: "2026-11-12"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-11-11"
---

# 7 Production Habits We Learned at Wix. The Hard Way

2 days ago

7 min read

![post-mortems software, production, Wix Engineering](https://static.wixstatic.com/media/66bc35_7cae15381dbd476982c28180d7451440~mv2.jpg/v1/fill/w_980,h_576,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/66bc35_7cae15381dbd476982c28180d7451440~mv2.jpg)

## **Introduction**

On-call starts in ten minutes. You feel it - that low-grade dread before the shift begins. The Slack pings, the dashboards you half-understand, the alerts that fire at 2am for reasons.

It doesn't have to feel like that.

After eight years at Wix leading the editor server team, running post-mortems, teaching production bootcamps, and being on the receiving end of more incidents than I care to count, I've found that winning production isn't mainly about better tooling or more headcount. It starts with habits. Small, repeatable behaviors that compound over time until production becomes something you understand and trust, not something you fear.

Here are the seven habits that changed how our team operates.

## **First: The Mindset Shift**

Before the habits, there's a prerequisite. You have to change how you think about production.

**See behind the numbers** It's easy to look at an error rate graph and see... a line. A number. A percentage. But each data point on that graph is a user. A business. Someone who couldn't complete checkout, or save their work, or send a message. Even a 0.001% error rate at Wix scale means something real is happening to real people.

**Stop blaming.** When incidents happen, and they will,  the only useful question is "what can I do better?"

**Believe you can make a difference.** Even if the problem lives in a framework you don't own, or a service run by another team. If you see a gap, own it. Raise the priority. Open the ticket. Make the PR. If you don't, nobody will.

This mindset is the foundation. Everything else builds on it. Habits are the way to turn our mindset into actions.

## **Habit 1: Leave Production Better Than You Found It**

On-call can feel like a jungle. Alerts firing, Slack threads spinning up, half the context living in someone else's head. It's tempting to just survive the shift and hand it off.

Resist that. Production is a marathon, not a sprint.

If on every shift you improve one small thing, such as a noisy alert threshold, a missing log line, a confusing runbook entry, those improvements accumulate. Over time, the jungle becomes a garden. It doesn't happen dramatically, it happens incrementally, one shift at a time, by everyone on the team.

Better to pick one thing and see it through end-to-end than to touch five things and leave all of them half-fixed. Closed loops compound. Open edges don't.

## **Habit 2: Ask Why - Repeatedly**

This is the Five Whys method, and it's deceptively powerful. The idea: when something breaks, don't stop at the first explanation. Keep asking why until you hit something actionable. Here's a real example from our team:

We got an alert: a service was down in a specific datacenter.

- **Why was the service down?** A failing health check to a DB table.
- **Why couldn't the service connect to the table?** A slow query from a dev environment was locking the master DB replica.
- **Why did dev queries even reach the master replica?** They should have been routed to the read replica - or blocked entirely.
- **Why should we have this health check?** Always Question the design and architecture that allowed the symptom to become an incident. Can we still serve traffic while the DB is down?
- **Why did we only find out when the service was already down?** We were missing an upstream alert.

Five whys. Five actionable improvements: better monitoring, query routing fix, a fallback for the DB dependency, a soft-dependency redesign, and an earlier alert threshold. All from one incident, just by not stopping at the first answer.

The point isn't to blame the dev environment or the slow query. The point is to use the incident as a map to where the system is fragile - and fix it.

## **Habit 3: Manage Stress Deliberately**

You are at your best when you're calm. That's not a platitude; it's a practical constraint. Panic narrows thinking. Calm expands it.

Find what works for you. Some people have a mantra. Some people make coffee before touching anything. What works for me is remembering: I'm not alone. There are other engineers, other teams, and we're all trying to solve the problem together.

I had an incident where I'd modified a rendering library, and some time later we started getting alerts - deadlocks taking down random pods in production. The thread dump pointed directly to the class I'd just changed. That's a very specific kind of stress.

I took a breath. Investigated. Fixed the issue. And then crucially I didn't just move on. I wrote a [post](https://www.wix.engineering/post/how-not-to-add-deadlock-to-your-critical-flow-3-simple-steps) for the team: three specific things you should check before modifying code in a critical synchronous flow to avoid introducing a deadlock. The incident became a document. The document prevented future incidents.

Stress is going to happen. The habit is not eliminating it, it's having a practice that lets you get through it without it degrading your judgment.

## **Habit 4: Run Post-Mortems for Learning, Not Blame**

Every significant incident has learning potential. Post-mortems are the ritual for extracting that learning before it fades. A few principles worth holding onto:

The **only** goal is to prevent the same class of problem from happening again. Not to assign responsibility. Not to document that someone made a mistake. To understand what systemic conditions made the mistake possible, and change them.

Do it with the full team, not just the people directly involved. Diverse perspectives surface things that insiders miss. And the people who weren't in the incident room often ask the most useful questions.

Be transparent. A post-mortem that's written defensively is useless. A post-mortem that's honest about what was misunderstood, what signals were missed, and what assumptions were wrong  that's valuable.

## **Habit 5: Run On-Call Handovers as Team Events**

The handover from one on-call engineer to the next is an underrated opportunity. Most teams do it as a quick Slack message or a brief sync between two people. We've found that opening it up to the whole team changes the value dramatically.

What the team gets from a full-team handover:

- **Pattern recognition across shifts.** What if the same flaky alert fired three weeks in a row? With only two-person handovers, you might never notice.
- **Collective challenge of decisions made under pressure.** Sometimes what seemed like the right call at 2am looks different in the light of day with fresh eyes.
- **Shared ownership of follow-up items.** Things that start on one shift don't fall through the cracks.

And something less tangible: if you made it through a week with production stable and users happy, a team handover is the right place to acknowledge that. Keeping production running is real work. It deserves recognition.

## **Habit 6: First Thing, Roll Back - But Understand Why**

When an incident is in flight, time is everything. The fastest path to stability is often the simplest: roll back to the last known good state. Close the experiment. Revert the version.

This is good default thinking. But and this is important, it's a default, not a rule.

I learned this during a shift where we were seeing a high error rate that correlated exactly with a recent service GA. I rolled back immediately, as trained. The error rate got worse.

What had happened: the new version had introduced a change to a cache key. During the gradual rollout, the cache had been warming up gradually. The immediate rollback caused a massive cache invalidation, a cold cache hit wave that hammered the downstream service.

The rollback made it worse because I hadn't understood the system well enough to know that rollback had a cost in this specific case.

The real lesson wasn't "don't roll back." It was: **production doesn't start when you get the alert. Production starts in the design phase.** That cache key change should have been deployed behind a feature toggle, giving us precise control over the exposure and the ability to safely roll it forward or back without side effects.

Roll back is still the right first instinct. Just make sure you understand what rollback means in the context of the specific change.

## **Habit 7: Use AI Across the Entire Production Loop**

This is evolving fast, but the direction is clear: AI is accelerating how quickly code gets written and deployed. The production environment will grow faster, which means the tools we use to understand and manage it need to keep up.

There are a few places where we've found AI genuinely useful in production contexts:

**Investigation.** AI can help you reason through an unfamiliar system, summarize a long incident thread, or suggest hypotheses when you're staring at a log you've never seen before.

**Applying lessons learned.** After a post-mortem, you can encode the lessons as context. Your AI coding tools have access to - specific patterns to avoid, invariants to check, questions to ask before deploying certain kinds of changes. The learning doesn't live only in a doc that nobody reads.

**Day-to-day routines.** Drafting handover summaries. Brainstorming mitigation strategies. Explaining a complex alert to a team member who's newer to the codebase.

The goal isn't to hand production over to AI. The goal is to use it to close the gap between how fast things change and how fast we can understand what's happening.

## **The Seven Habits, Summarized**

1. **Leave production better than you found it**  one small thing per shift, completed end-to-end
2. **Ask why repeatedly**  don't stop at the first explanation, go until you hit something actionable
3. **Manage stress deliberately**  find your practice, and use it
4. **Run post-mortems** for learning, never blame. with the full team, with full transparency
5. **Run on-call handovers as team events** patterns emerge, follow-through happens, ownership spreads
6. **First thing, roll back**  but understand what rollback means in your specific context
7. **Use AI across the loop**  investigation, lesson encoding, day-to-day routines

## **Practical Takeaways**

If you're only going to take one thing from this: pick one habit you're not practicing today, and try it on your next on-call shift. Just one. If it's the Five Whys, write them out after the next incident you're involved in. Force yourself past the first answer.

If it's the handover, invite two more people than usual to the next one. See what they notice. If it's the "leave it better" mindset  before you close your next shift, ask: what's the one thing I could fix right now that would make the next shift easier? Then fix it.

These habits don't require buy-in from leadership or a team-wide initiative. You can start practicing them alone, today. And over time, they change the texture of production  from something you endure to something you actually understand.

Mistakes will keep happening. The goal isn't to eliminate them. The goal is to make sure each one makes the system a little bit better.

![Guy Nahum, Wix Engineering](https://static.wixstatic.com/media/66bc35_b1829c17e1f24c60adaf816451d28bef~mv2.png/v1/fill/w_56,h_49,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/66bc35_b1829c17e1f24c60adaf816451d28bef~mv2.png)

This post was written by Guy Nahum
