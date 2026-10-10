---
"source": "https://devblogs.microsoft.com/dotnet/testing-uwp-and-winui-3-apps-with-mstest"
"title": "UWP and WinUI 3 apps: UI testing with MSTest"
"author": "Amaury Levé"
"date_published": "2026-10-05"
"date_clipped": "2026-10-08"
"category": ".NET Ecosystem"
"source_type": "rss"
---

Reliable testing of UWP and WinUI 3 apps needs the app’s real UI dispatcher,
not just a single-threaded apartment (STA) thread, so that test setup, async
test code, and cleanup all run with UI-thread access. A WinUI 3 test still
looks this simple:

```
[UITestMethod]
public async Task GridCanBeCreatedOnTheUIThread()
{
    await Task.Yield();

    var grid = new Grid();

    Assert.IsTrue(grid.DispatcherQueue.HasThreadAccess);
}
```

With [MSTest](https://learn.microsoft.com/dotnet/core/testing/unit-testing-with-mstest)
4.5 and [Microsoft.Testing.Platform](https://aka.ms/testingplatform) (MTP) 2.5,
you can use the same UI-thread testing pattern for UWP and WinUI 3 apps. The
supported models are classic and modern UWP, packaged or unpackaged WinUI 3,
and WinUI hosts that use AppContainer.
`MSTest.Sdk` picks the launch path for each model. It starts unpackaged apps
directly and uses
[`Microsoft.Testing.Extensions.PackagedApp`](https://www.nuget.org/packages/Microsoft.Testing.Extensions.PackagedApp)
to register and activate packaged apps by AUMID. For AppContainer hosts, it
also grants the exact package SID access to the controller and report pipes.
Packaged and sandboxed apps do not start as the initial test tool.
`MSTest.Sdk` launches a normal full-trust sidecar controller that owns
test arguments, cancel requests, reports, retries, and the final exit code. It
then starts the app that hosts the tests. No `Microsoft.NET.Test.Sdk`,
`vstest.console`, `UwpTestHostRuntimeProvider`, or Visual Studio deployment
runtime is used.

For more background, read the
[introduction to MSTest.Sdk](https://devblogs.microsoft.com/dotnet/introducing-mstest-sdk/)
and the overview of
[Microsoft.Testing.Platform support across .NET test frameworks](https://devblogs.microsoft.com/dotnet/mtp-adoption-frameworks/).

**Packaged activation needs machine setup**

To register an unsigned build-output layout, you need Developer Mode or a similar sideloading policy. Therefore, run AppContainer tests non-elevated, and confirm the policy on your CI agent, not just your workstation.

## Choose the model for UWP and WinUI 3 apps

Packaging and sandboxing are separate choices. Packaging adds MSIX
identity and AUMID activation; the trust level decides whether the process is
full trust or runs in AppContainer.

![Application models for UWP and WinUI 3 apps select direct startup or package registration and AUMID activation](https://devblogs.microsoft.com/dotnet/mstest-windows-app-hosting.svg)

| Application model | Identity and trust | MTP test-host path |
| --- | --- | --- |
| [Classic UWP](https://github.com/microsoft/testfx/tree/main/samples/public/ClassicUwpMtpApp) (`uap10.0`) | MSIX, AppContainer | Sidecar controller, UAP adapter/bootstrap assets, AUMID activation |
| [Modern UWP](https://github.com/microsoft/testfx/tree/main/samples/public/UwpMtpApp) (`UseUwp`) | MSIX, AppContainer | Sidecar controller, Native AOT host, AUMID activation |
| [Unpackaged WinUI 3](https://github.com/microsoft/testfx/tree/main/samples/public/WinUIMtpUnpackagedApp) | No package identity, full trust | Direct apphost launch |
| [Packaged WinUI 3](https://github.com/microsoft/testfx/tree/main/samples/public/WinUIMtpPackagedApp) | MSIX, full trust | Sidecar controller, package registration, AUMID activation |
| [WinUI 3 `packagedClassicApp` with AppContainer trust](https://github.com/microsoft/testfx/tree/main/samples/public/WinUIMtpAppContainerApp) | MSIX, AppContainer | Sidecar controller and exact package-SID pipe authorization |

For WinUI, start unpackaged unless the behavior under test needs package
identity, packaged activation contracts, or an exact match with installed app
behavior. In contrast, UWP is inherently packaged and sandboxed.

## Select MSTest.Sdk and MTP for UWP and WinUI 3 apps

At the solution or repo root, use `global.json` to pin MSTest.Sdk 4.5
and select Microsoft.Testing.Platform for the native .NET 10
`dotnet test` experience:

```
{
  "test": {
    "runner": "Microsoft.Testing.Platform"
  },
  "msbuild-sdks": {
    "MSTest.Sdk": "4.5.0"
  }
}
```

Otherwise, .NET 10 uses VSTest for `dotnet test`.
MSTest.Sdk 4.5 includes MTP 2.5, the app-model sidecar controller, UWP
adapter/bootstrap assets, and the packaged launcher.

## Configure UWP and WinUI 3 apps

### Modern UWP

For a modern UWP project, the test setup is small:

```
<Project Sdk="MSTest.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0-windows10.0.26100.0</TargetFramework>
    <UseUwp>true</UseUwp>
    <PublishAot>true</PublishAot>
  </PropertyGroup>
</Project>
```

Keep the app’s XAML, manifest, architecture, and Native AOT settings. Then,
from `OnLaunched`, pass the activation string to the generated MTP helper:

```
using Microsoft.Testing.Extensions;

protected override async void OnLaunched(LaunchActivatedEventArgs args)
{
    Window.Current.Activate();
    string[] testArguments =
        PackagedAppExtensions.GetTestApplicationArguments(args.Arguments);
    Environment.ExitCode =
        await MicrosoftTestingPlatformApplication.RunAsync(testArguments);
    Exit();
}
```

### Classic UWP

Classic `uap10.0` projects keep their existing UWP project structure and
import `MSTest.Sdk` alongside `MSBuild.Sdk.Extras`. MSTest 4.5 includes the
UAP-compatible adapter, generated bootstrap, packaged-app launcher, and TRX
client assets. The sidecar builds the `.build.appxrecipe` layout,
installs its declared frameworks, and starts the app by AUMID.

Classic and modern UWP builds still need the Visual Studio MSBuild/UWP
toolchain. However, they no longer need its VSTest runtime or deployment
provider.
See the [UWP and WinUI testing guide](https://github.com/microsoft/testfx/blob/main/docs/winui-testing.md)
for the complete classic project imports and package layout.

Therefore, run UWP tests from a Developer PowerShell for Visual Studio. Build
with the desktop MSBuild toolchain, then invoke the MTP target:

```
msbuild .\MyUwpTests.sln /restore /p:Configuration=Release /p:Platform=x64
msbuild .\MyUwpTests.csproj /t:InvokeTestingPlatform /p:Configuration=Release /p:Platform=x64
```

### AppContainer-configured WinUI 3

A packaged WinUI 3 app is full trust by default. For example, to test a
supported `packagedClassicApp` AppContainer setup, keep the packaged WinUI host
shown below and set `uap10:TrustLevel="appContainer"` in the manifest. The
host still receives normal process arguments, while MTP grants only that
package SID access to its controller, cancellation, TRX, HangDump, and Retry
pipes. Do not grant `ALL APPLICATION PACKAGES`.

Then, run this AppContainer shape from a non-elevated Developer PowerShell
through the MTP MSBuild target:

```
dotnet build .\MyAppContainerTests.csproj -c Release -p:Platform=x64
dotnet msbuild .\MyAppContainerTests.csproj /t:InvokeTestingPlatform /p:Configuration=Release /p:Platform=x64
```

## Build the self-hosted WinUI 3 test app

The following complete WinUI 3 test app supplies that dispatcher and runs
MSTest inside the app itself. Build this shared host once; the packaged and
unpackaged deltas come afterward. Three pieces make up that shared project:

![The csproj configures the MSTest runner; UnitTestApp hosts the platform; test classes run on its published dispatcher](https://devblogs.microsoft.com/dotnet/winui-mstest-project-layout.svg)

### Configure the shared project

You need Windows, the .NET 10 SDK, and the Windows App SDK tooling (installed
by Visual Studio’s “Windows application development” workload, or restored
from NuGet if you build from the CLI). Then, start from Visual Studio’s
“Blank App, Packaged (WinUI 3 in Desktop)” template, retain its
`Package.appxmanifest` and package assets for the packaged form, and apply
this shared project setup.

```
<Project Sdk="MSTest.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net10.0-windows10.0.19041.0</TargetFramework>
    <TargetPlatformMinVersion>10.0.17763.0</TargetPlatformMinVersion>
    <UseWinUI>true</UseWinUI>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

  <ItemGroup>
    <Page Remove="UnitTestApp.xaml" />
    <ApplicationDefinition Include="UnitTestApp.xaml" />
    <ProjectCapability Include="TestContainer" />
  </ItemGroup>

  <ItemGroup>
    <PackageReference Include="Microsoft.WindowsAppSDK"
                      Version="1.8.251106002" />
  </ItemGroup>
</Project>
```

### Define the application entry point

The `ApplicationDefinition` points to this minimal `UnitTestApp.xaml`:

```
<Application
    x:Class="MyWinUiTests.UnitTestApp"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <Application.Resources />
</Application>
```

### Host the test run from OnLaunched

The WinUI app owns its entry point through this `ApplicationDefinition`.
`MSTest.Sdk` detects that entry point, suppresses its own competing `Main`,
and generates a reusable `MicrosoftTestingPlatformApplication.RunAsync`
helper. Finally, the app’s code-behind creates the window, publishes its
dispatcher, and calls that helper:

```
using Microsoft.UI.Xaml;
using Microsoft.VisualStudio.TestTools.UnitTesting.AppContainer;

namespace MyWinUiTests;

public partial class UnitTestApp : Application
{
    private Window? _window;

    public UnitTestApp() => InitializeComponent();

    protected override async void OnLaunched(LaunchActivatedEventArgs args)
    {
        _window = new Window();
        _window.Activate();
        UITestMethodAttribute.DispatcherQueue = _window.DispatcherQueue;

        try
        {
            Environment.ExitCode = await MicrosoftTestingPlatformApplication.RunAsync(Environment.GetCommandLineArgs()[1..]);
        }
        finally
        {
            _window.Close();
            Exit();
        }
    }
}
```

That single `OnLaunched` override plays out in this order every time the app
starts, whether launched directly or activated by AUMID:

```
sequenceDiagram
    participant OS as Windows
    participant App as UnitTestApp.OnLaunched
    participant MTP as Microsoft.Testing.Platform
    participant Tests as MSTest UITestMethod tests

    OS->>App: Launch (apphost or AUMID activation)
    App->>App: Create and activate the Window
    App->>Tests: Publish UITestMethodAttribute.DispatcherQueue
    App->>MTP: MicrosoftTestingPlatformApplication.RunAsync
    MTP->>Tests: Run tests on the published dispatcher
    MTP-->>App: Test-run result
    App->>App: Environment.ExitCode = result
    App->>OS: Window.Close + Exit
```

Assigning `Environment.ExitCode` is important: a WinUI-generated entry point
returns `void`, so without it a failing test run can look successful to a
build or CI system. `MSTest.Sdk` owns MSTest references, extension
registration, and the packaged-app launcher registration. The
[WinUI testing guide](https://github.com/microsoft/testfx/blob/main/docs/winui-testing.md)
covers the generated helper and hosting model in more depth.

### Verify the dispatcher in a UI test

The app and tests now form one host. For example, this async test
checks that `TestInitialize`, the test body, and `TestCleanup` keep access to
the UI dispatcher:

```
using Microsoft.UI.Dispatching;
using Microsoft.UI.Xaml.Controls;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace MyWinUiTests;

[TestClass]
public sealed class ViewTests
{
    private bool _initializedOnUiThread;
    private bool _verifyCleanupOnUiThread;

    [TestInitialize]
    public async Task InitializeAsync()
    {
        await Task.Yield();
        _initializedOnUiThread =
            DispatcherQueue.GetForCurrentThread()?.HasThreadAccess == true;
    }

    [TestCleanup]
    public async Task CleanupAsync()
    {
        await Task.Yield();

        if (_verifyCleanupOnUiThread)
        {
            Assert.IsTrue(
                DispatcherQueue.GetForCurrentThread()?.HasThreadAccess == true);
        }
    }

    [UITestMethod]
    public async Task ControlCanBeCreatedAfterAsyncInitialization()
    {
        _verifyCleanupOnUiThread = true;
        await Task.Yield();

        var grid = new Grid();

        Assert.IsTrue(_initializedOnUiThread);
        Assert.IsTrue(grid.DispatcherQueue.HasThreadAccess);
    }
}
```

`[STATestMethod]` can provide an STA thread, but it does not create a WinUI
dispatcher. `[UITestMethod]` dispatches the full MSTest call for each test,
including its setup and cleanup.

## Apply deployment models to UWP and WinUI 3 apps

For UWP and WinUI 3 apps, apply the delta that matches the deployment model
you chose in “Choose the model for UWP and WinUI 3 apps.” `MSTest.Sdk` keeps
the runner setup shared between both models.

### Unpackaged WinUI 3 (default choice)

Add these properties and do not include MSIX manifest or package asset items:

```
<PropertyGroup>
  <WindowsPackageType>None</WindowsPackageType>
  <EnableMsixTooling>false</EnableMsixTooling>
</PropertyGroup>
```

The resulting apphost is a standard executable. As a result,
Microsoft.Testing.Platform uses its normal launch path, and this route does
not use VSTest’s appx runtime provider.

### Packaged full-trust WinUI 3 (when you need identity)

Remove the two unpackaged overrides; do not leave
`<WindowsPackageType>None</WindowsPackageType>` in the project. Retain the
template’s normal `Package.appxmanifest` and package assets. The output then
has MSIX identity, so Windows must register the package layout and activate the
test host by AUMID. It needs a Windows target framework moniker (TFM) at
`10.0.19041.0` or later and Developer Mode or a similar sideloading policy for
unsigned build output.

In addition, `MSTest.Sdk` adds and registers the packaged-app launcher for
packaged WinUI projects. Leave
`TESTINGPLATFORM_PACKAGEDAPP_LAUNCHER` unset. Its default, `auto`, enables the
packaged launch path only when a matching `AppxManifest.xml` describes the
app. Otherwise it keeps the normal, faster launch path with no controller
restart or deployment-copy overhead. The
[WinUI testing guide](https://github.com/microsoft/testfx/blob/main/docs/winui-testing.md)
covers the `always` and `never` overrides for less common scenarios.

**Validate on your CI agent first**

Confirm Developer Mode (or your sideloading policy) and a clean, passing exit code on your own packaged app and CI agent, as covered in “Packaged activation needs machine setup” above, before wiring this into a required gate.

### Run it

Use `dotnet run` for either deployment model. It launches the generated
apphost, which hosts Microsoft.Testing.Platform inside the process that owns
the window and dispatcher:

```
dotnet run
```

The .NET 10 native MTP runner also supports `dotnet test` for either
deployment model:

```
dotnet test --project .\MyWinUiTests.csproj -c Release -a x64
```

For an unpackaged app, you can also launch the generated apphost directly.
However, do not use `dotnet exec`, which puts `dotnet.exe` in the middle and
can break WinUI resource loading.

A window flashes briefly while the test runs, and the console reports a
summary:

```
Passed! - Failed: 0, Passed: 1, Skipped: 0, Total: 1, Duration: 63ms - MyWinUiTests.dll (net10.0-windows10.0.19041.0)
```

The packaged development layout can remain registered after the run. Remove
it when needed by using its manifest `Identity` name:

```
Get-AppxPackage -Name '<package identity name>' |
  Remove-AppxPackage -PreserveApplicationData
```

## Validate UWP and WinUI 3 apps on the target machine

For a packaged test host, a passing build is only the first step. Therefore,
check your actual CI agent image, not just a developer workstation, for a user
context that can register the package, the required Developer Mode or
sideloading policy, and the frameworks declared by the package. Otherwise, a
workstation that already has the UWP framework packages or Windows App SDK
runtime installed can hide a gap that only appears on a clean build agent.

Framework-dependent WinUI 3 apps need the matching Windows App SDK runtime on
the agent. A self-contained WinUI 3 build can remove that machine need, but test
it using the exact package model that will run in CI.

## Start testing UWP and WinUI 3 apps

Use this checklist to start testing UWP and WinUI 3 apps:

1. Select Microsoft.Testing.Platform in `global.json` and use
   `MSTest.Sdk` 4.5.
2. For modern UWP, set `UseUwp` and `PublishAot`. For classic UWP, import
   `MSTest.Sdk` into the existing project. For WinUI 3, set `UseWinUI` and
   choose packaged or unpackaged deployment.
3. Call the generated `MicrosoftTestingPlatformApplication.RunAsync` helper
   from `OnLaunched`. Modern UWP restores `args.Arguments` through
   `PackagedAppExtensions.GetTestApplicationArguments`; WinUI uses process
   arguments. Publish the UI dispatcher where required.
4. Run full-trust WinUI with `dotnet run` or `dotnet test`. Run UWP and
   AppContainer WinUI through the `InvokeTestingPlatform` MSBuild target from
   a non-elevated Developer PowerShell.
5. For packaged and AppContainer models, confirm Developer Mode (or your
   sideloading policy) and run non-elevated on the test agent.

[Get the UWP and WinUI testing guide](https://github.com/microsoft/testfx/blob/main/docs/winui-testing.md)

## One test platform for UWP and WinUI 3 apps

Keep `MSTest.Sdk`, the generated MTP helper, and `[UITestMethod]` across the
Windows app models. Let the SDK choose direct startup for unpackaged
WinUI or the sidecar controller for package registration, AUMID activation,
and AppContainer isolation.

Three takeaways to carry forward:

* Reuse the same MSTest lifecycle and UI-dispatcher tests across UWP and
  WinUI 3.
* Use direct apphost startup for unpackaged WinUI; let MTP register and
  AUMID-activate packaged or AppContainer hosts.
* Validate the exact package model, required frameworks, trust level, and
  machine policy that your CI agents will run.

For more detail, see the [UWP and WinUI testing guide](https://github.com/microsoft/testfx/blob/main/docs/winui-testing.md)
and the [MSTest documentation](https://learn.microsoft.com/dotnet/core/testing/unit-testing-with-mstest).
