---
source: "https://andrewlock.net/exploring-the-dotnet-11-preview-2-dotnet-gets-union-types/"
title: ".NET (OK, C#) finally gets union types🎉: Exploring the .NET 11 preview - Part 2"
author: "Andrew Lock"
date_published: "2026-05-19"
date_clipped: "2026-09-16"
category: ".NET Ecosystem"
source_type: "rss"
capture_format: "attributed-summary"
---

# .NET (OK, C#) finally gets union types🎉: Exploring the .NET 11 preview - Part 2

Source: [.NET (OK, C#) finally gets union types🎉: Exploring the .NET 11 preview - Part 2](https://andrewlock.net/exploring-the-dotnet-11-preview-2-dotnet-gets-union-types/)

## Attributed content summary

Andrew Lock examines C# union types using .NET 11 preview 4. A union represents one of several potentially unrelated types, supporting result and optional-value modeling without forcing those types into a shared inheritance hierarchy.

Switch expressions inspect the contained case and receive exhaustiveness warnings when an alternative is missing. Nullable alternatives require corresponding null handling. The article explains compiler-generated wrappers, the UnionAttribute and IUnion conventions, and how custom implementations participate in the feature.

For API design, the useful distinction is between explicitly enumerating possible outcomes and returning an object whose callers must interpret informally. Review allocation and representation tradeoffs before choosing a custom wrapper.

This is historical preview evidence from May 2026. Language settings, helper-type workarounds, IDE support, and runtime-targeting instructions describe that preview; confirm them against the SDK actually in use rather than treating the installation recipe as current release guidance.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
