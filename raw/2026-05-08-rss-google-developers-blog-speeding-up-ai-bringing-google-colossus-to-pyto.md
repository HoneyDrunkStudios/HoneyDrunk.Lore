---
source: "https://developers.googleblog.com/speeding-up-ai-bringing-google-colossus-to-pytorch-via-gcsfs-and-rapid-bucket/"
title: "Speeding Up AI: Bringing Google Colossus to PyTorch via GCSFS and Rapid Bucket"
author: "Google Developers Blog"
date_published: "unknown"
date_clipped: "2026-05-08"
category: "AI / LLM Research & Tooling"
source_type: "rss"
---

# Speeding Up AI: Bringing Google Colossus to PyTorch via GCSFS and Rapid Bucket

Source: https://developers.googleblog.com/speeding-up-ai-bringing-google-colossus-to-pytorch-via-gcsfs-and-rapid-bucket/

Speeding Up AI: Bringing Google Colossus to PyTorch via GCSFS and Rapid Bucket
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
"name": "Speeding Up AI: Bringing Google Colossus to PyTorch via GCSFS and Rapid Bucket",
"item": "https://developers.googleblog.com/speeding-up-ai-bringing-google-colossus-to-pytorch-via-gcsfs-and-rapid-bucket/"
}]
}
{
"@context": "https://schema.org",
"@type": "Article",
"headline": "Speeding Up AI: Bringing Google Colossus to PyTorch via GCSFS and Rapid Bucket",
"description": "Google Cloud has introduced a high-performance integration that connects Rapid Storage directly to PyTorch via the fsspec interface to eliminate AI training bottlenecks. By utilizing Google’s Colossus architecture and bidirectional gRPC streaming, the solution offers up to 15 TiB/s aggregate throughput and significant reductions in latency. These improvements allow developers to speed up total training time by 23% with zero code changes required beyond updating the storage bucket type.",
"image": "https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/image_2_1.2e16d0ba.fill-800x400.png",
"datePublished": "2026-04-29",
"author": [
{ "@type": "Person", "name": "Trinadh Kotturu", "url": "/search/?author=Trinadh+Kotturu" },
{ "@type": "Person", "name": "Martin Durant", "url": "/search/?author=Martin+Durant" }
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
Cloud 
Speeding Up AI: Bringing Google Colossus to PyTorch via GCSFS and Rapid Bucket 
APRIL 29, 2026 
Trinadh Kotturu 
Senior Product Manager 
Martin Durant 
fsspec maintainer, Anaconda, Inc 
Share 
Facebook 
Twitter 
LinkedIn 
Mail 
Today, we are announcing a major performance boost for AI/ML workloads using the PyTorch ecosystem on Google Cloud. By integrating Rapid Storage, powered by Google’s Colossus storage architecture, directly with PyTorch via the industry-standard fsspec interface, we are enabling researchers and developers to keep their GPUs busier than ever before.
The challenge: Keeping GPUs fed As model sizes grow, data loading and checkpointing often become the primary bottlenecks in training. Data preparation activities to train models involve fetching and processing terabytes and petabytes of data from remote storage mechanisms like object storage. Standard REST-based storage access can struggle to meet the extreme throughput and low-latency requirements of modern distributed training, wasting valuable GPU resources.
Rapid Bucket: Rapid Storage via bi-di gRPC Our new Rapid Bucket solution provides high-performance object storage in dedicated zonal buckets. By bypassing legacy REST APIs and utilizing persistent gRPC bidirectional streams, we’ve brought the power of Colossus, filesystem stateful protocols that power YouTube and Google Search, directly to the PyTorch ecosystem.
Key performance metrics of Rapid Storage Extreme Throughput: 15+ TiB/s aggregate throughput. Ultra-Low Latency: <1ms for random reads and append writes. High QPS: Rapid Bucket provides 20M+ QPS. Fsspec - PyTorch’s Pythonic file interface fsspec is the pervasive Pythonic interface for file systems in the PyTorch ecosystem. It is already used for:
Data preparation: Dask, Pandas, Hugging Face Datasets, Ray Data Checkpoints: PyTorch Lightning, Torch.dist, Weights & Biases Inference: vLLM 
There are various backend implementations of fsspec for many different storage systems, which can all be integrated under a single layer, eliminating the need to write specific code for each backend. By integrating Rapid Storage with gcsfs (the Google Cloud Storage implementation of fsspec), developers can leverage speed gains provided by Rapid with a simple fsspec.open() call — no complex code rewrites required.
Under the hood: Leveraging Colossus To achieve a performance boost with Rapid Buckets, we optimized the entire data path:
Stateful grpc-based streaming: gRPC bi-directional streaming keeps the connection alive, minimizing per-operation overhead like connection setup, auth, metadata etc., and enabling efficient, stateful data exchange for multiple reads or appends within a single object. Direct path: Google Cloud Storage(GCS) Rapid Bucket uses direct connectivity for its gRPC bi-directional streaming APIs (BidiReadObject, BidiWriteObject) to achieve maximum performance by connecting clients directly to underlying Colossus files. Non-Rapid traffic to GCS would typically have more network hops than direct paths, making read/write latencies over Rapid significantly lower. For more details, see Rapid storage internal working. Zonal co-location: By placing storage in the same zone as your compute (e.g., us-central1-a ), we eliminate cross-zone latency. Prior to Rapid buckets, data in a regional bucket and compute(accelerators) can be in different zones and access the data induced latency. No-Op User Migration: Preserved the existing fsspec API while entirely upgrading internal traffic from HTTP to BiDi-gRPC for Rapid buckets. By adding bucket-type auto-detection to gcsfs, PyTorch and other fsspec clients transparently utilize Rapid with zero manual configuration. Results A dataset of 134M rows totaling around 451GB was loaded onto 16 GKE nodes, each containing eight A4 GPUs. Training was conducted in 100 steps, with a checkpoint after every 25 steps using PyTorch Lightning. We benchmarked the performance of total training time, including the data load times, and we observed a performance gain of 23% using Rapid Bucket compared with Standard regional bucket. 
Microbenchmarking — that is, measuring the performance of a building block like I/O or resource usage — confirms these gains. Throughput improved by 4.8x for reads (both sequential and random) and 2.8x for writes. These tests used 16MB IO sizes across 48 processes. You can find more details at GCSFS-performance-benchmarks .
Get started Getting started with GCSFS on Rapid Bucket is easy. Your existing code and scripts remain the same. You just need to change the bucket to a Rapid Bucket to take advantage of the performance boost.
To install: 
Rapid Bucket integration is available from version 2026.3.0. 
pip install gcsfs 
Python
Copied 
Code sample to read/write from GCS Rapid: 
import gcsfs
# Initialize the filesystem
fs = gcsfs.GCSFileSystem()
# Writing to a Rapid bucket
with fs.open('my-zonal-rapid-bucket/data/checkpoint.pt', 'wb') as f:
f.write(b"model data...")
# Appending to an existing object (Native Rapid feature)
with fs.open('my-zonal-rapid-bucket/data/checkpoint.pt', 'ab') as f:
f.write(b"appended data...") 
Python
Copied 
posted in:
Cloud 
Cloud 
Announcements 
Explore 
Explore 
Influence 
PyTorch 
GCS 
fsspec 
Rapid 
AIML 
Previous 
Next 
Related Posts 
Mobile 
AI 
Case Studies 
Announcements 
Building real-world on-device AI with LiteRT and NPU
APRIL 23, 2026 
AI 
Cloud 
Tutorials 
Case Studies 
Supercharging LLM inference on Google TPUs: Achieving 3X speedups with diffusion-style speculative decoding
MAY 4, 2026 
AI 
Cloud 
Announcements 
Agents CLI in Agent Platform: create to production in one CLI
APRIL 22, 2026 
Cloud 
Firebase 
Mobile 
Web 
Announcements 
Advancing agentic AI development with Firebase Studio
JULY 10, 2025 
Cloud 
AI 
Industry Trends 
Solutions 
Stanford’s Marin foundation model: The first fully open model developed using JAX
JULY 16, 2025 
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
