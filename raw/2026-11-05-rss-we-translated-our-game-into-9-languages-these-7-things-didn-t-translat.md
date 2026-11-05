---
source: "https://dev.to/giftclub/we-translated-our-game-into-9-languages-these-7-things-didnt-translate-1k5b"
title: "We translated our game into 9 languages. These 7 things didn't translate."
author: "Gift Club"
date_published: "2026-11-05"
date_clipped: "2026-11-05"
category: "Game Development / Unity"
source_type: "rss"
source_last_modified: "2026-11-05"
---

# We translated our game into 9 languages. These 7 things didn't translate.

Our small team's browser game now runs in English, Russian, Ukrainian, Spanish, Polish, Italian, Turkish, German and French. That's more than 8,500 strings per language.

I expected the volume to be the hard part. It wasn't. The hard part was finding out how many assumptions about language we'd built into our code.

Here are seven of them.

## 1. A placeholder can't take a suffix

In English, this is fine:

```
Someone got {{name}}'s gift first
```

Turkish has no separate word for "of". It adds a suffix to the name, and the suffix depends on the name's vowels:

```
Ahmet'in   Murat'ın   Ali'nin   Ömür'ün
```

Your string doesn't know the name, so it can't know the suffix. We stopped trying to pick one and reworded the sentence so the variable stands alone:

```
Hediyeyi biri önce aldı: {{name}}
```

That's roughly "Someone got the gift first: {{name}}".

If you need a suffix, put it on a fixed word next to the variable. "In {{name}}" became `{{name}} oyununda`, literally "in the {{name}} game", where the suffix sits on "game".

**Lesson:** never attach grammar directly to a variable.

## 2. The percent sign moves

```
const label = value + "%"; // works until it doesn't
```

| Language | Result |
| --- | --- |
| English | 30% |
| Turkish | %30 |
| German | 30 % |
| French | 30 % |

The sign leads in Turkish. In German and French there's a space before it, and it has to be a no-break space, or the `%` can wrap onto a line by itself.

`Intl` already knows this:

```
new Intl.NumberFormat("tr", { style: "percent" }).format(0.3); // "%30"
new Intl.NumberFormat("de", { style: "percent" }).format(0.3); // "30 %"
```

Check its output against what you want for each language, though. It gives "30 %" for Spanish and Russian too, for example.

## 3. French punctuation needs its own space

French puts a space before `!`, `?`, `:` and `;`. A normal space lets the punctuation wrap onto the next line, alone, which looks like a bug. So our French strings use a no-break space:

```
"levelUpTitle": "Niveau supérieur\u00a0!"
```

The catch is that a no-break space looks exactly like a normal one in most editors, so you won't catch this by reading the file.

## 4. "{{name}} invited you" has a gender problem

English verbs don't care who did the inviting. Russian past-tense verbs do, and your string doesn't know the player's gender. Each language got its own answer:

| Language | String | How it deals with gender |
| --- | --- | --- |
| Spanish | `{{name}} te invitó` | The verb has no gender here |
| Turkish | `{{name}} seni davet etti` | The language has no grammatical gender |
| Polish | `{{name}} cię zaprasza` | Present tense avoids it ("is inviting you") |
| Russian | `{{name}} пригласил(а) тебя` | Both forms in one word |

That `(а)` adds the feminine ending. It looks a little odd at first, but Russian-speaking users see it all the time in apps.

**Lesson:** rewording is often better than adding gender logic to your code.

## 5. A correct translation can still be wrong

Telegram's official Russian word for a story is «история». It's correct, and it's also the everyday word for "history".

So a button that means "Post a story" could read as something about history. We switched to «сторис», the word people actually use, even though it isn't the official one. It's a borrowed word that doesn't change its ending, which also makes it easy to drop into any sentence.

No linter would ever catch this. You only find it by reading the string where it appears and asking what a real person would think it means.

## 6. Tone needs a check, too

Most of these languages have a formal and an informal "you". We use the informal one everywhere, because it's a game and the formal one feels like a letter from a bank.

Translators, human or machine, drift back to the formal one, so we added a check that runs on every locale file edit and flags formal words:

```
FORMAL = {
    "es": re.compile(r"(?<!\w)usted(?!\w)", re.I),
    # ...one pattern per language
}
```

The same script reports any key that's missing from a language. Plurals can trip that up, because English only needs `_one` and `_other` while Russian and Polish also use `_few` and `_many`. A naive comparison reports false errors, so we strip the plural suffix before comparing keys:

```
jq -r '[paths(scalars) | join(".") | sub("_(zero|one|two|few|many|other)$"; "")]
       | unique | .[]' en.json
```

## 7. Long words don't fit

Every layout we had was tested in English first, and English is short.

"Tap a tile to dig" fits a button easily. The Russian version, «Нажми на клетку, чтобы копать», pushed the button off the screen and took the price with it:

[![Before: a long Russian label pushes a green button off the screen edge. After: a shorter label fits inside the button with its price.](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fyj0i13zmo1ueb3imnvo0.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fyj0i13zmo1ueb3imnvo0.png)

We didn't try to squeeze it in. We shortened the text to «Выбери клетку» ("Pick a tile") and made the label truncate before the price, so the part that matters always stays visible.

Our Match-3 score row broke in a sneakier way. In this narrow row, the score ran into the moves label, and the Russian clock, «44 с», wrapped onto two lines:

[![Before: the score overlaps the moves label and the clock wraps onto two lines. After: everything stays on one row and the moves label is shortened with an ellipsis.](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fudjql3igxncpp7ou9pfe.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fudjql3igxncpp7ou9pfe.png)

The fix was to decide what's allowed to shrink: the score and the clock keep their width and never wrap, and the moves label gives way first. It's not pretty at this width, but everything's still readable, and you can see the fix wasn't free.

**Lesson:** test on your smallest phone in your longest language, and decide up front which element gives way.

## What I'd tell myself before starting

- **Translate sentences, not fragments.** Almost every problem above gets worse when you glue strings together.
- **Let the variable stand alone.** Don't attach grammar or units to it in your code.
- **Write down your fixed terms and tone.** Otherwise every new batch of strings drifts.
- **Test your longest language on your smallest phone.** That's where layouts break first.
- **Automate what you can, then read the rest in context.** A script can find a missing key, but it can't tell you that a word means "history".

What's the worst translation bug you've ever shipped? I'd love to hear it, especially in a language I haven't run into yet.
