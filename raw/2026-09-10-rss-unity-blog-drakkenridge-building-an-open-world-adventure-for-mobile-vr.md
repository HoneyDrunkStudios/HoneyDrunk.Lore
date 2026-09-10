---
source: "https://unity.com/blog/drakkenridge-building-open-world-mobile-vr-rpg-unity-ecs"
title: "DrakkenRidge: Building an open-world adventure for mobile VR"
author: "unknown"
date_published: "2026-09-08"
date_clipped: "2026-09-10"
category: "Game Development / Unity"
source_type: "rss"
---

# DrakkenRidge: Building an open-world adventure for mobile VR

Source: https://unity.com/blog/drakkenridge-building-open-world-mobile-vr-rpg-unity-ecs

Blog
DrakkenRidge: Building an open-world adventure for mobile VR Sep 8, 2026 | 7 Min Simeon Acker and Cyril Guichard - Garage Collective GUEST BLOG Made with Unity World building Made with Unity World building Programming More More Made with Unity, DrakkenRidge is an open-world action RPG from Garage Collective, designed and optimized for mobile VR. In this guest blog, the team shares how they leverage various design and performance techniques while using Unity’s Entity Component System as the backbone of rendering.
Introducing DrakkenRidge VR We’re Garage Collective, the team behind DrakkenRidge , an open-world action RPG built for VR where you can visit any point you see on the horizon. Take on the role of a powerful Mage Hunter and explore six beautifully handcrafted islands – each totally unique, with its own characters, quests, dungeons, and secrets.
This journey will take you from warm comfortable beaches to breathtaking snowy peaks; from lush mystical forests to perilous chasms deep beneath the earth. Craft new items, battle dozens of artfully designed creatures and foes, and unlock new schools of magic that can turn every encounter into a unique experience.
Building a game of this scope as a two-person team probably wouldn’t be possible without the Entity Component System . In this post, we’ll cover how we used these tools to make our expansive adventure game.
Mixing techniques for smoother game development There are several huge advantages when using ECS to build a game, but as a small independent studio we had to weigh other factors as well when deciding how to design and engineer DrakkenRidge for mobile VR.
There are two main challenges when using ECS:
The steep learning curve: Developing with ECS requires a complete paradigm shift away from typical object-oriented logic. The separation of Entity systems from traditional game object systems can make their interactions with each other challenging. So the question for us became:
Which objects and interactions should leverage the power of ECS, and which objects should remain as traditional GameObjects and MonoBehaviours?
Entities in DrakkenRidge DrakkenRidge consists of massive open environments, with tens of thousands of objects in a given space – potentially thousands of them being visible to the player at any given time.
Rendering these as traditional GameObjects requires a large memory overhead, with the engine needing to evaluate the entire scene hierarchy and calculate Transform components for each object. When rendering thousands of objects, especially on a mobile device, the GPU will noticeably suffer.
So what if we take these objects and render them as Entities ?
As Entities, they avoid much of the rendering and memory overhead associated with GameObjects and instead are batched together in memory chunks using the Entities Graphics system.
Additionally, the DrakkenRidge art pipeline heavily utilizes the technique of Texture Atlassing, allowing the massive environments to use fewer Materials overall (see our blog post on Texture Atlassing here ).
Entities Graphics can group and handle all objects that share a common mesh and material, and then the engine can create tightly packed draw calls and render many objects at once.
The result of this can save hundreds of batches and SetPass calls.
Rendering thousands of objects – with only eight SetPass calls
Custom Entity systems DrakkenRidge utilizes ECS for rendering thousands of objects at once. But even with the massive performance gains this unlocks, there is still more we can do to improve the experience on mobile VR platforms.
Distance authoring system The first feature we created for our DrakkenRidge Entities is the distance authoring system. It takes into account a variety of variables to determine when an object should be either hidden or visible to the player.
Because the player’s vision extends very far in the open world, thousands of distant objects could be in view at once. This system prioritizes which of these should remain prominently visible, and which should fade into the background. Environmental effects, such as distance fog, are used to cover the transition as distant objects fade from view.
Distance Authoring component with custom values for runtime Entity culling
Unique culling values are generated in-Editor for each Entity based on a variety of parameters. This data is then passed, at Entity-creation time , to systems which use that pre-calculated data to make runtime decisions for when Entities should be rendered or culled.
Custom Entity groups Using the DrakkenRidge distance authoring system, Entities can be assigned to groups with shared decision-handling, to allow, for example, a section of the city to be quickly rendered or culled based on various in-game factors, instead of each entity in the city deciding individually.
Grouped Entities with shared decision-handling
Entity LODs The third feature of the DrakkenRidge distance authoring system allows entities to be swapped out on the fly for another entity that would be even cheaper to render. This technique was originally written to address the issue of more expensive shaders and materials.
While the environment models in DrakkenRidge are already highly optimized, some shaders add a noticeable cost. This Entity LOD (Level of Detail) system allows for rendering “versions of entities with higher cost shaders” only when necessary.
/// If using a simplified LOD object, see if we are in its range
if (inDistanceReturn.useLOD)
{
if (inDistanceReturn.isInDistanceLOD)
{
ecbParallel.SetEnabled(unfilteredChunkIndex, inDistanceReturn.lodEntity, true);
if (ChildLookup.TryGetBuffer(inDistanceReturn.lodEntity, out lodChildBufferData))
{
var newParent = inDistanceReturn.lodEntity;
SetEnableChildren(
entityCanBeReEnabledComponentLookup: entityCanBeReEnabledComponentLookup,
unfilteredChunkIndex: unfilteredChunkIndex,
parentEntity: newParent,
enabled: true,
childBufferData: lodChildBufferData,
ChildLookup: ChildLookup,
ecbParallel: ecbParallel);
} When conditions are met, use a simplified LOD for the Entity.
CPU optimizations DrakkenRidge ’s distance authoring calculations run through burst-compiled Jobs for maximum CPU performance.
Unity Jobs are functions that can be scheduled as asynchronous tasks to run in the background, and the Burst Compiler accelerates CPU-heavy tasks by translating them into highly optimized native machine code.
[BurstCompile]
public partial struct ProcessBufferJob : IJobChunk
{
internal EntityCommandBuffer.ParallelWriter ecbParallel;
public EntityTypeHandle entityTypeHandle;
[ReadOnly] public BufferTypeHandle<Child> childTypeHandle;
[ReadOnly] public ComponentTypeHandle<DistanceCompData> distanceCompDataTypeHandle;
// A BufferLookup for random access to Child buffers.
[ReadOnly] public BufferLookup<Child> childLookup;
[ReadOnly] public ComponentLookup<Disabled> disabledComponentLookup;
public PlayerDesignatorCompData targetDesignator;
public HelperStructToUpdateEnabledEntities addToBufferStruct;
public Entity playerEnt;
public void Execute(in ArchetypeChunk chunk, int unfilteredChunkIndex, bool useEnabledMask, in v128 chunkEnabledMask)
{
var entities = chunk.GetNativeArray(entityTypeHandle);
var childAccessor = chunk.GetBufferAccessor(ref childTypeHandle);
var distanceCompData = chunk.GetNativeArray(ref distanceCompDataTypeHandle);
bool hasChildBuffer = chunk.Has(ref childTypeHandle);
DynamicBuffer<Child> lodChildBufferData;
for (int i = 0; i < chunk.Count; i++)
{
Entity currentEntity = entities[i]; Tip: One optimization for DynamicBuffer is to cast it to a NativeArray before iteration: “var lodChildNativeArray = lodChildBufferData.AsNativeArray();”
GameObjects and physics in DrakkenRidge In DrakkenRidge , 90% of the world is rendered using ECS, running its own tasks in the background to keep the visible environment in a beautiful and optimized state.
But for our small development team of one programmer and one artist, we made the decision to build many of our close-up VR interactions using traditional GameObjects and MonoBehaviors. This allowed for faster iteration time in an environment of rapid testing and frequent design cycles.
Physics interactions and combat VR interactions in DrakkenRidge are driven largely by physics simulations. This includes everything from grabbing and manipulating objects, to player climbing and parkour, to spell-casting and melee combat.
Players can interact with physics-based climbing challenges.
Running physics simulations in the open world
Combat in DrakkenRidge is driven by a system that blends unique animations with per-joint physics behaviours. Each AI decides how to make their death feel reactive and rewarding based on the situation.
Combining per-joint physics with scripted animations to build unique reactions
Many items and spells in DrakkenRidge allow the player to deal damage to several enemies at once, often resulting in physics simulations being run on many character rigs simultaneously.
Applying explosive physics to groups of AI
Physics optimizations Realtime physics simulations can be costly, especially on mobile platforms. To help mitigate this, each physics object in the world keeps track of the location of the player, and whether or not the player is in a position to interact with the simulation.
For example, the player can climb long chains built from physics-driven links that interact with each other and the world around them. These physics colliders, joints, and rigidbodies are dynamically enabled/disabled based on whether the player is directly manipulating, or in view of, the chain.
As a general rule, we render objects at great distances, but only allow physics interactions with objects that are nearby. In a VR game, where the action happens up close, this aligns with what the player expects.
Further optimizations When deciding how to optimize our rendering for mobile VR, we considered how each environment was built and chose the solution to best fit our needs.
In addition to ECS, we considered a variety of techniques, including LODs and impostors .
GameObject LODs Rendering GameObjects with LODs consists of having multiple versions of a given object to be rendered at different distances from the player. For example, a highly detailed house model is swapped out for a very simplified low-poly version, saving on rendering time when the player is far away from the object.
In DrakkenRidge , every object is already modeled in a highly optimized low-poly retro art style, and the vast majority of the world is handled through ECS, so traditional 3D LODs would provide no real advantage.
However, the distance authoring system we created was built to handle rendering of LODs for distant Entities, when necessary.
Impostors An impostor system takes 3D GameObjects and converts them into 2D billboards when the player is at a distance from them. This works best for dense, distant background objects such as forests. DrakkenRidge utilizes imposters in some situations.
Properly implemented impostors are indistinguishable from their 3D counterparts.
In DrakkenRidge we tested a variety of optimization techniques, choosing carefully which to implement. Unity ECS by far provided the greatest performance gains, rendering our entire world at a fraction of the cost of using the traditional GameObject pipeline.
Closing thoughts For DrakkenRidge , our combination of design and optimization techniques proved to be the perfect recipe, allowing us to build a unique VR adventure. The open world is powered by ECS for Unity, and our close-up interactions are engineered with the familiar GameObject and physics workflow, allowing the team to design, test, and iterate quickly.
Open-world RPGs for mobile VR don’t have to be out of reach, and we look forward to seeing more developers take on the adventure!
DrakkenRidge VR is out now . Explore more Made with Unity games on our Steam Curator page , and check out more stories from Unity developers on the Unity Blog and Resource Hub .
