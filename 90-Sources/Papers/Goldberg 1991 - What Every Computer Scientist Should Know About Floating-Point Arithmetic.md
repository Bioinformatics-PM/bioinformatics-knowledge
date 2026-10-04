---
aliases:
  - Goldberg 1991
  - What Every Computer Scientist Should Know About Floating-Point Arithmetic
tags:
  - type/source
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - David Goldberg
journal: ACM Computing Surveys
year: 1991
url: "https://doi.org/10.1145/103162.103163"
access: free
---

# Goldberg 1991 - What Every Computer Scientist Should Know About Floating-Point Arithmetic

> [!abstract]
> The classic tutorial on floating-point numbers: how they are represented, where rounding error comes from and how to bound it, and what the IEEE 754 standard guarantees.

## Why this source

Thirty years on, it is still the reference that numerical-computing courses and language documentations point to for the reasons behind floating-point surprises. It states the representation and error definitions (units in the last place, relative error, machine epsilon) precisely, then explains the IEEE 754 formats, special values and exactly rounded operations, so every later claim about rounding can be traced to a definition.

## Coverage

Citation: Goldberg D. "What Every Computer Scientist Should Know About Floating-Point Arithmetic". *ACM Computing Surveys* 23(1):5-48, March 1991. doi:10.1145/103162.103163. An edited reprint is published free as an appendix of Oracle's (formerly Sun's) *Numerical Computation Guide*.

| Part | Content | Vault notes |
|---|---|---|
| Rounding error | Floating-point formats (base, precision, exponent range), ulps and relative error, machine epsilon, guard digits, cancellation | [[Floating-Point Arithmetic]], [[Rounding Error]] |
| The IEEE standard | Single and double formats and their parameters, biased exponents, special quantities (NaN, infinity, signed zero, denormalized numbers), exactly rounded operations, exceptions | [[Floating-Point Arithmetic]] |
| Systems aspects | Languages, compilers and exception handling, with examples of how hardware and compilers can support careful numerics | [[Numerical Stability]] |

Cited in [[Floating-Point Arithmetic]].

## How to use it

- L1: read the representation part and the description of the IEEE formats and special values, with [[Floating-Point Arithmetic]].
- L2: read the rounding-error part (ulps, relative error, cancellation) before [[Rounding Error]] and [[Numerical Stability]].
- L3: skim the systems part when a result changes with compiler flags or hardware.

## Caveats

- Written for IEEE 754-1985; the 2008 and 2019 revisions keep the binary single and double formats it describes but add others (decimal formats, fused multiply-add).
- Its machine epsilon is the rounding bound $(\beta/2)\beta^{-p}$ ($2^{-53}$ for doubles), half of the "epsilon" reported by Python and NumPy ($2^{-52}$, the gap after 1.0).
- Long (43 pages) and proof-heavy in places: the theorems can be skipped on a first read.
- Verified in this pass: citation, issue, date, DOI and the paper's structure (representation and rounding error with machine epsilon, then the IEEE standard, then systems aspects); the free Oracle reprint.
