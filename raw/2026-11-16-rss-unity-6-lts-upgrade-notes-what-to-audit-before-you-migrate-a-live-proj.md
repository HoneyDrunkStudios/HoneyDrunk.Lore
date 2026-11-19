---
source: "https://dev.to/juegostudiosofficial/unity-6-lts-upgrade-notes-what-to-audit-before-you-migrate-a-live-project-3k5m"
title: "Unity 6 LTS Upgrade Notes: What to Audit Before You Migrate a Live Project"
author: "Juego Studios"
date_published: "2026-11-16"
date_clipped: "2026-11-16"
category: "Game Development / Unity"
source_type: "rss"
---

# Unity 6 LTS Upgrade Notes: What to Audit Before You Migrate a Live Project

Upgrading a prototype to a new Unity version is an afternoon. Upgrading a game that's already live, with players, save files, a CI pipeline, and a content cadence, is a project. Most painful upgrades we've seen weren't caused by one big breaking change. They came from a dozen small things nobody wrote down before the version bump.

This is the audit list we run before moving a live project to Unity 6 LTS. It's engine-version-agnostic enough to reuse for the next upgrade too.

## 0. Branch, freeze, and baseline first

- Cut a dedicated upgrade branch. Don't upgrade on main while the live team keeps shipping.
- Record a **baseline** on the current version: build times, build size per platform, frame time and memory on your lowest-spec target, and load times for two or three key scenes. Without numbers from before, "it feels slower" turns into a week-long argument.
- Make sure the current version's Library folder isn't committed and that a clean checkout builds. If it doesn't build clean today, it won't build clean after the upgrade.

## 1. Packages and third-party code

- Export the full list from `Packages/manifest.json` and `packages-lock.json`. For every package, note who owns it and whether a Unity 6 compatible version exists.
- Asset Store plugins and native SDKs (ads, analytics, attribution, platform services) are usually the long pole. Check each vendor's release notes before you upgrade, not after.
- Search for code that depends on APIs marked obsolete in your current version. Compiler warnings you've ignored for a year tend to become errors.
- Flag any package you've forked or embedded. Those need a manual diff.

## 2. Rendering

- Confirm which render pipeline you're on and read the upgrade guide for that pipeline specifically.
- If you're on URP, check your custom renderer features and render passes. Unity 6 moves URP toward the Render Graph API, so custom passes written against the older API need review. Budget time for this instead of assuming the compatibility path will hold forever.
- Re-check shader variants and build size. Shader stripping settings and keyword counts can shift after an upgrade.
- Capture reference screenshots of key scenes before upgrading and compare after. Lighting, post-processing, and color space differences are easy to miss in motion.

## 3. Addressables and content delivery

- This is the one that hurts live games most. If players already have cached bundles, you need a clear plan for content catalog compatibility between the old and new player builds.
- Rebuild all Addressables groups on the new version in a test environment and verify that an upgraded client can still load content and that an older client (if you support one) doesn't pull bundles it can't read.
- Check your remote load paths, catalog versioning, and any custom `IResourceProvider` code.

## 4. Save data and serialization

- Load real save files from production (anonymized) on the upgraded build. Test old saves on the new build, not only fresh ones.
- Look for anything serialized by type name or assembly name. Renamed or moved types can silently drop data.
- If you use `JsonUtility`, a third-party serializer, or binary formats, write a quick round-trip test before upgrading so you have something to run after.

## 5. CI and build pipeline

- Update build agents and editor images in a way you can roll back. Keep the old editor version installed until the upgrade ships.
- Re-check command-line build scripts, `-executeMethod` entry points, and any custom `IPreprocessBuildWithReport` / `IPostprocessBuildWithReport` hooks.
- Confirm platform modules, SDK and NDK versions, Xcode version, and signing steps for each target platform.
- Run your full automated test suite on the upgrade branch in CI, not just locally.

## 6. Platform and store requirements

- Check minimum OS versions, target API levels, and any store-side requirements for each platform you ship on. An upgrade is a good moment to catch these, and a bad moment to discover them during submission.

## 7. Regression pass before merge

- Rerun the baseline from step 0 and compare.
- Run a full smoke test on every target platform, including install-over-old-version, save migration, and purchase restore if you have IAP.
- Ship to a small cohort or a test track first if your platforms allow it.

For the regression part, we keep a printable patch-day checklist that works for engine upgrades too: [Patch Day Regression Checklist](https://juegostudiosofficial.itch.io/patch-day-regression-checklist).

## A note on timing

Don't start a major engine upgrade two weeks before a seasonal content drop. Pick a window after a release, keep the live branch on the old version until the upgrade branch has passed its regression pass, and merge only when both the code team and the content team have signed off.

---

*I work at Juego Studios, where our team handles [Unity game development](https://www.juegostudio.com/unity3d-game-development) and engine upgrades for live projects. If you've hit an upgrade issue not on this list, I'd like to hear about it in the comments.*
