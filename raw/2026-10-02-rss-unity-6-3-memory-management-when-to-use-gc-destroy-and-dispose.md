---
source: "https://dev.to/gamedevtoollab/unity-63-memory-management-when-to-use-gc-destroy-and-dispose-4dec"
title: "Unity 6.3 Memory Management: When to Use GC, Destroy, and Dispose"
author: "GameDevToolLab"
date_published: "2026-10-02"
date_clipped: "2026-10-02"
category: "Game Development / Unity"
source_type: "rss"
---

# Unity 6.3 Memory Management: When to Use GC, Destroy, and Dispose

##
[
](#introduction)
Introduction

Should you assign `null`

, call `Destroy`

, or use `Dispose`

? What about `Resources.UnloadUnusedAssets`

and `GC.Collect`

?

The confusion starts when **dropping a C# reference, destroying a Unity object, and releasing an acquired asset reference** are treated as the same operation. Unity uses several kinds of memory; garbage collection does not manage them all.[1](#fn1)

This guide starts with how a resource was acquired, who owns it, and how long it remains in use. The goal is to prevent both leaks and premature cleanup of resources that someone still needs.


Scope and validation:This article targetsUnity 6.3 LTS (6000.3)and conventional GameObject/MonoBehaviour development. The Japanese source records a documentation review datedSeptember 15, 2026, using Addressables 2.10, Collections 2.6, and Memory Profiler 1.1 documentation. Package versions are separate from the Editor version. Entities-specific lifecycles and native plugin internals are outside this article's scope.An independent review of the Japanese version reported successful compilation of the four complete C# examples in

Unity 6000.3.22f1, Addressables 2.10.3, and Collections 2.6.3. That report is not a runtime test. This English edition has not been recompiled, run in a Player, or measured on a target device; comments and diagnostic messages have been translated.

##
[
](#1-choose-the-cleanup-method-by-acquisition-not-just-type)
1. Choose the cleanup method by acquisition, not just type

Unity distinguishes managed memory, C# unmanaged memory, and native memory. Allocations accessed through `NativeArray`

and similar APIs may appear under native memory in the Profiler. **C# garbage collection cannot reclaim every kind of Unity or GPU resource.** IL2CPP still uses garbage collection for managed memory.[1](#fn1)

| How the resource was acquired | Normal cleanup | Common mistake |
|---|---|---|
Ordinary C# object, array, or `List<T>`
|
Remove unnecessary references; let GC reclaim it | Expecting `null` to free memory immediately |
GameObject from `Object.Instantiate`
|
`Destroy` the instance you own |
Treating deactivation as destruction |
| Material, Mesh, Texture2D, or ScriptableObject you created | The owner calls `Destroy`
|
Destroying a shared asset you only reference |
`Addressables.LoadAssetAsync` |
`Addressables.Release` the acquired handle |
Calling `Destroy` on the asset instead |
Instance from `Addressables.InstantiateAsync`
|
Use `Addressables.ReleaseInstance` for manual cleanup |
Confusing it with an ordinary `Instantiate` clone |
`NativeArray` or similar allocation you own |
`Dispose` , respecting allocator lifetime and Job dependencies |
Disposing borrowed views or copies twice |
Owned object from `new RenderTexture`
|
Stop using it; `Destroy` for final cleanup, `Release` for GPU resources only |
Assuming `Release` destroys the object |
`RenderTexture.GetTemporary` |
`RenderTexture.ReleaseTemporary` |
Destroying a borrowed resource |
`GraphicsBuffer` or `ComputeBuffer` you created |
`Dispose` or the corresponding `Release`
|
Only dropping the C# reference |
Owned file, network, or other `IDisposable` resource |
`using` or `Dispose`
|
Assuming the interface executes cleanup automatically |

The following sections provide the API references. The rule is: **pair acquisition with the matching cleanup, at the end of the agreed lifetime.** When passing a resource elsewhere, distinguish ownership transfer from borrowing.

A generated `Texture2D`

and one loaded through Addressables have the same type but different cleanup requirements. Avoid a generic `ReleaseEverything(UnityEngine.Object obj)`

that decides solely from the type.

##
[
](#2-why-memory-remains-even-with-garbage-collection)
2. Why memory remains even with garbage collection

###
[
](#assigning-raw-null-endraw-removes-one-reference)
Assigning `null`

removes one reference

An ordinary C# object becomes eligible for collection when it is no longer reachable. Setting one variable to `null`

does not help while another reference keeps it alive.[2](#fn2)


```
var data = new byte[1024 * 1024];
var anotherReference = data;
data = null;
// anotherReference still refers to the same array.
// Setting data to null does not remove that other reference.
Debug.Log(anotherReference.Length);
```


Common retention paths include static collections and persistent services holding scene objects. Closing a screen does not remove references from those longer-lived owners, which can also retain the objects' associated data.

Ask **what still keeps the object reachable**, not whether you wrote `null`

. Memory Profiler identifies unintended references and missing cleanup as common causes of leaks.[3](#fn3)

###
[
](#-raw-listlttgtclear-endraw-does-not-discard-capacity)
`List<T>.Clear()`

does not discard capacity

`Clear()`

sets the count to zero and removes references held by the elements, but retains `Capacity`

. Consider `TrimExcess()`

or changing `Capacity`

separately when reducing the backing storage is appropriate.[4](#fn4)


```
// Assume items is a List<ItemData> held by this class.
items.Clear();
// Consider this only at a boundary where large capacity is no longer needed.
items.TrimExcess();
```


Shrinking every frame only to grow again adds unnecessary work. Keep capacity for reusable working buffers; consider shrinking after unusually large temporary workloads at a screen or session boundary.

Also, `List<GameObject>.Clear()`

does not destroy its GameObjects, and `List<IDisposable>.Clear()`

does not dispose its elements. **Cleaning up each resource and removing collection references are separate steps.**

###
[
](#-raw-dispose-endraw-is-not-another-name-for-gc)
`Dispose`

is not another name for GC

`IDisposable`

defines explicit resource cleanup. GC does not discover the interface and automatically call `Dispose()`

. The caller must arrange it through `using`

or `try/finally`

.[5](#fn5)

Implementing `IDisposable`

on a `MonoBehaviour`

likewise does not make `Destroy`

call it. Connect disposal to your component's cleanup path explicitly.

##
[
](#3-what-raw-destroy-endraw-doesand-does-notdestroy)
3. What `Destroy`

does—and does not—destroy

###
[
](#gameobject-destruction-is-separate-from-asset-cleanup)
GameObject destruction is separate from asset cleanup

`Destroy(gameObject)`

destroys that GameObject, its components, and its Transform children. It does not recursively destroy every Material or Texture referenced by those components.[6](#fn6)[7](#fn7)

Ten character instances may share one Material and Texture. Destroying those assets when one character dies would break the other nine. Keep **instance lifetime** separate from **shared asset lifetime**.

Actual destruction is deferred until after the current Update loop. Do not diagnose a leak from a measurement immediately after calling `Destroy`

, or replace it with `DestroyImmediate`

in runtime code. Account for deferred destruction in the lifecycle instead.[6](#fn6)

###
[
](#unitys-raw-null-endraw-does-not-only-mean-no-c-reference)
Unity's `== null`

does not only mean “no C# reference”

A `UnityEngine.Object`

has a managed object and a corresponding native object. After native destruction, the managed object can remain: Unity's `== null`

may be `true`

while `ReferenceEquals(obj, null)`

is `false`

.[8](#fn8)

A destroyed component retained in a static field can still keep its large managed arrays alive. Memory Profiler exposes this kind of state as a `Leaked Managed Shell`

.[9](#fn9)

Use Unity's operator when testing a Unity object's lifetime:


```
if (target != null)
{
target.DoSomething();
}
```


The `?.`

and `??`

operators do not perform Unity's destroyed-object check. `target?.DoSomething()`

is not a safe guard against a destroyed component. This does not prohibit those operators on ordinary C# objects.[8](#fn8)

###
[
](#putting-everything-in-raw-ondestroy-endraw-is-not-enough)
Putting everything in `OnDestroy`

is not enough

Choose cleanup points according to the required lifetime.

| Required lifetime | Acquisition and cleanup |
|---|---|
| Only while enabled | Start in `OnEnable` ; end in `OnDisable`
|
| While the component exists | Acquire during initialization; use explicit cleanup / `OnDestroy`
|
| One operation |
`using` or `try/finally`
|
| Across multiple screens or scenes | An explicit, longer-lived owner |

`OnDestroy`

is only called for GameObjects that were previously active. If another system injects resources into an object that remains inactive, that system needs an explicit cleanup path rather than relying only on `OnDestroy`

.[10](#fn10)

The examples below are ordinary runtime components. `ExecuteAlways`

and Editor extensions require cleanup paths beyond normal Play Mode lifecycles.

##
[
](#4-track-the-materials-meshes-and-textures-you-create)
4. Track the Materials, Meshes, and Textures you create

###
[
](#some-getters-can-create-instances)
Some getters can create instances

`renderer.material`

can instantiate a Material. The first access to `MeshFilter.mesh`

can duplicate an existing Mesh or create a new one. Cleanup of the generated objects is your responsibility.[7](#fn7)[11](#fn11)

This does **not** mean every read of the same Renderer's `material`

creates another Material. The risk is overlooking the initial instantiation or later replacement and recreation.

For reference-only access, consider `sharedMaterial`

and `sharedMesh`

. Changes to shared objects affect other users; sharing is not permission to modify them indiscriminately.

###
[
](#example-destroy-only-the-material-you-explicitly-cloned)
Example: destroy only the Material you explicitly cloned

Save this as `RuntimeMaterialOwner.cs`

and attach it to a MeshRenderer with one Material. This component assumes exclusive control of the Renderer's first Material slot.


```
using UnityEngine;
[RequireComponent(typeof(MeshRenderer))]
public sealed class RuntimeMaterialOwner : MonoBehaviour
{
private MeshRenderer _renderer;
private Material _originalMaterial;
private Material _ownedMaterial;
private void Awake()
{
_renderer = GetComponent<MeshRenderer>();
_originalMaterial = _renderer.sharedMaterial;
if (_originalMaterial == null)
{
Debug.LogError("Assign a source Material to clone.", this);
return;
}
// Create the owned Material explicitly instead of relying on an implicit clone.
_ownedMaterial = new Material(_originalMaterial)
{
name = _originalMaterial.name + " (Owned Runtime)"
};
_renderer.sharedMaterial = _ownedMaterial;
}
public void ReleaseOwnedMaterial()
{
Material owned = _ownedMaterial;
_ownedMaterial = null;
if (_renderer != null &&
_renderer.sharedMaterial == owned && owned != null)
{
_renderer.sharedMaterial = _originalMaterial;
}
_originalMaterial = null;
if (owned != null)
{
Destroy(owned);
}
}
private void OnDestroy()
{
ReleaseOwnedMaterial();
}
}
```


Cleanup destroys **the Material recorded when it was created**, without accessing `renderer.material`

again. Calling `ReleaseOwnedMaterial()`

before `OnDestroy`

leaves the ownership field empty, so the later call does not destroy it again.

Do not share this owned Material with other objects. To share it, move ownership to something that outlives every user. Cloning a Material does not give you ownership of its Textures. Retain any Addressables handles needed while the source assets are used.

Apply the same pattern to `new Mesh`

, `new Texture2D`

, and `ScriptableObject.CreateInstance`

. Do not include Inspector-assigned shared assets in this cleanup indiscriminately.

##
[
](#5-match-addressables-acquisitions-with-releases)
5. Match Addressables acquisitions with releases

###
[
](#-raw-release-endraw-relinquishes-an-acquired-reference)
`Release`

relinquishes an acquired reference

Addressables tracks assets and AssetBundles with its own reference counts. Explicit loads need corresponding releases; assigning a C# variable to `null`

does not decrement those counts.[12](#fn12)

Retain a handle while using its result. Copying the handle does not acquire an independent reference. An additional owner needs an explicit acquisition, such as a separate load or the documented `Acquire`

operation, and a matching release.[13](#fn13)

`IsValid()`

is **not an ownership flag telling you whether your caller still owes a release**. Another user can retain the same underlying operation. Track your own ownership and released state separately.

###
[
](#example-release-a-screens-acquisition-even-during-loading)
Example: release a screen's acquisition even during loading

Save this as `AddressableRawImage.cs`

and attach it to a UGUI RawImage. Install UGUI and Addressables, mark a Texture as Addressable, and set its address. This component alone writes the RawImage's `texture`

, retaining the asset only while the component is active and enabled.


```
using UnityEngine;
using UnityEngine.AddressableAssets;
using UnityEngine.ResourceManagement.AsyncOperations;
using UnityEngine.UI;
[RequireComponent(typeof(RawImage))]
public sealed class AddressableRawImage : MonoBehaviour
{
[SerializeField] private string _address;
private RawImage _image;
private AsyncOperationHandle<Texture2D> _handle;
private bool _ownsHandle;
private void Awake()
{
_image = GetComponent<RawImage>();
}
private void OnEnable()
{
if (string.IsNullOrWhiteSpace(_address))
{
Debug.LogError("Set the Texture address.", this);
return;
}
_handle = Addressables.LoadAssetAsync<Texture2D>(_address);
_ownsHandle = true;
_handle.Completed += OnCompleted;
}
private void OnCompleted(AsyncOperationHandle<Texture2D> handle)
{
if (!_ownsHandle || !handle.Equals(_handle))
{
return;
}
if (handle.Status != AsyncOperationStatus.Succeeded)
{
string error = handle.OperationException?.Message
?? "Unknown loading error";
ReleaseLoad();
Debug.LogError($"Failed to load Texture: {error}", this);
return;
}
if (_image == null)
{
ReleaseLoad();
return;
}
_image.texture = handle.Result;
}
private void ReleaseLoad()
{
if (!_ownsHandle)
{
return;
}
var handle = _handle;
_ownsHandle = false;
_handle = default;
// Stop using the asset before releasing the handle.
if (_image != null)
{
_image.texture = null;
}
if (handle.IsValid())
{
handle.Completed -= OnCompleted;
Addressables.Release(handle);
}
}
private void OnDisable() => ReleaseLoad();
private void OnDestroy() => ReleaseLoad();
}
```


The example releases failed operations as well as successful ones: failed handles still have operation instance data to release.[13](#fn13)

Releasing before completion does not immediately cancel the underlying load. Addressables allows a pending acquisition to be released, with cleanup occurring after completion. The example also removes the callback so it cannot update a closed screen.[14](#fn14)

###
[
](#do-not-confuse-ordinary-raw-instantiate-endraw-with-raw-instantiateasync-endraw-)
Do not confuse ordinary `Instantiate`

with `InstantiateAsync`


Cloning a Prefab loaded through `LoadAssetAsync<GameObject>`

with ordinary `Object.Instantiate`

**does not automatically increment Addressables' reference count for that clone**. Releasing the load handle while clones remain can invalidate the lifetimes of their dependent Materials and Textures.[15](#fn15)

Keep the Prefab load handle until all owned clones have finished being destroyed. Because `Destroy`

is deferred, do not release the final handle immediately after requesting destruction. Inactive instances waiting in a pool still count as users.

For manual cleanup of `Addressables.InstantiateAsync`

instances, use `ReleaseInstance`

. With the default `trackHandle: true`

, you can pass the instance; with `false`

, retain the operation handle and pass it to `ReleaseInstance(handle)`

instead. Do not release twice through different cleanup paths.[16](#fn16)[17](#fn17)

Scene unloading can automatically release instances created with `trackHandle: true`

. That does not mean every asset separately acquired through `LoadAssetAsync`

is automatically released too.[18](#fn18)

###
[
](#a-zero-reference-count-does-not-guarantee-an-immediate-memory-drop)
A zero reference count does not guarantee an immediate memory drop

An asset whose reference count reaches zero may remain in memory while another asset in the same AssetBundle is still used. Inspect asset and Bundle dependencies, not only individual counts.[12](#fn12)

Packing persistent assets and large screen-specific assets together makes their lifetimes harder to separate. Once acquisitions and releases balance, consider grouping Bundle contents by lifetime.

##
[
](#6-unloading-a-scene-is-not-the-same-as-unloading-unused-assets)
6. Unloading a scene is not the same as unloading unused assets

###
[
](#-raw-unloadsceneasync-endraw-does-not-unload-every-asset)
`UnloadSceneAsync`

does not unload every asset

`SceneManager.UnloadSceneAsync`

destroys the GameObjects belonging to the scene and removes it from SceneManager. The API explicitly states that assets are not unloaded by this operation alone.[19](#fn19)

For ordinary scene management, consider waiting for scene unloading, removing unnecessary references, then waiting for `Resources.UnloadUnusedAssets()`

at a suitable loading-screen boundary.


```
// Excerpt from a coroutine.
// sceneToUnload is a loaded Scene managed by ordinary SceneManager APIs.
// Run this outside the scene being unloaded, with another scene kept loaded.
var unload = UnityEngine.SceneManagement.SceneManager
.UnloadSceneAsync(sceneToUnload);
if (unload != null)
{
yield return unload;
}
// By this point, owners must have cleared unnecessary caches and references.
yield return Resources.UnloadUnusedAssets();
```


For Addressables-loaded scenes, use Addressables' scene-unloading API and handle management instead. This snippet is not a replacement for that cleanup.[18](#fn18)

###
[
](#-raw-unloadunusedassets-endraw-is-not-a-universal-free-everything-button)
`UnloadUnusedAssets`

is not a universal “free everything” button

`Resources.UnloadUnusedAssets`

examines references through the GameObject hierarchy, script components, and static variables to identify unused assets. A long-lived cache may keep an otherwise unnecessary asset referenced.[20](#fn20)

**The script execution stack is not examined.** Do not equate this with C# GC reachability and assume a local variable protects the asset. Keep required assets in references Unity tracks, such as fields on an appropriate owner; preserve the corresponding Addressables acquisition too.[20](#fn20)

Do not make this a per-frame cleanup operation. Measure its necessity and cost at suitable transitions. Following it with `GC.Collect()`

still does not reclaim every category of memory.

###
[
](#direct-asset-and-assetbundle-unloading-also-requires-ownership)
Direct asset and AssetBundle unloading also requires ownership

`Resources.UnloadAsset`

targets assets stored on disk and invalidates the specified asset. Ensure no other user still needs it. It is not a general cleanup API for arbitrary runtime-created objects.[21](#fn21)

For manually managed AssetBundles, `Unload(false)`

leaves loaded assets alive; `Unload(true)`

destroys them and can break active users. Unloading with `false`

and reloading can also produce duplicate assets. Do not manually unload Bundles owned by Addressables.[22](#fn22)

##
[
](#7-manage-raw-nativearray-endraw-ownership-alongside-its-final-job-dependency)
7. Manage `NativeArray`

ownership alongside its final Job dependency

###
[
](#respect-the-allocators-lifetime)
Respect the allocator's lifetime

Using an unmanaged allocation from C# does not make GC responsible for it. Collections allocators have different lifetime requirements.[23](#fn23)

| Allocator | Lifetime and constraints |
|---|---|
`Temp` |
Use within the allocating thread and scope. Main-thread allocations are reclaimed at the end of the frame; Job-local allocations at the end of that Job. Do not pass main-thread Temp allocations into Jobs. |
`TempJob` |
Dispose within four frames of allocation. The deadline is not a promise of automatic, safe cleanup. |
`Persistent` |
Retain as long as needed, then dispose explicitly. |

Avoid keeping `Temp`

allocations across network waits or `await`

. A short-lived allocation must not depend on an unpredictable delay.

###
[
](#example-dispose-only-after-the-job-completes)
Example: dispose only after the Job completes

Save this as `NativeJobOwner.cs`

and attach it to a GameObject. It owns an array while enabled and waits for the array's Job before disposing on disable.


```
using Unity.Collections;
using Unity.Jobs;
using UnityEngine;
public sealed class NativeJobOwner : MonoBehaviour
{
private NativeArray<int> _values;
private JobHandle _lastUse;
private struct FillJob : IJobParallelFor
{
public NativeArray<int> Values;
public void Execute(int index)
{
Values[index] = index * 2;
}
}
private void OnEnable()
{
_values = new NativeArray<int>(256, Allocator.Persistent);
try
{
_lastUse = new FillJob { Values = _values }
.Schedule(_values.Length, 64);
}
catch
{
ReleaseOwnedData();
throw;
}
}
private void ReleaseOwnedData()
{
if (!_values.IsCreated)
{
return;
}
// Wait for the last Job using the array before disposing it.
_lastUse.Complete();
_values.Dispose();
_values = default;
_lastUse = default;
}
private void OnDisable() => ReleaseOwnedData();
private void OnDestroy() => ReleaseOwnedData();
}
```


`Complete()`

blocks the caller when necessary. This example prioritizes safe cleanup. When several Jobs use the allocation, combine their dependencies so `_lastUse`

really represents every outstanding user.[24](#fn24)

To defer waiting, `Dispose(JobHandle)`

can schedule a disposal Job. After scheduling disposal, do not pass the array to new work, and track the returned handle. Complete the disposal Job at the appropriate shutdown or synchronization boundary.[25](#fn25)


```
// values is an owned NativeArray; lastUse includes all Jobs that use it.
JobHandle disposal = values.Dispose(lastUse);
values = default;
// Do not use values or any aliases after scheduling disposal.
// To avoid waiting here, retain disposal in the owner and Complete it later.
disposal.Complete();
```


###
[
](#copying-the-struct-does-not-duplicate-the-allocation)
Copying the struct does not duplicate the allocation

Here, `a`

and `b`

do not own separate array storage:


```
var a = new NativeArray<int>(16, Allocator.Persistent);
var b = a;
a.Dispose();
// Invalid: b.Dispose(); This tries to dispose the same allocation through a copy.
// Invalid: Debug.Log(b[0]); This tries to access memory already disposed.
b = default;
```


Disposal updates `IsCreated`

on the struct being disposed, not every copy. Another copy may still report `true`

. **An IsCreated check does not make disposal through arbitrary copies safe.**


[23](#fn23)Similarly, `Texture2D.GetRawTextureData<T>()`

returns a direct `NativeArray`

view of the Texture's data. Do not dispose it as an owned allocation, and respect invalidation caused by modifying or destroying the Texture. The non-generic `GetRawTextureData()`

overload instead returns a `byte[]`

copy; the shared name does not imply shared ownership rules.[26](#fn26)

##
[
](#8-gpu-resources-need-more-than-dropping-c-references)
8. GPU resources need more than dropping C# references

###
[
](#rendertexture-raw-release-endraw-and-raw-destroy-endraw-have-different-roles)
RenderTexture `Release`

and `Destroy`

have different roles

`RenderTexture.Release()`

frees hardware resources but does not destroy the RenderTexture object. Using it again can recreate those GPU resources.[27](#fn27)

For a RenderTexture you created with `new RenderTexture`

, final cleanup might look like this:


```
// Cleanup excerpt. This owner created _ownedRt with new RenderTexture.
// This example assumes the Camera is the only consumer.
if (_ownedRt != null)
{
if (_camera != null && _camera.targetTexture == _ownedRt)
{
_camera.targetTexture = null;
}
if (RenderTexture.active == _ownedRt)
{
RenderTexture.active = null;
}
_ownedRt.Release();
Destroy(_ownedRt);
_ownedRt = null;
}
```


This explicitly releases GPU storage before destroying the object. It does not mean every final `Destroy`

requires a preceding `Release`

. Distinguish **releasing GPU storage for later reuse** from **ending the object's lifetime**.

Also stop use through RawImage, Materials, global Shader properties, or other consumers. Do not apply this cleanup to a RenderTexture owned by someone else.

###
[
](#return-raw-gettemporary-endraw-resources-with-raw-releasetemporary-endraw-)
Return `GetTemporary`

resources with `ReleaseTemporary`


`RenderTexture.GetTemporary`

borrows from Unity's internal pool. Return it with `ReleaseTemporary`

, including on exceptions or early returns.[28](#fn28)


```
// Synchronous temporary-work excerpt, not a rendering pipeline RenderPass.
RenderTexture previous = RenderTexture.active;
RenderTexture temporary = RenderTexture.GetTemporary(256, 256, 0);
try
{
RenderTexture.active = temporary;
GL.Clear(true, true, Color.clear);
// Perform temporary work that finishes within this scope.
}
finally
{
RenderTexture.active = previous;
RenderTexture.ReleaseTemporary(temporary);
}
```


Do not keep using a cached reference after returning it, or destroy the borrowed RenderTexture yourself. Another operation may reuse it after return.

###
[
](#explicitly-clean-up-graphicsbuffer-and-computebuffer)
Explicitly clean up GraphicsBuffer and ComputeBuffer

Call `Dispose`

or the corresponding `Release`

on buffers you created when they are no longer used. Dropping C# references is not sufficient GPU resource management.[29](#fn29)[30](#fn30)

First stop scheduling rendering or compute work that uses the buffer. Async GPU readback and other outstanding operations can extend its required lifetime beyond the screen that requested it.

URP Render Graph also distinguishes resources created inside the graph from imported external resources. Do not independently destroy graph-managed resources, or assume importing a resource transfers ownership of a custom RTHandle to the graph.[31](#fn31)

###
[
](#discard-cpu-copies-only-when-you-no-longer-need-cpu-access)
Discard CPU copies only when you no longer need CPU access

Runtime-generated Textures and Meshes may retain CPU copies alongside GPU data. Once CPU reads and edits are finished, these APIs can discard that storage:[32](#fn32)[33](#fn33)


```
// Only after creation and editing are finished, with no further CPU reads or writes.
texture.Apply(updateMipmaps: true, makeNoLongerReadable: true);
mesh.UploadMeshData(markNoLongerReadable: true);
```


This does not end the Texture or Mesh's lifetime. GPU data remains available for rendering, and final object cleanup is still separate. Do not apply this when later code needs to read pixels or edit vertices.

For Textures, discarding the CPU copy also fixes the uploaded resolution: subsequent mipmap-limit changes no longer affect it. Do not apply the option indiscriminately just to reduce memory.[32](#fn32)

##
[
](#9-events-async-operations-and-pools-can-retain-resources)
9. Events, async operations, and pools can retain resources

###
[
](#a-longlived-event-publisher-can-retain-its-subscribers)
A long-lived event publisher can retain its subscribers

An event publisher retains subscribers through registered delegates. If the publisher survives, a forgotten subscription can keep an unnecessary subscriber reachable.[34](#fn34)

The problem is not “events always leak,” but **a long-lived publisher retaining a shorter-lived subscriber**. For notifications needed only while a screen is enabled, pair subscription and unsubscription as follows.

Save this as `ScoreObserver.cs`

:


```
using System;
using UnityEngine;
public static class ScoreEvents
{
public static event Action<int> Changed;
public static void Publish(int score) => Changed?.Invoke(score);
[RuntimeInitializeOnLoadMethod(
RuntimeInitializeLoadType.SubsystemRegistration)]
private static void ResetForPlayMode()
{
Changed = null;
}
}
public sealed class ScoreObserver : MonoBehaviour
{
private void OnEnable()
{
ScoreEvents.Changed += OnScoreChanged;
}
private void OnDisable()
{
ScoreEvents.Changed -= OnScoreChanged;
}
private void OnScoreChanged(int score)
{
Debug.Log($"Score: {score}", this);
}
}
```


If notifications are needed while disabled, this lifetime is wrong: use the component's full lifetime or an explicit session instead.

Do not assume that writing a similar anonymous lambda during unsubscription removes the original registration. Use a named method or retain the registered delegate when unsubscription is required.[34](#fn34)

With Domain Reload disabled, static variables and events survive between Play Mode sessions. The reset above clears the event between sessions, but **resetting a static field does not release native resources**. Clean up owned buffers or load handles before discarding their references.[35](#fn35)

###
[
](#cancellation-and-resource-cleanup-are-separate-operations)
Cancellation and resource cleanup are separate operations

`MonoBehaviour.destroyCancellationToken`

corresponds to destruction of that component. Retrieve and retain it before destruction, then pass it to async APIs that accept cancellation. Disabling is not destruction: a UI that merely closes also needs a screen-session lifetime.[36](#fn36)

For an owned `CancellationTokenSource`

, `Cancel()`

and `Dispose()`

are separate. `Dispose()`

does not request cancellation. Request cancellation, confirm users have finished, and dispose when it no longer races with other operations.[37](#fn37)

Work that cannot be canceled, or that completes late, still needs cleanup for unused results and handles. The Addressables example separates “do not update the screen” from “release the acquisition.”

Coroutines stop when their GameObject becomes inactive or their MonoBehaviour is destroyed, but not merely because `MonoBehaviour.enabled = false`

. Cleanup placed after a `yield`

is not guaranteed to run on every exit path.[38](#fn38)

Dispose owned `UnityWebRequest`

instances on success, failure, interruption, and screen destruction. The request and resources obtained from its result, such as a Texture, can have separate lifetimes.[39](#fn39)

###
[
](#pools-retain-objects-for-reuse-returning-is-not-final-cleanup)
Pools retain objects for reuse; returning is not final cleanup

Object pools reduce repeated creation and destruction by keeping objects available. Returning an object is therefore different from finally releasing its resources.[40](#fn40)

On return, reset references to previous users, event subscriptions, and running operations. Whether large buffers should remain allocated depends on reuse frequency and the memory budget.

`ObjectPool<T>.maxSize`

limits how many returned objects the pool retains, not the total number that can be checked out simultaneously. Enforce a separate checkout limit when you need a total memory cap.[41](#fn41)

`Clear()`

acts on pooled objects and invokes a configured `actionOnDestroy`

. Storing GameObjects does not automatically make the pool destroy them without that callback. Checked-out objects need separate tracking and cleanup.[40](#fn40)

##
[
](#10-verify-cleanup-by-returning-to-the-same-state)
10. Verify cleanup by returning to the same state

###
[
](#gc-alloc-and-leaks-measure-different-problems)
GC Alloc and leaks measure different problems

High per-frame `GC Alloc`

indicates allocation churn and potential GC work. Near-zero `GC Alloc`

does not prove that previously allocated Textures, native arrays, or caches have been released.

Unity 6.3's incremental GC spreads collection work across frames to reduce long pauses. It does not collect reachable objects or fix missing Addressables releases. The Web platform does not support incremental GC.[42](#fn42)

Before adding periodic `GC.Collect()`

, investigate retained references, unreleased handles, and native resources that lack cleanup.

###
[
](#distinguish-used-reserved-and-osreported-memory)
Distinguish used, reserved, and OS-reported memory

Unity reserves memory for reuse. Used and reserved memory differ, and managed heap space is not guaranteed to return to the OS at a particular time.[43](#fn43)[2](#fn2)

A process memory number that does not immediately fall is not proof of a leak. Conversely, spare capacity in reserved memory can temporarily hide a growing leak from that same metric.

Inspect unwanted object counts, sizes, reference paths, and loaded assets and handles first. Unity cannot fully track all driver and platform allocations, so combine these observations with target-platform measurements.[43](#fn43)

###
[
](#a-repeatable-measurement-procedure)
A repeatable measurement procedure

Use Memory Profiler snapshot comparisons taken **after returning to the same screen and state**.[3](#fn3)

| Stage | Procedure |
|---|---|
| Warm-up | Open and close the target screen or scene once to exercise initial loads and caches. |
| Snapshot A | Return to the baseline screen and wait for normal cleanup to finish. |
| Repeat | Perform the same open/close or scene-transition sequence, for example ten times. |
| Snapshot B | Return to A's state and wait for the same completion conditions. |
| More repetitions and C | Repeat again to distinguish a plateau from continued accumulation. |
| Investigate | Trace growing types and instances to owners, references, cleanup paths, and Addressables dependencies. |

Ten repetitions are an example, not a universal pass threshold. Choose counts and tolerances based on usage, device budgets, and intended caching.

Do not compare snapshots with pending destruction, unloading, async loading, or disposal Jobs against snapshots where all cleanup has completed. If normal cleanup includes `UnloadUnusedAssets`

, wait for it every time.

Keep ordinary behavior tests separate from diagnostic tests that force GC or additional unloading. Extra cleanup used only in a test does not prove the normal lifecycle releases resources correctly.

Editor snapshots include the Editor's own memory. Use them for quick investigation, but perform final checks against a Player, such as a Development Build, on the target device and scripting backend.[44](#fn44)

###
[
](#narrow-the-investigation-by-symptom)
Narrow the investigation by symptom

| Symptom | First places to investigate |
|---|---|
| Material/Mesh counts grow after every screen closure | Implicit `material` /`mesh` clones, ownership fields, missing destruction |
| GameObjects disappear but large managed arrays remain | Statics, events, persistent services, `Leaked Managed Shell`
|
| Textures remain after Addressables releases | Unreleased handles, other assets in the same Bundle, dependencies |
| Native memory keeps growing | Owned native containers, disposal Job dependencies, buffer cleanup |
| Rendering breaks after adding cleanup | Destroyed shared assets, early final handle release, cleanup during borrowing |
| Memory rises and then plateaus | Intended pools, caches, or reservation—or unnecessary retention |

These are starting points, not diagnoses. Identify who owns the remaining resource and why it is still retained.

##
[
](#conclusion-decide-ownership-before-choosing-a-cleanup-api)
Conclusion: decide ownership before choosing a cleanup API

Unity memory management cannot be reduced to “set everything to `null`

,” “destroy everything,” or “run GC at the end.” Ask three questions:

-
**Who acquired it, and how?**Distinguish creation, loading, and borrowing; match the cleanup method. -
**Who still needs it?**Include shared users, pooled instances, Jobs, and async work—not just the screen that created it. -
**Does every exit path release exactly what it owns?**Cover success, failure, cancellation, disabling, and destruction.

Then verify repeated transitions back to the same state.

**Preventing leaks and preventing premature cleanup both begin with explicit ownership and lifetimes.**

##
[
](#references)
References

These are the primary sources cited by the Japanese edition. Unity URLs generally target 6000.3; package URLs retain their documented version series. They are preserved here rather than silently updated to newer releases.

-
Unity 6.3 Manual,

[Memory in Unity introduction](https://docs.unity3d.com/6000.3/Documentation/Manual/performance-memory-overview.html).[↩](#fnref1) -
Unity 6.3 Manual,

[Managed memory introduction](https://docs.unity3d.com/6000.3/Documentation/Manual/performance-managed-memory-introduction.html).[↩](#fnref2) -
Memory Profiler 1.1,

[Find memory leaks](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@1.1/manual/find-memory-leaks.html).[↩](#fnref3) -
Microsoft Learn,

. The cited contract concerns element references, Count, and Capacity; this does not equate Unity's runtime with .NET 10.`List<T>.Clear`

[↩](#fnref4) -
Microsoft Learn,

[Using objects that implement IDisposable](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/using-objects).[↩](#fnref5) -
Unity 6.3 Scripting API,

[Object.Destroy](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Object.Destroy.html),[Object.DestroyImmediate](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Object.DestroyImmediate.html).[↩](#fnref6) -
Unity 6.3 Scripting API,

[Renderer.material](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Renderer-material.html).[↩](#fnref7) -
Memory Profiler 1.1,

[Analyze managed shell objects](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@1.1/manual/managed-shell-objects.html).[↩](#fnref9) -
Unity 6.3 Scripting API,

[MonoBehaviour.OnDestroy](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html).[↩](#fnref10) -
Unity 6.3 Scripting API,

[MeshFilter.mesh](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/MeshFilter-mesh.html).[↩](#fnref11) -
Addressables 2.10,

[Managing Addressable asset memory](https://docs.unity3d.com/Packages/com.unity.addressables@2.10/manual/memory-assets.html).[↩](#fnref12) -
Addressables 2.10,

[Wait for asynchronous loads to complete](https://docs.unity3d.com/Packages/com.unity.addressables@2.10/manual/AddressableAssetsAsyncOperationHandle.html),[ResourceManager.Acquire](https://docs.unity3d.com/Packages/com.unity.addressables@2.10/api/UnityEngine.ResourceManagement.ResourceManager.html#UnityEngine_ResourceManagement_ResourceManager_Acquire_UnityEngine_ResourceManagement_AsyncOperations_AsyncOperationHandle_).[↩](#fnref13) -
Addressables 2.10,

[Wait for asynchronous loads with coroutines](https://docs.unity3d.com/Packages/com.unity.addressables@2.10/manual/load-wait-asynchronous-coroutines.html).[↩](#fnref14) -
Addressables 2.10,

[Load assets](https://docs.unity3d.com/Packages/com.unity.addressables@2.10/manual/load-assets.html). For an explicit explanation of reference counting, also see the official Addressables 1.18 section[Instantiating objects from Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@1.18/manual/LoadingAddressableAssets.html#instantiating-objects-from-addressables). Its older sample code is not reproduced as the implementation for this article.[↩](#fnref15) -
Addressables 2.10 API,

[Addressables.InstantiateAsync](https://docs.unity3d.com/Packages/com.unity.addressables@2.10/api/UnityEngine.AddressableAssets.Addressables.InstantiateAsync.html).[↩](#fnref16) -
Addressables 2.10 API,

[Addressables.ReleaseInstance](https://docs.unity3d.com/Packages/com.unity.addressables@2.10/api/UnityEngine.AddressableAssets.Addressables.ReleaseInstance.html).[↩](#fnref17) -
Addressables 2.10,

[Unload Addressable assets](https://docs.unity3d.com/Packages/com.unity.addressables@2.10/manual/UnloadingAddressableAssets.html).[↩](#fnref18) -
Unity 6.3 Scripting API,

[SceneManager.UnloadSceneAsync](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/SceneManagement.SceneManager.UnloadSceneAsync.html).[↩](#fnref19) -
Unity 6.3 Scripting API,

[Resources.UnloadUnusedAssets](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html).[↩](#fnref20) -
Unity 6.3 Scripting API,

[Resources.UnloadAsset](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Resources.UnloadAsset.html).[↩](#fnref21) -
Unity 6.3 Scripting API,

[AssetBundle.Unload](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/AssetBundle.Unload.html).[↩](#fnref22) -
Collections 2.6,

[Allocator overview](https://docs.unity3d.com/Packages/com.unity.collections@2.6/manual/allocator-overview.html).[↩](#fnref23) -
Unity 6.3 Scripting API,

[JobHandle.Complete](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Unity.Jobs.JobHandle.Complete.html).[↩](#fnref24) -
Unity 6.3 Scripting API,

.`NativeArray<T>.Dispose`

[↩](#fnref25) -
Unity 6.3 Scripting API,

[Texture2D.GetRawTextureData](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Texture2D.GetRawTextureData.html).[↩](#fnref26) -
Unity 6.3 Scripting API,

[RenderTexture.Release](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/RenderTexture.Release.html).[↩](#fnref27) -
Unity 6.3 Scripting API,

[RenderTexture.GetTemporary](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/RenderTexture.GetTemporary.html).[↩](#fnref28) -
Unity 6.3 Scripting API,

[GraphicsBuffer](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/GraphicsBuffer.html).[↩](#fnref29) -
Unity 6.3 Scripting API,

[ComputeBuffer.Release](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/ComputeBuffer.Release.html).[↩](#fnref30) -
Unity 6.3 URP Manual,

[Create a texture in the Render Graph system](https://docs.unity3d.com/6000.3/Documentation/Manual/urp/render-graph-create-a-texture.html),[Import a texture into the Render Graph system](https://docs.unity3d.com/6000.3/Documentation/Manual/urp/render-graph-import-a-texture.html).[↩](#fnref31) -
Unity 6.3 Scripting API,

[Texture2D.Apply](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Texture2D.Apply.html).[↩](#fnref32) -
Unity 6.3 Scripting API,

[Mesh.UploadMeshData](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Mesh.UploadMeshData.html).[↩](#fnref33) -
Microsoft Learn,

[How to subscribe to and unsubscribe from events](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/events/how-to-subscribe-to-and-unsubscribe-from-events).[↩](#fnref34) -
Unity 6.3 Manual,

[Domain reloading](https://docs.unity3d.com/6000.3/Documentation/Manual/domain-reloading.html).[↩](#fnref35) -
Unity 6.3 Scripting API,

[MonoBehaviour.destroyCancellationToken](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/MonoBehaviour-destroyCancellationToken.html).[↩](#fnref36) -
Microsoft Learn,

[CancellationTokenSource.Dispose](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtokensource.dispose?view=net-10.0).[↩](#fnref37) -
Unity 6.3 Scripting API,

[MonoBehaviour.StopCoroutine](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/MonoBehaviour.StopCoroutine.html).[↩](#fnref38) -
Unity 6.3 Scripting API,

[UnityWebRequest.Dispose](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Networking.UnityWebRequest.Dispose.html).[↩](#fnref39) -
Unity 6.3 Scripting API,

.`ObjectPool<T>`

[↩](#fnref40) -
Unity 6.3 Scripting API,

.`ObjectPool<T>`

constructor[↩](#fnref41) -
Unity 6.3 Manual,

[Garbage collection modes](https://docs.unity3d.com/6000.3/Documentation/Manual/performance-incremental-garbage-collection.html).[↩](#fnref42) -
Unity 6.3 Manual,

[Memory Profiler module reference](https://docs.unity3d.com/6000.3/Documentation/Manual/ProfilerMemory.html).[↩](#fnref43) -
Memory Profiler 1.1,

[Capture and import snapshots](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@1.1/manual/snapshot-capture.html).[↩](#fnref44)
