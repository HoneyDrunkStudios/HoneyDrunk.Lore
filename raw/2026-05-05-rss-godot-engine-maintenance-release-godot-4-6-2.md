---
source: "https://godotengine.org/article/maintenance-release-godot-4-6-2/"
title: "Maintenance release: Godot 4.6.2"
author: "Godot Engine"
date_published: "Wed, 01 Apr 2026 12:00:00 +0000"
date_clipped: "2026-05-05"
category: "Game Development / Unity"
source_type: "rss"
---

# Maintenance release: Godot 4.6.2

Source: https://godotengine.org/article/maintenance-release-godot-4-6-2/

While the majority of our team continues to focus on development snapshots for Godot 4.7 , we still have a commitment to maintenance releases for the latest stable version. Specifically, our release support policy promises active support until the successor’s first patch release, so there’s still room for yet more maintenance releases in the future. As for now, we’d like to thank everyone who took the time to evaluate and ratify our release candidates for Godot 4.6.2.
Maintenance releases are expected to be safe for an upgrade, but we recommend to always make backups, or use a version control system such as Git, to preserve your projects in case of corruption or data loss.
Please consider supporting the project financially , if you are able. Godot is maintained by the efforts of volunteers and a small team of paid contributors. Your donations go towards sponsoring their work and ensuring they can dedicate their undivided attention to the needs of the project.
Download Godot 4.6.2 now or try the online version of the Godot editor .
Download Godot 4.6.2 stable
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
The cover illustration is from Bombun , a wholesome 3D platformer where you guide Bombun, a bomb-throwing bunny, on a mission to defend her floating fortress from a friend-turned-foe. You can buy the game on Steam , and follow the developer on Bluesky or itch.io . 
Changes 
61 contributors submitted 122 fixes for this release. See our interactive changelog for the complete list of changes since the 4.6.1-stable release .
3D: Fix 3D focus selection for subgizmos ( GH-116972 ). 
3D: Fix DirectionalLight3D property list ( GH-117189 ). 
Animation: Check playback_queue existance after emit animation_finished signal ( GH-116676 ). 
Animation: Deselect bezier keyframes when switching animations ( GH-116953 ). 
Animation: Fix timeline cursor following mouse during marker selection ( GH-117634 ). 
Animation: Fix visual shift of animation editor keys during selection ( GH-117290 ). 
Core: Fix String::split_ crash on empty string ( GH-117353 ). 
Core: Fix editable children state when duplicating instantiated nodes ( GH-117041 ). 
Core: RingBuffer: Fix T read() method reading empty buffer ( GH-117388 ). 
Core: RingBuffer: Fix overreading on methods that take an offset as an argument ( GH-117151 ). 
Editor: Fix build profile generator creating bogus profiles ( GH-115410 ). 
Editor: Fix mute button after pausing and stopping ( GH-116537 ). 
Editor: Fix theme item inspector tooltips for Window subclasses ( GH-115245 ). 
Editor: Set accessibility name on Tree inline cell editor when editing ( GH-117135 ). 
Editor: Stop autocomplete from eating words by default ( GH-117464 ). 
Export: Android Editor: Copy keystore to temp file during export ( GH-116161 ). 
GDExtension: Add missing GDVIRTUAL_BIND(_get_supported_extensions) on MovieWriter ( GH-117479 ). 
GUI: Fix “Custom” anchor preset being ignored if the parent isn’t a Control ( GH-117488 ). 
GUI: Fix RichTextLabel drag selection not working after double-click ( GH-117201 ). 
GUI: TextEdit: Fix clipping of last character due to right margin rounding ( GH-116850 ). 
GUI: TextServer: Ignore language of embedded object replacement spans when updating line breaks ( GH-116197 ). 
Import: Blender attempts should be incremented to avoid endless loop ( GH-116589 ). 
Physics: Jolt Physics: Make MoveKinematic more accurate when rotating a body by a very small angle ( GH-115327 ). 
Physics: Jolt Physics: Rework how gravity is applied to dynamic bodies to prevent energy increase on elastic collisions ( GH-115305 ). 
Physics: Jolt Physics: Swapping vertices of triangle if it is scaled inside out ( GH-115089 ). 
Platforms: Android: Fix FileAccess crash when using treeUri in Gradle-built apps ( GH-117131 ). 
Platforms: Fix macOS Steam time tracking lost when opening a project ( GH-117335 ). 
Platforms: iOS: Add UIScene lifecycle events ( GH-116395 ). 
Platforms: iOS: Propagate VC UI preferences to SwiftUI hosting controller ( GH-116633 ). 
Platforms: macOS: Enable wake for events if Magnet is running ( GH-116524 ). 
Platforms: Wayland: Improve mapping robustness and synchronization ( GH-117385 ). 
Platforms: Windows: Set current driver when ANGLE init fails ( GH-117253 ). 
Rendering: Apply fixed size properly for mono/stereo rendering ( GH-115147 ). 
Rendering: Fix accidental write-combined memory reads in canvas renderer ( GH-115757 ). 
Rendering: Fix Tangent decoding detection when computing vertex skinning ( GH-117401 ). 
Rendering: Fix viewport debanding not working with spatial scalers ( GH-114890 ). 
Rendering: macOS: Force ANGLE (GL over Metal) when running in VM ( GH-117371 ). 
This release is built from commit 001aa128b .
Known incompatibilities 
As of now, there are no known incompatibilities with the previous Godot 4.6.1 release. We encourage all users to upgrade to 4.6.2. 
If you experience any unexpected behavior change in your projects after upgrading to 4.6.2, please file an issue on GitHub .
Bug reports 
As a tester, we encourage you to open bug reports if you experience issues with this release. Please check the existing issues on GitHub first, using the search function with relevant keywords, to ensure that the bug you experience is not already known.
In particular, any change that would cause a regression in your projects is very important to report (e.g. if something that worked fine in previous 4.x releases, but no longer works in this snapshot).
Support 
Godot is a non-profit, open-source game engine developed by hundreds of contributors on their free time, as well as a handful of part and full-time developers hired thanks to generous donations from the Godot community . A big thank you to everyone who has contributed their time or their financial support to the project!
If you’d like to support the project financially and help us secure our future hires, you can do so using the Godot Development Fund .
Donate now
