---
source: "https://unity.com/blog/hand-tracking-tools-for-unity-xr"
title: "Hand Tracking in Unity: XR Hand Capture & Simulation"
author: "unknown"
date_published: "2026-06-11"
date_clipped: "2026-07-04"
category: "Game Development / Unity"
source_type: "web"
---

# Hand Tracking in Unity: XR Hand Capture & Simulation

Source: https://unity.com/blog/hand-tracking-tools-for-unity-xr

# The Future of XR Is Hands-First — And Unity's Tools Are Ready

**Co-authors: **Isaac Seah (Principal Technical Product Manager), Alexandra Serralta (Senior Software Engineer), Ketki Jadhav (Staff Product Designer) and Dave Ruddell (Senior Manager, Software Engineering)

**Why Hands-First Is the Future of XR**

Hand tracking has been a supported input type in XR for several years, but most projects still treat it as secondary, added after the core experience is built around controllers. For a growing set of experiences, that priority no longer makes sense. Games built around gestures, physical manipulation, or direct object interaction are inherently better expressed through hands: more natural, more intuitive, and impossible to replicate with a controller.

Getting there has historically meant overcoming two key tooling challenges: building reliable custom hand gestures required significant scripting work, and iterating on hand interactions was difficult without a headset physically nearby. Two additions across Unity's XR packages address both of these directly. XR Hand Capture in the XR Hands package lets you record real hand poses on-device and import them into Unity as reusable gesture assets. Hands Simulation, added to the XR Interaction Simulator in XR Interaction (XRI) Toolkit, brings full hand tracking development experience to the Unity Editor so you can iterate without a headset.

This post covers how both features work, when to use them, and how to integrate them into an existing project.

**XR Hands Capture**

The [XR Hands package](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.8/manual/index.html) exposes joint data per frame via the XRHandSubsystem. Building a gesture on top of that data means defining a set of joint angle and finger shape conditions that, when satisfied simultaneously, constitute a recognized pose. For simple gestures like pinch and poke, the package ships with ready-to-use implementations. For anything custom, the previous approach required per-finger, finger-shape configuration and that meant iterating entirely on-device.

While foundational, that manual process was slow and less reliable compared to what’s now possible with XR Hands Capture. Precise gesture fidelity, which is critical for gameplay mechanics like signature poses, 3D object manipulation, or fine UI control, was hard to achieve when you were manually defining each finger shape by hand. These approximations resulted in solutions that were slow to produce, more fragile across different hand shapes, and lacked the natural, intuitive feeling essential for truly compelling hands-first experiences.

**How it works**

XR Hands Capture addresses this by recording the actual joint data produced by the XRHandSubsystem while you perform a pose on-device, then generating an XRHandShape asset from that recording. You're authoring gestures from ground truth rather than approximation, which means the resulting interactions hold better across hand sizes and movement variation, and feel the way they're supposed to feel.

**The workflow:**

- Import the HandCapture sample from the XR Hands package in Package Manager.
- Deploy and open the sample scene on your OpenXR device.
- Perform the pose you want to capture. The scene records live joint data from the XRHandSubsystem into an XRHandCaptureSequence.
- Import the recording into the Unity Editor using the XR Hand Capture inspector window (Window > XR > XR Hand Capture).
- Extract the XRHandShape asset — a serialized representation of the hand pose that can be referenced by any StaticHandGesture component or custom detection logic.
- Adjust tolerances if needed and re-record to refine.

Because both the XRHandCaptureSequence and XRHandShape are generated from real capture data, the gesture library you build reflects how hands actually move, making those interactions feel natural when a player uses them. It also means non-engineers can participate in gesture authoring: a designer or animator can record and iterate on poses directly on-device without touching code, which keeps the designers and animators — the people who care most about how an interaction feels — directly involved in shaping it.

**Hands Simulation in the XR Interaction Simulator**

The XR Interaction Simulator in [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.5/manual/index.html) lets developers run XR experiences inside the Unity Editor without a physical device, useful for early-stage iteration where putting on a headset every test cycle adds significant overhead. Until recently, it supported controller input only. Projects built around hand tracking had no equivalent, meaning hand interaction development was fundamentally headset-dependent. Now, alongside the standard built-in hand gestures like poking, pinching, and grabbing, you can also test your own custom gestures directly in the simulator, a feature you won't find anywhere else outside of Unity's XR tools.

**How to Get Started**

[Download the latest version of Unity (6.3 or newer)](https://unity.com/releases/unity-6) to begin, then add these features via the Unity Package Manager.

- XR Hands Capture ships as part of the XR Hands package (1.7 and newer). You can install or update to the latest version and import the `HandCapture` sample to get started. Full documentation and API reference are available in the
[XR Hands docs](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/manual/index.html). - Hands Simulation is available in the XR Interaction Simulator as part of the XR Interaction Toolkit package (3.5 and newer) and XR Hands (1.8 and newer). Install or update to the latest version and import the XRI Starter Assets sample. See the XRI docs for setup details.

For a broader starting point, the [XR Interaction Toolkit Examples](https://github.com/Unity-Technologies/XR-Interaction-Toolkit-Examples) includes reference scenes covering common hands-first interaction patterns. If you're looking for a community reference for XR Hands Capture specifically, Dilmer Valecillos has put together a [hands capture demo project](https://github.com/dilmerv/XRHandsCaptureDemo) worth checking out. Curious what developers are building with Unity XR? [Take a look](https://unity.com/solutions/xr).

**What's Next**

Ongoing work spans both packages. In XR Hands, active areas include pose data compliance with the OpenXR specification, Palm Pose extension support, input action mappings across pinch, poke, aim, and device poses, and poke interaction refinements. We're also expanding support for OpenXR extensions that expose whether hand data originates from bare-hand camera tracking or controller-driven estimation, relevant for games that want to adapt mechanics based on how a player is physically interacting. In XRI, we continue investing in the XR Interaction Simulator as a reliable proxy for on-device testing as hands-first use cases grow.

[Join us for a livestream](https://on.unity.com/XRHands_Livestream) on July 9 at 12 pm ET with a special guest from Meta to see XR Hand Capture and the XRI Simulator in action, with a live Q&A and a look at what's coming next.
