---
source: "https://godotengine.org/article/release-candidate-godot-4-6-3-rc-2/"
title: "Release candidate: Godot 4.6.3 RC 2"
author: "Godot Engine"
date_published: "Sat, 16 May 2026 12:00:00 +0000"
date_clipped: "2026-05-19"
category: "Game Development / Unity"
source_type: "rss"
---

# Release candidate: Godot 4.6.3 RC 2

Source: https://godotengine.org/article/release-candidate-godot-4-6-3-rc-2/

We rarely opt for Saturday releases for these snapshots, as the majority of the team are already enjoying their weekend (hopefully you are as well!). However, we had some exciting new regression fixes for the upcoming 4.6.3 maintenance release, so we didn’t feel right just sitting on them. As such, we’re dropping the next release candidate now, so users can get their hands on it even earlier than usual!
Please consider supporting the project financially , if you are able. Godot is maintained by the efforts of volunteers and a small team of paid contributors. Your donations go towards sponsoring their work and ensuring they can dedicate their undivided attention to the needs of the project.
Jump to the Downloads section , and give it a spin right now, or continue reading to learn more about improvements in this release. You can also try the Web editor , the XR editor , or the Android editor for this release. If you are interested in the latter, please request to join our testing group to get access to pre-release builds.
The illustration picture for this article comes from The Greenening , a incremental game where you embark on a wholesome journey to explore and reawaken a forgotten world. You can buy the game on Steam , and follow the developer on YouTube or Bluesky . 
What’s new 
14 contributors submitted 21 improvements for this release. See our interactive changelog for the complete list of changes since 4.6.3 RC 1 . You can also review all changes included in 4.6.3 compared to the previous 4.6.2 maintenance release .
This section covers all changes made since 4.6.3 RC 1 , which are largely regression fixes:
3D: Fix 3D viewport selection getting stuck when editing a GridMap ( GH-117521 ). 
3D: Fix Marker3D editor gizmo being darker than intended for negative axis lines ( GH-116995 ). 
3D: Fix mouse wheel zoom scrolling contents in the GridMap editor ( GH-117378 ). 
3D: Fix problems with undoing selection and pasting in GridMap editor ( GH-116814 ). 
Animation: Fix compressed Pos3D track interpolation ( GH-118159 ). 
Editor: Avoid repeats in resource gather ( GH-118926 ). 
Editor: Fix and improve the editor layout dialog ( GH-117846 ). 
Editor: Fix blurry icons in the inspector dock’s object selector ( GH-115222 ). 
Editor: Fix FileSystem dock visual separation when docked at bottom ( GH-115267 ). 
Editor: Fix keying state not being updated for sub-inspectors ( GH-117673 ). 
Editor: Fix right clicking an item in filesystem ItemList draws focus ( GH-114968 ). 
Editor: Fix text alignment in check box inside EditorInspectorSection s ( GH-117683 ). 
Editor: Update the notification for Auto-exposure ( GH-114732 ). 
GDScript: Fix GDScript LSP test link errors when websocket is disabled ( GH-114951 ). 
GDScript: Pattern guard warning fix ( GH-110523 ). 
GUI: Fix RichTextLabel not updating after change scroll_active field ( GH-114467 ). 
GUI: Fix TextEdit IME error on mouse over ( GH-111859 ). 
Platforms: Fix clipboard history not updating on subsequent copies in Wayland ( GH-116648 ). 
Platforms: Wayland: Unify clipboard sending code ( GH-117873 ). 
Rendering: Add project setting to disable new Volumetric fog blending behavior ( GH-119414 ). 
Rendering: Fix LightmapGI probe update speed setting not applying in Compatibility ( GH-117771 ). 
This release is built from commit e880d6bbf .
Downloads 
Download Godot 4.6.3 rc2
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
During the Release Candidate stage, we focus exclusively on solving showstopping regressions (i.e. something that worked in a previous release is now broken, without workaround). You can have a look at our current list of regressions and significant issues which we aim to address before releasing 4.6.3. This list is dynamic and will be updated if we discover new showstopping issues after more users start testing the RC snapshots.
With every release we accept that there are going to be various issues, which have already been reported but haven’t been fixed yet. See the GitHub issue tracker for a complete list of known bugs .
Bug reports 
As a tester, we encourage you to open bug reports if you experience issues with this release. Please check the existing issues on GitHub first, using the search function with relevant keywords, to ensure that the bug you experience is not already known.
In particular, any change that would cause a regression in your projects is very important to report (e.g. if something that worked fine in previous 4.x releases, but no longer works in this snapshot).
Support 
Godot is a non-profit, open-source game engine developed by hundreds of contributors in their free time, as well as a handful of part and full-time developers hired thanks to generous donations from the Godot community . A big thank you to everyone who has contributed their time or their financial support to the project!
If you’d like to support the project financially and help us secure our future hires, you can do so using the Godot Development Fund .
Donate now
