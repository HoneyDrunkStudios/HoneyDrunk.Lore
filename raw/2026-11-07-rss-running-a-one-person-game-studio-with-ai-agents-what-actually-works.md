---
"source": "https://dev.to/wabiplant/running-a-one-person-game-studio-with-ai-agents-what-actually-works-6jf"
"title": "Running a One-Person Game Studio With AI Agents: What Actually Works"
"author": "wabiplant"
"date_published": "2026-11-07"
"date_clipped": "2026-11-07"
"category": "Game Development / Unity"
"source_type": "rss"
---

# Running a One-Person Game Studio With AI Agents: What Actually Works

Source: https://dev.to/wabiplant/running-a-one-person-game-studio-with-ai-agents-what-actually-works-6jf

My "studio" is one person in Japan, a handful of shipped products, and an AI agent named Muse that works the operational side with me. The games include Samurai 100 Slash Lite (a Unity action RPG and still my most popular title), Acid Rogue Shooting (a Godot roguelite shooter with a two-player mode), a comedy quiz app, a chord-planning app, and a musician-matching web service — plus a beat-'em-up in development.

People imagine the interesting part is generating code or art. Honestly, the part that changed my life is dumber and better: the agent runs the *operations* — the repetitive, forgettable, absolutely essential work that used to eat my evenings. Here's what that looks like in practice, including the parts that don't work.

## The morning numbers

Every day, a scheduled job collects the previous day's figures: App Store Connect analytics, ad revenue from multiple networks, website search data. It merges them into a single private dashboard — downloads, impressions, revenue, review movement — so I start the day looking at one page instead of logging into five consoles.

The value isn't the charts. It's that anomalies surface without me hunting: a product whose impressions fell off a cliff, a revenue line that stopped reporting because a data source broke. The agent also runs small, bounded improvement loops on store pages — promotional text experiments it may apply on its own, while anything that changes a title or needs a new build waits for my approval. That boundary (automate the reversible, escalate the irreversible) is the rule that makes the whole arrangement safe to run unattended.

## The rejection detective story

My favorite example of agent work is an App Store rejection for Acid Rogue Shooting. The review said, in effect, "the tracking-permission dialog never appears." My first instinct was a timing bug — the dialog request firing too late or after the wrong screen.

The agent took the plugin apart instead. The ad plugin I was using turned out to have **no API for requesting tracking permission at all**. The dialog wasn't mistimed; it was structurally impossible — the code to show it could never have worked, no matter when it ran. That reframing changed the fix entirely: request permission in my own code before any ad initialization, and if the user declines, fall back to non-personalized ads. A resubmission on that basis moved the process forward, and I verified the refusal path myself on my phone: dialog appears, declining it skips the consent form, the game plays, a banner shows.

A human debugging that alone (me, at midnight) would have burned hours moving the request earlier and later. The agent's advantage wasn't speed — it was refusing to accept the framing of the problem until the structure underneath was checked.

## The unglamorous bulk work

A Unity project of mine had grown to nearly 45 GB — years of imported assets, most of them unreferenced. The agent inventoried everything, separated what the current build actually uses from what it doesn't, moved the unused material into an archive folder (never delete originals — that rule is absolute), and rebuilt the project's version control from scratch. The project came back at under 5 GB, loads faster, and — verified by actually playing it — still works, with the battle results flowing into the game's RPG framework as before.

This category of work is where agents quietly pay for themselves: inventory, cross-referencing, careful bulk moves, then proof that nothing broke.

## What doesn't work

Honesty section. Screen control is the big friction: when the agent operates the same computer I'm working on, our inputs collide — a window focus changes mid-task, a click lands in my document. Work that needs my machine's GUI goes best when I'm away from it, and some dialogs (a native file picker, for instance) are simply invisible to remote control, so file hand-offs are designed to avoid them — the agent leaves an instruction file at a known path instead of asking me to browse for attachments.

The agent also can't judge feel. It can prove a hitbox extends 10 pixels past the sword's visual tip; it cannot tell me whether the combo *feels* good. And its reports need discipline: left alone, it summarizes optimistically, so I require every report to separate "verified," "failed," and "not checked."

## The shape of the thing

One person plus an agent is not a big studio. It's a small studio with an extremely reliable operations department that never sleeps and occasionally needs its homework checked. The products get steadier, the store pages get tended, the metrics get read — and I get to spend my limited hours on the part only I can do: making the games worth playing.

---

Indie game developer in Japan. I build games like Samurai 100 Slash Lite and Acid Rogue Shooting, and write about developing with AI agents. Portfolio: <https://portfolio.wabiplant.workers.dev/>
