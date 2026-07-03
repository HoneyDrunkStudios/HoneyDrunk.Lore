---
source: "https://devblogs.microsoft.com/dotnet/skiasharp-4-0-stable/"
title: "SkiaSharp 4.0 is here: announcing the first stable release - .NET Blog"
author: ".NET Blog"
date_published: "2026-06-29"
date_clipped: "2026-07-03"
category: ".NET Ecosystem"
source_type: "web"
---

# SkiaSharp 4.0 is here: announcing the first stable release - .NET Blog

Source: https://devblogs.microsoft.com/dotnet/skiasharp-4-0-stable/

On Demand
Missed .NET Day on Agentic Modernization? Watch the coding demos and agentic workflow sessions on demand.
Watch now
Matthew Leibowitz
SkiaSharp has been the backbone of cross-platform 2D graphics in .NET for over a decade. It powers pixel-perfect text,
geometry, and image rendering across mobile, desktop, web, and server using the
open-source Skia engine
, and it sits under .NET MAUI, WebAssembly, WinUI 3, and
frameworks like
Uno Platform
. A few months ago we shipped SkiaSharp 4.0 Preview 1. Today we are
taking the next big step.
SkiaSharp 4.148.0 is now available. This is the first stable release of SkiaSharp v4.
Get SkiaSharp 4.148.0 on NuGet
Read the full
SkiaSharp 4.148.0 release notes
for every
detail, and explore the new
SkiaSharp website and interactive gallery
.
It rolls up all of the v4 preview work into one stable package you can ship with confidence. If you have been waiting
for v4 to settle before upgrading, this is the release to move to. And to celebrate, the .NET Foundation and Uno
Platform are hosting a half-day SkiaSharp event focused on what is new, what is improved, and how to get the most out of
v4.
What is in it
A better engine, for free.
The native Skia engine is current through milestone m148: years of upstream rendering,
codec, performance, and security work that benefits every app automatically, with no code changes. Sharper downscaled
images, automatic photo orientation, more accurate colors, and broad performance gains all come along for the ride.
New capabilities.
Full OpenType variable font axis control across SkiaSharp and HarfBuzzSharp, color font palettes
for emoji and icon fonts, and animated WebP encoding with
SKWebpEncoder
.
A cleaner, more correct API.
v4 completes a long migration: legacy APIs are retired and the surface is clean.
Underneath, the object lifecycle was reworked so native singletons are properly reference counted, quietly fixing a
whole class of use-after-free crashes that could occur when the garbage collector finalized managed wrappers during
in-flight native calls. The kind of fix you never see, which is the point.
Modernized underneath.
The test suite moved to xUnit v3, builds run on reproducible Docker images, device and
WebAssembly testing runs through DeviceRunners, and every bundled native dependency was updated with the latest security
fixes.
Both animations were drawn and encoded with SkiaSharp 4.148.0 itself: variable-font axes and color-font palettes
rendered to frames, then written as animated WebP.
See the source
.
Faster where it counts
A newer engine should not just do more, it should do it faster. In our initial testing on the hardware-accelerated GPU
backend, the work that dominates modern app UIs (elevated cards, drop shadows, and layered surfaces) renders up to
24%
faster
on v4 than on the previous stable release, with no regressions anywhere else.
Comparing the last stable release (3.119) against v4 over OpenGL, a busy dashboard of shadowed cards rose from 65 to 80
FPS, and a scrolling activity feed from 47 to 58 FPS, both about 24% faster in our initial testing. Scenes that do not
lean on shadows, like charts, text, and vector maps, were already efficient and carry over unchanged, so you get the
upside with no downside. As a bonus, procedural Perlin-noise shaders run about 6 times faster on the CPU, a nice win for
generative textures and effects.
Initial testing on Windows 11 and .NET 10 over OpenGL. Absolute frame rates vary by GPU and driver.
Built a little differently
SkiaSharp wraps an enormous Google C++ codebase, and a lot of the work that used to be manual toil is now driven by
agentic workflows: syncing upstream Skia milestones, auditing for upstream CVEs, generating release notes and API diffs,
and keeping the docs current. The point is not the automation for its own sake. It is that the human time now goes to
API design and correctness, which is exactly where it should be, and it is a big part of how the project keeps pace with
Chrome’s release train.
Keeping pace with Skia, together
Going forward, SkiaSharp has a stronger commitment to staying in lock step with upstream Skia milestones. This has been
one of the most consistent pieces of feedback from the community and from Microsoft internal teams: developers need a
more predictable way to understand which SkiaSharp versions are current, how they map to Skia, and how fixes reach them.
Thanks to the co-maintenance partnership between the .NET team and Uno Platform, SkiaSharp now ships on a regular
cadence in two channels that follow upstream Skia milestones. The Stable channel corresponds to the Skia milestones in
Chrome’s Stable and Extended Stable channels, while the Preview channel corresponds to the milestone in Chrome’s Beta
channel. If you build on SkiaSharp, you can plan around it with more confidence.
The next preview is already here.
SkiaSharp 4.150.0 Preview 2
is on NuGet now. Its
headline is Graphite, the next-generation Skia GPU backend contributed by Uno Platform, alongside new image and color
filter APIs, SkSL image filters, and more.
Thank you, Uno Platform
SkiaSharp 4 is the result of the .NET team and
Uno Platform
building it together. Uno builds
their rendering pipeline on SkiaSharp, which makes them one of the most active and invested contributors to the project,
and it shows. Working alongside the .NET team, their engineers contributed major pieces of this release and the next:
engine upgrades, the full variable font implementation, object-lifecycle and crash fixes, cross-platform binding
generator tooling that lowered the barrier for other contributors, the interactive WebAssembly gallery, and the upcoming
Graphite backend.
A faster-moving SkiaSharp makes Uno apps better, and a strong Uno community makes SkiaSharp better. Thank you to Ramez
Gerges, Elie Bariche, Sasha Krsmanovic, and everyone at Uno. We are excited to keep building together. You can read more
about
how Uno Platform contributed to SkiaSharp 4
on their blog.
Explore what is possible in the interactive
SkiaSharp gallery
, or try your own code
live in
SkiaFiddle, powered by Uno Platform
.
Tune in: the SkiaSharp live event
To celebrate the release, the .NET Foundation and Uno Platform are hosting a live event dedicated entirely to SkiaSharp,
with members of the .NET team. We will walk through everything in this release, show it off live, and talk about what is
ahead, including the co-maintenance model and the road to Graphite.
If you want the full story behind 4.0, this is where to get it.
📅 Date:
June 30, 11am to 3pm ET
📺 Where to watch:
Uno Platform on YouTube, X, and LinkedIn, and the .NET Foundation YouTube channel
🔗 Event details:
platform.uno/skiasharp
Come for the demos, stay for the deep dives. We will see you there.
Summary
SkiaSharp 4.148.0 is the first stable release of SkiaSharp v4: a current Skia engine, variable fonts, color palettes,
animated WebP, a cleaner and more correct API, and a predictable release cadence.
Try it on NuGet
, read the
release notes
, give us feedback at
github.com/mono/SkiaSharp
, and join us at the
SkiaSharp live event on June 30
. Happy SkiaSharp-ing.
Category
.NET
.NET MAUI
Topics
.NET
graphics
SkiaSharp
Uno Platform
Share
Author
Matthew Leibowitz
5
comments
Join the discussion.
Leave a comment
Cancel reply
Sign in
Sort by :
Newest
Newest
Popular
Oldest
Can I please ask if SkiaSharp 4 will run without problems on Blazor Server, Blazor WASM and Blazor Hybrid, and whether it can interoperate with Figma? Thank you.
Co-pilot says…
Blazor Model | SkiaSharp 4 Support | Notes |
Blazor WASM | ✔ Full support | Runs Skia in WebAssembly; great for canvas graphics
Blazor Server | ✔ Partial | Server‑side rendering only; not ideal for animation
Blazor Hybrid (MAUI) | ✔ Best support | Full native Skia GPU backend
Figma Interop | ✔ Indirect | SVG, PNG, Lottie, tokens
Why do you say SkiaSharp sits under WinUI3? Isn’t that DirectX and WIC all along (DirectComposition, Direct2D)
What’s the redistributable size please?
Awesome
Read next
June 29, 2026
Packaging and Package Identity for .NET apps with WinApp CLI on Windows
Zachary Teutsch
June 29, 2026
.NET 8 and .NET 9 will reach End of Support on November 10, 2026
Rahul Bhandari (MSFT)
Stay informed
Get notified when new posts are published.
Follow this blog
Are you sure you wish to delete this
comment?
