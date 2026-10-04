---
aliases:
  - pytest documentation
tags:
  - type/source
  - domain/computer-science
  - level/L1
  - level/L2
kind: tool
tier: C
authors:
  - pytest-dev team
institution: pytest-dev
year:
edition:
url: "https://docs.pytest.org/en/stable/"
access: free
---

# pytest

> [!abstract]
> pytest is the de facto testing framework of the Python ecosystem; this note points to its official documentation.

## Why this source

pytest is the test runner of the [[Bioinformatics Lab]]. Its documentation is the reference for fixtures, parametrization and exception checks. Tier C: it documents a tool; the reasons to test come from [[Wilson 2014 - Best Practices for Scientific Computing]] and [[Research Software Engineering with Python (Irving)]].

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| "How to use fixtures" | A test requests a fixture by listing it as a parameter; built-in fixtures such as `request` (with `request.param` for parametrized fixtures) and `tmp_path` | [[Unit Testing]] |
| Parametrizing tests | `@pytest.mark.parametrize` runs one test function on several argument sets | [[Unit Testing]] |
| API reference, `pytest.raises` | Asserts that a block raises an exception; `match` is a regular expression tested with `re.search` against the string form of the exception | [[Unit Testing]], [[Defensive Programming]] |

Cited in [[Unit Testing]]. The test outputs shown in that note come from pytest 9.1.1 (Python 3.13).

## How to use it

- L1: read "Get started", then "How to use fixtures" and the parametrization page while writing the first tests of [[01-dna-engine]].
- L2: plugins for coverage and property-based testing ([[Property-Based Testing]]).

## Caveats

- Check the documentation version matching the installed pytest (`pytest --version`).
- Verified in this pass: the documentation URL and the fixture, parametrization and `pytest.raises` pages summarized above.
