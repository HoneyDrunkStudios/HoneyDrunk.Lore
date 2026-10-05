---
"source": "https://dev.to/sam_novak_574b07811e18495/snapshot-testing-a-particle-effect-in-pixijs-8-what-has-to-stay-fixed-for-the-same-frame-twice-5efo"
"title": "Snapshot-testing a particle effect in PixiJS 8: what has to stay fixed for\
  \ the same frame twice"
"author": "Sam Novak"
"date_published": "2026-10-05"
"date_clipped": "2026-10-05"
"category": "Technical Art & Creator Tools"
"source_type": "rss"
---

# Snapshot-testing a particle effect in PixiJS 8: what has to stay fixed for the same frame twice

Particle effects are random on purpose, which makes them awkward to review. Two people look at the same pull request, see two different bursts, and can't tell whether anything changed.

NixieFX, the particle runtime I used here, says its simulation is deterministic: the same effect with the same seed replays the same way. I wanted to know exactly what "the same" requires in practice. So I stepped one effect to a fixed time under different conditions, captured the particle positions and the rendered pixels, and compared them.

Short version: the seed isn't enough on its own. You also have to fix the timestep.

*Note: I'm involved with the NixieFX project. The runs were done in a Claude Code session, and this post was drafted with AI and reviewed by hand. Every number and image below comes from those runs.*

##
[
](https://dev.to#setup)
Setup

-
`nixie-fx`

0.1.17,`pixi.js`

8.22.0, WebGL renderer - A Chromium 152 browser on macOS, one machine
- Canvas 320 × 240 (76,800 pixels), 1 effect unit = 60 px

The effect is a CLI-generated 2D effect, edited into a one-shot burst: 36 particles from a small circle, random speed 1 to 3 units/s, random lifetime 0.5 to 1.1 s, color and size over lifetime, additive blending.


```
npm install pixi.js nixie-fx
npx nixie-fx effect create --project ./vfx --name ember-burst --profile pixi-ui-2d
npx nixie-fx validate ./vfx
npx nixie-fx export ./vfx
```


`effect create`

expects a `vfx-editor.prj`

project file in the folder and errors without one. I wrote that small JSON file by hand.

##
[
](https://dev.to#the-snapshot-function)
The snapshot function

Stop Pixi's ticker so nothing advances on its own, then drive time yourself:


```
import { Application } from "pixi.js";
import { loadVfxExportBundle } from "nixie-fx/export";
import { PixiVfxRenderer, createPixiVfx2dProjection } from "nixie-fx/pixi";
const W = 320, H = 240;
const app = new Application();
await app.init({ width: W, height: H, background: "#15121a", antialias: true });
app.ticker.stop(); // tests drive time, not requestAnimationFrame
const projection = createPixiVfx2dProjection({
originX: W / 2, originY: H / 2 + 20, pixelsPerUnit: 60, yAxis: "up",
});
const base = "./vfx/out/vfx/";
const getJson = (p) => fetch(base + p).then((r) => r.json());
const manifest = await getJson("manifest.json");
const effectsByPath = {};
for (const { path } of manifest.effects) effectsByPath[path] = await getJson(path);
const bundle = loadVfxExportBundle(
{ manifest, effectsByPath },
{ requiredBackend: "pixi2d", requiredEffectIds: ["ember-burst"] },
);
const ember = bundle.effectsById.get("ember-burst");
async function snapshot({ seed, t, dt }) {
const vfx = new PixiVfxRenderer({ parent: app.stage, projection });
const fx = vfx.createEffect(ember, { position: [0, 0, 0], seed });
for (let elapsed = 0; elapsed < t - 1e-9; ) {
const step = Math.min(dt, t - elapsed);
vfx.update(step); // seconds, not milliseconds
elapsed += step;
}
// 1) Particle state: position, size and alpha of every live particle.
const state = fx.getParticleDebugQuads().map((q) => ({
x: +q.x.toFixed(2), y: +q.y.toFixed(2), w: +q.width.toFixed(2), a: +q.alpha.toFixed(3),
}));
// 2) Pixels: read the canvas in the same task as render(),
// before the WebGL drawing buffer is cleared.
app.renderer.render(app.stage);
const c = document.createElement("canvas");
c.width = W; c.height = H;
const ctx = c.getContext("2d");
ctx.drawImage(app.canvas, 0, 0);
const pixels = ctx.getImageData(0, 0, W, H).data;
vfx.destroy();
return { state, stateHash: await sha256(JSON.stringify(state)), pixelHash: await sha256(pixels) };
}
async function sha256(data) {
const bytes = typeof data === "string" ? new TextEncoder().encode(data) : data;
const d = await crypto.subtle.digest("SHA-256", bytes);
return [...new Uint8Array(d)].map((b) => b.toString(16).padStart(2, "0")).join("");
}
```


`getParticleDebugQuads()`

is the useful part. It returns the screen-space quad for every live particle, so you can compare the simulation without reading back a single pixel.

##
[
](https://dev.to#what-i-compared)
What I compared

Baseline: seed 7, stepped to t = 0.35 s in steps of 1/60 s. Every other run changed one thing.

| Run (vs. baseline) | Particle state | Pixels changed | Max position drift |
|---|---|---|---|
| Same seed, same step, again | identical | 0 | 0 px |
| Same, reusing one renderer for two effects in a row | identical | 0 | 0 px |
| Seed 8 instead of 7 | different | 2,772 | 104.35 px |
| Step 1/30 s instead of 1/60 | different | 1,915 | 3 px |
| Step 1/120 s instead of 1/60 | different | 1,686 | 1.5 px |
| One 0.35 s step | different | 1,584 | 59.93 px |

All runs had 36 live particles at 0.35 s.

Same seed and same step gave byte-identical pixels, which makes this usable as a test. A different seed gives a visibly different burst, as it should.

The step size is the catch. Changing only the step from 1/60 to 1/30 moved particles by up to 3 px. You can't see that by eye, but every particle's pixels changed, so a pixel hash fails. Doing it in one big step moved some particles by almost 60 px.

That matters because the usual game loop passes `ticker.deltaMS / 1000`

, which varies frame to frame. That's correct for playing the effect, and it means a live frame won't match a stored baseline. Tests need their own fixed-step loop like the one above.

Checking more than one time point is cheap and catches different bugs. At 0.70 s only 20 of the 36 particles were still alive, so a lifetime change shows up there even if the 0.35 s frame looks fine.

##
[
](https://dev.to#turning-it-into-a-test)
Turning it into a test

- Make the seed injectable. In the game, a random seed per trigger keeps every burst different. In tests, pass a constant.
- Store the particle state JSON (or its hash) for two or three time points next to the effect file.
- In the test page, re-run
`snapshot()`

with the same seed, step and times, and compare against the stored state. - When the effect is meant to change, regenerate the baseline in the same commit, so the diff shows up in review.

I'd make the state JSON the main check and keep the pixel hash as a second, stricter one. The state comes from the simulation. The pixels also depend on the GPU and browser.

##
[
](https://dev.to#one-thing-that-surprised-me)
One thing that surprised me

My first version of this effect also set gravity and drag. Its runs came out with exactly the same hashes as a copy with both set to zero. Looking at the runtime source, gravity is only sampled when the emitter's velocity module is enabled, and I had left that module off. The values were in the effect file and validation passed with no warnings, but the simulation ignored them. A snapshot test with a known baseline catches that kind of quiet no-op. Looking at the effect doesn't.

##
[
](https://dev.to#limits)
Limits

-
**One machine, one browser.**I didn't compare across GPUs, operating systems or browsers. Pixel hashes may not match across them; I'd expect the particle-state JSON to travel better, but I haven't verified that. -
**Rounding.**I rounded state to 0.01 px and alpha to 0.001. Tighter rounding makes the test stricter and more fragile. -
**2D backend only.**Everything here ran through the PixiJS adapter. The validator also flagged that`depthTest`

and`depthInk`

export as 2.5D draw-order rules on Pixi, not a real depth buffer, so don't expect depth-sorting settings to behave like they do in 3D. Per the docs, lit shading and mesh-surface emission aren't supported on the Pixi backend either. -
**Needs a browser.**The test page loads Pixi and renders through WebGL. Running it in CI means a headless browser; I didn't set that up for this post.

Most Nixie FX + Pixi JS demos show an effect playing. This one is about pinning it down. The loading code and the per-frame `update()`

call are the same ones the [NixieFX PixiJS particle effects tutorial](https://nixiefx.com/pixijs-particle-effects/) walks through. The difference is who controls time.
