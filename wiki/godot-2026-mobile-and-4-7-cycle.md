# Godot 2026 Mobile and 4.7 Cycle

## Decision-useful summary
Godot's 2026 signal is mobile maturity plus active 4.7 stabilization and rendering feature growth. The 4.7 cycle moved through dev snapshots and beta with GUI/editor/rendering/export improvements; HDR output is planned for 4.7 on Windows, macOS, iOS, visionOS, and Linux/Wayland for Forward+ and Mobile renderers. 4.6.2 maintained the stable line. Mobile remains strategic: around half of game revenue, the largest market segment, and roughly 49% of surveyed Godot developers targeting mobile. [sources: raw/2026-05-04-rss-godot-engine-dev-snapshot-godot-4-7-dev-3.md; raw/2026-05-06-rss-godot-engine-dev-snapshot-godot-4-7-dev-4.md; raw/2026-05-05-rss-godot-engine-dev-snapshot-godot-4-7-dev-5.md; raw/2026-05-04-rss-godot-engine-dev-snapshot-godot-4-7-beta-1.md; raw/2026-05-05-rss-godot-engine-maintenance-release-godot-4-6-2.md; raw/2026-05-05-rss-godot-engine-godot-mobile-update-april-2026.md; raw/2026-05-07-rss-godot-engine-hdr-output-arrives-in-godot-4-7.md]

## Claims
- Godot 4.7 dev 3 included long-awaited features, especially GUI-related improvements, and requested broad testing before stabilization. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-04-rss-godot-engine-dev-snapshot-godot-4-7-dev-3.md]
- Godot 4.7 dev 4 highlighted nearest-neighbor scaling for 3D viewports, `Control.custom_maximum_size`, improved `Tree` drag-and-drop, inspector array layout fixes, 188 fixes from 88 contributors, and build commit `755fa449c`. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-godot-engine-dev-snapshot-godot-4-7-dev-4.md]
- Godot 4.7 dev 5 landed near feature freeze and highlighted asset store API work, individual export template handling, RichTextLabel image scaling in `em`, inline text shader previews, rectangular area lights, audio bus UI revamp, Android export splash options, Wayland touch support, and raytracing pipeline refactors. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-05-rss-godot-engine-dev-snapshot-godot-4-7-dev-5.md]
- Godot 4.7 beta 1 marked the cycle's first beta snapshot and shifted emphasis toward regression fixes and bug-hunting sprints. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-04-rss-godot-engine-dev-snapshot-godot-4-7-beta-1.md]
- Godot 4.7 beta 2 resolved over 100 regressions since beta 1, included 153 fixes from 74 contributors, built from commit `777579205`, and still had known XR macOS quit-crash and GUI tooltip regressions. confidence: 1 source, last-confirmed 2026-05-12. [source: raw/2026-05-12-rss-godot-engine-dev-snapshot-godot-4-7-beta-2.md]
- Godot 4.7 adds HDR output support on Windows, macOS, iOS, visionOS, and Linux/Wayland for Forward+ and Mobile renderers; Android HDR remains planned for a future release, and Compatibility/Web are excluded due to graphics API limitations. confidence: 1 source, last-confirmed 2026-05-07. [source: raw/2026-05-07-rss-godot-engine-hdr-output-arrives-in-godot-4-7.md]
- Enabling Godot HDR output depends on supported platform/driver/renderer choices: Direct3D 12 on Windows, Metal or Vulkan on Apple platforms, Vulkan with Wayland on Linux, and `Display > Window > HDR > Request HDR Output`. confidence: 1 source, last-confirmed 2026-05-07. [source: raw/2026-05-07-rss-godot-engine-hdr-output-arrives-in-godot-4-7.md]
- Godot 4.6.2 is a maintenance release for the latest stable line while the team continues 4.7 development; users are advised to back up or use version control before upgrades. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-05-rss-godot-engine-maintenance-release-godot-4-6-2.md]
- Godot's April 2026 mobile update says mobile games represent about half of global game revenue, are the largest market segment, and are targeted by about 49% of Godot developers in community polls. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-05-rss-godot-engine-godot-mobile-update-april-2026.md]
- Xogot shows Godot editor/runtime adapted for iPad and iPhone with an iOS-native interface layer. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-04-rss-godot-engine-godot-showcase-xogot-godot-for-ipad-iphone.md]

## Typed entities
- project: Godot Engine
- version: Godot 4.7 dev 3
- version: Godot 4.7 dev 4
- version: Godot 4.7 dev 5
- version: Godot 4.7 beta 1
- version: Godot 4.6.2
- project: Xogot
- organization: Xibbon
- platform: iOS
- platform: Android
- platform: visionOS
- platform: Windows
- platform: macOS
- platform: Linux/Wayland
- renderer: Godot Forward+
- renderer: Godot Mobile renderer
- renderer: Godot Compatibility renderer
- concept: mobile export
- concept: HDR output
- concept: tone mapping
- concept: AgX tonemapper
- concept: nearest-neighbor scaling
- concept: Tree drag-and-drop
- concept: RichTextLabel image scaling
- concept: inline shader previews
- concept: rectangular area lights

## Explicit relationships
- Godot 4.7 beta 1 supersedes earlier 4.7 dev snapshots for release-readiness posture.
- Godot 4.7 dev 4 and dev 5 preserve feature-detail evidence that supports evaluating 4.7 before final release.
- Godot 4.7 HDR output depends-on supported OS, rendering driver, and Forward+/Mobile renderers.
- Compatibility renderer limitations contradict Web HDR output availability in Godot 4.7.
- Godot 4.6.2 maintains the stable 4.6 line while Godot 4.7 depends-on regression testing before release.
- Xogot uses Godot Engine and an iOS interface layer to bring Godot editing to iPad/iPhone.
- Godot mobile work depends-on repeatable builds, fewer device-specific surprises, and smoother testing/export flows.

## HoneyDrunk implications
- Treat Godot 4.7 features as promising but pre-release until final/patch release; use 4.6.2 for stable production baselines.
- Mobile Godot is worth watching if HoneyDrunk explores iPad-first or mobile-first tooling/game prototypes.
- HDR output may matter for visual-forward prototypes, but it narrows renderer/platform choices and excludes Web for now.
- Nearest-neighbor 3D viewport scaling may matter for stylized/pixel-art 3D prototypes where crisp low-resolution presentation is part of the look.

## Confidence and quality notes
- Quality posture: decision-usable for tracking engine direction; not enough to pick Godot over Unity without project-specific constraints.
- Supersession: 4.7 beta 1 supersedes dev snapshots for release-stage signal, but dev snapshots preserve feature detail.
- Privacy filter: no private data copied.
