---
source: "https://dev.to/nabeelbaghoor/the-unity-native-plugin-bug-is-never-the-call-it-is-the-thread-m24"
title: "The Unity Native Plugin Bug Is Never the Call. It Is the Thread."
author: "Nabeel Hassan"
date_published: "2026-10-20"
date_clipped: "2026-10-21"
category: "Game Development / Unity"
source_type: "rss"
canonical_source: "https://nabeelbaghoor.com/blog/unity-native-plugins-ios-android/"
---

# The Unity Native Plugin Bug Is Never the Call. It Is the Thread.

If you come from web development, a "native bridge" sounds like the scary part of a mobile project. You picture weeks of JNI and Objective-C. In Unity, the actual calls take an afternoon. `AndroidJavaObject` on one side, `DllImport("__Internal")` on the other, done.

Then the plugin ships, and it breaks in ways that have nothing to do with the calls. A callback updates the UI and the app crashes on some devices but not others. The feature works in the development build and silently does nothing in the store build. Someone renames a GameObject and a whole integration stops responding without a single error.

I have written Unity native plugins in a few different contexts: alongside the [Repocket C# SDK at Geonode](https://dev.to/nabeelbaghoor/one-c-core-three-platforms-what-shipping-a-background-networking-sdk-taught-me-5b2a), where I also set up the Unity and Windows CI/CD pipelines, on AR work at ARCortex that sat on ARKit and ARCore, and on a [clinical eye-tracking app at Nystag](https://dev.to/nabeelbaghoor/the-headset-is-the-sensor-building-vr-a-clinician-will-actually-act-on-40li) that depended on a headset vendor's SDK. Different products, same set of bugs. Here is the structure I now use and the places it actually breaks.

## First, check you need one

Every native plugin is code you maintain on two extra platforms, through every Unity upgrade and every OS release. So before writing one, I check that Unity or a maintained package really does not cover it.

You genuinely need native code when a platform API has no Unity wrapper (background execution, network state callbacks, VPN or tunnel APIs, some permissions), when a vendor only ships an `.aar` and an `.xcframework`, or occasionally when latency demands it. If a well-maintained package exists, I use it even if it is heavier than I would like. The abstraction someone else maintains is usually worth more than the control you give up.

## One interface, three implementations

Every native feature gets a single C# interface, and the rest of the app only ever sees that:

```
public interface IDeviceBridge
{
    void Start(string config);
    void Stop();
    event Action<string> StateChanged;
}
```

Behind it sit three implementations, picked by platform defines:

```
#if UNITY_ANDROID && !UNITY_EDITOR
    bridge = new AndroidDeviceBridge();
#elif UNITY_IOS && !UNITY_EDITOR
    bridge = new IosDeviceBridge();
#else
    bridge = new EditorDeviceBridge();
#endif
```

The third one is the important one. None of your native code exists in the editor, so without a fake, every designer who presses Play hits an exception, and every test that touches the feature has to be skipped. With a fake, the feature behaves plausibly in the editor and tests run against it.

It also keeps the native surface small. The Java and Objective-C sides only have to satisfy a handful of methods, not whatever shape the vendor SDK happens to expose. This is the same boundary I used in the Repocket SDK: share the logic, never the platform. The shared code should never learn what a Java class is.

## Android: the calls are easy, the build is not

On Android, the native side is a small Java or Kotlin class in an `.aar` or as source under `Assets/Plugins/Android`. C# reaches it like this:

```
using var activity = new AndroidJavaClass("com.unity3d.player.UnityPlayer")
    .GetStatic<AndroidJavaObject>("currentActivity");
plugin = new AndroidJavaObject("com.example.bridge.DeviceBridge", activity);
plugin.Call("start", config);
```

For callbacks into C#, you can use `UnitySendMessage`, which targets a GameObject and a method by name. I avoid it. It is stringly typed, and both strings break silently on a rename. That is the "nothing responds and nothing errors" bug from the intro. I prefer `AndroidJavaProxy`, which lets C# implement a Java interface directly, so the Java side just calls a listener and the compiler has a chance to help you.

What actually costs time on Android:

- **Gradle dependency conflicts.** Your plugin wants one version of a library, another SDK in the project wants another. Sometimes the build fails. Worse, sometimes it succeeds and crashes at runtime. Declare dependencies through a resolver instead of copying jars around, and give the dependency list one owner.
- **Manifest merging.** Your permissions, services and activities have to survive into the final merged manifest. Read the merged output, not your plugin's manifest.
- **R8 shrinking.** If minification is on, R8 can strip the exact class your C# looks up by name. Anything reached by reflection needs a keep rule.

## iOS: extern "C" and someone has to own the string

On iOS, native code lives in `.m`, `.mm` or Swift files under `Assets/Plugins/iOS`, and everything is statically linked, so C# calls it through P/Invoke against `__Internal`:

```
[DllImport("__Internal")]
private static extern void bridge_start(string config);
```

```
// DeviceBridge.mm (extern "C" needs Objective-C++)
extern "C" void bridge_start(const char* config) {
    NSString* cfg = [NSString stringWithUTF8String:config];
    [[DeviceBridge shared] startWithConfig:cfg];
}
```

Swift works, but it needs a C or Objective-C shim in front because P/Invoke only sees C symbols. Callbacks into C# go through a static function pointer marked `[MonoPInvokeCallback]`. Under IL2CPP it must be static, so you route the result to the right C# object yourself.

The iOS problems:

- **Frameworks.** If your code uses a system framework, the generated Xcode project must link it. Do it in a `PostProcessBuild` script. If you fix it by hand in Xcode, it vanishes on the next build.
- **Info.plist keys.** Camera, microphone, location, local network: each needs a usage description. A missing key is a crash at the moment you ask for permission, or a review rejection. Also add these in post-processing.
- **String ownership.** Returning a `char*` to C# means somebody owns that memory. Copy it into a buffer the C# side is allowed to free, and agree on that convention once for the whole bridge.

## Threading is the bug

If I had to name the single most common failure in Unity native plugins, it is this one. Native callbacks arrive on whatever thread the OS or the SDK chose, and nearly all of the Unity API only works on the main thread.

Touch a `Transform`, start a coroutine or update UI from a network callback thread, and you get an exception, a crash, or my favourite, a bug that only reproduces on some devices. Web developers will recognise the shape: it is like a callback firing outside the event loop you thought you were in.

The fix is boring and non-negotiable. Every callback from native code pushes onto a thread-safe queue, and a `MonoBehaviour` drains it in `Update`:

```
static readonly ConcurrentQueue<Action> mainThread = new();

void Update()
{
    while (mainThread.TryDequeue(out var work)) work();
}
```

No callback touches Unity directly. Ever. Once that rule is in place, the "only on some devices" class of bug mostly disappears, because you have stopped racing the main thread.

The reverse direction needs the same discipline. Do not block the main thread waiting for native work, and design for being paused. On mobile, the OS can suspend you at any moment, which was a large part of what made background networking in the Repocket SDK hard. `OnApplicationPause` is a normal event for a plugin, not an edge case, and I test pause and resume on real devices, not just launch and run.

## The release build is a different program

Release builds use IL2CPP with managed code stripping, and stripping removes code that looks unused. Anything only reached from native code or by reflection, like a callback method or a type the plugin creates by name, can be removed. The result is the second bug from the intro: works in development, silently dead in the store build.

Two defenses. A `link.xml` that preserves the types the bridge needs, and testing the real release configuration on real devices before every release. It is also why native plugins sit at the top of my checklist when [upgrading Unity on a live project](https://dev.to/nabeelbaghoor/a-unity-upgrade-compiles-fine-that-is-the-problem-h0f). They are code Unity cannot see, so they are the first thing an upgrade breaks quietly.

## Let CI build both platforms

A plugin that builds on my laptop proves very little. My laptop has a particular Xcode, a particular Android SDK and a Gradle cache that hides missing dependencies. The only check I trust is a clean machine building both platforms from scratch on every change.

That was a big part of the value of the [Unity CI pipeline](https://dev.to/nabeelbaghoor/your-unity-pipeline-does-not-need-tests-yet-2ib4) at Geonode. A change that compiled for Android but broke iOS, or a post-process script that only worked with one Xcode version, showed up the same day instead of on release day. For plugins, I want CI producing the actual release artifacts, because stripping and manifest merging problems only exist in the final build.

## The checklist I use

Before I call a native feature done:

1. One C# interface, three implementations, including an editor fake.
2. The native layer is thin. It translates; it holds no product logic.
3. Every callback is marshalled to the main thread through a queue.
4. Build configuration is code: Gradle deps, manifest entries, frameworks, Info.plist keys all come from scripts.
5. Stripping is handled with `link.xml` and keep rules, and checked on a release build.
6. Pause and resume are tested on real devices.
7. CI builds both platforms from a clean state on every change.

None of it is clever. That is the point. A native plugin is where two toolchains, two operating systems and two threading models meet, and the goal is for the rest of the team to never have to think about it.

If you have written Unity plugins, I am curious what bit you that is not on this list. My guess is threading, but I would love to be wrong.

*This is adapted from a longer version on my site: [Unity native plugins for iOS and Android](https://nabeelbaghoor.com/blog/unity-native-plugins-ios-android/).*
