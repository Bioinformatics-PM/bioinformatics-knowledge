---
aliases: []
tags:
  - type/source
  - domain/biology
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Stephen J. Freeland
  - Laurence D. Hurst
journal: Journal of Molecular Evolution
year: 1998
url: "https://doi.org/10.1007/PL00006381"
access: paid
---

# Freeland 1998 - The Genetic Code Is One in a Million

> [!abstract]
> A simulation study comparing the standard genetic code with a million random alternative codes, finding it exceptionally good at limiting the effect of errors.

## Why this source

It gives a quantitative answer to "is the code a frozen accident?". The authors generated a million random codes with the same block structure and measured how much each one changes amino acid properties when a codon is misread or mutated. With a weighting that reflects realistic error patterns, about one random code in a million did better than the natural one. It is the standard reference for the error-minimization hypothesis.

## Coverage

Citation: Freeland SJ, Hurst LD. "The genetic code is one in a million". *Journal of Molecular Evolution* 47(3):238-248 (1998). doi:10.1007/PL00006381.

| Part | Content | Vault notes |
|---|---|---|
| Method | Random alternative codes scored by the cost of single-base errors | [[Genetic Code]], [[Codon]] |
| Error model | Weighting of transitions, transversions and codon positions | [[Mutation]] |
| Result and interpretation | The standard code is near-optimal for error minimization | [[Molecular Evolution]] |

Cited in [[Genetic Code]].

## How to use it

- L2: read the introduction and results after the degeneracy section of [[Genetic Code]].
- L3: reimplement a small version: shuffle amino acid assignments between codon blocks, score each code with a simple property (for example hydrophobicity), and compare with the standard table.

## Caveats

- The result depends on the chosen amino acid property, the error weights and the space of alternative codes; other choices give less extreme ranks.
- Error minimization is one hypothesis for the code's structure, alongside historical and stereochemical ones.
- Metadata (authors, journal, volume, issue, pages, DOI) verified in this pass.
