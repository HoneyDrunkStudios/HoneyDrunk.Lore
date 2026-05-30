---
source: "https://unity.com/topics/render-pipelines-strategy-for-2026"
title: "Render Pipelines strategy for 2026"
author: "Unity"
date_published: "unknown"
date_clipped: "2026-05-30"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Render Pipelines strategy for 2026

Source: https://unity.com/topics/render-pipelines-strategy-for-2026

Render Pipelines strategy for 2026 Advancing URP Maintaining HDRP and supporting Nintendo Switch™ 2 Deprecating the Built-In Render Pipeline Conclusion We want to share where our focus is when it comes to Unity’s render pipelines. This is a topic we know is on a lot of your minds, and one we discussed extensively with many of you, including at Unite Barcelona. We’ve heard your feedback about the complexity that comes from fragmented options, and we’re making some key changes in 2026 to simplify things and focus our efforts where they can make the biggest impact for you.
Advancing the Universal Render Pipeline (URP) to enable developers to rapidly innovate, prototype, and bring to market any game of any genre with high performance across every platform. We are concentrating our efforts to bring forward even faster performance, build time, enhanced stability and extensibility, as well as new beautiful 3D lighting runtime capabilities for dynamic and procedural worlds. Maintaining the High Definition Render Pipeline (HDRP), focusing only on expanding platform reach with Nintendo Switch™ 2 support and stability . We want to ensure that developers who leverage HDRP have a clear path to reach new players. Starting the official Built-In Render Pipeline deprecation process in 6.5 , to simplify our product, enable our ecosystem to focus on our latest technologies moving forward, and accelerate our focus on URP. The Built-In Render Pipeline will still be available at least through Unity 6.7 LTS (due at the end of the year) to support studios with live games, but we strictly do not recommend it for any new titles. The final removal version is not yet decided and will depend on your feedback. Advancing URP 
URP is the render pipeline used for the vast majority of Unity games released in the past three years. It is the most flexible, and allows studios to target any genre on any platform from 2D to 3D and mobile, XR to the latest consoles. Our new strategy aims to make as much space as possible for URP to progress faster than ever before.
We are continuing to bring more performance and build time optimizations, improve its extensibility even further, and address issues to the highest quality standards.
We are heavily investing in enhancing its visual capabilities to cover genres requiring dynamic 3D content and dynamic lighting conditions on the widest range of platforms. This will include physical light units support, pre and auto exposure, physical sky and dynamic sky manager, real-time global illumination (see a sneak peek demo at the end of this presentation ), screen space reflections, on-tile post-processing for mobile devices, and more.
While we bring these new features, we want to make sure that they don’t significantly impact build time, build size, and overall performance if one does not need them, while making sure that they are designed with scalability and extensibility in mind.
Preview of dynamic diffuse Global Illumination and Screen Space Reflections in URP Maintaining HDRP and supporting Nintendo Switch™ 2 
HDRP is already feature-rich , enabling you to achieve high quality visuals without having to invest your time implementing common rendering features. These tools power many successful and beautiful games like Harold Halibut , ProjectZ: Beyond Order , V Rising , PGA Tour 2K25 , Node: The Last Favor of the Antarii , Into the Dead: Our Darkest Days , and many more, as well as many industrial applications like archviz, configurators or simulators like VirtaMed .
While no new features are planned for HDRP , we are actively working to bring HDRP support to Nintendo Switch™ 2 in 2026. This will allow HDRP games to reach a wider audience and showcase the power of this new platform leveraging a feature set optimized around GPU compute capabilities. We are actively validating on internal and selected external projects at the moment, and we will release official HDRP support to Nintendo Switch™ 2 for all Nintendo developers in 6.5 .
Going forward, we are focusing maintenance of HDRP on stability, regressions, and critical issues of widely used functionalities while we continue to accelerate URP's feature set and capabilities.
For more information on HDRP support for Nintendo Switch™ 2, refer to the Nintendo Developer Portal for enrolled developers.
Deprecating the Built-In Render Pipeline 
To reduce our graphics engine fragmentation, simplify onboarding, allow our ecosystem to focus entirely on our default technologies, and lower maintenance costs for everyone, we are starting the process of officially deprecating the Built-In Render Pipeline.
First we are marking the Built-In Render Pipeline as deprecated in Unity 6.5 . This means that we strongly encourage using URP when starting any new project, and converting all education and Asset Store content to be compatible by default with URP.
For existing live games using the Built-In Render Pipeline, we encourage you to start looking into porting your project to Scriptable Render Pipelines.
While a removal date has not yet been decided , we can guarantee that the Built-In Render Pipeline will continue to be available in the Unity 6.7 LTS version. This means that you will be covered with official Built-In Render Pipeline support at least until the end of 2028 (and 2029 with Unity Enterprise or Unity Industry licenses ) . 
It is our firm intention to remove availability of the Built-In Render Pipeline in the future, but before we decide for a final end date, we want to hear from you .
If you are interested in migrating your project from the Built-In Render Pipeline, we have multiple resources ready for you:
Documentation: Migrating from the Built-In Render Pipeline to URP Documentation: Render pipeline feature comparison Webinar: Best practices for migrating from the Built-in Render Pipeline to URP Talk at Unite 2024: Transitioning from the Built-in Render Pipeline to URP and HDRP Conclusion 
What this all boils down to is making your life easier. You shouldn't have to make a big, complex decision about a render pipeline before you even get started. We want you to be able to focus on what really matters: shipping innovative games. This change will make it easier to get the visuals you're after on all the platforms you want to target - even with dynamic lighting - and it will help ensure that Asset Store content works right out of the box.
As always, thank you for being a part of this community. Keep the questions and feedback coming.
To provide feedback, refer to our Discussions post on Render Pipelines strategy for 2026 .
To know more about all Scriptable Render Pipelines and tooling improvements in Unity 6:
Graphics rendering: Getting the best performance with Unity 6 | Unite 2024 Graphics rendering: Getting the best performance with Unity 6.1 | GDC 2025 Glow up your graphics with Unity 6.3LTS and beyond | Unite 2025 Achieve your vision faster with technical artist tools in Unity 6 | Unite 2024 Making it shine: Advanced visual techniques in Unity | Unite 2025 
‎‎‎‎‎‎
Nintendo Switch is a trademark of Nintendo.
