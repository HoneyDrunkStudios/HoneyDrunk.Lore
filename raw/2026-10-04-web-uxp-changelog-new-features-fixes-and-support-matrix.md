---
source: https://blog.developer.adobe.com/en/publish/2026/07/uxp-changelog-and-support-matrix
title: 'UXP Changelog: New Features, Fixes, and Support Matrix'
author: Kasi Viswanathan K
date_published: '2026-07-29'
date_clipped: '2026-10-04'
category: Technical Art & Creator Tools
source_type: web
capture_method: full-readable-extraction
---

# UXP Changelog: New Features, Fixes, and Support Matrix

Source: https://blog.developer.adobe.com/en/publish/2026/07/uxp-changelog-and-support-matrix

# UXP Changelog and Product Support Matrix


Adobe's Unified eXtensibility Platform (UXP) continues to evolve with every release, bringing new capabilities, closer alignment with web standards, and important stability fixes to plugin developers across Adobe's creative applications.

This post pulls together the recent UXP changelog alongside a product support matrix, so you can see at a glance what changed in each version and which UXP release ships with each host application.

**UXP Changelog**

**UXP 9.4**

**New features/enhancements**

- Added
`queueMicrotask`

support, enabling newer JavaScript tooling and modern asynchronous patterns in plugins. - WebView navigation responses now expose HTTP status codes, enabling improved error handling for hosted content.
- Expanded CSS
`text-decoration`

support for greater compatibility with web standards. - Unhandled JavaScript exceptions in third-party plugins are now captured and reported to improve runtime diagnostics. It's an opt-in at the moment to enable some transition time. e.g. block in
`manifest.json`


```
{
"featureFlags": {
"uncaughtException": true,
"unhandledRejection": true
}
}
```


**Bug fixes**

- Fixed UNC path handling for WebView
`src`

, video`src`

, and video`poster`

attributes on Windows. - Fixed inconsistent dialog resize behavior across different content and size combinations.

**UXP 9.3**

**New features/enhancements**

- Added support for the video
`poster`

attribute (supported only on MacOS). Plugins can display a custom image before playback begins or while video content is loading. - Plugin command results are now stringified by default, preventing unexpected
`undefined`

return values. - Added support for
`file://`

URLs alongwith`#fragments`

via`shell.openPath()`

on macOS. Opening`file:///…/index.html#endnote-001`

now opens the default browser at the exact anchor on macOS, without requiring any page scroll. - Restricted the WebView
`uxpHost`

object to the main document. Embedded subframes no longer have access to plugin messaging APIs.

**Bug fixes**

- Prevented media
`timeUpdate`

events from being dispatched while the media player is not playing.

**UXP 9.2**

**New features/enhancements**

- System Sleep/Awake Events: introduced system sleep and wakeup events in the plugin JS layer for better control over features like video playback.
`window.addEventListener("sleep", () => { console.log("System is sleeping"); });`

`window.addEventListener("awake", () => { console.log("System is awake"); });`



**UXP 9.1**

**New features/enhancements**

- SystemVideo
`timeUpdate`

Event: the UXP video element now emits a`timeUpdate`

event like the HTML5 video element. - Video Element Audio Support: the UXP video element can now play audio files.
- URLSearchParams Module Support: added the
`URLSearchParams`

module to UXP. - WebView Drag & Drop Support: added drag and drop between UXP panels and WebView-based panels; WebView can accept drops of various data types from anywhere, bypassing UXP.
- Improved Image Loading: multiple views can load the same URL without triggering false error states or visible flicker.
- Enriched WebView load error messages:
`WebViewEvent.message`

now provides more detailed cause info for better debugging. - WebView improvements.
- Disabled swipe navigation on WebView2 for consistency with macOS WKWebView; all WebView2 gestures (Swipe, Zoom Control, Pinch Zoom) are now disabled.
- Removed the
`allow`

field from`permissions.webview`

config;`permissions.webview.allow`

in the manifest is no longer used.

**UXP 9.0**

**New features/enhancements**

- Webview enhancements
- WebView2 now uses Fluent overlay scrollbars for a modern UI experience
- requiredPermissions.webview.domains is now optional, simplifying manifest configuration

- SecureStorage methods now follow the Web Storage API spec for error handling
- XMLHttpRequest.readyState is exposed in
[XMLHttpRequest](https://developer.adobe.com/photoshop/uxp/2022/uxp-api/reference-js/global-members/data-transfers/xml-http-request)now for correctness

**UXP Product Support Matrix**

**UXP Version**

**Photoshop**

**Premiere**

**InDesign**

### 9.4.0

### —

### —

### —

### 9.3.0

### 27.7

### 26.3

### 21.4

### 9.2.1

### —

### 26.2

### 21.3

### 9.2.0

### 27.4

### —

### —

### 9.0.3

### —

### —

### 21

### 9.0.2

### 26.11

### —

### —

### 9.0.1

### 26.10

### —

### —

### 8.4.0

### 26.9

### —

### —

### 8.3.0

### 26.8

### —

### —

### 8.1.6

### —

### —

### 20.4

### 8.1.4

### 26.6.1

### —

### —

### 8.1.2

### 26.6

### —

### —

### 8.1.1

### 26.3

### —

### —

### 8.1.0.1

### 26.1

### —

### —

### 8.1.0

### 26

### 26.0.2

### —

### 8.0.1

### —

### —

### 20.2.1

## Accessing Beta and Prerelease Builds

New UXP versions become available when host applications integrate them into their beta and prerelease builds before general release. As each host application has its own release schedule, the availability of a new UXP version may vary across applications. When a host application integrates a newer UXP runtime, that version becomes available in both its public beta build and its prerelease program.

Beta builds are publicly available to all Creative Cloud users. In the Creative Cloud desktop app, go to Applications and click Beta in the top navigation bar. Here, you can select and install the beta builds you want. These are installed in parallel to the core product. As with release builds, the Creative Cloud desktop app will notify you when updates are available for any of the beta versions.

InDesign and Photoshop provide prerelease versions in addition to the beta versions. Prerelease builds are only available only under NDA and after you have joined the prerelease program. You can apply to join the [InDesign Developer Prerelease Program](https://www.adobeprerelease.com/beta/D1A76A97-F7DC-4552-DE3C-FF5F211C7492) on the prerelease site. Access to the Photoshop prerelease program is by invitation only. Prerelease programs have a separate NDA-protected forum where you can ask questions and provide feedback to the product team. InDesign's prerelease program even offers debug builds for developers.

**Stay in the Loop**

That covers the recent UXP updates and where each host application currently stands. Whether you're maintaining an existing plugin or building something new, we hope this reference makes it easier to target the right UXP version with confidence.

If you're just getting started, here are some resources to help you build with UXP:

[Documentation, APIs, and Developer Console](https://developer.adobe.com/creative-cloud/)[Developers Live Community Hub — including upcoming events and the Developers Blog](https://developer.adobe.com/developers-live)[Adobe Developers Community LinkedIn Group](https://www.linkedin.com/groups/12425244)[Get the latest news with our monthly newsletter](https://www.adobe.com/subscription/ccdevnewsletter.html)

Do you have questions about UXP or feedback on a specific release? Join the conversation on the [Creative Cloud Developer Forums](https://forums.creativeclouddeveloper.com/), where our team and the developer community are ready to help.
