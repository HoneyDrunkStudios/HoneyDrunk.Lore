---
source: "https://andrewlock.net/finding-the-total-number-of-processors-on-a-machine-with-dotnet"
title: "Finding the total number of processors on a machine with .NET"
author: "Andrew Lock"
date_published: "2026-08-25"
date_clipped: "2026-09-13"
category: ".NET Ecosystem"
source_type: "rss"
capture_mode: "attributed-summary"
full_text_fetched: "true"
---

# Finding the total number of processors on a machine with .NET

Original source: [Finding the total number of processors on a machine with .NET](https://andrewlock.net/finding-the-total-number-of-processors-on-a-machine-with-dotnet)

## Source-content summary

Andrew Lock distinguishes the host's total logical processor count from processors available to a constrained process. In modern .NET, Environment.ProcessorCount accounts for process restrictions, which makes it unsuitable when diagnostics specifically need the host total.

The article develops platform-specific implementations: native calls on Windows and macOS, and parsing Linux's online CPU ranges from /sys/devices/system/cpu/online. A wrapper selects the implementation by operating system. Lock suggests placing it behind a dependency-injected singleton and caching the result, while explicitly noting the example had not yet shipped in production.

HoneyDrunk relevance: make capacity and diagnostic metrics explicit about whether they describe the machine or the application's allocation. Treat the sample as implementation evidence to validate against the actual container, operating system, and CPU topology; a host total should not silently become the worker concurrency budget.

Capture note: This is an attributed summary of the fetched article, not a verbatim full-text archive. The original source retains the complete examples and discussion.
