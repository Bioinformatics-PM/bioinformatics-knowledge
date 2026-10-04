---
aliases:
  - NumPy docstring standard
  - numpydoc docstring guide
tags:
  - type/source
  - domain/computer-science
  - level/L1
  - level/L2
kind: website
tier: A
authors:
  - numpydoc maintainers (NumPy project)
institution: NumPy project
year:
edition:
url: "https://numpydoc.readthedocs.io/en/latest/format.html"
access: free
---

# numpydoc Style Guide

> [!abstract]
> The specification of NumPy-style docstrings: which sections a docstring has, in which order, and how each is written, used across the scientific Python ecosystem.

## Why this source

NumPy, SciPy, pandas and many bioinformatics libraries document their functions in this format, so learning it once makes their reference pages readable and lets your own docstrings render with the same tools. It is the normative description of the format (earlier versions were titled "numpydoc docstring guide").

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| Sections | Short summary (one line, without the function name or variable names); extended summary (functionality, not implementation or theory); Parameters; Returns; Raises (only non-obvious or likely errors); See Also; Notes (for example the algorithm); Examples (doctest format, to illustrate usage, very strongly encouraged) | [[Software Documentation]] |
| Example page | A complete example module | [[Software Documentation]] |

Cited in [[Software Documentation]].

## How to use it

- L1: copy the section order for every public function of [[01-dna-engine]].
- L2: render the docstrings into API pages with Sphinx and the numpydoc extension.

## Caveats

- A living page; versioned copies exist for each numpydoc release.
- Verified in this pass: URL, page title, and the content of the sections listed above.
