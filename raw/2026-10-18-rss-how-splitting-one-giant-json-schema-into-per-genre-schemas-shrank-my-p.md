---
source: "https://dev.to/lng_l_95dcf5de35ba45ef/how-splitting-one-giant-json-schema-into-per-genre-schemas-shrank-my-prompts-3x-and-stopped-a-7b-2p32"
title: "How splitting one giant JSON schema into per-genre schemas shrank my prompts 3x (and stopped a 7B model from planting wheat in platformers)"
author: "Lượng Lê"
date_published: "2026-10-17"
date_clipped: "2026-10-18"
category: "Game Development / Unity"
source_type: "rss"
---

# How splitting one giant JSON schema into per-genre schemas shrank my prompts 3x (and stopped a 7B model from planting wheat in platformers)

I'm building [Spawn Point](https://github.com/leluong141996-dev/Spawn-Point), an open-source 2D game generator. Instead of asking an LLM to write buggy GDScript or draw pixels, I fine-tuned a 7B model to output a game design as structured JSON. Plain Python and pre-tested Godot components then assemble that JSON into a playable game.

This is the story of the **v5 release**: one schema change that paid off more than any amount of training data, a brand-new genre, and a regression I knowingly shipped anyway.

[![Star Run, a side-scrolling shooter generated from a one-line prompt](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fsw0jt8xd3xx87l0lrxd7.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fsw0jt8xd3xx87l0lrxd7.gif)

## The Problem: One giant schema to rule them all

Up until v4, the model filled out a single monolithic schema called `GameBrief` with around 20 fields: `player`, `enemies`, `crops`, `towers`, `goal`, `hazards`, `length`, `feel`, `juice`...

For a platformer, half of those fields are meaningless. For a cozy farming game, `hazards` and `jump_tiles` make zero sense.

Here's the catch with **guided decoding**: it guarantees the output is *valid JSON* matching your schema, but it doesn't guarantee the output makes *sense*. My 7B model would happily design a hardcore platformer with `crops: ["Wheat"]`, or a tower defense game where the player has a `double_jump` ability. Both are 100% valid JSON. Both are completely broken game designs.

On top of that, the system prompt was massive because it had to explain every single field across every genre, plus include a full few-shot example turn.

## The Fix: A Discriminated Union

In v5, the model outputs `{"genre": "...", ...}` first, and the schema immediately branches so **only that genre's fields exist**:

```
class _Look(BaseModel):
    genre: str          # Declared first so it leads every JSON object
    title: str
    palette: Palette = "night"

class PlatformerW(_Look):
    genre: Literal["platformer"]
    player: PlatformerPlayer
    enemies: list[PlatformerEnemy]
    ...

class FarmW(_Look):
    genre: Literal["farm"]
    crops: list[str]
    enemies: list[FarmPest]   # A pest can only be a walker or chaser
    ...

_UNION = TypeAdapter(
    Annotated[Union[PlatformerW, FarmW, ...], Field(discriminator="genre")]
)
```

Getting this to work smoothly with guided decoding took three specific tricks:

1. **`genre` must come first in the token stream.** With guided decoding, once the model commits to the `"genre"` token, the grammar mask locks in and only allows fields valid for that specific class. Since Pydantic orders inherited fields first, I declared `genre: str` at the top of the base `_Look` class and let subclasses narrow it down with `Literal[...]`.
2. **Close every object and strip OpenAPI keywords.** Pydantic's `.model_json_schema()` emits an OpenAPI-specific `discriminator` keyword and leaves `additionalProperties` open by default. I added a post-processing step to strip `discriminator`, inject `additionalProperties: false` everywhere, and wrap the root in `{"type": "object"}` (since several inference servers require an object at the root).
3. **Treat the LLM output as a wire format.** My game assembler, session manager, and test suite still use the monolithic `GameBrief` internally. The new per-genre classes act strictly as a wire protocol, converting back and forth via `from_wire()` and `to_wire()`. This lets me iterate on what the LLM sees without refactoring the entire game engine.

### The Results

* **3x shorter prompts:** The system prompt is roughly a third of its old size: no more explaining a zoo of unrelated fields, and no more giant few-shot example turn.
* **50% smaller edit prompts:** The entity-edit prompt dropped from **4,182 to 2,075 characters** once I gave it a compact view of the entities.
* **No more mixed-up genres inside one design:** Platformers with wheat crops are gone, simply because they are no longer expressible in the grammar. (The model can still pick the wrong genre for an ambiguous prompt; it just can't mix fields from two of them.)
* **Native Vietnamese support:** Previously, I ran a translation step in front of the model. v5 drops it and reads Vietnamese prompts directly, trained alongside English.

## Bonus: Adding a new genre is now dirt cheap

The best part of per-genre schemas is how easy it is to expand the engine. To add a **side-scrolling space shooter** in v5, all I needed was one small Pydantic model, a few synthetic data builders, and the Godot components.

The new shooter genre includes:

* Four enemy archetypes (`drifter`, `weaver`, `diver`, `gunship`)
* Power-ups that add guns
* A three-layer parallax starfield
* Auto-firing weapons (making it super mobile-friendly)

My favorite piece of component reuse is the **boss fight**: it's just a standard wave spawner with `autostart = false` that triggers when the regular level spawner emits its `cleared` signal. No new component required.

👉 **You can play the generated games right in your browser here:** [Spawn Point Web Demo](https://leluong141996-dev.github.io/Spawn-Point/)

## The Honest Part: What got worse in v5

I evaluate the model by running hand-written prompts through the entire pipeline and grading the final game. A test only passes if the playable game matches everything requested in the prompt. (At temperature `0.4`, run-to-run variance is about 1–3 prompts per set, so I only care about swings larger than that.)

| Evaluation set | v4 | v5 (full precision) | v5 (4-bit AWQ) |
| --- | --- | --- | --- |
| **New capabilities** (16 sealed prompts: shooters + v4 fixes) | 56% | **88%** | **75%** |
| **Real-world prompts** (30 EN & VI human-written) | 87% | 80% | 77% |
| **Older sealed set** (12 prompts, first nine genres) | 67% | 58% | n/a |

On held-out synthetic examples with exactly one right answer, v5 gets 73% of briefs, 98% of tweaks and 100% of entity edits (v5 format only, so there is no v4 number to compare).

v4 couldn't be expected to know shooters, so the first row isn't a fair fight. The other two rows are real regressions.

### Why did the older sets dip?

In my final training patch for v5, I added examples to fix a bug where the model missed *implied* enemies ("a tank shooting monsters"). I over-corrected: when the prompt names the player only indirectly, v5 now often answers with the default "Hero". Some old prompts are also genuinely ambiguous now that shooters and farms exist ("a space shooter" can be side-scrolling).

I decided to ship v5 anyway, document the exact weakness in the model card, and fix it properly in a v5.1 patch. I'm a firm believer that a model card that honestly lists regressions is way more useful to developers than one that only cherry-picks wins.

## 5 Takeaways for Structured LLM Outputs

If you're building with small local models and constrained decoding, here's what I learned the hard way:

1. **Shrink the output space before adding data.** I spent a lot of time curating training data for v3 and v4. Making invalid state combinations unrepresentable in the schema achieved more in a single afternoon.
2. **Put your discriminator token first.** Verify that your JSON schema actually forces the model to pick the branch before generating payload fields.
3. **Decouple your LLM wire format from your app's internal state.** Let the LLM read and write compact, specialized schemas while your backend works with a stable canonical model.
4. **Patches skew the model, even with replay.** My last fine-tune mixed old rows back in and still over-corrected on one behavior. Re-run *all* your eval sets after every patch, not just the one you were fixing.
5. **Track and publish your regressions.** Future you (and your users) will thank you for the honesty.

## Try it out locally

If you have Python installed, you can spin up the local LLM and generate a playable Godot game in three commands:

```
pip install spawnpoint-studio

# Downloads and serves the model:
# Uses the 4-bit AWQ build on a 12GB+ NVIDIA GPU with Docker,
# or falls back automatically to the GGUF build via Ollama.
spawnpoint llm up

spawnpoint create "a side-scrolling space shooter with a boss"
```

### Links

* 💻 **GitHub Repo:** [leluong141996-dev/Spawn-Point](https://github.com/leluong141996-dev/Spawn-Point)
* 🤗 **Model (AWQ):** [smoky1496/SpawnPoint-Coder-7B-AWQ](https://huggingface.co/smoky1496/SpawnPoint-Coder-7B-AWQ)
* 🤗 **Model (GGUF for Ollama):** [smoky1496/SpawnPoint-Coder-7B-GGUF](https://huggingface.co/smoky1496/SpawnPoint-Coder-7B-GGUF)

---

**Question for the community:** If you've used guided decoding / structured outputs in production, did you go with one giant schema or break it down into smaller ones? What edge cases broke your setup? Let me know in the comments! 👇
