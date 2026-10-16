---
source: "https://dev.to/nabeelbaghoor/your-xr-app-quietly-assumes-a-standing-adult-with-two-hands-58b6"
title: "Your XR App Quietly Assumes a Standing Adult With Two Hands"
author: "Nabeel Hassan"
date_published: "2026-10-12"
date_clipped: "2026-10-13"
category: "Game Development / Unity"
source_type: "rss"
---

# Your XR App Quietly Assumes a Standing Adult With Two Hands

If you build for the web, you have a reflex for accessibility by now. Semantic HTML, focus order, alt text, contrast ratios, a screen reader pass before release. It is not perfect, but there is a shared floor and tooling that tells you when you fall through it.

Then you open a headset project and almost none of that applies. There is no DOM for a screen reader to walk. There is no keyboard focus. Text does not get resized by the operating system. There is not even a flat surface at a predictable distance. What you get instead is a long list of assumptions about a human body that nobody wrote down, and every one of them shuts somebody out.

I have spent most of my career in Unity and XR, on things like ERIS XR (firefighter training) and Planes XR (location-based AR) for ARCortex and a clinical eye-tracking app for Nystag on the Vive Focus 3. This is the version of our XR accessibility guide I would hand to another developer, not to a buyer.

## The assumptions hiding in a "normal" scene

Open almost any VR prototype and you will find it quietly expects:

* a standing adult of roughly average height
* full range of motion, including turning all the way around and reaching above the head
* two working hands with a steady grip that can hold a trigger down
* good vision, normal color vision, and working stereo depth perception
* full hearing, including the ability to tell where a sound came from
* a stomach that tolerates moving without walking

None of these were decisions. They are defaults that fell out of whoever was wearing the headset during development. For a consumer game the cost is lost players. For mandatory training, a clinical assessment or a public exhibit, the cost is a person who cannot complete something they were required or invited to do.

The standards situation does not rescue you either. WCAG was written for pages and documents and only partly maps onto a 3D scene. The W3C has published XR accessibility user requirements, and the game accessibility guidelines cover a lot of the same ground from the player side. Both are good checklists. Neither is a compliance target for a headset app the way WCAG is for a website, so build to the intent instead of hunting for a badge.

## The one principle: every task has more than one route

If I had to compress the whole topic into one engineering rule, it is redundancy. Every essential task should be completable more than one way: controller or hand, standing or seated, by sound or by sight, by grabbing or by picking from a list.

That rule is also what keeps it cheap. Retrofitting accessibility means reworking scenes that were built around one input and one output. Designing for it up front mostly means your interaction layer has a small number of swappable paths, and each new scene uses them instead of talking to the controller directly.

In Unity that looks roughly like this. It is illustrative, not lifted from a client project:

```
// Illustrative: scenes depend on "the user activated this",
// never on "the right trigger was held for 0.5s".
public interface IActivationSource
{
    event System.Action<Interactable> Activated;
}

public class Interactable : MonoBehaviour
{
    public UnityEvent onActivate;
    bool toggled;

    // Every source funnels here: grab, ray select, gaze dwell, voice.
    public void Activate(AccessSettings s)
    {
        if (s.holdActionsAsToggles) { toggled = !toggled; }
        onActivate.Invoke();
    }
}

[System.Serializable]
public class AccessSettings
{
    public bool seatedMode;
    public float heightOffset;      // recalibrated, not assumed
    public bool holdActionsAsToggles;
    public float grabReach = 0.6f;  // metres; raise it to pull objects closer
    public float dwellSeconds = 1.2f;
    public bool captions = true;
    public float textScale = 1f;
}
```

The point is not the specific class shape. It is that "hold the trigger" and "grab with your left hand" never appear in scene scripts. Once that boundary exists, adding gaze plus dwell or a one-handed scheme is a new `IActivationSource`, not a rewrite of every level.

## Five kinds of exclusion, and the boring fixes

### Reach, posture and mobility

The most common failure. Controls placed high, objects on the floor, a scenario that needs you to turn around, or twenty minutes on your feet. That excludes wheelchair users, people with back or joint problems, people recovering from injury, and anyone who just cannot stand that long.

* Support seated use for every task, not just a seated menu. If the scenario needs someone to look behind them, give them snap-turn.
* Let users recalibrate height instead of building the world around an average standing eye line.
* Bring objects to the user. A reach distance setting or a pull-to-hand action removes most "I cannot reach it" bugs.
* Keep frequent controls low and close to the body. Everyone's shoulders will thank you.

### Hands and fine motor control

Two hands, steady grip, hold-to-act. That excludes limb differences, tremors, arthritis, an arm in a sling.

Ask for one-handed completion of every task, remappable controls, toggles instead of holds, and generous target sizes. The situational version of this showed up for us on ERIS XR: firefighters wear gloves, which changes what a hand can reliably do. Designing for a gloved hand and designing for limited dexterity overlap almost completely.

### Vision

* Text needs a size setting and enough contrast against whatever is behind it. In passthrough mixed reality, what is behind it is a real room you do not control.
* Never carry meaning with color alone. Red and green states should also differ in shape, icon or label.
* Do not make depth the only cue. People without stereo vision judge distance from size, shadow and motion, so a task that depends purely on binocular depth needs a second cue.
* Check that the headset you pick takes glasses spacers or prescription inserts. That is a hardware decision, not a code one, but it decides who can even start.

### Hearing

Spatial audio is one of XR's best tools and a wall if it is the only channel. A spoken instruction, an alarm behind the user, a character's line: each needs a visual equivalent.

Captions are harder here than on video because there is no bottom of the screen. They have to follow the user's view, say who is speaking, and point toward a sound that is out of sight. If any speech is generated at runtime, such as an AI character, it needs captioning as it is generated, not only for the scripted lines.

### Comfort and cognition

Some people cannot tolerate artificial locomotion at all. Some are sensitive to flashing or sudden loud sounds. Some find a dense scene overwhelming. The failure mode is silent: they take the headset off and do not tell you why.

Teleport and snap-turn, a way to reduce effects, short instructions, a pause that actually pauses, and resume without losing progress. I went deeper on the movement side in [Motion Sickness Is a Bug Your VR Team Cannot Reproduce](https://dev.to/nabeelbaghoor/motion-sickness-is-a-bug-your-vr-team-cannot-reproduce-5bdg).

## When the user did not choose to be there

Accessibility weighs more when the person in the headset has no choice.

Clinical tools are the clearest case. With Nystag, the people in the headset are patients in a clinic, and some of them may already feel unwell. Instructions have to be simple, setup has to fit a wide range of people, and the operator needs a way to help without taking the headset back.

Mandatory training is similar. If an XR module is part of someone's job, a person who cannot use it needs an equivalent path that is not a lesser version. Sometimes that is an accessible mode in the headset. Sometimes it is the same scenario on a flat screen. Decide which before rollout, not after the first complaint.

Shared and public experiences add one more constraint: settings have to be personal. In a shared mixed reality scene, one person's caption size or seated height cannot change the world for everyone else, which means those settings live per user and never get synced as scene state. If you have built multiplayer XR, you know that line between "my view" and "our world" is already the hardest part. This is one more thing on the "my view" side of it.

## How to test it

A checklist catches the obvious gaps. It does not tell you whether a person can finish the task.

* Run your longest scenario seated, one-handed, with sound off and comfort settings on. Note exactly where it breaks.
* Measure completion and time, not enjoyment. An accessible mode that exists but takes three times as long is a bug report.
* Test with disabled users, recruited and paid for their time. A handful of real users with relevant needs will find more than any internal review.
* Keep a feedback route open after launch, because the people you excluded are the least likely to have been in the pilot.

## What it costs

It depends almost entirely on timing. Decided in the spec, it is mostly design plus a modest amount of interaction layer work. Added after content production, it means reopening scenes that were built for a standing, two-handed, hearing, stereo-sighted user, and that is where the bill shows up.

The nice side effect is that redundancy helps people with no disability at all. Captions help in a loud workshop. Seated mode helps the tired trainee at the end of a shift. One-handed controls help the technician holding a real tool in the other hand. In my experience accessible XR is just sturdier XR.

The longer, client-facing version of this, with the questions to ask before commissioning a build, is on the Null Studio blog: [XR accessibility](https://nullstud.io/blog/xr-accessibility/).

If you have shipped XR with an accessibility mode, I would love to hear which single setting got used the most. My bet is seated mode, but I have never seen real numbers.
