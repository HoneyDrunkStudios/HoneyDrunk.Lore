---
source: "https://andrewlock.net/exploring-the-dotnet-11-preview-6-automatic-csrf-protection-based-on-fetch-metadata-http-headers"
title: "Automatic CSRF protection based on Fetch Metadata headers: Exploring the .NET 11 preview - Part 6"
author: "Andrew Lock"
date_published: "2026-08-04"
date_clipped: "2026-09-13"
category: "Security & Ethical Hacking"
source_type: "rss"
capture_mode: "attributed-summary"
full_text_fetched: "true"
---

# Automatic CSRF protection based on Fetch Metadata headers: Exploring the .NET 11 preview - Part 6

Original source: [Automatic CSRF protection based on Fetch Metadata headers: Exploring the .NET 11 preview - Part 6](https://andrewlock.net/exploring-the-dotnet-11-preview-6-automatic-csrf-protection-based-on-fetch-metadata-http-headers)

## Source-content summary

Andrew Lock examines Fetch Metadata-based CSRF protection introduced in ASP.NET Core's .NET 11 preview 6. Browser-provided request-context headers let the framework classify request origins, reducing reliance on synchronizer-token validation for supported configurations.

The article compares the new approach with existing antiforgery tokens, explains relevant headers, and walks through the framework's request-handling decisions and configuration. It distinguishes Blazor SSR and Minimal API adoption from MVC and Razor Pages, where existing token validation can remain active as well.

Lock's experiment removing the older protection from MVC/Razor Pages is explicitly described as unverified and not recommended for direct adoption. HoneyDrunk relevance: review authentication cookies, endpoint types, browser compatibility, and framework-version behavior together before changing CSRF defenses. Retain the preview-version boundary and validate supported configuration against the eventual release rather than copying the experimental removal technique.

Capture note: This is an attributed summary of the fetched article, not a verbatim full-text archive. The original source retains the complete examples and discussion.
