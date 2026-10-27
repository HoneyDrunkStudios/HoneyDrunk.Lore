---
source: "https://dev.to/battleofpirates/how-i-added-english-to-my-solo-dev-unity-mmo-without-touching-130-ui-files-4gdj"
title: "How I added English to my solo-dev Unity MMO without touching 130 UI files"
author: "Battle"
date_published: "2026-10-26"
category: "Game Development / Unity"
source_type: "rss"
date_clipped: "2026-10-26"
---

# How I added English to my solo-dev Unity MMO without touching 130 UI files

My game, [Battle of Pirates](https://battleofpirates.com), is a free online pirate MMO for Windows: real-time naval PvP, fleets, fortress sieges, boss events. I build it alone in Turkey, so for two years every string in the game was hardcoded Turkish. Players here search for it as an *online korsan oyunu*, and that was fine until the game started showing up on itch.io and IndieDB and international players arrived.

The problem: about **1,700 unique UI strings across 130 C# files**, all built in code (`text.text = "AYARLAR"`), plus hundreds of server messages sent from Node.js. Wrapping every literal in a `T("...")` call would touch every file and risk breaking a live game.

## The trick: translate at the last moment, not at the source

Instead of changing the code that sets text, I translate the text *after* it is set and *before* it is drawn. A single `MonoBehaviour` runs late in `LateUpdate` (`[DefaultExecutionOrder(32000)]`), so it runs after all game code but before Unity renders the canvases:

```
foreach (Text t in texts) {
    string s = t.text;
    if (ReferenceEquals(seen[t.GetInstanceID()], s)) continue; // unchanged, skip
    string r = BopLoc.Translate(s);
    if (r != s) t.text = r;
}
```

Only Texts whose string reference changed are processed, so the per-frame cost is a reference comparison. When the language is Turkish, the component doesn't exist at all: zero risk for existing players.

## One dictionary file, two kinds of entries

Translations live in a plain tab-separated file in `Resources/`:

- **exact** entries: `AYARLAR → SETTINGS`
- **fragment** entries for strings built by concatenation: `"Seviye " → "Level "`, `" inci" → " pearls"`

Fragments are applied longest-first and only on word boundaries, so `" sa"` (hours) never breaks a word like `saldırı`. Rich-text tags such as `<color=...>` are skipped, and each segment between tags is translated on its own.

## Server messages for free

Because translation happens on the client at display time, the server needed no changes. A message like `"Kaptan23 artık arkadaşın!"` hits the fragment `" artık arkadaşın!" → " is now your friend!"` and shows as *Kaptan23 is now your friend!*

## Things I had to handle

- **Input fields:** skip the `textComponent` of every `InputField`, or you'd translate what the player is typing.
- **Switching back to Turkish live:** store the original string for every Text you changed, and restore it when the player switches back.
- **Trailing spaces:** they kept getting stripped from the dictionary file, so the loader copies the key's leading and trailing spaces onto the value.

## Result

About 1,670 dictionary entries, one new C# file, and a language toggle on the login screen. The English update shipped as a normal patch through the game's own launcher.

It's not a replacement for a real localization pipeline, but for a solo dev with a live game, it got a second language out in a day without a risky refactor.

If you want to see it running, Battle of Pirates is free on [battleofpirates.com](https://battleofpirates.com) and the [Microsoft Store](https://apps.microsoft.com/detail/9NL43LVCMVXX). Questions about the approach are welcome in the comments!
