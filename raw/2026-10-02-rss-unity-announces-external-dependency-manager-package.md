---
source: "https://unity.com/blog/external-dependency-manager"
title: "Unity Announces External Dependency Manager Package"
author: "Maria Sifniotis; Julius Miknevicius"
date_published: "2026-09-29"
date_clipped: "2026-10-02"
category: "Game Development / Unity"
source_type: "rss"
---

# Unity Announces External Dependency Manager Package

# Unity Announces External Dependency Manager Package

We're pleased to announce External Dependency Manager (EDM), an official Unity package for handling native Android and iOS dependencies, distributed via the Unity Package Manager (UPM). Additionally, Google has [announced](https://github.com/googlesamples/unity-jar-resolver?tab=readme-ov-file) the deprecation of EDM4U on October 26, 2026. We've been collaborating with Google to make the transition a smooth one for both game developers and SDK maintainers.

If you currently use Google's External Dependency Manager for Unity (EDM4U), EDM will feel familiar. It's built on a fork of EDM4U and brought into Unity as an official package. It will be actively maintained by Unity, with engine compatibility, feature updates, and bug fixes.

Keep reading for what's changing, why it matters, and what it means for you. For technical details, FAQ, and full migration details, head to our [Discussions post](https://discussions.unity.com/t/introducing-external-dependency-manager-edm-unitys-official-package-for-mobile-native-dependencies/1737255) and our official [EDM documentation](https://docs.unity3d.com/Packages/com.unity.external-dependency-manager@2.1/manual/index.html).

**How to get started with EDM**

Game developers and SDK maintainers using Google's External Dependency Manager for Unity (EDM4U) can switch to Unity's External Dependency Manager (EDM) without rewriting their setup. EDM is free for Unity 2022.3 and later, and it reads the same XML dependency files that SDKs use with EDM4U. For full setup details, see the [EDM documentation](https://docs.unity3d.com/Packages/com.unity.external-dependency-manager@2.1/manual/get-started-with-edm.html).

**For game developers**

**Install EDM from the Unity Package Manager.**Go to Window > Package Management > Package Manager, search the Unity Registry for "External Dependency Manager," and select Install.**Choose EDM as the active dependency manager.**If EDM4U is already in your project, Unity asks which dependency manager to use. Nothing is deleted, and you can switch back anytime from Assets > External Dependency Manager.**Remove EDM4U when you're ready.**If you installed EDM4U yourself, you can uninstall it. If EDM4U came into your project through an SDK, keep it installed until that SDK moves to EDM.

We expect existing projects to migrate without issue, but if you hit something unexpected, please report it using the Unity Editor's built-in [Bug Reporter](https://unity.com/releases/editor/qa) (Help > Report a Bug).

**For SDK maintainers**

EDM fully supports the existing XML dependency specification. To make EDM the recommended dependency manager for your Unity SDK, follow the [plug-in distributor guide](https://docs.unity3d.com/Packages/com.unity.external-dependency-manager@2.1/manual/get-started-with-edm.html#plug-in-distributor-guide).

**Why are mobile dependencies important?**

Most mobile games depend on SDKs for services such as ads, analytics, monetization, and push notifications. Each SDK brings its own native Android and Apple library dependencies in order to work correctly, and with an average game shipping multiple SDKs, a library conflict is close to inevitable. Without a tool to manage those dependencies, two challenges can surface:

- Manually integrating platform-specific Android and iOS libraries into a Unity project is complex.
- Resolving conflicting dependencies between SDKs takes manual work and is error-prone.

EDM solves both by letting SDKs declare the libraries they need in a plain text file. It then orchestrates the inclusion of those dependencies so they can be resolved by the relevant system (Gradle, CocoaPods, or Swift Package Manager) and ensures the libraries your SDK and game need end up in the final build.

**What Unity owning EDM means for you**

The official EDM package is the first step toward making mobile dependency management a first-class citizen of the Unity Engine. With this capability under Unity's stewardship, you get compatibility with the latest platform and engine changes alongside the native library resolution features you already rely on. While this initial release is focused on stability and helping transition from Google EDM4U, it already contains a number of fixes and improvements in areas such as CocoaPods/Ruby integration and user experience.

**We’re here to help**

Stability and project continuity are our first priority throughout this migration, for SDK maintainers and game developers alike. This is the start of a longer investment in mobile dependency management at Unity, and the fastest way to shape what comes next is to tell us what you need.

Questions or feedback? Let us know in the [Discussions thread](https://discussions.unity.com/t/introducing-external-dependency-manager-edm-unitys-official-package-for-mobile-native-dependencies/1737255).
