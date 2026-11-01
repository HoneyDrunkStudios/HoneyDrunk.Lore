---
source: "https://dev.to/raphael_tan_9c17abd05a891/running-neural-networks-in-a-unity-editor-tool-with-compute-shaders-mf5"
title: "Running neural networks in a Unity editor tool with compute shaders"
author: "Raphael TAN"
date_published: "2026-10-29"
date_clipped: "2026-10-31"
category: "Technical Art & Creator Tools"
source_type: "rss"
canonical_source: "https://medium.com/@raphael.tan.fr/running-neural-networks-in-a-unity-editor-tool-with-compute-shaders-49cc0188477d"
---

# Running neural networks in a Unity editor tool with compute shaders

I recently released Sound Finder, a Unity Asset Store plugin, and building it meant solving an unusual problem: running up to twelve neural networks inside the Unity editor, without Sentis, ONNX Runtime or Python.

The plugin searches a sound library by how things sound. That takes models that turn sounds and text into fingerprints you can compare, a pitch model, an onset detector, and two text-to-audio models built from four networks each. They all run on an inference runtime I wrote in C# and HLSL compute shaders.

On my laptop's RTX 4060, the runtime generates about 12 seconds of audio in 2.45 seconds. ONNX Runtime, Microsoft's reference engine for these models, does the same 32-bit math on the same GPU in 1.35 seconds with DirectML.

Why would a search tool generate audio? When you type a description, Sound Finder generates a short example sound and looks for real sounds close to it, alongside matching your words against the sounds and the filenames. The example is only a search key. The results always come from your library.

**TL;DR:** running a model in Unity is easy. Running it inside someone else's Unity project is the hard part, because you don't control their builds, their GPU, their download or their editor. Each of those changed how I built this.

## Why not use Sentis?

Sentis, Unity's own inference package (now called Inference Engine), is the obvious way to run a model in Unity. For a game, it's probably the right one.

Sound Finder isn't part of a game. It's editor-only: it helps you pick sounds, and nothing of it ends up in your build. Sentis is a runtime package, so depending on it would mean adding it to every customer's project, for a tool that never runs in their game. I didn't want that.

For the same reason, there's no native code: no ONNX Runtime DLLs, no Python process. A native plugin means a binary per platform and per CPU architecture, and one more licence to carry. Sound Finder is C# and compute shaders only.

That left writing my own runtime. To be clear about one thing: I never benchmarked Sentis against it. The comparisons in this article are with ONNX Runtime.

## What does an inference runtime actually need?

Less than I expected. The models are ONNX files: a graph of operations, plus the weights. Running one takes four pieces.

- **A parser.** A small hand-written reader for ONNX's protobuf format, so there's no protobuf dependency. It also reads weights stored in separate files, which large models use.
- **A plan.** Order the graph so every operation runs after its inputs exist, and free each intermediate tensor right after its last use. GPU buffers come from a pool, so freeing and reusing them is cheap.
- **Kernels.** A kernel is a compute shader function that runs one kind of operation on the GPU. 56 kernels in 23 .compute files, plus CPU code for shape operations, cover 68 ONNX operation types, and the twelve models Sound Finder uses need 61 of them.
- **Everything around the model.** Tokenizers for the text models, written in C#, and the audio front-end: the mel spectrogram the audio model expects, computed with an FFT on the GPU.

What surprised me is how few kinds of operation the models use. Attention has no kernel of its own: once exported, it's matrix multiplications and a softmax. GELU, RMSNorm and rotary embeddings arrive already broken down into basic math. Matrix multiplication, convolution, normalization and elementwise math, done well, covered every model I needed.

## How do you know the GPU is computing the right thing?

A broken kernel rarely crashes. It returns numbers, and the rest of the model turns them into output that looks plausible. So before trusting any speed figure, I compared every stage with a reference implementation on the same inputs: ONNX Runtime on the CPU for the large models, PyTorch for the small ones. For the bundled text-to-audio model, every stage matches ONNX Runtime with a correlation of 1.000000.

## What made it fast, and what made it slower?

The first version that ran Stable Audio Open Small end to end took 35 seconds cold and 17 warm. What made the difference:

- **Tiled matrix multiplication.** Each group of 256 threads computes a 64×64 block of the output. It loads the inputs into shared memory 16 values deep at a time, and each thread accumulates a 4×4 block of results in registers, in 32-bit floats.
- **Convolutions without im2col.** The usual trick copies input patches into a big matrix and runs a matrix multiply on it. My 1-D convolutions read their input directly and skip taps that fall outside the signal. The audio decoder got 4.9 times faster.
- **Fusion.** The decoder's activation, SnakeBeta, is five operations in the exported graph. The runtime spots that pattern at load and runs it as one kernel, in all 36 decoder blocks.
- **Constant folding.** Parts of the graph that depend only on the weights are computed once, at load. That cut one model's dispatch time from 103 ms to 58 ms.
- **Free casts.** The exported models convert between 16-bit and 32-bit floats in places. My runtime does all its math in 32-bit, so those conversions just reuse the buffer. T5, one of the text encoders, went from 861 ms to 351 ms.

Two textbook optimizations made it slower.

**Command buffers.** The standard advice for cutting CPU overhead in Unity is to record dispatches into a CommandBuffer and submit them together. In my runtime, it only gave correct results if no buffer went back to the pool until the command buffer had run. That meant about ten times more live buffers: the decoder went from about 20 to about 200, many over 1 MB. The text encoder got 15% faster, each diffusion step got 56% slower, and the decoder 230% slower. I reverted it.

**Half precision.** Storing weights as 16-bit floats halves their size, and 16-bit math should be faster. I built 16-bit input and output variants of the decoder's convolution and activation kernels. All passed their tests, and none was measurably faster on my RTX 4060 under DX11. DX11's shader compiler, FXC, ignores the min16float hint, so the math stays 32-bit anyway. Real 16-bit math needs the newer DXC compiler and DX12. My DXC attempt ran measurably slower, and I can't choose which graphics API my customers' editors run on. ONNX Runtime shows what that costs: through DirectML, which runs on DX12, its 16-bit path takes 0.9 seconds instead of 1.35.

So the math is 32-bit everywhere, and low precision is only a storage format. 16-bit weights stay packed in GPU memory where the matrix and convolution kernels can read them directly. The 8-bit format in the next section exists only on disk.

## What if the model can't ship in your package?

For text search, I wanted Stable Audio Open Small, a text-to-audio model from Stability AI. Its weights couldn't go in the package. That's a licence problem: as I read the Asset Store's submission guidelines, the Stability AI Community License isn't one they allow for components bundled inside an asset. And I wanted the base asset to be fully working and compliant.

My first answer was a server: generate on a cloud GPU and send the audio back. The model was fast there, but the hosting platform's cold starts put queries at 6 to 14 seconds, and nothing on my side could fix that. A search box can't wait that long, so I shut the server down and went fully local.

Sound Finder now bundles MeanAudio, an open text-to-audio model of about a billion parameters, and offers Stable Audio Open Small as an optional one-time download from my own GitHub, checked by hash. Bundling MeanAudio raised two problems.

**Size.** In 32-bit floats, MeanAudio is 4.4 GB. The usual shortcut, converting the whole graph to 16-bit, broke it: the converted graphs mixed types and output all zeros. So I wrote my own 8-bit format: each output channel of a weight is stored as 8-bit integers, with one 32-bit scale. MeanAudio went from 4.4 GB to 1.1 GB. The mean error per tensor is about 1%, and in a listening test with 10 prompts at a fixed seed, the two versions sounded very close.

**Load time.** With the integers turned back into 32-bit floats on the CPU, loading took 17.9 seconds. Doing it in a compute shader, straight into the GPU buffers, brought it to 3.1 seconds, with zero mismatches against the CPU version across the 479 million weights I checked.

The 8-bit format saves download size and disk space, not GPU memory: on the GPU, the weights are 32-bit again. Once it has generated, MeanAudio holds about 3.8 GB of GPU memory, on top of about 0.45 GB for the search models. Stable Audio Open Small holds about 2.6 GB: 1 GB of 16-bit weights, and 1.6 GB of buffers the runtime keeps pooled for the next generation.

## How do you keep the editor usable while models run?

In a game, you decide what each frame is spent on. In an editor tool, the person is typing, scrolling and listening while the models work, and in Unity, GPU work belongs to the main thread, the same one that draws the editor. What I ended up with:

- **Time slices.** Generation runs the graph on the main thread, operation by operation, and yields after 12 ms until the next editor update.
- **One queue to the GPU.** Indexing decodes and analyses audio on worker threads. Anything that touches the GPU goes through a queue that the main thread drains two calls at a time per editor update, so a big batch doesn't hold the editor long enough for Unity's "Hold on" dialog.
- **No waiting on readbacks.** Results come back through AsyncGPUReadback, with a blocking fallback after 30 frames.
- **A budget for decoding.** Clip decoding gets at most 30 ms per editor update.
- **Working in the background.** When the editor loses focus, Unity updates it much less often. The indexer requests its own updates, so indexing keeps going while you're in another window.
- **GPU setup on the main thread.** Parsing a model can happen on a worker thread. Creating its GPU buffers can't.
- **Domain reloads.** Every script change reloads the C# domain, and GPU buffers that aren't released before it leak. Everything is disposed on reload.

What's still not great: the optional Stable Audio model doesn't use those time slices yet. Each of its stages runs as one call, so the editor freezes for about 0.2 seconds per diffusion step and 0.7 seconds for the final decoding.

## What would I tell another asset creator?

- **Decide first what you won't put in your customers' projects.** That decision picks your runtime.
- **Compare every stage against a reference you didn't write,** before you measure speed.
- **Measure textbook optimizations on your customers' hardware.** Command buffers and 16-bit math made mine slower or no faster.
- **Keep low precision for storage when you can't choose the graphics API,** and do the math in 32-bit.
- **Give editor work a time budget per update,** and keep every GPU call on the main thread.

## The details

Soundly, Soundminer and Sononym search a sound library from their own app. Sound Finder does it inside the Unity editor: describe the sound, imitate it into your microphone, or drop in a clip, and the pick goes straight into your AudioClip field. It's an editor-only tool for Unity 6 that runs entirely on your machine, with no account and no API key. I develop and test it on Windows.

Text search works out of the box with MeanAudio. The optional higher-quality model, a one-time download of about 1 GB, is Stable Audio Open Small, powered by Stability AI, under the Stability AI Community License.

[Sound Finder on the Unity Asset Store](https://assetstore.unity.com/packages/tools/audio/sound-finder-truly-listening-audio-search-browser-392296)

Questions about the runtime are welcome in the comments. Bugs and feature requests for Sound Finder go to [GitHub issues](https://github.com/RaphTan63/SoundFinder/issues), and you can find me on [LinkedIn](https://www.linkedin.com/in/raphaeltan-prog/).

*Cover: Unity Inspector illustration over a photo of a Palit GeForce RTX 5090 by [PantheraLeo1359531](https://commons.wikimedia.org/wiki/File:Palit_GeForce_RTX_5090_Gamerock_20250530_HOF4166_RAW-Export.png), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), cropped and composited. This article is not sponsored by or affiliated with Unity Technologies or its affiliates. Unity is a trademark or registered trademark of Unity Technologies or its affiliates in the U.S. and elsewhere.*
