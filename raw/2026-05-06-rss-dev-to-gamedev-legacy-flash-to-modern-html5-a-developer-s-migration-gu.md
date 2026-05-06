---
source: "https://dev.to/oceanviewgames/legacy-flash-to-modern-html5-a-developers-migration-guide-4ik0"
title: "Legacy Flash to Modern HTML5: A Developer's Migration Guide"
author: "DEV.to Gamedev"
date_published: "Tue, 05 May 2026 19:46:07 +0000"
date_clipped: "2026-05-06"
category: "Game Development / Unity"
source_type: "rss"
---

# Legacy Flash to Modern HTML5: A Developer's Migration Guide

Source: https://dev.to/oceanviewgames/legacy-flash-to-modern-html5-a-developers-migration-guide-4ik0

try {
if(localStorage) {
let currentUser = localStorage.getItem('current_user');
if (currentUser) {
currentUser = JSON.parse(currentUser);
if (currentUser.id === 3759146) {
document.getElementById('article-show-container').classList.add('current-user-is-article-author');
}
}
}
} catch (e) {
console.error(e);
}
Ocean View Games 
Posted on May 5 
• Originally published at oceanviewgames.co.uk 
Legacy Flash to Modern HTML5: A Developer's Migration Guide
# gamedev 
# unity3d 
# programming 
Adobe Flash is dead. As of December 2020, all major browsers removed Flash support entirely. But thousands of Flash applications - educational tools, training simulations, interactive exhibits, and games - still have value. Their content is relevant. Their audiences still exist. Only their technology is obsolete.
During our founder's previous tenure at a development agency, we led the migration of The Great Fire of London - an educational game originally built for the Museum of London - from Flash to HTML5. The kicker? The original source code was lost. 
That project taught us a comprehensive methodology for Flash-to-HTML5 migration that we now apply through our legacy modernisation service . This guide covers the full process.
Step 1: Assess What You Have
Before writing any code, audit the Flash application thoroughly.
Source Code Available
If you have the original .fla files and ActionScript source:
Export the timeline as a frame-by-frame reference 
Catalogue all assets (vector graphics, bitmap images, audio files, fonts) 
Document the class structure and state machine 
Identify external dependencies (server calls, local storage, third-party libraries) 
Source Code Lost
If you only have the compiled .swf file (our situation with The Great Fire of London):
Use a SWF decompiler (JPEXS Free Flash Decompiler is the best open-source option) to extract assets and inspect bytecode 
Document every screen, interaction, and animation by playing through the application and recording video 
Build a behaviour specification - a document describing exactly what the application does, screen by screen, interaction by interaction 
Treat the compiled SWF as a "black box" reference implementation 
Key Takeaway: If source code is lost, the decompiled output is a reference, not a starting point. Attempting to directly port decompiled ActionScript to JavaScript produces unmaintainable code. Reverse-engineer the behaviour, then rewrite cleanly.
Step 2: Choose Your Target Technology
Flash applications vary enormously in complexity. The right HTML5 technology depends on what you are migrating.
Simple Interactive Content (Forms, Slideshows, Quizzes)
Plain HTML/CSS/JavaScript - no framework needed 
Keep it simple. These applications do not need a game engine. 
2D Games and Animations
Framework 
Best for 
Phaser 
The most popular HTML5 game framework. Excellent for 2D games with sprite-based graphics. 
PixiJS 
A 2D rendering engine without the game-specific features. Good if you want more control. 
Canvas API 
For simpler animations where a framework is overkill. 
Complex Interactive Applications
Option 
Details 
TypeScript + Phaser 
Our choice for The Great Fire of London. TypeScript provides the type safety that makes large codebases maintainable. 
Unity WebGL 
If the application is complex enough to warrant a full engine, Unity exports to WebGL. However, the download size is significantly larger. 
For most Flash migrations, Phaser + TypeScript is the sweet spot. It is lightweight, well-documented, and maps naturally to Flash's display list model.
Step 3: Extract and Optimise Assets
Flash assets need transformation for the web.
Vector Graphics
Flash's vector format does not translate directly to web standards. Options:
Export to SVG - preserves scalability. Good for UI elements and icons. 
Rasterise to PNG/WebP - simpler but loses scalability. Acceptable for game sprites at fixed resolutions. 
Recreate in code - for simple shapes, drawing them with Canvas or SVG paths produces smaller files than exporting bitmaps. 
For The Great Fire of London, we extracted the original vector assets and converted them to optimised sprite sheets. This reduced the total asset download size and draw calls compared to rendering individual vectors.
Audio
Flash commonly used proprietary audio formats. Convert to:
Format 
Notes 
MP3 
Universal browser support 
OGG 
Better compression, supported in most browsers (with MP3 fallback for Safari) 
WebM 
For longer audio tracks where file size matters 
Fonts
Flash applications often embed fonts that may not have web licences. Verify licensing before converting to WOFF2 format. If the original font is unlicensed for web use, find a visually similar alternative.
Step 4: Rebuild the Logic
This is the core of the migration. Do not port line-by-line. Rewrite.
Why Rewriting Beats Porting
ActionScript and JavaScript share a common ancestor (ECMAScript), which makes line-by-line porting tempting. Resist this temptation. Flash code was written for Flash's execution model:
Flash has a frame-based timeline that JavaScript does not 
Flash's display list model differs from the DOM and Canvas 
Flash's event model differs from browser events 
ActionScript 2 and 3 have different class systems, neither of which maps cleanly to modern JavaScript/TypeScript 
A direct port carries over Flash-era patterns that produce slow, fragile web code.
Our Approach
Work from the behaviour specification (Step 1), not the source code 
Build a clean TypeScript architecture using modern patterns 
Implement each screen/interaction as an independent module 
Test each module against the original Flash application for behavioural parity 
For The Great Fire of London, we catalogued every interaction, animation timing, and win-state condition from the Flash version, then wrote modern TypeScript to replicate these behaviours exactly.
Step 5: Modernise the UI for Responsive Screens
Flash applications were built for fixed resolutions - typically 800x600 or 1024x768 in a 4:3 aspect ratio. Modern devices range from 320px-wide phones to 2560px-wide monitors in 16:9 or taller.
Responsive Layout Strategy
Decouple UI from the game world. In Flash, UI elements were often placed at absolute pixel positions on the stage. In HTML5, anchor UI elements to screen edges and corners. 
Use relative units - percentages and viewport units instead of fixed pixels 
Design breakpoints - define how the layout adapts at phone, tablet, and desktop widths 
Test on real devices - responsive design that looks correct in Chrome DevTools sometimes breaks on actual hardware 
For The Great Fire of London, we re-engineered the layout from 4:3 CRT to responsive 16:9, ensuring the game worked on Chromebooks (the primary hardware in UK classrooms) as well as iPads and desktop browsers.
Touch Support
Flash applications assumed mouse input. Add:
Touch event handlers alongside mouse events 
Larger tap targets (minimum 44x44 points) 
Gesture support where appropriate (pinch-to-zoom for maps, swipe for navigation) 
Step 6: Optimise for Target Hardware
Flash applications ran in a browser plugin with its own runtime. HTML5 runs in the browser's JavaScript engine, which has different performance characteristics.
Common Performance Pitfalls
Pitfall 
Solution 
DOM manipulation in animation loops 
Use Canvas or WebGL for rendering, not DOM elements 
Unoptimised sprite sheets 
Pack sprites into atlases to reduce HTTP requests and draw calls 
Memory leaks 
Flash's garbage collector was aggressive. JavaScript's is not. Explicitly clean up references to prevent memory growth over long sessions. 
Audio latency 
Use the Web Audio API, not HTML5 <audio> elements, for low-latency game audio 
School Hardware Considerations
Educational Flash migrations often target school hardware - Chromebooks, aging Windows desktops, and shared iPads. This hardware is significantly less powerful than consumer devices.
For The Great Fire of London, we optimised specifically for:
Chromebooks with 2-4GB RAM and integrated graphics 
Slow school Wi-Fi with high latency and packet loss 
Shared devices where browser cache may be cleared between sessions 
This meant aggressive asset compression, minimal JavaScript bundle size, and no assumptions about hardware acceleration.
Key Takeaway: Your target hardware defines your performance budget. Educational migrations target the weakest devices in a school's inventory, not the newest.
Step 7: Test for Parity
The final step is verifying that the HTML5 version behaves identically to the original Flash version. For educational content, this is critical - teachers have lesson plans built around specific interactions.
Our testing protocol:
Side-by-side comparison - run the Flash version (via a standalone Flash Player) alongside the HTML5 version 
Interaction audit - verify every clickable element, animation, and state transition 
Timing verification - ensure animations play at the same speed (Flash used frame-based timing; HTML5 uses time-based) 
Edge case testing - rapid clicking, window resizing, tab switching, network interruption 
Accessibility review - add keyboard navigation and screen reader support that the Flash version lacked 
Timeline and Cost Expectations
A Flash-to-HTML5 migration typically takes:
Project type 
Typical timeline 
Simple interactive content 
2-4 weeks 
2D game with moderate complexity 
6-12 weeks 
Complex application with lost source code 
12-20 weeks 
The primary cost drivers are: whether source code exists, the number of unique screens/interactions, and the target device range.
Related Reading
Great Fire of London Case Study - Our reverse-engineering rescue mission 
Legacy Modernisation Services - How we approach legacy migrations 
Fire of London Project Page - The finished product 
Educational Game Development Services - Our approach to serious games and educational content. 
Top comments (0) 
Subscribe 
Personal 
Trusted User 
Create template
Templates let you quickly answer FAQs or store snippets for re-use.
Submit 
Preview 
Dismiss 
Code of Conduct 
• 
Report abuse 
Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink .
Hide child comments as well
Confirm
For further actions, you may consider blocking this person and/or reporting abuse
