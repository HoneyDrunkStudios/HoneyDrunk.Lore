---
source: "https://dev.to/twitched_6016c48959c7d53e/audio-reactive-ui-in-unity-ui-toolkit-fire-lasers-and-rain-that-follow-the-music-13d4"
title: "Audio-Reactive UI in Unity UI Toolkit: Fire, Lasers and Rain That Follow the Music"
author: "twitched"
date_published: "2026-10-23"
date_clipped: "2026-10-25"
category: "Game Development / Unity"
source_type: "rss"
---

# Audio-Reactive UI in Unity UI Toolkit: Fire, Lasers and Rain That Follow the Music

[![A music player switching songs: flames, then neon lasers, then rain re-theme the whole screen](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F6ek65sbvhsxw3w6l30h7.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F6ek65sbvhsxw3w6l30h7.gif)  
*Switching the track re-themes the whole screen in one tween.*

I wanted a music player screen where the whole room follows the song. It has three tracks, and each one is a different genre: metal brings fire, synthwave brings lasers and a neon grid, lo-fi brings rain on the glass. Loud passages make the fire roar and the rain pour, and every beat lands as a surge, a flash or a gust. You can grab the record and scratch it, and pausing freezes every effect mid-air.

It's built in Unity's UI Toolkit, the newer UI system that works like HTML and CSS (UXML for layout, USS for styles), and every animation is a tween (an animation from one value to another over time) from Cascade, a UI Toolkit tween library I make. You can play it in your browser here (click once for sound): <https://twitchedd.itch.io/cascade-audio-studio>

This is how it came together, including the parts that didn't work the first time.

### One tween changes the whole room

The starting point was an older version of the screen with a single look. For this one I redesigned it in  
Figma with three genres side by side. Each has its own colours, title font, corner shapes and spectrum style  
(spikes for metal, neon bars for synthwave, soft dots for lo-fi).

To avoid twenty animations landing at slightly different times, everything follows one `Value` tween from 0  
to 1. Every drawn part reads the same number on each frame and blends  
from the old genre to the new one: the glows, the spectrum ring, the waveform, the meters, the corner radii.  
Halfway through, the ring shrinks to nothing, switches shape and grows back.

```
morph = screen.Animate().Value(0f, 1f, seconds, Frame).Ease(Ease.InOutCubic);
```

Switching genre again mid-morph just cancels the old tween and starts from wherever the room is, so you can  
mash the next button and it never snaps.

### Building the weather

Each genre has its own effects, and every one of them is a looping tween. The motion itself is all tweens; only  
the music measurements update every frame.

**The fire took two tries.** The first flames were flat shapes, and when they overlapped they stacked like  
paper cutouts. The second version draws each flame as a soft gradient (white-hot at the base, orange in the  
body, red at the tip, fading out at the edges), so overlapping flames blend into one fire. It's set in three  
rows: tall dark-red flames behind the panels, an orange row in front, and a short white-hot row along the  
bottom. Each flame runs three loops of different lengths: one bends it, one stretches it, one flickers it.  
Because the lengths never line up, the fire never repeats.

```
Track(tongue.Animate().Value(start, start + Mathf.PI * 2f, R(0.9f, 1.8f), v => tongue.Phase = v).Loop(LoopMode.Restart));
Track(tongue.Animate().ScaleTo(R(1.06f, 1.2f), R(0.18f, 0.34f)).From(R(0.82f, 0.94f)).Loop(LoopMode.PingPong));
Track(tongue.Animate().Fade(R(0.65f, 0.85f), R(0.12f, 0.28f)).From(1f).Loop(LoopMode.PingPong));
```

**The rain was too quiet.** The first version was thin and faint, and against the dark background you could  
barely tell it was raining. Now there are two depths: about 120 thin, faint drops in the distance and 40  
brighter, thicker ones close to the glass that fall almost twice as fast. Each drop fades from an invisible  
tail to a bright head, so it reads as a falling streak, and small splash rings pop along the bottom where  
the rain lands.

The lasers are a ping-pong rotate, the grid floor is a looping `Value`, and the stars twinkle on fades.

### Connecting it to the music

The songs are real audio, so the room can react to what's actually playing. Each frame the app reads the  
spectrum, folds it into bands and draws the ring from them. Two signals come out of that:

* **Beats.** When the bass jumps well above its recent average, that's a beat. Each genre answers in its own
  way: the fire surges, the lasers flash, the rain gusts sideways and splashes.
* **Loudness.** A level that rises fast and falls slowly. Each genre scales its effects with it.

```
switch (genre)
{
    case 0: flames.style.scale = new Scale(new Vector3(1f, 0.35f + 0.95f * energy, 1f)); break; // the fire roars
    case 1: foreach (var beam in lasers) beam.Energy = 0.1f + 0.8f * energy; break;            // lasers brighten
    case 2: SetRainDensity(energy); break;                                                    // drizzle to downpour
}
```

A loud passage makes the fire roar up from the bottom edge, and a quiet one settles it into embers. The rain  
is my favourite: every drop has its own loudness threshold, so a quiet intro is a drizzle of distant drops,  
more join as the song builds, and the fast close streaks only come in on the loud parts.

The catch with two signals is that they can fight. If the beat and the loudness both write the fire's height,  
a beat lifts it and the loudness pulls it straight back down. So they get separate jobs: loudness sets the  
fire's height (its scale), and the beat surge is a quick `MoveY` that lands on top of it. For the rain, the gust is a `Nudge`, which is additive, so it pushes the rain sideways without  
fighting the loops that make it fall.

```
flames.Animate().MoveY(-22f, 0.07f).Ease(Ease.OutQuad).Then().MoveY(0f, 0.45f).Ease(Ease.OutCubic);
rainLayer.Animate().Nudge(-6f - 14f * energy, 0f, 0.4f);
```

### Controlling it live

[![Pausing the music freezes the flames, embers and rain mid-air](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fge9so55vfz2aww6zjmy7.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fge9so55vfz2aww6zjmy7.gif)

**Pause freezes the world.** I keep the handle of every effect loop. Pausing the music calls `Pause()` on all  
of them, so the flames, embers, lasers and rain stop exactly where they are, mid-air. Play carries on from  
that frame.

```
void PauseEffects()  { foreach (var t in fxTweens) t.Pause(); }
void ResumeEffects() { foreach (var t in fxTweens) t.Resume(); }
```

**The record behaves like a turntable.** My first spin was a looping rotation, and you could see it: every lap  
restarted, so the speed hiccuped slightly once per turn. I replaced it with a motor. The record has one speed,  
every frame turns it by that speed, and starting, braking and recovering after a scratch are all `Value`  
tweens on that one number. At full speed nothing is tweening, so the spin is perfectly steady. The music's  
pitch follows the speed, so the song slides up as the platter starts and down as it brakes, like real vinyl.

```
void SetMotor(float speed, float seconds, EaseFunction ease)
{
    motor?.Cancel();
    motor = vinyl.Animate().Value(spinSpeed, speed, seconds, v => spinSpeed = v).Ease(ease);
}

SetMotor(NormalSpin, 0.9f, Ease.InOutSine);   // play: spin up to 33⅓
SetMotor(0f, 1.4f, Ease.OutQuad);             // pause: the brake
```

[![A cursor scratches the spinning record back and forth, then lets it spin back up](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fknfw8qwam3c8jcz96iyl.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fknfw8qwam3c8jcz96iyl.gif)

**You can scratch it.** Grab the record and the music stops dead, like a hand on vinyl. Drag it and the sound  
follows your hand. Let go and it keeps the speed of your flick, then the motor eases it back to 33⅓.

The first version lagged behind the mouse, and it took a while to see why. I was reading the record's angle  
back from Unity's resolved style, which is one frame behind whatever you just wrote, so every drag step  
started from a stale angle. Now the angle lives in a variable and the record turns on the move event itself.  
I also moved the speed measurement to once per frame, so when your hand stops, the sound stops straight away  
instead of playing the last speed until the next mouse move.

**The rest is for poking at.** Drag the waveform to seek. Drag the mixer faders, and double-click one to spring  
it home with a little overshoot. Tap the reaction buttons fast and it builds a combo: bigger bursts, a  
springing x2, x3, x4, and the room answers harder each time.

### Getting it into a browser

Unity's web player has four limits that needed workarounds:

* It can't read the audio spectrum, so on the web the music is real but the ring and the beats follow a simulated signal at each song's tempo.
* It can't play sound backwards, so backwards scratches go silent.
* It doesn't run the mixer's filters, so only the LEVEL fader changes what you hear.
* It holds all audio until the first click, so the "song ended, play the next one" check only counts near the end of a song.

None of the animation code changed, because Cascade runs on UI Toolkit's own scheduler.

### Takeaways

* Reduce the music to two signals (beats and a loudness level) and let every effect read them. It keeps each effect's code tiny and makes adding a genre cheap.
* Give each signal its own property, so a beat kick lands on top of the loudness level instead of fighting it.
* Keep the handles of looping animations. Pausing them is what makes "freeze the world" a one-liner.
* When something lags behind the mouse by a frame, check whether you're reading back a value the engine resolves later.

### Try it

* Play it in the browser: <https://twitchedd.itch.io/cascade-audio-studio>
* The original devlog on itch: <https://twitchedd.itch.io/cascade-audio-studio/devlog/1711007/making-a-music-player-ui-that-plays-along-with-the-song>
* Cascade Lite, the free (MIT) tier; everything here except the springs and staggered bursts works with it: <https://assetstore.unity.com/packages/slug/394764>

The sample itself comes to Cascade in a future update.

What would you map to the music for a fourth genre?
