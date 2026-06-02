---
source: "https://developer.adobe.com/firefly-services/docs/photoshop/"
title: "Adobe Photoshop API - Firefly Services"
author: "Adobe Developer"
date_published: "unknown"
date_clipped: "2026-06-02"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Adobe Photoshop API - Firefly Services

Source: https://developer.adobe.com/firefly-services/docs/photoshop/

data-slots=image, heading, text
Adobe Photoshop API - Firefly Services 
Unlock the potential of Adobe Photoshop and cutting edge AI/ML services through an easy-to-use RESTful API. 
data-slots=heading, text, button
data-variant=secondary
data-backgroundColor=background-color-gray
data-borderColor=#14b8a6
data-hasborder=true
🚀 Now Generally Available - Photoshop API v2 
Photoshop API v2 is now generally available. This release introduces major improvements in scalability, flexibility, and programmability, enabling teams to build production-grade, high-volume content workflows. v2 addresses these gaps and introduces a more extensible foundation for modern content pipelines. 
Learn more 
Overview 
Welcome to the Adobe Photoshop API, now integrated into Firefly Services. Our API follows REST-like principles, utilizing standard HTTP response codes, verbs, and authentication methods that return JSON-encoded responses. While the examples provided are in cURL, feel free to develop your application in any preferred language.
This guide will assist you in:
Creating a project within the Adobe Developer Console 
Obtaining and authenticating your credentials 
Constructing personalized workflows by chaining API calls to various endpoints within the Firefly Services APIs 
Developing event-driven applications through Adobe I/O Events 
Photoshop API v2 — General Availability 
Photoshop API v2 is the unified next-generation surface for Photoshop and Lightroom-style workflows in Firefly Services: one architecture, consistent request and response patterns, and flexible output destinations. If you've worked with v1, you likely encountered limitations around file size, embedded assets, and rigid workflows. v2 addresses these gaps and introduces a more extensible foundation for modern content pipelines.
What's new in v2 
Linked Smart Objects 
Photoshop API v2 adds support for linked smart objects, a foundational improvement for content supply chains.
In v1, embedded smart objects created several challenges:
PSD files increased in size quickly and often exceeded the 2GB limit 
Assets were duplicated across files instead of reused 
Updating assets downstream was difficult to manage and govern 
With linked smart objects:
Assets are referenced instead of embedded 
File sizes remain manageable, even in large-scale workflows 
Updates propagate across templates and variants 
Teams can centralize and govern shared assets 
This enables more efficient, maintainable, and scalable content systems.
Increased file size limits 
Maximum file size increased from 2GB to 5GB 
This allows for significantly more complex documents and removes a key limitation for enterprise use cases.
UXP scripting (JavaScript automation) 
Photoshop API v2 introduces support for UXP scripting, allowing developers to execute JavaScript directly within Photoshop workflows.
This adds a programmable layer to automation and unlocks advanced use cases:
Copy fitting and dynamic text adjustments 
Conditional logic based on inputs or metadata 
Automated recoloring and localization 
Trapping and print-specific adjustments 
Compliance and brand rule enforcement 
Previously, these scenarios required custom workarounds or waiting for new API capabilities. With UXP scripting:
Teams can define and maintain their own logic 
Business rules can be embedded directly into workflows 
Automation becomes extensible rather than fixed 
This significantly expands what can be built with the API.
More powerful action workflows 
Support for Generative Fill , Generative Expand , and additional actions 
Adobe action files are now published and customizable 
Outputs can be dynamically generated at runtime without predefining assets 
Richer document intelligence 
Artboards are now first-class objects with full metadata (size, presets, background) 
Ability to extract embedded smart objects without opening Photoshop 
Expanded layer metadata including text settings, blend ranges, and layout details 
Expanded creative control 
Improved smart object workflows with support for SVG and linked assets 
New replacement and transformation capabilities 
Enhanced text rendering for complex and multilingual content 
Improved color management with ICC profile support 
Built for scale 
Support for files up to 5GB 
Longer processing times for complex jobs 
Improved error handling with more actionable responses 
Flexible storage options for both prototyping and production workflows 
Photoshop API v2 services 
Many useful Photoshop operations are available in the v2 API. Here are just a few:
Remove background — Detect and isolate the main subject with AI and remove the background while preserving the subject for use in composites and cutouts. 
Smart Objects — Create and replace embedded and linked Smart Objects in a PSD so new imagery fits the original layer bounds and keeps its aspect ratio. 
Product Crop — Smart-crop images by detecting the subject and framing it as the focal point. 
ActionJSON — Apply Photoshop Actions from an ATN file programmatically and adjust the action payload for more flexible, dynamic edits. 
Explore all available services in the Photoshop API v2 guides or browse endpoints in the Photoshop API v2 reference .
Migration from v1 
Photoshop API v1 will reach end of life on July 31, 2026. Teams should begin planning migration to v2 immediately to take advantage of the new capabilities and avoid service disruption.
To support a smooth transition, we provide topic-based migration guides covering edit, document, layer, actions, output, artboard, manifest, and status flows. Versioned /v2 endpoints and a dedicated v2 OpenAPI reference exist alongside the legacy v1 reference, so you can compare contracts and plan migration without merging the two.
Start your migration: 
Photoshop API v2 migration guides — v1-to-v2 topic guides and v2 workflow documentation 
Photoshop API v2 reference — Full endpoint reference for the photoshopv2-api.json specification 
Discover 
data-slots=heading, link, text
Get Started 
Getting Started Guide 
Get started with the Adobe Photoshop Firefly Services. 
data-slots=link, text
Photoshop API v2 guides 
Recommended. Migration guides, v1-to-v2 topics, and workflow guides for the v2 API. 
data-slots=link, text
Photoshop API v2 reference 
Recommended. Browse the OpenAPI reference for Photoshop API v2 endpoints. 
data-slots=link, text
Tutorials 
Explore our tutorials page for comprehensive guidance. 
data-slots=link, text
Photoshop API v1 guides (Deprecated) 
⚠️ Deprecated — End of life July 31, 2026. Migration to v2 is required. Reference only; do not use for new integrations. 
data-slots=link, text
Photoshop API v1 reference (Deprecated) 
⚠️ Deprecated — End of life July 31, 2026. Migration to v2 is required. Reference only; do not use for new integrations.
