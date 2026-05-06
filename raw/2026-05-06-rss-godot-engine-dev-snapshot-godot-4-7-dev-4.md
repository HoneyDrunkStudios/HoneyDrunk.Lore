---
source: "https://godotengine.org/article/dev-snapshot-godot-4-7-dev-4/"
title: "Dev snapshot: Godot 4.7 dev 4"
author: "Godot Engine"
date_published: "Thu, 09 Apr 2026 12:00:00 +0000"
date_clipped: "2026-05-06"
category: "Game Development / Unity"
source_type: "rss"
---

# Dev snapshot: Godot 4.7 dev 4

Source: https://godotengine.org/article/dev-snapshot-godot-4-7-dev-4/

As we edge ever closer to feature freeze, many of our contributors have been hard at work to get their highly-anticipated features in hopes of Godot 4.7 integration. Fortunately for them, we’ve managed to accomodate several of these proposals, and are excited to showcase them today! Your testing will be crucial to ensure that everything listed stays in scope for a 4.7 release, so be sure to give this latest build a spin after the highlights
Please consider supporting the project financially , if you are able. Godot is maintained by the efforts of volunteers and a small team of paid contributors. Your donations go towards sponsoring their work and ensuring they can dedicate their undivided attention to the needs of the project.
Jump to the Downloads section , and give it a spin right now, or continue reading to learn more about improvements in this release. You can also try the Web editor , the XR editor , or the Android editor for this release. If you are interested in the latter, please request to join our testing group to get access to pre-release builds.
The cover illustration is from Poke ALL Toads , a puzzle game starring mischievous fairies on a queat to poke ALL toads. You can buy the game on Steam , and follow the developer on Bluesky , YouTube , or itch.io . 
Highlights 
Rendering: Add nearest-neighbor scaling 
We’re starting things out with one of the most anticipated integrations for our rendering system: nearest-neighbor scaling for 3D viewports. Over the course of nearly three years, Hugo Locurcio has been refining GH-79731 to ensure that 3D titles with pixel-art aesthetics or lower resolution scaling will still look crisp without any compromise to performance:
Bilinear 
Nearest (new behavior) 
GUI: Add custom_maximum_size property to Control 
Our previous development snapshot had a large focus on GUI improvements, and that QOL continues with the new custom_maximum_size property for Control . Enzo Novoselic in GH-116640 has at last brought us the maximal equivalent to the existing custom_minimum_size , enabling the fine-tuning of GUI element sizes to their full potential.
GUI: Improve drag and drop in Tree 
vaner spear-headed GH-112993 in order to improve the overall usability and intuitiveness of Tree drag-and-drop functionality. Now when performing a drag-and-drop operation, there will be an always-present vertical indicator showing the potential parental chain, leveraging a standalone CanvasItem to prevent StyleBox occlusion.
Old 
New 
What’s more, this operation will now consider the x-position of the cursor while determining a to-be parent when in indent space (leftmost, empty space), whereas item space largely retains current behavior. This implementation mirrors what one would commonly find in vector design software.
Editor: Increase available space for array properties 
Have you ever wondered why the inspector takes up so much negative space when working with arrays? Turns out it wasn’t done deliberately; it just so happened to be using the default offset of 0.5! Tomasz Chabora rightfully found this quite silly, and whipped up GH-118008 to rectify this oversight.
Old 
New 
And more! 
There are too many exciting changes to list them all here, but here’s a curated selection:
2D: Rework TileSet editor proxy objects ( GH-117574 ). 
3D: Add vector components to 3D ruler tool ( GH-106785 ). 
Editor: Add folding to the Visual Profiler tree ( GH-118120 ). 
Editor: Add type filters to create dialog ( GH-111518 ). 
Editor: Hide renderer selector in main editor window and add editor setting ( GH-117754 ). 
Editor: Make right-clicking on unfocused scene tabs possible ( GH-112919 ). 
GDExtension: Allow viewing GDExtensions from inside project settings ( GH-118063 ). 
GDScript: LSP: Calculate simple string insertions on the server-side ( GH-117710 ). 
Particles: Fix angular velocity ( GH-117861 ).
NOTE: This is technically compatibility-breaking, but it’s bringing the functionality in-line with how its always been documented. 
Particles: Fix particles moving when timescale is 0 ( GH-109911 ). 
Platforms: Android: Allow implementing java interfaces from GDScript ( GH-115498 ). 
Platforms: Windows: Implement OneCore TTS support using C++/WinRT (no deps) ( GH-116349 ). 
Platforms: Windows: Use OneCore/WinRT emoji picker when available ( GH-116351 ). 
Changelog 
88 contributors submitted 188 fixes for this release. See our interactive changelog for the complete list of changes since 4.7-dev3 . You can also review all changes included in 4.7 compared to the previous 4.6 feature release .
This release is built from commit 755fa449c .
Downloads 
Download Godot 4.7 dev4
Linux
Standard
.NET
macOS
Standard
.NET
Windows
Standard
.NET
Export templates and other downloads
Make a Donation
.thankyou-wrapper {
position: fixed;
top: 0;
left: 0;
right: 0;
bottom: 0;
background: rgba(0, 0, 0, 0.85);
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
z-index: 10;
}
.thankyou {
background: var(--base-color);
box-shadow: var(--more-shadow);
padding: 30px;
display: flex;
flex-direction: column;
align-items: center;
text-align: center;
position: relative;
border-radius: 13px;
}
.thankyou-reading {
font-size: 16px;
}
.thankyou-reading-list {
font-size: 16px;
margin: 0;
margin-left: 48px;
padding-left: 0;
}
.thankyou-donate {
margin-bottom: 24px;
text-align: center;
}
.btn.btn-donate {
background-color: var(--primary-color);
color: hsla(0, 0%, 100%, 0.9);
font-size: 22px;
font-weight: 600;
margin-bottom: 26px;
}
.thankyou h2 {
text-shadow: var(--base-shadow);
font-size: 36px;
font-weight: 800;
margin-bottom: 12px;
}
.thankyou h2 .anchored-link {
/* Hiding the anchored text automatically added on blogposts */
display: none !important;
}
.thankyou p {
max-width: 620px;
font-size: 25px;
}
@media (max-width: 768px) {
.thankyou-wrapper {
display: block;
}
.thankyou {
position: absolute;
top: 0;
left: 0;
right: 0;
bottom: 0;
overflow: scroll;
padding: 30px 40px 18px 40px;
}
.thankyou-reading-list {
margin-left: 24px;
}
.btn-close-thankyou-popup {
width: 48px;
height: 48px;
display: flex;
justify-content: center;
align-items: center;
}
}
.btn-close-thankyou-popup {
cursor: pointer;
position: absolute;
top: 12px;
right: 12px;
}
.btn-close-thankyou-popup img {
background: transparent !important; /* for overwriting the style in the blogposts img */
}
@media (prefers-color-scheme: light) {
.btn-close-thankyou-popup img {
filter: invert(1);
opacity: 0.75;
}
}
document.addEventListener('DOMContentLoaded', () => {
const thankYouWrapper = document.getElementById('thank-you');
// Close itself, when clicked outside of the popup area.
thankYouWrapper.addEventListener('click', (e) => {
if (e.target === thankYouWrapper) {
thankYouWrapper.style.display = 'none';
}
});
// Close with a close button.
const thankYouBackButton = document.querySelector('.btn-close-thankyou-popup');
thankYouBackButton.addEventListener('click', () => {
thankYouWrapper.style.display = 'none';
});
// Open from the main download buttons.
const downloadButtons = document.querySelectorAll('.btn-download, .download-button');
downloadButtons.forEach((it) => {
if (it.dataset?.external === "yes") {
return;
}
it.addEventListener('click', () => {
thankYouWrapper.style.display = '';
document.querySelector('.btn.btn-donate').focus();
});
});
// Open from the all downloads list.
const downloadLinks = document.querySelectorAll('.download-link');
downloadLinks.forEach((it) => {
it.addEventListener('click', () => {
thankYouWrapper.style.display = '';
});
});
// Close the dialog when the user presses the escape key.
document.addEventListener('keydown', (e) => {
if (e.key === 'Escape') {
thankYouWrapper.style.display = 'none';
}
});
});
Godot is downloading... 
Godot exists thanks to donations from people like you. Help us continue our work:
Make a Donation
Standard build includes support for GDScript and GDExtension.
.NET build (marked as mono ) includes support for C#, as well as GDScript and GDExtension.
While engine maintainers try their best to ensure that each preview snapshot and release candidate is stable, this is by definition a pre-release piece of software . Be sure to make frequent backups, or use a version control system such as Git, to preserve your projects in case of corruption or data loss.
Known issues 
With every release we accept that there are going to be various issues, which have already been reported but haven’t been fixed yet. See the GitHub issue tracker for a complete list of known bugs .
There are currently no known issues introduced by this release.
Bug reports 
As a tester, we encourage you to open bug reports if you experience issues with this release. Please check the existing issues on GitHub first, using the search function with relevant keywords, to ensure that the bug you experience is not already known.
In particular, any change that would cause a regression in your projects is very important to report (e.g. if something that worked fine in previous 4.x releases, but no longer works in this snapshot).
Support 
Godot is a non-profit, open-source game engine developed by hundreds of contributors in their free time, as well as a handful of part and full-time developers hired thanks to generous donations from the Godot community . A big thank you to everyone who has contributed their time or their financial support to the project!
If you’d like to support the project financially and help us secure our future hires, you can do so using the Godot Development Fund platform managed by the Godot Foundation . There are also several alternative ways to donate which you may find more suitable.
Donate now
