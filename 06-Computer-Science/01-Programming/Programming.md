---
aliases:
  - Scientific Python
  - Programmation
tags:
  - type/moc
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
prerequisites: []
projects:
  - "[[01-dna-engine]]"
  - "[[02-sequence-translation]]"
  - "[[07-evolution-simulator]]"
  - "[[bio-core]]"
sources:
  - "[[Python for Data Analysis (McKinney)]]"
  - "[[MIT - Course 6-7 Computer Science and Molecular Biology]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[Université Paris-Saclay - Licence Double Diplôme Informatique Sciences de la Vie]]"
  - "[[MIT 6.100L - Introduction to CS and Programming Using Python]]"
  - "[[Coursera JHU - Genomic Data Science Specialization]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
---

# Programming

> [!abstract]
> Python as a scientific language: the object and memory model behind its performance, streaming large files, NumPy arrays and pandas data frames, typed domain models, notebooks versus packages, and enough R and C to read the tools of the field.

## Why it matters for bioinformatics

Python is where bioinformatics is prototyped, taught and glued together. Computational biology degrees require an introductory programming course: in Python at MIT, and at Paris-Saclay in the first year, next to an introduction to bioinformatics.[^mit67][^psisv][^cmu] What differs from web or backend work is the data: sequencing files larger than RAM that must be streamed, numeric arrays where Python loops are far too slow, and tables of samples by features. This syllabus skips what a professional developer knows and concentrates on those differences, which the [[Bioinformatics Lab]] stack (Python 3.13+, uv, Ruff, pytest, mypy, then NumPy, SciPy, pandas, Biopython) exercises from the first project.

## Before you start

No prerequisite: this syllabus assumes you already program professionally. Study it in parallel with [[Unix Shell]] ([[Computer Systems]]) and [[Unit Testing]] ([[Software Engineering]]).

## Learning path

> [!tip] Review only
> Items 1 to 3 are generic: skim them for Python-specific idioms in an evening, then spend the time on items 4 to 11 (streaming and arrays) and on Stage 2 (data frames, typing). Write the algorithm by hand once before reaching for a library, as the Lab rules require.

### Stage 1 - Foundations (L1)

1. [[Python Programming]] (L1): review only: syntax, built-in types, comprehensions, modules and the standard library of Python 3.13.
2. [[Object-Oriented Programming]] (L1): review only: classes, protocols and composition over inheritance, applied to biological domain objects.
3. [[Functional Programming]] (L1): review only: pure functions, higher-order functions and immutability, which make scientific code testable and easy to parallelize.
4. [[Python Object Model]] (L1): explain references, mutability, identity and boxed numbers, and why a list of a million floats costs far more memory and time than an array.
5. [[Iterator]] (L1): stream records lazily with generators and `itertools`, so that a sequencing file larger than RAM is processed in constant memory.
6. [[File Input and Output]] (L1): read and write text and binary files, handle encodings and gzip-compressed streams, with context managers and `pathlib`.
7. [[Regular Expression]] (L1): parse headers and identifiers with regular expressions, and know why they are the wrong tool for motifs with mismatches.
8. [[Command-Line Interface]] (L1): expose a tool with `argparse` or Typer, read stdin, write stdout, return exit codes, so it composes in Unix pipelines and workflows.
9. [[Scientific Python Ecosystem]] (L1): know what NumPy, SciPy, pandas, Matplotlib, scikit-learn and Biopython each provide, and which layer a problem belongs to.
10. [[Computational Notebook]] (L1): explore in Jupyter, avoid hidden state and out-of-order execution, and move stable code into a tested package.
11. [[N-Dimensional Array]] (L1): create and reshape NumPy arrays, choose dtypes, reduce along axes, and tell views from copies.

### Stage 2 - Core (L2)

12. [[Array Indexing]] (L2): select with slices, boolean masks and integer (fancy) indexing, and predict which operations return views.
13. [[Broadcasting]] (L2): apply the broadcasting rules to combine arrays of different shapes without loops or copies (all pairwise distances in one expression).
14. [[Data Frame]] (L2): load, type, clean and join tabular data with pandas or Polars, handle missing values, and keep one observation per row.
15. [[Split-Apply-Combine]] (L2): group, aggregate, transform and reshape (long versus wide) sample-by-feature tables.
16. [[Type Hint]] (L2): annotate functions and data (generics, `Protocol`, `numpy.typing`) and check them with mypy.
17. [[Value Object]] (L2): model a sequence, an interval or a variant as an immutable, validated, typed value (frozen dataclass), the domain-model pattern of the Lab.
18. [[R Programming]] (L2): read and run R and Bioconductor code (vectors, data frames, formulas), the language of the Bioconductor ecosystem taught in genomic data science courses.[^jhu][^ph525]

### Stage 3 - Advanced (L3)

19. [[Foreign Function Interface]] (L3): call compiled C, C++ or Rust libraries from Python (`ctypes`, pybind11, PyO3), as Python wrappers of htslib do.
20. [[C Programming]] (L3): read the C code of core tools (samtools, BWA, minimap2): pointers, manual memory management, structs, and why they are fast.

## Uses from other domains

- [[Vectorization]] ([[Scientific Computing]]): why array code is fast; read it right after [[N-Dimensional Array]].
- [[Data Visualization]] ([[Descriptive Statistics]]): plotting arrays and data frames with Matplotlib.
- [[Tidy Data]]: the table layout that [[Data Frame]] and [[Split-Apply-Combine]] assume.
- [[Computational Reproducibility]] ([[Reproducibility]]): why notebook code must end up in scripts and packages.
- [[FASTA Format]] and [[FASTQ Format]] ([[Bioinformatics Foundations]]): the first files you will stream and parse.
- [[Python Packaging]] and [[Unit Testing]] ([[Software Engineering]]): how the code of this syllabus is organized and checked.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 6.100L - Introduction to CS and Programming Using Python]] | MIT | L1 | Review only: computation and Python, basic algorithms and data structures, testing and debugging, complexity[^mit6100l] |
| [[Université Paris-Saclay - Licence Double Diplôme Informatique Sciences de la Vie]] | Université Paris-Saclay | L1 | Python programming in the first year, next to an introduction to bioinformatics[^psisv] |
| [[Coursera JHU - Genomic Data Science Specialization]] | Johns Hopkins University | L2 | Courses "Python for Genomic Data Science" (Python and notebooks) and "Bioconductor for Genomic Data Science" (R)[^jhu] |
| [[HarvardX PH525x - Data Analysis for the Life Sciences]] | Harvard University | L2 | PH525.1x "Statistics and R", then Bioconductor in PH525.5x: the R side of item 18[^ph525] |

## Reference books

- [[Python for Data Analysis (McKinney)]] (3rd ed.): NumPy arrays and vectorized computation, then pandas (loading, cleaning, merging, reshaping, group operations); the practical reference for Stage 1 items 9 to 11 and all of Stage 2.[^mckinney]

## Lab projects

- [[01-dna-engine]]: a typed, immutable sequence object ([[Value Object]]), a CLI and a Python API.
- [[02-sequence-translation]]: streaming over reading frames with [[Iterator|generators]].
- [[07-evolution-simulator]]: population state as [[N-Dimensional Array|arrays]], updated without Python loops.
- [[bio-core]]: the shared domain model, typed and validated.

## References

[^psisv]: [[Université Paris-Saclay - Licence Double Diplôme Informatique Sciences de la Vie]]: Python programming is a first-year unit, taught next to an introduction to bioinformatics.
[^mit67]: [[MIT - Course 6-7 Computer Science and Molecular Biology]]: 6.100A Introduction to Computer Science Programming in Python, then 6.1010 Fundamentals of Programming, in the required core.
[^cmu]: [[Carnegie Mellon University - BS Computational Biology]]: 02-120 Programming for Scientists (or 15-112) opens the computer science core.
[^mckinney]: [[Python for Data Analysis (McKinney)]], 3rd ed.: coverage of Python and Jupyter, NumPy (arrays and vectorized computation) and pandas (loading, cleaning, merging, reshaping, group operations).
[^mit6100l]: [[MIT 6.100L - Introduction to CS and Programming Using Python]]: MIT's required introductory programming course since 2022, successor of 6.0001.
[^jhu]: [[Coursera JHU - Genomic Data Science Specialization]]: the specialization pairs a Python course with a Bioconductor (R) course, next to command-line and statistics courses.
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]]: PH525.1x "Statistics and R" assumes no R background; PH525.5x introduces Bioconductor.
