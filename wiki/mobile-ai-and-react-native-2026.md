# Mobile AI and React Native 2026

## Decision-useful summary
React Native AI coding support is becoming specialized. Callstack's Apex source argues that React Native work has enough framework, native-module, library, and cross-platform nuance that a domain-specialized model can be useful even when general coding models improve. Treat Apex as a scout signal for model specialization and local evals, not as proof that HoneyDrunk should switch mobile model defaults. [source: raw/2026-06-01-web-introducing-apex-a-fast-specialized-model-for-react-native.md]

## Claims
- Apex is a focused React Native coding model based on Gemma 4, trained with supervised fine-tuning and GRPO after proof-of-concept experiments on other bases such as Devstral and Qwen. confidence: 1 vendor/source-author source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-introducing-apex-a-fast-specialized-model-for-react-native.md]
- Callstack says Apex is evaluated against React Native Evals and is meant to improve the React Native performance-to-cost ratio relative to larger general models within that narrow domain. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-introducing-apex-a-fast-specialized-model-for-react-native.md]
- The training data is described as curated from recent GitHub repositories and React Native ecosystem work rather than a random broad web scrape. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-introducing-apex-a-fast-specialized-model-for-react-native.md]

## Typed entities
- model: Apex
- company: Callstack
- framework: React Native
- benchmark: React Native Evals
- base model: Gemma 4
- model family: Devstral
- model family: Qwen
- training method: supervised fine-tuning / SFT
- training method: Group Relative Policy Optimization / GRPO

## Explicit relationships
- Apex depends-on React Native-specific training data and evaluation rather than broad coding benchmarks alone.
- Domain specialization complements [[edge-ai-and-ai-infrastructure-2026]] model-routing decisions.
- React Native agent workflows depend-on native module, platform constraint, and ecosystem-library knowledge.

## HoneyDrunk implications
- If HoneyDrunk starts React Native work, create a small React Native eval set before adopting Apex or any routing default.
- Track domain-specialized models as cost-control candidates, especially for repetitive framework-specific tasks.

## Confidence and quality notes
- Quality posture: useful scouting signal, but vendor-authored and requires local benchmark validation.
- Privacy filter: no private repository data copied; public model/company/framework names retained.

## 2026-06-18 compile additions: Android 17 as intelligence-system and adaptive-first release

### Source-backed claims
- Android 17 introduces AppFunctions as a platform API plus Jetpack library that lets apps expose local capabilities as orchestratable tools for Android MCP, with Gemini integration in private preview and a test agent app for discovery/execution simulation. Source: `raw/2026-06-18-web-android-developers-googleblog-com-android-developers-blog-android-17-i.md`. confidence: 1 official Android Developers Blog source, last-confirmed 2026-06-18.
- Android 17 removes opt-outs for orientation and resizability restrictions on large-screen devices for apps targeting API level 37, while games remain exempt by Google Play category. Source: `raw/2026-06-18-web-android-developers-googleblog-com-android-developers-blog-android-17-i.md`. confidence: 1 source, last-confirmed 2026-06-18.
- Android 17 makes Android development Compose-first: new Android APIs, libraries, tools, and guidance will be built for Jetpack Compose, while legacy View components and View-based Jetpack libraries move to maintenance mode. Source: `raw/2026-06-18-web-android-developers-googleblog-com-android-developers-blog-android-17-i.md`. confidence: 1 source, last-confirmed 2026-06-18.
- Android 17 adds stricter app memory limits, generational GC improvements, lock-free `MessageQueue`, stricter `static final` behavior, local-network access controls, SMS OTP protections, post-quantum signing support, safer native dynamic-code loading, and NPU access declaration requirements. Source: `raw/2026-06-18-web-android-developers-googleblog-com-android-developers-blog-android-17-i.md`. confidence: 1 source, last-confirmed 2026-06-18.

### Typed entities
- platform: Android 17 / API level 37
- API: AppFunctions
- protocol/surface: Android MCP
- library: Jetpack Compose
- library: Material 3 Adaptive
- component: lock-free `MessageQueue`
- permission: `ACCESS_LOCAL_NETWORK`
- signing scheme: v3.2 APK Signature Scheme
- algorithm: ML-DSA
- manifest feature: `FEATURE_NEURAL_PROCESSING_UNIT`

### Explicit relationships
- AppFunctions expose app-local state and capabilities to device agents, making Android apps tool providers as well as UI surfaces.
- Adaptive-first requirements supersede legacy large-screen opt-outs for API 37 non-game apps.
- Compose-first guidance supersedes View-based feature growth for new Android UI work.
- Local network and dynamic-code-loading restrictions add privacy/security gates that app SDKs, libraries, and game engines must support.

### HoneyDrunk implications
- If HoneyDrunk builds Android apps or SDKs, target adaptive layouts and Compose-first implementation before API 37 forces late compatibility work.
- Treat AppFunctions as a future agent integration surface, but require local-state privacy review and explicit user intent before exposing app actions to assistants.
- For Android game work, track the game exemption separately from app/store tooling dependencies that may still need Android 17 compatibility.

### Quality notes
- Official platform announcement. Some integrations are preview/private-preview and should be checked against current Android docs before implementation.
