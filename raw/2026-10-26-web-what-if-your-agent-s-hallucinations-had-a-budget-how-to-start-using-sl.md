---
source: "https://grafana.com/blog/what-if-your-agent-s-hallucinations-had-a-budget-how-to-start-using-slos-for-agent-behavior/"
title: "What if your agent's hallucinations had a budget? How to start using SLOs for agent behavior"
author: "Ivana Huckova"
date_published: "2026-09-24"
category: "DevOps & CI/CD"
source_type: "web"
date_clipped: "2026-10-26"
---

# What if your agent's hallucinations had a budget? How to start using SLOs for agent behavior

![What if your agent's hallucinations had a budget? How to start using SLOs for agent behavior](https://grafana.com/mw/_next/image/?url=https%3A%2F%2Fa-us.storyblok.com%2Ff%2F1022730%2F1200x630%2F2f346b408d%2Fslo-for-agents-meta.jpeg&w=3840&q=75)

# What if your agent's hallucinations had a budget? How to start using SLOs for agent behavior

[![Ivana Huckova](https://grafana.com/mw/_next/image/?url=https%3A%2F%2Fs3.amazonaws.com%2Fa-us.storyblok.com%2Ff%2F1022730%2F022eb23c76%2Fivana_huckova.jpg&w=3840&q=75)

Ivana Huckova](https://grafana.com/author/ivana?pg=what-if-your-agent-s-hallucinations-had-a-budget-how-to-start-using-slos-for-agent-behavior)

•

2026-09-24•10 min

[![Twitter](https://a-us.storyblok.com/f/1022730/18x14/455626a417/icon-twitter-gray.svg)](https://twitter.com/intent/tweet?text=What%20if%20your%20agent's%20hallucinations%20had%20a%20budget%3F%20How%20to%20start%20using%20SLOs%20for%20agent%20behavior&url=)[![Facebook](https://a-us.storyblok.com/f/1022730/8x14/08ec63c702/icon-facebook-gray-sm.svg)](https://www.facebook.com/sharer/sharer.php?u=)[![LinkedIn](https://a-us.storyblok.com/f/1022730/16x16/6788867fe2/icon-linkedin-grey.svg)](https://www.linkedin.com/sharing/share-offsite/?url=)

At Grafana Labs, observability is what we do. So as we started building AI agents, we naturally reached for the same instincts we bring to every system: measure it, set targets, and make reliability something you can reason about instead of hope for.

That instinct led us somewhere unexpectedly useful. It turns out one of the oldest ideas in reliability engineering, the error budget, maps beautifully onto one of the newest problems in software: how do you know if an AI agent is actually any good?

This is what we discovered when we pointed our observability toolkit at agent behavior. We think it's a genuinely clean way to think about agent quality, and we want to share it with you.

## **The part of the agent you can't see**

You can have every usual signal in place: latency, token counts, error rates, traces of every tool call. And none of them answer the question that matters most for an agent: *Is it good?* 

A response can come back in 800 milliseconds, cost almost nothing, throw zero errors, **and still be confidently, fluently wrong**. 

That gap matters because every change to your agent is a small gamble when you can't measure quality. Tweak a prompt and hope; swap a model and cross your fingers; ship it and wait for someone to complain. These are the exact blind spot observability exists to remove.

## **Turn behavior into a number with evaluations**

So we measure behavior directly using evaluations; the same way we once turned "Is the site up?" into a simple percentage.

That's really all an [evaluation](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) is, after all. You ask a judge—often another language model—to read a conversation, or a single message, or one tool call, and score it. 

Was it grounded in the context it was given, or did it make things up? Did it actually do what the user asked? Was it toxic? Did it leak personal information? Did it fall for a prompt injection? The judge hands back a verdict, pass or fail, or a rating on a scale, and suddenly the thing you couldn't see has a value you can look at.

Some of these you don't even need a model for. A humble regex knows perfectly well whether a response leaked an API key or name-dropped a competitor. In Grafana Cloud's [Agent Observability](https://grafana.com/products/cloud/agent-observability?pg=what-if-your-agent-s-hallucinations-had-a-budget-how-to-start-using-slos-for-agent-behavior&plcmt=in-text), the cheap deterministic checks and the fancier model-based judges sit happily side by side.

One thing worth saying early: quality isn't a single number. "Good" is really a handful of separate behaviors, and they fail independently. An agent can be perfectly grounded and still be slow. It can be helpful and still occasionally toxic. It can nail the answer and quietly cost three times as much as it should to get there. 

So instead of chasing one blended accuracy score that averages all of that away, it helps to pick the few behaviors that actually matter for your agent and give each its own measurement. Groundedness. Fulfillment. Toxicity. Latency. Cost. Each becomes a number in its own right, and each can get its own budget.

You can calibrate the judge to score  based on your desired behavior. Sometimes a plain pass or fail is enough. Other times a rating is more informative, and that's perfectly fine. For example, if you score groundedness on a one-to-five scale, just draw a line to turn it into a target: say anything four and above counts as a pass. Either way, what you end up with is a rate you can hold a target against—the fraction of conversations that cleared the bar.

![A Grafana dashboard measures executions, pass rate, fails, evaluators, judge cost, and pass rate by evaluator](https://grafana.com/mw/_next/image/?url=https%3A%2F%2Fa-us.storyblok.com%2Ff%2F1022730%2F1999x1032%2F47ab28919a%2Fslo-for-agents-pass-rate.png%2Fm%2Ffilters%3Aformat(webp)%3Aquality(90)%2F&w=3840&q=75)

The point is that behavior, the thing that felt too fuzzy to pin down, is now a metric. You've made agent quality measurable, and the moment you do, it's finally in view and ready to act on.

And getting there in Grafana Cloud can start with a simple ask: have [Grafana Assistant](https://grafana.com/products/cloud/ai-assistant/?pg=what-if-your-agent-s-hallucinations-had-a-budget-how-to-start-using-slos-for-agent-behavior&plcmt=in-text) create an evaluation for a behavior you care about.

![In Grafana Assistant, a user asks to to create an online evaluation for an e-commerce agent for hallucinations. The AI then identifies the evaluator and outlines the next steps](https://grafana.com/mw/_next/image/?url=https%3A%2F%2Fa-us.storyblok.com%2Ff%2F1022730%2F1999x1456%2Fe071bb1470%2Fslo-for-agents-create-eval.png%2Fm%2Ffilters%3Aformat(webp)%3Aquality(90)%2F&w=3840&q=75)

As it runs on real conversations, you'll start to see how often your agent clears the bar.

![Blog image](https://grafana.com/mw/_next/image/?url=https%3A%2F%2Fa-us.storyblok.com%2Ff%2F1022730%2F1999x1455%2F7f1df859b4%2Fslo-for-agents-eval-questions.png%2Fm%2Ffilters%3Aformat(webp)%3Aquality(90)%2F&w=3840&q=75)

From there, Assistant creates and enables evaluation rules that are specific to each agent.

![Assistant shows its work as it summarizes the evaluators that have been created and enabled](https://grafana.com/mw/_next/image/?url=https%3A%2F%2Fa-us.storyblok.com%2Ff%2F1022730%2F1999x1448%2Ff12ad84dd2%2Fslo-for-agents-eval-rules.png%2Fm%2Ffilters%3Aformat(webp)%3Aquality(90)%2F&w=3840&q=75)

## **A number alone isn't enough**

Here's the part where observability experience pays off, because we've seen this trap before. 

A quality score sitting alone on a dashboard leads to a predictable problem. Maybe you start reacting to every little dip, or you cry wolf a few too many times. Before you know it, everyone quietly learns to ignore the graph. We've all got that Slack channel full of warnings nobody reads. A shiny new agent metric can easily become another one.

What the number is missing is a decision. That's exactly what a service level objective, or SLO, adds.

The idea is simpler than the acronym. You take your measurement and you commit to a target for it. In this case, let's say you want to measure the fraction of conversations a judge marks as fulfilled, so you set it at 95% fulfilled over 30 days. The interesting part is what's left over. If you're aiming for 95%, the other 5% isn't a failure. It's a budget.

![A screenshot of SLI dashboards in an Agent Observability Evaluation - helpfulness SLO](https://grafana.com/mw/_next/image/?url=https%3A%2F%2Fa-us.storyblok.com%2Ff%2F1022730%2F1999x1176%2F269fad42b3%2Fslo-for-agents-helpfullness-slo.png%2Fm%2Ffilters%3Aformat(webp)%3Aquality(90)%2F&w=3840&q=75)

That small shift changes how the whole thing feels. Unreliability, up to a point, stops being something to stamp out and becomes something to spend.

## **The budget is permission, not pressure**

The best part of this idea isn't math; it's permission.

When you have the remaining budget, the message is clear: go for it. Try the ambitious prompt, test the new model, or take the swing, because you planned for a little failure. When the budget runs low, it flips just as clearly: ease off the new features, quality needs some love. Red light, green light, except the light is your own data instead of a gut feeling in a meeting.

There's a lovely bit from an [episode of "Grafana's Big Tent" podcast](https://grafana.com/blog/service-level-objectives-how-slos-have-changed-the-business-of-observability/?pg=what-if-your-agent-s-hallucinations-had-a-budget-how-to-start-using-slos-for-agent-behavior&plcmt=in-text) where an SRE calls the error budget a fail-safe. Nobody thinks about it all day, he says, but it brings you back to reality when you mess up. That's the vibe we want on an agent team: not fear, not slamming the brakes the second a judge scores wobbles, just a quiet "it's OK, go build things," with a number that taps you on the shoulder when it's time to slow down.

And the budget cuts both ways. Before you ship a new prompt or model, you can replay it against conversations you already know and confirm it still lands inside your targets, so a change that quietly breaks one behavior never reaches users. Agents need that safety net more than most software, because the pressure to move fast is intense, and it's so tempting to just ship on vibes.

## **The quiet drift is the one to worry about**

Once you start thinking about budgets, your attention shifts. You stop fixating on the shape of any single graph and start watching how fast you're spending. That shift matters a lot for agents specifically.

A sharp spike from a rough afternoon of bad conversations is loud and tends to get noticed. And against a 30-day budget it might barely leave a mark, which is genuinely useful to know, because it saves you from panicking over something you'll survive.

The one to actually keep an eye on is the opposite: the slow, quiet burn. A tiny, steady decline where no single conversation looks alarming, but a little quality drains away each day. Maybe a prompt has slowly gone stale. Maybe a model upgrade was subtly worse for your use case. Maybe your users are gradually asking for different things. Agents are almost designed to hide this, because their answers stay fluent and plausible even when they're drifting, and no simple threshold will catch it. But a budget will, because it measures the accumulation rather than any one moment.

That's also why budget-based alerts are worth trusting. When they fire, something is usually really wrong, and it's worth looking at. In a world already tired of noisy alerts, that peace of mind counts for a lot.

## **But what target do you even pick?**

This is usually the next honest question: what number do you aim for? Is 85% fulfillment good? Is 95% unrealistic? It's genuinely harder than picking an uptime target because there's less gut feel for what's achievable with an agent.

You don't have to pluck it from the air. Once your evaluations have been running long enough to build up a useful sample, ask Assistant to recommend SLO targets based on their scores. In your own Grafana Cloud environment, that gives you a starting point grounded in how your agent actually behaves. You can then ask Assistant to create the SLOs, turning those measurements into targets and budgets.

![A screenshot of a settings page in Grafana for tracking the evaluation's pass rate against a target and alert on error-budget burn](https://grafana.com/mw/_next/image/?url=https%3A%2F%2Fa-us.storyblok.com%2Ff%2F1022730%2F1999x1037%2F8eb941c4a8%2Fslo-for-agents-what-happened-with-results.png%2Fm%2Ffilters%3Aformat(webp)%3Aquality(90)%2F&w=3840&q=75)

From there it's your call. Nudge the target up if you can afford to be stricter, or down if you need more room. A young agent racing into a new space might happily accept a coin-flip chance of missing its target, while an agent in front of paying customers might want only a 5% chance of a slip. The point is choosing with your eyes open.

## **We don't have to reinvent this part**

The striking thing, when you zoom out, is how little of this is actually new. Agent teams are facing a question reliability folks chewed on for years: how do you move fast, take real risks, and still keep people's trust? The answer was always to make what you care about measurable, pick a target, and treat the gap as a budget to spend. And that same answer travels surprisingly well to today. The only new piece is the measurement, and evaluations give us that.

So the pieces link up cleanly. Evaluations turn behavior into a number, the number gets a target, and the gap becomes a budget: permission to experiment, an early warning for regressions, and a shared language a PM and an on-call engineer can both speak. None of it asks you to invent a new philosophy of software, just to point out the one observability already given us at your agent.

So give your agent's behavior a number, give that number a budget, and then, inside that budget, build a little more freely. We'd genuinely love to hear how it goes.

## From behavior to budgets, with a little assistance

Everything we’ve described sounds useful, but it also sounds like work. Decide what behaviors matter. Create evaluations for them. Watch the results. Pick sensible targets. Turn those targets into SLOs.

As we’ve seen along the way, Assistant can help you put those pieces together. You can simply ask it to create evaluations for one of your agents, or all of them. Let those evaluations run for a while and build up a useful sample of real data. Then ask Assistant to recommend targets and create SLOs based on what it’s seeing.

You choose what matters for your agents, and Assistant helps with the setup. From your first evaluation to targets and budgets grounded in real conversations, you can get started just by asking.

Turns out, even your agents can use a little help from an agent.

*Miss out on ObservabilityCON 2026? Check out* *[our blog post recapping all the big announcements](https://grafana.com/blog/observabilitycon-2026-announcements/?pg=what-if-your-agent-s-hallucinations-had-a-budget-how-to-start-using-slos-for-agent-behavior&plcmt=in-text)**!*
