---
source: "https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/"
title: "NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports"
author: ".NET Blog"
date_published: "Mon, 18 May 2026 17:00:00 +0000"
date_clipped: "2026-05-19"
category: ".NET Ecosystem"
source_type: "rss"
---

# NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports

Source: https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/

If you’ve run NuGet Audit or a vulnerability scanner on a .NET project, you’ve likely seen warnings for transitive packages you never explicitly installed.
In many cases, those packages — such as System.Text.Json or System.Text.Encodings.Web — are already provided at a newer version by the .NET Runtime Libraries, so the package vulnerability warning is a false positive.
In .NET 10, NuGet audits transitive dependencies by default (via NuGetAuditMode set to all ), and package pruning removes packages from the restore graph when the .NET Runtime Libraries already provide them.
In our telemetry, projects with these defaults have 70% fewer transitive vulnerability reports compared to projects using the previous defaults.
Background: How We Got Here 
Many libraries on nuget.org target netstandard2.0 for maximum compatibility, and still carry dependencies on packages like System.Memory and System.Text.Json — packages that are now part of the .NET Runtime Libraries .
And this isn’t only about older packages — as the platform evolves, packages that once shipped independently become part of the .NET Runtime Libraries. For example, System.IO.Pipelines started as a standalone NuGet package and later became part of the platform.
Consider a .NET 10 project that depends on one of these libraries.
That library may pull in System.Text.Json 8.0.0 as a transitive dependency — even though the .NET 10 runtime already ships a newer version.
The package on nuget.org still exists, NuGet still resolves it, and when a CVE is published against it, vulnerability scanners still flag it.
The core issues are:
False-positive vulnerability warnings : when a CVE is published against a platform-provided package, NuGet Audit reports it as a transitive vulnerability — even when the .NET Runtime Libraries already provide a patched version. The package is in the graph, but it is not what your app actually uses. 
Larger restore graphs : more packages to resolve means more downloads, more graph entries, and more noise. 
Stale package references : older and unsupported package entries can remain in the graph even when the app is actually using the in-box .NET Runtime Libraries implementation. Pruning removes those redundant references and makes it clearer that your app is not depending on an old package separately. 
To see how pruning addresses these issues, it helps to look at what happens during restore.
What is Package Pruning? 
Package pruning removes platform-provided packages from the NuGet dependency graph at restore time.
If a package is already supplied by the .NET Runtime Libraries, NuGet can exclude it from the resolved graph.
The .NET SDK includes a list of packages provided by each target framework, along with the highest version that framework supplies.
If a transitive dependency falls within that range, NuGet prunes it.
For example, net8.0 includes System.Text.Json 8.0.x , so a transitive dependency on System.Text.Json 9.0.0 is not pruned when targeting net8.0 because the platform does not provide that version.
Here’s what happens at restore time:
Transitive packages in the pruning range are removed from the graph. They are not downloaded, do not appear in restore outputs, and are not surfaced by audit as transitive package dependencies. 
Direct packages in the pruning range are handled differently. NuGet applies PrivateAssets='all' and IncludeAssets='none' , more explicitly communicating that the .NET Runtime Libraries version will be used instead and the package does not flow into your published nuspec. The reference remains in your project file until you remove it. 
When a direct PackageReference can be removed entirely from your project because it is prunable in every target framework, NuGet raises NU1510 .
Before and After 
Consider a project targeting net10.0 that references Microsoft.Extensions.AI and NuGet.Protocol .
Without pruning, dotnet list package --include-transitive restores a vulnerable transitive package and surfaces a warning:
Sample.csproj : warning NU1903: Package 'System.Formats.Asn1' 6.0.0 has a known high severity vulnerability, https://github.com/advisories/GHSA-447r-wph3-92pm
Project 'Sample' has the following package references
[net10.0]:
Top-level Package Requested Resolved
> Microsoft.Extensions.AI 10.0.1 10.0.1
> NuGet.Protocol 6.9.1 6.9.1
Transitive Package Resolved
> Microsoft.Extensions.AI.Abstractions 10.0.1
> Microsoft.Extensions.Caching.Abstractions 10.0.0
> Microsoft.Extensions.DependencyInjection.Abstractions 10.0.0
> Microsoft.Extensions.Logging.Abstractions 10.0.0
> Microsoft.Extensions.Primitives 10.0.0
> Newtonsoft.Json 13.0.3
> NuGet.Common 6.9.1
> NuGet.Configuration 6.9.1
> NuGet.Frameworks 6.9.1
> NuGet.Packaging 6.9.1
> NuGet.Versioning 6.9.1
> System.Diagnostics.DiagnosticSource 10.0.0
> System.Formats.Asn1 6.0.0
> System.Numerics.Tensors 10.0.0
> System.Security.Cryptography.Pkcs 6.0.4
> System.Security.Cryptography.ProtectedData 4.4.0
> System.Text.Json 10.0.0
> System.Threading.Channels 10.0.0 
With pruning enabled, System.Formats.Asn1 is removed from the transitive graph and the warning disappears.
Other platform-provided packages such as System.Diagnostics.DiagnosticSource , System.Text.Json , and System.Threading.Channels are also pruned because they are redundant on net10.0 .
Project 'Sample' has the following package references
[net10.0]:
Top-level Package Requested Resolved
> Microsoft.Extensions.AI 10.0.1 10.0.1
> NuGet.Protocol 6.9.1 6.9.1
Transitive Package Resolved
> Microsoft.Extensions.AI.Abstractions 10.0.1
> Microsoft.Extensions.Caching.Abstractions 10.0.0
> Microsoft.Extensions.DependencyInjection.Abstractions 10.0.0
> Microsoft.Extensions.Logging.Abstractions 10.0.0
> Microsoft.Extensions.Primitives 10.0.0
> Newtonsoft.Json 13.0.3
> NuGet.Common 6.9.1
> NuGet.Configuration 6.9.1
> NuGet.Frameworks 6.9.1
> NuGet.Packaging 6.9.1
> NuGet.Versioning 6.9.1
> System.Numerics.Tensors 10.0.0
> System.Security.Cryptography.Pkcs 6.0.4
> System.Security.Cryptography.ProtectedData 4.4.0 
This is the practical effect of pruning: packages already covered by the .NET Runtime Libraries no longer appear as transitive dependencies, eliminating the false-positive reports they would otherwise generate.
Projects with deeper dependency trees or libraries that pull in more platform-provided packages will often see a larger reduction.
What Changed in .NET 10 
Package pruning first shipped as an opt-in feature in .NET SDK 9.0.200. In .NET 10, it is part of the default experience.
For projects that target .NET 10 or later:
Package pruning is enabled by default 
Direct PackageReference items in the pruning range are automatically privatized (as described above), and NU1510 signals when a reference can be removed entirely 
If any target framework in a multi-targeted project is net10.0 or later, pruning applies to all target frameworks in that project.
In the same release, NuGetAuditMode defaults to all in .NET 10, so NuGet now audits transitive dependencies by default.
Pruning and NuGetAuditMode=all work together: pruning removes platform-provided packages from the graph, and auditing expands to the remaining transitive dependencies so you can identify and remove real vulnerabilities in packages your app actually uses.
In our telemetry, projects with these defaults have 70% fewer transitive vulnerability reports compared to projects using the previous defaults.
The benefits go beyond vulnerability auditing.
When NuGet removes platform-provided packages from the graph, there are fewer packages to resolve, fewer transitive version constraints to reconcile, and fewer opportunities for conflicts or resolution failures.
In our telemetry, restores with pruning enabled show a measurably higher success rate than restores without it.
The smaller graph also means less work during restore — on a per-project level, pruning can reduce restore time by up to 50%.
<!-- .NET 10 defaults -->
<PropertyGroup>
<NuGetAuditMode>all</NuGetAuditMode>
<RestoreEnablePackagePruning>true</RestoreEnablePackagePruning>
</PropertyGroup> 
Summary 
Package pruning makes NuGet’s dependency graph better reflect what your app actually uses.
In .NET 10, that means fewer false-positive transitive vulnerability reports, smaller restore graphs, faster and more reliable restores, and audit results that are easier to act on.
More packages may become part of the .NET Runtime Libraries over time, and pruning will keep dependency graphs focused on actual dependencies rather than platform-provided ones.
For more details, see the documentation on package pruning .
We’d love to hear your feedback — let us know how pruning works for your projects on GitHub .
