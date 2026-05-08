---
source: "https://developers.googleblog.com/building-real-world-on-device-ai-with-litert-and-npu/"
title: "Building real-world on-device AI with LiteRT and NPU"
author: "Google Developers Blog"
date_published: "unknown"
date_clipped: "2026-05-07"
category: "AI / LLM Research & Tooling"
source_type: "rss"
---

# Building real-world on-device AI with LiteRT and NPU

Source: https://developers.googleblog.com/building-real-world-on-device-ai-with-litert-and-npu/

Building real-world on-device AI with LiteRT and NPU
- Google Developers Blog
{
"@context": "https://schema.org",
"@type": "BreadcrumbList",
"itemListElement": [{
"@type": "ListItem",
"position": 1,
"name": "Google for Developers Blog",
"item": "https://developers.googleblog.com/"
},{
"@type": "ListItem",
"position": 2,
"name": "Building real-world on-device AI with LiteRT and NPU",
"item": "https://developers.googleblog.com/building-real-world-on-device-ai-with-litert-and-npu/"
}]
}
{
"@context": "https://schema.org",
"@type": "Article",
"headline": "Building real-world on-device AI with LiteRT and NPU",
"description": "LiteRT is a production-ready framework designed to help mobile developers unlock the power of Neural Processing Units (NPUs), overcoming the performance and battery limitations of traditional CPU or GPU processing. By providing a unified API that abstracts away hardware complexities, it allows industry leaders like Google Meet and Epic Games to deploy sophisticated AI models for real-time video, animation, and speech recognition with significantly higher efficiency. The platform further supports developers through benchmarking tools and cross-platform compatibility, enabling seamless AI deployment across mobile devices, AI PCs, and industrial IoT hardware.",
"image": "https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Gemini_Generated_Image_ignk8signk8.2e16d0ba.fill-800x400.png",
"datePublished": "2026-04-23",
"author": [
{ "@type": "Person", "name": "Chintan Parikh", "url": "/search/?author=Chintan+Parikh" },
{ "@type": "Person", "name": "Shuangfeng Li", "url": "/search/?author=Shuangfeng+Li" },
{ "@type": "Person", "name": "Weiyi Wang", "url": "/search/?author=Weiyi+Wang" },
{ "@type": "Person", "name": "Gerardo Carranza", "url": "/search/?author=Gerardo+Carranza" }
]
}
Products
Develop 
Android
Chrome
ChromeOS
Cloud
Firebase
Flutter
Google Assistant
Google Maps Platform
Google Workspace
TensorFlow
YouTube
Grow 
Firebase
Google Ads
Google Analytics
Google Play
Search
Web Push and Notification APIs
Earn 
AdMob
Google Ads API
Google Pay
Google Play Billing
Interactive Media Ads
Solutions
Events
Learn
Community
Groups 
Google Developer Groups
Google Developer Student Clubs
Woman Techmakers
Google Developer Experts
Tech Equity Collective
Programs 
Accelerator
Solution Challenge
DevFest
Stories 
All Stories
Developer Program
Blog
Search
Products
More
Solutions
Events
Learn
Community
More
Developer Program
Blog
Develop
Android
Chrome
ChromeOS
Cloud
Firebase
Flutter
Google Assistant
Google Maps Platform
Google Workspace
TensorFlow
YouTube
Grow
Firebase
Google Ads
Google Analytics
Google Play
Search
Web Push and Notification APIs
Earn
AdMob
Google Ads API
Google Pay
Google Play Billing
Interactive Media Ads
Groups
Google Developer Groups
Google Developer Student Clubs
Woman Techmakers
Google Developer Experts
Tech Equity Collective
Programs
Accelerator
Solution Challenge
DevFest
Stories
All Stories
Building real-world on-device AI with LiteRT and NPU 
APRIL 23, 2026 
Chintan Parikh 
Product Manager 
Shuangfeng Li 
Software Engineer 
Weiyi Wang 
Software Engineer 
Gerardo Carranza 
Software Engineer 
Share 
Facebook 
Twitter 
LinkedIn 
Mail 
Users benefit from instant AI features like real-time video effects, ASR, and motion capture in their mobile apps. However, for developers, running sophisticated models on-device often comes with balancing unique challenges related to managing device thermals, preserving battery life, and preventing frame drops. To deliver fast, responsive AI experiences without compromising performance, LiteRT unlocks Neural Processing Units (NPUs) , the hardware specifically built for these workloads.
LiteRT is a cross-platform production-ready framework for on-device AI, offering CPU, GPU, and NPU acceleration across mobile, desktop, and IoT platforms. Designed for performance and scalability, LiteRT simplifies the deployment of high-speed AI features, through a unified API. This abstracts the complexity of integrating with multiple NPU SDKs, allowing developers to target diverse silicon without writing vendor-specific code.
Translating NPU performance into meaningful experiences LiteRT is already hardened across Google products, popular apps, and even SDKs. Utilized by industry leaders including Google Meet, Epic Games, and Argmax Inc. here is what NPU acceleration looks like in real-world production apps.
Google Meet : By leveraging the mobile NPU, Google Meet successfully deployed an Ultra-HD segmentation model 25x larger than previous versions - without sacrificing inference speed. Crucially, it maintains a consistent power footprint, creating thermal headroom necessary to deliver higher-quality background replacement throughout a typical 20-30 min session.
Sorry, your browser doesn't support playback for this video
Epic Games, Inc : High-fidelity, real-time animation experiences demand exceptional efficiency. Epic’s Live Link Face (Beta) app for Android enables creators to capture performances from a single camera, then generate and stream real-time MetaHuman facial animation directly from their devices into Unreal Engine.
Real-time facial solving is computationally intensive and requires consistently low latency. By using LiteRT on the NPU, Epic unlocks dedicated on-device acceleration on supported Android devices, enabling up to 30 FPS performance for real-time MetaHuman animation.
Sorry, your browser doesn't support playback for this video
Real-time MetaHuman facial animation in Unreal Engine with NPU 
Argmax Inc recently launched the Argmax Pro SDK for Android for on-device speech recognition in collaboration with LiteRT. By utilizing LiteRT and AI Pack feature delivery via Google Play, Argmax was able to bring its top-tier accuracy and real-time speed while respecting app size constraints on Android. Crucially, they leveraged LiteRT's Ahead-Of-Time (AOT) compilation to eliminate costly on-device compilation steps, enabling frontier speech models like NVIDIA Parakeet TDT 0.6B v2 to run with industry-leading latency.
Performance testing across Google Tensor, MediaTek and Qualcomm Technologies SoCs, Argmax Pro SDK showed that upgrading from GPU to NPU delivers over 2x speedup . Beyond the speedups, the power efficiency of NPUs enabled Argmax SDK Enterprise customers like Heidi Health to conduct reliable on-device live transcription for extended sessions while mitigating impact to battery life. Finally, by offloading runtime libraries and models to on-demand downloads via Play's AI Packs, the device dynamically obtains the model that's optimized for the specific NPU.
Sorry, your browser doesn't support playback for this video
Argmax's Kotlin-first SDK brings top-tier accuracy and real-time speed to Android, with seamless NPU and GPU acceleration by Google LiteRT. 
Google AI Edge Gallery App : To help developers test and validate the performance of NPU acceleration, we are happy to announce that the Google AI Edge Gallery App now features NPU support for select Gemma models and built-in benchmarking tools. Available on Android , AI Edge Gallery lets you quickly see the true potential of AI performance on mobile hardware. Developers can also access the Google AI Edge Gallery on GitHub to build their own experiences.
Sorry, your browser doesn't support playback for this video
Explore various on-device LLM use cases with Google AI Edge Gallery 
Scaling performance across the hardware spectrum While the performance gains in speech, animation, and video are clear, the path to the NPU has historically been difficult to unlock for developers, due to various vendor-specific SDKs and complexities. By providing a streamlined workflow and cross platform support, LiteRT enables developers to deploy advanced models, from mobile phones to industrial IoT and AI PCs, without sacrificing performance or portability.
Cross-platform NPU support 
As highlighted in the recent Google AI Edge Gemma 4 blog post, LiteRT extends NPU acceleration beyond mobile, allowing you to deploy your models across a range of hardware using a single framework. For the industrial edge, LiteRT supports platforms like the Qualcomm Dragonwing ™ IQ8 Series , which also powers Arduino VENTUNO Q , enabling high-reliability use cases like robotics and smart manufacturing with models like Gemma 4 . For desktop, LiteRT is preparing for AI PCs through OpenVINO™ integration with Intel® Core™ Ultra series 2 and 3 processors, delivering significant power savings and responsiveness for local GenAI workloads.
Performance validation at scale 
Google AI Edge Portal provides a benchmark service across 100+ of the most popular mobile phones with insights on ML workloads across devices, accelerators and configurations. Developers can now make data-driven deployment decisions, such as whether to use AOT or JIT, that best suit their use cases and their target devices. To use the latest Portal NPU features, sign up for our private preview here .
Sorry, your browser doesn't support playback for this video
Google AI Edge Portal Benchmarking Results 
Get started with your NPU journey With our production-ready NPU integrations, LiteRT provides a unified workflow that abstracts away low-level complexities across both Just-In-Time (JIT) and Ahead-Of-Time (AOT) deployment.
Dive into our documentation and start your journey with NPU acceleration today.
Documentation: Explore the LiteRT & LiteRT-LM documentation for comprehensive development guides. GitHub repos : Visit LiteRT and LiteRT-LM GitHub repos for latest updates and implementation details. Samples : Check out the LiteRT-Samples GitHub repo for reference code. Use the AI Edge Gallery app as a starting point to build your own app. Models : Visit LiteRT Hugging Face Community for ready-to-use open models like Gemma 4 . We keep actively optimizing the open weight model family, ensuring that its architectural improvements are mapped directly to high-speed NPU kernels. You can access those models using LiteRT-LM CLI . More details in ‘Bring state-of-the-art agentic skills to the edge with Gemma 4.’ Google Tensor - Sign up for experimental access to Google Tensor ML SDK Let us know your feedback and feature requests by opening an issue on our GitHub channel . We can’t wait to see what you build!
Acknowledgements Google: Akshat Sharma, Alice Zheng, Andrew Zhang, Ashley Lin, Byungchul Kim, Changming Sun, Charlie Xu, Chenchen Tang, Chunlei Niu, Cormac Brick, Derek Bekebrede, Fabian Bergmark, Fengwu Yao, Gerardo Carranza, Gregory Karpiak, Jae Yoo, Jing Jin, Jingjiang Li, Julius Kammerl, Jun Jiang, Lu Wang, Maria Lyubimtseva, Mariana Quesada, Marissa Ikonomidis, Matt Kreileder, Matthias Grundmann, Meghna Johar, Na Li, Ping Yu, Renjie Wu, Rishika Sinha, Sachin Kotwani, Salil Tambe, Siargey Pisarchyk, Siargey Pisarchyk, Somdatta Banerjee, Steven Toribio, Suleman Shahid, Terry Heo, Wai Hon Law, Weiyi Wang, Xiaoming Hu 
Partners: Alen Huang, Ankit Kapoor, Arda Atahan Ibis, Atila Orhon, Brian Keene, Chen Cen, Cheng-Dao Lee. Cheng-Yen Lin, Chun-Hsueh Lee (Jack), Chun-Ting Lin (Graham), Code Lin, Deep Yap, Dylan Angus, Felix Baum, HungChun Liu, Jhih-Kuan Lin, Jiun-Kai Yang (Kelvin), Kedar Gharat, Ken Sieger, Laxmi Rayapudi, Lei Chen, Mike Tremaine, Ming-Che Lin (Vincent), Poyuan Jeng, MetaHuman Team, Vinesh Sukumar, Waimun Wong, Yi-Ru Chen, Yu-Ting Wan, Zach Nagengast 
posted in:
Mobile 
AI 
Case Studies 
Announcements 
Learn 
Explore 
Influence 
Previous 
Next 
Related Posts 
Mobile 
Web 
How-To Guides 
Announcements 
A2UI v0.9: The New Standard for Portable, Framework-Agnostic Generative UI
APRIL 17, 2026 
AI 
Cloud 
Tutorials 
Case Studies 
Supercharging LLM inference on Google TPUs: Achieving 3X speedups with diffusion-style speculative decoding
MAY 4, 2026 
AI 
Cloud 
Case Studies 
Best Practices 
Build Better AI Agents: 5 Developer Tips from the Agent Bake-Off
APRIL 14, 2026 
Pay 
Mobile 
Web 
Tutorials 
Announcements 
New enhancements for merchant initiated transactions with the Google Pay API
APRIL 15, 2026 
Connect
Blog
Bluesky
Instagram
LinkedIn
X (Twitter)
YouTube
Programs
Google Developer Program
Google Developer Groups
Google Developer Experts
Accelerators
Women Techmakers
Google Cloud & NVIDIA
Developer consoles
Google API Console
Google Cloud Platform Console
Google Play Console
Firebase Console
Actions on Google Console
Cast SDK Developer Console
Chrome Web Store Dashboard
Google Home Developer Console
Android
Chrome
Firebase
Google Cloud Platform
All products
Manage cookies
Terms
Privacy
