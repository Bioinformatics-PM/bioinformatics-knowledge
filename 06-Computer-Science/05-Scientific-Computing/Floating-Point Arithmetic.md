---
aliases:
  - IEEE 754
  - Floating Point
  - Double Precision
  - binary64
  - Machine Epsilon
  - NaN
  - Arithmétique en virgule flottante
tags:
  - type/concept
  - domain/computer-science
  - domain/mathematics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Integer Representation]]"
  - "[[Logarithm]]"
  - "[[Python Object Model]]"
related:
  - "[[Rounding Error]]"
  - "[[Numerical Stability]]"
  - "[[Log-Space Arithmetic]]"
  - "[[Condition Number]]"
  - "[[Vectorization]]"
  - "[[N-Dimensional Array]]"
  - "[[Numerical Testing]]"
  - "[[Missing Data]]"
  - "[[Phred Quality Score]]"
  - "[[Likelihood Function]]"
projects:
  - "[[07-evolution-simulator]]"
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[Goldberg 1991 - What Every Computer Scientist Should Know About Floating-Point Arithmetic]]"
  - "[[Python Documentation]]"
  - "[[Python for Data Analysis (McKinney)]]"
---

# Floating-Point Arithmetic

> [!abstract]
> A `float` is a binary number with 53 significant bits and a movable exponent: most decimals such as 0.1 are stored approximately, every operation rounds, NaN and infinity are ordinary values, and two floats are therefore compared with a tolerance, never with `==`.

## Definition

A **floating-point number** has the form $\pm d_0.d_1 \dots d_{p-1} \times \beta^{E}$: a **significand** of $p$ digits in base $\beta$ and an **exponent** $E$ within $[E_{\min}, E_{\max}]$. The IEEE 754 standard fixes binary formats and requires that addition, subtraction, multiplication, division and square root be **exactly rounded**: computed as if exactly, then rounded to the nearest representable number, ties to even.[^goldberg] Its **double** format (binary64) has $p = 53$, an 11-bit exponent with $E_{\min} = -1022$ and $E_{\max} = 1023$, and 64 bits in total.[^goldberg] Python's `float` is a C `double`, which on almost all machines is IEEE 754 binary64,[^types][^tut] and NumPy's `float64` is the same type, beside `float32` and `float16`.[^mck4]

## Why it matters

- **Likelihoods underflow.** A tree or HMM likelihood multiplies thousands of probabilities below 1; the product leaves the representable range and becomes exactly 0 (Advanced), which is why [[08-phylogenetic-engine]] works in [[Log-Space Arithmetic|log space]].
- **Tests and filters.** `0.1 + 0.2 == 0.3` is `False`. A filter such as `freq == 0.3` in [[07-evolution-simulator]], or a unit test comparing a computed GC content with `==`, fails for reasons unrelated to the biology ([[Numerical Testing]]).
- **NaN is the missing value of numeric arrays.** pandas and NumPy mark missing measurements with NaN, which is unequal to everything including itself and propagates through sums and means ([[Missing Data]]).
- **Single precision loses integers.** `float32`, common for large expression matrices and GPU code, holds only 24 significant bits: genome positions above $2^{24} = 16\,777\,216$ are no longer exact (Deeper).

## Core (L1)

![[ieee754-binary64-layout.svg]]

**The 64 bits.** One sign bit $s$, an 11-bit **biased exponent** $e$ ($E = e - 1023$) and a 52-bit **fraction** $f$. For normal numbers the leading significand bit is always 1 and is not stored, which gives 53 bits of precision with 52 stored.[^goldberg] Two exponent values are reserved:[^goldberg]

| Exponent bits $e$ | Fraction $f$ | Value |
|---|---|---|
| all zeros | 0 | $\pm 0$ (signed zero) |
| all zeros | $\neq 0$ | subnormal (denormalized): $\pm 0.f \times 2^{-1022}$ |
| 1 to 2046 | any | normal: $\pm 1.f \times 2^{e - 1023}$ |
| all ones | 0 | $\pm\infty$ |
| all ones | $\neq 0$ | NaN (not a number) |

The decoder below reads these fields from the bytes of any Python float (outputs from Python 3.11, NumPy 2.4.6):

```python
import math
import struct
from decimal import Decimal


def fields(x: float) -> tuple[int, int, int]:
    """Sign bit, biased exponent (11 bits) and fraction (52 bits) of a double."""
    bits = int.from_bytes(struct.pack(">d", x), "big")
    return bits >> 63, (bits >> 52) & 0x7FF, bits & ((1 << 52) - 1)


def from_fields(s: int, e: int, f: int) -> float:
    if e == 0x7FF:                                   # all ones: infinity or NaN
        return math.nan if f else (-1) ** s * math.inf
    if e == 0:                                       # all zeros: zero or subnormal, no hidden 1
        return (-1) ** s * (f / 2**52) * 2.0**-1022
    return (-1) ** s * (1 + f / 2**52) * 2.0 ** (e - 1023)


for x in (1.0, -2.5, 0.1, 5e-324, math.inf, math.nan):
    s, e, f = fields(x)
    print(f"{x!r:>7}  s={s} e={e:4d} f={f:#015x}  ->", from_fields(s, e, f))
print((0.1).hex(), Decimal(0.1))
```

```text
    1.0  s=0 e=1023 f=0x0000000000000  -> 1.0
   -2.5  s=1 e=1024 f=0x4000000000000  -> -2.5
    0.1  s=0 e=1019 f=0x999999999999a  -> 0.1
 5e-324  s=0 e=   0 f=0x0000000000001  -> 5e-324
    inf  s=0 e=2047 f=0x0000000000000  -> inf
    nan  s=0 e=2047 f=0x8000000000000  -> nan
0x1.999999999999ap-4 0.1000000000000000055511151231257827021181583404541015625
```

**0.1 is not 0.1.** $1/10$ has an infinite binary expansion ($0.000110011\ldots_2$), so the stored value is the nearest double, slightly above 0.1; Python prints `0.1` because it shows the shortest decimal string that maps back to the same double.[^tut] `Decimal(0.1)` reveals the exact stored value.

**Machine epsilon.** `sys.float_info.epsilon` $= 2^{-52} \approx 2.22 \times 10^{-16}$ is the gap between 1.0 and the next double.[^sys] Rounding to nearest makes the relative error of storing a number, or of each exactly rounded operation, at most half that gap, $u = 2^{-53} \approx 1.11 \times 10^{-16}$, which Goldberg calls machine epsilon.[^goldberg] A double therefore carries about 15 to 16 significant decimal digits.

**Compare with a tolerance.** `math.isclose(a, b, rel_tol=1e-09, abs_tol=0.0)` tests $|a - b| \le \max(\text{rel\_tol} \cdot \max(|a|, |b|), \text{abs\_tol})$.[^math] A relative tolerance is meaningless near 0, where an absolute tolerance is needed:

```python
print(0.1 + 0.2 == 0.3, 0.1 + 0.2, math.isclose(0.1 + 0.2, 0.3))
print((0.1 + 0.2) + 0.3 == 0.1 + (0.2 + 0.3))
print(1e16 + 1 == 1e16, float(2**53 + 1) == 2**53)
print(math.isclose(1e-12, 0.0), math.isclose(1e-12, 0.0, abs_tol=1e-9))
```

```text
False 0.30000000000000004 True
False
True True
False True
```

Addition is not associative, `1e16 + 1` rounds back to `1e16` (the gap between doubles there is 2), and $2^{53} + 1$ is the first integer a double cannot hold.

**NaN and infinity.** Overflow gives `inf`, `inf - inf` gives `nan`; any ordered comparison with NaN is false, so NaN is not equal to itself.[^goldberg][^cmp] Python raises `ZeroDivisionError` on `1.0 / 0.0` where NumPy returns `inf` or `nan`. One more trap: membership tests in Python containers check identity before equality, so the *same* NaN object is found in a list while an equal-looking one is not.[^cmp]

```python
nan = float("nan")
print(nan == nan, nan != nan, math.isnan(nan), nan in [nan], float("nan") in [float("nan")])
print(math.inf - math.inf, 1e308 * 10, 0.0 == -0.0, math.copysign(1, -0.0))
try:
    1.0 / 0.0
except ZeroDivisionError as err:
    print("ZeroDivisionError:", err)
import numpy as np

arr = np.array([2.0, np.nan, 1.0])
print(arr.mean(), np.nanmean(arr), np.sort(arr), (arr == np.nan).any(), np.isnan(arr).sum())
with np.errstate(divide="ignore", invalid="ignore"):
    print(np.array([1.0, 0.0, -1.0]) / 0.0)
```

```text
False True True True False
nan inf True -1.0
ZeroDivisionError: float division by zero
nan 1.5 [ 1.  2. nan] False 1
[ inf  nan -inf]
```

Test for missing values with `math.isnan` or `np.isnan`, never with `== np.nan`; use the `nan`-aware reductions (`np.nanmean`) only when ignoring missing values is the intended analysis.

## Deeper (L2)

**Spacing grows with magnitude.** Between consecutive powers of two there are $2^{52}$ equally spaced doubles, so the gap $\mathrm{ulp}(x)$ (unit in the last place) doubles at each power of two while the *relative* gap stays near $2^{-52}$ (lower panel of the figure). `float32` has $p = 24$: about 7 significant digits (NumPy guarantees 6), and integers are exact only up to $2^{24}$.[^mck4]

```python
import sys

fi = sys.float_info
print(fi.mant_dig, fi.epsilon, fi.epsilon == 2**-52, fi.max, fi.min, math.ulp(0.0))
print(1.0 + 2**-53 == 1.0, math.nextafter(1.0, 2.0) - 1.0)
print(math.ulp(1.0), math.ulp(3.1e9), math.ulp(1e16))
print(np.float32(16_777_217), np.finfo(np.float32).eps, np.finfo(np.float32).precision, np.finfo(np.float64).precision)
pos = np.array([123_456_789, 123_456_790, 123_456_791])      # invented genome positions
print(pos.astype(np.float32).astype(np.int64))
```

```text
53 2.220446049250313e-16 True 1.7976931348623157e+308 2.2250738585072014e-308 5e-324
True 2.220446049250313e-16
2.220446049250313e-16 4.76837158203125e-07 2.0
1.6777216e+07 1.1920929e-07 6 15
[123456792 123456792 123456792]
```

`sys.float_info.min` is the smallest *normal* double; subnormals extend down to `5e-324` with fewer significant bits.[^sys][^goldberg] Three neighbouring positions on a chromosome collapse to one `float32` value, so coordinates belong in integer types ([[Integer Representation]]).

**Summation order matters.** Each addition rounds, and the errors accumulate differently depending on the order. `math.fsum` returns an accurately rounded sum by tracking partial sums,[^math] NumPy's `sum` is much more accurate than a naive loop, and a running total in `float32` drifts far:

```python
vals = [0.1] * 10_000_000
total32 = np.float32(0.0)
for v in np.full(10_000_000, 0.1, dtype=np.float32):
    total32 += v
print(sum(vals), math.fsum(vals), np.sum(np.array(vals)), total32)
```

```text
999999.9998389754 1000000.0 1000000.0 1.087937e+06
```

The `float32` loop is off by 8.8 %: once the total is large, each added 0.1 is rounded to the coarse spacing of the total. Why some algorithms amplify such errors and others do not is the subject of [[Rounding Error]] and [[Numerical Stability]].

**NumPy's tolerance is asymmetric.** `np.isclose(a, b)` tests $|a - b| \le \text{atol} + \text{rtol} \cdot |b|$ with defaults `rtol=1e-05`, `atol=1e-08`, so the order of arguments matters and every value below $10^{-8}$ is "close" to 0:

```python
a, b = 1.0, 1.00001
print(np.isclose(a, b, atol=0), np.isclose(b, a, atol=0), math.isclose(a, b, rel_tol=1e-5), math.isclose(b, a, rel_tol=1e-5))
import inspect

print(inspect.signature(math.isclose), inspect.signature(np.isclose))
print(np.isclose(1e-9, 0.0), np.isclose(1e-9, 2e-9))
```

```text
True False True True
(a, b, *, rel_tol=1e-09, abs_tol=0.0) (a, b, rtol=1e-05, atol=1e-08, equal_nan=False)
True True
```

For probabilities of order $10^{-9}$ (rare variants, p-values) the default `atol` declares everything equal: set `atol` to the scale of your data, or compare logarithms.

## Advanced (L3)

**Underflow of products.** Multiplying per-site likelihoods of $10^{-3}$ (invented) passes below the smallest normal double at 103 sites, loses precision gradually through the subnormals, and reaches exactly 0 at 108 sites:

```python
p = 1e-3                                                        # invented per-site likelihood
print(p**100, p**107, p**108, next(n for n in range(1, 1000) if p**n == 0.0))
print(np.prod(np.full(1000, p)), np.log(np.full(1000, p)).sum())
```

```text
1.000000000000002e-300 1e-321 0.0 108
0.0 -6907.755278982137
```

A real alignment has thousands of sites, so the product of likelihoods is 0 for every tree and the comparison is lost; the sum of logarithms, $-6907.76$, is perfectly representable. Working with logarithms, and adding probabilities stored as logarithms, is [[Log-Space Arithmetic]]; why the naive formula fails while the log form works is a question of [[Numerical Stability]].

**Reproducibility.** Because addition is not associative, a parallel or vectorized reduction that changes the order of terms can change the last bits of a result; so can a different library version or number of threads. Bit-identical results across machines are therefore the exception: tests compare with tolerances chosen from the size of the computation, and pipelines record versions ([[Numerical Testing]]).

**Exact alternatives.** When decimal values must be exact (concentrations entered by a user, money), Python's `decimal` and `fractions` modules represent them exactly, at a large cost in speed; they are not for array computation.[^tut]

## Mathematical representation

- **Normal doubles**: $x = (-1)^s \left(1 + f/2^{52}\right) 2^{E}$ with $f \in \{0, \dots, 2^{52} - 1\}$ and $E \in [-1022, 1023]$; the largest is $(2 - 2^{-52})\,2^{1023} \approx 1.798 \times 10^{308}$, the smallest positive normal $2^{-1022} \approx 2.225 \times 10^{-308}$, the smallest subnormal $2^{-1074} \approx 4.9 \times 10^{-324}$.
- **Spacing**: for $2^E \le |x| < 2^{E+1}$, $\mathrm{ulp}(x) = 2^{E - 52}$, so $\mathrm{ulp}(x)/|x| \in (2^{-53}, 2^{-52}]$.
- **Rounding model**: with $\mathrm{fl}$ the rounding to nearest, $\mathrm{fl}(x) = x(1 + \delta)$ with $|\delta| \le u = 2^{-53}$ for $x$ in the normal range; exact rounding of the basic operations gives $\mathrm{fl}(a \circ b) = (a \circ b)(1 + \delta)$, $|\delta| \le u$, for $\circ \in \{+, -, \times, /\}$.[^goldberg]
- **Integers**: every integer $|n| \le 2^{53}$ is a double; $2^{53} + 1$ is not (the spacing there is 2). For `float32`, replace 53 by 24.
- **Tolerance tests**: `math.isclose`: $|a - b| \le \max(r \max(|a|, |b|), t)$, symmetric in $a, b$.[^math] `np.isclose`: $|a - b| \le t + r|b|$, not symmetric.

## Computational representation

| Python / NumPy | Format | Significant bits | Typical use |
|---|---|---|---|
| `float`, `np.float64` | binary64 | 53 | default for statistics and likelihoods |
| `np.float32` | binary32 | 24 | large matrices, GPU code, when memory dominates |
| `np.float16` | binary16 | 11 | storage only, machine learning |

`sys.float_info` and `np.finfo(dtype)` give the limits of each format; `math.ulp`, `math.nextafter` and `np.spacing` give local spacing; `float.hex` and `float.as_integer_ratio` show the exact stored value.[^sys][^math][^types] A missing value in a numeric NumPy or pandas column is a NaN, which forces the column to a float dtype.[^mck7]

## Worked example

> [!example] Decoding the double nearest to 0.1
> Bytes (from `struct.pack(">d", 0.1).hex()`): `3f b9 99 99 99 99 99 9a`.
> 1. **Split the 64 bits**: `0 | 01111111011 | 1001 1001 ... 1001 1010`. Sign $s = 0$.
> 2. **Exponent**: $01111111011_2 = 1019$, so $E = 1019 - 1023 = -4$; $2^{-4} = 1/16$.
> 3. **Significand**: $f = \mathtt{0x999999999999A}$, $1 + f/2^{52} = 1.6000000000000000888\ldots$ The pattern `1001` repeats because $1.6 = 1.1001\,1001\ldots_2$, and the final `A` (`1010`) is the rounded-up last digit.
> 4. **Value**: $1.6000000000000000888\ldots / 16 = 0.1000000000000000055511151231257827\ldots$
> 5. **Error**: $5.55 \times 10^{-18}$ absolute, $5.55 \times 10^{-17}$ relative, below $u = 2^{-53} \approx 1.11 \times 10^{-16}$ as the rounding model guarantees.
> 6. **Consequence**: `0.1 + 0.2` adds two such approximations and rounds again, landing one ulp above the double nearest to 0.3: hence `0.30000000000000004`.

## Common misconceptions

> [!warning] "0.1 + 0.2 != 0.3 is a Python bug"
> It is the binary representation: every language using IEEE doubles gives the same result.[^tut] Compare with `math.isclose`, or compute in integers (counts, base pairs) when exactness matters.

> [!warning] "Machine epsilon is the smallest positive float"
> `sys.float_info.epsilon` ($2.2 \times 10^{-16}$) is the gap after 1.0, a *relative* precision; the smallest positive double is about $4.9 \times 10^{-324}$. Texts also disagree by a factor of 2: Goldberg's machine epsilon is the rounding bound $2^{-53}$, Python's and NumPy's is $2^{-52}$.[^goldberg][^sys]

> [!warning] "A tolerance of 1e-9 works everywhere"
> A relative tolerance fails near 0 (`math.isclose(1e-12, 0.0)` is `False`) and an absolute one fails for large or tiny magnitudes (`np.isclose(1e-9, 2e-9)` is `True`). Choose tolerances from the scale and the accumulated error of the computation.

> [!warning] "NaN behaves like None"
> `x == np.nan` is always `False`, `np.mean` of an array with one NaN is NaN, and `np.sort` puts NaN last. Detect missing values with `isnan`, and decide explicitly whether to drop, impute or propagate them ([[Missing Data]]).

## Exercises

> [!question] Exercise 1 (L1)
> `round(2.675, 2)` returns `2.67`, not `2.68`. Explain using `Decimal(2.675)`, then say what `round(0.5)`, `round(1.5)` and `round(2.5)` return and why.

> [!success]- Solution
> `Decimal(2.675)` is `2.67499999999999982236431605997495353221893310546875`: the stored double is just below 2.675, so rounding to two decimals correctly gives 2.67.[^funcs] `round(0.5)`, `round(1.5)`, `round(2.5)` give `0 2 2`: exact ties (these three are exactly representable) round to the even neighbour.[^funcs]

> [!question] Exercise 2 (L1)
> Predict each value: `0.1 * 3 == 0.3`, `math.isclose(0.1 * 3, 0.3)`, `float("nan") == float("nan")`, `1e16 + 1 == 1e16`, `math.isclose(1e-12, 0.0)`.

> [!success]- Solution
> `False` (`0.1 * 3` is `0.30000000000000004`), `True`, `False` (NaN is unequal to itself), `True` (spacing 2 at $10^{16}$), `False` (relative tolerance near 0; add `abs_tol`).

> [!question] Exercise 3 (L2)
> Decode the double with bytes `40 0C 00 00 00 00 00 00` by hand, then check with `struct.unpack(">d", bytes.fromhex("400C000000000000"))`.

> [!success]- Solution
> Bits: `0 | 10000000000 | 1100 0000 ...`. $e = 1024$, $E = 1$; $f = \mathtt{0xC000000000000}$, so $1 + f/2^{52} = 1 + 1/2 + 1/4 = 1.75$; value $1.75 \times 2 = 3.5$. `struct.unpack` gives `3.5`, and `fields(3.5)` gives `(0, 1024, 3377699720527872)` with $3377699720527872 = 3 \times 2^{50}$.

> [!question] Exercise 4 (L2, Python)
> Convert Phred scores $Q \in \{10, 20, 30, 40\}$ to error probabilities $p = 10^{-Q/10}$ and back with $Q = -10 \log_{10} p$ ([[Phred Quality Score]]). The round trip is exact here; is it safe to test it with `==` in general?

> [!success]- Solution
> ```python
> Q = np.array([10, 20, 30, 40])
> perr = 10.0 ** (-Q / 10)
> print(perr, -10 * np.log10(perr), np.array_equal(-10 * np.log10(perr), Q))
> ```
> ```text
> [0.1    0.01   0.001  0.0001] [10. 20. 30. 40.] True
> ```
> Equality holds for these inputs, but $10^{-Q/10}$ and $\log_{10}$ each round, and nothing guarantees an exact round trip for other $Q$ (non-integers, other libraries). Round to the nearest integer when $Q$ must be an integer (`np.rint`), or compare with `np.isclose(..., atol=1e-9)`.

> [!question] Exercise 5 (L3, Python)
> With per-site likelihood $10^{-3}$, from which number of sites $n$ does the product become exactly 0, and from which does it leave the normal range? Derive both from $\log_{10}$ of the limits, then check numerically.

> [!success]- Solution
> Normal range ends at $2.2 \times 10^{-308}$: $10^{-3n} < 2.2 \times 10^{-308}$ for $3n > 307.65$, i.e. $n \ge 103$. The result is 0 when $10^{-3n}$ is below half the smallest subnormal, $\approx 2.5 \times 10^{-324}$: $3n > 323.6$, i.e. $n \ge 108$. The code in Advanced prints `1e-321` for $n = 107$ and `0.0` for $n = 108$, and finds 108. The log-likelihood $-3n \ln 10$ never underflows.

> [!question] Exercise 6 (L3)
> Using $\mathrm{ulp}(x) = 2^{E - p + 1}$, compute the spacing of `float64` and of `float32` around a genome position of $1.5 \times 10^8$, and say which positions `float32` can represent there. Check with `math.ulp` and `np.spacing`.

> [!success]- Solution
> $2^{27} \approx 1.34 \times 10^8 \le 1.5 \times 10^8 < 2^{28}$, so $E = 27$. `float64`: $2^{27 - 52} = 2^{-25} \approx 3 \times 10^{-8}$, every integer is exact. `float32`: $2^{27 - 23} = 16$, only multiples of 16 are representable, so up to 8 bp of error per position. `np.spacing(np.float32(1.5e8))` gives `16.0`; `math.ulp(3.1e9)` gives `4.77e-07` (Deeper), still far below 1 for doubles.

## Mastery checklist

- [ ] 1 Recognized: I can name the three fields of a double, say that 0.1 is stored approximately, and list NaN, infinity and signed zero.
- [ ] 2 Understood: I can explain machine epsilon (both definitions), ulp spacing, exact rounding, and why `==` fails.
- [ ] 3 Practiced: I can decode a double by hand and in Python, choose `math.isclose` or `np.isclose` tolerances, and handle NaN in arrays.
- [ ] 4 Applied: [[07-evolution-simulator]] and [[08-phylogenetic-engine]] compare floats with stated tolerances and avoid underflow in likelihoods.
- [ ] 5 Explained: I can teach float32 versus float64 trade-offs, summation-order effects on reproducibility, and why products of probabilities need logarithms.

## References

[^goldberg]: [[Goldberg 1991 - What Every Computer Scientist Should Know About Floating-Point Arithmetic]], *ACM Computing Surveys* 23(1):5-48: floating-point formats, machine epsilon as the relative rounding bound, the IEEE 754 double format (precision 53, 11-bit biased exponent, $E_{\min} = -1022$, $E_{\max} = 1023$), special values (signed zero, denormalized numbers, infinities, NaN and its comparisons), exactly rounded operations with round to even.
[^types]: [[Python Documentation]], 3.13, Library Reference, "Built-in Types": floats implemented as C doubles; `float.hex` and `float.as_integer_ratio`.
[^tut]: [[Python Documentation]], 3.13, "The Python Tutorial", "Floating-Point Arithmetic: Issues and Limitations": decimal fractions approximated by binary fractions, 0.1, shortest repr, the same behaviour in every language using the hardware's floating point, `decimal` and `fractions`, and "Representation Error" (IEEE 754 binary64, 53 bits of precision, on almost all machines).
[^sys]: [[Python Documentation]], 3.13, Library Reference, `sys.float_info`: `epsilon` (difference between 1.0 and the least representable value greater than 1.0), `max`, `min` (minimum normalized float), `mant_dig`.
[^math]: [[Python Documentation]], 3.13, Library Reference, `math`: `isclose` (formula, defaults `rel_tol=1e-09`, `abs_tol=0.0`), `fsum` (accurate floating-point sum tracking partial sums), `ulp`, `nextafter`, `isnan`.
[^cmp]: [[Python Documentation]], 3.13, Language Reference, "Expressions", comparisons: not-a-number values are not equal to themselves; for containers, `x in y` is equivalent to `any(x is e or x == e for e in y)`.
[^funcs]: [[Python Documentation]], 3.13, Library Reference, "Built-in Functions", `round`: ties go to the even choice; `round(2.675, 2)` gives 2.67 because most decimal fractions cannot be represented exactly.
[^mck4]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 4 "NumPy Basics: Arrays and Vectorized Computation": half, single and double precision floating-point dtypes, `float64` compatible with the C double and the Python float.
[^mck7]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 7 "Data Cleaning and Preparation": NaN as the missing-data sentinel of numeric data.
