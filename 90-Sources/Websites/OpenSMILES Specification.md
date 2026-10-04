---
aliases:
  - OpenSMILES
  - OpenSMILES spec
tags:
  - type/source
  - domain/chemistry
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
kind: website
tier: A
authors:
  - Craig A. James (editor)
institution: Blue Obelisk (OpenSMILES project)
url: "http://opensmiles.org/opensmiles.html"
access: free
---

# OpenSMILES Specification

> [!abstract]
> The community-maintained open standard of the SMILES line notation: a formal grammar of how atoms, bonds, branches, rings, charges and stereochemistry are written, and how the string is interpreted as a molecule.

## Why this source

SMILES was introduced in [[Weininger 1988 - SMILES, a Chemical Language and Information System]], but dialects diverged between programs. OpenSMILES, started in 2007 by Craig James within the Blue Obelisk open-source chemistry community, writes one open specification so that different toolkits read the same string the same way. It separates a **syntactic** specification (which characters are allowed, and where) from a **semantic** one (which molecule a valid string denotes).

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| Atoms | Organic-subset atoms written bare, with implicit hydrogens; bracket atoms with isotope, symbol, chirality, hydrogen count, charge and class | [[Skeletal Formula]] |
| Bonds, branches, rings | `-` single, `=` double, `#` triple, `:` aromatic; parentheses for branches; digits for ring closures | [[Skeletal Formula]], [[Functional Group]] |
| Aromaticity | Lowercase aromatic atoms | [[Aromaticity]] |
| Stereochemistry | Tetrahedral centers with `@` and `@@` (order of neighbors seen from the first neighbor); double-bond configuration with `/` and `\` | [[Stereochemistry]], [[Chirality]], [[Cis-Trans Isomerism]] |

## How to use it

- L1: the basic rules (atoms, bonds, branches, rings) are enough to read most database strings.
- L2-L3: the chirality section when writing or checking stereo-aware code; the grammar when writing a parser.

## Caveats

- Version number and date of the current document not verified here.
- Real toolkits still differ in edge cases (aromaticity perception, implicit hydrogens of aromatic atoms other than carbon): test strings across tools.
