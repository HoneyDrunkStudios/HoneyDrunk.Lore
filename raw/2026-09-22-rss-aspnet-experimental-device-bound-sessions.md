---
source: "https://andrewlock.net/exploring-the-dotnet-11-preview-8-experimental-support-for-device-bound-session-credentials-in-aspnetcore"
title: "Experimental support for Device Bound Session Credentials (DBSC) in ASP.NET Core: Exploring the .NET 11 preview - Part 8"
author: "Andrew Lock"
date_published: "2026-09-22"
date_clipped: "2026-09-22"
category: ".NET Ecosystem"
source_type: "rss"
capture_format: "attributed-summary"
---

# Experimental support for Device Bound Session Credentials (DBSC) in ASP.NET Core: Exploring the .NET 11 preview - Part 8

Source: [Experimental support for Device Bound Session Credentials (DBSC) in ASP.NET Core: Exploring the .NET 11 preview - Part 8](https://andrewlock.net/exploring-the-dotnet-11-preview-8-experimental-support-for-device-bound-session-credentials-in-aspnetcore)

Attributed summary of the fetched written article; not a full reproduction. Source claims have not been independently reproduced.

Andrew Lock walks through the experimental Microsoft.AspNetCore.Authentication.DeviceBoundSessions package for .NET 11. It layers device-bound sessions over an existing cookie scheme, replacing long-lived bearer credentials with short-lived session cookies and a separately scoped refresh mechanism.

Registration associates a browser-generated public key with the session. Refresh requires a signed challenge, reducing the usefulness of copying session credentials to another device. The ASP.NET Core implementation supplies registration and refresh handlers, derived cookie schemes, and policy-based forwarding.

For ASP.NET Core Identity, the integration must target the actual application cookie scheme. Lock demonstrates constructing AuthenticationBuilder when Identity's helpers hide the usual authentication-builder chain. HTTPS is required, and server logs help inspect exchanges that are not shown in the normal browser network view.

The package remains experimental even when .NET 11 reaches general availability, according to the article. HoneyDrunk relevance: prototype cookie-theft resistance with explicit browser and authentication-flow validation, preserving normal sign-in, sign-out, and fallback behavior.
