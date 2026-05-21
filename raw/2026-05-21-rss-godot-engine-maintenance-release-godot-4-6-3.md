---
source: "https://godotengine.org/article/maintenance-release-godot-4-6-3/"
title: "Maintenance release: Godot 4.6.3"
author: "Godot Engine"
date_published: "Wed, 20 May 2026 12:00:00 +0000"
date_clipped: "2026-05-21"
category: "Game Development / Unity"
source_type: "rss"
---

# Maintenance release: Godot 4.6.3

Source: https://godotengine.org/article/maintenance-release-godot-4-6-3/

Progress on Godot 4.7 has continued without a hitch, but the need for more 4.6 maintenance releases remains ever-present. Our commitment to active support brings us to today’s release of Godot 4.6.3.
Maintenance releases are expected to be safe for an upgrade, but we recommend to always make backups, or use a version control system such as Git, to preserve your projects in case of corruption or data loss.
Please consider supporting the project financially , if you are able. Godot is maintained by the efforts of volunteers and a small team of paid contributors. Your donations go towards sponsoring their work and ensuring they can dedicate their undivided attention to the needs of the project.
Download Godot 4.6.3 now or try the online version of the Godot editor .
Download Godot 4.6.3 stable
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
The cover illustration is from The Adventures of Sir Kicksalot , a first-person action game where you can use an arsenal of kicking, weaponry, sorcery, stealth, and more kicking to cleverly defeat your foes. You can buy the game or try the demo on Steam , and follow the developer on itch.io . 
Changes 
41 contributors submitted 86 fixes for this release. See our interactive changelog for the complete list of changes since the 4.6.2-stable release .
This release is built from commit 35e80b3a8 .
2D: Update layer selector when modifying the TileMap in the inspector ( GH-117256 ). 
3D: Fix Marker3D editor gizmo being darker than intended for negative axis lines ( GH-116995 ). 
3D: Fix wrong rotation of cells while being pasted in the GridMap editor ( GH-116683 ). 
Animation: Fix SplineIK crash cases ( GH-117959 ). 
Buildsystem: Annual Android versions bump for 2026 ( GH-113761 ). 
C#: Prevent SourceGenerators from becoming a transitive dependency ( GH-114868 ). 
Core: Android: Fix the use of --main-pack in template builds ( GH-119495 ). 
Core: Debugger: Rather than looping infinitely on data read errors, drop the connection ( GH-113905 ). 
Core: Fix race in RefCounted::unreference() ( GH-118678 ). 
Core: Improve thread-safety of Object signals ( GH-117511 ). 
Editor: Avoid repeats in resource gather ( GH-118926 ). 
Editor: Don’t print UID errors when cache is not initialized ( GH-118527 ). 
Editor: Fix and improve the editor layout dialog ( GH-117846 ). 
Editor: Fix game speed UI not resetting when game is restarted (from editor) ( GH-116568 ). 
Export: iOS: Fix one-click deploy with Xcode 26 ( GH-118559 ). 
GUI: Fix TextEdit IME error on mouse over ( GH-111859 ). 
GUI: RTL: Fix character click offsets after the table ( GH-117011 ). 
Import: Copy scene unique ID when replacing imported instance ( GH-118522 ). 
Input: Android: Fix handling of back navigation when targeting API level 36 ( GH-117653 ). 
Input: Fix incorrect reading of joypad UTF8 raw_name in Input.get_joy_info() ( GH-115218 ). 
Physics: Fix over-removal of area overlaps when using Jolt ( GH-118285 ). 
Rendering: Add project setting to disable new Volumetric fog blending behavior ( GH-119414 ). 
Rendering: Fix GLES3 batching skipping rendering all items on specific buffer sizes ( GH-117725 ). 
Rendering: Fix LightmapGI probe update speed setting not applying in Compatibility ( GH-117771 ). 
Rendering: Select relevant 3D lights per mesh on GLES3 and Mobile renderers ( GH-107234 ). 
Known incompatibilities 
As of now, there are no known incompatibilities with the previous Godot 4.6.2 release. We encourage all users to upgrade to 4.6.3. 
If you experience any unexpected behavior change in your projects after upgrading to 4.6.3, please file an issue on GitHub .
Bug reports 
As a tester, we encourage you to open bug reports if you experience issues with this release. Please check the existing issues on GitHub first, using the search function with relevant keywords, to ensure that the bug you experience is not already known.
In particular, any change that would cause a regression in your projects is very important to report (e.g. if something that worked fine in previous 4.x releases, but no longer works in this snapshot).
Support 
Godot is a non-profit, open-source game engine developed by hundreds of contributors in their free time, as well as a handful of part and full-time developers hired thanks to generous donations from the Godot community . A big thank you to everyone who has contributed their time or their financial support to the project!
If you’d like to support the project financially and help us secure our future hires, you can do so using the Godot Development Fund platform managed by Godot Foundation . There are also several alternative ways to donate which you may find more suitable.
Donate now
