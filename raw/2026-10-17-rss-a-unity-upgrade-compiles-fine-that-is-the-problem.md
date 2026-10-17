---
"source": "https://dev.to/nabeelbaghoor/a-unity-upgrade-compiles-fine-that-is-the-problem-h0f"
"title": "A Unity Upgrade Compiles Fine. That Is the Problem."
"author": "Nabeel Hassan"
"date_published": "2026-10-14"
"date_clipped": "2026-10-17"
"category": "Game Development / Unity"
"source_type": "rss"
"canonical_source": "https://nabeelbaghoor.com/blog/upgrading-unity-version-live-project"
---

# A Unity Upgrade Compiles Fine. That Is the Problem.

If you come from web work, a framework upgrade has a shape you trust. You bump the version, the type checker lights up, a few tests go red, you fix them, the build goes green, you ship. The failures are loud, and loud failures are cheap.

Unity upgrades do not have that shape. The project opens in the new editor, everything compiles, the scene plays, and a week later someone on the team is holding one specific phone saying "it just feels different". Nothing threw. Nothing is red. The build is green and wrong.

I have done this upgrade a lot over five-plus years of Unity work, more often on projects I inherited than ones I started. The one that shaped how I do it now was at RAQTS, where I stepped in as CTO and the Unity layer was part of a live product with players and facilities using it every night. You do not get to "try the new version and see" on a product like that. So here is the process I actually use, written for people who know how to ship software but have not had Unity quietly change underneath them yet.

## Why it fails quietly

Four structural reasons, and the last one is the one that hurts.

**The editor rewrites your project.** Opening a project in a newer version reimports assets and can reserialise scenes, prefabs and project settings. The resulting diff is enormous, and almost all of it is noise. The three lines that matter are buried in three thousand that do not.

**Packages move on their own schedule.** The render pipeline, the input system, XR and AR packages each have their own version rules. A new editor often forces new package versions, and each of those brings its own breaking changes. You thought you were doing one upgrade. You are doing five.

**Native code sits underneath.** Plugins compiled against one toolchain, Android Gradle and SDK settings, iOS Xcode project generation: all of these shift between versions, and none of them show up in the editor.

**Behaviour changes without an error.** Physics, lighting, shader compilation, UI layout and timing can all come out slightly different. A compile error costs you ten minutes. A change in feel that reaches users costs you a release, because nobody sees it in the editor.

## Write down why you are upgrading

"Newer is better" is not a reason. A store requirement, a platform SDK you need, a package that will not install on your current version, a bug that is fixed upstream and costing you: those are reasons. The reason picks the target.

My default target is the latest LTS release that satisfies the reason, not the newest release available. LTS gets fixes for longer and changes less underneath you. For a product that has to work every night, boring is a feature.

Write the reason in the ticket. Halfway through, when the upgrade gets painful (it will), that one sentence is what stops the team from either abandoning the branch or letting it swell into a rewrite.

## Get a baseline before you touch anything

At any point during the upgrade I want to answer one question: is this different from what we had?

That needs three things:

* **A tagged build of the current version**, produced by CI, installed on the real test devices and left there. If your builds are not reproducible yet, fix that first. I wrote about the order I set that up in, tests last, in [Your Unity Pipeline Does Not Need Tests Yet](https://dev.to/nabeelbaghoor/your-unity-pipeline-does-not-need-tests-yet-2ib4).
* **A written list of the flows that matter**, the ten or so things a user actually does, so anyone can walk them and not just the person who built them.
* **A few numbers**: build size, time to the first interactive screen, and frame time on your weakest supported device.

Without a baseline, every report after the upgrade becomes an argument about whether it "was always like that". With one, you put two phones side by side and look.

## Audit before you open the new editor

An hour of reading here saves days later. Before the project ever opens in the new version, I list:

* **Every package** in the manifest, and whether a compatible version exists for the target.
* **Every native plugin and third-party SDK**, especially analytics, ads, payments, networking, and anything with Android or iOS native code. These are the most common blockers because you are waiting on someone else's release.
* **Render pipeline and custom shaders.** Shaders written against an older pipeline version are a classic source of silent visual change.
* **Input handling.** Projects that mix the old input manager with the newer input system tend to surface problems here.
* **Platform settings**: Android minimum and target API levels, Gradle setup, iOS minimum version, and any post-process build scripts that edit the generated Xcode or Gradle project.

Anything with no compatible version is a decision you make before the upgrade, not a surprise halfway through. Sometimes the honest answer is that an abandoned plugin has to be replaced first, as its own separate piece of work. Same instinct as the first week on an inherited codebase: find the thing nobody owns before it finds you.

## The branch mechanics

This is the part I am most strict about, because it is what keeps the diff reviewable:

1. **Dedicated branch.** Nothing lands on it except the upgrade.
2. **Close the editor, clear the `Library` folder**, then open the project in the new version so the reimport is clean.
3. **Commit the editor's automatic changes on their own**, before you fix a single thing. That commit is the editor's work. Everything after it is yours, and a reviewer can now tell the two apart.
4. **Fix compile errors, then every warning that mentions an obsolete API.** Deprecation warnings are next year's compile errors.
5. **One major version at a time** if you are several behind. Jumping across many at once stacks every migration into one diff nobody can read.

Keep the branch short. A long-lived upgrade branch fights every feature merged in the meantime, and resolving merge conflicts in scene and prefab YAML is one of the worst jobs in the engine.

## Test on devices, against the baseline

The editor is exactly where an upgrade looks fine. Install the upgraded build next to the baseline build on the same physical devices and walk the written flows. What I specifically look for:

* **Visual differences**: lighting, colour, shadows, transparency, UI scaling, safe areas.
* **Performance on the weakest device**: frame time and memory. On standalone headsets this is even tighter, which I went into in [Standalone VR Gives You 11 Milliseconds a Frame](https://dev.to/nabeelbaghoor/standalone-vr-gives-you-11-milliseconds-a-frame-the-editor-will-not-warn-you-3pk2).
* **First launch after an update, not just a clean install.** Saved data, cached content and player preferences have to survive. This one gets missed constantly because a fresh install is what you get by default when you test.
* **Platform features**: AR tracking, permission prompts, push notifications, purchases, deep links, backgrounding and resuming.

## Ship it like the risky release it is

An engine upgrade is one of the riskiest releases a Unity product makes. Treat it that way:

* **Release it alone.** No features in the same build. If something regresses, you want exactly one suspect.
* **Staged rollout** on Google Play and phased release on the App Store, so a problem reaches a small share of users first.
* **Watch crash and error reporting** closely for the first days, against the previous version's numbers.
* **Keep the backend tolerant of the old version**, because plenty of users will sit on it for weeks. I wrote a whole post on that: [The App Version You Shipped in March Is Still Calling Your API](https://dev.to/nabeelbaghoor/the-app-version-you-shipped-in-march-is-still-calling-your-api-3lkl).

The thing web developers underestimate: on mobile you cannot roll back a shipped build the way you roll back a deploy. The store review cycle is the real constraint, so the bar before you submit has to be higher than it feels necessary.

## How often

The cheapest upgrade is a small one. A project that moves to each new LTS within a few months does a series of boring migrations. A project left alone for several years eventually faces one huge jump, usually forced by a store deadline at the worst possible moment.

For live products my rule is: plan an upgrade at least once a year, schedule it in a quiet period, and put it on the roadmap as maintenance rather than squeezing it between features. Platform requirements like Google Play raising the target API level it accepts arrive on a calendar. Being ahead of that calendar is much cheaper than chasing it.

## The short version

* Have a specific reason, and target the LTS release that satisfies it.
* Build a known-good baseline on real devices before you touch anything.
* Audit packages, plugins, shaders, input and platform settings first.
* Dedicated branch, one major version at a time, editor changes in their own commit.
* Test on devices against the baseline, including updating over an existing install.
* Ship the upgrade alone, staged, with crash reporting watched.

A good Unity upgrade looks like nothing happened. That is the whole goal, and it only comes from treating it as a small migration project with a plan, not a Friday afternoon menu click.

I would like to hear from other Unity people here: what is the quietest regression an upgrade ever slipped past you? Mine are almost always "works on a clean install, breaks on update".

*Originally published on [nabeelbaghoor.com](https://nabeelbaghoor.com/blog/upgrading-unity-version-live-project/).*
