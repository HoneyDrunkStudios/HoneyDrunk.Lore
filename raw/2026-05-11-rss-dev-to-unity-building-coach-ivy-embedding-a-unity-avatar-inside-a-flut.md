---
source: "https://dev.to/likwifi/building-coach-ivy-embedding-a-unity-avatar-inside-a-flutter-app-4mpm"
title: "Building Coach Ivy: Embedding a Unity Avatar Inside a Flutter App"
author: "DEV.to Unity"
date_published: "Fri, 08 May 2026 10:16:30 +0000"
date_clipped: "2026-05-11"
category: "Game Development / Unity"
source_type: "rss"
---

# Building Coach Ivy: Embedding a Unity Avatar Inside a Flutter App

Source: https://dev.to/likwifi/building-coach-ivy-embedding-a-unity-avatar-inside-a-flutter-app-4mpm

try {
if(localStorage) {
let currentUser = localStorage.getItem('current_user');
if (currentUser) {
currentUser = JSON.parse(currentUser);
if (currentUser.id === 3917789) {
document.getElementById('article-show-container').classList.add('current-user-is-article-author');
}
}
}
} catch (e) {
console.error(e);
}
Minas Aslanyan 
Posted on May 8 
Building Coach Ivy: Embedding a Unity Avatar Inside a Flutter App
# ai 
# mobile 
# unity3d 
Most nutrition apps feel like spreadsheets with a barcode scanner.
Coach Ivy started with a different idea:
What if calorie tracking felt less like filling out a form and more like talking to a tiny 3D anime coach who actually reacts to your meals?
That single product decision changed the whole technical architecture.
A normal Flutter UI was not enough. We needed a real-time 3D character, facial animation, avatar customization, mood reactions, and smooth communication between the app layer and the avatar layer.
So we built Coach Ivy as a hybrid mobile app:
Flutter for the app UI, onboarding, food logging, subscriptions, analytics, and navigation 
Unity embedded inside the Flutter layer for the 3D avatar experience 
Ready Player Me / Animaze-style avatar generation for creating the character base 
SALSA LipSync for 3D BlendShape-based mouth animation 
A custom message bridge between Flutter and Unity so the AI coach could react to app events 
The result is an AI calorie tracker that feels less like a database form and more like a playful character experience.
This post is a breakdown of the dev side.
Why Flutter + Unity?
Flutter is great for building polished mobile apps quickly.
It gives you fast UI iteration, cross-platform structure, and a strong ecosystem for things like Firebase, RevenueCat, analytics, onboarding, and app flows.
But Flutter is not the best tool when your core product experience depends on a 3D animated character.
For Coach Ivy, the avatar was not just decoration. It was part of the product.
The user logs food, gets feedback, sees progress, and Ivy reacts. That means the character needed:
Idle animations 
Facial expressions 
Mood states 
Mouth movement 
BlendShape control 
A proper 3D scene 
Lighting, camera, and model control 
Unity is much better for that part.
So instead of forcing everything into Flutter, we split the app into two layers:
Flutter app layer
- onboarding
- food logging
- meal photo flow
- nutrition results
- subscriptions
- analytics
- app navigation
Unity avatar layer
- 3D character
- animations
- facial expressions
- BlendShapes
- avatar scene
- camera / lighting
- mood reactions
Enter fullscreen mode 
Exit fullscreen mode 
Flutter owns the product.
Unity owns the character.
That separation made the app much easier to reason about.
The Core Architecture
At a high level, Coach Ivy works like this:
User action in Flutter
↓
Flutter sends event to Unity
↓
Unity updates avatar state
↓
Avatar reacts visually
↓
Flutter continues app flow
Enter fullscreen mode 
Exit fullscreen mode 
For example:
User scans a meal
↓
Flutter receives calories/macros from AI
↓
Flutter sends a "meal_logged" event to Unity
↓
Unity plays Ivy's reaction animation
↓
Ivy changes facial expression / mouth / pose
Enter fullscreen mode 
Exit fullscreen mode 
This is especially important for a photo calorie tracker , because the user experience should not end at “here are your numbers.”
The meal scan gives the data.
The avatar gives the reaction.
That is what makes the app feel alive.
Embedding Unity Inside Flutter
The tricky part is not making a Unity scene.
The tricky part is making Unity behave like part of a mobile app.
A standalone Unity app usually owns the full screen. But Coach Ivy needed Unity to live inside a Flutter experience.
Flutter still handles:
Navigation 
Screens 
Buttons 
Paywalls 
Forms 
Photo upload 
App state 
Unity is embedded as a visual and interactive layer.
In Flutter, the Unity view becomes part of the widget tree.
A simplified version looks like this:
Stack ( 
children: [ 
UnityWidget ( 
onUnityCreated: onUnityCreated , 
onUnityMessage: onUnityMessage , 
), 
Positioned ( 
bottom: 24 , 
left: 16 , 
right: 16 , 
child: MealResultCard (), 
), 
], 
) 
Enter fullscreen mode 
Exit fullscreen mode 
This lets us combine a real 3D character with Flutter-native UI.
That is powerful because the app still feels like a normal mobile app, not like a game menu wrapped around forms.
Communication Between Flutter and Unity
The bridge between Flutter and Unity is where the product starts to feel alive.
Flutter knows what the user is doing.
Unity knows how Ivy should react.
So Flutter passes events to Unity.
A simplified Flutter-side example:
void sendMealLoggedEvent ( MealResult result ) { 
final payload = { 
"type" : "meal_logged" , 
"calories" : result . calories , 
"protein" : result . protein , 
"tone" : "sassy" , 
"emotion" : "surprised" , 
}; 
unityController . postMessage ( 
"IvyAvatarController" , 
"OnFlutterEvent" , 
jsonEncode ( payload ), 
); 
} 
Enter fullscreen mode 
Exit fullscreen mode 
Then Unity receives it:
public void OnFlutterEvent ( string json ) 
{ 
var evt = JsonUtility . FromJson < IvyEvent >( json ); 
switch ( evt . type ) 
{ 
case "meal_logged" : 
PlayMealReaction ( evt ); 
break ; 
case "goal_completed" : 
PlayCelebration (); 
break ; 
case "water_reminder" : 
PlayReminderExpression (); 
break ; 
} 
} 
Enter fullscreen mode 
Exit fullscreen mode 
The key lesson:
Do not send random commands everywhere. Create a small event protocol.
Instead of calling Unity methods like this:
OpenMouth()
Blink()
LookAngry()
MoveArm()
SayText()
Enter fullscreen mode 
Exit fullscreen mode 
It is cleaner to send product-level events:
meal_logged
goal_completed
coach_message_started
coach_message_finished
streak_lost
streak_saved
Enter fullscreen mode 
Exit fullscreen mode 
Unity translates those into animations.
That keeps the Flutter side clean and avoids turning the app into a mess of random animation calls.
Avatar Generation Pipeline
For the avatar base, we used a Ready Player Me / Animaze-style workflow.
The rough pipeline looked like this:
Generate avatar
↓
Export avatar model
↓
Import into Unity
↓
Configure materials and rig
↓
Set up BlendShapes
↓
Connect animation controllers
↓
Render avatar inside Flutter
Enter fullscreen mode 
Exit fullscreen mode 
The important part was not just getting a model into Unity.
The important part was making sure the model had the right facial controls.
For a talking and expressive coach, the avatar needs useful facial BlendShapes.
At minimum, we wanted control over:
Mouth open / closed 
Smile 
Frown 
Blink 
Brows 
Surprised face 
Angry / strict expression 
Viseme-like mouth shapes for talking 
Without those, the character looks like a 3D statue.
And a nutrition coach that judges your snack choices should not look like a statue.
That personality is also why we positioned Coach Ivy as a kawaii calorie tracker , not just another food logging utility.
Using BlendShapes for Facial Animation
BlendShapes are named facial shape targets on a mesh.
For example:
mouthSmile
mouthOpen
eyeBlinkLeft
eyeBlinkRight
browDown
jawOpen
Enter fullscreen mode 
Exit fullscreen mode 
In Unity, they can be controlled from code through the SkinnedMeshRenderer .
Simplified example:
public class IvyFaceController : MonoBehaviour 
{ 
[ SerializeField ] private SkinnedMeshRenderer faceRenderer ; 
private int smileIndex ; 
private int mouthOpenIndex ; 
private void Awake () 
{ 
smileIndex = faceRenderer . sharedMesh . GetBlendShapeIndex ( "mouthSmile" ); 
mouthOpenIndex = faceRenderer . sharedMesh . GetBlendShapeIndex ( "mouthOpen" ); 
} 
public void SetSmile ( float value ) 
{ 
faceRenderer . SetBlendShapeWeight ( smileIndex , value ); 
} 
public void SetMouthOpen ( float value ) 
{ 
faceRenderer . SetBlendShapeWeight ( mouthOpenIndex , value ); 
} 
} 
Enter fullscreen mode 
Exit fullscreen mode 
Then a reaction can blend several facial states together:
public void PlaySassyReaction () 
{ 
SetSmile ( 65f ); 
SetBrowDown ( 25f ); 
SetMouthOpen ( 15f ); 
} 
Enter fullscreen mode 
Exit fullscreen mode 
This is where the character starts feeling less like a model and more like a personality.
Using SALSA for 3D Mouth Animation
For mouth movement, we used SALSA-style 3D BlendShape animation.
Instead of manually animating every mouth frame, the system can drive mouth shapes from audio or speech intensity.
The practical setup looks like this:
Audio / speech event
↓
SALSA analyzes signal
↓
SALSA drives mouth BlendShapes
↓
Avatar appears to speak
Enter fullscreen mode 
Exit fullscreen mode 
For Coach Ivy, this matters because the avatar is not just standing there.
She reacts, talks, complains, celebrates, and gives feedback.
The personality only works if the face supports it.
A basic text response is useful.
A 3D coach reacting with facial animation is much more memorable.
The Biggest Challenge: Lifecycle
Embedding Unity into Flutter is not just a rendering problem.
It is a lifecycle problem.
Mobile apps pause, resume, background, foreground, rotate, rebuild widgets, and sometimes kill views aggressively.
Unity does not behave like a normal Flutter widget.
So we had to think carefully about:
When Unity loads 
Whether Unity should stay alive between screens 
How to avoid reloading the scene too often 
How to pause animations when not visible 
How to avoid memory spikes 
How to handle hot restarts during development 
How to recover if the Unity view is destroyed 
The rule that helped:
Treat Unity like a heavy runtime, not like a normal UI component.
Do not rebuild it casually.
Do not mount and unmount it every time the user changes a tab.
Keep the Unity scene stable and send it events.
Performance Notes
A 3D avatar inside a mobile app can get expensive quickly.
Here are a few things that helped.
1. Keep the Unity scene small
We did not need a full game world.
We needed:
One avatar 
Simple lighting 
One camera 
Controlled animations 
Lightweight background 
The less Unity has to render, the better the app feels.
2. Avoid unnecessary texture size
Avatar textures can become surprisingly heavy.
For mobile, it is usually better to compress and resize aggressively instead of shipping desktop-quality textures.
3. Use Flutter for UI, not Unity
It is tempting to build buttons and overlays in Unity.
But for Coach Ivy, Flutter is better for app UI.
Unity should render the character.
Flutter should render the product interface.
4. Send events, not constant updates
Flutter should not spam Unity every frame.
Instead of sending:
mouth = 0.1
mouth = 0.2
mouth = 0.4
mouth = 0.3
Enter fullscreen mode 
Exit fullscreen mode 
Send:
coach_message_started
coach_message_finished
meal_logged
Enter fullscreen mode 
Exit fullscreen mode 
Let Unity handle animation internally.
What I Would Do Differently
If I were starting again, I would define the Flutter to Unity event contract earlier.
Something like:
type IvyEvent = 
| { type : " avatar_ready " } 
| { type : " meal_logged " ; calories : number ; protein : number ; mood : string } 
| { type : " coach_speaking " ; text : string ; emotion : string } 
| { type : " goal_completed " ; goalType : string } 
| { type : " idle_state " ; state : string }; 
Enter fullscreen mode 
Exit fullscreen mode 
Even if the app is not written in TypeScript, writing the protocol this way helps.
It prevents random one-off messages from growing into chaos.
Why This Was Worth It
This setup is more complex than a normal Flutter app.
But it also makes Coach Ivy feel different.
The point was not to build another calorie tracker.
The point was to make nutrition tracking feel more emotional, playful, and personal.
A Flutter-only app can track calories.
A Unity-powered avatar can react to them.
That difference matters.
Especially in consumer apps, the experience is part of the product.
For Coach Ivy, the 3D avatar is not just visual polish.
It is the interface.
You can see the live app here: Coach Ivy on the App Store .
Final Architecture
The final structure looks roughly like this:
Coach Ivy Mobile App
Flutter
├── onboarding
├── auth
├── meal logging
├── AI nutrition analysis
├── subscriptions
├── analytics
└── Unity bridge
Unity
├── avatar scene
├── Ready Player Me avatar
├── BlendShape controllers
├── SALSA mouth animation
├── idle animations
├── emotion states
└── Flutter event receiver
Enter fullscreen mode 
Exit fullscreen mode 
The main lesson:
Use the right engine for the right layer.
Flutter is excellent for app structure.
Unity is excellent for real-time character experience.
Together, they made Coach Ivy possible.
Closing Thought
Embedding Unity inside Flutter is not the simplest architecture.
But if your app depends on a living, reactive, animated character, it can be the right one.
Coach Ivy needed to feel like a cute but slightly bossy AI nutrition coach.
That meant the avatar had to move, react, talk, and judge food choices with personality.
Flutter gave us the app.
Unity gave us the character.
The bridge between them gave Coach Ivy her soul.
You can try the app at coachivy.app or download it from the App Store .
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
