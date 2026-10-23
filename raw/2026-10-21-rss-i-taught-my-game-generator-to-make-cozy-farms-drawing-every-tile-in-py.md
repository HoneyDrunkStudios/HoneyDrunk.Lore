---
source: "https://dev.to/lng_l_95dcf5de35ba45ef/i-taught-my-game-generator-to-make-cozy-farms-drawing-every-tile-in-python-heres-what-broke-ca0"
title: "I taught my game generator to make cozy farms, drawing every tile in Python. Here's what broke along the way"
author: "Lượng Lê"
date_published: "2026-10-21"
date_clipped: "2026-10-21"
category: "Game Development / Unity"
source_type: "rss"
---

# I taught my game generator to make cozy farms, drawing every tile in Python. Here's what broke along the way

[Spawn Point](https://github.com/leluong141996-dev/Spawn-Point) turns one sentence into a playable Godot 4 game. A small fine-tuned model writes the game design as JSON; plain Python and tested Godot components do everything else. This month I pointed it at one genre and tried to make it good: the cozy farm.

Type `spawnpoint create "nông trại mùa đông, trồng bắp cải, có cáo"` (a winter farm, cabbages, a fox) and you get this kind of thing:

[![A generated island farm: farmhouse, fenced field, animal pen, pond, woods](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Flp1zqpnt317rcir9lany.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Flp1zqpnt317rcir9lany.png)

There are no image files anywhere in that picture. Every tile, tree, chicken and cabbage is drawn by Python at build time. Here is how, and the parts that went wrong.

## 1. The ground is one picture, not tiles

My first instinct was a tileset with autotile rules. Instead, the whole map's ground is painted as one image:

- The level is a grid of characters (`.` grass, `:` path, `~` water).
- Each terrain type becomes a pixel mask, upscaled 16x and **blurred, then thresholded with a little noise**. That one trick gives rounded corners and bumpy, hand-drawn-looking edges for free.
- Outlines are just "pixels outside the mask that touch it", in a darker colour.
- A cliff is "water pixels within 6 px below land". Islands get a brown cliff on their south side automatically.

Tufts, flowers, lily pads and reeds are sprinkled per cell with a seeded RNG, so the same farm always looks the same.

The same code paints four seasons by swapping a colour table and the tree list:

[![The same farm in spring, autumn, winter and the desert](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F02vu1sigawa6pxmc37fr.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F02vu1sigawa6pxmc37fr.png)

And in motion, winter and the desert:

[![A winter farm in play](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Ftqaxt22xwswosjbxm049.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Ftqaxt22xwswosjbxm049.gif)

[![A desert farm in play](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fqcqqamjd60qq4i8tmu5h.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fqcqqamjd60qq4i8tmu5h.gif)

**What broke:** I used `scipy.ndimage` for the blur and the distance transform. It worked on my machine and failed in CI, because scipy was never a dependency. I rewrote it with numpy (a separable blur and erosion), and the numpy erosion gave the map a thin light frame, because it treated "outside the picture" as land. The fix was padding with `mode="edge"`.

## 2. Walking behind trees needs two small engine features

A top-down farm looks flat until the farmer can walk *behind* a tree. That needed:

- **Y-sorting**: entities lower on screen draw in front.
- **Footprints**: each object stands on the bottom of its drawing and only a small box at its feet collides. The collision used to be traced from the whole sprite, so a tree's crown blocked you.

Both became one-line options in the game graph (`"y_sort": true`, `"base": [22, 14]`).

[![The farmer feeding the hens and the cow, then collecting eggs and milk](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Feac5elfs6yq75ci6ape5.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Feac5elfs6yq75ci6ape5.gif)

## 3. A season, not a level

The farm became a season of a few days: 6:00 to 22:00, gold light in the evening, dark at night. You sleep in the farmhouse bed (or drop off in the fields), and overnight the crops you watered grow. Some days it rains and every crop stays watered; a winter farm gets snow instead. Seeds cost money, animals must be fed before they give eggs or milk, and a workbench sells tool upgrades.

[![Evening turns to night on the farm](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fm2a64osc8utgnztcfv96.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fm2a64osc8utgnztcfv96.gif)

[![Walking into the farmhouse](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fuzyj2tji2dpacuu36mio.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fuzyj2tji2dpacuu36mio.gif)

The farm also **saves itself** to `user://` (IndexedDB in the browser): the day, the money, every plot, the animals, which trees you chopped. Close the tab, come back, carry on. Two details that took a bug each:

- The GIF recorder and the playtest bots must never touch the save, or the next recording starts from wherever the last bot left off.
- `R` (restart) has to clear the save, or "restart" just reloads the same day.

## 4. The bug that made my farmer walk backwards

After recording the demo GIFs, someone pointed out the farmer was moonwalking: walking left while facing right.

The sprite flipping was fine. The **GIF autopilot** set every player's aim to "the nearest enemy", which is right for a shooter. On a farm, the nearest enemy was a crow, so the farmer kept facing the crow while walking away from it. A farmer with a sword had the same bug in real play, because sword aim followed the mouse. The fix was two lines: a farmer always faces where it walks.

Facing the right way now, and fishing from the pond's shore:

[![Fishing: cast, wait for the bite, reel in](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fn1v6wnchsycbv715qmle.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fn1v6wnchsycbv715qmle.gif)

## 5. The model kept ignoring the fox

The model got "a farm with crows that eat the crops" right. It missed pests mentioned in passing: "*có cáo*" ("there's a fox"), "*with a raccoon around*". I wrote a sealed set of 16 such prompts (before any training) and the released model got 12.

The first training patch fixed the fox, then put pests on *peaceful* farms and started ignoring named farmers ("a cat farmer" came back as "Farmer"). The cause was in my synthetic data: **every new example used the default farmer and almost all of them had pests.** The model learned exactly that.

The second patch used half named farmers, more explicit "no pests / peaceful" farms, and more replay of the previous patch. Results, fully-right prompts:

| set | v5.1 | v5.2 |
| --- | --- | --- |
| sealed: farm pests named in passing (16) | 75% | 100% |
| 30 real prompts (4-bit build you download) | 80% | 83% |
| sealed shooters (4-bit build) | 88% | 94% |

v5.2 is a prompt or two behind on two dev sets, which is within my run-to-run noise. After release, "nuôi gà và câu cá" ("raise chickens and fish") came back once with **Fish** as a pest, so the normalizer now drops farm animals and fish from a farm's pest list. Some fixes belong in code, not in the weights.

## 6. Testing on a phone without a phone

I checked the touch controls with headless Chrome at phone size. My first script dispatched synthetic `PointerEvent`s at the on-screen buttons, and nothing happened. The game was fine: the touch code calls `setPointerCapture()`, which throws for a pointer id the browser never saw. Real input through the DevTools protocol worked: the stick walked the farmer to the door and ACT went inside. The phone test did find one real problem: the seed buttons covered the middle of the screen. Seeds are now picked by tapping the hotbar.

## Try it

[![Working the field](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Faoxofbfgrgvfidvr8ryq.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Faoxofbfgrgvfidvr8ryq.gif)

```
pip install -U spawnpoint-studio
spawnpoint llm up      # serves the model (12 GB NVIDIA GPU + Docker, or Ollama)
spawnpoint create "a cozy autumn farm with pumpkins, watch out for crows"
```

Or play the demo farm in the browser, phone included: [leluong141996-dev.github.io/Spawn-Point](https://leluong141996-dev.github.io/Spawn-Point/).

- Repo: <https://github.com/leluong141996-dev/Spawn-Point>
- Model: <https://huggingface.co/smoky1496/SpawnPoint-Coder-7B-AWQ> / <https://huggingface.co/smoky1496/SpawnPoint-Coder-7B-GGUF>

If you've generated art procedurally, what was the trick that made it stop looking generated? For me it was blurring a mask and thresholding it with noise.
