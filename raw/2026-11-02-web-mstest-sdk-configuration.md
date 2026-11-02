---
source: "https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-sdk"
title: "MSTest SDK configuration"
author: "MarcoRossignoli"
date_published: "unknown"
date_clipped: "2026-11-02"
category: ".NET Ecosystem"
source_type: "web"
date_updated: "2026-10-01"
---

# MSTest SDK configuration

Capture note: The page update date is recorded separately; an original publication date was not available.

This article covers advanced configuration options for MSTest.Sdk. For basic setup and getting started, see [Get started with MSTest](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-getting-started).

Important

By default, MSTest.Sdk uses the [MSTest runner with MTP](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-running-tests), including with [dotnet test](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test). This requires modifying your CI and local CLI calls, and also impacts the available entries of the *.runsettings*. You can keep the old integrations and tools by [switching to VSTest](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-sdk#select-the-runner).

MSTest.Sdk sets `EnableMSTestRunner` and `TestingPlatformDotnetTestSupport` to true by default. For more information about dotnet test and its different modes, see [Testing with dotnet test](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test).

## Test utility helper libraries

If the project that uses MSTest.Sdk is intended to be a test utility helper library, and doesn't by itself contain any runnable tests, the project should have `<IsTestApplication>false</IsTestApplication>`.

## Select the runner

By default, MSTest SDK relies on [MTP](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-running-tests), but you can switch to [VSTest](https://learn.microsoft.com/en-us/visualstudio/test/vstest-console-options) by adding the property `<UseVSTest>true</UseVSTest>`.

## Test Windows application models

Starting with MSTest.Sdk 4.5, the default MTP runner supports the following Windows application models:

* Classic UWP projects that target `uap10.0`.
* Modern UWP projects that use .NET 10 and set `UseUwp` to `true`.
* Packaged full-trust WinUI 3 projects.
* Unpackaged WinUI 3 projects.
* WinUI 3 `packagedClassicApp` projects that set `TrustLevel="appContainer"`.

MSTest.Sdk supplies compatible MTP 2.5 components and starts a full-trust app-model sidecar for packaged and AppContainer test hosts. The sidecar registers the package, activates the selected application by AUMID, authorizes the exact package SID for AppContainer communication, and recovers result artifacts from package storage.

UWP projects still require the Visual Studio UWP workload and desktop MSBuild for build-time support. They don't require `Microsoft.NET.Test.Sdk`, `vstest.console`, or the Visual Studio UWP test runtime provider.

For project configuration, run commands, and samples, see [Test UWP and WinUI 3 apps with MSTest and MTP](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-winui).

Starting with MSTest.Sdk 4.5 preview, set `EnableWindowsUIAutomation` to `true` to add the matching `MSTest.Windows.UIAutomation` package to a Windows-targeted project. This feature launches and automates an external unpackaged Win32, Windows Forms, or WPF application rather than hosting tests inside a UWP or WinUI app. For details, see [Test Windows desktop apps with MSTest UI Automation](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-ui-automation).

## Extend MTP

You can customize the MTP experience through a set of [NuGet package extensions](https://learn.microsoft.com/en-us/dotnet/core/testing/microsoft-testing-platform-features). To simplify and improve this experience, MSTest SDK introduces two features:

* [Microsoft.Testing.Platform profile](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-sdk#microsofttestingplatform-profile)
* [Enable or disable extensions](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-sdk#enable-or-disable-extensions)

Starting with MSTest 4.4, the MSTest adapter uses its native MTP integration and no longer depends on `Microsoft.Testing.Extensions.VSTestBridge`. Reference the bridge explicitly only when the MTP test application must run a framework through its VSTest adapter.

### Microsoft.Testing.Platform profile

The concept of *profiles* allows you to select the default set of configurations and extensions that will be applied to your test project.

You can set the profile using the property `TestingExtensionsProfile` with one of the following three profiles:

* `None` - No extensions are enabled.
* `Default` - Enables the recommended extensions for this version of MSTest.SDK. This is the default when the property isn't set explicitly.

  Enables the following extensions:

  + [Code Coverage](https://learn.microsoft.com/en-us/dotnet/core/testing/microsoft-testing-platform-code-coverage#microsoft-code-coverage)
  + [Trx Report](https://learn.microsoft.com/en-us/dotnet/core/testing/microsoft-testing-platform-test-reports#visual-studio-test-reports-trx)
  + [Azure DevOps Report](https://learn.microsoft.com/en-us/dotnet/core/testing/microsoft-testing-platform-test-reports#azure-devops-reports) (MSTest.Sdk 4.3.0+)
  + [GitHub Actions Report](https://learn.microsoft.com/en-us/dotnet/core/testing/microsoft-testing-platform-test-reports#github-actions-reports) (MSTest.Sdk 4.3.0+; the package was prerelease in 4.3.x and follows the MTP release version starting in 4.4)
* `AllMicrosoft` - Enables the Microsoft extensions selected for broad out-of-the-box use, including extensions with a restrictive license. Experimental and API-only extensions can still require explicit opt-in.

  Enables all extensions from the `Default` profile, plus the following extensions:

  + [Crash Dump](https://learn.microsoft.com/en-us/dotnet/core/testing/microsoft-testing-platform-crash-hang-dumps#crash-dump)
  + [Fakes](https://learn.microsoft.com/en-us/dotnet/core/testing/microsoft-testing-platform-fakes) (MSTest.Sdk 3.7.0+)
  + [Hang Dump](https://learn.microsoft.com/en-us/dotnet/core/testing/microsoft-testing-platform-crash-hang-dumps#hang-dump)
  + [Hot Reload](https://learn.microsoft.com/en-us/dotnet/core/testing/microsoft-testing-platform-hot-reload#hot-reload)
  + [HTML Report](https://learn.microsoft.com/en-us/dotnet/core/testing/microsoft-testing-platform-test-reports#html-reports)
  + [Retry](https://learn.microsoft.com/en-us/dotnet/core/testing/microsoft-testing-platform-retry#retry)

  In MSTest.Sdk versions 3.11.0 through 4.2.x, the Azure DevOps Report extension is included only in `AllMicrosoft`.

Note

The profiles reference the Azure DevOps Report and GitHub Actions Report packages, but reporting remains disabled at runtime. Pass `--report-azdo` to enable Azure DevOps reporting. To enable GitHub Actions reporting, run the tests on GitHub Actions and pass `--report-gh`.

Here's a full example, using the `None` profile:

```
<Project Sdk="MSTest.Sdk/4.1.0">

    <PropertyGroup>
        <TargetFramework>net10.0</TargetFramework>
        <TestingExtensionsProfile>None</TestingExtensionsProfile>
    </PropertyGroup>

</Project>
```

| Extension/Profile | None | Default | AllMicrosoft |
| --- | --- | --- | --- |
| [Code Coverage](https://www.nuget.org/packages/Microsoft.Testing.Extensions.CodeCoverage) |  | ✔️ | ✔️ |
| [Crash Dump](https://www.nuget.org/packages/Microsoft.Testing.Extensions.CrashDump) |  |  | ✔️ |
| [Fakes](https://www.nuget.org/packages/Microsoft.Testing.Extensions.Fakes) |  |  | ✔️¹ |
| [Hang Dump](https://www.nuget.org/packages/Microsoft.Testing.Extensions.HangDump) |  |  | ✔️ |
| [Hot Reload](https://www.nuget.org/packages/Microsoft.Testing.Extensions.HotReload) |  |  | ✔️ |
| [HTML Report](https://www.nuget.org/packages/Microsoft.Testing.Extensions.HtmlReport) |  |  | ✔️ |
| [GitHub Actions Report](https://www.nuget.org/packages/Microsoft.Testing.Extensions.GitHubActionsReport) |  | ✔️³ | ✔️³ |
| [Retry](https://www.nuget.org/packages/Microsoft.Testing.Extensions.Retry) |  |  | ✔️ |
| [Trx](https://www.nuget.org/packages/Microsoft.Testing.Extensions.TrxReport) |  | ✔️ | ✔️ |
| [Azure DevOps Report](https://www.nuget.org/packages/Microsoft.Testing.Extensions.AzureDevOpsReport) |  | ✔️³ | ✔️² |

¹ MSTest.Sdk 3.7.0+
² MSTest.Sdk 3.11.0+
³ MSTest.Sdk 4.3.0+

### Enable or disable extensions

Extensions can be enabled and disabled by MSBuild properties with the pattern `Enable[NugetPackageNameWithoutDots]`.

For example, to enable the crash dump extension (NuGet package [Microsoft.Testing.Extensions.CrashDump](https://www.nuget.org/packages/Microsoft.Testing.Extensions.CrashDump)), you can use the following property `EnableMicrosoftTestingExtensionsCrashDump` set to `true`:

```
<Project Sdk="MSTest.Sdk/4.1.0">

<PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <EnableMicrosoftTestingExtensionsCrashDump>true</EnableMicrosoftTestingExtensionsCrashDump>
</PropertyGroup>

</Project>
```

For a list of all available extensions, see [MTP features](https://learn.microsoft.com/en-us/dotnet/core/testing/microsoft-testing-platform-features).

Some MTP extensions remain opt-in and aren't included in the `Default` or `AllMicrosoft` profiles:

* Starting with MSTest.Sdk 4.3, set `<EnableMicrosoftTestingExtensionsJUnitReport>true</EnableMicrosoftTestingExtensionsJUnitReport>`, then pass `--report-junit`.
* Starting with MSTest.Sdk 4.4, set `<EnableMicrosoftTestingExtensionsCtrfReport>true</EnableMicrosoftTestingExtensionsCtrfReport>`, then pass `--report-ctrf`.
* To reference the OpenTelemetry extension, set `<EnableMicrosoftTestingExtensionsOpenTelemetry>true</EnableMicrosoftTestingExtensionsOpenTelemetry>`. Because the extension requires API configuration, register it in your custom entry point as described in [OpenTelemetry](https://learn.microsoft.com/en-us/dotnet/core/testing/microsoft-testing-platform-open-telemetry).

These extensions are available only with MTP.

Warning

It's important to review the licensing terms for each extension as they might vary.

Enabled and disabled extensions are combined with the extensions provided by your selected extension profile.

This property pattern can be used to enable an additional extension on top of the implicit `Default` profile (as seen in the previous CrashDumpExtension example).

You can also disable an extension that's coming from the selected profile. For example, disable the `MS Code Coverage` extension by setting `<EnableMicrosoftTestingExtensionsCodeCoverage>false</EnableMicrosoftTestingExtensionsCodeCoverage>`:

```
<Project Sdk="MSTest.Sdk/4.1.0">

    <PropertyGroup>
        <TargetFramework>net10.0</TargetFramework>
        <EnableMicrosoftTestingExtensionsCodeCoverage>false</EnableMicrosoftTestingExtensionsCodeCoverage>
    </PropertyGroup>

</Project>
```

In MSTest.Sdk 4.3.0 and later, the `Default` profile references the Azure DevOps Report and GitHub Actions Report packages. To remove either package reference, set `<EnableMicrosoftTestingExtensionsAzureDevOpsReport>false</EnableMicrosoftTestingExtensionsAzureDevOpsReport>` or `<EnableMicrosoftTestingExtensionsGitHubActionsReport>false</EnableMicrosoftTestingExtensionsGitHubActionsReport>`. If you keep the package references, Azure DevOps reporting starts only when you pass `--report-azdo`. GitHub Actions reporting starts only when you run the tests on GitHub Actions and pass `--report-gh`.

## Features

Outside of the selection of the runner and runner-specific extensions, `MSTest.Sdk` also provides additional features to simplify and enhance your testing experience.

### Test with Aspire

Aspire is an opinionated, cloud-ready stack for building observable, production ready, distributed applications. Aspire is delivered through a collection of NuGet packages that handle specific cloud-native concerns. For more information, see the [Aspire docs](https://aspire.dev/get-started/what-is-aspire/).

Note

This feature is available from MSTest.Sdk 3.4.0.

By setting the property `EnableAspireTesting` to `true`, you can bring all dependencies and default `using` directives you need for testing with `Aspire` and `MSTest`.

```
<Project Sdk="MSTest.Sdk/4.1.0">

    <PropertyGroup>
        <TargetFramework>net10.0</TargetFramework>
        <EnableAspireTesting>true</EnableAspireTesting>
    </PropertyGroup>

</Project>
```

### Test with Playwright

Playwright enables reliable end-to-end testing for modern web apps. For more information, see the official [Playwright docs](https://playwright.dev/dotnet/docs/intro).

Note

This feature is available from MSTest.Sdk 3.4.0.

By setting the property `EnablePlaywright` to `true` you can bring in all the dependencies and default `using` directives you need for testing with `Playwright` and `MSTest`.

```
<Project Sdk="MSTest.Sdk/4.1.0">

    <PropertyGroup>
        <TargetFramework>net10.0</TargetFramework>
        <EnablePlaywright>true</EnablePlaywright>
    </PropertyGroup>

</Project>
```

## Migrate to MSTest SDK

Consider the following steps that are required to migrate to the MSTest SDK.

### Update your project

When migrating an existing MSTest test project to MSTest SDK, start by replacing the `Sdk="Microsoft.NET.Sdk"` entry at the top of your test project with `Sdk="MSTest.Sdk"`

```
- Sdk="Microsoft.NET.Sdk"
+ Sdk="MSTest.Sdk"
```

Add the version to your `global.json`:

```
{
    "msbuild-sdks": {
        "MSTest.Sdk": "4.1.0"
    }
}
```

You can then start simplifying your project.

Remove default properties:

```
- <EnableMSTestRunner>true</EnableMSTestRunner>
- <OutputType>Exe</OutputType>
- <IsPackable>false</IsPackable>
- <IsTestProject>true</IsTestProject>
```

Remove default package references:

```
- <PackageReference Include="MSTest"
- <PackageReference Include="MSTest.TestFramework"
- <PackageReference Include="MSTest.TestAdapter"
- <PackageReference Include="MSTest.Analyzers"
- <PackageReference Include="Microsoft.NET.Test.Sdk"
```

Finally, based on the extensions profile you're using, you can also remove some of the `Microsoft.Testing.Extensions.*` packages.

### Update your CI

Once you've updated your projects, if you're using MTP (default) and if you rely on `dotnet test` to run your tests, you must update your CI configuration. For more information and to guide your understanding of all the required changes, see [dotnet test integration](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test).

If you're using the VSTest mode of `dotnet test`, here's an example update when using the `DotNetCoreCLI` task in Azure DevOps:

The default MSTest.Sdk extension profile supplies the `Microsoft.Testing.Extensions.TrxReport` and `Microsoft.Testing.Extensions.CodeCoverage` packages required by the added options. If you select the `None` profile, enable or reference both extensions before you use the options.

```
\- task: DotNetCoreCLI@2
  inputs:
    command: 'test'
    projects: '**/**.sln'
-    arguments: '--configuration Release'
+    arguments: '--configuration Release -- --report-trx --results-directory $(Agent.TempDirectory) --coverage'
```

## Reflection source generator

MSTest 4.3 introduced the reflection source generator in the independently versioned, experimental `MSTest.SourceGeneration` package. Starting with MSTest 4.4, the package graduates from experimental status and uses the MSTest version.

Native AOT projects include the source generator automatically. For a non-NativeAOT project that uses MSTest.Sdk, opt in with `<EnableMSTestSourceGeneration>true</EnableMSTestSourceGeneration>`. MSTest.Sdk aligns the `MSTest.SourceGeneration`, `MSTest.TestFramework`, and `MSTest.TestAdapter` versions through `MSTestVersion`.

The SDK also supports source generation in reusable test libraries and projects that use Central Package Management. It supplies matching `MSTest.TestAdapter` runtime hooks and generates the required `PackageVersion` items.

.NET Standard doesn't support these runtime hooks. When you enable source generation for a .NET Standard target, the SDK reports this error:

> MSTest source generation is not supported for .NET Standard target frameworks because the required MSTest.TestAdapter runtime hooks are unavailable.

The source generator discovers tests at compile time. When the generator is active, test classes must declare `[TestClass]` directly instead of inheriting it. The [MSTEST0069](https://learn.microsoft.com/en-us/dotnet/core/testing/mstest-analyzers/mstest0069) analyzer flags classes that rely on an inherited `[TestClass]`.

Starting with MSTest 4.3.2, `MSTestSourceGenMode` defaults to `ReflectionFree` for trimmed and Native AOT projects. This mode uses generated metadata and invokers where it supports the test shape. On runtimes that support reflection, MSTest falls back to reflection for unsupported or missing generated entries.

Starting with MSTest 4.4, reflection-free generation materializes complete inherited attribute metadata, including `AttributeUsage` and `AllowMultiple`. On MTP, it can bypass runtime discovery and validation for plain synchronous `[TestMethod]` and `[DataRow]` methods. Async tests, custom test method attributes, `DynamicData`, custom `ITestDataSource` implementations, and ambiguous test shapes use the fallback path. VSTest also retains its existing path.

Reflection-free mode reports these diagnostics:

| ID | Unsupported test shape |
| --- | --- |
| `AOTSG0001` | Static test class |
| `AOTSG0002` | Open generic test class, including a class nested in a generic type |
| `AOTSG0003` | Class that generated code can't access, including a file-local class or private or private-protected nesting |
| `AOTSG0004` | Generic test method |
| `AOTSG0005` | Test method with a `ref`, `in`, or `out` parameter |

## Experimental features

The following MSTest 4.3 features are **experimental**. Their public APIs are subject to change, and they're surfaced behind experimental diagnostics. To opt in, acknowledge the corresponding diagnostic ID.

### Programmatic test filtering with `ITestFilter`

Note

Introduced in MSTest 4.3.0 (experimental).

The experimental `ITestFilter` extension point, registered through `[TestFilterProviderAttribute]`, lets you decide programmatically whether each test runs, before any test class is loaded. This is useful for custom selection logic that can't be expressed with command-line filters.

Implement `ITestFilter.Filter(TestFilterContext)` to inspect metadata without loading the test class:

```
public sealed class MyFilter : ITestFilter
{
    public TestFilterResult Filter(TestFilterContext context) =>
        context.DisplayName.Contains("Nightly", StringComparison.Ordinal)
            ? TestFilterResult.Run : TestFilterResult.Drop;
}
```

Return `TestFilterResult.Run` to run the test, `Drop` to omit it without a result, or `Skip(reason)` to report a skipped result. MSTest can call one filter instance concurrently, so implementations must be thread-safe. Command-line and test-explorer filters run before `ITestFilter`, while `[Ignore]` is evaluated afterward.

Starting with MSTest 4.4, .NET projects can use the generic, type-safe registration form `[assembly: TestFilterProvider<MyFilter>]`. The compiler then enforces that `MyFilter` implements `ITestFilter` and has a public parameterless constructor. The generic attribute isn't available for .NET Framework. For a multi-targeted project, select the generic or non-generic form with a target-framework preprocessor symbol.

```
#if NET
[assembly: TestFilterProvider<MyFilter>]
#else
[assembly: TestFilterProvider(typeof(MyFilter))]
#endif
```

Starting with MSTest 4.4, the [MSTEST0081](https://learn.microsoft.com/en-us/dotnet/core/testing/mstest-analyzers/mstest0081) analyzer fully validates the non-generic registration form. For the generic form, it still reports generic filter types and assemblies that register more than one provider.

### `TestRun.Current` and planned tests

Note

Introduced in MSTest 4.3.0 (experimental).

The experimental `TestRun.Current` API (from RFC 014) exposes information about the current run, including the set of planned tests, so extensions and fixtures can inspect what's scheduled to execute.

## Known limitations

The NuGet-provided MSBuild SDKs (including MSTest.Sdk) have [limited tooling support](https://github.com/NuGet/Home/issues/13127) when it comes to updating their version, meaning that the usual NuGet update and Visual Studio UI for managing NuGet packages doesn't work as expected. You'll need to manually update the version in the `global.json` file and in the project file. (This applies even if you use Dependabot due to issues [dependabot-core#12824](https://github.com/dependabot/dependabot-core/issues/12824) and [dependabot-core#8615](https://github.com/dependabot/dependabot-core/issues/8615).)

## See also

* [MTP–related properties](https://learn.microsoft.com/en-us/dotnet/core/project-sdk/msbuild-props#microsofttestingplatformrelated-properties)
* [VSTest–related properties](https://learn.microsoft.com/en-us/dotnet/core/project-sdk/msbuild-props#vstestrelated-properties)
