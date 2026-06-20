---
source: "https://dev.to/gamedevtoollab/a-practical-guide-to-unity-addressables-bundle-splitting-and-lz4lzma-compression-49m6"
title: "A Practical Guide to Unity Addressables Bundle Splitting and LZ4/LZMA Compression"
author: "GameDev Tool Lab"
date_published: "2026-06-19"
date_clipped: "2026-06-20"
category: "Game Development / Unity"
source_type: "web"
---

# A Practical Guide to Unity Addressables Bundle Splitting and LZ4/LZMA Compression

Source: https://dev.to/gamedevtoollab/a-practical-guide-to-unity-addressables-bundle-splitting-and-lz4lzma-compression-49m6

GameDevToolLab 
Posted on Jun 19 
A Practical Guide to Unity Addressables Bundle Splitting and LZ4/LZMA Compression
# unity3d 
# addressables 
# assetbundle 
Overview
In the previous article, we looked at Addressables download concurrency, label design, and batch downloads using labels.
One important point there was this:
Labels are only the entry point for specifying what you want to download. The actual files downloaded are AssetBundles. 
In other words, even if your label design looks clean, a rough Bundle layout can still cause unexpected assets to be downloaded together.
This time, we will look at how to split AssetBundles and how to choose compression settings.
In particular, this article covers:
Whether Bundles should be split into smaller units or grouped together 
How to handle many small files, such as VN / adventure game scenario text files 
How to split assets that will keep increasing over time, such as character 3D models 
How to think about Pack Together , Pack Separately , and Pack Together By Label 
How to choose between LZ4 and LZMA 
This is not an introduction to the official features. The focus is on practical decision-making for real projects.
Label design and Bundle splitting must be considered together
In Addressables, you can use Addresses and Labels to specify which assets to load or download.
However, the actual files downloaded are AssetBundles.
For example, suppose you define labels like this:
Label 
Purpose 
chapter_01 
Assets used in Chapter 1 
chapter_02 
Assets used in Chapter 2 
character_alice 
Assets related to Alice 
character_bob 
Assets related to Bob 
If you only look at the labels, it may seem like the assets are managed in a fine-grained way.
But if the actual Bundle is packed as one large Bundle, downloading only chapter_01 may still download other assets included in the same Bundle.
So, in Addressables, these two concepts need to be considered separately:
Item 
Role 
Address / Label 
Specifies which assets are requested 
AssetBundle 
The actual unit downloaded, cached, and loaded 
Label design alone does not determine the download unit.
Label design and Bundle splitting must be designed together. 
What does Bundle splitting affect?
Bundle splitting is not just a way to organize things in the Editor.
In practice, it affects the following:
Affected area 
Description 
Download unit 
Which files are downloaded together 
Cache unit 
Which units are stored on the device 
Update unit 
Which Bundles become update targets during content updates 
Load unit 
Which Bundles are required at load time 
Number of files 
Affects download requests and file open operations 
Management cost 
Catalogs, dependencies, and operation rules become more complex 
Splitting Bundles into smaller units makes it easier to download only what is needed and reduce update size.
On the other hand, if the number of Bundles increases too much, download requests, cached files, file open operations, catalog complexity, and dependency management cost all increase.
So with Addressables, “smaller is always better” is not the right answer.
The basic approach is:
Group what should be grouped, and split what should be split, based on how the assets are actually used. 
Bundle Mode options
In Addressables Group settings, you can choose a Bundle Mode.
The main options are:
Bundle Mode 
Description 
Suitable cases 
Pack Together 
Packs assets in the group into Bundles together 
Small files, or data used together 
Pack Separately 
Packs each Addressable entry in the group into a separate Bundle 
Characters, stages, costumes, and other assets with clear update units 
Pack Together By Label 
Packs assets with the same label set together 
Cases where you want to manage or download by label 
One important detail is that Pack Separately does not mean “one asset per Bundle.”
It means one Bundle per Addressable entry .
If a folder is marked as an Addressable entry, the contents under that folder may be packed into one Bundle.
Also, scene assets are handled as separate Bundles from normal assets. Even with Pack Together , everything is not necessarily packed into a single file.
Avoid casually saying “one address, one file”
In real projects, people sometimes describe Pack Separately as “one address, one file.”
That may be fine for a rough conversation, but it is better to be careful when writing design documents or articles.
As an Addressables setting, the accurate term is Pack Separately .
Pack Separately creates a separate Bundle for each Addressable entry in the group.
So the following cases are not as simple as “one asset = one Bundle”:
A folder is registered as an Addressable entry 
Sprite Atlases or Sub Assets are involved 
Scenes and normal assets are mixed 
Dependencies are moved into separate Bundles 
For a rough explanation, “one address, one file” may be understandable.
But for actual design, it is safer to think in terms of Pack Separately .
Cases where grouping Bundles is acceptable
First, let’s look at cases where grouping assets into Bundles is reasonable.
Asset characteristic 
How to think about it 
Each file is small 
Creating individual Bundles may make the file count a bigger problem 
There are many files 
Download requests and file open operations can increase 
They are used together 
Splitting does not change the actual load unit much 
Individual updates are rare 
Fine-grained update units provide little benefit 
The management unit is clear 
Easy to group by chapter, event, language, and so on 
Typical examples include:
VN / adventure game scenario text 
Dialogue text 
Small .txt files 
Small configuration files 
Master data 
Localization text 
Lightweight ScriptableObject assets 
For this kind of data, creating one Bundle per file may not be the easiest approach to operate.
Especially when each file is only a few KB to a few dozen KB, and there are hundreds or thousands of them, the downside of increasing the number of files can become more noticeable than the benefit of fine-grained Bundles.
Many small files, such as VN scenario text
VN / adventure game scenario text is an easy example where grouping often makes sense.
For example, suppose you have a structure like this:
Scenario/
Chapter01/
scene_001.txt
scene_002.txt
scene_003.txt
...
Chapter02/
scene_001.txt
scene_002.txt
scene_003.txt
...
Enter fullscreen mode 
Exit fullscreen mode 
If every .txt file is packed into its own Bundle, the number of files increases quickly.
When the file count increases, the following costs also increase:
More download requests 
More cached files 
More file open operations 
More file lookup and management cost 
Catalog and dependency checks become more tedious 
Of course, if you need to update each scenario file independently, or if you absolutely do not want to download a scenario until the user is about to read it, splitting into smaller units may be valid.
But in many cases, grouping like this is easier to operate:
Grouping unit 
Example 
Chapter 
scenario_chapter_01 
Event 
scenario_event_summer 
Language 
scenario_ja , scenario_en 
Delivery unit 
scenario_initial , scenario_update_001 
For scenario text, users often play by chapter or event.
So grouping Bundles by those units usually makes operation easier.
Cases where Bundles should be split
On the other hand, there are also cases where splitting Bundles is better.
Asset characteristic 
How to think about it 
Each asset is large 
Downloading unnecessary data becomes costly 
The addition unit is clear 
Easy to update by character, costume, or stage 
Individual updates are frequent 
Update diffs can be kept smaller 
The asset may not be used 
It can be downloaded only when needed 
There is a sales or unlock unit 
Works well with DLC, gacha, event rewards, etc. 
Typical examples include:
Character 3D models 
Character-specific Meshes 
Character-specific Textures 
Character-specific Materials 
Character-specific Animations 
Costumes 
Weapons 
Stages 
Large Prefabs 
VFX 
Voice assets 
If you group these too aggressively, operation can become painful.
In particular, assets such as characters and stages often increase over time. Splitting Bundles by the unit in which they are added makes them easier to manage.
Assets that keep increasing, such as character 3D models
Character 3D models are an easy example where splitting Bundles often makes sense.
Suppose all characters are packed into one Bundle:
character_all.bundle
Alice
Bob
Carol
Dave
Eve
Enter fullscreen mode 
Exit fullscreen mode 
With this layout, adding just one new character can make the entire character_all.bundle an update target.
Even if a user only needs Alice, they may still download Bob and the other characters because they are in the same Bundle.
On the other hand, if you split Bundles by character, the update and download units become clearer:
character_alice.bundle
character_bob.bundle
character_carol.bundle
character_dave.bundle
character_eve.bundle
Enter fullscreen mode 
Exit fullscreen mode 
With this layout, if only Alice is needed, only Alice’s Bundle can be downloaded.
When adding a new character, you can add a new Bundle and avoid updating existing character Bundles as much as possible.
A character Bundle may contain assets like this:
character_alice.bundle
Alice.prefab
Alice.mesh
Alice.material
Alice_texture_base
Alice_texture_normal
Alice_animation_idle
Alice_animation_run
Enter fullscreen mode 
Exit fullscreen mode 
This kind of layout is practical because larger assets that are used together are grouped by their addition and update unit .
Pack Together By Label is useful, but depends on label design
Pack Together By Label packs assets with the same label set into Bundles.
If your label design is clean, this can make it easier to create Bundles by label.
For example:
Asset 
Labels 
Alice-related assets 
character_alice , initial_download 
Bob-related assets 
character_bob , event_001 
Chapter 1 scenario 
scenario_chapter_01 , initial_download 
Chapter 2 scenario 
scenario_chapter_02 , update_001 
However, if labels are messy, relying on Pack Together By Label can easily produce an unintended Bundle layout.
For example, if management labels, download labels, event labels, and search labels are mixed together, the number of label combinations increases and the Bundle layout becomes hard to read.
When using Pack Together By Label , it is safer to separate label responsibilities:
Label type 
Example 
Notes 
Download labels 
initial_download , chapter_01 
These may affect Bundle splitting 
Classification labels 
character , scenario 
Decide whether they should affect Bundle splitting 
Management labels 
deprecated , debug 
Avoid mixing them with runtime labels 
Event labels 
event_001 
Also consider what happens after the event ends 
Increasing the number of labels is not bad by itself.
But when using Pack Together By Label , the label set directly affects the Bundle layout, so you need operation rules.
How to decide whether to group or split
As a rough guide:
Asset characteristic 
Recommendation 
Many small files 
Group them 
Used together by chapter or event 
Group them 
Little need for individual updates 
Group them 
Too many files are being created 
Group them 
Each asset is large 
Split them 
Addition unit is clear 
Split them 
Added by character, costume, or stage 
Split them 
You do not want to download unused assets 
Split them 
You want to keep update diffs small 
Split them 
In more practical terms:
Group many small files 
Split large assets with clear addition units 
Group assets that are used together 
Split assets that may not be used 
Split assets with different update units 
These are the basic rules for Bundle splitting.
Difference between LZ4 and LZMA
Next, let’s look at compression settings.
In Addressables Group settings, you can choose the compression format for Bundles.
The common choices are LZ4 and LZMA.
Compression 
Characteristics 
LZMA 
High compression ratio, useful for reducing download size 
LZ4 
Chunk-based and easier to handle at load time 
Uncompressed 
No decompression cost, but file size tends to be larger 
LZMA treats the entire Bundle as one compressed stream.
This usually gives a higher compression ratio, but the decompression cost during loading can become larger.
LZ4 compresses data in chunks.
Its compression ratio is usually lower than LZMA, but it is easier to read only the needed parts, and it tends to be lighter to handle at load time.
Cases where LZMA is easy to recommend
LZMA is useful when you want to reduce download size.
However, in real projects, it is safer to decide based on what is inside the Bundle .
As a rule of thumb:
If 1 Bundle is close to 1 asset, LZMA is easy to recommend.
If 1 Bundle contains multiple assets, LZ4 should be the default.
Enter fullscreen mode 
Exit fullscreen mode 
Here, “1 Bundle = 1 asset” means cases like:
One large binary file 
One large TextAsset 
One video file 
One audio file 
One Prefab packed into its own Bundle 
One Texture packed into its own Bundle 
These Bundles are likely to be loaded almost entirely when used.
That makes it easier to benefit from LZMA’s high compression ratio.
On the other hand, be careful with a Bundle like this:
character_alice.bundle
Alice.prefab
Alice.mesh
Alice.material
Alice_texture_base
Alice_texture_normal
Alice_animation_idle
Alice_animation_run
Enter fullscreen mode 
Exit fullscreen mode 
This is a “one character, one Bundle” layout, but the Bundle still contains multiple assets.
Even if it looks like one unit called Alice at the application level, the Bundle itself is a collection of multiple assets.
So it is safer not to casually decide “one character Bundle means LZMA.”
LZMA is easy to recommend only when the layout is close to 1 Bundle = 1 asset .
Use LZ4 as the default for Bundles containing multiple assets
LZMA treats the entire Bundle as one compressed stream.
So even if you only want to read part of the Bundle, the decompression cost of the whole Bundle can become an issue at load time.
When multiple independent assets are grouped into one Bundle, LZ4 is usually easier to operate.
Bundle layout where LZ4 should be the default 
Reason 
Bundle containing multiple Addressable entries 
You may only read part of it 
Bundle containing many small files 
The purpose is reducing file count, so partial access matters 
Chapter-level scenario Bundle 
You may not read every file in the chapter at once 
Master data Bundle 
Only some data may be referenced 
Localization Bundle 
Data may be read by language or screen 
Character-related asset Bundle 
Often contains Prefab, Mesh, Texture, Animation, etc. 
Bundle where stable load time and memory behavior matter 
Avoiding full-stream decompression is safer 
The important point is:
“One character, one Bundle” and “one Bundle, one asset” are different things. 
Even if a character has its own Bundle, if that Bundle contains a Prefab, Meshes, Textures, Materials, and Animations, it is still a multi-asset Bundle.
In that case, using LZ4 as the default usually makes load-time behavior more stable.
Cases where LZ4 should be the default
LZ4 is suitable when you care about load-time handling.
In Addressables, it is common to group multiple assets into one Bundle. In practice, LZ4 is usually the default choice for multi-asset Bundles .
Bundle layout 
Reason 
Bundle containing many small files 
You may only read part of it 
Chapter-level scenario Bundle 
Files are often read in sequence 
Master data Bundle 
Only some data may be referenced 
Localization Bundle 
Data may be read by language or screen 
Bundle containing multiple Addressable entries 
LZMA is more affected by whole-Bundle decompression 
Character-related asset Bundle 
Often contains multiple assets 
Bundle where stable load time matters 
Chunk-based compression is easier to operate 
For Bundles that group multiple files, such as VN scenario text, LZ4 is often easier to handle.
Group the Bundle to reduce the number of files.
But use LZ4 because you may only read part of the Bundle.
This combination is very practical.
Practical recommended settings
As a starting point, the following rules are easy to work with:
Asset type 
Bundle split 
Compression 
One large TextAsset 
1 asset per Bundle 
LZMA recommended 
One large binary file 
1 asset per Bundle 
LZMA recommended 
One video file 
1 asset per Bundle 
LZMA recommended, but also consider compression of the video format itself 
One audio file 
1 asset per Bundle 
LZMA recommended, but also consider compression of the audio format itself 
One Texture 
1 asset per Bundle 
LZMA recommended, but judge based on the size after texture compression 
VN scenario text 
Group by chapter or event 
LZ4 
Dialogue text 
Group by chapter, event, or language 
LZ4 
Master data 
Group by type or update unit 
LZ4 
Localization 
Group by language 
LZ4 
Character 3D models 
Consider one Bundle per character 
LZ4 if the Bundle contains multiple assets 
Costumes 
Consider one Bundle per costume 
LZ4 if the Bundle contains multiple assets 
Stages 
Consider one Bundle per stage 
LZ4 if the Bundle contains multiple assets 
Large VFX 
Split by usage unit 
LZ4 if the Bundle contains multiple assets 
Voice assets 
Split by character, chapter, or event 
LZ4 if multiple files are grouped together 
The key point is to think about Bundle granularity and compression format separately.
Splitting Bundles, such as one Bundle per character, is useful for reducing download and update units.
However, if that Bundle contains multiple assets, LZ4 should be the default compression choice.
Conversely, if a Bundle contains only one asset, LZMA is easy to recommend.
Condition 
Recommendation 
1 Bundle is close to 1 asset 
LZMA recommended 
The whole Bundle is always read 
LZMA is easier to recommend 
You strongly want to reduce initial download size 
LZMA is easier to recommend 
Multiple Addressable entries are included 
LZ4 by default 
You may only read part of the Bundle 
LZ4 by default 
Many small files are grouped together 
LZ4 by default 
You want stable load time 
LZ4 by default 
Web delivery is involved 
Start with LZ4 in mind 
Of course, the final decision should be based on real device measurements.
Even with “1 asset per Bundle,” the perceived behavior changes depending on asset type, size, device performance, and load timing.
Measure download size, load time, and memory usage on real devices before making the final decision.
Notes on Bundle splitting
There are a few additional things to keep in mind when splitting Bundles.
Duplicate dependencies
When Bundles are split into smaller units, shared dependencies become important.
For example, if multiple characters reference the same Material or Texture, the dependency layout can become complicated depending on how you split the Bundles.
You need operation rules for whether shared assets should be moved into a shared Bundle or kept with each character.
Do not look only at update diffs
Splitting Bundles into smaller units makes update diffs easier to reduce.
But the trade-off is an increased number of Bundles.
If you only look at update size, you may want to split everything. But download requests, cache count, and load-time management cost should be considered together.
Think about initial downloads and additional downloads separately
Assets needed for the initial download and assets downloaded later should not be judged by the same rule.
Type 
How to think about it 
Initial download 
Group assets needed immediately after launch and reduce the number of downloads 
Additional download 
Download only what is needed by character, stage, or event 
Optional download 
Download voices, high-resolution textures, etc. only when needed 
For initial downloads, grouping more aggressively can be easier.
For additional downloads, making the unit clear is usually easier to operate.
Do not mix the responsibilities of labels and Bundle Mode too much
Labels are useful, but trying to solve everything with labels can break the design.
Labels for specifying download targets 
Labels for search or classification 
Labels for management 
Labels for events 
Labels for debugging 
If all of these are mixed together and you use Pack Together By Label , the Bundle layout becomes difficult to understand.
When adding labels, consider whether each label is allowed to affect Bundle splitting.
Practical checklist
Finally, here is a checklist for deciding Bundle layout.
Group or split
[ ] Are these assets used together? 
[ ] Do you want to download them individually? 
[ ] Do you want to update them individually? 
[ ] Is each file large? 
[ ] Is the number of files getting too high? 
[ ] Is there a clear unit such as character, chapter, stage, or event? 
[ ] Is this part of the initial download or an additional download? 
[ ] Are unnecessary assets being downloaded? 
Compression settings
[ ] Is download size the priority? 
[ ] Is load time the priority? 
[ ] Is the layout close to 1 Bundle = 1 asset? 
[ ] Does the Bundle contain multiple assets? 
[ ] Is there a chance that only part of the Bundle will be read? 
[ ] Did you measure download size on a real device? 
[ ] Did you measure load time on a real device? 
[ ] Did you measure memory usage on a real device? 
Operation
[ ] Does the label design match the Bundle layout? 
[ ] Are you relying too much on Pack Together By Label ? 
[ ] Have you decided how to handle shared dependencies? 
[ ] Are you balancing update size and file count? 
[ ] Will the design still work after more assets are added post-release? 
Summary
With Addressables Bundle splitting, neither “split everything” nor “group everything” is always correct.
The important thing is to decide based on how the assets are used, update units, download units, file count, and load-time cost.
For data such as VN scenario text, where each file is small but there are many files, grouping by chapter or event can be easier to operate.
This is because increasing the number of files also increases download requests, cached files, file open operations, file lookup cost, and management cost.
On the other hand, for assets such as character 3D models, where each asset is large and new assets are likely to be added over time, splitting by character can be easier to manage.
For compression, the rule of thumb is:
If 1 Bundle is close to 1 asset, LZMA is recommended. If the Bundle contains multiple assets, use LZ4 by default. 
LZMA is useful when compression ratio is the priority, but because whole-Bundle decompression can become an issue, it is safer to avoid it when multiple independent load targets are grouped into one Bundle.
On the other hand, if the Bundle effectively contains one asset, such as one large TextAsset, one binary file, or one Texture, LZMA is easy to recommend.
In the end, always measure download size, load time, and memory usage on real devices before making the final decision.
Addressables can look complicated if you only look at the settings.
But in practice, the basic idea is simple:
Group small files. Split large assets with clear addition units. For compression, use LZMA when 1 Bundle is close to 1 asset, and use LZ4 by default for multi-asset Bundles. 
Starting from this policy makes it easier to build a Bundle layout that does not break down over time.
Top comments (0) 
Subscribe 
Personal 
Trusted User 
Create template
Templates let you quickly answer FAQs or store snippets for re-use.
Submit 
Preview 
Dismiss 
Code of Conduct 
• 
Report abuse 
Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink .
Hide child comments as well
Confirm
For further actions, you may consider blocking this person and/or reporting abuse
