---
source: https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications
title: 'CEP to UXP: Creative Cloud Plugin Migration Timeline'
author: Aubrey Cattell
date_published: '2026-09-24'
date_clipped: '2026-10-04'
category: Technical Art & Creator Tools
source_type: web
capture_method: full-readable-extraction
---

# CEP to UXP: Creative Cloud Plugin Migration Timeline

Source: https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications

# Investing in the Future of Creative Cloud Extensibility: UXP Comes to Our Flagship Applications


**Adobe is bringing UXP to additional flagship apps (After Effects, Illustrator, and Media Encoder), and formalizing a multi-year, phased transition away from CEP.**

UXP (Unified Extensibility Platform), first introduced in 2018, is already the foundation for production third-party plugins in [Photoshop](https://developer.adobe.com/photoshop/uxp/2022/), [InDesign](https://developer.adobe.com/indesign/uxp/), and [Premiere](https://developer.adobe.com/premiere-pro/uxp/), and a public beta now live in [Media Encoder](https://community.adobe.com/announcements-509/uxp-now-available-in-adobe-media-encoder-beta-1641441).

Today we’re taking the next step, the culmination of years of platform investment: extending UXP to our remaining flagship apps, After Effects and Illustrator, and formalizing a multi-year phased transition away from CEP, the legacy platform UXP replaces.

CEP’s technology has fallen behind: It depends on third-party components that are no longer actively maintained, and on Apple Silicon it still runs Photoshop through Rosetta 2 translation, a bridge Apple plans to retire in 2027. CEP no longer works reliably, and we will retire it at the end of 2029. If you have CEP-based plugins in production, now is the time to start moving them to UXP.

UXP uses a different security and architectural model than CEP. Migrations may require adopting UXP-supported patterns rather than a 1:1 port, and Webview and Hybrid plugins help bridge cases where the architectures differ today. The bottom line, though, is this: UXP supports the workflows you rely on, while being on a more modern, secure, and capable platform.

## What this means for you, including key milestones

This transition applies to Creative Cloud desktop flagship apps only; Acrobat, Adobe Express, and Lightroom aren’t affected. With respect to specific applications:

**Media Encoder:**Public beta UXP plugins now live.**Premiere:**GA UXP plugins + Hybrid plugins available.**After Effects:**Public beta UXP plugins by November 2026.**InDesign:**UXP plugins have been available since 2023; GA Hybrid plugins in Summer 2027.**Illustrator:**Public beta UXP plugins by Spring 2027.**Photoshop:**UXP plugins have been available since 2020, and the Adobe Marketplace will stop accepting new CEP plugin submissions starting March 2027.

Additional details:

- Every flagship app gets a guaranteed
**minimum**of two years from its UXP public beta before CEP is removed from new versions of that app. - Starting December 2029, CEP will no longer be included in these apps. Until then, existing plugins already in the Adobe Marketplace will continue to work and can still receive updates.
- ExtendScripts are not affected by this transition.

## March 2027 Photoshop milestone

Photoshop is the first app to reach a CEP transition milestone. Starting **March 2027**, the Adobe Marketplace will no longer accept new CEP plugin submissions for Photoshop.

Photoshop introduced UXP-powered extensibility to third-party developers six years ago, and most plugins are now built using UXP. Very few new CEP extensions have shipped for Photoshop in recent quarters.

### What this means:

- New CEP plugins for Photoshop can’t be submitted to the Marketplace after March 2027, but existing plugins can be updated.
- You can find UXP plugins (as well as CEP and C++ plugins) on both Adobe Exchange and in the Creative Cloud Desktop app.
- CEP plugins distributed outside the Marketplace are not affected by this milestone. Plugins can also be distributed on external marketplaces.
- CEP plugins will be disabled by default in Photoshop from December 2027.
- For new Photoshop plugin development, UXP is the path forward.

Other flagship apps follow their own timelines. Premiere stops accepting new CEP submissions in December 2027, and InDesign follows in January 2028. Both move to CEP-disabled-by-default in December 2028. After Effects, Illustrator, and Media Encoder stop accepting new CEP submissions and move to CEP-disabled-by-default together in December 2028 as well.

When CEP is disabled by default, users can easily turn it back on, but it’s the clearest signal yet that it’s time to move to UXP-powered workflows.

## What UXP offers

UXP is Adobe's modern extensibility platform, designed for the performance, security, and hardware reality of today's desktop environments. Unlike the legacy stack it replaces, UXP is built on current web standards and runs natively on today’s hardware.

### What developers get with UXP:

**Modern developer platform:**UXP lets developers use modern frameworks, technologies, and patterns. This increases developer capabilities and velocity, enabling richer, faster experiences for users.**Modern operating system support:**Full support for modern architectures, including Apple Silicon and Windows on ARM.**Deeper product integration:**UXP plugins integrate deeply with Creative Cloud host apps, enabling more consistent, native-feeling experiences for users.**Stronger security and user trust:**UXP's more rigorous security model creates a safer foundation for plugins, helping users feel confident in what they install.**Access to new product capabilities:**New capabilities across Creative Cloud apps are being added exclusively to UXP. Developers building on UXP gain access to features that will never be available to CEP, including future integrations across the Adobe ecosystem.**Proven maturity:**UXP already powers thousands of plugins in Photoshop, InDesign, and Premiere.

## Migration support

We know migrations take time, especially for complex plugins used in production workflows. That’s why every flagship app gets a guaranteed two-year window from its UXP public beta, and why we’re investing in the tooling, documentation, and direct support to help you use that time well:

- Detailed migration guides, API references, and supported patterns at
[developer.adobe.com/uxp](https://developer.adobe.com/uxp). - Hybrid plugins in flagship apps, which let developers bridge complex workflows.
- Direct support through the
[developer forums](https://forums.creativeclouddeveloper.com/). [Office hours and developer-facing sessions](https://developer.adobe.com/developers-live/)throughout this process.- Developer tooling, support, and funding for developers who are building tools that help others in the community create new UXP plugins or migrate from CEP.


## Get involved

Thank you for building with Adobe. Join us at [Adobe Developers Live](https://events.ringcentral.com/events/adobe-developers-live-2026-code-connect-build-whats-next/registration) on September 29 and 30 to hear more about this transition and ask the team your questions directly.
