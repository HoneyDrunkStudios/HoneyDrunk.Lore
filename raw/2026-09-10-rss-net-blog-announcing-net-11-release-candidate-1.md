---
source: "https://devblogs.microsoft.com/dotnet/dotnet-11-rc-1/"
title: "Announcing .NET 11 Release Candidate 1"
author: ".NET Team"
date_published: "2026-09-08"
date_clipped: "2026-09-10"
category: ".NET Ecosystem"
source_type: "rss"
---

# Announcing .NET 11 Release Candidate 1

Source: https://devblogs.microsoft.com/dotnet/dotnet-11-rc-1/

.NET 11 Release Candidate 1 is now available. This is our first release
candidate, which comes with a
go-live support license
so you can confidently use this release for your production applications. This
release of .NET 11 is supported in the new
Visual Studio 2026 Insiders release alongside
Visual Studio Code with the C# Dev Kit. Check out the full release notes below
and get started today.
Download .NET 11 RC1
This release contains the following highlights and improvements.
📚Libraries
Signal processes and inspect termination status
Experimental caller-driven TLS sessions
DNS record resolution on Linux
JSON support for new numeric types and binary schemas
JSON closed-type polymorphism and union support
Async options validation
Construct BitArray values from spans
Reuse compression encoders and decoders
TLS channel binding on Unix
Faster authenticated encryption on Apple platforms
AES Key Wrap support
Breaking changes
Bug fixes
Community contributors
Full Release Notes
⏱️Runtime
In-process crash reporting on Unix
Half operations use FP16 hardware instructions
Full Release Notes
🛠️ SDK
dotnet test improves mobile application testing
dotnet test adds run-level controls and result layouts
Container publishing produces reproducible images and skips redundant uploads
File-based programs add Native AOT reuse and formatting support
dotnet format limits configuration discovery to included files
Additional CLI improvements
Full Release Notes
🧱 MSBuild
Create and extract tar archives
Expose item glob patterns to build tooling
Full Release Notes
📦 NuGet
Pack reuses existing project evaluations
Vulnerable package updates work with warnings as errors
Full Release Notes
C#
C# 15 stabilizes unions and other language features
Unsafe Evolution refinements
Full Release Notes
F#
Record spreads
Record constructors
Direct delegate construction
Efficient interpolated strings
Reflection-free record and union formatting
Full Release Notes
🌐 ASP.NET Core
SignalR authentication refresh APIs are finalized
SignalR TypeScript client supports authentication refresh
Blazor Server circuits update after authentication refresh
OpenAPI reflects obsolete APIs
Select an environment for build-time OpenAPI
Negotiate authentication uses TLS channel binding
Experimental Blazor AI components for agentic user interfaces
Full Release Notes
📱 .NET MAUI
Testing
Controls
Platform features
XAML
.NET for Android
Apple platforms (.NET for iOS, Mac Catalyst, macOS, tvOS)
Full Release Notes
🖥️ Windows Forms
Manage kiosk-style experiences
Modern visual styles stabilize for RC 1
Full Release Notes
🚀 Get started
To get started with .NET 11,
install the .NET 11 SDK .
If you’re on Windows, we recommend installing the latest version of
Visual Studio 2026 Insiders .
You can also use Visual Studio Code and the
C# Dev Kit
extension with .NET 11.
📦 Join a .NET community standup
Join us each week and engage with the developers and product managers behind
.NET for
community standups .
📢 .NET 11 Discussions
The team has been making release announcements alongside full
release notes
on the
dotnet/core GitHub Discussions .
🔔 Stay up-to-date with .NET 11
You can stay up-to-date with all the features of .NET 11 with:
What’s new in .NET 11
What’s new in C# 15
What’s new in ASP.NET Core
What’s new in Entity Framework Core
Breaking Changes in .NET 11
.NET 11 Releases
