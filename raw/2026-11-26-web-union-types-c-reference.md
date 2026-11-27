---
source: "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/union"
title: "Union types (C# reference)"
author: "BillWagner"
date_published: "unknown"
date_clipped: "2026-11-26"
category: ".NET Ecosystem"
source_type: "web"
discovered_via: "https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/union-types"
date_updated: "2026-10-23"
---

# Union types (C# reference)

A *union type* represents a value that can be one of several *case types*. Unions provide implicit conversions from each case type, exhaustive pattern matching, and enhanced nullability tracking. Use the `union` keyword to declare a union type:

```
public union Pet(Cat, Dog, Bird);
```

This declaration creates a `Pet` union with three case types: `Cat`, `Dog`, and `Bird`. You can assign any case type value to a `Pet` variable. The compiler ensures that `switch` expressions cover all case types.

The C# language reference documents the most recently released version of the C# language. It also contains initial documentation for features in public previews for the upcoming language release.

The documentation identifies any feature first introduced in the last three versions of the language or in current public previews.

Tip

To find when a feature was first introduced in C#, consult the article on the [C# language version history](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-version-history).

Declare a union when a value must be exactly one of a fixed set of types and you want the compiler to enforce that every possibility is handled. Common scenarios include:

- **Result-or-error returns**: A method returns either a success value or an error value, and the caller must handle both. A union like `union Result(Success, Error)` makes the set of outcomes explicit.
- **Message or command dispatching**: A system processes a closed set of message types. A union ensures new message types produce compile-time warnings at every `switch` that doesn't handle them yet.
- **Replacing marker interfaces or abstract base classes**: If you use an interface or abstract class solely to group types for pattern matching, a union gives you exhaustiveness checking without requiring inheritance or shared members.

A union differs from other type declarations in important ways:

- Unlike a `class` or `struct`, a union doesn't define new data members. Instead, it composes existing types into a closed set of alternatives.
- Unlike an `interface`, a union is closed—you define the complete list of case types in the declaration, and the compiler uses that list for exhaustiveness checks.
- Unlike a `record`, a union doesn't add equality, cloning, or deconstruction behavior. A union focuses on "which case is it?" rather than "what fields does it have?"

Union types rely on the [UnionAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.unionattribute) and [IUnion](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.iunion) types in the `System.Runtime.CompilerServices` namespace. The .NET 11 runtime includes these types.

## Union declarations

A union declaration specifies a name and a list of case types:

```
public union Pet(Cat, Dog, Bird);
```

*Case types* can be any type that converts to `object`, including classes, structs, interfaces, type parameters, nullable types, and other unions. The following examples show different case type possibilities:

```
public record class Cat(string Name);
public record class Dog(string Name, string Breed);
public record class Bird(string Name);
```

```
public record class None;
public record class Some<T>(T Value);
public union Option<T>(None, Some<T>);
```

```
public union IntOrString(int, string);
```

When a case type is a value type (like `int`), a union declaration boxes the value and stores it as a single `object?` reference. [Custom union types](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/union#custom-union-types) can use a different storage strategy.

A union declaration can include a body with additional members, just like a struct, subject to some restrictions. Union declarations can't include instance fields, auto-properties, or field-like events. You also can't declare public constructors with a single parameter, because the compiler generates those constructors as union creation members. Any constructor you declare must use a `this(...)` initializer to delegate, directly or indirectly, to a generated constructor. The following `Length` union adds a `TotalMeters` property that uses pattern matching to handle every case type, along with an `Add` method that combines two lengths:

```
public record class Meters(double Value);
public record class Feet(double Value);

public union Length(Meters, Feet)
{
    public double TotalMeters => this switch
    {
        Meters m => m.Value,
        Feet f => f.Value * 0.3048,
        _ => throw new InvalidOperationException("The Length has no value."),
    };

    public Length Add(Length other) => new Meters(TotalMeters + other.TotalMeters);
}
```

## Union conversions

An implicit *union conversion* exists from each case type to the union type:

```
static void BasicConversion()
{
    Pet pet = new Dog("Rex", "Labrador");
    Console.WriteLine(pet.Value); // output: Dog { Name = Rex, Breed = Labrador }

    Pet pet2 = new Cat("Whiskers");
    Console.WriteLine(pet2.Value); // output: Cat { Name = Whiskers }
}
```

Union conversions work by calling the corresponding generated constructor. If a user-defined implicit conversion operator exists for the same type, the user-defined operator takes priority over the union conversion. If more than one case type is equally applicable to the source value, the union conversion is ambiguous, and the compiler reports an error. For details on conversion priority, see the [feature specification](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/csharp-15.0/unions).

A union conversion to a nullable union struct (`T?`) also works when `T` is a union type:

```
static void NullableUnionExample()
{
    Pet? maybePet = new Dog("Buddy", "Beagle");
    Pet? noPet = null;

    Console.WriteLine(Describe(maybePet)); // output: Buddy
    Console.WriteLine(Describe(noPet));    // output: no pet

    static string Describe(Pet? pet) => pet switch
    {
        Dog d => d.Name,
        Cat c => c.Name,
        Bird b => b.Name,
        null => "no pet",
    };
}
```

## Union pattern matching

When you use a type or declaration pattern on a union expression, the pattern tests the union's contents, not the union instance. For example, a `Dog` pattern tests whether `Value` is a `Dog`:

```
static void PatternMatching()
{
    Pet pet = new Dog("Rex", "Labrador");

    var name = pet switch
    {
        Dog d => d.Name,
        Cat c => c.Name,
        Bird b => b.Name,
    };
    Console.WriteLine(name); // output: Rex
}
```

The pattern's form determines which value it tests:

| Pattern | Behavior on a union expression |
| --- | --- |
| Type or declaration pattern, such as `Dog` or `Dog dog` | Tests the contents against the specified type. |
| Property or positional pattern with a type, such as `Dog { Breed: "Labrador" }` | Tests the contents against the type, then applies the nested patterns to that case value. |
| Property or positional pattern without a type, such as `{ Name: "Rex" }` | Uses the union instance's properties or `Deconstruct` method. |
| List pattern | Uses the union instance's count and indexing members, not those of its contents. |
| `var` or discard `_` pattern | Captures or matches the incoming union instance without unwrapping it. |
| Constant or relational pattern | Tests the contents. The `null` pattern also handles a null union reference or nullable wrapper. |

For example, define a `Pet` union with a read-only `Name` property that delegates to the contained `Cat` or `Dog`. The type patterns in the property's `switch` expression test the contents:

```
public union Pet(Cat, Dog)
{
    public string Name => this switch
    {
        Cat cat => cat.Name,
        Dog dog => dog.Name,
        null => "",
    };
}
```

The typed pattern `Dog { Breed: "Labrador" }` tests the contents and reads the dog's `Breed`, a property the union doesn't have. The untyped pattern `{ Name: "Rex" }` reads the union's `Name` property instead, so it also matches a cat named Rex:

```
Pet pet = new Dog("Rex", "Labrador");
Console.WriteLine(pet is Dog { Breed: "Labrador" }); // output: True
Console.WriteLine(pet is { Name: "Rex" });           // output: True
pet = new Cat("Rex");
Console.WriteLine(pet is Dog { Breed: "Labrador" }); // output: False
Console.WriteLine(pet is { Name: "Rex" });           // output: True
```

The `not` pattern negates its nested pattern. In `pet is not null`, the nested `null` pattern checks the contents, so `not null` is a useful has-a-value test. In contrast, an empty untyped property pattern, `{ }`, checks the union instance. It always matches a nonnullable struct union, even when `Value` is null:

```
Pet empty = default;
Console.WriteLine(empty is { });       // output: True
Console.WriteLine(empty is not null);  // output: False
if (empty is var captured)
{
    Console.WriteLine(captured.Value is null); // output: True
}
```

Logical patterns preserve these distinctions. In `var pet and not null`, `var pet` captures the incoming union, and `not null` tests whether it has non-null contents. In `not null and var pet`, the `var` pattern still captures the incoming union: `not` doesn't change the value passed to the right-hand pattern. By contrast, in `Dog and { Breed: "Labrador" }`, the type pattern passes the matched `Dog` to the property pattern.

Note

A type pattern must be compatible with at least one case type. For the `Pet` declarations in this article, `pet is Pet` produces compiler error CS8121: none of their case types can match `Pet`. It isn't a runtime test of the union instance. To check for contents, use `pet is not null` or `pet.Value is not null`; to capture the union itself, use a `var` pattern.

In short, type and declaration patterns test the contents. Recursive patterns with a type test the contents too; recursive patterns without a type use the union's own members. These rules are the same in an `is` expression and a `switch` expression.

### Null matching

For struct unions, the `null` pattern checks whether `Value` is null:

```
static void NullHandling()
{
    Pet pet = default;
    var description = pet switch
    {
        Dog d => d.Name,
        Cat c => c.Name,
        Bird b => b.Name,
        null => "no pet",
    };
    Console.WriteLine(description); // output: no pet
    Console.WriteLine(pet.Value is null); // output: True
}
```

For class-based unions, `null` succeeds when either the union reference itself is null or its `Value` property is null:

```
Result<string>? result = null;
if (result is null) { /* true — the reference is null */ }

Result<string> empty = new Result<string>((string?)null);
if (empty is null) { /* true — Value is null */ }
```

For nullable union struct types (`Pet?`), `null` succeeds when the nullable wrapper has no value or when the underlying union's `Value` is null.

## Union exhaustiveness

A `switch` expression is exhaustive over a union's case types when it handles each case type. If nullability analysis also considers the contents non-null, you don't need a discard (`_`) or `var` arm:

```
static void PatternMatching()
{
    Pet pet = new Dog("Rex", "Labrador");

    var name = pet switch
    {
        Dog d => d.Name,
        Cat c => c.Name,
        Bird b => b.Name,
    };
    Console.WriteLine(name); // output: Rex
}
```

To handle null contents, prefer a `null` arm over a `var` or discard (`_`) arm. The `null` pattern states your intent and preserves warnings when you add a new case type without a matching arm. A `var` or discard arm also accepts any new case, so the compiler can't warn you about that missing case.

When the tracked null state of `Value` is "maybe null," the compiler also warns if you omit a `null` arm. For example, `NullablePet` has a nullable case type, so its parameter's contents might be null:

```
public union NullablePet(Cat?, Dog, Bird);

static string DescribeNullableCase(NullablePet pet) => pet switch
{
    Cat cat => cat.Name,
    Dog dog => dog.Name,
    Bird bird => bird.Name,
    null => "no pet",
};
```

Removing the `null` arm from this switch produces warning CS8655.

Nullable analysis doesn't guarantee that a generated union has non-null contents at runtime. A default union contains null, including when it's a default-initialized field or array element. If all case types are nonnullable, the default tracked state of `Value` is nevertheless "not null," so the compiler doesn't necessarily warn about an omitted `null` arm. Handle `null` for correctness whenever default contents can reach your switch:

```
static void NullHandling()
{
    Pet pet = default;
    var description = pet switch
    {
        Dog d => d.Name,
        Cat c => c.Name,
        Bird b => b.Name,
        null => "no pet",
    };
    Console.WriteLine(description); // output: no pet
    Console.WriteLine(pet.Value is null); // output: True
}
```

For this `Pet` example, removing the `null` arm produces no missing-null-arm warning unless earlier code changes the tracked null state, but the switch throws [SwitchExpressionException](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.switchexpressionexception) when it receives the default value. An earlier `is null` test can change the tracked state and cause a warning. This behavior is separate from definite assignment: the compiler rejects a read of an unassigned local variable.

## Nullability

The compiler tracks the null state of a union's `Value` property through the following rules:

- The default null state of a union's `Value` property is "maybe null" if the default null state of any case type is "maybe null." Otherwise, the default null state is "not null."
- When you create a union value from a case type (through a constructor or union conversion), `Value` gets the null state of the incoming value.
- When the non-boxing access pattern's `HasValue` or `TryGetValue(...)` members query the union's contents, the null state of `Value` becomes "not null" on the `true` branch.

## Custom union types

The compiler converts a `union` declaration to a `struct` declaration. The struct is marked with the `[System.Runtime.CompilerServices.Union]` attribute and implements the `IUnion` interface. It includes a public constructor for each case type and a `Value` property. The language provides implicit union conversions that call those constructors. That generated form is opinionated. It's always a struct, always boxes value-type cases, and always stores contents as `object?`.

You might need different behavior if you want to adapt an existing type, create a class-based union, or use a custom storage strategy, or if you need interop support. You can create a union type manually.

Any class or struct with a `[Union]` attribute is a *union type* if it follows the *basic union pattern*. The basic union pattern requires:

- A `[Union]`  attribute on the type.
- One or more public constructors, each with a single by-value or `in` parameter. The parameter type of each constructor defines a *case type*.
- A public `Value` property of type `object?` (or `object`) with a `get` accessor.

All the preceding union members must be public. The compiler uses these members to implement union conversions, pattern matching, and exhaustiveness checks. You can also implement the [non-boxing access pattern](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/union#non-boxing-access-pattern) or create a [class-based union type](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/union#class-based-union-types). Your custom union type can add more members.

The compiler assumes that custom union types satisfy these behavioral rules:

- **Soundness**: `Value` always returns `null` or a value of one of the case types, including for a default struct value. A custom union can represent its default value as a non-null case, unlike the null contents of a default generated union.
- **Stability**: If you create a union value from a case type, `Value` matches that case type (or is `null` if the input was `null`).
- **Creation equivalence**: If a value is implicitly convertible to two different case types, both creation members produce the same observable behavior.
- **Access pattern consistency**: The `HasValue` and `TryGetValue` members, if present, behave equivalently to checking `Value` directly.

The following example shows a custom union type:

```
[System.Runtime.CompilerServices.Union]
public struct Shape : System.Runtime.CompilerServices.IUnion
{
    private readonly object? _value;

    public Shape(Circle value) { _value = value; }
    public Shape(Rectangle value) { _value = value; }

    public object? Value => _value;
}

public record class Circle(double Radius);
public record class Rectangle(double Width, double Height);
```

```
static void ManualUnionExample()
{
    Shape shape = new Shape(new Circle(5.0));

    var area = shape switch
    {
        Circle c => Math.PI * c.Radius * c.Radius,
        Rectangle r => r.Width * r.Height,
    };
    Console.WriteLine($"{area:F2}"); // output: 78.54
}
```

### Non-boxing access pattern

A custom union type can optionally implement the *non-boxing access pattern* to enable strongly typed access to value-type cases without boxing during pattern matching. This pattern requires:

- A `HasValue` property of type `bool` that returns `true` when `Value` isn't `null`.
- A `TryGetValue` method for each case type that returns `bool` and delivers the value through an `out` parameter. `TryGetValue` returns `true` only when `Value` is a non-null value of that case type. The `out` parameter's type is identity-convertible to the case type, or to the underlying value type when the case type is a nullable value type.

```
[System.Runtime.CompilerServices.Union]
public struct IntOrBool : System.Runtime.CompilerServices.IUnion
{
    private readonly int _intValue;
    private readonly bool _boolValue;
    private readonly byte _tag; // 0 = none, 1 = int, 2 = bool

    public IntOrBool(int? value)
    {
        if (value.HasValue)
        {
            _intValue = value.Value;
            _tag = 1;
        }
    }

    public IntOrBool(bool? value)
    {
        if (value.HasValue)
        {
            _boolValue = value.Value;
            _tag = 2;
        }
    }

    public object? Value => _tag switch
    {
        1 => _intValue,
        2 => _boolValue,
        _ => null
    };

    public bool HasValue => _tag != 0;

    public bool TryGetValue(out int value)
    {
        value = _intValue;
        return _tag == 1;
    }

    public bool TryGetValue(out bool value)
    {
        value = _boolValue;
        return _tag == 2;
    }
}
```

```
static void NonBoxingExample()
{
    IntOrBool val = new IntOrBool((int?)42);

    var description = val switch
    {
        int i => $"int: {i}",
        bool b => $"bool: {b}",
    };
    Console.WriteLine(description); // output: int: 42
}
```

For pattern matching, the compiler calls `TryGetValue` for type-pattern checks (such as `union is T`) and `HasValue` for null-pattern checks (such as `union is null`), avoiding boxing for value-type cases. Each member applies to its own pattern kind—neither is a fallback for the other. When a member is missing, the compiler checks the `Value` property for that pattern instead. For more information, see [How the compiler generates code for pattern matching](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/union#union-member-providers).

### Union member providers

A union type can delegate its union members to a public nested `IUnionMembers` interface that it directly contains and implements. That interface is the *union member provider*. The compiler finds union members only on the provider interface, including inherited members. Members declared only on the union type itself aren't used as union members.

When using a union member provider, the interface must declare these required members:

- **Static `Create` methods**: One for each case type, with a single parameter and a return type identity-convertible to the union type. These methods establish your case types.
- **`Value` property**: A public `object` or `object?` property with a `get` accessor that returns the contained value.

You can optionally declare these members on the interface so the compiler generates more efficient pattern matching code:

- **`TryGetValue` methods**: One for each case type, returning `bool` with an `out` parameter of the case type.
- **`HasValue` property**: A public `bool` property with a `get` accessor returning `true` when `Value` isn't `null`.

**How the compiler generates code for pattern matching**: `TryGetValue` and `HasValue` apply to different kinds of patterns—neither is a fallback for the other:

- For a *type pattern*, such as `union is T`, the compiler calls `TryGetValue(out T value)` when declared, extracting the value and applying the pattern to it without boxing. Otherwise, the compiler applies the pattern to the `Value` property, which performs a runtime type check against `T` and can box the value when `T` is a value type.
- For a *null pattern*, such as `union is null`, the compiler calls `HasValue` when declared to test whether the union contains a value. Otherwise, the compiler applies the null pattern to the `Value` property directly.

Each member is independently optional: without `TryGetValue`, type patterns use `Value`; without `HasValue`, null patterns use `Value`. Declaring either member lets the compiler generate more efficient, strongly typed code for that pattern kind:

```
[System.Runtime.CompilerServices.Union]
public struct Outcome<T> : Outcome<T>.IUnionMembers
{
    private readonly object? _value;

    private Outcome(object? value) => _value = value;

    public interface IUnionMembers
    {
        static Outcome<T> Create(T? value) => new(value);
        static Outcome<T> Create(Exception? value) => new(value);
        object? Value { get; }

        // Optional but recommended: TryGetValue enables efficient pattern matching
        bool TryGetValue(out T value);
        bool TryGetValue(out Exception value);
    }

    object? IUnionMembers.Value => _value;

    public bool TryGetValue(out T value)
    {
        if (_value is T t)
        {
            value = t;
            return true;
        }
        value = default!;
        return false;
    }

    public bool TryGetValue(out Exception value)
    {
        if (_value is Exception e)
        {
            value = e;
            return true;
        }
        value = default!;
        return false;
    }
}
```

Union member providers are useful when the union type needs a private constructor or when the creation logic requires a factory pattern, such as with `record class` union types.

### Class-based union types

A class can also be a union type. This type of union is useful when you need reference semantics or inheritance:

```
[System.Runtime.CompilerServices.Union]
public class Result<T> : System.Runtime.CompilerServices.IUnion
{
    private readonly object? _value;

    public Result(T? value) { _value = value; }
    public Result(Exception? value) { _value = value; }

    public object? Value => _value;
}
```

```
static void ClassUnionExample()
{
    Result<string> ok = new Result<string>("success");
    Result<string> err = new Result<string>(new InvalidOperationException("failed"));

    Console.WriteLine(Describe(ok));  // output: OK: success
    Console.WriteLine(Describe(err)); // output: Error: failed

    static string Describe(Result<string> result) => result switch
    {
        string s => $"OK: {s}",
        Exception e => $"Error: {e.Message}",
        null => "null",
    };
}
```

For class-based unions, the `null` pattern matches both a null reference and a null `Value`.

## C# language specification

For more information, see the [Unions](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/csharp-15.0/unions) feature specification.

## See also

- [The C# type system](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/)
- [Pattern matching](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/patterns)
- [Switch expression](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/switch-expression)
- [Value types](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-types)
- [Records](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/record)
