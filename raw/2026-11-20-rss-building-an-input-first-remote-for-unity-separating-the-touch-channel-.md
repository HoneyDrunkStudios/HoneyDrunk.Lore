---
source: "https://dev.to/wabiplant/building-an-input-first-remote-for-unity-separating-the-touch-channel-from-the-video-channel-1pe"
title: "Building an input-first remote for Unity: separating the touch channel from the video channel"
author: "Wabiplant"
date_published: "2026-11-20"
date_clipped: "2026-11-20"
category: "Game Development / Unity"
source_type: "rss"
---

# Building an input-first remote for Unity: separating the touch channel from the video channel

Playtesting is where touch input goes to be humbled. A drag that feels perfect with a mouse falls apart under a real thumb; a tap target that's generous on a monitor turns out to be exactly finger-width wrong. So you test on the device — and if you develop in Unity, the standard way to do that without a build-deploy cycle is Unity Remote 5.

Unity Remote is a reasonable tool with two constraints that shaped everything in this article. On iOS it connects over USB only. And it always streams a compressed video of the game view back to the phone, with your input riding along the same pipeline. If what you actually need is *input* — which, in my workflow, was most of the time — you are tethered to a cable and paying latency for a picture of your own monitor.

HyperSonic Remote is the tool I built to remove those two constraints. It's an iOS app plus a free, open-source receiver package for Unity. This article is about the design decisions, the measurements, and the one bug that cost more time than the networking did.

## The core decision: input is the product, video is an option

Most remote tools are video tools that also carry input. HyperSonic inverts that. There are two completely separate channels:

- **Input channel:** UDP, small JSON packets. Touches are sent in normalized coordinates with a bottom-left origin, and touch phases use the same numeric values as `UnityEngine.TouchPhase`, so mapping them into Unity concepts on the receiving side is a cast, not a translation table.
- **Video channel:** TCP, length-prefixed JPEG frames. Three presets — Lightweight (480 px wide, 10 fps, quality 30), Standard (854 px, 20 fps, q55), and Clean (1280 px, 30 fps, q75).

The video stream can be turned **completely off**. Not "low quality" — off. In input-only mode, the only thing on the network is touch data. That single decision drives the latency characteristics of the whole tool, because it removes three costs at once: JPEG encode time on the Editor side, decode time on the phone, and bandwidth contention on the same Wi-Fi radio that your input packets need.

## Latency: measure it in the protocol, not in a spreadsheet

Latency claims about remote tools are usually vibes. I wanted a number the tool reports about itself, so the input protocol has a ping packet that the receiver echoes immediately. Round-trip time, halved, cross-checked against frame timestamps on the Unity side.

In my development environment (iPhone and Mac on the same Wi-Fi network, one router hop), one-way input latency in input-only mode measured **3.6–4.2 ms**. I'll be precise about the caveat: that's a quiet network, and your mileage will vary with your router and your RF environment. The more robust claim is the *delta*: turning the video stream on adds encode, decode, and contention, and you can feel all three in the input. If you're testing input, streaming video is pure overhead.

The app shows the measured latency, so anyone can reproduce the measurement on their own network rather than trusting mine.

## Discovery and connection: the boring parts that decide whether a tool gets used

A remote tool lives or dies on setup friction. The rules I set were: no scene setup, nothing to install on the PC beyond the package, and reconnects that happen on their own.

- The receiver starts listening automatically when you press Play. There's no prefab to place and no bootstrap scene.
- Discovery uses Bonjour service advertisement (`_hypersonic._udp` for input, `_hypersonic._v._tcp` for video), with a plain UDP broadcast discovery packet as a fallback for networks where Bonjour doesn't traverse.
- USB works without asking the user to run iproxy by hand: the Editor package includes a small usbmux relay that forwards the connection while Play is running. (On Windows this relies on the Apple Mobile Device Service; on Linux, on usbmuxd — both OS-level components, documented in the README.)

Installation is: Package Manager → "Add package from git URL" → Play. Unity 2022.3 or later, no dependencies.

## The bug that ate the schedule: touches that live and die inside one frame

Here's the problem I didn't anticipate. A fast tap on the phone can begin and end *between two Unity frames*. If the receiver models touch state as a snapshot — "here is the current state of each finger" — then a phase can be overwritten before Unity ever observes it. The `Began` of a tap, or its `Ended`, simply never exists on the Unity side.

The symptom is maddening: most input works, but UI clicks and interaction systems that wait for a complete press cycle silently never fire. It presents exactly like "the remote doesn't work with my UI framework."

The fix was to stop modeling state and start modeling **transitions**. The receiver keeps a per-finger phase queue: every phase change is queued in order, and `Began` and `Ended` are each guaranteed to be visible for at least one full frame. If you're building anything that forwards input across a process or network boundary — a remote, a replay system, a test harness — this is the lesson I'd underline: forward the event stream, not the snapshot.

## The wall: you cannot inject into `Input.touches`

One limitation deserves to be stated as plainly in the article as it is in the README. Unity does not expose any public API for feeding `Input.touches` or `Input.mousePosition` from outside. Unity Remote can do it because it's built into the engine; no third-party tool can.

So the package exposes its own list, `HyperSonicReceiver.Touches`, and projects merge it at their input entry point — a few lines where input is read. To reduce that friction, the package ships:

- a generic bridge for uGUI (`HyperSonicUGUIBridge`),
- a virtual touchscreen feeder for the Input System (`HyperSonicInputSystemFeeder`),
- a sample adapter for ORK Framework, which polls input in its own way and needed a dedicated path.

If you're designing a tool in this space, my honest advice is to budget more time for this integration surface than for the networking. The networking was the easy part.

## Pricing, stated plainly

Input is free, permanently — including input-only mode. The iOS app's Pro tier (monthly $2.99 / yearly $22.99 / one-time $59.99) removes ads and unlocks all video presets, and watching a rewarded ad gives 30 ad-free minutes if you'd rather not pay. The Unity receiver package is free and open source regardless of what you do in the app.

## Try it

- Receiver package (free, open source): <https://github.com/wabiplant/hypersonic-remote-for-unity-receiver>
- iOS app: <https://apps.apple.com/app/hypersonic-remote-for-unity/id6834049800>

If you try it, the two things I'd most like to hear about are the latency you measure on your own network, and which input framework you'd want an adapter for next.

*HyperSonic Remote is an independent tool by wabiplant and is not affiliated with or endorsed by Unity Technologies.*
