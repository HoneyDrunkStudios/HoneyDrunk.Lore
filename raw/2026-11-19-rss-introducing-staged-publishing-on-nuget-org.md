---
source: "https://devblogs.microsoft.com/dotnet/nuget-staged-publishing"
title: "Introducing staged publishing on NuGet.org"
author: "Jon Douglas"
date_published: "2026-11-17"
date_clipped: "2026-11-19"
category: ".NET Ecosystem"
source_type: "rss"
---

# Introducing staged publishing on NuGet.org

Source: https://devblogs.microsoft.com/dotnet/nuget-staged-publishing

A successful build tells you that your pipeline finished. It does not tell you that you meant to release. Today, we are introducing **staged publishing on NuGet.org**, available to all package publishers, so you can prepare and validate packages privately before making an explicit decision to publish them.

Upload a security fix ahead of its coordinated disclosure. Gather the packages for a feature release without exposing an unfinished set. Let automation prepare a large update, then review it on NuGet.org before it reaches the people who depend on it.

**Your pipeline prepares the release. You decide when it goes live.**

## A release boundary you control

With a normal package push, upload starts the public publishing process. Staged publishing adds a place to stop: the package goes through NuGet.org validation, but stays private until an authorized maintainer promotes it through the website.

That gives you time to review what you are about to ship, fix validation problems, and choose the release moment.

Staging is opt-in. Existing `dotnet nuget push` workflows continue to work. You can adopt staging for a security-sensitive package or a coordinated release without changing every publishing workflow at once.

Staging also differs from unlisting. An unlisted package can still be restored by its exact version. A staged package is not available to consumers at all.

## Prepare your release on NuGet.org

The website is where you review staged content and approve its release. You can stage a single package or organize related packages into a staging group.

### Stage and validate

On the NuGet.org upload page, choose the staging option under **Publishing Mode** when uploading your package. You can also upload from your pipeline using the CLI example below.

NuGet.org runs the package through its validation pipeline, including malware scanning, signature checks, and repository signing. Once validation succeeds, the package is ready for promotion. It stays out of public package pages, search results, and restore operations.

You can inspect the staged package and its validation status in the website’s package management experience. If validation fails, fix the problem and stage a replacement before release day.

Staging does not provide a private restore feed, even for the owner. Test your packages and their dependencies using a local or private feed first, then stage the release artifacts on NuGet.org.

### Organize a staging group

A staging group collects the packages for a release under one staging owner, either a user or an organization. For example, a library, its integrations, and its analyzers can share a group for an upcoming feature release.

In NuGet.org package management, create a group, add the staged packages for that release, and review each package’s validation status. The group gives you a release-level view instead of requiring you to keep track of separate uploads.

Permissions follow the staging owner. Being a co-owner of a package does not automatically grant access to content staged on behalf of a different owner.

![NuGet.org package management showing staging groups, package counts, validation status, and the Create Staging Group button.](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/11/nuget-staged-publishing-manage-packages.webp)

### Review and promote

Before promotion, check that the group contains the package IDs and versions you intend to release and that every package has passed validation. Compare that set with your release plan, including any dependencies that need to ship alongside it.

When you are ready, choose **Promote** for an individual package or **Promote group** for a group on NuGet.org. Promotion requires an authorized user signed in with two-factor authentication enabled on their account. You can promote an individual package or approve a group in one action.

For a group, packages that are still validating or have failed validation must be addressed before promotion can begin. After promotion starts, check its progress and outcome on the website. If an item fails, follow up on that item rather than assuming the whole release completed.

Group promotion is not an atomic release. Packages move through NuGet.org’s public distribution pipeline independently, so they may become restorable at different times. Account for that window when coordinating dependencies and announcements.

![Contoso 2.4.0 staging group showing five ready package and symbol entries and the Promote group button.](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/11/nuget-staged-publishing-promote-ready.webp)

## A human decision before a public release

Automation is good at repeating a process. A release still deserves someone asking, “Is this the version we intend to put into other people’s applications?”

Staged publishing creates that checkpoint. The build can run unattended and upload its artifacts. An authorized maintainer then reviews the release and takes the action that makes it public.

For a large staged update, that approval provides a human-presence checkpoint for the release set. It keeps the final publishing decision with a person while allowing the preparation work to scale.

There is an important distinction here: having two-factor authentication enabled and approving through an authenticated website session is not the same as completing a fresh two-factor challenge for every promotion. We are not claiming a new authentication challenge for each package or group.

The security boundary is strongest when automation has **staging-only permissions**. A staging-only API key can upload staged packages but cannot use the normal push path to publish them directly. Trusted Publishing policies can also be restricted to staging only.

If someone compromises that pipeline credential, they can submit content for review, but they cannot use it to release packages directly to consumers. That does not make the uploaded content trustworthy. Review the artifacts, investigate unexpected uploads, and continue protecting your build system and maintainer accounts.

We recommend pairing staging with [NuGet Trusted Publishing](https://learn.microsoft.com/nuget/nuget-org/trusted-publishing). Trusted Publishing reduces reliance on long-lived secrets through short-lived credentials tied to your workflow. Staging adds a separate approval boundary before publication.

## Make room for the release you intended

Staging is useful whenever preparation and publication should happen at different times.

**Security fixes:** Prepare packages ahead of a coordinated disclosure and resolve validation problems before the release window. Keep the fix private while you coordinate with affected teams. At the agreed time, approve promotion and monitor public availability.

**Feature releases:** Gather related packages while documentation, samples, and announcements are being finished. Review the complete release set before publishing, rather than making each upload a public event.

**Large updates:** Let multiple builds contribute artifacts to a staging group. Check what is present, catch an omitted package, and approve the intended set from one place. Plan for the distribution window rather than promising simultaneous availability.

**Routine releases:** Even a single-package release benefits from a final check of the package ID, version, and artifact. A passing pipeline should not have to be your last opportunity to notice a mistake.

Staging is a preparation window, not permanent storage. Staged content expires if it is not promoted. Keep an eye on expiration notices when planning a longer release cycle.

## Basic CLI staging in .NET 11 RC2

The .NET 11 RC2 SDK supports basic staging uploads. Use the staging command instead of a normal push when you want the package held for review.

For a CLI-based workflow, an upload looks like this:

```
dotnet package stage push ./artifacts/Contoso.Library.1.2.0.nupkg \
  --source https://api.nuget.org/v3/index.json \
  --api-key "$NUGET_API_KEY"
```

`NUGET_API_KEY` represents a staging-capable credential supplied securely by your workflow. Do not put the credential in source control. For the strongest separation, use a staging-only credential.

To send an upload to a group, supply its ID. If the group does not exist yet, NuGet.org creates it automatically:

```
dotnet package stage push ./artifacts/Contoso.Library.1.2.0.nupkg \
  --source https://api.nuget.org/v3/index.json \
  --api-key "$NUGET_API_KEY" \
  --group november-release
```

An accepted upload does not mean validation has finished or the package is public. Return to NuGet.org to review validation and promote the release.

### What’s coming to the CLI

Listing and group management will come in a future SDK update. The proposed command shape includes:

```
dotnet package stage list
dotnet package stage group create november-release --name "November release"
dotnet package stage group list
dotnet package stage group add november-release Contoso.Library@1.2.0
```

These are roadmap examples, not a promise of final syntax or a release date. Promotion remains a NuGet.org website action; do not plan on a CLI approval command.

## Try it with your next release

Start with one package or a small release group. Test the artifacts, stage them, and review their validation status on NuGet.org. Give your pipeline staging-only permissions, then have an authorized maintainer approve publication when the release is ready.

For teams managing security disclosures or larger releases, rehearse that workflow before the day you need it. Check permissions, group membership, expiration, and the time it takes for promoted packages to become restorable.

We would like to hear where the workflow fits and where it gets in your way. Share feedback through [NuGetGallery issues](https://github.com/NuGet/NuGetGallery/issues) for the website or [NuGet/Home issues](https://github.com/NuGet/Home/issues) for the CLI.

The people restoring your packages may never see the care that went into a release. Staged publishing gives you a place to exercise that care before they have to trust the result.
