---
source: "https://dev.to/gamedevtoollab/unity-63-input-system-a-practical-guide-to-gameplay-ui-and-rebinding-5bjk"
title: "Unity 6.3 Input System: A Practical Guide to Gameplay, UI, and Rebinding"
author: "GameDevToolLab"
date_published: "2026-10-14"
date_clipped: "2026-10-16"
category: "Game Development / Unity"
source_type: "rss"
date_modified: "2026-10-14"
---

# Unity 6.3 Input System: A Practical Guide to Gameplay, UI, and Rebinding

Detecting a key press is only the beginning of input handling.

The click that opens a menu also fires a weapon. Closing the pause screen makes the character jump. Mouse and gamepad camera controls feel inconsistent. A custom key binding disappears after restarting the game.

These problems share a design boundary: **reading input is not the same as deciding whether gameplay should accept it.**

This guide covers that boundary in Unity 6.3, from Input System setup to physics updates, UI interaction, pausing, and rebinding. The main examples target a single-player game controlled with a keyboard, mouse, or gamepad.

> **Version scope:** Unity 6.3 LTS (`6000.3`) and the Input System 1.20 API family. As of October 14, 2026, Unity's [package listing](https://docs.unity3d.com/6000.3/Documentation/Manual/com.unity.inputsystem.html) identifies **1.20.1** as released for Unity 6.3. Check your installed version in Package Manager. This is a practical input-design guide, not a list of features introduced exclusively in Unity 6.3.
>
> **Verification scope:** The code is a documentation-based reference implementation. It has **not** been compiled in the Unity Editor or tested in a running game or on target hardware.

## 1. Start with the Input System for new projects

Unity offers the legacy Input Manager, accessed through `UnityEngine.Input`, and the Input System package. For a new game, the Input System is a useful default when you need device-independent controls and configurable bindings. Unity's [input overview](https://docs.unity3d.com/6000.3/Documentation/Manual/Input.html) describes it as the newer, more flexible, better-supported approach.

Legacy input code often connects gameplay directly to a physical key:

```
// Legacy Input Manager example.
// Do not paste this into a project with only the new Input System enabled.
if (Input.GetKeyDown(KeyCode.Space))
{
    Debug.Log("Jump input");
}
```

Enter fullscreen mode

Exit fullscreen mode

With the Input System, make **“the Jump action was performed”** the gameplay entry point, rather than “Space was pressed.” Bind Space and a gamepad's bottom face button to the same action, and the jump implementation no longer needs a separate branch for each device. See Unity's [Actions documentation](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/Actions.html).

### Check the installation settings

Install the package through Package Manager, then inspect `Edit > Project Settings > Player > Other Settings > Active Input Handling`.

`Input System Package (New)` enables the new backend, `Input Manager (Old)` enables the legacy backend, and `Both` enables both. Changing this setting requires an Editor restart. See the [installation guide](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/Installation.html).

**Selecting Both is not a general fix for input bugs.**

It can help during a staged migration involving legacy assets. It will not prevent duplicate gameplay calls when old and new input code both invoke the same attack method. Decide which backend each input path uses.

## 2. Understand actions and bindings first

The core concepts separate a physical input from its meaning in your game. Unity's [Actions](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/Actions.html) and [Workflows](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/Workflows.html) documentation provides the broader model.

| Concept | Responsibility | Example |
| --- | --- | --- |
| Device / Control | A device and an input element on it | Keyboard / Space, Gamepad / leftStick |
| Action | The meaning of an operation | Move, Jump, Submit |
| Binding | A connection between a control and an action | Space → Jump |
| Action Map | A group of actions managed together | Player, UI |
| Input Action Asset | An asset containing maps, bindings, and related settings | An `.inputactions` file |
| Control Scheme | Device requirements and associated binding groups | Keyboard&Mouse, Gamepad |

An **Interaction** defines how an input must be performed. A **Processor** transforms its value. A [Hold Interaction](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.Interactions.HoldInteraction.html) waits for a sustained press; a deadzone processor can filter small [stick inputs](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.Controls.StickControl.html).

The basic flow is:

```
Keyboard Space -----+
                    +-- Binding -- Jump Action -- Gameplay jump request
Gamepad south ------+
```

Enter fullscreen mode

Exit fullscreen mode

Because the connection is separate from gameplay, adding a [rebinding screen](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/rebind-action-runtime.html) does not require rewriting the jump itself.

## 3. Choose one input-reading workflow

The Input System supports several workflows. Unity's [workflow guide](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/Workflows.html) presents **project-wide actions** as a standard starting point: configure one shared asset and access it from code. `PlayerInput` is another option, particularly when players need their own device assignments.

The main example here uses **project-wide actions for a single player**.

`PlayerInput`, generated C# wrappers, and `InputActionReference` are valid alternatives. The risk is accidentally mixing different action instances: changing a binding on one instance while gameplay reads another.

### Configure project-wide actions

Assign an Input Action Asset under `Project Settings > Input System Package > Input Actions`. Create one when none is assigned; inspect the existing asset otherwise. Project-wide actions are preloaded at startup and enabled by default. See [project-wide actions](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/about-project-wide-actions.html) and the [using-actions workflow](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/using-actions-workflow.html).

Create the following actions. Keep the existing `UI` map separate from gameplay.

| Map / Action | Action Type / Value | Bindings | Assumption used here |
| --- | --- | --- | --- |
| `Player/Move` | Value / Vector2 | WASD as a 2D Vector Composite; `<Gamepad>/leftStick` | WASD uses Digital Normalized |
| `Player/Jump` | Button | `<Keyboard>/space`; `<Gamepad>/buttonSouth` | No explicit Interaction |

Configure WASD as the **Up, Down, Left, and Right parts of a 2D Vector Composite**, not four independent Vector2 bindings. `buttonSouth` identifies a gamepad's bottom face button; it is not an instruction to label that button “A” on every controller.

The code looks up `Player/Move` and `Player/Jump`. Keep these names consistent between the asset and the implementation.

## 4. Separate “pressed,” “just pressed,” and “performed”

### Action Type is not the C# value type

The Action Type choices `Value`, `Button`, and `Pass Through` describe behavior, not C# types such as `float` or `Vector2`. See the [InputActionType reference](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.InputActionType.html).

`Value` handles values such as movement direction and resolves competing controls. `Button` is intended for button-like behavior with a press threshold. `Pass Through` normally forwards changes without that control-conflict resolution.

Using Pass Through everywhere is not a shortcut to a simpler design. A UI with several pointers has different requirements from a character that needs one movement direction.

### Choose the appropriate polling API

| API | Question it answers |
| --- | --- |
| `ReadValue<Vector2>()` | What is the current value, such as movement direction? |
| `IsPressed()` | Is the action currently considered pressed? |
| `WasPressedThisFrame()` | Did its input cross the press threshold in this input frame? |
| `WasReleasedThisFrame()` | Did it transition out of the pressed state in this input frame? |
| `WasPerformedThisFrame()` | Did the action reach `performed` in this input frame? |

Here, “frame” depends on the Input System's [update mode](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.InputSettings.UpdateMode.html). This guide assumes Dynamic Update. The [InputAction API](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.InputAction.html) documents these distinctions.

For a [Hold Interaction](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.Interactions.HoldInteraction.html), beginning a press and satisfying the hold duration are different events. Using `WasPressedThisFrame()` for a hold-to-confirm command reacts before the hold requirement has been met.

**Choose whether you need a press-threshold transition or confirmation that the action has reached `performed`.**

### Callbacks do not necessarily mean “once per press”

Actions have `started`, `performed`, and `canceled` phases. Their transitions depend on Action Type and Interaction, and changing input can produce multiple callbacks in one frame. Do not treat `performed` as a once-per-rendered-frame update. See [action callbacks](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/set-callbacks-on-actions.html) and the [InputAction reference](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.InputAction.html).

Likewise, `canceled` does not always mean the player physically released a button. Disabling an action that is in progress can cancel it. A map disabled when opening a menu should not accidentally trigger another gameplay operation through its cancellation handler.

An `InputAction.CallbackContext` is valid during its callback. Copy the value or timestamp you need; do not retain the context for later use. The [callback guide](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/set-callbacks-on-actions.html) explains this lifetime constraint.

```
// Example statements inside an input callback.
// Copy the values instead of storing the context in a queue.
Vector2 direction = context.ReadValue<Vector2>();
double inputTime = context.time;
```

Enter fullscreen mode

Exit fullscreen mode

Pair event subscriptions with unsubscriptions. Two separately written lambdas in `+=` and `-=` do not reliably identify the same subscription; use a named handler or retain the delegate you subscribed.

## 5. Separate input collection from gameplay consumption

### Do not mix Update and FixedUpdate blindly

`Update Mode` selects when the Input System processes events. This guide uses the default, `Process Events In Dynamic Update`, which processes input before the normal `Update` callbacks. Physics commonly runs in `FixedUpdate`, whose frequency does not match rendering.

Do not read action frame-state APIs from `FixedUpdate` simply because that was your previous input pattern. Unity documents that input-state queries in the wrong update context can log errors in the Editor and development builds. Define both the input-update interval and the gameplay-consumption interval. See [InputSettings.UpdateMode](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.InputSettings.UpdateMode.html).

Here, **Update collects input; physics receives cached values and a request it can consume once**.

```
Input System update
    |
Update: cache movement / retain a jump request
    |
FixedUpdate: read cached movement / consume the request once
```

Enter fullscreen mode

Exit fullscreen mode

This is a bridge between update loops, not a promise of zero input latency. Player-loop ordering still determines when physics receives a newly collected request.

### Reference implementation: a buffer that reads shared actions

Save the following as `GameplayInputBuffer.cs` and attach it to a GameObject that remains active during gameplay. It requires the project-wide actions configured above and Dynamic Update mode.

```
using UnityEngine;
using UnityEngine.InputSystem;

public sealed class GameplayInputBuffer : MonoBehaviour
{
    private InputAction moveAction;
    private InputAction jumpAction;

    private Vector2 move;
    private bool jumpRequested;
    private bool gameplayAllowed = true;
    private int blockedFrame = -1;

    // Return cached input instead of reading shared actions in FixedUpdate.
    public Vector2 Move => CanUseInput ? move : Vector2.zero;

    private bool CanUseInput =>
        isActiveAndEnabled &&
        gameplayAllowed &&
        Application.isFocused &&
        Time.frameCount != blockedFrame &&
        moveAction != null &&
        jumpAction != null &&
        moveAction.enabled &&
        jumpAction.enabled;

    private void Start()
    {
        InputActionAsset actions = InputSystem.actions;
        if (actions == null)
        {
            Debug.LogError(
                "Assign a project-wide Input Action Asset.", this);
            enabled = false;
            return;
        }

        moveAction = actions.FindAction("Player/Move");
        jumpAction = actions.FindAction("Player/Jump");

        if (moveAction == null || jumpAction == null)
        {
            Debug.LogError(
                "Player/Move and Player/Jump are required.", this);
            enabled = false;
        }
    }

    private void Update()
    {
        if (!CanUseInput)
        {
            ClearBufferedInput();
            return;
        }

        move = Vector2.ClampMagnitude(
            moveAction.ReadValue<Vector2>(), 1f);

        // Keep the request until the next physics update consumes it.
        // Assignment alone could clear it in an Update before consumption.
        jumpRequested |= jumpAction.WasPerformedThisFrame();
    }

    // Use a single consumer. Reading the request here clears it.
    public bool ConsumeJump()
    {
        bool result = CanUseInput && jumpRequested;
        jumpRequested = false;
        return result;
    }

    // Call from the manager that controls states such as pause or dialogue.
    public void SetGameplayAllowed(bool allowed)
    {
        if (gameplayAllowed == allowed)
            return;

        gameplayAllowed = allowed;
        DiscardForCurrentFrame();
    }

    // Prevent a UI operation in this frame from carrying into gameplay.
    public void DiscardForCurrentFrame()
    {
        blockedFrame = Time.frameCount;
        ClearBufferedInput();
    }

    private void OnEnable()
    {
        DiscardForCurrentFrame();
    }

    private void OnDisable()
    {
        ClearBufferedInput();
    }

    private void OnApplicationFocus(bool hasFocus)
    {
        // Discard on both focus loss and focus regain.
        DiscardForCurrentFrame();
    }

    private void ClearBufferedInput()
    {
        move = Vector2.zero;
        jumpRequested = false;
    }
}
```

Enter fullscreen mode

Exit fullscreen mode

Project-wide actions are shared resources. This component **borrows them for reading**: it does not disable them or call `Dispose()` from `OnDisable`. It also caches action references rather than searching every frame. This ownership choice follows from the shared [project-wide workflow](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/about-project-wide-actions.html), not a rule that every independently owned action must stay enabled.

#### What the consumer must do

In the controller's `FixedUpdate`, read `Move` and call `ConsumeJump()` once. Use the returned request and conditions such as grounded state to decide whether to jump.

**Calling `ConsumeJump()` only while grounded can preserve an airborne request until landing.** For this sample, consume first, then decide whether the current gameplay state permits the jump.

The boolean means only “at least one unconsumed request exists.” It does not count multiple presses or implement a timed input-buffer window. Combos, replays, and network synchronization need an appropriate history or queue, usually with timestamps or simulation ticks.

## 6. Preserve the meaning of movement and look input

### Diagonal movement and analog magnitude

Adding W and D as `(1, 1)` produces a vector of length `√2`. Multiplying it directly by movement speed makes diagonal movement faster.

For keyboard input, a 2D Vector Composite in [Digital Normalized mode](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.Composites.Vector2Composite.html) normalizes the digital direction. Check the Composite's mode rather than assuming all configurations behave the same way.

However, do not apply `normalized` indiscriminately to gamepad input:

```
Stick input: (0.2, 0.0)

Preserve its value -> movement reflects the slight deflection
Normalize it      -> (1.0, 0.0), losing the original magnitude
```

Enter fullscreen mode

Exit fullscreen mode

The sample uses `Vector2.ClampMagnitude(value, 1f)` to cap oversized vectors while retaining analog values below length 1.

Gamepad sticks also normally have a deadzone at the Control level. Adding another deadzone to the Binding without checking the existing setup can make the effective deadzone larger than intended. Inspect the [StickControl configuration](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.Controls.StickControl.html) before stacking processors.

### Mouse delta and stick input have different units

Mouse `delta` is accumulated movement within an input update. A stick reports its current deflection. These are not interchangeable quantities. See [DeltaControl](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.Controls.DeltaControl.html) and [StickControl](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.Controls.StickControl.html).

For camera rotation, a useful interpretation is:

```
Mouse:
Rotation = displacement this update * sensitivity

Stick:
Rotation = deflection * maximum angular speed * deltaTime
```

Enter fullscreen mode

Exit fullscreen mode

Multiplying mouse displacement by `deltaTime` again can introduce unwanted frame-rate dependence. Custom sensitivity definitions or filtering may differ, but start by separating **displacement from velocity**.

One clear design uses `LookPointer` bound to `<Mouse>/delta` and `LookStick` bound to `<Gamepad>/rightStick`, converting each separately. A shared Look action still needs an interpretation that accounts for the contributing device.

Because mouse delta accumulates, repeatedly adding every callback's value can also double-count earlier movement. Decide whether to poll the accumulated value once or process individual event deltas. The [DeltaControl API](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.Controls.DeltaControl.html) explains its accumulation behavior.

## 7. Pausing time is not the same as pausing input

`Time.timeScale = 0` does not disable gameplay actions. It also stops `FixedUpdate`, so an unpause command handled only by physics will have no opportunity to run. See [Time.timeScale](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Time-timeScale.html) and [input update modes](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.InputSettings.UpdateMode.html).

Manage input permissions separately from time. For example:

| Map / Responsibility | Normal gameplay | Menu open |
| --- | --- | --- |
| Player: movement, attacks | Accept input | Reject input |
| UI: navigation, submit, cancel | Accept only where needed, such as the HUD | Accept input |
| System: pause toggle | Accept according to game state | Accept the unpause command |

`System` is a suggested map name, not a guaranteed built-in map.

Merely separating actions into maps does not establish this policy. [Project-wide actions](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/about-project-wide-actions.html) are enabled by default; a manager must set map states or acceptance conditions at startup and during transitions.

Calling `SetGameplayAllowed(false)` clears pending input and blocks this buffer. Calling it with `true` allows input again. It does **not** block another script that reads the actions directly.

Choose where the policy lives: one input entry point, centrally managed map activation, or consistently applied gameplay acceptance rules.

### Do not carry the menu-closing input into gameplay

Disabling a map does not necessarily clear an already-recorded `WasPressedThisFrame()` result during the same input frame. The [action API](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.InputAction.html) distinguishes recorded input from the action's current enabled state.

That is why the sample discards input for the transition frame. It gives gameplay a separate acceptance boundary.

However, this does not fully solve returning to gameplay while still holding the confirm button. Commands such as confirm and attack may need a **release-before-reacceptance** state. Value actions' initial-state checks after enabling are also not identical to Button press detection; see the [InputAction reference](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.InputAction.html).

Finally, processing the same pause command in both UI and System can open and immediately close a menu. One manager should own the state transition.

## 8. Handle UI input separately from gameplay

### uGUI and UI Toolkit need different configurations

Unity 6.3's input setup depends on the UI stack. A UI Toolkit-only screen does not automatically require a scene EventSystem just because an older tutorial uses one. See Unity's [runtime UI event-system documentation](https://docs.unity3d.com/6000.3/Documentation/Manual/UIE-Runtime-Event-System.html).

| UI configuration | Basic setup when using the Input System |
| --- | --- |
| uGUI | EventSystem + InputSystemUIInputModule |
| UI Toolkit only | Default runtime event system; no scene EventSystem required |
| uGUI and UI Toolkit together | EventSystem + InputSystemUIInputModule for integration |

Check that a legacy `StandaloneInputModule` has not been left in an incompatible configuration. Do not add duplicate modules or EventSystems without deciding which route owns UI event processing. See [InputSystemUIInputModule](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.UI.InputSystemUIInputModule.html).

### A UI click does not automatically block gameplay fire

A UI control handling a click and gameplay being allowed to fire are separate decisions.

Input System 1.20 does provide overlap handling through `InputAction.Priority` when `shortcutKeysUseActionPriority` is enabled. That mechanism is not, by itself, a complete policy for menu visibility, focus, or game state. See the [Priority API](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.InputAction.html).

For a full-screen menu, blocking gameplay input centrally is often clearest. When a small UI shares the screen with active gameplay, decide which recipient owns each pointer operation.

### Be careful when calling IsPointerOverGameObject

A common pattern is to call this from an input callback:

```
// This is not automatically safe to call inside an input callback.
EventSystem.current.IsPointerOverGameObject();
```

Enter fullscreen mode

Exit fullscreen mode

`InputSystemUIInputModule` updates pointer state as part of EventSystem processing. Input action callbacks run earlier, so querying there can read the previous frame's UI state and produces a warning. See the [module's API documentation](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.UI.InputSystemUIInputModule.html).

Possible designs include storing the request and checking after UI processing, or explicitly raycasting from a stored pointer position. Under the normal update order, `LateUpdate` can be a place for post-processing. But checking only the current hover state there does not classify every interaction correctly.

A drag that starts over UI may need to remain owned by that UI after the pointer leaves it. Conversely, dragging from the world onto UI should not necessarily transfer ownership.

**Record the starting owner and pointer ID, then retain that ownership until release.** For multiple touches, one global “pointer is over UI” boolean is insufficient.

With `InputSystemUIInputModule`, a negative ID in `IsPointerOverGameObject` means **any pointer**, not specifically the mouse. Text-field focus is also a separate state from pointer hover. See the [pointer-query reference](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.UI.InputSystemUIInputModule.html).

### Keep cursor locking consistent with screen state

A first-person game may lock and hide the cursor during play, then unlock and show it in menus. Focus changes can affect the lock state, so reconcile it with the current screen state rather than setting it only once at startup. See [Cursor.lockState](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Cursor-lockState.html).

## 9. With PlayerInput, read that player's actions

`PlayerInput` manages player-associated devices, control schemes, and notification behavior. It is useful for scenarios such as local multiplayer. See the [component overview](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/about-player-input-component.html).

When switching from the project-wide approach, the critical change is where action references come from:

```
// Initialization excerpt for a component that uses PlayerInput.
// playerInput must refer to the intended player.
InputAction moveAction = playerInput.actions.FindAction("Player/Move");
```

Enter fullscreen mode

Exit fullscreen mode

For player-specific input, do not replace that reference with `InputSystem.actions` or construct a separate generated wrapper with `new`.

When multiple `PlayerInput` components use the same asset, the first uses the supplied actions and subsequent players receive copies. The safe rule is not “every PlayerInput always creates a copy”; it is **use the target component's `actions` property**. Rebinding must target that same instance. See [PlayerInput.actions](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.PlayerInput.html).

Similarly, `Gamepad.current` does not mean “the gamepad assigned to this player.” Use player-device pairing and that player's actions.

### Avoid duplicate notification paths

PlayerInput supports Send Messages, Broadcast Messages, Invoke Unity Events, and Invoke CSharp Events. Message-based handlers use `InputValue`, while other routes use `InputAction.CallbackContext`. See [notification behaviors](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/select-notification-behavior.html).

Registering an Inspector Unity Event and subscribing the same operation directly to `performed` can execute it twice. Choose one notification route for each gameplay operation.

PlayerInput's configured notification behavior and direct subscriptions to `playerInput.actions` are separate mechanisms. When a route such as `onActionTriggered` delivers multiple phases, filter for the phase you need, for example with `context.performed`. See [notifications](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/select-notification-behavior.html) and [callbacks](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/set-callbacks-on-actions.html).

Also check `Default Action Map`. When it is unspecified, PlayerInput itself does not enable a map at startup. Other code enabling a map is a separate case, as documented in [PlayerInput](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.PlayerInput.html).

For player-specific UI, connect PlayerInput's `UI Input Module` to an `InputSystemUIInputModule` configured with the same Action Asset. Multiplayer UI requires more than duplicating an ordinary EventSystem for every player; follow the [PlayerInput UI workflow](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/use-player-input-component-ui.html).

Device-lost and device-regained notifications let you implement a policy for disconnection: pause, switch devices, or require confirmation on return. When disconnecting pauses gameplay, clear pending requests through the central manager so stale commands do not execute after reconnection. See [notification behaviors](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/select-notification-behavior.html).

## 10. Rebinding needs reliable cleanup, not just a start button

`PerformInteractiveRebinding()` supports runtime control reassignment through Binding Overrides rather than rewriting the original bindings. Unity's **Rebinding UI** sample, available through Package Manager, is a useful starting point. See the [runtime rebinding guide](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/rebind-action-runtime.html).

Starting an input-listening operation is only one part of a usable controls screen.

### Identify the binding you are changing

Jump can have both keyboard and gamepad bindings. WASD additionally contains a Composite root and separate direction parts. Rebind the intended **part**, not the Composite root as though it were one key.

Storing only an array index in long-lived UI configuration is fragile: editing the asset can reorder bindings. Retain the [Binding ID](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.InputBinding.html#UnityEngine_InputSystem_InputBinding_id) and resolve its current index at runtime. Deleting and recreating a binding changes its ID, so even this approach needs a migration policy when the asset changes incompatibly.

### Manage the rebinding lifecycle

The target action must be disabled when configuring the operation against it. Coordinate gameplay gating and Action or Map state with the input manager; merely blocking this article's buffer does not disable the underlying action. See [RebindingOperation](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.InputActionRebindingExtensions.RebindingOperation.html).

| Stage | Responsibility |
| --- | --- |
| Before starting | Resolve the target binding, disable the action, and define accepted controls and cancellation |
| Listening | Retain the operation and avoid capturing the input that opened the rebinding screen |
| Completion | Refresh the displayed binding and save overrides |
| Cancellation | Return the screen to its normal state without treating the operation as a completed assignment |
| Screen closure or destruction | Cancel the active operation and clean it up |
| Every exit path | Dispose the operation and restore input permissions appropriate to the current screen state |

`RebindingOperation` owns unmanaged resources. Missing `Dispose()` can leak memory. Cover completion, cancellation, component disablement, screen destruction, and setup exceptions. See the [rebinding documentation](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/rebind-action-runtime.html).

Do not blindly re-enable an action because it was enabled before rebinding. Another modal screen may now require gameplay to remain blocked. Restore input according to the manager's **current** state.

Filter accepted controls so a keyboard rebind does not capture mouse movement or an unrelated gamepad. `WithCancelingThrough()` provides a cancellation path. Reserving Escape for cancellation also means it cannot be assigned through that particular interaction. See [rebinding configuration](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/rebind-action-runtime.html).

### Define conflicts and recovery behavior

Whether several actions may share a key is a game-design decision. Permit it, swap assignments, or warn according to your intended controls.

If every confirm, back, and menu command can be rebound, players may make the settings screen impossible to navigate. Keep a way to recover, such as a reset-to-defaults control or a recovery command outside the editable bindings.

## 11. Save binding overrides and restore the same runtime asset

Use `SaveBindingOverridesAsJson()` and `LoadBindingOverridesFromJson()` to persist overrides. Serializing the whole Action Asset with `ToJson()` is not equivalent. See [InputActionRebindingExtensions](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.InputActionRebindingExtensions.html).

The following single-user example belongs in `BindingOverrideStorage.cs`. Its recovery policy is to remove invalid saved settings and return to the asset's default bindings.

```
using System;
using UnityEngine;
using UnityEngine.InputSystem;

public static class BindingOverrideStorage
{
    // Migrate or update this key when the action/binding layout breaks compatibility.
    private const string SaveKey = "input.binding-overrides.v1";

    public static void Save(InputActionAsset runtimeActions)
    {
        Validate(runtimeActions);

        string json = runtimeActions.SaveBindingOverridesAsJson();
        PlayerPrefs.SetString(SaveKey, json);
        PlayerPrefs.Save();
    }

    public static bool TryLoad(InputActionAsset runtimeActions)
    {
        Validate(runtimeActions);

        if (!PlayerPrefs.HasKey(SaveKey))
            return false;

        try
        {
            string json = PlayerPrefs.GetString(SaveKey);
            if (string.IsNullOrWhiteSpace(json))
                throw new FormatException("Saved binding data is empty.");

            runtimeActions.LoadBindingOverridesFromJson(
                json, removeExisting: true);
            return true;
        }
        catch (Exception exception)
        {
            // Handle exceptions only at the saved-settings restoration boundary.
            // This is not a pattern for suppressing errors throughout the game.
            runtimeActions.RemoveAllBindingOverrides();
            PlayerPrefs.DeleteKey(SaveKey);
            PlayerPrefs.Save();

            Debug.LogWarning(
                "Could not restore input settings; defaults have been restored." +
                $" {exception.GetType().Name}: {exception.Message}");
            return false;
        }
    }

    public static void ResetToDefaults(InputActionAsset runtimeActions)
    {
        Validate(runtimeActions);

        runtimeActions.RemoveAllBindingOverrides();
        PlayerPrefs.DeleteKey(SaveKey);
        PlayerPrefs.Save();
    }

    private static void Validate(InputActionAsset runtimeActions)
    {
        if (runtimeActions == null)
            throw new ArgumentNullException(nameof(runtimeActions));
    }
}
```

Enter fullscreen mode

Exit fullscreen mode

Pass the Action Asset that **gameplay actually uses**:

| Workflow | Save and restore this asset |
| --- | --- |
| Project-wide actions | `InputSystem.actions` |
| PlayerInput | The target player's `playerInput.actions` |

Load once after the runtime asset is available and before accepting gameplay input. Unconditionally loading whenever the settings screen opens can overwrite unsaved edits.

A successful JSON load does not guarantee that every saved Binding ID still matches the current asset. Parsing success and a complete, correct configuration migration are different checks. See the [override-loading API](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.InputActionRebindingExtensions.html).

This example uses one user and one storage key. Multiple profiles or players need separate save keys **and** separate application targets. Save when settings are committed, not every frame.

For readable labels, use `GetBindingDisplayString()` and, where appropriate, device-specific icons instead of displaying paths such as `<Gamepad>/buttonSouth` directly. See the [binding-display API](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.InputActionRebindingExtensions.html).

## 12. Text and touch need more than gameplay button handling

### Distinguish physical keys from entered text

Keyboard controls represent physical key positions. Different layouts need not produce the same character at a given position, so converting key codes into characters is not a complete text-entry implementation. See the [Keyboard API](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.Keyboard.html).

Custom text entry may use `Keyboard.onTextInput`, but also needs to consider IME composition, including Japanese text, uncommitted text, caret movement, selection, and paste. For names or chat, begin with a UI text field and suppress gameplay shortcuts while it has text-entry focus.

“Accept WASD whenever the pointer is outside the field” fails as soon as a focused field keeps receiving text after the mouse moves away. Coordinate **text-entry focus** with gameplay permission.

### Track each finger's interaction

For frame-by-frame tap or swipe tracking, EnhancedTouch provides finger and touch history rather than requiring you to assemble everything from the low-level [Touchscreen](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.Touchscreen.html) API.

Call `EnhancedTouchSupport.Enable()` before using it, and balance that with `Disable()` when the usage ends. Multiple callers must balance their enable and disable counts; opening a screen repeatedly must not keep adding unmatched enables. See [EnhancedTouchSupport](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.EnhancedTouch.EnhancedTouchSupport.html).

Do not assume touch array index zero still represents the same ongoing interaction. Track touch IDs or the appropriate Finger, including whether its gesture began on UI or in the game world.

## 13. Debug the path before blaming gameplay code

Open `Window > Analysis > Input Debugger` to inspect devices, control state, and actions. Unity's [Input Debugger guide](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/the-input-debugger-window.html) describes the available inspection tools.

Trace the input path in order:

```
Is the device recognized?
    |
Does the relevant control value change?
    |
Does the binding resolve to that control?
    |
Is the action / map enabled?
    |
Do control schemes or device assignments exclude it?
    |
Does input reach the intended notification route?
    |
Does gameplay reject or consume it before the expected operation?
```

Enter fullscreen mode

Exit fullscreen mode

The following checks narrow down common symptoms:

| Symptom | Start by checking |
| --- | --- |
| A legacy asset stops responding after migration | Active Input Handling and old API dependencies |
| PlayerInput does not react | Default Action Map, notification behavior, and assigned devices |
| One press executes an operation several times | Phase filtering, duplicate subscriptions, multiple routes, and repeated consumption |
| Physics misses or repeats commands | Update Mode, sampling location, request retention, and consumption |
| Input remains after unpausing or regaining focus | Cached-state clearing, same-frame history, and release-before-reacceptance rules |
| Clicking UI also fires a weapon | UI/gameplay acceptance rules and pointer-query timing |
| A slight stick deflection causes full speed | Unconditional normalization and processor configuration |
| Only mouse look changes with frame rate | Extra time factors applied to delta |
| A rebind has no effect | Whether the modified and read Action Assets are the same runtime instance |
| A rebind disappears after restart | Save/load ordering, storage key, and changes to Binding IDs |

These are starting points, not diagnoses. One successful key press in the Editor is not a sufficient acceptance test.

Test menu transitions, focus changes while holding controls, gamepad disconnection and reconnection, different frame rates, and closing a screen during rebinding. Those transitions expose problems that a normal play-through can miss.

## Conclusion

Reliable input handling depends less on memorizing key-query APIs than on defining **what an operation means, who owns it, when it is consumed, and when pending input is discarded**.

Use actions to separate devices from gameplay. Separate collection from consumption. Make UI and pause permissions explicit. Rebind and restore the actual runtime asset, and make every rebinding exit path safe.

With those boundaries in place, adding gamepad support, configurable controls, or more screens becomes an extension of the design rather than another independent input path.
