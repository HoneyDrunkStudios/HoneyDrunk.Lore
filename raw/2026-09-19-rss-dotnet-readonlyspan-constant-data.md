---
source: "https://andrewlock.net/removingbyte-array-allocations-in-dotnet-framework-using-readonlyspan-t"
title: "Removing byte[] allocations in .NET Framework using ReadOnlySpan<T>"
author: "Andrew Lock"
date_published: "2026-04-21"
date_clipped: "2026-09-19"
category: ".NET Ecosystem"
source_type: "rss"
capture_format: "attributed-summary"
---

# Removing byte[] allocations in .NET Framework using ReadOnlySpan<T>

Source: [Removing byte[] allocations in .NET Framework using ReadOnlySpan<T>](https://andrewlock.net/removingbyte-array-allocations-in-dotnet-framework-using-readonlyspan-t)

*Attributed summary of the fetched written article; not a verbatim reproduction.*

Andrew Lock examines how a ReadOnlySpan<byte> over constant byte data can point directly into assembly metadata instead of allocating an array. This is a compiler optimization, and his .NET Framework example uses System.Memory to provide the span type.

The article validates the behavior by inspecting emitted IL. The optimized example loads an address and length and constructs a span over existing data, avoiding array construction and copying. UTF-8 literals can use the same general mechanism.

There are sharp limits: the demonstrated portable optimization depends on immutable access, constant elements, and byte-sized primitives. Changing element types or making values nonconstant can change generated code and introduce allocations. A property that syntactically constructs an array should not be assumed allocation-free without checking its compilation target.

HoneyDrunk implication: consider this for fixed protocol bytes or parsing tables, then inspect generated IL and measure the actual target build. This is an April technical reference selected for its compiler-level caveats, not a newly released runtime feature.
