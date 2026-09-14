---
source: "https://andrewlock.net/exploring-the-dotnet-11-preview-7-the-pain-of-serializing-unions-and-closed-class-hierarchies-with-system-text-json"
title: "The pain of serializing unions and closed class hierarchies with System.Text.Json: Exploring the .NET 11 preview - Part 7"
author: "Andrew Lock"
date_published: "2026-09-01"
date_clipped: "2026-09-13"
category: ".NET Ecosystem"
source_type: "rss"
capture_mode: "attributed-summary"
full_text_fetched: "true"
---

# The pain of serializing unions and closed class hierarchies with System.Text.Json: Exploring the .NET 11 preview - Part 7

Original source: [The pain of serializing unions and closed class hierarchies with System.Text.Json: Exploring the .NET 11 preview - Part 7](https://andrewlock.net/exploring-the-dotnet-11-preview-7-the-pain-of-serializing-unions-and-closed-class-hierarchies-with-system-text-json)

## Source-content summary

Andrew Lock explores System.Text.Json behavior for C# union types and closed class hierarchies using .NET 11 preview 7. Primitive unions can serialize directly to a JSON value, while derived-class members require appropriate polymorphic configuration.

The walkthrough tests inferred closed-type polymorphism and encounters restrictions around accessibility, nested inheritance, and serialization configuration. It also examines deserialization, illustrating why a type that is convenient to model does not automatically produce a usable bidirectional JSON contract.

These observations are explicitly tied to a preview release, and the article mentions subsequent RC1 API changes. HoneyDrunk relevance: evaluate concrete request/response shapes, nested hierarchies, and round-trip behavior before exposing new language constructs through public APIs. Preserve this as preview-era evidence; do not interpret every reported limitation as confirmed behavior in later .NET releases.

Capture note: This is an attributed summary of the fetched article, not a verbatim full-text archive. The original source retains the complete examples and discussion.
