---
source: "https://learn.unity.com/article/understanding-memory-management-in-unity"
title: "Understanding Memory Management in Unity"
author: "Jemin Lee"
date_published: "unknown"
date_clipped: "2026-10-28"
category: "Game Development / Unity"
source_type: "web"
---

# Understanding Memory Management in Unity

Source: https://learn.unity.com/article/understanding-memory-management-in-unity

Why Unity's memory usage never drops back down: how the managed heap, garbage collection, and the Large Object Heap actually work.

Unity Technologies

Last updated: September 18, 2026•Intermediate•10m

## Introduction

The following article was written by Jemin Lee, a Partner Engineer at Unity.

Over the years, there are two questions I’ve heard many times whenever developers start profiling memory in Unity:

1. *Why doesn’t my managed heap or virtual memory usage drop, even after the GC runs?*
2. *Is it true that calling* *GC.Collect()* *multiple times can reduce physical or dirty memory usage?*

The short answers are:

- Unity’s GC doesn’t free heap memory - **it recycles it**. This is intentional.
- And while physical memory *can* decrease in some cases, **manually triggering GC is almost always the wrong way to achieve it** .

In this article, we’ll dive into Unity’s managed heap and how the Garbage Collector (GC) actually works, and tackle the myth of manually forcing memory cleanup.

## How OS Memory Works

Before we dive into Unity, let’s take a quick refresher on how the operating system (OS) handles memory.

### Physical vs. Virtual Memory

Your device has a fixed amount of Physical Memory (RAM). This is the hardware where data is loaded for real-time access. However, your application doesn’t interact with physical memory directly. Instead, it operates in its own sandboxed Virtual Memory (VM).

This is a crucial design that enables the OS to efficiently manage physical RAM, allowing your app to focus on its functionality without needing to worry about the details. For example, the OS can compress less-used heap regions in Physical Memory to make space, and your app will never know the difference.

### Page and Frame

Virtual memory is divided into pages. The typical page size is 16KB on mobile (iOS, Android) and 4KB on desktop (Windows, Linux). Therefore, the total virtual memory usage of your app is equal to the number of pages multiplied by the page size.

The pages of virtual memory can be mapped to physical memory as shown in the following figure. The unit of physical memory that corresponds to a page is called a frame.

- Paging in: Loading a page of virtual memory into a page frame of physical memory.
- Paging out: Releasing an unnecessary page frame from physical memory.

Let’s look at a quick example. Imagine your code asks the OS for enough memory to hold a large array corresponding to 3 pages(48KB).

```csharp
const int sizeOfPage = 16384;
const int numberOfPages = 3;

// Allocate an int array corresponding to 3 pages
int* array = (int *)malloc(numberOfPages * sizeOfPage);
```

***Side note**: This is a simplified example that assumes a malloc call mmap/VirtualAlloc - which reserves virtual memory. But malloc internally could use brk/sbrk or its own pool (User-space allocator) for small allocations.*

When malloc returns, you’re getting virtual memory only. At this point, no physical frames have been assigned yet.

Now, what happens when we actually use that memory?

```
array[0] = 141;
```

When we set `array[0] = 141`, this triggers what’s called a **page fault**: OS detects that we’re accessing a virtual page that hasn’t been paged in yet. Then, OS will load the page into Physical Memory.

And that page becomes what we call ‘dirty’ - meaning it’s been modified.

### Note : Windows vs Unix-like memory model

There are three concepts regarding mapping pages into Physical Memory.

- Reservation : Reserve virtual address space without physical memory.
- Committing : Assign physical pages to the reserved virtual address range.
- Decommitting : Release physical pages back to the OS while keeping the virtual address space reserved.

And Windows gives you explicit APIs for all of this: **VirtualAlloc** and **VirtualFree**. Windows separates three concepts very clearly. The developer can call VirtualAlloc/Free to explicitly manage each step.

On Unix-like systems (Linux, macOS, iOS, Android), reservation and commit are not strictly separated.

mmap API from Unix-like OS reserves address space, but commit is lazy. There is no explicit commit or decommit. The closest equivalent to the Windows decommitting API is madvise(DONTNEED), which is only a suggestion. The OS ultimately decides when memory is reclaimed.

### Clean vs. Dirty Page

When a page is brought into physical memory, the OS keeps track of whether your app has modified it. This creates two categories:

- **Clean Pages:** Pages without any written value yet, or pages containing data that has **not been changed**.

Think of your game’s executable code, read-only data, or textures. If the OS is low on memory, it can safely discard a clean page because it can always be reloaded from the original file on disk. Clean pages have a low impact on your app’s stability.

- **Dirty Pages:** Pages that your app has **written to and modified**.

The OS *cannot* discard this page from RAM, because the data would be lost. **Dirty pages are the primary contributor to your app’s true memory footprint.**

## Understanding the Managed Heap Structure

Now let’s move into Unity-specific territory. The managed heap.

### Managed Heap

The managed heap is where all your C# object allocations occur. This is managed by the garbage collector.

### Segments

The managed heap doesn’t work with raw pages directly. Instead, it uses what we call segments - sometimes also referred to as blocks. Each segment consists of one or multiple pages, depending on the garbage collector implementation and platform configuration.

A segment serves as the GC’s internal management unit and can hold one or more managed objects. The GC allocates, marks, and sweeps memory within segments, while the operating system manages physical memory at the page level.

Additional Note: Object allocation does not occur on a per-page basis.

The diagram is intentionally drawn to illustrate the general concept of a segment being composed of multiple pages. However, in Unity’s current GC default configuration, the GC heap block size typically matches the OS page size. As a result, in practice, a segment often maps 1:1 to a single OS page.

That does not mean a segment can contain only one object.

While a memory segment is ultimately reserved and mapped at the OS page level, small object allocation does not occur on a per-page basis. Instead, small object allocations are subdivided and packed within a single segment, allowing multiple managed objects to share the same underlying OS page.

For example, assume a platform where the page size is 16 KB, and the GC heap block size is also configured to be 16 KB, resulting in a 1:1 mapping between a segment and an OS page.

If a single 4-byte float is allocated inside that segment, the OS will treat the entire 16 KB page as dirty, because memory is tracked at page granularity at the OS level.

However, this does not mean that the remaining space inside the page is unusable. From the GC’s perspective, only 4 bytes are occupied, and the remaining space within the same segment can still be subdivided and reused for additional small object allocations.

## How allocation and garbage collection works in Managed Heap?

Let’s see what’s really going on on Managed Heap. Here you can see multiple segments containing multiple objects in the Managed Heap.

When you allocate a new object, it is placed in an existing segment if there’s room. If there’s not enough free space for the new allocation, the GC creates a new empty segment and puts the new object there.

When garbage collection executes, unreachable objects (also known as dead objects) are logically collected. The gray blocks below represent objects collected by GC.

The memory regions occupied by dead objects inside segments are recorded in a free list for future reuse. Note that dead objects are no longer referenced, but their pages are still mapped in physical memory and marked as dirty by the OS.

Later, when new objects are allocated:

- (1) GC reuses the memory regions that previously held collected objects when a new allocation fits their available space.
- (2) If the remaining free space within those segments isn’t large or contiguous enough, GC will search for another suitable region within the existing heap.
- (3) If no such region is found, it expands the managed heap by reserving a new memory segment from the OS.

## But why doesn’t the memory usage drop?

So far, we’ve seen how GC removes unused objects and how those freed spaces can be reused for new allocations.

However, here’s the key point: even after all objects inside pages have been collected, those pages are not immediately unmapped or released back to the operating system.

Heap pages that once held collected objects remain mapped in physical memory, still marked as dirty pages at the OS level. Even if Unity GC marks them as reusable, the OS still considers them dirty because they once contained modified data.

From the OS’s perspective, these pages remain part of the app’s memory footprint until they’re explicitly unmapped - something Unity’s GC rarely does in real time.

That’s why, in tools like Xcode Instruments, you’ll still see a large *Dirty Size* even after a GC pass - those pages aren’t cleared physically, only *logically*.

### Empty but Dirty Segments

After a GC cycle, you might have segments that are logically empty but whose backing OS pages are still resident in physical memory. No live objects are inside, but they’re still occupying RAM because they contain dirty pages.

In most cases, this is actually fine. No problem at all. These segments are often reused soon for new allocations, so keeping them in memory makes sense.

But when does it become a problem? If a segment remains empty for a long time and still contains dirty pages, it unnecessarily consumes physical memory. That’s when the GC needs to take action.

### What Unity GC does

Unity automatically unmaps heap segments that have remained completely empty for multiple GC cycles (every 6th GC.Collect, but this number may vary between engine versions). This process frees long-unused segments from physical memory while keeping the same virtual heap size.

Unity GC removes heap segments that have been empty for several GC cycles and remaps new segments of the same size and at the same virtual address space. The total virtual heap size stays the same, but resident memory may occasionally shrink.

This remapping behavior can also refresh memory locality. When Unity remaps the pages of a long-unused segment, the operating system provides newly allocated physical pages, often placed in more recently accessed memory regions, which could provide a tiny performance improvement.

Side note: Unmapping unused segments on Windows

On Windows, because Windows supports explicit decommitting through VirtualFree, the GC decommits the pages of an empty segment without dropping the segment entirely.

### **Important :** Why You Shouldn’t Trigger This Manually

Although calling GC.Collect() multiple times can sometimes cause this unmapping to occur, doing so manually is not recommended.

This process is intended only for long-unused segments.

If you call GC.Collect() several times in the same frame, it will also unmap pages that were freed only a frame or two ago - pages that Unity would have reused in the next frame anyway.

This causes unnecessary CPU work, more frequent remapping, and possible heap fragmentation.

In short, Unity already handles long-unused segments automatically, and even optimizes memory locality. Forcing GC manually to achieve this doesn’t reduce real memory usage; it only interrupts Unity’s natural optimization cycle.

## Large Object Heap

Everything discussed so far applies to the **general managed heap.** But in Unity’s current GC (based on Boehm GC), large managed objects that exceed a certain size threshold are handled through a separate allocation path. The GC places large objects on the **large object heap(LOH)**.

Typical examples of large objects include large managed arrays (such as byte[], vector3[], etc.) or huge temporary buffers used during loading or processing. Large objects follow **different allocation, reuse, and reclamation rules** compared to small objects.

### How large?

The definition of a large object is GC-implementation specific.  
For example, [in Microsoft’s .NET runtime:](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/large-object-heap)

> *If an object is greater than or equal to 85,000 bytes in size,*  
> *it’s considered a large object and allocated on the Large Object Heap.*

In Unity, the large-object threshold is typically 8KB on mobile and 2KB on desktop, but the exact value depends on platform and build configuration.

**Side Note**

In Unity GC, an object equal to or larger than MAXOBJBYTES is treated as a large object. MAXOBJBYTES is defined as half of HBLKSIZE(which is GC’s internal heap block size).

For IL2CPP builds, you can verify this value directly in the generated Xcode project by inspecting `gc_priv.h` under the `Il2CppOutputProject/IL2CPP/external/bdwgc`.

### How large objects are allocated

When a large object is allocated, the **GC bypasses the regular small-object free lists.** This means it does not attempt to reuse fragmented free space between small objects (which in practice would not be suitable for large allocations anyway).

Instead:

- The requested size is rounded up to a whole number of heap blocks
- A **contiguous sequence of heap blocks** is allocated.
- That entire range is treated as a **single, atomic object.**

For example (assuming a 4 KB heap block size):

- Requesting 6 KB → 8 KB (2 blocks) allocated
- Requesting 17 KB → 20 KB (5 blocks) allocated

Once allocated, the large object **exclusively occupies** that contiguous block range.

### Cross-allocation constraints

Large objects are tracked using **dedicated large-object free lists**, which are separate from the regular small-object free lists. As a result:

- Free space within a **live** large-object block range is never reused for small-object allocations.
- Likewise, fragmented free space between small objects is never combined to satisfy a single large object allocation.

At first glance, this behavior may seem wasteful. For example, consider a case where a 17 KB large object is allocated in 20KB block range (five contiguous blocks). Although there may be unused space remaining within that range, that space cannot be sub-allocated for smaller objects.

Similarly, once the 17 KB object becomes unreachable and is collected, the entire 20 KB block range becomes free. At that point, it might appear that the GC could reuse that space for multiple smaller allocations. In practice, **it is most naturally reused by another large allocation of a similar size.**

A freed large-object block is initially reused as a whole. **While the GC can reuse regions previously occupied by large objects for other purposes, this requires the block to be explicitly repurposed and split, which does not happen automatically at collection time.**

This is a design choice. Large objects are treated as indivisible units to avoid ambiguous liveness and bookkeeping complexity

### LOH Fragmentation

Because of these characteristics, large objects tend to contribute more visibly to **memory fragmentation**:

- Reuse requires a sufficiently large, contiguous block.
- Smaller allocations cannot borrow space from large free blocks.
- Large free regions may remain unused for long periods if no similarly sized allocation occurs.

However, completely free large blocks are not wasted forever. They may later be repurposed when allocation pressure requires it.

### What happens when a large object is freed

When a large object becomes unreachable and is collected:

- The block range is immediately added to the **large object free list**
- Another large allocation can reuse this space directly
- This is the **fast path** and happens without overhead

Adjacent free blocks are coalesced when possible, forming larger contiguous free regions. The freed block retains its full size and is managed purely based on size, not on its previous use.

At this stage, the block remains intact. It is not immediately made available to small-object allocation paths.

Allocation-time reuse and lazy splitting

If a future allocation requires heap space and no suitable block is available through the usual path, the GC may:

- Select a completely free large heap block.
- Split it on demand.
- Use a portion of it as backing storage for the allocation.
- Return the remaining portion to the free list.

This lazy splitting occurs at allocation time(not during collection).

Large objects monopolize their block ranges while alive, and freed blocks are reused conservatively. It’s split and repurposed only when future allocation pressure requires it.

## Unity’s Current GC and Future Changes(CoreCLR)

The behavior described in this article reflects **Unity 6’s current garbage collector implementation**, which is based on a Boehm GC. **Boehm GC is a conservative, non-moving garbage collector.**

### Conservative GC

In a conservative GC, objects are **never relocated** during collection. Live objects remain exactly where they were originally allocated inside a segment, and the collector only identifies which objects are reachable and which are not.

Memory is reclaimed by marking dead objects as free, not by rearranging live ones. Because objects are not moved, **heap compaction does not occur.**

> Compaction is a GC strategy where live objects are moved closer together,  
> eliminating gaps between them and reducing fragmentation.

Over time, this naturally leads to fragmentation inside heap segments: free spaces may exist, but they are often too small or too scattered to be reused efficiently.

This design is intentional. Moving objects during GC is expensive. It requires relocating objects in memory **and updating all references** that point to them.

In practice, **allocation speed is often prioritized over long-term fragmentation**. Avoiding object movement keeps allocations simple and cheap.

Additionally, to move objects safely, the GC must know exactly which values are real object references. However, a conservative GC does not have that level of precision.

Instead, it treats **any value that looks like a pointer into the managed heap as a potential reference**, even if it is not an actual object reference. This approach deliberately prioritizes safety over precision.

### CoreCLR - Moving GC

As Unity continues its transition toward newer .NET runtimes and **CoreCLR**, some of the constraints described above may change.

**CoreCLR-based garbage collectors** are **precise and compacting** by design. They are able to relocate live objects and update references, which reduces fragmentation.

However, a GC optimized for general-purpose workloads is not automatically a perfect fit for **real-time game engines,** as moving objects and compacting memory introduce additional CPU workloads.

Any use of compaction will need to be **tuned specifically for real-time workloads.** For this reason, Unity will not simply adopt CoreCLR’s GC behavior “as-is”.

## Summary

- Virtual Memory ≠ Physical Memory
- Memory segments (blocks) are allocated and freed in page units
- Small object allocations are subdivided and packed within a segment
  - Multiple small objects can share the same underlying OS page
- A single large object occupies one or more contiguous segments exclusively
- Dead objects don’t reduce physical memory
- GC performs logical cleanup, not physical unmapping.
- Dirty pages remain mapped and visible in OS profilers until Unity remaps them.
- The managed heap’s virtual size only grows, while resident memory may shrink slightly over time
- Manual GC.Collect() calls to trigger remapping segments only hurt performance. Let Unity handle it.
- Large managed objects are allocated through a separate large-object allocation path
- Unity 6’s current GC is based on a conservative, non-moving GC, which prioritizes safety and predictable allocation over compaction.
- CoreCLR introduces precise, moving, and compacting GC capabilities, which may change some of the behaviors described above.
- CoreCLR in Unity will be carefully tuned for real-time game workloads

## Unity Documentation and related resources

### Unity documentation

- [Memory in Unity](https://docs.unity3d.com/Manual/performance-memory.html)
- [Memory Performance Data](https://docs.unity3d.com/Manual/profiler-memory.html)
- [Memory Profiler Package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@1.2/manual/index.html)

### YouTube

- [Memory Profiler Walkthrough & Tutorial](https://www.youtube.com/watch?v=Uuzd39AjFWQ)

### Related articles

- [Ultimate Guide to Profiling Unity Games](https://unity.com/resources/ultimate-guide-to-profiling-unity-games)
