---
source: "https://andrewlock.net/exploring-the-dotnet-11-preview-5-improvments-to-process-apis"
title: "Improvements to reading Process outputs: Exploring the .NET 11 preview - Part 5"
author: "Andrew Lock"
date_published: "2026-07-07"
date_clipped: "2026-09-14"
category: ".NET Ecosystem"
source_type: "rss"
capture_mode: "attributed-summary"
content_note: "Substantive summary of the fetched readable article; not a verbatim full-text archive."
---

# Improvements to reading Process outputs: Exploring the .NET 11 preview - Part 5

Source: [Improvements to reading Process outputs: Exploring the .NET 11 preview - Part 5](https://andrewlock.net/exploring-the-dotnet-11-preview-5-improvments-to-process-apis)

## Attributed article summary

Andrew Lock explains how sequentially reading redirected stdout and stderr can deadlock: a child fills one pipe while its parent waits for the other to close. For existing .NET applications, start both asynchronous reads before awaiting completion; event-based readers are another option when output must be processed as it arrives.

The article describes .NET 11 preview APIs for capturing text, bytes, or lines while draining both streams safely. ReadAllText and its asynchronous counterpart return stdout and stderr together. Line APIs expose the stream identity and support enumerable or asynchronous-enumerable consumption. Timeouts and cancellation bound waiting.

The preview implementation uses platform-specific multiplexing for synchronous reads and asynchronous coordination for nonblocking consumption.

HoneyDrunk relevance: subprocess wrappers for agent tools and build automation should drain both streams concurrently and bound execution. API names and availability here describe the July preview source; verify against the target SDK before adopting them.
