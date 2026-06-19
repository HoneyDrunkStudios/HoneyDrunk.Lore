---
source: "https://www.indiehackers.com/post/i-rebuilt-the-same-saas-plumbing-four-times-so-i-built-the-thing-i-wish-existed-45a36ac78d"
title: "I rebuilt the same SaaS plumbing four times. So I built the thing I wish existed."
author: "unknown"
date_published: "2026-06-10"
date_clipped: "2026-06-19"
category: "Solo Dev / Indie SaaS"
source_type: "web"
---
# I rebuilt the same SaaS plumbing four times. So I built the thing I wish existed.

This isn't a "how I hit $1M ARR" post. I'm early — the product is young, the revenue is small, and I'd be lying if I dressed it up as anything else. But I've spent the last stretch building something I think a lot of people here will recognize the need for, and I wanted to write the honest version of the story while it's still early enough to be honest about.

The thing I kept doing:

I build small SaaS products. Across four of them, I noticed I was doing the exact same thing every single time before I ever got to the part that was actually my idea.

Auth. Then billing. Then multi-tenant workspaces. Then roles and permissions. Then notifications, then the email setup, then usage metering. Weeks, every time, on the layer that no user has ever signed up for. By the fourth product I wasn't learning anything anymore — I was retyping the same Stripe webhook handlers and session logic, slightly worse than the time before, while the part I was actually excited about sat untouched.

The realization that stuck with me: when one of those products didn't work out, the idea was never the expensive part. Ideas are free. What I'd actually burned was the weeks of plumbing I built for users who never showed up. The plumbing is never the variable you're testing — but it's the thing that eats your runway before you're allowed to find out if the idea was any good.

So I stopped, and decided to build that layer once, properly, as something reusable. That's BuildBase.

How it gets built:

It's one React/Next.js SDK that hands you the operational layer of a SaaS — auth, multi-tenant workspaces, RBAC, billing, notifications, feature flags, workflows — so the only thing you build is the part that's actually your product.

The backend is Node, Mongo with a database-per-organization for tenant isolation, Redis and BullMQ for the queues. The server SDK is framework-agnostic, so it drops into Express, Hono, or a NestJS backend, not just Next.js.

The proof that it works isn't a logo wall, because I don't have one. It's that the same SDK runs all four of my own paid products in production. If it breaks, my own revenue breaks first. That's the bar — if it's not good enough for my products, it has no business being in yours.

The part I actually care about:

If there's one reason this exists beyond "I was tired of rebuilding auth," it's usage-based billing.

Charging a flat monthly subscription is a solved problem. Charging for usage — credits, tokens, generations, API calls — is not, and it's exactly the model most AI and modern SaaS products need now. The trap is that metering looks easy and enforcement is brutal: retries that double-charge, counters that drift under concurrent writes, quota resets that fire on the wrong cycle, overages that don't reconcile with Stripe. I know because I shipped those bugs myself and found them in production months later.

So BuildBase records usage idempotently (retries can't double-charge), enforces quotas server-side rather than as a button you can re-enable from devtools, and bills overages to your own Stripe. It's bring-your-own-Stripe — the money lives in an account you own, and I take no cut of your revenue.

That's the wedge: the piece most auth tools and templates leave you to build yourself.

Where it honestly stands:

This is the section most product posts skip, and it's the one I think matters most on a forum full of builders who can smell inflation.

It's young — version 1.0.x. It's React/Next.js only. It is not a five-minute drop-in; you wire a few backend endpoints, though the starter template does that for you. The server and billing layer have a real test suite, including security tests. There's no enterprise traction, no big numbers, no SOC 2 badge — and I'm not going to pretend otherwise, because the fastest way to lose this audience is to claim a maturity I haven't earned.

The roughest edge I'll own publicly: clean export and migration tooling isn't finished. If you adopt a tool like this, the way out has to be as clear as the way in, and that's the next thing I'm hardening. I'd rather tell you that than have you find out later.

What I'm learning about distribution:

Since the GTM side is mine, here's the honest version of what's actually moving the needle this early: not much that's flashy.

The thing I keep relearning is that with AI making the building trivial, the only real moat left is distribution — and most builders, me included, are far better at the first thing than the second. What's worked isn't link-drops or growth hacks. It's being genuinely useful in the communities where the people with this exact pain already hang out, for weeks, before ever mentioning the product. Leading with the problem, not the pitch. Talking about the cost of rebuilding the plumbing, because that's a thing people feel and share, where "check out my SDK" gets scrolled past.

It's slow and unsexy. No skyrocket. Just compounding. But the conversations it's started — strangers articulating the billing pain back to me in their own words — have been worth more than any launch spike, because they tell me the wedge is real.

What's next:

Smoother onboarding. The migration tooling. Transparent pricing once I've actually modeled the cost to serve, instead of pulling a number out of the air. And continuing to harden the parts that need to hold up as more people build on it.

If you're building a SaaS on React/Next.js — especially something usage-based — I'd genuinely like your eyes on it, and more than that, I'd like to know where it's confusing or what you'd never use. That feedback is what shapes what I fix next.

And if you're earlier than me and staring down three weeks of auth and billing before you can test your idea: don't pour that time in before you know the idea has legs. Whatever you use to skip it — mine or anything else — the plumbing was never the thing you were testing.

Trending on Indie Hackers

I got my first $159 in sales after realizing I was building in silence
I spent more time setting up cold email than actually selling. Here is what fixed it.
Three Days Before Launch, I Let My Own Tool Tear Me Apart
I got tired of rewriting the same content for 9 different platforms. So I built Repostify.
I thought I was building a news visualization tool. Users thought it was a catch-up tool.
A pattern I keep seeing in EdTech: traffic isn't usually the problem.
