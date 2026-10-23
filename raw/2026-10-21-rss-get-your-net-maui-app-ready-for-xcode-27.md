---
source: "https://devblogs.microsoft.com/dotnet/migrate-dotnet-maui-apps-uikit-scene-lifecycle"
title: "Get Your .NET MAUI App Ready for Xcode 27"
author: "Gerald Versluis"
date_published: "2026-10-19"
date_clipped: "2026-10-21"
category: ".NET Ecosystem"
source_type: "rss"
---

# Get Your .NET MAUI App Ready for Xcode 27

Your existing .NET MAUI app builds with Xcode 27, installs on an iPhone running iOS 27, shows its splash screen, and then disappears. Not exactly the grand entrance you were hoping for.

That symptom can have many causes. But if the only thing that changed is that you’re now building with Xcode 27 and running the app on iOS 27, and you see the device log message below, your .NET MAUI app needs a few changes:

```
UIScene life cycle is required for apps built with this SDK.
```

UIKit’s scene lifecycle manages each instance of an app’s user interface, including its windows and transitions between foreground and background states. It works alongside the application lifecycle, which manages the app process as a whole. Apple introduced this model with iOS 13, and .NET MAUI already supports it.

This is an Xcode 27 compatibility requirement, not a broken .NET MAUI lifecycle. Existing .NET MAUI projects might still use only the older application lifecycle because updating .NET MAUI or its workloads doesn’t rewrite their platform files. It’s not specific to the iPhone Duo. Every iOS app built with Xcode 27, on any form factor, needs to adopt this pattern. An existing binary built with an older SDK doesn’t suddenly need this migration just because someone updates their phone.

For a straightforward app, the change is small: a scene delegate and an `Info.plist` entry. The part that deserves your attention is everything you’ve added over the years, such as authentication callbacks, deep links, and App Actions.

That’s where the `maui-xcode27-migration` agent skill comes in. It guides your coding agent through the project checks, the migration, and the verification. You still review the changes, and the manual steps below explain what it’s doing.

## Let an AI agent handle the migration

The [.NET MAUI CLI](https://github.com/dotnet/maui-labs) can install agent skills into your development environment. A skill is a set of instructions and supporting resources for the agent. It’s not another runtime dependency in your app.

The Xcode 27 migration skill requires **Microsoft.Maui.Cli 0.1.0-preview.13.26512.5 or later**. Install that preview release:

```
dotnet tool install --global Microsoft.Maui.Cli --version 0.1.0-preview.13.26512.5
```

If you already have it installed, update it instead:

```
dotnet tool update --global Microsoft.Maui.Cli --version 0.1.0-preview.13.26512.5
```

**Preview tooling**

The .NET MAUI CLI and this skill are experimental and are not covered by the Microsoft Support Policy. The CLI downloads the skill from the public `dotnet/maui-labs` catalog, so catalog discovery and installation require network access.

From your app’s repository, check that the CLI can find the skill and install it for GitHub Copilot CLI:

```
maui ai list skill
maui ai add skill maui-xcode27-migration --env CopilotCli --yes
```

If you use another AI provider, check `maui ai add skill --help` and change the `--env` option accordingly. Run the command from the app repository you want to change, because the skill is installed for that project.

Restart or reload your agent session so it picks up the new skill, then ask:

```
Prepare this .NET MAUI app for Xcode 27. Inspect the project
and toolchain first, preserve custom lifecycle behavior, and validate
the migration. Ask before changing the SDK or dropping support for
older OS versions.
```

You don’t need to name the skill in your request. A compatible agent should pick `maui-xcode27-migration` from the installed skills based on the task. If you want to remove any doubt, feel free to name it explicitly.

The CLI installs the skill, and your coding agent does the migration. There’s no `maui migrate` command in this workflow, and installing the skill on its own doesn’t touch your app.

Prefer to manage the skill directly with GitHub Copilot CLI? Follow the official [GitHub Copilot plugin installation documentation](https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing), then add the `maui-labs` marketplace and install the `dotnet-maui` plugin:

```
copilot plugin marketplace add dotnet/maui-labs
copilot plugin install dotnet-maui@dotnet-maui-labs
```

You can also find the [migration skill directly in the `dotnet/maui-labs` repository](https://github.com/dotnet/maui-labs/tree/main/plugins/dotnet-maui/skills/maui-xcode27-migration). Pick one installation method so you don’t end up with duplicate copies.

## What the skill checks

Before editing anything, the skill should work out which project, .NET SDK, .NET MAUI packages, Apple workloads, and Xcode version you’re actually using. A `global.json`, shared package versions, or an existing custom scene delegate can all change the right approach.

The migration covers:

- **Compatible versions.** Match the Apple workload to Xcode, update the required .NET MAUI packages, and check deployment targets without silently dropping older OS support.
- **Scene configuration.** Add or reconcile the delegate and manifest for the iOS and Mac Catalyst targets, including configuration-specific plist files. Preserve existing scene customizations, launch-screen settings, and multi-window behavior.
- **Custom behavior.** Review app-delegate overrides as well as lifecycle registrations, authentication, warm and cold links, notification taps, startup work that needs a window, and App Actions.
- **Verification.** Run a read-only lifecycle audit, review the diff, build the affected targets, and test launch and the behaviors the migration can change. Report anything that could not be exercised.

Commit or otherwise save your current work before starting, and go through the resulting diff before accepting it. A successful build doesn’t prove that an authentication redirect or a Home screen shortcut still works.

If you’d rather do things by hand, the instructions are below.

## Before you start: check your app and toolchain

Scene lifecycle support was available before Xcode 27, so your app might already use it. If you already have a `MauiUISceneDelegate` and matching scene manifest, good news: you can skip the migration steps below. You should still check the toolchain versions and test your app on iOS 27.

At the time of writing, the released .NET 10 iOS and Mac Catalyst workloads **27.0.10722 require Xcode 27.0**. Installing a newer Xcode doesn’t automatically make it compatible with that workload. Check the [.NET for iOS and Mac Catalyst release notes](https://github.com/dotnet/macios/releases/tag/dotnet-10.0.1xx-xcode27.0-10722) and use the matching versions rather than disabling the SDK’s Xcode check.

**Check your setup**

Run `maui doctor` for a quick check of your active .NET SDK, .NET MAUI workload, selected Xcode, and Apple SDK compatibility. It also checks supporting components such as the Xcode license, command-line tools, and installed iOS runtimes.

For a .NET 10 app, update your .NET MAUI packages to **10.0.110 or higher** before enabling scenes. The two-file launch fix can work with an older .NET MAUI version because `MauiUISceneDelegate` already exists there. However, 10.0.110 also includes the scene-side App Actions dispatch and relevant `WebAuthenticator` forwarding. Treat the package update as part of the migration, otherwise you might fix the launch and silently break those integrations.

Template projects often get `$(MauiVersion)` from the installed workload. To pin the minimum version explicitly, add this to your `.csproj`:

```
<PropertyGroup>
  <MauiVersion>10.0.110</MauiVersion>
</PropertyGroup>
```

If you already manage this version elsewhere, update that value instead. Don’t downgrade a newer compatible version.

Apps created with the .NET MAUI 10.0.110 templates already have the scene configuration. Existing projects aren’t retrofitted by a package or workload update, so you’ll need to do that part yourself.

## Add the scene delegate

In your existing app, create `Platforms/iOS/SceneDelegate.cs` and paste in this code. If the file already exists, check its base class and registration instead of adding a second delegate:

```
using Foundation;
using Microsoft.Maui;

namespace MyMauiApp;

[Register("SceneDelegate")]
public class SceneDelegate : MauiUISceneDelegate
{
}
```

Replace `MyMauiApp` with your app’s namespace. For this default setup, keep the class public and the registration name as `SceneDelegate`. If your app already has a custom registered scene delegate, preserve its behavior and use its registered name consistently in the manifest instead of adding a competing delegate.

Yes, that’s the whole class. .NET MAUI does the actual window setup for you. Leave your existing `AppDelegate : MauiUIApplicationDelegate` exactly where it is too. The scene delegate works alongside it, not instead of it.

## Add the scene manifest

Open `Platforms/iOS/Info.plist` as XML and add the following inside the root `<dict>`. If you already have a `UIApplicationSceneManifest`, update its existing scene configuration instead of adding a duplicate key:

```
<key>UIApplicationSceneManifest</key>
<dict>
  <key>UIApplicationSupportsMultipleScenes</key>
  <false/>
  <key>UISceneConfigurations</key>
  <dict>
    <key>UIWindowSceneSessionRoleApplication</key>
    <array>
      <dict>
        <key>UISceneConfigurationName</key>
        <string>__MAUI_DEFAULT_SCENE_CONFIGURATION__</string>
        <key>UISceneDelegateClassName</key>
        <string>SceneDelegate</string>
      </dict>
    </array>
  </dict>
</dict>
```

Three details matter here:

- Keep `__MAUI_DEFAULT_SCENE_CONFIGURATION__` exactly as shown. That’s the name .NET MAUI expects.
- Match the delegate name in the plist with the C# registration: `SceneDelegate` and `[Register("SceneDelegate")]` in this example.
- Leave `UIApplicationSupportsMultipleScenes` set to `false` unless your app really supports multiple windows.

You don’t need a `UISceneStoryboardFile`. .NET MAUI creates the window in code, and your existing splash screen configuration stays as it is.

If you have custom scene configuration names or override `GetConfiguration` or `WillConnect`, review them together rather than replacing the manifest wholesale. The default `MauiUISceneDelegate` window-creation path expects `__MAUI_DEFAULT_SCENE_CONFIGURATION__`; a different name needs an existing custom implementation that handles window creation.

Some apps select a different plist for Debug, Release, customer, or environment builds. Add or reconcile the manifest in every plist that can produce a shipping app. If you only update the default file, one configuration can still crash right after the splash screen. Preserve the existing `MauiSplashScreen` or `UILaunchStoryboardName` setup while editing these files.

That’s the iOS scene configuration done. If you don’t target Mac Catalyst, skip ahead to the minimum OS versions.

## Do the same for Mac Catalyst

If your project also targets Mac Catalyst, make the same two changes there:

1. Add `Platforms/MacCatalyst/SceneDelegate.cs`.
2. Add the same `UIApplicationSceneManifest` section to `Platforms/MacCatalyst/Info.plist`.

## Check your minimum OS versions

The .NET for iOS and .NET for Mac Catalyst 27 SDKs also raise the minimum supported versions: iOS needs at least `15.0`, and Mac Catalyst needs at least `17.0` (macOS 14 Sonoma). In your app’s `.csproj`, update the existing `SupportedOSPlatformVersion` entries if yours are lower:

```
<SupportedOSPlatformVersion Condition="$([MSBuild]::GetTargetPlatformIdentifier('$(TargetFramework)')) == 'ios'">15.0</SupportedOSPlatformVersion>
<SupportedOSPlatformVersion Condition="$([MSBuild]::GetTargetPlatformIdentifier('$(TargetFramework)')) == 'maccatalyst'">17.0</SupportedOSPlatformVersion>
```

These entries belong inside a `<PropertyGroup>`. Replace the existing values instead of adding duplicates, because a later definition can override your change. Keep each version directly between its XML tags, without leading or trailing whitespace.

Keep a higher deployment target if your app already requires one. If you must retain support for iOS versions below 15 or macOS 12 and 13, moving to these SDKs requires a support-policy decision. Stay on a compatible 26.x SDK while you decide, rather than silently dropping those users. This SDK minimum is separate from scene adoption; see the [.NET MAUI template deployment-target guidance](https://github.com/dotnet/maui/blob/main/src/Templates/README.md#mac-catalyst-deployment-target).

## Check any custom app behavior

With scenes enabled, UIKit no longer calls the `AppDelegate` activation, backgrounding, URL, and user-activity callbacks. That goes for both `ConfigureLifecycleEvents` registrations and methods you override in `AppDelegate`, such as `OpenUrl` or `ContinueUserActivity`. Move that logic to the corresponding scene events:

| Existing event | Scene event |
| --- | --- |
| `OnActivated` | `SceneOnActivated` |
| `OnResignActivation` | `SceneOnResignActivation` |
| `DidEnterBackground` | `SceneDidEnterBackground` |
| `WillEnterForeground` | `SceneWillEnterForeground` |
| `OpenUrl` | `SceneOpenUrl` |
| `ContinueUserActivity` | `SceneContinueUserActivity` |

The callback arguments differ, so move the logic instead of just renaming the registration. If you instead override methods in your `SceneDelegate`, call the corresponding `base` implementation. The framework’s window setup, lifecycle events, and authentication forwarding depend on that behavior.

For custom deep links, also handle `SceneWillConnect`: URLs and user activities that launch the app arrive in its `UISceneConnectionOptions`. That callback runs before .NET MAUI creates the window, so defer navigation until the window is ready.

If your app opens content from a notification tap, inspect `connectionOptions.NotificationResponse` as another cold-start input. Preserve that route separately from ordinary push registration and `DidReceiveRemoteNotification`, which remain application-level callbacks.

A regular launch may have no URL or user-activity payload. Guard against absent `UrlContexts` and `UserActivities` before enumerating them, even when the binding’s nullability annotation suggests a value will be there.

`FinishedLaunching` still runs, but the standard .NET MAUI scene path creates the window later through the scene delegate. `AppDelegate.Window` stays `null`. Code that accesses it after `base.FinishedLaunching` needs to use the appropriate scene window when it is ready instead. The cross-platform `Window` lifecycle events keep working; do not duplicate that forwarding.

.NET MAUI 10.0.110 handles scene-based App Actions and forwards the relevant URL and user-activity callbacks to `WebAuthenticator`. That authentication handling is not general app deep-link navigation and does not replay cold-start links for you. Test authentication and your own links with the app both running and fully closed.

If you use App Actions, make sure every custom `PerformActionForShortcutItem` handler calls its completion callback **exactly once**. Pass `true` when the action was handled and `false` when it was not. A handler can respond asynchronously after returning, but returning alone does not acknowledge the action.

Even a handler that only writes a log message needs to respond. As an example, add `using Microsoft.Maui.LifecycleEvents;` to `MauiProgram.cs`, then register this observer inside `CreateMauiApp`, before `return builder.Build();`:

```
builder.ConfigureLifecycleEvents(events =>
{
#if IOS || MACCATALYST
    events.AddiOS(ios => ios
        .PerformActionForShortcutItem((application, shortcutItem, completion) =>
        {
            Console.WriteLine($"App Action received: {shortcutItem.Type}");
            completion(false);
        }));
#endif
});
```

The default .NET MAUI builder already forwards App Actions to Essentials. You don’t need this logging observer unless you want it, and you shouldn’t add another `Platform.PerformActionForShortcutItem` registration. If your `AppDelegate` overrides `PerformActionForShortcutItem`, that override is no longer called with scenes enabled. Move its custom logic into a registration like the one above, completion callback included.

## Rebuild and try it

Restore and build the iOS target:

```
dotnet restore -p:TargetFramework=net10.0-ios
dotnet build -f net10.0-ios --no-restore
```

If the simulator still seems to have an old version of your app, uninstall it, delete the app project’s `bin` and `obj` folders, and run those two commands again.

Launch both Debug and Release builds on a regular iPhone or iPad simulator running iOS 27 with the matching workload and Xcode. A successful build or launch on iOS 26 doesn’t prove that the app will launch on iOS 27 when built with Xcode 27. Check a cold launch, background and foreground transitions, your authentication flow, links and notification taps with the app both running and closed, and App Actions. If you target Mac Catalyst, build and exercise that target too.

You don’t need an iPhone Duo simulator to verify this migration. Device-specific layouts and the Xcode 27.1 tooling are a separate topic that we’ll cover in a follow-up post soon.
