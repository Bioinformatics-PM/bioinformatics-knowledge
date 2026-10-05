---
aliases:
  - Python
  - Python 3
  - Python (Programming Language)
  - Programmation Python
tags:
  - type/concept
  - domain/computer-science
  - level/L1
mastery: 0
prerequisites: []
related:
  - "[[Python Object Model]]"
  - "[[Object-Oriented Programming]]"
  - "[[Functional Programming]]"
  - "[[Iterator]]"
  - "[[File Input and Output]]"
  - "[[Scientific Python Ecosystem]]"
  - "[[String]]"
  - "[[Hash Table]]"
projects:
  - "[[01-dna-engine]]"
  - "[[bio-core]]"
sources:
  - "[[Python Documentation]]"
  - "[[Python for Data Analysis (McKinney)]]"
  - "[[MIT 6.100L - Introduction to CS and Programming Using Python]]"
---

# Python Programming

> [!abstract]
> Review sheet for a professional developer: the Python 3.13 types, slicing rules, comprehensions and standard-library modules that scientific and sequence code uses every day, and the few semantics that differ from other languages.

## Definition

**Python** is a general-purpose language with high-level built-in data structures, dynamic typing and an interpreted execution model; **CPython** is its reference implementation, distributed by the Python Software Foundation.[^tut][^new] Python 3.13 (released 7 October 2024) is the version the [[Bioinformatics Lab]] targets; its headline changes are a new interactive interpreter, an experimental free-threaded build without the global interpreter lock (PEP 703) and an experimental JIT compiler (PEP 744).[^new]

## Why it matters

- It is the language of the Lab projects and of introductory programming in computational biology degrees (see [[Programming]]); [[Biopython]], NumPy and pandas sit on top of the built-ins below ([[Scientific Python Ecosystem]]).
- Sequence work is string work: slicing, counting and hashing k-mers map directly onto `str`, `Counter` and `set` ([[String]], [[Hash Table]], [[K-mer]]).
- The semantics that cause real bugs in analyses (integer versus true division, banker's rounding, float equality, aliasing) are few and worth knowing cold.

## Core (L1)

### Built-in types

| Type | Mutable | Literal | Typical use in sequence code |
|---|---|---|---|
| `int` | no | `248_956`, `0b1011` | positions, counts; **unlimited precision**[^types] |
| `float` | no | `0.5`, `1e-9` | frequencies, p-values; a C `double`[^types] ([[Floating-Point Arithmetic]]) |
| `bool` | no | `True` | a subtype of `int`: `sum(b in "GC" for b in seq)` counts[^types] |
| `str` | no | `"ACGT"` | sequences, identifiers: immutable Unicode code points[^types] |
| `bytes` | no | `b"ACGT"` | raw file content, packed data ([[File Input and Output]]) |
| `list` | yes | `[1, 2]` | ordered collections you append to |
| `tuple` | no | `(chrom, pos)` | fixed records, dictionary keys[^mck3][^l9] |
| `dict` | yes | `{"ATG": "M"}` | lookup tables; **insertion order is guaranteed** since 3.7[^types] |
| `set`, `frozenset` | yes, no | `{"AT", "GC"}` | membership, deduplication in $O(1)$ average ([[Hash Table]]) |

Mutability and identity are the subject of [[Python Object Model]]; read it before writing any code that shares lists between functions.

### Syntax worth having in muscle memory

- **Slices** `s[i:j]` are 0-based and half-open: length $j - i$, and `s[:k] + s[k:] == s`. This is the BED convention; a 1-based inclusive region $[a, b]$ (GFF, VCF) is `s[a - 1:b]` ([[Genomic Coordinate System]]).
- **Comprehensions**: list `[f(x) for x in xs if p(x)]`, set `{...}`, dict `{k: v for ...}`, and generator expressions `(...)` that produce items lazily ([[Iterator]]).[^mck3]
- **Unpacking**: `name, seq, qual = fields`, `first, *rest = items`, `for i, base in enumerate(seq)`, `for a, b in zip(r1, r2, strict=True)`.
- **f-strings** with format specifications: `f"{gc:.3f}"`, `f"{n:>10,}"`.
- **Functions**: defaults, keyword-only parameters after `*`, `*args` and `**kwargs`; annotate them ([[Type Hint]]).
- **Structural pattern matching** (`match`, Python 3.10+) dispatches on the shape of a parsed record: `case [name, seq, qual] if len(seq) == len(qual):`.
- **Exceptions**: raise a subclass of `ValueError` for malformed input, chain with `raise ... from err`, and catch only what you can handle ([[Defensive Programming]]).
- **Modules**: one file is a module, a directory of modules a package; guard script code with `if __name__ == "__main__":` ([[Python Packaging]], [[Command-Line Interface]]).

### Standard library map

| Need | Module | Vault note |
|---|---|---|
| counting, grouping, queues | `collections` (`Counter`, `defaultdict`, `deque`) | [[Hash Table]], [[Queue]] |
| lazy pipelines | `itertools` | [[Iterator]] |
| higher-order tools, caching | `functools`, `operator` | [[Functional Programming]] |
| paths, files, compression | `pathlib`, `io`, `gzip`, `csv`, `json` | [[File Input and Output]], [[Delimited Text Format]] |
| headers and identifiers | `re` | [[Regular Expression]] |
| command-line tools | `argparse`, `sys`, `subprocess` | [[Command-Line Interface]] |
| domain objects | `dataclasses`, `typing`, `enum` | [[Object-Oriented Programming]], [[Value Object]] |
| packed numbers | `array`, `struct` | [[Python Object Model]] |
| numerics | `math`, `statistics`, `random` | [[Random Number Generation]] |
| parallelism | `concurrent.futures`, `multiprocessing` | [[Functional Programming]], [[Parallel Computing]] |

## Computational representation

```python
import math
from collections import Counter

seq = "ATGGCGTTAGCCGATAA"                      # invented toy sequence
print(seq[0:3], seq[-3:], len(seq), seq[3:9])  # 0-based, half-open slices
codons = [seq[i:i + 3] for i in range(0, len(seq) - 2, 3)]
print(codons)
gc = sum(base in "GC" for base in seq) / len(seq)   # True counts as 1
print(f"GC = {gc:.3f}")
counts = Counter(seq)
print(counts.most_common(2), sorted(counts))
lengths = {"contig_2": 15_210, "contig_1": 1_204_331}   # invented; dicts keep insertion order
for name, n in lengths.items():
    print(f"{name:>9}: {n:>10,} bp")
print(7 / 2, 7 // 2, -7 // 2, 2 ** 70, round(2.5), round(3.5))
print(0.1 + 0.2 == 0.3, math.isclose(0.1 + 0.2, 0.3))
```

```text
ATG TAA 17 GCGTTA
['ATG', 'GCG', 'TTA', 'GCC', 'GAT']
GC = 0.471
[('A', 5), ('G', 5)] ['A', 'C', 'G', 'T']
 contig_2:     15,210 bp
 contig_1:  1,204,331 bp
3.5 3 -4 1180591620717411303424 2 4
False True
```

The incomplete last codon (`AA`) is dropped by the `range` bound; `-7 // 2` floors to $-4$; `round` sends ties to the even neighbour.[^funcs]

## Worked example

> [!example] Codon usage of a toy coding sequence (invented)
> `cds = "ATGGCTGCTAAAGCTTAA"`.
> 1. Codons with a generator expression: `Counter(cds[i:i + 3] for i in range(0, len(cds) - 2, 3))` gives `Counter({'GCT': 3, 'ATG': 1, 'AAA': 1, 'TAA': 1})`.
> 2. Total: `sum(counts.values())` = 6 codons.
> 3. Frequencies with a dict comprehension over the sorted items: `{'AAA': 0.167, 'ATG': 0.167, 'GCT': 0.5, 'TAA': 0.167}`.
> 4. Three lines, no index bookkeeping: the same pattern scales to a genome's coding sequences ([[Codon Usage Bias]]).

## Common misconceptions

> [!warning] "`/` on integers truncates"
> That was Python 2. In Python 3, `/` is true division (`7 / 2 == 3.5`) and `//` is floor division, which rounds toward $-\infty$ (`-7 // 2 == -4`), not toward zero.[^types]

> [!warning] "`round` rounds halves up"
> `round(2.5) == 2`: ties go to the even neighbour. Use `decimal` or an explicit rule when a report must round halves up.[^funcs]

> [!warning] "Compare floats with `==`"
> `0.1 + 0.2 == 0.3` is `False` because neither value is exactly representable in binary. Compare with `math.isclose` and a tolerance chosen for the quantity ([[Floating-Point Arithmetic]]).

## Exercises

> [!question] Exercise 1 (L1)
> A GFF feature spans positions 5 to 10 (1-based, inclusive) of `ACGTTGCAAGGCTTAC` (invented). Write the slice and its length.

> [!success]- Solution
> `genome[4:10]` gives `TGCAAG`, length $10 - 5 + 1 = 6$: subtract 1 from the start only, because the slice end is already exclusive.

> [!question] Exercise 2 (L2, Python)
> Group a tab-separated sample sheet (columns `sample`, `lane`, `fastq`) into a dictionary from sample to its sorted FASTQ files, using only the standard library.

> [!success]- Solution
> ```python
> import csv, io
> from collections import defaultdict
>
> sheet = "sample\tlane\tfastq\nS2\tL001\tS2_L001.fq.gz\nS1\tL002\tS1_L002.fq.gz\nS1\tL001\tS1_L001.fq.gz\n"  # invented
> files = defaultdict(list)
> for row in csv.DictReader(io.StringIO(sheet), delimiter="\t"):
>     files[row["sample"]].append(row["fastq"])
> print({s: sorted(fs) for s, fs in sorted(files.items())})
> # {'S1': ['S1_L001.fq.gz', 'S1_L002.fq.gz'], 'S2': ['S2_L001.fq.gz']}
> ```
> `defaultdict(list)` removes the "key missing" branch; with a real file, pass `open(path, newline="", encoding="utf-8")` ([[File Input and Output]]).

> [!question] Exercise 3 (L2)
> A script keeps 10,000 wanted read identifiers in a list and tests `if name in wanted` for every read. Why is it slow, and what is the one-line fix?

> [!success]- Solution
> Membership in a list scans it, $O(n)$ per test; in a `set` it is a hash lookup, $O(1)$ on average ([[Hash Table]]).[^mck3] Fix: `wanted = set(wanted)`. Measured with CPython 3.13 (1,000 queries, 10,000 identifiers, one run on one machine): about 120 ms with the list, 0.2 ms with the set.

## Mastery checklist

- [ ] 1 Recognized: I can list the built-in types with their mutability and the main standard-library modules.
- [ ] 2 Understood: I can explain half-open slicing, true versus floor division, banker's rounding and why `dict` order is reliable.
- [ ] 3 Practiced: I write comprehensions, `Counter` and `defaultdict` code and pattern matching without looking them up.
- [ ] 4 Applied: the parsing and counting code of [[01-dna-engine]] uses these idioms, checked with Ruff and pytest.
- [ ] 5 Explained: I can review a colleague's analysis script and point out the Python-specific pitfalls above.

## References

[^tut]: [[Python Documentation]], 3.13, "The Python Tutorial" (introduction) and Glossary ("CPython").
[^new]: [[Python Documentation]], "What's New in Python 3.13".
[^types]: [[Python Documentation]], 3.13, Library Reference, "Built-in Types": numeric types (unlimited-precision integers, floats as C doubles, `bool` as a subtype of `int`, `/` and `//`), text sequences, mapping types (insertion order guaranteed since 3.7).
[^funcs]: [[Python Documentation]], 3.13, Library Reference, "Built-in Functions": `round` rounds ties to the even choice.
[^mck3]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 3 "Built-In Data Structures, Functions, and Files": tuples, lists, dicts, sets, comprehensions, list versus set membership.
[^l9]: [[MIT 6.100L - Introduction to CS and Programming Using Python]], lecture 9 "Lambda Functions, Tuples, and Lists".
