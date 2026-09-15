---
source: "https://andrewlock.net/exploring-the-dotnet-11-preview-4-closed-class-hierarchies/"
title: "Closed class hierarchies: Exploring the .NET 11 preview - Part 4"
author: "Andrew Lock"
date_published: "2026-06-30"
date_clipped: "2026-09-15"
category: ".NET Ecosystem"
source_type: "rss"
capture_format: "attributed-summary"
extraction_status: "full written page fetched; readable body reviewed"
---

# Closed class hierarchies: Exploring the .NET 11 preview - Part 4

Source: [Closed class hierarchies: Exploring the .NET 11 preview - Part 4](https://andrewlock.net/exploring-the-dotnet-11-preview-4-closed-class-hierarchies/)

## Attributed content summary

Andrew Lock explains the closed class hierarchy feature as implemented in .NET 11 preview 5. A closed base constrains direct derivation to its assembly, allowing the compiler to reason about the available alternatives and check switch expressions for missing cases.

Unlike a catch-all branch on an ordinary hierarchy, an exhaustive switch over a closed hierarchy can warn when a new case is introduced. Closed hierarchies organize related types through inheritance; unions describe permitted alternatives without requiring that inheritance relationship. Sealing all derived cases enables additional compile-time checks for impossible conversions.

The article also covers generic restrictions and compiler metadata that communicates the feature to consuming assemblies. Derived classes are not automatically closed.

Historical limitation: the setup instructions use preview language settings and a temporary ClosedAttribute workaround for preview 5. Preserve that context; do not apply the workaround to newer SDKs without checking whether it remains necessary. The durable value is the modeling and exhaustiveness tradeoff, not the old installation recipe.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
