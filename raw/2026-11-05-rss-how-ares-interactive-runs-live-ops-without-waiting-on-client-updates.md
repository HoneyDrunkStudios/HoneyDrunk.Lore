---
source: "https://unity.com/blog/ares-interactive-live-service-games"
title: "How Ares Interactive runs live ops without waiting on client updates"
author: "Adam Axler (Unity)"
date_published: "2026-11-04"
date_clipped: "2026-11-05"
category: "Game Development / Unity"
source_type: "rss"
---

# How Ares Interactive runs live ops without waiting on client updates

Running a live game means building for constant change. Teams need to keep players engaged with new events, balance updates, offers, and content, while keeping performance and stability intact.

Ares Interactive runs two very different live games: [*Baseball Hits 26*](https://aresinteractive.com/games/baseballhits/), developed by its 7th Inning team, and *The [Walking Dead: Aftermath](https://aresinteractive.com/games/the-walking-dead-aftermath/)*, developed by its Swift Games studio. *Baseball Hits 26* stays closely tied to the real-world baseball calendar. *The Walking Dead: Aftermath* builds its live service around a roguelite foundation that can expand without disrupting the core loop.

We spoke with Andre Taube, studio head at 7th Inning, and Carsten Granig, managing director of Swift Games Germany. They told us how they structure live service systems, manage remote content and configuration, shorten iteration cycles, and keep mobile releases stable as both games continue to evolve.

![Baseball Hits 26](https://img.youtube.com/vi/dt7k6S9HTac/hqdefault.jpg)

### **Building live ops around data rather than client releases**

*Baseball Hits 26* was built to give baseball fans and gamers a quintessential baseball experience that’s easy to pick up anytime, anywhere, in short bursts or longer strategic play. That approachability sits alongside real-world baseball decisions, progression, live events, social clubs, and communication features. Keeping those systems current means treating the game as something that is always changing rather than something that simply shipped.

For example, if an MLBPA-licensed player performs particularly well in a game or series, the team can feature that player in live events within the following week.

“That level of relevance is made possible by our nimble, data-driven server updates and our live ops team’s ability to quickly slot in the right matchups,” says Taube.

The team built its own backend and live ops pipeline so it could change events, store sales, offers, rewards, and matchmaking tuning without waiting for a client release or server deployment.

At the foundation is a custom content-delivery and remote-configuration system with more than 50 configuration domains covering players, events, store items, reward boxes, battle passes, and other systems. The team manages changes through an admin panel. The system validates the changes before accepting them, and servers pick them up within seconds without a restart.

Everything is versioned and logged. The team can review or roll back to any prior state, and can stage changes against internal test accounts before promoting them to production.

Event scheduling sits on that same foundation. Events, tournaments, and limited-time sales have defined start and end windows. A segmentation engine handles targeting and powers A/B testing, so the team can trial new offers or event formats with a fraction of the audience before a wider rollout.

In practice, that lets the team run as many as four events in a single week, such as Prime Club and Tower Club events, each with its own bonus players and featured offers tied to it.

“Owning the whole stack pays off most when something goes wrong in the middle of an event,” Taube says. “The team can diagnose the issue, fix the config, compensate affected players, and push the [config] update to clients, all within minutes and all from one place.”

Simplify your content management with Addressables

[Learn more](https://unity.com/how-to/simplify-your-content-management-addressables#addressables-groups)

### **Keeping content delivery and mobile releases predictable**

The team uses [Addressables](https://docs.unity3d.com/6000.3/Documentation/Manual/com.unity.addressables.html) specifically for stadium bundles. One default stadium ships in the app, so first-time players don’t need an extra download. The team packages every other stadium as a bundle, uploaded to the team’s server and downloaded on demand when a player selects it.

The team stress-tests each stadium bundle on its lowest-end devices to ensure it stays within strict size and memory budgets. A shared common bundle holds assets reused across stadiums, so the same data isn’t duplicated in every download.

The same emphasis on predictability applies to iOS and Android releases. The team keeps platform-specific code to an absolute minimum, and both platforms share milestone and submission deadlines. The team creates and tests Android and iOS builds daily.

Because most content is data-driven, the live calendar doesn’t need to be tightly coupled to app store review timing.

The client is also designed around the assumption that every server call can fail.

“For live games specifically, treat every server call as unreliable by default,” Taube says. “Structure the client so a slow, dropped, or unresponsive server never breaks the player experience.”

That principle carries into device support. The team uses the [Device Simulator](https://docs.unity3d.com/6000.3/Documentation/Manual/device-simulator-introduction.html) to check UI coverage across the full range of screen sizes and resolutions it supports. The [Unity Profiler](https://docs.unity3d.com/6000.3/Documentation/Manual/Profiler.html) is used extensively to find performance hiccups during gameplay. The team also tests performance regressions on a wide range of physical Android and iOS devices, both with and without Wi-Fi.

For Taube, mobile teams should settle their device strategy early.

“Invest early in a strong architectural plan for device support, especially on Android, where fragmentation across hardware and OS versions is the real risk.”

### **Building The Walking Dead: Aftermath so live systems can evolve independently**

*Baseball Hits 26* is built to reflect a real-world sports calendar. *The Walking Dead: Aftermath* has a different live-service challenge: adding new ways to play without disrupting its underlying roguelite experience.

The action RPG roguelite places players in the world of *The Walking Dead*. They build teams of Survivors, including Rick Grimes, Daryl Dixon, and Michonne, and fight hordes of Walkers and other enemies in real-time combat. Between runs, players unlock Survivors and Gear, level them up, unlock skills, and build out their base.

“At its core, we wanted to create something that captures the constant danger and tough choices of *The Walking Dead* while delivering the replayability and progression you expect from a roguelite,” says Granig.

The live service builds on that foundation with challenges and constraints, plus social systems such as Alliances, cooperative events, and leaderboards.

“From a development standpoint, we built the game so those systems can evolve independently. That gives us the flexibility to continue expanding the live experience without disrupting the core roguelite loop.”

![The Walking Dead: Aftermath](https://img.youtube.com/vi/_w7bO1Yp3v8/hqdefault.jpg)

### **Making the tenth live feature as cheap to ship as the first**

Swift Games didn’t rebuild its live service foundation from scratch. It started from its previous live title, *Heroes vs Hordes*. Store, economy, authentication, analytics, remote configuration, and cloud-save systems came across as proven technology, while the new roguelite core was prototyped separately and then merged onto that foundation.

Anything expected to change weekly was designed to change without a client release. Designers author content and balance in spreadsheets and publish them as remote bundles, with each bundle stamped with the client versions it supports.

Save data is versioned with a migration chain, so a live update never orphans a long-time player. Time comes from the server rather than the device, because events and timed offers depend on it.

The tradeoff is that live features need to be designed not just to switch on, but to switch off safely.

“That is what keeps the tenth live feature about as cheap to ship as the first,” Granig says.

The game primarily uses [GameObjects](https://docs.unity3d.com/6000.3/Documentation/Manual/GameObjects.html) and [NVIDIA PhysX](https://docs.unity3d.com/6000.3/Documentation/Manual/PhysicsOverview.html). [Entities](https://docs.unity3d.com/6000.3/Documentation/Manual/com.unity.entities.html) and [Burst](https://docs.unity3d.com/6000.3/Documentation/Manual/com.unity.burst.html) are reserved for the A\* pathfinding system that moves enemies.

More important to live development is scoped dependency injection. The game has four nested contexts: root, save game, main screen, and gameplay. Each context is responsible for what it creates and for cleaning it up.

That means a live event can be structured as an installer plus a configuration file plugged into a context. When that context closes, its assets and subscriptions go with it.

The team also separates UI from logic. A shop or offer can exist as a plain C# class that can be tested without launching the Engine, while designers work directly with configuration assets.

### **Drawing a clear line between live data and game assets**

In *The Walking Dead: Aftermath*, Addressables handle memory management and loading rather than remote content delivery. Twenty-nine groups correspond to individual features, and they load and unload in much the same way as the game’s contexts.

Live content follows a separate pipeline built directly on the [AssetBundles](https://docs.unity3d.com/6000.3/Documentation/Manual/AssetBundlesIntro.html) API rather than Addressables. Bundles are built per platform, uploaded, and fetched by the game at runtime. Each one includes a hash, a checksum, and the oldest compatible client version.

The team’s rule is simple: “If designers want to change it every week, it belongs in a bundle. If it’s art or code, it belongs in the build.”

Inside that boundary, the team can still move events, rebalance rewards, retune offers, switch features or purchasing behavior on and off, and run A/B tests without going back to the stores. New art and new code require a build.

“We set that boundary intentionally so the live surface stays small enough that, when something breaks, we can identify what changed,” says Granig.

Visual variety follows a similarly controlled approach. Arenas are built by hand rather than procedurally generated. Instead of duplicating environments, the team changes their look through materials, lighting, and shaders on existing geometry. Around 35 shader graphs and 10 handwritten shaders make up that system.

“Because the arenas are built by hand, we can account for everything a player might see and measure all of it, rather than sampling and hoping.”

![The Walking Dead: Aftermath | Swift Games studio | Ares Interactive](https://cdn.sanity.io/images/fuvbjjlp/production/7c49e68140f3704e8db84c0c083da0dd2f54f1cd-1290x2796.png?w=3840&h=8323&fit=crop&auto=format&q=75)

The Walking Dead: Aftermath | Swift Games studio | Ares Interactive

### **Shortening the path from spreadsheet to live game**

Much of the team’s live ops speed comes from tooling.

Designers edit configuration themselves. Internal importers pull chapters, text, and reward tables directly from spreadsheets, and the spreadsheet stays the source of truth.

The result: If the team spots a live ops or balancing issue, it can push a fix in about 15 minutes instead of going through a full release process.

The build pipeline is designed to shorten iteration time, too. Deep profiling is a build switch rather than a dedicated branch, so developers can request a profiling build of whatever they’re working on when they suspect a regression. Work on caching and build times also helps the team handle the large number of builds it produces each day.

Because UI changes ship weekly, the team relies on the Device Simulator for notch and safe-area checks across different screen shapes. It doesn’t replace physical-device testing, but it catches layout issues earlier.

The hardest operational problem came from separating development and live environments. Firebase configuration is baked into build files, and Firebase, Play Services keys, Facebook configuration, bundle IDs, names, and icons all have to match.

The team eventually moved responsibility for those environments into continuous integration (CI). Development and live builds use different bundle IDs, names, and icons, so they can coexist on the same device. If a development build connects to the live server, an in-game warning appears. Uploads fail when configuration is missing, rather than silently targeting the wrong environment.

“We moved the responsibility into CI instead of leaving it to people,” Granig says.

![Baseball Hits 26 | 7th Inning | Ares Interactive](https://cdn.sanity.io/images/fuvbjjlp/production/a2d19943be3da6c52f2b3f32561e4a0bf439fe38-1290x2796.png?w=3840&h=8323&fit=crop&auto=format&q=75)

Baseball Hits 26 | 7th Inning | Ares Interactive

### **Start small, test early**

Both teams arrive at the same lesson from different directions: Sustainable live development depends on deciding early what needs to change, isolating it from what should stay stable, and building systems that assume something will eventually go wrong.

For *Baseball Hits 26*, that means a data-driven backend that can react quickly to the real baseball season while keeping client releases, devices, and server failures from interrupting play.

For *The Walking Dead: Aftermath*, that means modular live systems, tightly controlled configuration, and a deliberate boundary: Content can change remotely, while code and art ship in the build.

Granig’s advice for teams approaching their first live mobile game is to prove the core experience before building the live-service machinery around it.

“Put together one to three days of content and launch it before working on anything else. Then look at how many players come back the next day. If they do not return, no amount of late-game content is going to rescue it,” he explains.

“Then do it again. Add content, look at day three, and repeat. Start small, test early, and let the numbers tell you whether the game is working. The hard part is saying no to everything you want to build until the core loop proves itself.”

**[Baseball Hits 26](https://aresinteractive.com/games/baseballhits/) *and* [The Walking Dead: Aftermath](https://aresinteractive.com/games/the-walking-dead-aftermath/) *are available now on the App Store and Google Play. Check out more stories from Unity developers on the [Unity Blog](https://unity.com/blog) and [Resource Hub](https://unity.com/resources).***
