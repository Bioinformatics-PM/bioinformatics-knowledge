---
aliases:
  - Python Docs
  - docs.python.org
  - Python Language Reference
  - Python Standard Library Reference
tags:
  - type/source
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
kind: website
tier: A
authors:
  - Python Software Foundation
institution: Python Software Foundation
year: 2024
edition: "3.13"
url: "https://docs.python.org/3.13/"
access: free
---

# Python Documentation

> [!abstract]
> The official documentation of the Python language, maintained with CPython by the Python Software Foundation: tutorial, language reference, standard library reference, HOWTOs and the "What's New" release notes.

## Why this source

It is the normative description of the language (the Language Reference) and of every standard-library module, versioned with each release, so a claim can be pinned to the exact Python version the vault targets (3.13, released 7 October 2024). Books and courses explain Python; this is where their statements are checked. Pages also flag CPython implementation details (behaviour another implementation may not share) and record when a feature was added or changed ("Added in version 3.12", "Changed in version 3.13").

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| Tutorial | Informal tour: control flow, data structures, modules, input and output, classes | [[Python Programming]] |
| Language Reference, "Data model" | Objects, values and types (identity, type, value; mutability; garbage collection), special method names | [[Python Object Model]], [[Object-Oriented Programming]] |
| Language Reference, expressions and statements | Comprehensions, generator expressions, assignment and augmented assignment, `with`, function definitions and default values | [[Python Programming]], [[Iterator]] |
| Library Reference, built-in types and functions | Numeric types, sequences, `str` and `bytes`, `dict`, `set`, iterator types, `open` | [[Python Programming]], [[Iterator]], [[File Input and Output]] |
| Library Reference, modules | `itertools`, `functools`, `operator`, `copy`, `dataclasses`, `typing`, `collections`, `array`, `sys`, `tracemalloc`, `io`, `pathlib`, `gzip`, `codecs`, `contextlib`, `concurrent.futures` | [[Iterator]], [[Functional Programming]], [[File Input and Output]], [[Python Object Model]] |
| HOWTOs | Functional Programming HOWTO, Unicode HOWTO, Sorting HOWTO | [[Functional Programming]], [[File Input and Output]] |
| What's New in Python 3.13 | New interactive interpreter, experimental free-threaded build (PEP 703), experimental JIT compiler (PEP 744), `copy.replace` | [[Python Programming]] |

## How to use it

- L1: read the Tutorial once for idioms, then use the Library Reference as the reference for every module you import.
- L1 to L2: read "Data model" (sections on objects and special methods) with [[Python Object Model]]; read the `itertools` page with [[Iterator]].
- Always check the version selector: pages exist per release, and the "Added in" and "Changed in" notes say which interpreter a snippet needs.

## Caveats

- The documentation follows CPython; statements marked as implementation details (object addresses as identity, small-integer caching, reference counting) do not bind other implementations.
- The default page (`/3/`) shows the latest release; cite the 3.13 pages for the vault's target version.
- Verified in this pass: the 3.13 documentation URL, the 3.13 release date and headline features from "What's New in Python 3.13", `itertools.batched` (added in 3.12, `strict` option in 3.13) and `copy.replace` (added in 3.13).
