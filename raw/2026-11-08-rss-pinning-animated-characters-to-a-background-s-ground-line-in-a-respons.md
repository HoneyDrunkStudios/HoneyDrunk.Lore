---
source: "https://dev.to/vpstrial057_733ba46552745/pinning-animated-characters-to-a-backgrounds-ground-line-in-a-responsive-web-game-37m0"
title: "Pinning animated characters to a background's ground line in a responsive web game"
author: "VpsTrial057"
date_published: "2026-11-08"
date_clipped: "2026-11-08"
category: "Game Development / Unity"
source_type: "rss"
---

# Pinning animated characters to a background's ground line in a responsive web game

I build a small browser idle game, [OreSpark](https://orespark.com/?utm_source=devto&utm_medium=article&utm_campaign=os_devto), where miners walk around a painted mine scene and keep digging while you are away. The scene is a single illustration, and the characters are separate animated sprites on top of it.

The first version used flexbox to line the miners up in a row. It looked fine at one width and broke everywhere else: miners floated above the floor, stood on the wall, or sank into a cart. The problem is simple once you see it. **A flex row knows nothing about the picture behind it.** The floor in the illustration is not a straight line at a fixed pixel height, it is a shape painted into the image.

Here is the approach that fixed it.

## 1. Measure the ground on the image, not on the screen

Open the background at its native size and note, for each spot where a character should stand, the point under its feet. Store it as a fraction of the image, not in pixels:

```
// x, y = foot point as a fraction of the background image (0..1)
// s = scale, smaller for characters further back
const SPOTS = [
  { x: 0.18, y: 0.86, s: 1.00 }, // front left, near the cart
  { x: 0.47, y: 0.79, s: 0.85 }, // middle, on the rail level
  { x: 0.71, y: 0.73, s: 0.70 }, // back, near the tunnel
];
```

Because these are fractions of the image, they stay correct at any size, as long as the image itself keeps its proportions.

## 2. Keep the scene at the image's aspect ratio

The scene box must have exactly the same ratio as the illustration, otherwise the fractions point at the wrong place:

```
.scene {
  position: relative;
  width: 100%;
  aspect-ratio: 1600 / 900; /* the background's native size */
  background: url(mine.webp) center / 100% 100% no-repeat;
}
```

No `cover`, no cropping. If you crop the image on small screens, the ground moves and every spot is wrong.

## 3. Anchor each sprite by its feet

Position the sprite with `left` / `top` in percent, then shift it so the **bottom centre** of the sprite sits on the spot:

```
.miner {
  position: absolute;
  transform: translate(-50%, -100%) scale(var(--s));
  transform-origin: 50% 100%;
}
```

```
SPOTS.forEach((p, i) => {
  const el = scene.children[i];
  el.style.left = p.x * 100 + '%';
  el.style.top  = p.y * 100 + '%';
  el.style.setProperty('--s', p.s);
  el.style.zIndex = Math.round(p.y * 100); // lower on screen = closer = on top
});
```

Two details matter here:

- `transform-origin: 50% 100%` makes the scale grow up from the feet, so a smaller character in the back still touches the floor.
- `zIndex` from `y` gives you depth for free: characters lower on the screen are closer to the viewer and are drawn on top.

## 4. Size sprites relative to the scene

If the sprite has a fixed pixel width, it looks tiny on a wide screen and huge on a phone. Give it a width in percent of the scene instead, so the whole picture scales as one:

```
.miner { width: 9%; }
.miner img { width: 100%; height: auto; display: block; }
```

## 5. Animate inside, place outside

Walking, swinging a pickaxe or bobbing should be done on an inner element. The outer element only holds the position. That way an animation can never push the character off its ground point:

```
<div class="miner" style="left:18%;top:86%">
  <div class="miner__body"><img src="miner.webp" alt=""></div>
</div>
```

## Result

The same scene now works from a 360px phone to a wide desktop, and adding a character is just one more `{x, y, s}` line measured on the image. The rule that came out of it: **anything that stands on a picture should be positioned in the picture's coordinates.**

If you want to see the scene running, it is the home screen of [OreSpark](https://orespark.com/?utm_source=devto&utm_medium=article&utm_campaign=os_devto), a free play-to-earn idle mining game.
