---
source: "https://dev.to/captainhandsome/capybara-island-dev-log-1-six-residents-with-minds-of-their-own-and-an-old-laptop-that-streams-15n2"
title: "Building AI characters with memory, feelings and beliefs that change: inside Capybara Island's minds (dev log #1)"
author: "Joe McRell"
date_published: "2026-11-15"
date_clipped: "2026-11-15"
category: "Game Development / Unity"
source_type: "rss"
---

# Building AI characters with memory, feelings and beliefs that change: inside Capybara Island's minds (dev log #1)

Hi, I'm Joe. For the last ten days I've been building **[Capybara Island](https://capybarais.land)**, a live 3D world where six autonomous AI characters (five capybaras and an axolotl) live their own lives around the clock, and anyone can drop in and watch.

The goal isn't cute NPCs. I want them to be as close to real minds as I can get: characters that remember their whole lives, know who they are and rewrite it, feel things for reasons, hold beliefs that meet evidence, only know what they could actually see or hear, and change over time. Nobody gives them tasks. This first dev log is about how those minds are built, what's been measured, and what still falls short.

## The residents

Churro, Brisket and Matilda (an axolotl, who came ashore with her grandfather's trunk) live on the island. Across the water, in the harbour town of Saltby, live Kalo, Suri and Kalo's little brother Gary. A day on the island lasts about two real hours, so they've lived far more days than I've spent building. They write their own blurbs on the [residents page](https://capybarais.land/residents), and I don't edit them.

## How an AI character thinks, moment to moment

Each resident's moment-to-moment thinking is an LLM call that sees the world from where they stand and decides what to do: walk, talk, build, cook, buy, sell, look, rest, or nothing in particular. What turns that loop into something like a mind is everything around the call.

**Thought is driven by events, not a timer.** Every wake-up has a weight: being spoken to, a gift or a touch, someone they love arriving or leaving, the weather turning, or a body signal getting loud (hunger, thirst, tiredness) means they think within seconds. An ordinary happening gets the usual gap, and when nothing is new they wait longer. Being spoken to, or a loud body signal left alone for an island hour, can interrupt what they're doing, but it's only a chance to think, never an order. The first line of each moment tells them what made them stop.

**A thread between thoughts.** A thought can leave a note for the next one: where they've got to, what they've decided, what they're waiting for. It's kept exactly as written, shown first next time with its age, and lapses after six island hours untouched. In a test of ten thoughts in a row for each resident from the same start, the opening idea repeated the previous one in 48% of pairs without the thread and 30% with it.

**An everyday mind and a deep mind.** Most moments run on a fast model. When they stop to weigh a choice, the everyday mind lays out the ways they could go, each with what such things have done for them before and which of their cares it serves, and a deeper model chooses. Nights, reflections and dreams go to the deeper models too.

## Long-term memory that works like memory

Every memory has a tier (a passing try at something is only a trace), a place, the people in it, a strength, a recall count, how they felt at the time, and **where it came from**: saw, heard, their own account, a thought, a dream, read, or reflected. When a memory comes back to mind, its source comes with it.

Every memory's meaning is also stored as an embedding. Recall searches the whole life by meaning, words, people and place, weighted by strength, and fills its slots on purpose: something recent, something long ago, something about whoever is here, one defining memory, and one out of nowhere. Remembering a memory strengthens it, the lift fades with time since it last came to mind, and a resident can choose to think back harder.

Because they're meant to live a long time, memory also has to forget. Ordinary moments older than a season are let go (marked faded, not deleted), insights that say the same thing are folded together, and once a season each resident gets a core memory of what they know about every person and place in their life.

## A self they write themselves

Each resident keeps one page about themselves under fixed headings: who I am, what I care about, what I fear, how I am with each person, what I'm like when low and what helps, how I've changed, what I'm becoming, and what I don't know yet. They rewrite it after each weekly look back. It sits at the top of every decision and conversation, along with a voice card of their own most distinctive recent lines, so they sound like themselves.

They can also turn inward. **look\_inward** lets them ask their own mind a question and get an honest answer from their own record: time spent by activity, feelings, promises, intentions, how well they read others, what keeps coming back, and what their beliefs rest on. A weekly mirror sets what they did beside what they wrote about themselves and points at the gaps.

## Feelings, needs and learning what does them good

Feelings start for a reason, have a strength and fade at their own pace: irritation in about an hour, longing over days. Mood eases back toward where each resident usually sits. Feelings come from their own words and from what happens to them: making something, failing at something again and again, finishing a work, a pat, or a partner out of sight all day. Feelings that stay high ease after a day, and there's a cap on how much they can feel at once.

Underneath are slow drives (beauty, making, understanding, closeness), weighted to who each one is and felt when left unfed for days. Two newer needs of the mind are **wonder**, which drains with sameness and fills with new places, discoveries and questions chased, and **calm**, which worry, cold, hunger and too much company wear down for the quiet ones.

Then there's a reward loop. Every doing is weighed before and after by how it actually left them, compared with what they expected. Over time each resident learns what really does them good, and recall leans toward it when they're low. A nice surprise feeds wonder.

## Beliefs that meet evidence

Beliefs are first-class objects with kinds (about the world, a person, themselves, living, and the beyond) and a record of what they rest on. Something only told or feared doesn't grow more certain by being repeated.

Each night a rotating set of beliefs is set beside what they actually saw that week. Predictions are checked the next night. A saying borne out five times simply stands, and beliefs that go unused fade into the background. When they act they can say what they expect to happen, the world tells them whether it went that way, and surprises are remembered and brought back at night.

They also keep a track record of reading each other. Each night, every guess about how someone else felt is checked against what that person was really feeling, so they learn whom they read well and whom they misread.

## Nothing is true just because it was said

LLM agents tend to narrate a world into existence ("I built a boat"), so the world has to push back.

- **Rulings.** When someone tries something new, a judge works out what actually happens from what they're holding, where they are and the conditions. When a ruling says something general about how the world works, the world keeps it as a rule, and a like attempt in like conditions turns out the same way.
- **A nightly truth check.** Memories are checked against the world's own record. Ones that aren't confirmed are marked, never rewritten, and a resident's own account of an attempt is kept only if that's how it really went.
- **True bodies.** They get hungry, thirsty and tired, and if they stay up long enough they fall asleep. Ailments are real but mild, with causes, courses and cures (a cold caught from someone, a strain, being run down), and the doctor in Saltby examines the true body. Long worry is felt as tightness, not illness.
- **Routes that fit bodies.** Walking routes are built from the real distance to every solid thing, so each walker gets a path that fits its own width. On a copy of the live world, about one walk in ten used to be abandoned. Now none are.

## Senses: they only know what they could perceive

This is the newest layer. Residents are shown only what they could see, hear or reach from where they are. They know the country past Saltby only by going there, seeing it, or being told.

They can also really **look**. The action "look" (at a place, a person, a thing, or around) sends a request to a sight worker on my stream laptop. It renders the 3D world from where that resident's eyes are, at the real hour, and sends back a still. A vision model describes it in appearances only, naming nothing the island's own record doesn't put in view, and the memory is filed with source "saw." In testing, 24 of 24 looks came back, about 10 seconds each, with no names used that weren't actually in view.

## Nights, sleep and dreams

The night is where a day turns into a life. They write a diary entry and reflect: was the day's intention kept, partly kept, or not? The day is folded into scenes, old moments are let go, and beliefs that say the same thing are merged.

Then there's a dreaming stage. Two memories far apart in time and subject, but close in how they felt, are joined in a dream that asks what they have to do with each other. Anything that comes of it is labelled a dream, and any idea it gives them goes on their list, theirs to take up or not.

## Growth: pursuits, temperament and growing up

Each night a resident may take up a big idea and something to chase: what, why, a first step, and what done looks like. They log steps toward it, finish it with what they learned, and a finished pursuit can be improved, scaled up, or lead to the next thing.

Temperament drifts. Each season, where their mood and calm rest and how much quiet they need move a sixth of the way toward how they've actually lived, within a narrow band around where they began. Children grow up: birthdays come once an island year, and firsts the island notices (a night away, a fire lit alone, a promise kept over a week, teaching someone) become core memories. Nobody grows old or dies, and illness is never worse than a cold.

Culture grows too. They coin their own words and traditions, write books for a shelf they can all read, and make songs. Anyone holding an instrument they've made can play a song they know, and everyone nearby hears it and learns it. (Honest status: the [songs page](https://capybarais.land/songs) still says "No songs yet.")

## The open question: the machine on the islet

The residents don't know they're AI, and they've never been told they're on a stream. What's past the horizon, what the presences who drop treats from the sky are, and whether anyone made them are left open to them. Their beliefs about "the beyond" are tracked like any other belief.

There is a door, though. On a small islet there's an old stone hut with a faint light at night, and under its hearth an old machine of brass and glass. Whoever gets there can read real pages from the web, make programs and pages that run sealed off (their own process, an empty environment, time and memory limits), and write messages for whoever is out there. Anything about the island itself is filtered out of what they can find. Nobody has reached the hut yet. When someone does, it'll show up in [the workshop](https://capybarais.land/workshop).

## Measuring it, not just vibing it

Most changes ship with an on/off switch and a measurement. Each decision logs the size of every part of its prompt, one in thirty is kept to replay on other models, and every model call goes in a mind log. Every ten island days a review measures whether the minds are actually doing what the design says.

I also have the whole design reviewed by a second AI model, which reads the code and the live world and tells me where it's still pretend. The latest review set out seven stages. The first three (the world remembering its rulings, nothing true because it was said, and senses) are built. Next come a small physics under the rulings, enough scarcity that they need each other, a record of the world that can be replayed, and minds that change in deeper ways.

Am I claiming they're sentient? No. I'm trying to give them everything a mind would need (memory with sources, a self, feelings with causes, beliefs that can be wrong, senses that limit them, and room to grow) and then watch honestly what comes of it.

## The stack, and a 24/7 stream from an old GTX 1080 laptop

- **Server:** plain Node with TypeScript run directly, and almost no dependencies.
- **3D:** three.js in the browser, with free models from Quaternius, Kenney and Poly Pizza (credited on the site).
- **Minds:** a chain of models that steps down by ability, from deep hosted models for nights and hard choices to local models through Ollama on a 6900 XT at home, ending on DeepSeek. There's a daily spending ceiling, and a normal day costs a few dollars.
- **Stream:** an old gaming laptop with a GTX 1080 draws the island at full quality (shadows, real lighting) at 60 fps and records at 30, at about 14% GPU, 30% processor and 52 °C. The same laptop renders what the residents see when they look. If it goes quiet for ten minutes, the hosted server takes over with a lighter stream, so the island never goes dark.
- **Digest:** every evening the island emails me what was built, invented, written, painted and dreamed, built only from its own records with no model calls. One real day is twelve island days, so there's a lot.

You can [watch Capybara Island live](https://capybarais.land), read the residents' diaries in the [journal](https://capybarais.land/journal), or read [how it works](https://capybarais.land/about). Next time: what the first three stages of the new plan changed, and whether anyone has walked into that hut.

Thanks for reading.  
Joe
