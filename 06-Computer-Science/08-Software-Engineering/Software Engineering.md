---
aliases:
  - Research Software Engineering Practices
  - Génie logiciel
tags:
  - type/moc
  - domain/computer-science
  - domain/scientific-practice
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Programming]]"
projects:
  - "[[01-dna-engine]]"
  - "[[05-sequence-search]]"
  - "[[10-genomic-pipeline]]"
  - "[[Bioinformatics Lab]]"
sources:
  - "[[Biopython]]"
  - "[[ISCB - Bioinformatics Core Competencies]]"
  - "[[MIT - The Missing Semester of Your CS Education]]"
  - "[[MIT 6.100L - Introduction to CS and Programming Using Python]]"
---

# Software Engineering

> [!abstract]
> Engineering practices for research software in Python: version control, packaging and dependency management with uv, testing numerical and stochastic code, property-based testing, benchmarking, continuous integration, and releasing and sustaining scientific tools.

## Why it matters for bioinformatics

A bug in scientific software does not crash: it returns a plausible wrong number, and the error travels into a paper. Numerical code needs tests with tolerances and invariants rather than exact expected strings; a pipeline needs pinned dependencies to give the same result next year; a published tool needs a version, a license and a citation. The [[Bioinformatics Lab]] makes these practices mandatory from the first project (uv, Ruff, pytest, mypy, Hypothesis, GitHub Actions, a benchmarks folder), and the [[ISCB - Bioinformatics Core Competencies|ISCB core competencies]] frame bioinformatics training by what a practitioner must be able to do, which is the standard this syllabus aims at.[^iscb]

## Before you start

- [[Programming]]: [[Python Programming]], [[Type Hint]], [[Value Object]].
- [[Computer Systems]]: [[Unix Shell]], studied in parallel.

## Learning path

> [!tip] Review only
> As a professional developer, treat [[Version Control]], [[Static Analysis]] and [[Continuous Integration]] as review: an evening each to learn the Lab's conventions. Invest in what is specific to science: [[Numerical Testing]], [[Property-Based Testing]], [[Benchmarking]], [[Python Packaging]] with uv, and [[Software Release]] with a citable DOI.

### Stage 1 - Foundations (L1)

1. [[Version Control]] (L1): review only: Git branches, commits and pull requests; keep data and large binaries out of the repository.
2. [[Static Analysis]] (L1): review only: lint and format with Ruff and type-check with mypy, locally and in CI.
3. [[Unit Testing]] (L1): test small functions with pytest (fixtures, parametrization) on tiny hand-checked biological cases and edge cases (empty sequence, ambiguous bases, lowercase soft-masking).
4. [[Defensive Programming]] (L1): validate inputs at boundaries and fail fast with clear errors, so that invalid data never yields a plausible-looking result.
5. [[Software Documentation]] (L1): write NumPy-style docstrings, a README with the Lab's standard sections, and API documentation generated from code.
6. [[Python Packaging]] (L1): structure a `src`-layout package with `pyproject.toml`, a build backend and entry points, and manage it with uv.
7. [[Dependency Management]] (L1): declare Python dependencies with version constraints, resolve and lock them (`uv.lock`), and understand transitive dependencies and virtual environments.

### Stage 2 - Core (L2)

8. [[Numerical Testing]] (L2): test floating-point results with tolerances, against reference implementations and analytical cases, and test stochastic code with fixed seeds and statistical checks.
9. [[Property-Based Testing]] (L2): state invariants (reverse complement is an involution, edit distance is a metric) and let Hypothesis generate inputs and shrink counterexamples.
10. [[Benchmarking]] (L2): measure the runtime and memory of your own code reproducibly (warm-up, repetitions, variance), plot scaling on log-log axes, and track performance regressions.
11. [[Continuous Integration]] (L2): review only: run tests, linters and type checks on every push with GitHub Actions, using small bundled test datasets.
12. [[Layered Architecture]] (L2): keep scientific logic in libraries and out of interfaces (interface, domain and algorithm layers), as the Lab rules require.
13. [[Software Release]] (L2): version with semantic versioning, keep a changelog, publish to PyPI or Bioconda, and archive each release with a DOI and a citation file.

### Stage 3 - Advanced (L3)

14. [[Research Software]] (L3): apply the FAIR principles to research software, plan maintenance beyond the paper, and recognize the research software engineer's role in a group.

## Uses from other domains

- [[Reproducibility]] ([[Scientific Practice]]): the scientific goal that testing, pinning and releasing serve; [[Software Environment Management|Computational Environment]] extends [[Dependency Management]] to the whole software stack.
- [[Software Environment Management]] ([[Bioinformatics Engineering]]): conda and Bioconda environments for the non-Python tools of the field.
- [[Software License]] ([[Research Data Management]]): choosing a license before the first [[Software Release]].
- [[Pipeline Testing]] and [[Bioinformatics Tool Benchmarking]] ([[Bioinformatics Engineering]]): testing and benchmarking at the scale of whole workflows and of competing tools.
- [[Workflow Management System]] ([[Bioinformatics Engineering]]): where tested tools are assembled into pipelines.
- [[Container]] ([[Computer Systems]]): freezing the whole environment, beyond Python dependencies.
- [[Performance Profiling]] and [[Random Number Generation]] ([[Scientific Computing]]): what to measure before optimizing, and how to seed stochastic tests.
- [[Reverse Complement]] and [[Edit Distance]]: first targets for property-based tests.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT - The Missing Semester of Your CS Education]] | MIT | L1 | 2026 lectures on version control and Git, debugging and profiling, packaging and shipping code, code quality[^missing] |
| [[MIT 6.100L - Introduction to CS and Programming Using Python]] | MIT | L1 | Review only: testing and debugging as part of the introductory course[^mit6100l] |

## Reference books

- [[Research Software Engineering with Python (Irving)]]: packaging, testing, continuous integration and publishing, applied to a scientific Python project.
- [[Biopython]] (tool): once a concept is implemented by hand, use it as an independent oracle in the tests of [[01-dna-engine]] and [[02-sequence-translation]].[^biopython]

## Lab projects

- [[Bioinformatics Lab]]: the standard repository layout (`src`, `tests`, `benchmarks`, `pyproject.toml`, workflows) and the quality rules that apply to every project.
- [[01-dna-engine]]: [[Unit Testing]] and [[Property-Based Testing]] from day one.
- [[05-sequence-search]]: [[Benchmarking]] from 100 to 1M sequences.
- [[10-genomic-pipeline]]: pinned dependencies, logging and provenance.

## References

[^iscb]: [[ISCB - Bioinformatics Core Competencies]]: bioinformatics training framed by core competencies (what a trained person must be able to do) rather than by course lists.
[^biopython]: [[Biopython]]: recommended as a check of hand-written outputs in the tests of the first Lab projects, after the concept is implemented by hand.
[^missing]: [[MIT - The Missing Semester of Your CS Education]], 2026 edition: lectures "Debugging and Profiling", "Version Control and Git", "Packaging and Shipping Code" and "Code Quality".
[^mit6100l]: [[MIT 6.100L - Introduction to CS and Programming Using Python]]: testing and debugging are part of the introductory course, next to Python and complexity.
