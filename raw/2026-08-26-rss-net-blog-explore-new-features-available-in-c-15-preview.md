---
source: "https://devblogs.microsoft.com/dotnet/explore-csharp-15/"
title: "Explore new features available in C# 15 preview"
author: "Bill Wagner"
date_published: "2026-08-24"
date_clipped: "2026-08-26"
category: ".NET Ecosystem"
source_type: "rss"
---

# Explore new features available in C# 15 preview

Source: https://devblogs.microsoft.com/dotnet/explore-csharp-15/

C# 15 will ship with .NET 11 in November. All the new features are available in .NET 11 preview 7 for you to try now. C# 15 adds union types , closed hierarchies , the first preview of an updated unsafe model, collection expression arguments, extension indexers, and labeled break and continue . For more details on each of these features, see What’s new in C# 15 and the articles linked from that page.
Union types
A union type lets you say, in the type system, exactly which types a value may hold. With object , a marker interface, or an abstract base class, the runtime type can still be anything derived from object or anything that implements or derives from the shared type. A union constrains the value to one of the specified case types . The case types in a union aren’t necessarily related by inheritance. Use the closed hierarchies feature to restrict the set of types related by inheritance.
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);
public union Pet(Cat, Dog, Bird);
A Pet holds a Cat , a Dog , or a Bird . Each case type converts implicitly to Pet . Because the compiler knows the complete set, a switch expression over a non-null Pet is exhaustive without a discard or default arm:
Pet pet = new Dog("Rex");
string name = pet switch
{
Dog d => d.Name,
Cat c => c.Name,
Bird b => b.Name,
};
Union types are one expression of a broader design idea: make the allowed set of types explicit. Closed hierarchies , covered next, and the planned closed enums apply the same idea in other shapes.
For more, read the C# 15 union types post, try the Work with union types tutorial, and see the union types reference.
Closed hierarchies
Closed hierarchies apply the same idea to class hierarchies you design. The closed modifier on a class makes it implicitly abstract , and restricts its direct derived types to the declaring assembly. You declare which subtypes are allowed instead of leaving derivation open-ended. For example, you can model the states of a background job as records that derive from a closed base:
public closed record class JobStatus;
public record class Queued : JobStatus;
public record class Running(int PercentComplete) : JobStatus;
public record class Completed(TimeSpan Elapsed) : JobStatus;
public record class Failed(string Error) : JobStatus;
Closed hierarchies, union types, and the planned closed enums all express the allowed set of shapes directly in the type system. For rules, including how closed composes with inheritance, see the closed modifier and closed hierarchy patterns references.
Memory-safety redesign (preview)
C# 15 starts a redesign of unsafe : from a syntax marker—”there are pointers here”—to a contract the compiler can’t verify and a developer upholds. This is a preview feature in .NET 11 and C# 15. The model and syntax might change for .NET 12 and C# 16. The current preview includes two language changes you can try. You need to opt in explicitly: add <Features>$(Features);updated-memory-safety-rules</Features> and <LangVersion>preview</LangVersion> to your project file.
In the new model, pointer types no longer need an unsafe context. You can declare a pointer type, take an address with & , use the fixed statement, convert a stackalloc to a pointer, and use sizeof on an unmanaged type in a safe context.
Operations that dereference pointers still require unsafe : pointer indirection ( *p ), member access through a pointer ( p->m ), element access through a pointer ( p[i] ), fixed-size-buffer element access, and function-pointer invocation.
Finally, when a member adds the unsafe modifier to its signature, that member can be called only in an unsafe context. This is a breaking change from the current semantics of unsafe on a member. The member is declaring that its callers must ensure that the contract is followed, or propagate the unsafety by also including the unsafe modifier in its declaration.
Read Improving C# memory safety for the full model, and see the unsafe code reference for the rules implemented in preview in C# 15.
Important
This is a preview feature in .NET 11 and C# 15. The design isn’t final and will continue to evolve before it ships in its final form. We want people to try the preview behavior and give us feedback in csharplang so we can shape the final experience.
Collection expression arguments
Collection expressions convert to many collection types, but until now you couldn’t pass arguments to the underlying constructor or Create method. C# 15 adds a with(...) element, written first, that forwards arguments to the constructor or factory method.
This feature is necessary for the upcoming dictionary expressions syntax. You will often specify the comparer for a dictionary. You can use the feature now for sequence containers:
// Before
List<string> names = new(capacity: values.Length * 2);
names.AddRange(values);
var set = new HashSet<string>(StringComparer.OrdinalIgnoreCase) { "Hello", "HELLO" };
// After (C# 15)
List<string> names = [with(capacity: values.Length * 2), .. values];
HashSet<string> set = [with(StringComparer.OrdinalIgnoreCase), "Hello", "HELLO"];
Learn more in collection expression arguments .
Extension indexers
C# 14 introduced extension members: properties and operators alongside methods. C# 15 adds extension indexers , so you can index into a receiver as if the indexer were declared on its type. Indexers can’t be static, so the extension container must include a named receiver.
// Before: a helper method
public static class SequenceExtensions
{
public static int ElementAtIndex(this IEnumerable<int> sequence, int index)
=> sequence.ElementAt(index);
}
int third = numbers.ElementAtIndex(2);
// After (C# 15): an extension indexer
public static class SequenceExtensions
{
extension(IEnumerable<int> sequence)
{
public int this[int index] => sequence.ElementAt(index);
}
}
int third = numbers[2];
Learn more in the extension indexers reference.
Labeled break and continue
Breaking out of a nested loop usually means a flag, a goto , or an extracted method. With C# 15, you can label a loop and target it directly with break or continue .
// Before: a flag to unwind the outer loop
bool found = false;
foreach (Warehouse warehouse in warehouses)
{
foreach (Bin bin in warehouse.Bins)
{
if (bin.Sku == requestedSku && bin.Quantity > 0)
{
reserved = Reserve(bin);
found = true;
break;
}
}
if (found)
break;
}
// After (C# 15): label the loop and break it directly
scan: foreach (Warehouse warehouse in warehouses)
{
foreach (Bin bin in warehouse.Bins)
{
if (bin.Sku == requestedSku && bin.Quantity > 0)
{
reserved = Reserve(bin);
break scan;
}
}
}
The intent is in the code, with no flag to track. See the jump statements reference.
Try the preview
Download .NET 11 and try C# 15 on your apps. Read What’s new in C# 15 for the complete reference and participate in the ongoing discussions in csharplang .
