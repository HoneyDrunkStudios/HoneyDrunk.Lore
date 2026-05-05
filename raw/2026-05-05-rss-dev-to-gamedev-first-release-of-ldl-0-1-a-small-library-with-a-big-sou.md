---
source: "https://dev.to/jordancpp/first-release-of-ldl-01-a-small-library-with-a-big-soul-one-api-for-30-years-of-computer-history-g67"
title: "First Release of LDL 0.1 — A Small Library with a Big Soul. One API for 30 Years of Computer History"
author: "DEV.to Gamedev"
date_published: "Mon, 04 May 2026 17:29:32 +0000"
date_clipped: "2026-05-05"
category: "Game Development / Unity"
source_type: "rss"
---

# First Release of LDL 0.1 — A Small Library with a Big Soul. One API for 30 Years of Computer History

Source: https://dev.to/jordancpp/first-release-of-ldl-01-a-small-library-with-a-big-soul-one-api-for-30-years-of-computer-history-g67

try {
if(localStorage) {
let currentUser = localStorage.getItem('current_user');
if (currentUser) {
currentUser = JSON.parse(currentUser);
if (currentUser.id === 3753579) {
document.getElementById('article-show-container').classList.add('current-user-is-article-author');
}
}
}
} catch (e) {
console.error(e);
}
Evgeniy 
Posted on May 4 
First Release of LDL 0.1 — A Small Library with a Big Soul. One API for 30 Years of Computer History
# programming 
# c 
# linux 
# gamedev 
Hello, developers!
I'm excited to announce the first public release of the LDL library .
What is LDL?
LDL (Little Directmedia Layer) is more than just a cross-platform library — it's a bridge between different eras of software development . It lets you write code that runs just as well on Windows 95 as it does on Windows 11, on ancient Linux kernels as well as modern distributions, on FreeBSD 3.0 and the latest releases.
The library is written in pure C89 (ANSI C) , ensuring maximum portability — even to the most exotic compilers and platforms.
The Journey: From C++98 to C89
I originally wrote LDL in C++98 , which already provided good portability. But over time, I reconsidered my approach:
I switched entirely to C89 — this gives maximum compatibility with old compilers and platforms, including DOS, Windows 95, Solaris, and even PlayStation 1.
I abandoned the idea of releasing a full-featured 1.0 all at once — now releases are iterative :
First: windows, events, graphics ✅ 
Next: 2D renderer 🔜 
Then: audio and fonts 🔜 
This way, the project doesn't stall offline for years but grows gradually in front of the community.
Backends: Not a Replacement, but a Bridge
LDL doesn't try to replace SDL, SFML, or GLFW — it becomes a layer on top of them . Planned backends include:
SDL 1.2 
SDL 2.x 
SDL 3.x 
SFML 
GLFW 
This means you can build an LDL application on top of any of these libraries without changing a single line of code. The API stays the same; underneath, you can plug in any supported windowing and input system.
Why is this useful? 
If native support for a platform isn't ready yet, you can temporarily use a backend through an existing library. 
Developers already familiar with SDL or GLFW can try LDL without completely replacing their toolchain. 
You can leverage features from these libraries (like audio or fonts in SDL) earlier than they're implemented natively in LDL. 
Minimal Window Example
/*
* -----------------------------------------------------------------------------
* This example is in the public domain (CC0 1.0 Universal).
* You can copy, modify, use, and distribute it for any purpose.
* -----------------------------------------------------------------------------
*/ 
#include <LDL/LDL.h> 
int main ( void ) 
{ 
LDL_Result * result ; 
LDL_Context * context ; 
LDL_Window * window ; 
LDL_Event event ; 
result = LDL_ResultNew (); 
context = LDL_ContextNew ( LDL_ContextOpenGL1 ); 
window = LDL_WindowNew ( result , context , 
LDL_GetVec2i ( 0 , 0 ), 
LDL_GetVec2i ( 800 , 600 ), 
"LDL - Simple Window" , 
LDL_WindowModeResized ); 
if ( LDL_ResultIsOk ( result )) 
{ 
while ( LDL_WindowIsRunning ( window )) 
{ 
while ( LDL_WindowGetEvent ( window , & event )) 
{ 
if ( event . Type == LDL_EventIsQuit || 
LDL_EventIsKeyPressed ( & event , LDL_KeyEscape )) 
{ 
LDL_WindowStopEvent ( window ); 
} 
} 
LDL_WindowPresent ( window ); 
LDL_Delay ( 16 ); 
} 
LDL_WindowFree ( window ); 
LDL_ContextFree ( context ); 
LDL_ResultFree ( result ); 
} 
if ( LDL_ResultIsFail ( result )) 
{ 
printf ( "Error: %s \n " , LDL_ResultGetMessage ( result )); 
} 
return 0 ; 
} 
Enter fullscreen mode 
Exit fullscreen mode 
Features in Current Version (0.1)
Feature 
Support 
Windowing 
✅ Create, resize, close 
Events 
✅ Keyboard, mouse, resize, focus 
Keyboard 
✅ Full key mapping 
Mouse 
✅ Movement, clicks, scroll wheel 
OpenGL 1.0–4.6 
✅ From immediate mode to compute shaders 
Supported Platforms
OS 
Versions 
Windows 
95, 98, ME, 2000, XP, Vista, 7, 8, 10, 11 
Linux 
Kernel 2.0 – 6.x (1996–present) 
FreeBSD 
3.0 – 14.x (1998–present) 
Build & Install
# Install dependencies (Debian/Ubuntu) 
sudo apt-get install libx11-dev libgl1-mesa-dev
# Clone and build 
git clone https://github.com/JordanCpp/LDL.git
cd LDL
cmake -B build
cmake --build build
Enter fullscreen mode 
Exit fullscreen mode 
Roadmap: Version 0.2
The next major goal is adding a unified 2D renderer — a single interface for drawing sprites, lines, rectangles, and text that works identically on any hardware .
The developer doesn't need to think about what's under the hood: modern Vulkan, legacy OpenGL, or just a CPU with no GPU. LDL automatically selects the optimal backend. 
On modern systems → Vulkan or OpenGL with hardware acceleration 
On retro hardware → software rasterizer 
Same code. Same visual result. Everywhere. 
Planned 2D API Features:
Sprite loading and drawing 
Position, rotation, scale 
Color effects and transparency 
Line and rectangle drawing 
Text rendering with fonts 
Goal: Code written with LDL should live for decades — from '90s consoles and retro PCs to ultra-modern workstations — without rewrites or surprises.
Philosophy: The Charm of Old Hardware
"We stand on the shoulders of giants whose names we often forget, but whose work continues to shape our world every day." 
LDL is an attempt to preserve the connection between generations of developers. It doesn't try to replace existing solutions (like SDL or GLFW) — it complements them, providing a unified API for platforms that usually get left behind.
LDL isn't just a library. It's an attempt to preserve that special feeling of working with technology from the past:
The flicker of a CRT monitor 
The warmth of a fanless CPU working hard on every clock cycle 
How '90s engineers squeezed the impossible out of kilobytes of memory and megahertz of clock speed 
Today we have terabytes and teraflops, but we've lost something important — the art of doing more with less . LDL brings that approach back. Every line of the library is written with the thought that it might run on a Pentium 66 MHz with 8 MB of RAM .
Why Does This Matter?
Because modern software lives 3–5 years . We throw away working hardware not because it's broken, but because software has become too heavy and lazy.
LDL is a protest against planned obsolescence. It's code that doesn't require hardware upgrades every three years.
One codebase. Thirty years of computer history. And the charm felt by those who remember when programming was a true art of survival within constraints.
Screenshots
OpenGL 1.2 Examples
3D Atom Model 
Animated 3D Terrain 
Rotate 
Terrain Flight 
Water Wave Simulation 
OpenGL 2.1 Examples
Textured Terrain 
Solar System 
OpenGL 3.3 Examples
Animated Water Surface 
Rotating Cube 
Textured Sphere 
License
Component 
License 
LDL Library 
LGPLv3 
Example Code 
CC0 1.0 (Public Domain) 
GitHub: github.com/JordanCpp/LDL 
One API. One Codebase. Thirty Years of Computing History. 🚀
Top comments (1) 
Subscribe 
Personal 
Trusted User 
Create template
Templates let you quickly answer FAQs or store snippets for re-use.
Submit 
Preview 
Dismiss 
Collapse 
Expand 
PEACEBINFLOW
PEACEBINFLOW
PEACEBINFLOW
Follow 
Founder of SAGEWORKS AI — building the Web4 layer where AI, blockchain & time flow as one. Creator of Mind’s Eye and BinFlow. Engineering the future of temporal, network-native intelligence.
Email
peacethabibinflow@proton.me 
Location
BOTSWANA MAUN
Pronouns
he
Work
Founder & System Architect at SAGEWORKS AI
Joined
Oct 31, 2025 
• 
May 5
Dropdown menu 
Copy link 
Hide
There's something quietly radical about picking C89 not as a stylistic preference but as a time-travel mechanism. Most "portable" libraries target a spread of modern OSes and call it done — Linux, macOS, Windows, maybe a BSD if you're thorough. But targeting compiler dialects as your portability axis instead of platforms flips the problem on its head. It means your code's shelf life isn't tied to how fast APIs deprecate, but to how slowly the C standards committee moves, which is... actually a much more stable foundation.
The thing I'm turning over in my head is the backend-as-bridge architecture. Usually abstraction layers abstract downward — they hide platform details behind a uniform API. But LDL is abstracting sideways onto other abstraction layers. SDL already abstracts Win32 and X11 and Cocoa. So LDL-on-SDL becomes an abstraction on an abstraction, and normally that's a warning sign — the kind of thing that leads to leaky corners and impedance mismatches. But in this case, it seems intentional and maybe even clever: SDL becomes just another "platform" to target, same as raw Xlib or Win32 would be.
What I wonder about is where the friction shows up. When you're targeting SDL 1.2 on a Pentium running Windows 95 versus native Win32 on the same machine, do the two paths feel identical, or does the backend flavor leak through? Event ordering quirks, subtle timing differences, that kind of thing. A game loop from 1998 probably cares about that more than a modern one does.
The 2D renderer on a software rasterizer path is what'll really test the philosophy — when "same visual result" has to hold up between Vulkan on a 4090 and a CPU-only fallback on a machine with no GPU at all. That's a hard promise. Do you plan to pixel-match, or is it more of a perceptual equivalence you're aiming for?
Like comment: 
Like comment: 
1  like 
Like
Comment button 
Reply 
Code of Conduct 
• 
Report abuse 
Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink .
Hide child comments as well
Confirm
For further actions, you may consider blocking this person and/or reporting abuse
