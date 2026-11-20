---
source: "https://dev.to/juegostudiosofficial/shipping-your-mobile-game-in-hindi-tamil-or-bengali-a-text-rendering-checklist-before-4019"
title: "Shipping Your Mobile Game in Hindi, Tamil or Bengali? A Text-Rendering Checklist Before Localisation Starts"
author: "Juego Studios"
date_published: "2026-11-19"
date_clipped: "2026-11-20"
category: "Game Development / Unity"
source_type: "rss"
---

# Shipping Your Mobile Game in Hindi, Tamil or Bengali? A Text-Rendering Checklist Before Localisation Starts

A lot of mobile teams in India plan a regional-language release the same way they would plan Spanish or German: export the strings, send them to translators, import them back, ship. Then QA opens the Hindi build and the conjuncts are broken, the vowel signs sit on the wrong letter, and half the button labels are clipped at the top.

Indic scripts are not "just another font". They need complex text shaping, and that is a property of your text pipeline, not of your translation vendor. Here is the checklist we run before a single string goes out for translation.

## 1. Confirm your text stack actually shapes Indic scripts

Devanagari, Bengali, Tamil, Telugu, Kannada and Malayalam all rely on OpenType shaping: consonant clusters combine into conjuncts (क + ् + ष becomes क्ष), and some vowel signs are drawn before the consonant they follow in memory (कि). A renderer that maps one code point to one glyph will produce text that native readers find broken, even if every character is technically there.

- **Godot 4** ships an advanced text server built on HarfBuzz, so shaping is available by default.
- **Unreal Engine** uses HarfBuzz for Slate/UMG text shaping.
- **Unity** depends on which UI system and version you are on. Older TextMeshPro setups are a common source of broken Indic text, and newer Unity versions have added shaping options. Check your exact version and UI system rather than assuming.

Do this check in week one with a test scene, not in the last sprint.

## 2. Build a "torture string" for each script

Ask a native speaker for a short list of words that exercise the hard cases: conjuncts, reph (र्), vowel signs above, below and before the consonant, and nukta characters. For Hindi, something like क्षत्रिय, प्रकाश, कृपया, ज़िंदगी and श्रृंखला is a decent start. Put these strings on every UI widget type you use: buttons, tooltips, dialogue boxes, notifications and the store-facing screenshots.

## 3. Pick fonts with proper script coverage and a clear licence

The Noto family (for example Noto Sans Devanagari, Noto Sans Bengali, Noto Sans Tamil) is widely used because it covers these scripts and is released under the SIL Open Font License. Whatever you choose, check:

- every script you plan to ship is covered, including the Latin fallback for numbers and brand names,
- the licence allows embedding in a commercial app,
- the font atlas or dynamic font setup includes the glyphs shaping actually produces (conjunct glyphs are separate glyphs, so a pre-baked atlas built from your string list can miss them).

## 4. Budget vertical space, not just horizontal space

Teams usually plan for text expansion in width. Indic scripts also need more height: marks above the headline and below the baseline get clipped by line heights tuned for Latin text. Leave extra line spacing and padding in your UI layouts, and avoid fixed-height text boxes for anything a translator will touch.

## 5. Decide on numbers, dates and Hinglish up front

- Indian number grouping uses lakh and crore (1,00,000 rather than 100,000). Decide whether your in-game currency and leaderboard numbers follow it.
- Decide whether numerals stay in Western digits or use native digits, and apply it consistently.
- Many Indian players are comfortable with Hinglish or English UI terms like "Level" or "Shop". Agree a glossary with your translators so the same term is not handled three different ways.

## 6. Test on the phones your players actually use

A lot of your regional-language audience will be on budget Android devices. Dynamic font atlases that grow at runtime, and multiple fallback fonts all cost memory. Profile text-heavy screens on low-end devices, not just your development phone.

## 7. Give QA a readability pass, not only a "strings present" pass

Linguistic QA should look at text in context: is it readable at the size the HUD uses, does it clip, does it wrap mid-cluster? We have a short list of [HUD readability checks](https://www.tumblr.com/juegostudiosofficial/833355253041758208/7-quick-checks-for-a-game-hud-that-players-can) that applies just as much to Hindi as to English.

---

Getting this right early means localisation becomes a content task instead of an engineering fire drill. If you are planning a regional-language release and want help with the UI and rendering side, our [mobile game development team](https://www.juegostudio.com/mobile-game-development-company) works on exactly this kind of problem.

*Written by the team at Juego Studios.*
