---
source: "https://andrewlock.net/exploring-the-dotnet-11-preview-3-avoiding-tostring-allocations-with-stringbuilder-movechunks"
title: "Avoiding ToString() allocations with StringBuilder.MoveChunks: Exploring the .NET 11 preview - Part 3"
author: "Andrew Lock"
date_published: "2026-06-23"
date_clipped: "2026-09-14"
category: ".NET Ecosystem"
source_type: "rss"
capture_mode: "attributed-summary"
content_note: "Substantive summary of the fetched readable article; not a verbatim full-text archive."
---

# Avoiding ToString() allocations with StringBuilder.MoveChunks: Exploring the .NET 11 preview - Part 3

Source: [Avoiding ToString() allocations with StringBuilder.MoveChunks: Exploring the .NET 11 preview - Part 3](https://andrewlock.net/exploring-the-dotnet-11-preview-3-avoiding-tostring-allocations-with-stringbuilder-movechunks)

## Attributed article summary

StringBuilder.MoveChunks, introduced in the .NET 11 preview discussed here, transfers a builder's internal character chunks into a new builder and resets the original. It avoids materializing an intermediate string merely to transfer accumulated text.

The key difference from assigning the existing builder to another variable is ownership: callers retaining the original reference can continue using an emptied object without mutating the transferred content. The operation also differs from Clear because the original does not retain the transferred storage.

Lock connects this to a proposed Roslyn SourceText path that could consume builder content without ToString allocation while preserving downstream immutability. That Roslyn API was still a proposal at publication, with source-generator target-framework constraints unresolved.

HoneyDrunk relevance: consider explicit buffer ownership transfer in generation-heavy libraries. Benchmark allocation and reuse tradeoffs rather than assuming universal savings; do not treat the proposed Roslyn integration as shipped functionality.
