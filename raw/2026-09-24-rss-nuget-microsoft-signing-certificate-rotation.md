---
source: "https://devblogs.microsoft.com/dotnet/microsoft-author-signing-certificate-update-2026/"
title: "Microsoft is updating its author-signing certificate starting September 23, 2026"
author: "The NuGet Team"
date_published: "2026-09-23"
date_clipped: "2026-09-24"
category: ".NET Ecosystem"
source_type: "rss"
capture_method: "attributed-summary"
related_categories: ["Security & Ethical Hacking"]
---

# Microsoft is updating its author-signing certificate starting September 23, 2026

Attributed summary of the fetched article.

Microsoft announces a new author-signing certificate for NuGet packages starting September 23, 2026. The affected configurations are trusted-author allowlists and verification commands that explicitly pin Microsoft certificate fingerprints. Existing signed packages retain their original signatures.

The migration adds the new certificate while retaining older accepted certificates. Otherwise newly signed packages can fail with NU3034. Check all applicable nuget.config scopes, not only the repository copy. The article provides the certificate fingerprint, the trust command, and verification examples; consult the original before changing trust settings.

HoneyDrunk application: inventory package-signature enforcement in CI and developer configuration, then validate both old and newly signed packages after updating policy. Projects without explicit author-fingerprint restrictions are described as unaffected. Source confidence: official NuGet team guidance, captured as a dated migration record.

Source: [Original article](https://devblogs.microsoft.com/dotnet/microsoft-author-signing-certificate-update-2026/).
