---
source: "https://andrewlock.net/splitting-the-netescapades-enumgenerators-packages-the-road-to-a-stable-release"
title: "Splitting the NetEscapades.EnumGenerators packages: the road to a stable release"
author: "Andrew Lock"
date_published: "2026-03-10"
date_clipped: "2026-09-20"
category: ".NET Ecosystem"
source_type: "rss"
capture_format: "attributed-summary"
---

# Splitting the NetEscapades.EnumGenerators packages: the road to a stable release

Source: [Splitting the NetEscapades.EnumGenerators packages: the road to a stable release](https://andrewlock.net/splitting-the-netescapades-enumgenerators-packages-the-road-to-a-stable-release)

Attributed summary of the fetched full written article; not a verbatim reproduction. Claims remain source-specific and have not been independently reproduced.

Andrew Lock explains why adding option types to an enum generator's attribute assembly broke consumers that excluded runtime assets. Generated public methods now referenced an assembly those consumers intentionally withheld from downstream projects.

The remedy separates the generator from its optional runtime dependencies and retains a convenient metapackage. Referencing the generator alone can emit enum-specific option types; adding the runtime package enables shared option types. The metapackage supplies both for ordinary use.

The distinction between PrivateAssets and ExcludeAssets matters: one controls dependency propagation, while the other controls asset inclusion. Hiding generator tooling does not make types used by generated public APIs disappear as dependencies.

This is a March beta-era design account, not confirmation of the package's current release status. Its durable value is the packaging boundary and downstream-consumer failure mechanism.

HoneyDrunk relevance: review generated API signatures and test packaged library consumption before changing analyzer or source-generator dependencies across Node repositories.
