---
source: "https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/decimal-biginteger-floating-point-conversions"
title: "Decimal and BigInteger floating-point conversions are correctly rounded"
author: "gewarren"
date_published: "unknown"
date_clipped: "2026-11-19"
category: ".NET Ecosystem"
source_type: "web"
---

# Decimal and BigInteger floating-point conversions are correctly rounded

Source: https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/decimal-biginteger-floating-point-conversions

[Read in English](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/decimal-biginteger-floating-point-conversions)
[Edit](https://github.com/dotnet/docs/blob/main/docs/core/compatibility/core-libraries/11/decimal-biginteger-floating-point-conversions.md)

---

---

Note

Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/decimal-biginteger-floating-point-conversions) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Decimal and BigInteger floating-point conversions are correctly rounded

Conversions between [Decimal](https://learn.microsoft.com/en-us/dotnet/api/system.decimal) and binary floating-point types, and conversions from [BigInteger](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.biginteger) to binary floating-point types, now produce correctly rounded results. Previously, these conversions could truncate, round through intermediate values, or discard significant digits.

## Version introduced

.NET 11

## Previous behavior

Conversions from `float` and `double` to `decimal` retained only 7 and 15 significant decimal digits, respectively. This could hide the difference between a binary floating-point literal and a decimal literal:

```
using System.Globalization;

double value = 1.23;
decimal converted = (decimal)value;

Console.WriteLine(converted.ToString("G29", CultureInfo.InvariantCulture));
```

The output was:

```
1.23
```

Conversions from `decimal` to `float` or `double` could round more than once. For example:

```
using System.Globalization;

decimal value = 10000000000000.099609375m;
double converted = (double)value;

Console.WriteLine(converted.ToString("G99", CultureInfo.InvariantCulture));
```

The output was:

```
10000000000000.09765625
```

Conversions from `decimal` to `Half` or `BFloat16` first converted the value to `float`, which could also produce an incorrectly rounded result.

Conversions from `BigInteger` to `double` truncated discarded bits instead of rounding to the nearest representable value. For example:

```
using System.Globalization;
using System.Numerics;

BigInteger value = long.MaxValue / 2;
double converted = (double)value;

Console.WriteLine(converted.ToString("G17", CultureInfo.InvariantCulture));
```

The output was:

```
4.6116860184273874E+18
```

Conversions from `BigInteger` to `float`, `Half`, or `BFloat16` first converted the value to `double`, which could round twice and produce a result one unit in the last place away from the nearest representable value.

## New behavior

Starting in .NET 11, conversions round the exact source value once to the nearest representable destination value.

For the first example, the `double` value isn't exactly `1.23`. Its exact value is approximately `1.229999999999999982236431605997...`, so the converted `decimal` value is now:

```
1.229999999999999982236431606
```

For the second example, the converted `double` value is now:

```
10000000000000.099609375
```

Conversions from `decimal` to `Half` or `BFloat16` are also correctly rounded and can produce a different destination bit pattern than in previous versions.

For the `BigInteger` example, the converted `double` value is now:

```
4.6116860184273879E+18
```

Conversions from `BigInteger` to `float`, `Half`, or `BFloat16` are also correctly rounded.

If a conversion is evaluated as a compile-time constant, a compiler hosted by the .NET 11 SDK or a later SDK can embed the new result in the output assembly when the project is rebuilt, regardless of the project's target framework.

## Type of breaking change

This change is a [behavioral change](https://learn.microsoft.com/en-us/dotnet/core/compatibility/categories#behavioral-change).

## Reason for change

The previous conversion algorithms lost information that the destination type could represent and sometimes selected a value other than the nearest representable result. This caused precision errors in both directions of `decimal` conversion and in conversions from `BigInteger`. The new algorithms follow the expected floating-point rule of computation of the conversion as if with exact intermediate precision, followed by a single rounding to the destination type.

For more information, see [dotnet/runtime#130565](https://github.com/dotnet/runtime/pull/130565) and [dotnet/runtime#130566](https://github.com/dotnet/runtime/pull/130566).

## Recommended action

Don't assume that a binary floating-point literal and a decimal literal with the same source text represent the same value. If a value is intended to be decimal, use a decimal literal:

```
decimal value = 123.4567m;
```

instead of a conversion from a `double` literal:

```
decimal value = (decimal)123.4567;
```

To restore the previous result in general when you convert to `decimal`, round the converted value to 7 significant decimal digits for a `float` source or 15 significant decimal digits for a `double` source. The previous conversion rounded to nearest with ties to even; it didn't truncate. Positive and negative values were handled symmetrically.

For example, formatting the source value with the `G7` or `G15` standard numeric format string and parsing the result performs the corresponding significant-digit rounding for arbitrary finite values:

```
using System.Globalization;

static decimal ConvertToDecimalLikePrevious(float value)
{
    Span<char> text = stackalloc char[32];
    value.TryFormat(text, out int length, "G7", CultureInfo.InvariantCulture);
    return decimal.Parse(text[..length], NumberStyles.Float, CultureInfo.InvariantCulture);
}

static decimal ConvertToDecimalLikePrevious(double value)
{
    Span<char> text = stackalloc char[32];
    value.TryFormat(text, out int length, "G15", CultureInfo.InvariantCulture);
    return decimal.Parse(text[..length], NumberStyles.Float, CultureInfo.InvariantCulture);
}

decimal fromFloat = ConvertToDecimalLikePrevious(14.1f);          // 14.1
decimal fromDouble = ConvertToDecimalLikePrevious(-123.4567);     // -123.4567
```

The span-based implementation doesn't allocate. Values outside the range of `decimal` continue to throw an exception during parsing, as they did during conversion.

Update tests and serialized expected values that encoded the previous, incorrectly rounded result. This includes code that depended on `BigInteger` conversion truncation toward zero. If an application requires a specific legacy `float`, `double`, `Half`, or `BFloat16` bit pattern for a protocol or file format, encode that bit pattern explicitly rather than reproduce it through a numeric conversion.

There's no compatibility switch to restore the previous conversion algorithms.

## Affected APIs

- [Decimal.Decimal(Single)](https://learn.microsoft.com/en-us/dotnet/api/system.decimal.-ctor#system-decimal-ctor(system-single))
- [Decimal.Decimal(Double)](https://learn.microsoft.com/en-us/dotnet/api/system.decimal.-ctor#system-decimal-ctor(system-double))
- Explicit conversions from [Single](https://learn.microsoft.com/en-us/dotnet/api/system.single) and [Double](https://learn.microsoft.com/en-us/dotnet/api/system.double) to [Decimal](https://learn.microsoft.com/en-us/dotnet/api/system.decimal)
- Explicit conversions from [Decimal](https://learn.microsoft.com/en-us/dotnet/api/system.decimal) to [Single](https://learn.microsoft.com/en-us/dotnet/api/system.single) and [Double](https://learn.microsoft.com/en-us/dotnet/api/system.double)
- [Decimal.ToSingle(Decimal)](https://learn.microsoft.com/en-us/dotnet/api/system.decimal.tosingle#system-decimal-tosingle(system-decimal))
- [Decimal.ToDouble(Decimal)](https://learn.microsoft.com/en-us/dotnet/api/system.decimal.todouble#system-decimal-todouble(system-decimal))
- [Convert.ToDecimal(Single)](https://learn.microsoft.com/en-us/dotnet/api/system.convert.todecimal#system-convert-todecimal(system-single))
- [Convert.ToDecimal(Double)](https://learn.microsoft.com/en-us/dotnet/api/system.convert.todecimal#system-convert-todecimal(system-double))
- [Convert.ToSingle(Decimal)](https://learn.microsoft.com/en-us/dotnet/api/system.convert.tosingle#system-convert-tosingle(system-decimal))
- [Convert.ToDouble(Decimal)](https://learn.microsoft.com/en-us/dotnet/api/system.convert.todouble#system-convert-todouble(system-decimal))
- [Decimal.CreateChecked<TOther>(TOther)](https://learn.microsoft.com/en-us/dotnet/api/system.decimal.createchecked#system-decimal-createchecked-1(-0)), [Decimal.CreateSaturating<TOther>(TOther)](https://learn.microsoft.com/en-us/dotnet/api/system.decimal.createsaturating#system-decimal-createsaturating-1(-0)), and [Decimal.CreateTruncating<TOther>(TOther)](https://learn.microsoft.com/en-us/dotnet/api/system.decimal.createtruncating#system-decimal-createtruncating-1(-0)) when they convert to or from [Single](https://learn.microsoft.com/en-us/dotnet/api/system.single) or [Double](https://learn.microsoft.com/en-us/dotnet/api/system.double)
- Explicit conversion from [Decimal](https://learn.microsoft.com/en-us/dotnet/api/system.decimal) to [Half](https://learn.microsoft.com/en-us/dotnet/api/system.half)
- Explicit conversion from [Decimal](https://learn.microsoft.com/en-us/dotnet/api/system.decimal) to [BFloat16](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.bfloat16)
- Explicit conversions from [BigInteger](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.biginteger) to [Double](https://learn.microsoft.com/en-us/dotnet/api/system.double), [Single](https://learn.microsoft.com/en-us/dotnet/api/system.single), [Half](https://learn.microsoft.com/en-us/dotnet/api/system.half), and [BFloat16](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.bfloat16)
- Equivalent conversions performed through [IConvertible](https://learn.microsoft.com/en-us/dotnet/api/system.iconvertible) or the generic math interfaces

---
