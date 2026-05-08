---
source: "https://developers.googleblog.com/maxtext-expands-post-training-capabilities-introducing-sft-and-rl-on-single-host-tpus/"
title: "MaxText Expands Post-Training Capabilities: Introducing SFT and RL on Single-Host TPUs"
author: "Google Developers Blog"
date_published: "unknown"
date_clipped: "2026-05-08"
category: "AI / LLM Research & Tooling"
source_type: "rss"
---

# MaxText Expands Post-Training Capabilities: Introducing SFT and RL on Single-Host TPUs

Source: https://developers.googleblog.com/maxtext-expands-post-training-capabilities-introducing-sft-and-rl-on-single-host-tpus/

MaxText Expands Post-Training Capabilities: Introducing SFT and RL on Single-Host TPUs
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
"name": "MaxText Expands Post-Training Capabilities: Introducing SFT and RL on Single-Host TPUs",
"item": "https://developers.googleblog.com/maxtext-expands-post-training-capabilities-introducing-sft-and-rl-on-single-host-tpus/"
}]
}
{
"@context": "https://schema.org",
"@type": "Article",
"headline": "MaxText Expands Post-Training Capabilities: Introducing SFT and RL on Single-Host TPUs",
"description": "MaxText has introduced new support for Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) on single-host TPU configurations, leveraging JAX and the Tunix library for high-performance model refinement. These features enable developers to easily adapt pre-trained models for specialized tasks and complex reasoning using efficient algorithms like GRPO and GSPO. This update streamlines the post-training workflow, offering a scalable path from single-host setups to larger multi-host configurations.",
"image": "https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Building-1-banner_Tg8sqqU.2e16d0ba.fill-800x400.png",
"datePublished": "2026-04-16",
"author": [
{ "@type": "Person", "name": "Wei Wei", "url": "/search/?author=Wei+Wei" },
{ "@type": "Person", "name": "Weiren Yu", "url": "/search/?author=Weiren+Yu" }
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
MaxText Expands Post-Training Capabilities: Introducing SFT and RL on Single-Host TPUs 
APRIL 16, 2026 
Wei Wei 
Developer Advocate 
Weiren Yu 
Product Manager 
Share 
Facebook 
Twitter 
LinkedIn 
Mail 
In the rapidly evolving landscape of large language models (LLMs), pre-training is only the first step. To transform a base model into a specialized assistant or a high-performing reasoning engine, post-training is essential. Today, we are excited to announce new features in MaxText that streamline this process: Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) now available on single-host TPU configurations (such as v5p-8 and v6e-8).
By leveraging the power of JAX and the efficiency of the Tunix library, MaxText provides a high-performance, scalable path for developers to refine their models using the latest post-training techniques. You can explore the full documentation for SFT and RL to start your post-training journey on TPUs today.
Supervised Fine-Tuning (SFT): Precision Tuning Made Simple Supervised Fine-Tuning is the primary method for adapting a pre-trained model to follow specific instructions or excel at niche tasks. With the new single-host SFT support, users can now take an existing MaxText or Hugging Face checkpoint and fine-tune it on labeled datasets with minimal setup.
Key Highlights: 
Seamless Integration: Native support for Hugging Face datasets (e.g., ultrachat_200k). Flexible Checkpoints: Use existing MaxText checkpoints or convert Hugging Face models (like Gemma 3) directly within the ecosystem. Optimized Execution: Powered by Tunix, a JAX-based library specifically designed for post-training efficiency. 
Reinforcement Learning (RL): Advancing Reasoning Capabilities For tasks requiring complex logic and reasoning—such as math or coding—Reinforcement Learning is a game-changer. MaxText now supports several state-of-the-art RL algorithms on single-host TPUs, utilizing vLLM for high-throughput inference during the training loop. For example,
Group Relative Policy Optimization (GRPO) GRPO is a memory-efficient variant of PPO (Proximal Policy Optimization). It eliminates the need for a separate value function model, instead generating multiple responses per prompt and calculating relative advantages within the group. This significantly reduces the hardware footprint, making advanced RL accessible on a single TPU host. Group Sequence Policy Optimization (GSPO) GSPO focuses on sequence-level importance ratios and clipping. It improves training stability and efficiency by rewarding model behavior at the sequence level, making it particularly effective for enhancing performance on benchmarks like GSM8K. 
Getting Started To begin using these new features, ensure you have the latest post-training dependencies installed:
uv pip install maxtext[tpu-post-train]==0.2.1 --resolution=lowest
install_maxtext_tpu_post_train_extra_deps 
Shell
Copied 
Running SFT: You can launch an SFT run using the train_sft module, specifying your model, dataset, and output directory:
python3 -m maxtext.trainers.post_train.sft.train_sft \
model_name=${MODEL?} \
load_parameters_path=${MAXTEXT_CKPT_PATH?} \
run_name=${RUN_NAME?} \
base_output_directory=${BASE_OUTPUT_DIRECTORY?} 
Shell
Copied 
Running RL (GRPO/GSPO): For RL, the train_rl module handles the loading of policy and reference models, executes the training, and provides automated evaluation on reasoning benchmarks:
python3 -m maxtext.trainers.post_train.rl.train_rl \
model_name=${MODEL?} \
load_parameters_path=${MAXTEXT_CKPT_PATH?} \
run_name=${RUN_NAME?} \
base_output_directory=${BASE_OUTPUT_DIRECTORY?} \
loss_algo=gspo-token \
chips_per_vm=${CHIPS_PER_VM?} 
Shell
Copied 
What’s Next? While single-host support provides a powerful entry point for many developers, MaxText is built for scale. These same workflows are designed to transition seamlessly to multi-host configurations for those training larger models and utilizing massive datasets. Please stay tuned for more updates in this direction from us in the future.
posted in:
AI 
Cloud 
Announcements 
Explore 
Previous 
Next 
Related Posts 
Cloud 
Cloud 
Announcements 
Explore 
Speeding Up AI: Bringing Google Colossus to PyTorch via GCSFS and Rapid Bucket
APRIL 29, 2026 
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
How-To Guides 
Learn 
Building with Gemini Embedding 2: Agentic multimodal RAG and beyond
APRIL 30, 2026 
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
