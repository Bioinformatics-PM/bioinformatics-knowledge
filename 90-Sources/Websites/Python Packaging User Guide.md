---
aliases:
  - PyPUG
  - packaging.python.org
tags:
  - type/source
  - domain/computer-science
  - level/L1
  - level/L2
kind: website
tier: A
authors:
  - Python Packaging Authority
institution: Python Packaging Authority (PyPA)
year:
edition:
url: "https://packaging.python.org/"
access: free
---

# Python Packaging User Guide

> [!abstract]
> The official guide and specification collection for packaging, distributing and installing Python projects, maintained by the Python Packaging Authority.

## Why this source

Packaging tools change fast (setuptools, hatchling, flit, uv), but they implement shared standards. This guide hosts those standards (the `pyproject.toml` format, version and dependency specifiers, entry points) next to tutorials and "discussions" that explain design choices. It is the tool-neutral reference against which tool documentation such as [[uv]] is read.

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| Guide "Writing your pyproject.toml" | The `[build-system]` table (build backend and build dependencies, examples for setuptools, hatchling, flit-core, pdm-backend and uv_build), the `[project]` metadata table, `[project.scripts]` (console-scripts entry points) | [[Python Packaging]] |
| Discussion "src layout vs flat layout" | Import packages at the root (flat) or in `src/`; the src layout prevents accidental use of the in-development copy and requires installing the project to run it | [[Python Packaging]] |
| Discussion "install_requires vs requirements files" | Abstract requirements (names and version ranges a project minimally needs) versus concrete, exhaustive pinned lists for repeatable installs of a whole environment | [[Dependency Management]] |
| Specifications | `pyproject.toml` specification (from PEP 621), version specifiers (compatible release `~=`), dependency specifiers, entry points | [[Python Packaging]], [[Dependency Management]] |
| Glossary | Distribution package, import package, virtual environment, wheel | [[Python Packaging]], [[Dependency Management]] |

Cited in [[Python Packaging]] and [[Dependency Management]].

## How to use it

- L1: read "Writing your pyproject.toml" and the src-layout discussion while creating [[01-dna-engine]].
- L2: read the version-specifier specification before writing constraints for [[bio-core]], and the install_requires discussion before publishing a library ([[Software Release]]).

## Caveats

- A living site without editions: pages change with new standards; note the date when you rely on a detail.
- Tool-neutral by design: commands of a given tool (uv, pip) are documented by that tool.
- Verified in this pass: the guide pages and specifications listed above, the compatible-release semantics (`~=3.1` means `>= 3.1, == 3.*`), and the abstract versus concrete distinction.
