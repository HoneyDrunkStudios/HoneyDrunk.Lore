---
source: "https://godotengine.org/article/dev-snapshot-godot-4-7-beta-2/"
title: "Dev snapshot: Godot 4.7 beta 2"
author: "Godot Engine"
date_published: "Mon, 11 May 2026 12:00:00 +0000"
date_clipped: "2026-05-12"
category: "Game Development / Unity"
source_type: "rss"
---

# Dev snapshot: Godot 4.7 beta 2

Source: https://godotengine.org/article/dev-snapshot-godot-4-7-beta-2/

It’s been a couple of weeks since we saw the release of 4.7 beta 1 , and in that time we’ve managed to detect and resolve over 100 regressions! There’s still plenty of work to be done on the testing front, so users are encouraged to report whatever new issues crop up this newest release: Godot 4.7 beta 2.
Please consider supporting the project financially , if you are able. Godot is maintained by the efforts of volunteers and a small team of paid contributors. Your donations go towards sponsoring their work and ensuring they can dedicate their undivided attention to the needs of the project.
Jump to the Downloads section , and give it a spin right now, or continue reading to learn more about improvements in this release. You can also try the Web editor , the XR editor , or the Android editor for this release. If you are interested in the latter, please request to join our testing group to get access to pre-release builds.
The cover illustration is from Wax Heads , a cozy-punk narrative sim where you work in a struggling record store and chat to quirky customers with unique tastes. You can buy the game on Steam , and check out the developers— Rocío Tomé and Murray Somerwolff —on Bluesky! 
Highlights 
For an overview of what’s new overall in Godot 4.7, have a look at the highlights for 4.7 beta 1 , which cover a lot of the changes. This blog post only covers the changes between beta 1 and beta 2. This section covers the most relevant changes made since the beta 1 snapshot, which are largely regression fixes:
3D: Add undo/redo support for Pilot Mode camera movement ( GH-119349 ). 
Animation: Rename various signal parameters called ‘name’ ( GH-119316 ). 
Core: Fix a race in ResourceLoader::load_threaded_request() ( GH-118824 ). 
Documentation: Link to tutorial and add platform notes to HDR output docs ( GH-118692 ). 
Editor: Fix editor screenshots with HDR enabled ( GH-119013 ). 
Editor: Improve ‘Clear Output’ button position ( GH-118954 ). 
Export: Remove experimental warning from Use Gradle Build option on Android ( GH-119172 ). 
GDExtension: Deprecate GDExtension’s object_cast_to and classdb_get_class_tag , in favour of is_class casts ( GH-119254 ). 
GUI: Make internal children of built-in nodes use their parent’s material ( GH-115637 ). 
Rendering: Fix behavior of window_is_hdr_output_supported for Wayland and adjust warnings ( GH-117913 ). 
Rendering: HDR: Implement checking if surface supports HDR output ( GH-119091 ). 
XR: Update default OpenXR action map ( GH-118975 ). 
Changelog 
74 contributors submitted 153 fixes for this release. See our interactive changelog for the complete list of changes since 4.7-beta1 . You can also review all changes included in 4.7 compared to the previous 4.6 feature release .
This release is built from commit 777579205 .
Downloads 
Download Godot 4.7 beta2
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
During the beta stage, we focus on solving both regressions (i.e. something that worked in a previous release is now broken) and significant new bugs introduced by new features. You can have a look at our current list of regressions and significant issues which we aim to address before releasing 4.7. This list is dynamic and will be updated if we discover new showstopping issues after more users start testing the beta snapshots.
With every release, we accept that there are going to be various issues which have already been reported but haven’t been fixed yet. See the GitHub issue tracker for a complete list of known bugs .
XR: The Godot editor will crash upon quitting a XR project on macOS ( GH-119146 ). 
GUI: Popup menu tooltips don’t show up when the search bar is enabled ( GH-119407 ). 
Bug reports 
As a tester, we encourage you to open bug reports if you experience issues with this release. Please check the existing issues on GitHub first, using the search function with relevant keywords, to ensure that the bug you experience is not already known.
In particular, any change that would cause a regression in your projects is very important to report (e.g. if something that worked fine in previous 4.x releases, but no longer works in this snapshot).
Support 
Godot is a non-profit, open-source game engine developed by hundreds of contributors in their free time, as well as a handful of part and full-time developers hired thanks to generous donations from the Godot community . A big thank you to everyone who has contributed their time or their financial support to the project!
If you’d like to support the project financially and help us secure our future hires, you can do so using the Godot Development Fund platform managed by Godot Foundation . There are also several alternative ways to donate which you may find more suitable.
Donate now
