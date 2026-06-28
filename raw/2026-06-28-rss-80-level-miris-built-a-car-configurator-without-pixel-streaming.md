---
source: "https://80.lv/articles/miris-built-a-car-configurator-without-pixel-streaming-here-s-what-they-found/"
title: "Miris Built a Car Configurator Without Pixel Streaming"
author: "80 Level"
date_published: "2026-06-26"
date_clipped: "2026-06-28"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# Miris Built a Car Configurator Without Pixel Streaming

Source: https://80.lv/articles/miris-built-a-car-configurator-without-pixel-streaming-here-s-what-they-found/

The Miris Team 26 June 2026 Miris Built a Car Configurator Without Pixel Streaming: Here's What They Found # Interviews # Tech # VR # Rendering 
Miris built an interactive WebXR car configurator that streams HDR-grade material fidelity to desktop browsers, tablets, and headsets like Apple Vision Pro, all from a single 1.2GB source asset with no cloud GPU allocated per viewer. Here's how they did it and what it means for the future of interactive 3D.
A 1.2GB automotive source asset, streaming real-time with HDR reflections on paint. Accessible simultaneously across desktop browsers, tablets, and headsets like Apple Vision Pro. Same asset across all devices. No app install. No cloud GPU allocated per viewer. 
That is what the Miris team demonstrated with an internal WebXR car configurator built on the Miris spatial streaming platform . The goal was straightforward: find out if HDR-grade material fidelity, the kind that has historically required offline rendering or a dedicated cloud GPU per viewer, could reach the devices consumers actually have. Here’s what they learned. 
The Tradeoff the Industry Has Accepted for Years Every team shipping interactive 3D has had to answer the same question: high fidelity or broad reach? 
Pixel streaming delivers excellent visual quality. Cloud GPUs render the scene server-side, video is transmitted, and the result looks close to pre-rendered. The reason teams have invested in it is that it works. The reason it stalls at scale is that every concurrent user requires a dedicated GPU on the back end. Costs rise linearly with traffic. A successful launch becomes a budget event. For AR and VR endpoints, round-trip latency adds head-tracking lag that is difficult to engineer away. 
glTF-based web viewers eliminate the GPU dependency. They run on the user's local GPU, in any modern browser, with no server-side rendering at all. The cost ceiling disappears. What returns instead is a fidelity ceiling. To get a high-fidelity vehicle into a browser at acceptable load times, the asset has to be aggressively compressed. Paint reflections flatten. Material detail collapses, and surfaces disappear at delivery. 
Spatial streaming avoids these compromises. You can render on-device in real-time to remove the cost ceiling. And adaptive delivery from a source asset, calibrated to each device and network, brings fidelity that web mesh standards cannot reach. 
Why Materials Are the Hard Problem The visible quality of any automotive 3D experience comes down to how it handles paint. Automotive paint has a specular response that is one of the most demanding cases in real-time computer graphics. The way light moves across a hood. The way a reflection elongates as you walk around the car. These are the details a customer uses to evaluate whether a digital model is faithful to the real thing. 
HDR (high dynamic range) reflections are central to this. HDR is what lets a surface render bright highlights at their real brightness (for example, the sun on a hood, a streetlight blooming across a side panel) rather than flattened to a single ceiling value. For automotive paint, that response is what makes paint behave like paint and not like plastic. 
Delivering HDR-grade reflections to a head-mounted display through a WebXR-accessible streaming pipeline is the engineering lift in this build. Until now, this category of fidelity has only been achievable in contexts where reach wasn't the constraint: either you wait while an offline frame renders, or you provision a cloud GPU per viewer and accept the cost ceiling that comes with it. What changed is not the quality ceiling; offline rendering still wins on raw fidelity. What changed is where that fidelity can go: a head-mounted display, a tablet, a browser, rendering on-device in real time. 
What the Team Built The team purchased a 1.2GB 3D vehicle model from a major asset marketplace, conditioned it through the Miris platform , and built a WebXR configurator on top of it.  They designed this internal build to stress-test its streaming platform against one of the most demanding visual categories in commerce. 
The result is a fully interactive vehicle configurator that runs in any modern browser. You can swap paint colors, remove the roof and doors. You can navigate around both the exterior and interior. And the best part, the same experience (and same asset) runs on desktop browsers, tablets, mobile phones, and headsets. 72 configurable variations (paint colors crossed with door states) are streamable end-to-end, each a conditioned variant of the same source asset, served on demand based on user input. 
How this works: the Miris platform's upstream conditioning pass identifies which surfaces on the vehicle are reflective and how reflective they are, so reflection accuracy is preserved where it matters. The streaming pipeline allocates more detail to what is close to the viewer, less to what is farther away, and renders nothing for what is behind the viewer at all. Those decisions happen together in every frame, within the device's compute and thermal envelope. 
The image above is the source asset opened in Blender. That same file is what reaches every device. The asset is conditioned once through the Miris pipeline. From that point forward, adaptive streaming delivers as much of that source fidelity as each device and network can support. No per-platform rebuild. No per-device optimization pass. No format conversion. 
Why WebXR WebXR is the standards-based API that lets immersive experiences run in a browser, on any device that supports the spec, with no app install. No platform-specific build step. No app store review. No per-vendor SDK lock-in. The same WebXR runtime handles a desktop browser, a tablet, and a head-mounted display. 
Miris is OpenUSD -native at ingest, the open format professional tools already export. Anything that can be opened in Blender can be conditioned once and streamed through WebXR. On the roadmap: Unity support for native mobile and XR, with further engines to follow. 
The architecture mirrors how video delivery already works. Teams shipping video do not upload separate versions for desktop and mobile. They upload the highest-quality source file and the platform delivers the right experience to each viewer. Miris spatial streaming does this for 3D. 
Try It Whether you’re building an automotive configurator, a virtual showroom, or any cross-device experience where 3D is part of your pipeline, the Miris public beta is free and open. Bring your hardest asset. 
[Start for free → app.miris.com ] 
Subscribe to 80 Level Newsletters Latest news, hand-picked articles, and updates
Subscribe I consent to receive emails from 80 Level Privacy Policy Terms of use Keep reading
Learn more about Miris
3D Asset Streaming Platform Miris Launches Public Beta
Built for the Game & Digital Art Industry Get Our Media Kit Comments 0 Type your comment here Leave Comment Built for the Game & Digital Art Industry Get Our Media Kit
