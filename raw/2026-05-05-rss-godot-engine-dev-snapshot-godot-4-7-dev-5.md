---
source: "https://godotengine.org/article/dev-snapshot-godot-4-7-dev-5/"
title: "Dev snapshot: Godot 4.7 dev 5"
author: "Godot Engine"
date_published: "Fri, 17 Apr 2026 12:00:00 +0000"
date_clipped: "2026-05-05"
category: "Game Development / Unity"
source_type: "rss"
---

# Dev snapshot: Godot 4.7 dev 5

Source: https://godotengine.org/article/dev-snapshot-godot-4-7-dev-5/

As is tradition at this point: feature freeze arrived, and so too did countless last-minute pull requests from contributors. So despite the previous development snapshot releasing just one week ago, there’s no shortage of brand-new goodies ready to be experienced firsthand!
Please consider supporting the project financially , if you are able. Godot is maintained by the efforts of volunteers and a small team of paid contributors. Your donations go towards sponsoring their work and ensuring they can dedicate their undivided attention to the needs of the project.
Jump to the Downloads section , and give it a spin right now, or continue reading to learn more about improvements in this release. You can also try the Web editor , the XR editor , or the Android editor for this release. If you are interested in the latter, please request to join our testing group to get access to pre-release builds.
The cover illustration is from Lost Wiki: Kozlovka , a detective game where you explore a Wikipedia-esque database to solve a small-town mystery in 90s Eastern Europe. You can buy the game on Steam , and follow the developer on Bluesky , YouTube , or itch.io . 
Highlights 
Assetlib: Port asset store to new API 
Did you know we have an overhaul to our asset store in the works? Well… Now you do! Michael Alexsander has been hard at work bringing our current system into this new paradigm, culminating in GH-112992 fully supporting the new API. While we hope to showcase details on this new system in the future, for now we’ll simply highlight the more obvious improvements that this PR delivers.
Starting with the main selection screen, the way we display our asset items has been polished. Not only will it be easier to parse the asset items themselves, but more metadata and the current rating will be readily visible.
When accessing an asset in isolation, you’ll have immediate access to the current description and all existing changelogs. What’s more, the ability to change an asset’s version is now just one click away.
Editor: Rework export template dialog to allow individual templates 
A long-standing pain point for anyone that’s worked with export templates has been that they must be downloaded in bulk. This was in contrast to how our editor downloads were always isolated, causing the export templates to incur long download times for a range of platforms that aren’t necessarily relevant to a developer’s intended export targets.
This could be solved in two main ways: overhauling our existing distribution system to make the packages available in isolation, or somehow repurposing the existing bulk distribution to only distribute a subset of options.
Despite how absurd it sounded, Tomasz Chabora managed to implement the latter! GH-117072 managed the seemingly-impossible task of hijacking the bulk package and retrieving slices of the developer’s choosing. This is all achieved within the Godot editor itself, making the process as seamless and expedient as possible for users.
GUI: Enable scaling images relative to font size in RichTextLabel 
Malcolm Anderson brings new life to [img] tags in RichTextLabel with GH-112617 . Now width and height can specify em for their scaling. This would result in the following text…
Do you have any [img height=1em]coin.png[/img] coins?
...I said, [font_size=50]DO YOU HAVE ANY [img height=1em]coin.png[/img] COINS??[/font_size]
…displaying like this:
Shaders: Implement inline text shader previews 
A long-awaited quality-of-life addition to the text shader editor comes courtesy of Yuri Rubinsky , with his PR GH-117726 bringing inline previews. This is a C++ implementation of Godot Shader Previewer , a popular addon written in GDScript by Cashew OldDew . Much like the addon before it, this aims to reduce the amount of guesswork when constucting text shaders, as now one can readily see the resulting effects within the text editor itself:
Rendering: Add rectangular area light source 
Rendering has received a lot of love in these snapshots, and we’re ending things off strong with Emil Dobetsberger ’s work in GH-108219 delivering rectangular area light sources. By leveraging the new AreaLight3D , it’s now possible to render real-time light from a rectangle in 3D space.
And more! 
There are too many exciting changes to list them all here, but here’s a curated selection:
3D: Add vertex snap support for subgizmo points ( GH-117922 ). 
Audio: Revamp audio bus UI ( GH-118266 ). 
Editor: Allow moving and resizing the embedded game window on Android ( GH-118417 ). 
Editor: Improve Remote/Local SceneTreeDock buttons’ appearance ( GH-118192 ). 
Export: Android: Add export options to customize splash screen ( GH-114671 ). 
GDExtension: Add Variant::get_type_by_name to GDExtension Interface ( GH-117160 ). 
Input: Wayland: Implement touch support ( GH-113886 ). 
Platforms: Change embedded window options to use three stacked dots and add HDR info ( GH-118079 ). 
Rendering: Refactor raytracing pipelines ( GH-118044 ). 
Changelog 
71 contributors submitted 135 fixes for this release. See our interactive changelog for the complete list of changes since 4.7-dev4 . You can also review all changes included in 4.7 compared to the previous 4.6 feature release .
This release is built from commit a8643700c .
Downloads 
Download Godot 4.7 dev5
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
