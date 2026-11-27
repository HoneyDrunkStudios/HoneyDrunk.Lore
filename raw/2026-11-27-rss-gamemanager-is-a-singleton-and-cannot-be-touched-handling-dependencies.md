---
source: "https://dev.to/toanlb_dev/gamemanager-is-a-singleton-and-cannot-be-touched-handling-dependencies-for-new-unit-tests-gbk"
title: "GameManager Is a Singleton and Cannot Be Touched: Handling Dependencies for New Unit Tests"
author: "Toàn Lương Bảo"
date_published: "2026-11-27"
date_clipped: "2026-11-27"
category: "Game Development / Unity"
source_type: "rss"
---

# GameManager Is a Singleton and Cannot Be Touched: Handling Dependencies for New Unit Tests

When taking over a live Unity game that has been running in production for several years, a familiar scenario unfolds: almost every script you open contains calls like `GameManager.Instance`, `SoundManager.Instance`, or `DataManager.Instance`.

These global Singletons are scattered across hundreds of files. As features pile up, tweaking a single line of code in one system can silently break unrelated functionality elsewhere, triggering regression bugs.

Eventually, the engineering team agrees that automated unit testing must be integrated into the CI/CD pipeline to safeguard critical gameplay calculations. But the moment we start writing tests, a roadblock appears: core business logic is tightly coupled to `GameManager.Instance` (which inherits from `MonoBehaviour`). To test a simple damage formula or reward calculation, we are forced to instantiate GameObjects, load scenes, and initialize unrelated peripheral systems.

At that moment, the first instinct for many engineers is: *"Should we rewrite the architecture from scratch, remove all Singletons, and replace them with a [Dependency Injection](https://dev.to/en/posts/take-home-test-singleton-vs-di-framework/) framework like VContainer or Zenject?"*

In production reality, no Product Owner or Game Producer will pause live-ops releases for a month just so engineers can clean up code. The game must ship weekly updates on schedule. We need a pragmatic approach: write solid unit tests for new features today, while systematically containing and paying down legacy technical debt without disrupting release velocity.

Below is a practical 3-level dependency handling strategy, selected based on release deadlines and the allowable blast radius within the legacy codebase.

---

## 1. The Core Testing Bottleneck with Singletons

To understand why Singletons resist automated unit testing, let's examine how the C# runtime and Unity Engine operate:

- A clean unit test must be isolated between test cases and execute in memory within a few milliseconds.
- When a method directly calls `GameManager.Instance.PlayerLevel`, that call is hardcoded at the IL level via static binding and conceals a hidden dependency.
- Standard .NET mocking libraries (such as Moq or NSubstitute, which rely on `Castle.DynamicProxy`) cannot mock `GameManager.Instance` for two technical reasons:
  1. `DynamicProxy` works by generating runtime subclasses to intercept calls dispatched via virtual method tables (`interface` methods or `virtual`/`abstract` members). It cannot intercept static property access (`GameManager.Instance`) or non-virtual methods on concrete classes.
  2. Because `GameManager` inherits from `MonoBehaviour`, it cannot be instantiated via `new GameManager()` inside a pure C# unit test runner, as `MonoBehaviour` constructors require binding to a native C++ `GameObject` managed by the Unity Engine.

```
flowchart TD
    subgraph Problem["Bottleneck in Testing with Singletons"]
        Test["Unit Test Runner (CI/CD)"] -->|Calls method under test| Method["CalculateReward()"]
        Method -->|Hardcoded static binding| GM["GameManager.Instance (MonoBehaviour)"]
        GM -->|Native C++ binding| Engine["Unity Scene / GameObject Lifecycle"]
        GM -->|Pulls heavy subsystems| Res["SaveSystem / Audio / Network"]
    end
```

Consequently, testing a small calculation requires bootstrapping an entire PlayMode test scene with active GameObjects in memory, slowing down test execution and causing cascading failures whenever someone modifies `GameManager`.

To remove this bottleneck without halting feature delivery, we divide our approach into three progressive levels.

---

## 2. Level 1: Complete Isolation via Adapter / Wrapper (Zero Touch Legacy)

### When to Apply

This is the safest choice when delivering a feature under a tight sprint deadline, or when team policy dictates: **Do not modify a single line inside `GameManager.cs`** to guarantee zero regression risk for an upcoming build.

### How It Works

Core rule: The new feature (for example, `CombatRewardCalculator`) is forbidden from referencing `GameManager.Instance` inside its domain logic. Instead, the new feature defines a narrow interface for the exact data it needs (`IPlayerStatsProvider`), and we write a thin Adapter class at the boundary (`GameManagerStatsAdapter`) to bridge the two.

```
flowchart LR
    subgraph NewFeature["New Feature (Pure C#)"]
        Logic["CombatRewardCalculator"]
        Interface["IPlayerStatsProvider"]
    end

    subgraph Production["Game Runtime"]
        Adapter["GameManagerStatsAdapter"]
        Legacy["GameManager.Instance"]
    end

    subgraph Testing["Unit Test Runner"]
        Mock["FakePlayerStats"]
    end

    Logic -->|Depends on| Interface
    Adapter -.->|implements| Interface
    Adapter -->|Reads from| Legacy
    Mock -.->|implements| Interface
    Logic -.->|Injected during test| Mock
```

#### Level 1 Code Demo: Wrapping the Singleton with an Adapter

To illustrate this technique in a familiar production scenario, imagine maintaining a live-ops Turn-Based RPG that has been running for three years. The incoming task is to implement a new post-battle reward calculator (`CombatRewardCalculator`) that determines gold and experience bonuses based on player progression levels and stage bounty modifiers.

The core challenge is that legacy player stats are tightly locked inside a monolithic `GameManager.Instance` (`MonoBehaviour`). Furthermore, the new calculation logic must be 100% verified via fast CI/CD unit tests (< 5ms execution) without bootstrapping scenes, while strictly forbidding any destructive refactoring of `GameManager`, which is actively referenced by over 50 gameplay scenes.

The clean solution begins by having the new feature declare only the exact data contract it requires through an interface:

```
using System;

// 1. Narrow interface containing only what the new feature cares about
public interface IPlayerStatsProvider
{
    int CurrentLevel { get; }
    int BaseGold { get; }
}
```

The pure C# business logic receives this interface via constructor injection:

```
using System;

// 2. Pure C# domain logic, 100% independent of UnityEngine
public class CombatRewardCalculator
{
    private readonly IPlayerStatsProvider _statsProvider;

    public CombatRewardCalculator(IPlayerStatsProvider statsProvider)
    {
        _statsProvider = statsProvider ?? throw new ArgumentNullException(nameof(statsProvider));
    }

    public int CalculateGoldReward(int enemyBounty)
    {
        int multiplier = Math.Max(1, _statsProvider.CurrentLevel);
        return (_statsProvider.BaseGold + enemyBounty) * multiplier;
    }
}
```

In the production runtime, a lightweight Adapter acts as an Anti-Corruption Layer around `GameManager.Instance`:

```
// 3. Adapter bridging the new interface to the legacy Singleton
public class GameManagerStatsAdapter : IPlayerStatsProvider
{
    public int CurrentLevel => GameManager.Instance.PlayerLevel;
    public int BaseGold => GameManager.Instance.DefaultGoldBonus;
}
```

#### Writing Unit Tests at Level 1

In our test suite, we pass a simple fake implementation into `CombatRewardCalculator` without touching `GameManager` or loading any Unity Scene:

```
using NUnit.Framework;

[TestFixture]
public class CombatRewardCalculatorTests
{
    private class FakePlayerStats : IPlayerStatsProvider
    {
        public int CurrentLevel { get; set; }
        public int BaseGold { get; set; }
    }

    [Test]
    public void CalculateGoldReward_Level2_ReturnsDoubledReward()
    {
        var fakeStats = new FakePlayerStats { CurrentLevel = 2, BaseGold = 100 };
        var calculator = new CombatRewardCalculator(fakeStats);

        int result = calculator.CalculateGoldReward(enemyBounty: 50);

        // (100 + 50) * 2 = 300
        Assert.AreEqual(300, result);
    }
}
```

### Trade-Off Evaluation

- **Pros:** Zero regression risk to legacy code. We do not edit a single line inside `GameManager`, yet our new business logic has 100% isolated unit test coverage.
- **Cons:** Introduces an extra Adapter class. If dozens of features create ad-hoc Adapters without a long-term consolidation plan, wrapper classes will proliferate. Treat this as a pragmatic containment measure to stop technical debt from spreading into new code.

---

## 3. Level 2: Extracting Capability Interfaces (Minimal Touch on Singleton)

### When to Apply

When developing a medium-sized feature whose data contract will be reused across multiple modules, and the team allows minor, non-breaking signature additions to `GameManager.cs`.

### How It Works

Instead of extracting a monolithic `IGameManager` interface with fifty methods (which violates the Interface Segregation Principle), we define narrow, role-specific capability interfaces.

For example, if our new combat calculation class (`CombatDamageProcessor`) only needs enemy defense stats, we define `IEnemyStatsProvider` and have `GameManager` implement it directly.

```
flowchart TD
    subgraph LegacySingleton["GameManager.cs (Legacy God Class)"]
        GM["GameManager"]
    end

    subgraph Capabilities["Role-Specific Capability Interfaces"]
        IEnemy["IEnemyStatsProvider"]
        IScore["IScoreManager"]
    end

    GM -.->|implements| IEnemy
    GM -.->|implements| IScore

    LegacyCode["Hundreds of legacy scripts"] -->|Still call directly| GM
    NewCombatFeature["CombatDamageProcessor (Pure C#)"] -->|Depends only on| IEnemy
```

#### Level 2 Code Demo: Implementing a Capability Interface

Inside `GameManager.cs`, we append `IEnemyStatsProvider` to the class declaration without altering any existing methods:

```
using System;
using UnityEngine;

public interface IEnemyStatsProvider
{
    int Defense { get; }
    float DamageReductionRate { get; }
}

// GameManager implements the capability interface while keeping all legacy APIs intact
public class GameManager : MonoBehaviour, IEnemyStatsProvider
{
    public static GameManager Instance { get; private set; }

    [SerializeField] private int _enemyDefense = 20;
    [SerializeField] private float _damageReduction = 0.1f;

    public int Defense => _enemyDefense;
    public float DamageReductionRate => _damageReduction;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void OnDestroy()
    {
        if (Instance == this)
        {
            Instance = null;
        }
    }

    // Dozens of existing legacy methods remain untouched...
    public void OldLegacyMethod() { }
}
```

The new damage calculation logic lives inside a pure C# class that depends only on `IEnemyStatsProvider`:

```
using System;

public class CombatDamageProcessor
{
    private readonly IEnemyStatsProvider _statsProvider;

    public CombatDamageProcessor(IEnemyStatsProvider statsProvider)
    {
        _statsProvider = statsProvider ?? throw new ArgumentNullException(nameof(statsProvider));
    }

    public int ComputeDamage(int rawAttack)
    {
        float reducedAttack = rawAttack * (1f - _statsProvider.DamageReductionRate);
        int finalDamage = (int)Math.Round(reducedAttack) - _statsProvider.Defense;
        return Math.Max(1, finalDamage);
    }
}
```

At the Unity Scene layer, our bootstrap script or `MonoBehaviour` simply passes `GameManager.Instance` into `CombatDamageProcessor`:

```
var processor = new CombatDamageProcessor(GameManager.Instance);
int damage = processor.ComputeDamage(100);
```

#### Writing Unit Tests at Level 2

Because `CombatDamageProcessor` is a pure C# class bound only to `IEnemyStatsProvider`, unit tests execute directly in memory without touching `GameManager`:

```
using NUnit.Framework;

[TestFixture]
public class CombatDamageProcessorTests
{
    private class StubEnemyStats : IEnemyStatsProvider
    {
        public int Defense { get; set; }
        public float DamageReductionRate { get; set; }
    }

    [Test]
    public void ComputeDamage_AppliesReductionAndDefense_ReturnsExpectedDamage()
    {
        var stubStats = new StubEnemyStats
        {
            Defense = 20,
            DamageReductionRate = 0.1f
        };
        var processor = new CombatDamageProcessor(stubStats);

        // 100 * (1 - 0.1) - 20 = 90 - 20 = 70
        int damage = processor.ComputeDamage(rawAttack: 100);

        Assert.AreEqual(70, damage);
    }
}
```

### Trade-Off Evaluation

- **Pros:** Legacy scripts continue calling `GameManager.Instance` unchanged. New features depend on clean interfaces without requiring extra Adapter classes.
- **Cons:** `GameManager.cs` itself remains a God Class. If every feature attaches another interface onto `GameManager`, it may end up implementing fifteen interfaces over time. This is an effective stepping stone, but it does not shrink the internal responsibilities of `GameManager`.

---

## 4. Level 3: Extracting Pure C# Services and Turning GameManager into a Facade

### When to Apply

When working on core domain systems (such as scoring, inventory, or progression) or during stabilization sprints where the team can actively pay down technical debt.

### How It Works

Rather than deleting `GameManager.Instance` (which would break hundreds of existing scripts), we hollow out its internal logic into dedicated pure C# services and turn `GameManager` into a thin **Facade Coordinator**:

1. Extract cohesive state fields and domain methods out of `GameManager` into standalone pure C# classes (`ScoreService`, `InventoryService`).
2. Cover these pure C# services thoroughly with fast unit tests.
3. Have `GameManager` hold instances of these services and delegate calls to them.
4. Keep existing `GameManager.Instance.AddScore(10)` methods as one-line forwarding calls so all legacy scripts remain 100% compatible.

```
flowchart TD
    subgraph FacadePattern["GameManager as a Thin Facade Coordinator"]
        GM["GameManager.Instance (MonoBehaviour)"]
    end

    subgraph PureServices["Pure C# Domain Services (100% Unit Testable)"]
        ScoreSvc["ScoreService (Pure C#)"]
        InventorySvc["InventoryService (Pure C#)"]
        StatsSvc["PlayerStatsService (Pure C#)"]
    end

    GM -->|Owns and delegates to| ScoreSvc
    GM -->|Owns and delegates to| InventorySvc
    GM -->|Owns and delegates to| StatsSvc

    LegacyCode["Existing legacy scripts"] -->|"Calls GameManager.Instance.AddScore()"| GM
    NewCode["New features"] -->|Injected directly| ScoreSvc
```

#### Level 3 Code Demo: Extracting Services Safely Around Awake() Order

A common production trap when extracting fields out of a legacy [Singleton](https://dev.to/en/posts/why-large-projects-avoid-singleton/) into sub-services involves Unity's `Awake()` execution order. In legacy projects, many scripts call `GameManager.Instance.AddScore()` or query state right inside their own `Awake()` or `OnEnable()` callbacks.

If we initialize `_scoreService = new ScoreService()` exclusively inside `GameManager.Awake()`, and Unity happens to execute another script's `Awake()` before `GameManager.Awake()`, `_scoreService` will still be `null` and throw an immediate `NullReferenceException`. To prevent this regression, use **lazy initialization** (`??=`) on the service property so it is guaranteed to exist regardless of script execution order:

```
using System;
using UnityEngine;

// 1. Standalone pure C# service responsible solely for score rules
public class ScoreService
{
    public int CurrentScore { get; private set; }

    // Note: Scene MonoBehaviours subscribing to this event must unsubscribe (-=) in OnDestroy()
    public event Action<int> OnScoreChanged;

    public void AddScore(int amount)
    {
        if (amount <= 0) return;
        CurrentScore += amount;
        OnScoreChanged?.Invoke(CurrentScore);
    }

    public void Reset()
    {
        CurrentScore = 0;
        OnScoreChanged?.Invoke(CurrentScore);
    }
}

// 2. GameManager acts as a Facade preserving backward compatibility for legacy callers
public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }

    private ScoreService _scoreService;

    // Lazy initialization protects against legacy scripts calling into GameManager before its Awake() runs
    public ScoreService ScoreService => _scoreService ??= new ScoreService();

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            _scoreService ??= new ScoreService();
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void OnDestroy()
    {
        if (Instance == this)
        {
            Instance = null;
        }
    }

    // Backward-compatible forwarding APIs for hundreds of legacy scripts:
    public void AddScore(int amount) => ScoreService.AddScore(amount);
    public int GetCurrentScore() => ScoreService.CurrentScore;
}
```

#### Writing Unit Tests at Level 3

All scoring rules and event notifications inside `ScoreService` can now be tested directly with NUnit:

```
using NUnit.Framework;

[TestFixture]
public class ScoreServiceTests
{
    [Test]
    public void AddScore_PositiveAmount_UpdatesScoreAndFiresEvent()
    {
        var service = new ScoreService();
        int notifiedScore = -1;
        service.OnScoreChanged += score => notifiedScore = score;

        service.AddScore(50);
        service.AddScore(25);

        Assert.AreEqual(75, service.CurrentScore);
        Assert.AreEqual(75, notifiedScore);
    }

    [Test]
    public void AddScore_NonPositiveAmount_IgnoresAndDoesNotFireEvent()
    {
        var service = new ScoreService();
        bool eventFired = false;
        service.OnScoreChanged += _ => eventFired = true;

        service.AddScore(0);
        service.AddScore(-10);

        Assert.AreEqual(0, service.CurrentScore);
        Assert.IsFalse(eventFired);
    }
}
```

### Trade-Off Evaluation

- **Pros:** The cleanest long-term architectural path. Core domain logic moves out of `MonoBehaviour` into fast, testable pure C# classes while maintaining full backward compatibility for existing callers.
- **Cons:** Requires careful attention to initialization order and event lifecycles. For in-memory domain services like `ScoreService`, injecting the concrete class directly keeps tests simple; if a service performs external I/O (such as disk persistence or network requests), extract an `IScoreService` interface so downstream consumers can mock it easily.

---

## 5. Trade-Off Comparison Across All 3 Levels

Choosing the right level depends on your current sprint constraints and risk tolerance:

| Criteria | Level 1: Adapter / Wrapper | Level 2: Capability Interface | Level 3: Service Facade |
| --- | --- | --- | --- |
| Impact on Legacy Singleton | Zero lines changed | Minor interface declaration added | Internal logic extracted into sub-services |
| Unit Testability | Good for new feature logic | Great for new feature logic | Covers both legacy rules and new features |
| Implementation Speed | Very fast (a few hours) | Fast (half a day) | Requires careful data-flow planning |
| Regression Risk | Zero | Very low | Must guard initialization order and run regression tests |
| Technical Debt Reduction | Temporary containment | Moderate decoupling | High (gradually hollows out the God Class) |
| Best Suited For | Tight deadlines, urgent hotfixes | New features reading shared state | Touching core systems or refactoring sprints |

---

## 6. Pragmatic Rollout: Applying the Boy Scout Rule

When inheriting a multi-year Unity project filled with Singletons, avoid opening a massive pull request that touches hundreds of files to eradicate Singletons overnight. That approach almost always leads to severe merge conflicts, missed deadlines, and new regressions.

Instead, apply the **Boy Scout Rule** incrementally:

> *"Always leave the code you touch cleaner than you found it."*

- **When building a new feature:** Stop adding new `.Instance` calls inside business logic. Use Level 1 or Level 2 to isolate and unit-test your new code.
- **When fixing a bug inside `GameManager`:** Extract the buggy calculation into a pure C# service using Level 3, write a unit test reproducing the bug, fix it, and have `GameManager` forward the call.
- **Over consecutive sprints:** Heavy domain logic inside `GameManager` steadily drains into tested pure C# services, transforming a rigid legacy codebase into a modular architecture without stalling a single release.
