---
aliases:
  - NumPy paper
tags:
  - type/source
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Charles R. Harris
  - K. Jarrod Millman
  - Stéfan J. van der Walt
  - Ralf Gommers
  - Travis E. Oliphant
journal: Nature
year: 2020
url: "https://doi.org/10.1038/s41586-020-2649-2"
access: free
---

# Harris 2020 - Array Programming with NumPy

> [!abstract]
> The reference paper on NumPy by its core developers: the array model (data buffer, dtype, shape, strides), views, indexing and vectorized computation, and NumPy's role as the foundation and interoperability layer of scientific Python.

## Why this source

Peer-reviewed and written by the people who maintain NumPy, it explains in a few pages the concepts that every NumPy tutorial assumes (why slicing is free, what strides are, why arrays from other libraries can be used with NumPy functions) and states NumPy's place in the ecosystem. It is open access.

## Coverage

Citation: Harris CR, Millman KJ, van der Walt SJ, Gommers R, et al., Oliphant TE. "Array programming with NumPy". *Nature* 585:357-362 (2020). doi:10.1038/s41586-020-2649-2. Free at PMC7759461 and arXiv:2006.10256.

| Part | Content | Vault notes |
|---|---|---|
| Array data structure | Data buffer described by dtype, shape and strides; C or Fortran memory order | [[N-Dimensional Array]], [[Array Memory Layout]] |
| Indexing | Single elements, subarrays (views sharing data), boolean conditions, indexing by other arrays | [[N-Dimensional Array]], [[Array Indexing]] |
| Vectorization | Whole-array operations instead of Python loops | [[Vectorization]], [[Broadcasting]] |
| Ecosystem | NumPy as the base of scientific Python and an interoperability layer between array libraries | [[Scientific Python Ecosystem]] |

## How to use it

- L1: read the array-structure and indexing parts with [[N-Dimensional Array]].
- L2: read the ecosystem and interoperability parts with [[Scientific Python Ecosystem]], and the vectorization part with [[Vectorization]].

## Caveats

- A 2020 overview: API details (NumPy 2 changes to type promotion and the default string handling) are in the NumPy release notes, not here.
- Verified in this pass: citation (journal, volume, pages, year, DOI, PMC and arXiv records), the abstract's statements (array programming paradigm, use across sciences, interoperability layer), and text on strides and memory order, views and indexing. Figure-level details were not checked.
