---
source: "https://andrewlock.net/updates-to-netescapaades-enumgenerators-new-apis-and-system-memory-support"
title: "Recent updates to NetEscapades.EnumGenerators: new APIs and System.Memory support"
author: "Andrew Lock"
date_published: "2026-01-02"
date_clipped: "2026-09-28"
category: ".NET Ecosystem"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Andrew Lock explains enum-generator changes that consolidate parsing and serialization settings into value-type options. Callers can reject numeric strings, choose comparison behavior, and request invariant casing without a separate string transformation for known enum values.

For older target frameworks, a System.Memory reference and an MSBuild opt-in expose span-based overloads. An important limitation remains: numeric fallback may convert a span to a string when the older platform lacks an appropriate parsing overload, introducing an allocation.

HoneyDrunk application: make enum input acceptance explicit at API boundaries and benchmark serialization with real enum distributions. Verify older-target build configuration rather than assuming span support from a modern-runtime example.

This January 2026 backfill documents prerelease behavior. Package-reference auto-detection was described as experimental, and the article's closing version reference differs from its main walkthrough. Confirm the deployed package's API before applying examples.

Source: [Original article](https://andrewlock.net/updates-to-netescapaades-enumgenerators-new-apis-and-system-memory-support).

Capture note: Original attributed summary after fetching readable written content; not a full-text reproduction.
