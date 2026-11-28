---
source: "https://dev.to/toanlb_dev/2-week-deadline-where-does-clean-architecture-fit-fp"
title: "2-Week Deadline: Where Does Clean Architecture Fit?"
author: "Toàn Lương Bảo"
date_published: "2026-11-27"
date_clipped: "2026-11-28"
category: "Software Architecture"
source_type: "rss"
secondary_categories: ["Game Development / Unity"]
---

# 2-Week Deadline: Where Does Clean Architecture Fit?

There is a scenario familiar to almost anyone who has worked in mobile gaming, hyper-casual studios, or R&D prototyping teams:

Early Monday morning, your Lead or Producer walks in with urgent news: *"Marketing just spotted a surging trend. We need a playable prototype in 2 weeks to run a CPI validation campaign!"*

At that moment, developers typically gravitate toward one of two extremes:

1. **Dogmatic Clean Architecture:** Attempting textbook design patterns for a two-week prototype. You carve out four Clean Architecture rings, construct Use Cases, abstract Repositories behind interfaces, wire up a DI container, and write exhaustive unit tests for every method. By day 7, you are still building plumbing. The game misses its market test window, gets canceled, and every line of elegant code goes straight into the trash.
2. **Spaghetti Prototype:** Jamming all logic into a 3,000-line `GameManager.cs` file. Input handling, physics callbacks, sound triggers, scoring, and UI mutations are glued together with nested if-else ladders. The build ships right on time and test metrics look great. Management responds: *"Retention is awesome! Next week, let's add 5 new mechanics, 50 levels, ads, and IAP to scale!"* Suddenly, changing player move speed breaks weapon firing, UI buttons fail silently, and refactoring becomes a nightmare.

So here is the fundamental engineering question: **When faced with a strict 2-week deadline, should you discard architecture entirely, or is there a pragmatic middle ground?**

Based on years of shipping games under aggressive timelines, the solution is neither dogmatic purity nor chaotic hacking. It comes down to **pragmatic engineering compromise**.

---

## 1. The Disposable Architecture Mindset: Fast Internals, Strict Boundaries

In rapid prototyping, **Time-to-Market is king**. However, shipping fast does not mean writing unmaintainable garbage.

The core principle that keeps teams alive is **Disposable Architecture**: We accept that implementation details inside a module may be rushed or messy, but **the external boundary of that module must remain strictly isolated**.

```
flowchart TD
    subgraph BadPrototype["1. Spaghetti Prototype (No Boundaries)"]
        God["GameManager (3000 lines)\nInput, Combat, UI, Audio lumped together"]
        God -.->|"Tweaking mechanics breaks core flow"| Bug["System-wide cascading bugs"]
    end

    subgraph ModularBoundary["2. Disposable Architecture (Encapsulated Boundaries)"]
        Movement["Movement Module"]
        Combat["Combat Module"]
        UI["Health UI Module"]
        Coordinator["GameCoordinator (Slim Singleton)"]

        Combat -->|"Event OnDied"| UI
        Coordinator -->|"Enable or disable module"| Movement
        Coordinator -->|"Enable or disable module"| Combat
    end
```

Under this mindset, there are 3 non-negotiable boundaries you should never compromise, no matter how tight the deadline:

### Boundary 1: Flow Coordination via Singleton is Fine; God State is Not

In a 2-week sprint, constructor injection across deep inheritance trees slows you down. Using a [Singleton](https://dev.to/en/posts/why-large-projects-avoid-singleton/) as a fast global access point at the macro coordination level is an acceptable compromise.

However, the golden rule is: **Singletons may coordinate flow, but they must never store domain data**.

- `GameCoordinator.Instance` should only expose high-level orchestration: `StartGame()`, `PauseGame()`, `GameOver()`.
- Player health, inventory items, and score calculation belong in dedicated models or components. When designers tweak damage math, you modify a single isolated class without touching `GameCoordinator` or risking its lifecycle.

### Boundary 2: Decouple UI from Gameplay via Events and Rigorous Lifecycle Cleanup

During user acquisition tests, core gameplay mechanics might remain stable while **UI is redesigned repeatedly** based on conversion funnels and A/B tests.

If UI scripts reach directly into internal gameplay fields, replacing a horizontal health bar with a radial gauge requires rewriting combat code:

- The fix: Use simple `event Action` contracts. Gameplay simply fires: `OnHealthChanged?.Invoke(currentHp)`.
- UI views subscribe to state updates independently. If marketing asks for a complete UI reskin overnight, your gameplay scripts remain untouched.

> Warning
>
> Memory Leak Pitfalls with C# Events in Unity  
> In the .NET CLR, `MulticastDelegate` maintains a strong reference list (`_invocationList`) to subscribers. If a UI `MonoBehaviour` subscribes to a model with a longer lifecycle and omits unsubscribing (`-=`) in `OnDisable()` or `OnDestroy()`, the managed shell cannot be collected by the Garbage Collector. Furthermore, invoking that delegate after the underlying Unity object is destroyed throws a `MissingReferenceException`. Always adhere to: Subscribe in `OnEnable()`, unsubscribe in `OnDisable()`.

### Boundary 3: Encapsulate Features into Modular Blackbox Components

Instead of stacking movement, shooting, audio, and inventory into a single `PlayerController.cs`, decompose them into focused components attached to the same entity:

- `PlayerMovement`: Reads input and moves the Transform or Rigidbody.
- `PlayerWeapon`: Handles projectiles and fire rates.
- `PlayerCollector`: Detects trigger collisions with pickup items.

Inside `PlayerWeapon`, the code can be quick and dirty. But if designers suddenly request *"swap guns for melee swords"*, you simply detach `PlayerWeapon` and attach `PlayerMeleeAttack`. Movement and item collection keep running smoothly.

---

## 2. Practical Code: Spaghetti Coupling vs. Modular Boundaries

Consider a high-pressure scenario: You are participating in a 2-week Game Jam or building a rapid Proof-of-Concept for a Top-Down Arena Shooter (in the spirit of *Brotato* or *Crimsonland*). The player character dodges enemy swarms, equips distinct weapons (single-shot Pistol, multi-pellet Shotgun), takes collision damage, and tallies match scores.

Under an aggressive 14-day deadline, over-engineering a textbook Clean Architecture with full layers of Entities, Use Cases, Gateways, and DTOs burns valuable days on boilerplate, leaving no playable build for testing. Conversely, cramming weapon mechanics, health deductions, and HUD updates into a monolithic script guarantees that the codebase will seize up the moment designers request weapon adjustments in week two. The winning strategy is setting pragmatic boundaries: isolating volatile weapon logic behind lightweight interfaces and packaging health rules into pure C# classes verifiable by automated tests in seconds.

### 2.1. The Quick-and-Dirty Trap: Cascading Dependencies

During early prototype development, it is tempting to cram everything into one place:

```
using System;
using UnityEngine;

// Tightly coupled: One class carries all responsibilities
public class SpaghettiPlayerController : MonoBehaviour
{
    public int currentHp = 100;
    public int score = 0;
    public string currentWeaponType = "PISTOL";

    public void TakeDamage(int damage)
    {
        currentHp = Math.Max(0, currentHp - damage);

        // Issue 1: Direct coupling to UI presentation
        Debug.Log("Updating UI text: " + currentHp);

        if (currentHp <= 0)
        {
            // Issue 2: Hardcoded game over transition
            Debug.Log("Game Over! Trigger defeat screen");
        }
    }

    public int FireWeapon()
    {
        // Issue 3: Branching weapon math hardcoded into player
        if (currentWeaponType == "PISTOL")
        {
            return 10;
        }
        else if (currentWeaponType == "SHOTGUN")
        {
            return 25;
        }
        return 0;
    }
}
```

If designers introduce 3 new weapon variants with burst fire, spread patterns, and cooldown timers, this monolithic script balloons rapidly, risking regressions in health tracking and match states.

---

## 3. The Pragmatic Solution: Encapsulated Boundaries, MonoBehaviour Bridge, and Isolated Unit Tests

Rather than introducing heavy enterprise patterns with complex Use Case layers, we keep the architecture flat and clean using lightweight custom classes in our code sample: `PlayerBridge` (`MonoBehaviour` bridge), `PragmaticPlayer` (pure C# domain logic), the `IWeaponHandler` weapon contract, and `UIHealthView`:

```
flowchart LR
    Bridge["PlayerBridge (MonoBehaviour)"] -->|"Controls"| Player["PragmaticPlayer (Pure C#)"]
    Player -->|"Uses"| Weapon["IWeaponHandler\n(ScriptableObject or C# Class)"]
    Player -->|"Fires event"| UI["UIHealthView (Subscribes & Unsubscribes -=)"]
```

### 3.1. Flexible Weapon Contract and ScriptableObject Integration

Isolate weapon behaviors behind a lean interface. This contract allows developers to implement weapons via pure C# classes, or back them with a [`ScriptableObject`](https://dev.to/en/posts/when-to-use-prefab-json-scriptableobject/) so game designers can tweak balance directly in the Inspector without requiring code recompilation:

```
using System;
using UnityEngine;

// Minimal weapon contract
public interface IWeaponHandler
{
    string WeaponName { get; }
    int CalculateDamage();
}

public class PistolWeapon : IWeaponHandler
{
    public string WeaponName => "Pistol";
    public int CalculateDamage() => 15;
}

public class ShotgunWeapon : IWeaponHandler
{
    public string WeaponName => "Shotgun";
    public int CalculateDamage() => 40;
}

// ScriptableObject asset for rapid designer balancing
[CreateAssetMenu(fileName = "NewWeaponConfig", menuName = "Combat/Weapon Config")]
public class WeaponConfigSO : ScriptableObject, IWeaponHandler
{
    [SerializeField] private string weaponName = "Rifle";
    [SerializeField] private int baseDamage = 25;

    public string WeaponName => weaponName;
    public int CalculateDamage() => baseDamage;
}
```

### 3.2. Pure Player Class with Event Boundaries and Guard Clauses

The player class is written in pure C# with no `MonoBehaviour` dependency. Health tracking, weapon dispatching, and death checks are guarded against edge-case bugs:

```
public class PragmaticPlayer
{
    public int CurrentHp { get; private set; }
    public IWeaponHandler CurrentWeapon { get; private set; }
    public bool IsDead => CurrentHp <= 0;

    // Event boundary: Notifies external listeners on state changes
    public event Action<int> OnHealthChanged;
    public event Action OnDied;

    public PragmaticPlayer(int initialHp, IWeaponHandler startingWeapon)
    {
        CurrentHp = initialHp;
        CurrentWeapon = startingWeapon ?? throw new ArgumentNullException(nameof(startingWeapon));
    }

    public void EquipWeapon(IWeaponHandler newWeapon)
    {
        CurrentWeapon = newWeapon ?? throw new ArgumentNullException(nameof(newWeapon));
    }

    public int PerformAttack()
    {
        if (IsDead) return 0;
        return CurrentWeapon.CalculateDamage();
    }

    public void ReceiveDamage(int damage)
    {
        // Guard clause: Prevent dead state transitions or negative damage healing
        if (IsDead || damage <= 0) return;

        CurrentHp = Math.Max(0, CurrentHp - damage);
        OnHealthChanged?.Invoke(CurrentHp);

        if (CurrentHp == 0)
        {
            OnDied?.Invoke();
        }
    }
}
```

### 3.3. The Unity Engine Bridge: A Lean MonoBehaviour Presenter

To integrate pure C# domain logic into the Unity scene graph, we use a lightweight bridge component that also acts as a clean reference for lifecycle event subscriptions:

```
public class PlayerBridge : MonoBehaviour
{
    [SerializeField] private int maxHp = 100;
    [SerializeField] private WeaponConfigSO defaultWeapon;

    public PragmaticPlayer Model { get; private set; }

    private void Awake()
    {
        IWeaponHandler startingWeapon = defaultWeapon != null ? defaultWeapon : new PistolWeapon();
        Model = new PragmaticPlayer(maxHp, startingWeapon);
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Hazard"))
        {
            Model.ReceiveDamage(20);
        }
    }
}

// UI view demonstrating clean event lifecycle management
public class UIHealthView : MonoBehaviour
{
    [SerializeField] private PlayerBridge playerBridge;

    private void OnEnable()
    {
        if (playerBridge?.Model != null)
        {
            playerBridge.Model.OnHealthChanged += HandleHealthChanged;
        }
    }

    private void OnDisable()
    {
        // Unsubscribe strictly to prevent managed leaks and MissingReferenceExceptions
        if (playerBridge?.Model != null)
        {
            playerBridge.Model.OnHealthChanged -= HandleHealthChanged;
        }
    }

    private void HandleHealthChanged(int currentHp)
    {
        Debug.Log("UI health updated: " + currentHp);
    }
}
```

### 3.4. Fast Isolated Unit Testing with Test Stubs

Because dependencies are inverted behind interfaces, we can verify the player model using an in-test `StubWeapon` without depending on concrete classes or loading Unity scenes:

```
using NUnit.Framework;

[TestFixture]
public class PragmaticPlayerTests
{
    private class StubWeapon : IWeaponHandler
    {
        public string WeaponName { get; set; } = "StubGun";
        public int DamageToReturn { get; set; } = 30;
        public int CalculateDamage() => DamageToReturn;
    }

    [Test]
    public void PerformAttack_WithStubWeapon_ReturnsConfiguredDamage()
    {
        var stub = new StubWeapon { WeaponName = "Laser", DamageToReturn = 55 };
        var player = new PragmaticPlayer(initialHp: 100, startingWeapon: stub);

        int damage = player.PerformAttack();

        Assert.AreEqual(55, damage);
        Assert.AreEqual("Laser", player.CurrentWeapon.WeaponName);
    }

    [Test]
    public void EquipWeapon_SwappingWeapon_UpdatesDamageImmediately()
    {
        var initialStub = new StubWeapon { DamageToReturn = 10 };
        var upgradedStub = new StubWeapon { WeaponName = "Plasma", DamageToReturn = 99 };
        var player = new PragmaticPlayer(initialHp: 100, startingWeapon: initialStub);

        player.EquipWeapon(upgradedStub);
        int damage = player.PerformAttack();

        Assert.AreEqual(99, damage);
        Assert.AreEqual("Plasma", player.CurrentWeapon.WeaponName);
    }

    [Test]
    public void ReceiveDamage_FatalDamage_TriggersOnDiedEvent()
    {
        var stub = new StubWeapon();
        var player = new PragmaticPlayer(initialHp: 50, startingWeapon: stub);
        bool diedEventFired = false;
        player.OnDied += () => diedEventFired = true;

        player.ReceiveDamage(damage: 80);

        Assert.AreEqual(0, player.CurrentHp);
        Assert.IsTrue(player.IsDead);
        Assert.IsTrue(diedEventFired);
        Assert.AreEqual(0, player.PerformAttack());
    }

    [Test]
    public void ReceiveDamage_NegativeOrZeroDamage_DoesNotChangeHp()
    {
        var stub = new StubWeapon();
        var player = new PragmaticPlayer(initialHp: 100, startingWeapon: stub);

        // Negative damage should not heal the player
        player.ReceiveDamage(damage: -50);
        Assert.AreEqual(100, player.CurrentHp);

        player.ReceiveDamage(damage: 0);
        Assert.AreEqual(100, player.CurrentHp);
    }

    [Test]
    public void ReceiveDamage_WhenAlreadyDead_DoesNotTriggerOnDiedAgain()
    {
        var stub = new StubWeapon();
        var player = new PragmaticPlayer(initialHp: 20, startingWeapon: stub);
        int diedCount = 0;
        player.OnDied += () => diedCount++;

        player.ReceiveDamage(damage: 30); // Shot 1: Fatal
        player.ReceiveDamage(damage: 20); // Shot 2: Post-mortem

        Assert.AreEqual(1, diedCount);
    }
}
```

---

## 4. Long-Term Strategy: Investing in a Reusable Base Framework

The boundaries above solve the problem for a single 2-week prototype.

However, if your studio regularly produces hyper-casual or hybrid-casual prototypes, there is a strategy with vastly higher ROI: **Build a Reusable Base Framework**.

The premise is straightforward: Any feature needed across 10 consecutive games should be written once with high engineering standards:

```
flowchart TD
    subgraph BaseFramework["Shared Base Framework (Built Once, Tested Thoroughly)"]
        FSM["Game State Machine\n(Splash, Menu, Gameplay, Pause, GameOver)"]
        UIStack["Base UI Manager\n(LoadingScreen, Popup, Settings, Shop)"]
        Services["Service Wrappers\n(Ads, IAP, Analytics, Save/Load, Audio)"]
    end

    subgraph ProjectA["Game Prototype A (2 Weeks)"]
        MechA["Core Mechanic A\n(Runner Combat)"]
    end

    subgraph ProjectB["Game Prototype B (2 Weeks)"]
        MechB["Core Mechanic B\n(Tile Puzzle)"]
    end

    BaseFramework --> ProjectA
    BaseFramework --> ProjectB
```

With a solid Base Framework in place:

- Starting a new prototype takes minutes by pulling in the package template.
- 100% of your 2-week deadline is dedicated to the **Core Gameplay Mechanic**, which is what players actually care about and what determines retention.
- All boilerplate work (screen transitions, sound management, monetization hooks) is already solved and battle-tested.

---

## 5. Architectural Trade-offs Matrix

Every architectural decision involves compromises when shipping under severe time constraints:

| Evaluation Metric | Spaghetti Prototype | Full Clean Architecture | Pragmatic Modular Boundaries |
| --- | --- | --- | --- |
| **Time to Prototype** | Fastest (1-3 days) | Very Slow (1-2 weeks just for scaffolding) | Fast (Ships comfortably within 1-2 weeks) |
| **Cost if Project is Killed** | Negligible (Throwaway code) | Very High (Wasted architectural investment) | Low (Only boundary design invested) |
| **Scalability if Game Hits** | Dead end, requires complete rewrite | High, straightforward to expand | High, easily refactor or replace components |
| **Unit Test Coverage** | Near impossible due to scene coupling | Complete, tests across every domain layer | Pragmatic, focuses on critical core math |
| **Call Stack Traceability** | Transparent, directly traced in Call Stack | Complicated across Use Cases and Dispatchers | Requires care when tracing C# Event delegates |
| **Inspector Serialization** | Direct drag-and-drop on all fields | Requires custom wrappers or DI container | Needs MonoBehaviour Bridge for field serialization |
| **Architectural Overhead** | Lowest, accessible to beginners | Very High, requires team-wide discipline | Balanced, balances speed with maintainability |

---

## 6. Practical Takeaways: Surviving a 2-Week Sprint

When racing against the clock, keep these four principles in mind:

1. **Architecture Serves Business, Not Portfolio Aesthetics:**
   If a prototype fails to reach players in time to test market fit, flawless code has zero commercial value. Prioritize shipping a working gameplay loop over architectural perfection.
2. **Encapsulate for Easy Disposal:**
   Design components so that when game designers pivot mechanics, you can delete a script without destabilizing other systems on the GameObject.
3. **Keep UI Subservient to Gameplay:**
   Gameplay should never depend on UI views. Use unidirectional events from gameplay to presentation and always unsubscribe in `OnDisable()` so visual assets can be discarded and replaced cleanly.
4. **Turn Reusable Assets into a Base Framework:**
   The only sustainable way to code both quickly and cleanly under tight deadlines is reusing battle-tested infrastructure. A solid internal foundation is the ultimate competitive advantage for fast-moving game studios.
