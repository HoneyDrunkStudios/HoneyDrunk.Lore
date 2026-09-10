---
source: "https://devblogs.microsoft.com/dotnet/unions-and-closed-hierarchies-in-aspnetcore/"
title: "Use C# unions and closed hierarchies in ASP.NET Core"
author: "Dmitrii Korolev"
date_published: "2026-09-10"
date_clipped: "2026-09-10"
category: ".NET Ecosystem"
source_type: "rss"
---

# Use C# unions and closed hierarchies in ASP.NET Core

Source: https://devblogs.microsoft.com/dotnet/unions-and-closed-hierarchies-in-aspnetcore/

Sometimes an API contract says that a value can have more than one JSON type. Kubernetes has a practical example: maxUnavailable can be an absolute number, such as 2 , or a percentage, such as "25%" . Imagine an ASP.NET Core endpoint that exposes the same contract:
public union IntOrString(int, string);
app.MapGet("/deployments/{name}/max-unavailable", IntOrString (string name) => Deployments.GetMaxUnavailable(name));
Depending on the deployment, the response is either 2 or "25%" .
IntOrString uses the native union declaration introduced in C# 15 and .NET 11. A union is one named type that represents a value from a fixed list of case types. This union accepts an int or a string , but not a bool , a DateTime , or anything else. Union cases aren’t limited to classes in one hierarchy; they can include primitives, classes, interfaces, and nullable types.
Each case converts to the union directly without any casting:
IntOrString absolute = 2;
IntOrString percentage = "25%";
It is also quite natural to use a switch statement or expression to handle the active case. Normal C# pattern matching works:
static string Describe(IntOrString value) => value switch
{
int count => $"{count} pods",
string percentage => percentage,
};
Notice that there is no fallback arm such as _ => ... . The compiler knows every permitted case, so it checks that the switch handles them all. If another case is added to IntOrString , existing switches that don’t handle it produce a warning.
For example, suppose a string case is added to a union that previously contained only bool and decimal , but its formatter isn’t updated:
public union SettingValue(bool, decimal, string);
static string Describe(SettingValue value) => value switch
{
bool enabled => enabled ? "enabled" : "disabled",
decimal number => number.ToString(),
// missing string case
};
The compiler identifies the missing case:
warning CS8509: The switch expression does not handle all possible values of its input type (it is not exhaustive). For example, the pattern 'string' is not covered.
This feedback appears wherever the union is handled, so adding a case can’t silently leave an existing switch incomplete. That’s one of the main benefits of using a union instead of object or an open hierarchy.
Before native unions, developers usually reached for object , a shared base type, or a custom wrapper. object accepts too much, and a base type can’t group unrelated existing types such as int and string . A custom wrapper can enforce the set, but it also needs its own construction and matching APIs. A native union keeps the contract in the method signature, works with regular C# patterns, and has built-in support in System.Text.Json (STJ).
Other ways to model alternatives
Before choosing a union, it helps to separate it from two related features.
Polymorphism
Regular C# polymorphism models related types through inheritance. For example, Circle and Square can derive from a common Shape base class and share its members and behavior.
STJ has been able to serialize such a hierarchy with a discriminator. Mark the base type with [JsonPolymorphic] and register each supported derived type with [JsonDerivedType] . The resulting JSON identifies the active type explicitly (see $type entry in the JSON):
{"$type":"circle","radius":5}
STJ always works from that explicitly registered set; it doesn’t automatically include every type that might derive from the base in the future. If the C# base class remains open, the language doesn’t enforce the same set and a switch over it needs a fallback case.
Closed hierarchies
C# 15 adds support for closed class hierarchies . Adding the closed keyword to a base class prevents other assemblies from deriving directly from it. The compiler can then treat its known derived types as a complete list and check a switch for exhaustiveness:
public closed record class PaymentEvent(string PaymentId);
public sealed record class PaymentInitiated(string PaymentId) : PaymentEvent(PaymentId);
public sealed record class PaymentAuthorized(string PaymentId, decimal Amount) : PaymentEvent(PaymentId);
public sealed record class PaymentFailed(string PaymentId, string Reason) : PaymentEvent(PaymentId);
A closed hierarchy is union-like because it represents a known set of alternatives. In C#, however, it is still an inheritance hierarchy: its cases derive from a base class and can share members and behavior. When you control the hierarchy, closed enforces the fixed set in the language and lets STJ infer the derived types instead of registering each one explicitly.
The closed modifier affects the C# type relationship; it doesn’t change JSON by itself. The serialization section below shows the default behavior first, followed by the opt-in polymorphic behavior.
Choosing a model for your API
A union isn’t always the best choice whenever an API has several possible shapes. Start with whether you control the case types and the JSON contract.
When you are designing a new API and all alternatives are classes you control, prefer a closed hierarchy with a JSON discriminator. For example, PaymentInitiated , PaymentAuthorized , and PaymentFailed can derive from PaymentEvent . The discriminator makes the JSON self-describing, while closed lets the compiler check that every known event is handled.
Keep the base class open only when the model must remain extensible, such as an existing hierarchy designed for other assemblies to extend. STJ still requires every supported derived type to be registered explicitly, and callers need a fallback because the compiler can’t consider an open hierarchy exhaustive.
Choose a union when you must preserve an established discriminator-free contract, or when the cases can’t derive from one base class. This includes primitives and existing types you don’t control. A union preserves each case’s existing JSON shape and still gives callers a fixed set of types to handle.
That discriminator-free format is both a benefit and a tradeoff. Writing the active union case is straightforward. When reading, two cases can look the same in JSON and require explicit classification. For a new polymorphic contract you control, a closed hierarchy with a discriminator avoids that ambiguity.
Also consider how the contract will evolve. Adding a union case or a derived type to a closed hierarchy can produce warnings in existing exhaustive switches, immediately showing callers what they need to handle. An open hierarchy avoids that coupling by requiring a fallback from the start.
Closed-hierarchy serialization uses the same STJ polymorphism infrastructure described above. The closed modifier adds language-level guardrails, and InferClosedTypePolymorphism lets STJ discover the derived types from those guardrails.
ASP.NET Core union support comes from STJ. Unions therefore work where ASP.NET Core uses STJ: JSON request and response bodies, SignalR ‘s JsonHubProtocol , and Blazor ‘s JavaScript interop, persisted component state, and prerendered component parameters. They aren’t supported for query strings, route values, headers, or form fields. For more information, see Limitations .
Serializing and deserializing unions
A union type is declared with the union keyword and a list of case types. The examples throughout this article use the following declarations:
public union UnionIntString(int, string);
public union UnionBoolString(bool, string);
public union UnionNullableIntString(int?, string);
public record Cat(string Name, string Coat);
public record Dog(string Name, string Breed);
public union UnionPet(Cat, Dog);
STJ serializes a union value as its active case, with nothing added to represent the union itself. The union wrapper is unpacked and only the active case is written, using that case’s own JSON contract. There’s no envelope object, no $type field, and no discriminator of any kind:
JsonSerializer.Serialize(new UnionIntString(42)); // 42
JsonSerializer.Serialize(new UnionIntString("hello")); // "hello"
JsonSerializer.Serialize(new UnionPet(new Cat("Whiskers", "Tabby"))); // { "name": "Whiskers", "coat": "Tabby" }
STJ can select a union case automatically when the cases use different JSON types. For example, UnionBoolString(bool, string) is unambiguous because a JSON boolean maps to bool and a JSON string maps to string .
When multiple cases could match the same JSON value, STJ needs help choosing one. UnionPet(Cat, Dog) is ambiguous because both cases are JSON objects. If the payload follows an established discriminator-free contract that can’t be changed, the built-in structural classifier can distinguish object cases by their property names:
[JsonUnion(TypeClassifier = typeof(JsonUnionTypeStructuralClassifier))]
public union UnionPet(Cat, Dog);
Structural classification tradeoffs
The structural classifier must scan the JSON object before STJ can deserialize it, so classification adds work proportional to the payload size. Its decision depends on the case property names, which means changing those shapes can change how existing payloads are classified or make them ambiguous. Prefer a closed hierarchy with a discriminator for new contracts you control.
If the cases can’t be distinguished by structure, an advanced scenario can supply a custom JsonTypeClassifier .
The opening IntOrString endpoint is an output example. When that union is used as an HTTP request body, the web JSON settings also allow numbers to be read from strings, so a JSON string could match either case. Deserializing that contract requires explicit custom classification.
For an overview of STJ’s union support and classifier APIs, see What’s new in .NET libraries for .NET 11 .
Serializing and deserializing closed hierarchies
The closed modifier doesn’t require polymorphic serialization. When code uses a concrete derived type, STJ serializes and deserializes it like any other type and doesn’t add a discriminator:
var json = JsonSerializer.Serialize(new PaymentAuthorized("p-123", 42.5m), JsonSerializerOptions.Web);
var payment = JsonSerializer.Deserialize<PaymentAuthorized>(json, JsonSerializerOptions.Web);
{"paymentId":"p-123","amount":42.5}
This round trip works because both the writer and reader use the concrete PaymentAuthorized type. If an API instead uses the PaymentEvent base type, the JSON needs to identify which derived type to create. Polymorphic serialization can be enabled on the closed base type:
[JsonPolymorphic(InferClosedTypePolymorphism = true)]
public closed record class PaymentEvent(string PaymentId);
STJ then infers the derived types in the closed hierarchy and uses their type names as discriminators. An endpoint can deserialize a PaymentEvent request and serialize the active derived type back:
app.MapPost("/payment-event", (PaymentEvent paymentEvent) => paymentEvent);
This JSON is deserialized as PaymentAuthorized and serialized with the same discriminator:
{"$type":"PaymentAuthorized","paymentId":"p-123","amount":42.5}
The opt-in can instead be applied to a JSON pipeline with JsonSerializerOptions.InferClosedTypePolymorphism . The following sections use unions in their examples, but configured closed hierarchies flow through the same STJ-backed Minimal API, MVC, SignalR, and Blazor paths.
Minimal APIs
Unions work as request body parameters and as return types in both the runtime path ( RequestDelegateFactory ) and the source-generated Request Delegate Generator (RDG) . Behavior is identical across both.
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
// Request body: UnionBoolString is unambiguous (bool vs string), so it binds without a classifier.
app.MapPost("/flag", (UnionBoolString flag) => flag);
// Request body: UnionPet's cases are both objects, so it uses the built-in classifier shown earlier.
app.MapPost("/pet", ([FromBody] UnionPet pet) => TypedResults.Ok(pet));
// Return types: only the active case is serialized, and no classifier is needed to write.
app.MapGet("/value", () => new UnionIntString(42));
app.MapGet("/pet", () => new UnionPet(new Cat("Whiskers", "Tabby")));
app.Run();
Unions compose with the usual Minimal API return types. For example, a union can be returned asynchronously, wrapped in a nullable, or handed back through TypedResults :
app.MapGet("/maybe", () => new UnionNullableIntString((int?)null));
app.MapGet("/typed", () => TypedResults.Ok(new UnionPet(new Cat("Whiskers", "Tabby"))));
A union can also be a property of another model, an item streamed from an IAsyncEnumerable<T> , or the body slot of an [AsParameters] container. Union serialization also respects options configured through ConfigureHttpJsonOptions .
MVC controllers
Unions flow through the STJ input and output formatters, so controllers support them as action parameters and return types, including Task<TUnion> and ValueTask<TUnion> results:
[ApiController]
[Route("[controller]/[action]")]
[Produces("application/json")]
public class PetsController : ControllerBase
{
[HttpPost]
public UnionBoolString Echo([FromBody] UnionBoolString value) => value;
[HttpGet("{kind}")]
public UnionIntString Primitive(string kind) => kind switch
{
"value" => new UnionIntString(42),
_ => new UnionIntString("hi"),
};
}
Union serialization and deserialization follow the rules described earlier . Controllers use JsonSerializerDefaults.Web just like Minimal APIs, so the IntOrString input caveat in that section applies to controller actions too.
SignalR
JsonHubProtocol forwards reads and writes to System.Text.Json , so unions work as hub method parameters, return values, and stream items without any extra configuration:
public class ChatHub : Hub
{
// Union argument (client → server).
public Task Send(UnionIntString message) => Clients.All.SendAsync("Receive", message);
// Union return value (server → client).
public UnionPet GetPet() => new UnionPet(new Cat("Whiskers", "Tabby"));
// Union stream items (server → client).
public async IAsyncEnumerable<UnionIntString> Stream()
{
yield return 1;
yield return "two";
}
}
On the read path, the parameter, return, or stream-item Type resolved from the invocation binder drives the union converter, including any [JsonUnion] classifier.
Unlike HTTP JSON binding in Minimal APIs and MVC, JsonHubProtocol doesn’t treat a JSON String token as ambiguous for numeric cases, so a union such as UnionIntString(int, string) round-trips both the int and string cases without a classifier. Unions whose cases share the StartObject token, such as UnionPet(Cat, Dog) , are still ambiguous on read and require a classifier.
Unions are supported only with JsonHubProtocol . The MessagePack and Newtonsoft.Json hub protocols don’t support unions, because their underlying serializers have no union support.
Blazor
Blazor works with unions in two ways, depending on whether a value stays in-process or crosses a serialization boundary. In-process component parameters are assigned directly and need no serialization, while JavaScript interop, persisted component state, and prerendered parameters serialize unions with System.Text.Json and follow the same rules described earlier in this article.
Component parameters
A component parameter is set by direct assignment when a component is rendered from Razor markup or through RenderTreeBuilder.AddComponentParameter . In-process rendering doesn’t serialize parameters, so a union parameter works with no extra configuration:
<PetCard Pet="@(new UnionPet(new Cat("Whiskers", "Tabby")))" />
public class PetCard : ComponentBase
{
[Parameter]
public UnionPet Pet { get; set; }
}
JavaScript interop
JavaScript interop through IJSRuntime serializes arguments and return values with System.Text.Json . This is useful when a JavaScript API already accepts a union-shaped contract. For example, Element.scrollIntoView accepts either a Boolean alignment shorthand or an options object:
public sealed record ScrollIntoViewOptions(string Behavior, string Block, string Inline);
public union ScrollIntoViewArgument(bool, ScrollIntoViewOptions);
private ValueTask ScrollAsync(
ElementReference element,
ScrollIntoViewArgument argument) =>
JS.InvokeVoidAsync("scrollElementIntoView", element, argument);
await ScrollAsync(target, false);
await ScrollAsync(target, new ScrollIntoViewOptions("instant", "start", "nearest"));
window.scrollElementIntoView = (element, argument) =>
element.scrollIntoView(argument);
The active union case is serialized using the representation expected by JavaScript: either a JSON Boolean or an options object. No union envelope or discriminator is added.
Persisted component state
PersistentComponentState serializes state with System.Text.Json , so a union round-trips through PersistAsJson and TryTakeFromJson , including a union whose active case is null .
Prerendering
When a component is prerendered with Blazor Server or Blazor WebAssembly, its parameters are serialized into the component marker with System.Text.Json and deserialized when the component initializes on the client. Unions are supported across this boundary, including a union whose active case serializes to JSON null , such as a UnionNullableIntString that holds a null int? .
OpenAPI
The OpenAPI document represents a union as an anyOf schema, with one entry per case type:
"Cat": {
"type": "object",
"properties": {
"name": { "type": "string" },
"coat": { "type": "string" }
}
},
"Dog": {
"type": "object",
"properties": {
"name": { "type": "string" },
"breed": { "type": "string" }
}
},
"UnionIntString": {
"anyOf": [
{ "type": "integer", "format": "int32" },
{ "type": "string" }
]
},
"UnionPet": {
"type": "object",
"anyOf": [
{ "$ref": "#/components/schemas/Cat" },
{ "$ref": "#/components/schemas/Dog" }
]
}
Because a union case has no discriminator and is structurally identical to the standalone type, each case schema reuses the standalone component name. The Cat and Dog schemas referenced by UnionPet are the same components that a standalone Cat or Dog endpoint produces. This differs from polymorphic types, whose derived schemas are lifted to prefixed component names because they carry a $type discriminator.
An endpoint can also produce multiple response types for the same status code and content type. The Microsoft.AspNetCore.Mvc.ApiExplorer namespace preserves every declared response type, and the generated document emits an anyOf schema when several types share a content type:
public record Tyrannosaurus(string Name, double BiteForceNewtons);
public record Triceratops(string Name, int HornCount);
public record Velociraptor(string Name, double TopSpeedKmh);
public union UnionDinosaur(Tyrannosaurus, Triceratops, Velociraptor);
app.MapGet("/any-of", () => Results.Ok())
.Produces<UnionPet>(StatusCodes.Status200OK, "application/json")
.Produces<UnionDinosaur>(StatusCodes.Status200OK, "application/json");
The same support applies to MVC controllers that declare multiple ProducesResponseTypeAttribute attributes for one status code and content type.
Limitations
Union support requires System.Text.Json . Binding sources that don’t route through STJ don’t support unions:
Query string values
Route values
Header values
Form fields
These sources bind a string token to a target type without JSON parsing, so there’s no reliable way to choose a union case. A single query value such as ?id=42 provides no way to know whether to bind int , string , Guid , or another case. Because of this ambiguity, unions are intentionally not supported in these binding sources.
In Blazor, the same limitation applies to component parameters supplied from non-body sources, including [SupplyParameterFromQuery] and form binding with [SupplyParameterFromForm] . These bind string or form values without JSON parsing, so they don’t support unions.
Parameter binding for unions from non-body sources is still being explored. If you have a scenario that needs it, the team is gathering feedback on the union parameter binding issue .
Summary
The two opening examples make the choice concrete. Kubernetes maxUnavailable fits a union because it is an existing discriminator-free contract that accepts either an int or a string . PaymentEvent fits a closed hierarchy because its cases form one related family and the JSON can identify each event with a discriminator.
Both models let the compiler check exhaustive switches. Choose between them based on the relationship between the alternatives and the JSON contract you need to preserve.
Additional resources
C# union types (language reference)
What’s new in ASP.NET Core in .NET 11
JSON serialization and deserialization in .NET
How to serialize polymorphic types with System.Text.Json
Parameter binding in Minimal API applications
How to create responses in Minimal API apps
