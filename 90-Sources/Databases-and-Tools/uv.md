---
aliases:
  - uv package manager
  - Astral uv
tags:
  - type/source
  - domain/computer-science
  - level/L1
  - level/L2
kind: tool
tier: C
authors:
  - Astral
institution: Astral
year:
edition:
url: "https://docs.astral.sh/uv/"
access: free
---

# uv

> [!abstract]
> uv is a Python package and project manager by Astral that creates projects and virtual environments, resolves and locks dependencies, installs Python versions and builds packages; this note points to its official documentation.

## Why this source

uv is the project manager of the [[Bioinformatics Lab]]. Its documentation is the only authority on uv's own commands and on the `uv.lock` format. Tier C: it documents a tool and never backs a concept claim alone; the standards it implements are in [[Python Packaging User Guide]].

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| Concepts, "Structure and files" | `uv.lock` next to `pyproject.toml`: a universal (cross-platform) lockfile capturing the packages installed across Python markers (operating system, architecture, Python version); exact resolved versions, to be checked into version control; human-readable TOML managed by uv, not to be edited by hand, not usable by other tools; created or updated by `uv run`, `uv sync` and `uv lock`; the project environment in `.venv` | [[Dependency Management]] |
| Guide "Working on projects" | `uv init`, `uv add`, `uv run`, `uv sync`, `uv build` | [[Python Packaging]], [[Dependency Management]] |
| Concepts, "Resolution" | How uv resolves versions | [[Dependency Management]] |
| Guides on integrations | GitHub Actions, pre-commit | [[Continuous Integration]] |

Cited in [[Python Packaging]] and [[Dependency Management]]. The command outputs shown in those notes come from uv 0.8.17.

## How to use it

- L1: follow "Working on projects" when creating a Lab repository; read "Structure and files" before committing `uv.lock`.
- L2: read "Resolution" when a constraint conflict appears.

## Caveats

- uv evolves quickly (0.x versions): defaults such as the build backend chosen by `uv init` change between releases; check `uv --version` and the documentation of that version.
- Verified in this pass: the documentation URL and the content of "Structure and files" summarized above.
