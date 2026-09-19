---
source: "https://andrewlock.net/configuring-contextual-options-with-microsoft-extensions-options-contextual/"
title: "Configuring contextual options with Microsoft.Extensions.Options.Contextual"
author: "Andrew Lock"
date_published: "2026-04-01"
date_clipped: "2026-09-18"
category: ".NET Ecosystem"
source_type: "rss"
---

# Configuring contextual options with Microsoft.Extensions.Options.Contextual

Capture format: attributed summary of fetched public written content; not a full-text reproduction.

Andrew Lock examines Microsoft.Extensions.Options.Contextual as an experimental extension to the options pattern. Callers supply a context to an asynchronous options provider; generated context code populates a receiver that applies context-dependent values alongside ordinary configuration.

The walkthrough marks a partial context type with OptionsContext, implements IOptionsContextReceiver, configures a contextual loader, and retrieves options through IContextualOptions. Unlike named options, this uses arbitrary caller-provided context rather than a fixed collection of named configurations.

Lock questions whether indirection improves coupling: receivers depend on property-name strings, so renaming a property can still break behavior. At publication, the package remained prerelease and its experimental APIs required explicit suppression of EXTEXP0018, including generated-code usage. The example references version 10.4.0-preview.1.26160.2.

Lore relevance: a design tradeoff to assess before adopting context-driven configuration or feature-flag abstractions. This April article is historical evidence; its package maturity and adoption observations were not revalidated as current.

Source: [Original article](https://andrewlock.net/configuring-contextual-options-with-microsoft-extensions-options-contextual/).
