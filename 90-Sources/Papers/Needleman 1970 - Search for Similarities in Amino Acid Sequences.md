---
aliases:
  - Needleman-Wunsch paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L2
kind: paper
tier: S
authors:
  - Saul B. Needleman
  - Christian D. Wunsch
journal: Journal of Molecular Biology
year: 1970
url: "https://doi.org/10.1016/0022-2836(70)90057-4"
access: paid
---

# Needleman 1970 - Search for Similarities in Amino Acid Sequences

> [!abstract]
> "A general method applicable to the search for similarities in the amino acid sequence of two proteins": the first dynamic-programming method for global alignment of two sequences.

## Why this source

It stated an explicit optimality criterion for an alignment and gave an efficient computer method to find it. The approach belongs to the class of algorithms now called dynamic programming, and every global aligner descends from it.

## Coverage

Citation: Needleman SB, Wunsch CD. *J Mol Biol* 48:443-453 (1970). doi:10.1016/0022-2836(70)90057-4

| Part | Content | Vault notes |
|---|---|---|
| Problem | Find the best global correspondence between two protein sequences | [[Sequence Alignment]] |
| Method | Fill a matrix of partial scores, trace back the optimal path | [[Dynamic Programming]], [[Needleman-Wunsch Algorithm]] |

## How to use it

- L2: read after implementing [[Needleman-Wunsch Algorithm]] from a textbook; note how the original formulation differs from today's textbook version (gap penalties, scoring).
- Pair with [[Smith 1981 - Identification of Common Molecular Subsequences]] for the local variant.

## Caveats

- The original scoring and gap treatment differ from the modern formulation with linear or affine gap costs.
- Open-access status of the publisher PDF not verified.
