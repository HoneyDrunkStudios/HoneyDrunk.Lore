---
source: "https://dev.to/aws-heroes/i-built-a-minecraft-mod-where-every-sword-is-an-aws-service-heres-how-we-coded-it-with-ai-4epc"
title: "I Built a Minecraft Mod Where Every Sword is an AWS Service — Here's How We Coded It with AI"
author: "DEV.to Gamedev"
date_published: "Tue, 05 May 2026 01:43:58 +0000"
date_clipped: "2026-05-05"
category: "Game Development / Unity"
source_type: "rss"
---

# I Built a Minecraft Mod Where Every Sword is an AWS Service — Here's How We Coded It with AI

Source: https://dev.to/aws-heroes/i-built-a-minecraft-mod-where-every-sword-is-an-aws-service-heres-how-we-coded-it-with-ai-4epc

try {
if(localStorage) {
let currentUser = localStorage.getItem('current_user');
if (currentUser) {
currentUser = JSON.parse(currentUser);
if (currentUser.id === 493613) {
document.getElementById('article-show-container').classList.add('current-user-is-article-author');
}
}
}
} catch (e) {
console.error(e);
}
Carlos Cortez 🇵🇪 [AWS Hero] 
for AWS Heroes 
Posted on May 5 
I Built a Minecraft Mod Where Every Sword is an AWS Service — Here's How We Coded It with AI
# ai 
# aws 
# gamedev 
# showdev 
I Built a Minecraft Mod Where Every Sword is an AWS Service — Here's How We Coded It with AI
What happens when a cloud engineer picks up Minecraft modding for the first time? You get swords that invoke Lambda functions, store items in S3 buckets, and auto-scale damage like EC2 instances. Today we're going deep into how I built AWS Swords — a Fabric mod for Minecraft 1.21.1 where every weapon is inspired by a real AWS service, and every ability maps to actual cloud computing concepts.
The concept is straightforward: take the services we use every day in the cloud and turn them into Minecraft weapons with abilities that actually make sense. Lambda is serverless and ephemeral? The sword summons temporary allies that disappear after a few seconds. S3 stores objects? The sword absorbs items from the ground and retrieves them later. EC2 scales? The sword stacks damage the more you hit.
And the best part — I coded this entire mod alongside an AI agent. Every class, every texture animation, every ability was a conversation. Let me show you how.
📓 Full source code : The complete mod is available on CurseForge — clone it, build it, swing some cloud-powered swords.
Why AWS Swords?
I've been a modded Minecraft fan for years. Tech mods and RPG packs are my thing — Applied Energistics 2, Tech Reborn, Mekanism, Create, you name it. There's something deeply satisfying about building complex systems inside a game, automating everything, and watching it all come together. If you've ever spent an entire weekend wiring up an ME system or designing a Mekanism ore processing chain, you know exactly what I'm talking about.
So when I started thinking about a side project that combined my two worlds — cloud computing and gaming — the idea hit me: what if there was a tech mod, but for cloud computing? Not pipes and machines, but AWS services as weapons with abilities that mirror what the real services do. And I wanted to go all the way with it — build it for Minecraft 1.21.1, publish it officially on CurseForge, and include it in my current modded Minecraft series.
That's how AWS Swords was born. And what's interesting is how naturally AWS service behaviors map to game mechanics:
AWS Lambda → Ephemeral compute → Temporary allies that spawn and despawn 
Amazon S3 → Object storage → A sword that absorbs and retrieves items 
Amazon EC2 → Auto Scaling + Spot Instances → Stacking damage + random crits 
In practice, this means that every sword teaches you something about the service it represents, just by playing with it.
The Architecture
Here's the mod structure — and yes, it looks a lot like a microservices architecture:
aws-swords-mod/
├── src/main/java/com/awsswords/
│ ├── AwsSwordsMod.java # Entrypoint (the main() of mods)
│ ├── client/
│ │ └── AwsSwordsClient.java # Client-side particles
│ ├── entity/
│ │ └── LambdaMinionManager.java # Lifecycle manager for Lambda invocations
│ └── item/
│ ├── ModItems.java # Item registry (like a service catalog)
│ ├── ability/
│ │ └── SwordAbility.java # Interface — the contract every ability follows
│ └── sword/
│ ├── BaseSword.java # Abstract base — cooldowns, tooltips, particles
│ ├── LambdaSword.java # ⚡ Invoke: 1-3 temporary allies
│ ├── GreatswordOfLambda.java # ⚔ Mass Invoke: 3-5 holy allies
│ ├── S3Sword.java # ☁ PutObject / GetObject item storage
│ └── EC2Sword.java # ⚡ Auto Scaling + Spot Instance crits
├── src/main/resources/
│ ├── fabric.mod.json
│ └── assets/awsswords/
│ ├── lang/ # en_us.json + es_es.json
│ ├── models/item/ # JSON models per sword
│ └── textures/item/ # Animated PNGs + .mcmeta
└── build.gradle
Enter fullscreen mode 
Exit fullscreen mode 
The design follows a pattern any cloud architect would recognize: an interface defines the contract ( SwordAbility ), an abstract base class handles shared behavior ( BaseSword ), and each implementation is independent (one class per sword). Loose coupling, high cohesion. Just like good microservices.
The Tech Stack
Component 
Version 
Minecraft 
1.21.1 
Fabric Loader 
0.19.2 
Fabric API 
0.109.0+1.21.1 
Fabric Loom 
1.9 
Java 
21 
Gradle 
8.12 
Step 1: The Foundation — SwordAbility Interface
Every sword ability in the mod implements this interface. It's the contract — if you want to be an AWS sword, you need to define what happens on use, how long the cooldown is, and what the tooltip says.
public interface SwordAbility { 
void onUse ( PlayerEntity player , World world , ItemStack stack ); 
default void onAttack ( PlayerEntity player , Entity target , ItemStack stack ) {} 
int getCooldownTicks (); 
Text getDescription (); 
} 
Enter fullscreen mode 
Exit fullscreen mode 
What caught my attention is how clean this keeps things. Adding a new sword means implementing this interface and wiring it up. No giant switch statements, no spaghetti. The onAttack default method is there for swords like EC2 that need hit-based mechanics instead of right-click abilities.
Step 2: BaseSword — The Shared Infrastructure
The BaseSword abstract class handles everything that's common across swords: Netherite-tier stats, cooldown management, tooltip rendering, and the hook for ambient particles.
public abstract class BaseSword extends SwordItem { 
private final SwordAbility ability ; 
private final String lore ; 
protected BaseSword ( SwordAbility ability , String lore , Item . Settings settings ) { 
super ( ToolMaterials . NETHERITE , settings . attributeModifiers ( 
SwordItem . createAttributeModifiers ( ToolMaterials . NETHERITE , 3 , - 2.4f ))); 
this . ability = ability ; 
this . lore = lore ; 
} 
@Override 
public TypedActionResult < ItemStack > use ( World world , PlayerEntity player , Hand hand ) { 
ItemStack stack = player . getStackInHand ( hand ); 
if (! world . isClient && ! player . getItemCooldownManager (). isCoolingDown ( this )) { 
ability . onUse ( player , world , stack ); 
player . getItemCooldownManager (). set ( this , ability . getCooldownTicks ()); 
return TypedActionResult . success ( stack ); 
} 
return TypedActionResult . pass ( stack ); 
} 
@Override 
public void appendTooltip ( ItemStack stack , TooltipContext context , List < Text > tooltip , TooltipType type ) { 
tooltip . add ( ability . getDescription (). copy (). formatted ( Formatting . GOLD )); 
tooltip . add ( Text . literal ( "Cooldown: " + ability . getCooldownTicks () / 20 + "s" ). formatted ( Formatting . GRAY )); 
tooltip . add ( Text . literal ( lore ). formatted ( Formatting . DARK_PURPLE , Formatting . ITALIC )); 
} 
} 
Enter fullscreen mode 
Exit fullscreen mode 
Think of BaseSword as a base AMI — it has everything pre-configured, and each sword just layers its unique behavior on top. The use() method delegates to the ability, handles cooldowns, and makes sure we only run server-side logic (no duplicate execution on the client).
Step 3: Sword of Lambda — Serverless Allies
This is where it gets fun. AWS Lambda runs code on demand, scales automatically, and the compute is ephemeral — it disappears when the function finishes. So the Sword of Lambda invokes 1-3 baby zombie allies that fight for you and despawn after 5 seconds.
public class LambdaSword extends BaseSword { 
public LambdaSword ( Item . Settings settings ) { 
super ( new InvokeAbility (), "Runs on demand. No servers required." , settings ); 
} 
@Override 
protected ParticleEffect getAmbientParticle () { 
return ParticleTypes . ENCHANTED_HIT ; 
} 
@Override 
public boolean hasGlint ( ItemStack stack ) { return true ; } 
private static class InvokeAbility implements SwordAbility { 
@Override 
public void onUse ( PlayerEntity player , World world , ItemStack stack ) { 
if (!( world instanceof ServerWorld server )) return ; 
int count = 1 + world . random . nextInt ( 3 ); 
world . playSound ( null , player . getBlockPos (), SoundEvents . ENTITY_EVOKER_CAST_SPELL , 
SoundCategory . PLAYERS , 1 f , 1.5f ); 
for ( int i = 0 ; i < count ; i ++) { 
ZombieEntity minion = new ZombieEntity ( EntityType . ZOMBIE , world ); 
double angle = ( 2 * Math . PI * i ) / count ; 
double x = player . getX () + Math . cos ( angle ) * 2 ; 
double z = player . getZ () + Math . sin ( angle ) * 2 ; 
minion . refreshPositionAndAngles ( x , player . getY (), z , 
( float )( angle * 180 / Math . PI ), 0 ); 
minion . setBaby ( true ); 
minion . setCustomName ( Text . literal ( "λ Invocation" ). formatted ( Formatting . GOLD )); 
minion . setCustomNameVisible ( true ); 
server . spawnEntity ( minion ); 
server . spawnParticles ( ParticleTypes . FLAME , 
x , player . getY () + 0.5 , z , 10 , 0.3 , 0.5 , 0.3 , 0.02 ); 
LambdaMinionManager . track ( minion , 100 ); // 5 seconds 
} 
player . sendMessage ( Text . literal ( 
"§6⚡ Lambda Invoke: " + count + " function" + 
( count > 1 ? "s" : "" ) + " deployed!" ), true ); 
} 
@Override 
public int getCooldownTicks () { return 300 ; } // 15 seconds 
@Override 
public Text getDescription () { 
return Text . literal ( "⚡ Invoke — Summon 1-3 temporary allies" ); 
} 
} 
} 
Enter fullscreen mode 
Exit fullscreen mode 
A few things to note:
The minions spawn in a circle around the player using trigonometry — just like Lambda functions spinning up across availability zones 
Each minion gets a custom name tag: λ Invocation in gold text 
The LambdaMinionManager.track(minion, 100) call registers the entity for automatic cleanup after 100 ticks (5 seconds) 
The evoker cast spell sound gives it that magical "deploying to the cloud" feel 
The LambdaMinionManager — Lifecycle Management
This is the garbage collector for our serverless functions. It uses Fabric's ServerTickEvents to count down each minion's remaining ticks and despawn them with a puff of smoke:
public class LambdaMinionManager { 
private static final List < TrackedMinion > minions = new ArrayList <>(); 
public static void register () { 
ServerTickEvents . END_SERVER_TICK . register ( server -> { 
Iterator < TrackedMinion > it = minions . iterator (); 
while ( it . hasNext ()) { 
TrackedMinion tracked = it . next (); 
tracked . ticksLeft --; 
if ( tracked . ticksLeft <= 0 || ! tracked . entity . isAlive ()) { 
if ( tracked . entity . isAlive ()) { 
if ( tracked . entity . getWorld () instanceof ServerWorld sw ) { 
sw . spawnParticles ( ParticleTypes . SMOKE , 
tracked . entity . getX (), tracked . entity . getY () + 0.5 , 
tracked . entity . getZ (), 15 , 0.3 , 0.5 , 0.3 , 0.05 ); 
} 
tracked . entity . discard (); 
} 
it . remove (); 
} 
} 
}); 
} 
public static void track ( ZombieEntity entity , int ticks ) { 
minions . add ( new TrackedMinion ( entity , ticks )); 
} 
} 
Enter fullscreen mode 
Exit fullscreen mode 
Think of it as CloudWatch monitoring your Lambda executions — when the timeout hits, the function gets terminated. Clean, predictable lifecycle management.
Step 4: Greatsword of Lambda — Mass Invoke
Same concept, bigger scale. The Greatsword is the two-handed variant — slower attack speed (0.8 vs 1.6), higher damage (+15 vs +11), and it summons 3-5 allies that last 8 seconds instead of 5. It's like going from a single Lambda invocation to a fan-out pattern.
// attackDamage +7 (vs +3 normal), attackSpeed -3.2 (very slow, greatsword feel) 
super ( ToolMaterials . NETHERITE , settings . attributeModifiers ( 
SwordItem . createAttributeModifiers ( ToolMaterials . NETHERITE , 7 , - 3.2f ))); 
Enter fullscreen mode 
Exit fullscreen mode 
The minions get purple soul fire particles instead of regular flames, and their name tags read λ Holy Invocation — because when you're invoking 5 functions at once, it's practically a religious experience.
Step 5: Sword of S3 — Object Storage in Your Inventory
This one is my favorite. Amazon S3 stores and retrieves objects. So the Sword of S3 does exactly that:
Right-click → PutObject : absorbs the nearest item from the ground (4-block radius) into a virtual bucket 
Shift + Right-click → GetObject : retrieves the last stored item back to your inventory 
Max capacity : 5 objects (it's a bucket, not a data lake) 
Persistence : Items are stored in the sword's NBT data — they survive death 
private TypedActionResult < ItemStack > putObject ( ServerWorld world , PlayerEntity player , ItemStack sword ) { 
NbtList bucket = getBucket ( sword ); 
if ( bucket . size () >= MAX_OBJECTS ) { 
player . sendMessage ( Text . literal ( "§c✗ Bucket full! (5/5 objects)" ), true ); 
return TypedActionResult . fail ( sword ); 
} 
List < ItemEntity > items = world . getEntitiesByClass ( ItemEntity . class , 
new Box ( player . getBlockPos ()). expand ( 4 ), e -> ! e . isRemoved ()); 
if ( items . isEmpty ()) { 
player . sendMessage ( Text . literal ( "§7No items nearby to upload" ), true ); 
return TypedActionResult . fail ( sword ); 
} 
// Find nearest item 
ItemEntity nearest = items . get ( 0 ); 
double minDist = player . squaredDistanceTo ( nearest ); 
for ( ItemEntity ie : items ) { 
double d = player . squaredDistanceTo ( ie ); 
if ( d < minDist ) { minDist = d ; nearest = ie ; } 
} 
// Store item as NBT 
ItemStack picked = nearest . getStack (). copy (); 
NbtCompound itemNbt = new NbtCompound (); 
itemNbt . put ( "item" , picked . encodeAllowEmpty ( world . getRegistryManager ())); 
bucket . add ( itemNbt ); 
setBucket ( sword , bucket ); 
nearest . discard (); 
world . playSound ( null , player . getBlockPos (), SoundEvents . ENTITY_ENDERMAN_TELEPORT , 
SoundCategory . PLAYERS , 0.7f , 1.5f ); 
world . spawnParticles ( ParticleTypes . PORTAL , 
nearest . getX (), nearest . getY () + 0.5 , nearest . getZ (), 20 , 0.3 , 0.3 , 0.3 , 0.5 ); 
player . sendMessage ( Text . literal ( "§b☁ PutObject: " + picked . getName (). getString () + 
" uploaded (" + bucket . size () + "/" + MAX_OBJECTS + ")" ), true ); 
return TypedActionResult . success ( sword ); 
} 
Enter fullscreen mode 
Exit fullscreen mode 
The cool part here is the NBT storage pattern. In Minecraft 1.21.1, items use the new DataComponentTypes.CUSTOM_DATA system instead of the old direct NBT access. The sword stores a NbtList called s3bucket inside its custom data component — each entry is a serialized ItemStack . It's literally key-value storage, just like S3.
The visual feedback sells it: Portal particles on upload (your item is going to the cloud), Reverse Portal particles on download (it's coming back), and the Enderman teleport sound for both operations. Because if S3 had a sound, it would be a teleport.
The lore text? "11 nines of durability." — because S3 offers 99.999999999% durability, and that joke was too good to pass up.
Step 6: Sword of EC2 — Auto Scaling Damage
EC2 is all about compute that scales. The Sword of EC2 has two mechanics:
Auto Scaling (Active) : Consecutive hits within 4 seconds stack damage — +10% per hit, up to +50% at 5 stacks. Stop hitting for 4 seconds and it resets. Just like an Auto Scaling group ramping up instances under load.
Spot Instance (Passive) : 20% chance on every hit to land a critical strike with electric spark particles and a lightning sound. Because Spot Instances give you extra compute at a discount, but they can be interrupted at any time — you never know when you'll get one.
@Override 
public boolean postHit ( ItemStack stack , LivingEntity target , LivingEntity attacker ) { 
if (!( attacker instanceof PlayerEntity player ) || attacker . getWorld (). isClient ) { 
return super . postHit ( stack , target , attacker ); 
} 
ServerWorld world = ( ServerWorld ) attacker . getWorld (); 
long now = world . getTime (); 
UUID id = player . getUuid (); 
// Auto Scaling: increment stacks 
StackData data = playerStacks . computeIfAbsent ( id , k -> new StackData ()); 
if ( now - data . lastHitTick > STACK_TIMEOUT_TICKS ) { 
data . stacks = 0 ; // reset — scale-in after idle 
} 
data . lastHitTick = now ; 
if ( data . stacks < MAX_STACKS ) data . stacks ++; 
float bonus = data . stacks * 0.10f ; 
float bonusDamage = target . getMaxHealth () > 0 ? stack . getDamage () * bonus : 0 ; 
if ( bonusDamage > 0 ) { 
target . damage ( world . getDamageSources (). playerAttack ( player ), bonusDamage ); 
} 
// Spot Instance: 20% crit chance 
boolean spotCrit = world . random . nextFloat () < 0.20f ; 
if ( spotCrit ) { 
target . damage ( world . getDamageSources (). playerAttack ( player ), 4.0f ); 
world . spawnParticles ( ParticleTypes . ELECTRIC_SPARK , 
target . getX (), target . getY () + 1 , target . getZ (), 20 , 0.5 , 0.8 , 0.5 , 0.1 ); 
world . playSound ( null , target . getBlockPos (), SoundEvents . ENTITY_LIGHTNING_BOLT_IMPACT , 
SoundCategory . PLAYERS , 0.4f , 1.8f ); 
} 
// More particles at higher stacks — visual scaling 
world . spawnParticles ( ParticleTypes . SOUL_FIRE_FLAME , 
target . getX (), target . getY () + 1 , target . getZ (), 
2 + data . stacks * 3 , 0.3 , 0.5 , 0.3 , 0.02 ); 
int pct = ( int )( bonus * 100 ); 
String msg = "§b⚡ Auto Scaling: " + data . stacks + "/" + MAX_STACKS + " (+" + pct + "%)" ; 
if ( spotCrit ) msg += " §e⚡ SPOT CRIT!" ; 
player . sendMessage ( Text . literal ( msg ), true ); 
return super . postHit ( stack , target , attacker ); 
} 
Enter fullscreen mode 
Exit fullscreen mode 
Notice how the particle count scales with the stack count ( 2 + data.stacks * 3 ). At max stacks you get 17 soul fire particles per hit — the visual feedback tells you exactly how scaled up you are. The EC2 sword uses postHit instead of onUse because its mechanics are attack-based, not right-click-based. Different interaction model, same interface contract.
Step 7: Animated Textures and Visual Polish
Every sword has an 8-frame animated texture with interpolation. In Minecraft, you achieve this with a sprite sheet PNG (16x128 for 8 frames of 16x16) and a .mcmeta file:
{ 
"animation" : { 
"frametime" : 3 , 
"interpolate" : true 
} 
} 
Enter fullscreen mode 
Exit fullscreen mode 
The frametime: 3 means each frame lasts 3 ticks (0.15 seconds), and interpolate: true smoothly blends between frames. Combined with hasGlint() → true on every sword, you get that enchanted shimmer on top of the animation.
The color palettes map to the services:
Lambda : Orange/purple with fire and gems 
Greatsword of Lambda : Purple/pink holy warrior energy 
S3 : Green/teal with teal gems and green aura 
EC2 : Blue/orange katana-style with electric sparks 
Step 8: Client-Side Particles
The AwsSwordsClient class adds ambient particles when you're holding any AWS sword. It runs client-side only (no server overhead) and spawns subtle enchanted hit particles every 6 ticks:
public class AwsSwordsClient implements ClientModInitializer { 
@Override 
public void onInitializeClient () { 
ClientTickEvents . END_CLIENT_TICK . register ( client -> { 
ClientPlayerEntity player = client . player ; 
if ( player == null || !( player . getMainHandStack (). getItem () instanceof BaseSword )) return ; 
if ( player . getWorld (). getTime () % 6 == 0 ) { 
double x = player . getX () + ( player . getRandom (). nextDouble () - 0.5 ) * 0.5 ; 
double y = player . getY () + 0.8 + player . getRandom (). nextDouble () * 0.5 ; 
double z = player . getZ () + ( player . getRandom (). nextDouble () - 0.5 ) * 0.5 ; 
player . getWorld (). addParticle ( ParticleTypes . ENCHANTED_HIT , x , y , z , 0 , 0.02 , 0 ); 
} 
}); 
} 
} 
Enter fullscreen mode 
Exit fullscreen mode 
It's a small detail, but it makes the swords feel alive. You know you're holding something special.
Step 9: Registration and Localization
The ModItems class registers all swords with Fabric's registry and adds them to the Combat creative tab:
public class ModItems { 
public static final Item SWORD_OF_LAMBDA = register ( "sword_of_lambda" , 
new LambdaSword ( new Item . Settings ())); 
public static final Item GREATSWORD_OF_LAMBDA = register ( "greatsword_of_lambda" , 
new GreatswordOfLambda ( new Item . Settings ())); 
public static final Item SWORD_OF_S3 = register ( "sword_of_s3" , 
new S3Sword ( new Item . Settings ())); 
public static final Item SWORD_OF_EC2 = register ( "sword_of_ec2" , 
new EC2Sword ( new Item . Settings ())); 
private static Item register ( String name , Item item ) { 
return Registry . register ( Registries . ITEM , Identifier . of ( AwsSwordsMod . MOD_ID , name ), item ); 
} 
public static void register () { 
ItemGroupEvents . modifyEntriesEvent ( ItemGroups . COMBAT ). register ( entries -> { 
entries . add ( SWORD_OF_LAMBDA ); 
entries . add ( GREATSWORD_OF_LAMBDA ); 
entries . add ( SWORD_OF_S3 ); 
entries . add ( SWORD_OF_EC2 ); 
}); 
} 
} 
Enter fullscreen mode 
Exit fullscreen mode 
And because this is Breaking the Cloud, we ship with English and Spanish localization:
// en_us.json 
{ 
"item.awsswords.sword_of_lambda" : "Sword of Lambda" , 
"item.awsswords.greatsword_of_lambda" : "Greatsword of Lambda" , 
"item.awsswords.sword_of_s3" : "Sword of S3" , 
"item.awsswords.sword_of_ec2" : "Sword of EC2" 
} 
// es_es.json 
{ 
"item.awsswords.sword_of_lambda" : "Espada de Lambda" , 
"item.awsswords.greatsword_of_lambda" : "Gran Espada de Lambda" , 
"item.awsswords.sword_of_s3" : "Espada de S3" , 
"item.awsswords.sword_of_ec2" : "Espada de EC2" 
} 
Enter fullscreen mode 
Exit fullscreen mode 
Building and Running
Two scripts handle everything:
# Build the mod JAR 
#!/bin/bash 
export JAVA_HOME = /opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home
export PATH = " $JAVA_HOME /bin: $PATH " 
cd " $( dirname " $0 " ) /aws-swords-mod" && ./gradlew remapJar
# Run Minecraft with the mod loaded 
#!/bin/bash 
export JAVA_HOME = /opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home
export PATH = " $JAVA_HOME /bin: $PATH " 
cd " $( dirname " $0 " ) /aws-swords-mod" && ./gradlew runClient
Enter fullscreen mode 
Exit fullscreen mode 
The remapJar task is Fabric-specific — it remaps your compiled classes from development mappings (Yarn) to production mappings (intermediary) so the mod works in a real Minecraft installation. The output lands in build/libs/aws-swords-0.1.0.jar .
Coding with AI — How We Actually Built This
Here's the part that makes this project different. I didn't build this mod alone — I built it in conversation with an AI agent. Every single file in this project was a collaboration.
The workflow looked like this:
I described the vision : "I want a Minecraft mod where swords have AWS service abilities" 
We wrote a Statement of Work together : Service-to-ability mappings, damage values, cooldowns, visual effects 
We coded iteratively : One sword at a time, testing in-game between each one 
The AI handled the boilerplate : Gradle config, Fabric mod JSON, registry patterns, NBT serialization 
I made the design decisions : Which services to include, how abilities should feel, what the lore text should say 
The thing is, the AI was particularly good at the parts that would have taken me hours to figure out as a first-time Minecraft modder — things like the DataComponentTypes.CUSTOM_DATA pattern for NBT storage in 1.21.1, the ServerTickEvents hook for entity lifecycle management, and the TypedActionResult return types for item interactions.
But the creative decisions — Lambda should summon baby zombies because they're small and ephemeral , S3 should use portal particles because items are going to "the cloud" , EC2's lore should be "Choose your instance type wisely" — those were all human.
My advice for anyone trying this: use AI for the mechanics, bring the creativity yourself.
Lessons Learned
Challenge 
Solution 
First time with Fabric modding 
AI agent handled the boilerplate, I focused on game design 
NBT storage in 1.21.1 
New DataComponentTypes.CUSTOM_DATA system, not the old direct NBT 
Entity lifecycle (Lambda minions) 
Custom tick-based manager with ServerTickEvents 
Client vs Server logic 
world.isClient checks everywhere — particles client-side, logic server-side 
Animated textures 
8-frame sprite sheets + .mcmeta with interpolate: true 
Greatsword balance 
Higher damage (+7 vs +3) but much slower speed (-3.2 vs -2.4) 
S3 item persistence 
NBT serialization with encodeAllowEmpty + ItemStack.fromNbt 
EC2 stack tracking 
Per-player HashMap<UUID, StackData> with tick-based timeout 
What's Next
The SoW has 3 more swords planned for the MVP:
Sword of CloudWatch — "Describe Alarms": reveals all mobs in 30 blocks, showing HP and active effects. Like a scanner. "Observable by default." 
Sword of IAM — "Deny Policy": applies a debuff that blocks mob special abilities (no teleport for Endermen, no explosion for Creepers). "Explicit deny always wins." 
Sword of DynamoDB — "Burst Capacity": first 5 hits in 3 seconds deal increasing damage, then you enter "throttle" mode with reduced damage. "Single-digit millisecond latency." 
And Phase 2 includes SNS, SQS, Route 53, CloudFront, ECS, EKS, RDS, Kinesis, Step Functions, and Bedrock. Plus a rune and socket system. The roadmap is ambitious, but we're building it one sword at a time.
The Main Takeaway
You don't need to be a Minecraft modding expert to build a mod. You don't need to be a game designer to create fun mechanics. What you need is a clear vision, a good collaborator (AI or human), and the willingness to iterate.
The truth is, this project taught me more about Fabric's internals in a few hours than any tutorial could have. When you're building something you actually want to play, the learning happens naturally.
And if you're a cloud engineer who's ever wondered what your favorite AWS service would look like as a Minecraft weapon — now you know.
Connect with me: 
LinkedIn - Let's discuss cloud architecture and Minecraft mods 
X/Twitter - Follow for AWS, GenAI, and now gaming updates 
GitHub - Check out the full mod source code 
Dev.to - More technical deep-dives 
AWS Community - Join the conversation 
I'm Carlos Cortez, this is Breaking the Cloud , and today we broke it with diamond swords. See you in the next one!
Top comments (1) 
Subscribe 
Personal 
Trusted User 
Create template
Templates let you quickly answer FAQs or store snippets for re-use.
Submit 
Preview 
Dismiss 
Collapse 
Expand 
PEACEBINFLOW
PEACEBINFLOW
PEACEBINFLOW
Follow 
Founder of SAGEWORKS AI — building the Web4 layer where AI, blockchain & time flow as one. Creator of Mind’s Eye and BinFlow. Engineering the future of temporal, network-native intelligence.
Email
peacethabibinflow@proton.me 
Location
BOTSWANA MAUN
Pronouns
he
Work
Founder & System Architect at SAGEWORKS AI
Joined
Oct 31, 2025 
• 
May 5
Dropdown menu 
Copy link 
Hide
The line about AI handling the mechanics while you brought the creativity is the one that's going to stick with me. It maps onto something I've been noticing but hadn't articulated: the division of labor that actually works in these collaborations isn't "AI does the easy stuff, human does the hard stuff." It's "AI does the stuff with clear right answers, human does the stuff where there are no right answers." Fabric's NBT serialization pattern for 1.21.1 has a correct implementation. Whether S3 should sound like an Enderman teleport doesn't.
What's interesting is that this means the AI's value is highest in the areas where you, as a first-time modder, had the least intuition — the boilerplate, the registry patterns, the Gradle config. The stuff that would have taken hours of documentation reading. And your value was highest in exactly the areas where the AI would have produced something generic: the thematic coherence, the joke density, the decision to make Lambda minions baby zombies because they're "small and ephemeral." That's genuinely clever in a way that requires understanding both the AWS concept and the Minecraft aesthetic.
The EC2 sword's Spot Instance mechanic is the one that makes me think this mapping has more depth than a one-off gag. A 20% chance of a critical hit isn't just a random crit — it's specifically modeling the Spot Instance pattern where you get cheap compute that can vanish at any moment. The mechanic teaches the concept through play. I could see someone who's never touched AWS internalizing "EC2 has two different scaling models, one steady and one probabilistic" just from swinging the sword enough times.
The question I'm left with is whether the swords that map cleanly to discrete actions (Lambda summons allies, S3 stores items) will always feel more satisfying than the ones that map to more abstract services. CloudWatch revealing mobs in a radius makes intuitive sense as a scanner. But IAM denying mob special abilities — that's a debuff, which in Minecraft often feels less visceral than a summon or a storage mechanic. Do you think some AWS services just resist translation into satisfying game verbs, or does the right design always exist if you dig deep enough into what the service actually does?
Like comment: 
Like comment: 
1  like 
Like
Comment button 
Reply 
Code of Conduct 
• 
Report abuse 
Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink .
Hide child comments as well
Confirm
For further actions, you may consider blocking this person and/or reporting abuse
