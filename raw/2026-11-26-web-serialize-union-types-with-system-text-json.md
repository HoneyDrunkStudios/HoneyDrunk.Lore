---
source: "https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/union-types"
title: "Serialize union types with System.Text.Json"
author: "gewarren"
date_published: "unknown"
date_clipped: "2026-11-26"
category: ".NET Ecosystem"
source_type: "web"
discovered_via: "https://devblogs.microsoft.com/dotnet/announcing-dotnet-11/"
date_updated: "2026-09-29"
---

# Serialize union types with System.Text.Json

Starting in .NET 11, [JsonSerializer](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializer) supports [C# 15 union types](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/union). A union holds one of the case types in its declaration. `JsonSerializer` writes the active case value and can read it back.

## Serialize and deserialize union values

Declare a union whose cases have distinct JSON token types:

```
public union Payload(int, string, Message);
public sealed record Message(string Text);
```

Use `JsonSerializer` to serialize and deserialize the union:

```
Payload payload = new Message("Ready");
string json = JsonSerializer.Serialize(payload);
Payload copy = JsonSerializer.Deserialize<Payload>(json);
```

The serialized JSON contains the active case value rather than a wrapper or discriminator:

```
{"Text":"Ready"}
```

By default, the serializer classifies incoming JSON by token type. In the preceding union, a JSON number selects `int`, a JSON string selects `string`, and a JSON object selects `Message`.

With [JsonSerializerOptions.Web](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializeroptions.web#system-text-json-jsonserializeroptions-web), an `int` can also be read from a JSON string. Both the `int` and `string` cases of `Payload` then claim the string token type. Even `"25%"` throws [JsonException](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonexception) for ambiguity before the serializer parses either case. To read strings with web defaults, [provide a custom classifier](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/union-types#provide-a-custom-classifier) that chooses the case.

## Distinguish cases with the same JSON token type

Token classification can't distinguish two cases that both serialize as JSON objects. Apply [JsonUnionAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonunionattribute) and select [JsonUnionTypeStructuralClassifier](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonuniontypestructuralclassifier) to classify object cases by their property names:

```
[JsonUnion(TypeClassifier = typeof(JsonUnionTypeStructuralClassifier))]
public union Pet(Dog, Cat);
public sealed record Dog(string Name, string Breed);
public sealed record Cat(string Name, int Lives);
```

Here, `JsonUnionAttribute` selects a classifier for the existing `Pet` union; applying it to an ordinary type doesn't turn that type into a union.

The classifier selects `Dog` when the payload contains `Breed` and selects `Cat` when it contains `Lives`:

```
Pet pet = JsonSerializer.Deserialize<Pet>(
    """{"Name":"Rex","Breed":"Husky"}""");
```

For JSON objects, the structural classifier starts with the compatible object cases and narrows that set as it reads recognized root-level property names. Required properties remove cases when they're absent. [JsonUnmappedMemberHandling.Disallow](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonunmappedmemberhandling#system-text-json-serialization-jsonunmappedmemberhandling-disallow) removes a case when the payload contains a property that the case doesn't declare. Classification succeeds only when one case remains.

The structural classifier doesn't inspect property values, nested objects, string contents, or array elements. Keep these consequences in mind:

- A payload that leaves zero or multiple candidates throws [JsonException](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonexception).
- Overlapping or shadowed object contracts might be rejected when the classifier is created.
- Multiple non-object cases that use the same JSON token type aren't supported. For example, `Guid` and `string` both use JSON strings.
- A plain object case can't be mixed with a dictionary, `JsonObject`, or another non-POCO object-shaped case.
- Nested union cases and polymorphic cases aren't supported.
- [ReferenceHandler.Preserve](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.referencehandler.preserve#system-text-json-serialization-referencehandler-preserve) isn't supported.
- A configuration that can't distinguish its cases throws [NotSupportedException](https://learn.microsoft.com/en-us/dotnet/api/system.notsupportedexception) when the serializer builds the classifier.

## Choose unions or closed hierarchies

Use a union when you need to preserve a discriminator-free JSON format you don't control, or when the cases have distinct JSON shapes. For example, the `int` and `string` cases of `Payload` are distinguishable by JSON token type. For object cases such as `Pet(Dog, Cat)`, however, changes to property names can affect which case a structural classifier selects.

When you control the types and JSON contract, a [closed hierarchy with inferred polymorphism](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/polymorphism#infer-polymorphism-from-a-closed-hierarchy) can identify object cases with a discriminator instead:

```
[JsonPolymorphic(InferClosedTypePolymorphism = true)]
public closed record Event;
public sealed record Created(int Id) : Event;
public sealed record Deleted(int Id) : Event;
```

`JsonSerializer.Serialize<Event>(new Created(42))` writes `{"$type":"Created","Id":42}`. Both derived types declare `Id`, but the discriminator identifies the case independently of its properties. This makes case selection more stable as the properties evolve. Unlike union cases, the derived types must share a base class, and you must opt in to inferred polymorphism; the `closed` modifier alone doesn't add a discriminator.

## Provide a custom classifier

Derive from [JsonTypeClassifierFactory](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsontypeclassifierfactory) when default token classification or the built-in [JsonUnionTypeStructuralClassifier](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonuniontypestructuralclassifier) doesn't meet your requirements. A custom classifier can use other structural rules to select a union case. Register the factory in one of these locations:

- Assign a delegate to [JsonTypeInfo.TypeClassifier](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsontypeinfo.typeclassifier#system-text-json-serialization-metadata-jsontypeinfo-typeclassifier) when you customize the contract.
- Set [JsonUnionAttribute.TypeClassifier](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonunionattribute.typeclassifier#system-text-json-serialization-jsonunionattribute-typeclassifier) for one union.
- Add the factory to [JsonSerializerOptions.TypeClassifiers](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializeroptions.typeclassifiers#system-text-json-jsonserializeroptions-typeclassifiers) for reflection-based serialization.
- Set [JsonSourceGenerationOptionsAttribute.TypeClassifiers](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonsourcegenerationoptionsattribute.typeclassifiers#system-text-json-serialization-jsonsourcegenerationoptionsattribute-typeclassifiers) for a source-generation context.

A classifier reads the current JSON value and returns one of the case types from [JsonTypeClassifierContext.UnionCases](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsontypeclassifiercontext.unioncases#system-text-json-serialization-jsontypeclassifiercontext-unioncases). The serializer checks the contract delegate first, followed by the per-union factory, the options-level factories, and built-in token classification.

For ambiguous unions, the source generator reports a diagnostic unless a classifier is configured at generation time.

## Handle null and default union values

A union can declare nullable case types. JSON `null` selects the first nullable case. If the union has no nullable case, JSON `null` produces the default union value. For a compiler-generated struct union, the default value has no active case and serializes as JSON `null`.

## Customize a union contract

For advanced scenarios, customize the union metadata through [JsonTypeInfo](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsontypeinfo). A union's [JsonTypeInfo.Kind](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsontypeinfo.kind#system-text-json-serialization-metadata-jsontypeinfo-kind) value is [JsonTypeInfoKind.Union](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsontypeinfokind#system-text-json-serialization-metadata-jsontypeinfokind-union). Its contract exposes:

- [JsonTypeInfo.UnionCases](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsontypeinfo.unioncases#system-text-json-serialization-metadata-jsontypeinfo-unioncases), which contains [JsonUnionCaseInfo](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsonunioncaseinfo) entries.
- [JsonTypeInfo.UnionConstructor](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsontypeinfo.unionconstructor#system-text-json-serialization-metadata-jsontypeinfo-unionconstructor), which creates a union from a case type and value.
- [JsonTypeInfo.UnionDeconstructor](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsontypeinfo.uniondeconstructor#system-text-json-serialization-metadata-jsontypeinfo-uniondeconstructor), which returns the active case type and value.
- [JsonTypeInfo.TypeClassifier](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsontypeinfo.typeclassifier#system-text-json-serialization-metadata-jsontypeinfo-typeclassifier), which selects a case during deserialization.

For more information about modifying `JsonTypeInfo`, see [Customize a JSON contract](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/custom-contracts).

## See also

- [Union types (C# reference)](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/union)
- [Serialize polymorphic types](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/polymorphism)
- [Use source generation](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/source-generation)
- [Use C# unions and closed hierarchies in ASP.NET Core (.NET Blog)](https://devblogs.microsoft.com/dotnet/unions-and-closed-hierarchies-in-aspnetcore/)
