---
aliases:
  - Smith-Waterman paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L2
kind: paper
tier: S
authors:
  - Temple F. Smith
  - Michael S. Waterman
journal: Journal of Molecular Biology
year: 1981
url: "https://doi.org/10.1016/0022-2836(81)90087-5"
access: paid
---

# Smith 1981 - Identification of Common Molecular Subsequences

> [!abstract]
> The three-page letter defining the local alignment algorithm: find the pair of segments, one from each sequence, with maximal similarity.

## Why this source

It put the search for maximally similar segments on a rigorous basis with an efficient, simply programmed algorithm that allows insertions and deletions of arbitrary length. The Smith-Waterman algorithm remains the exact reference for local alignment that heuristics such as [[BLAST]] approximate.

## Coverage

Citation: Smith TF, Waterman MS. *J Mol Biol* 147:195-197 (1981). doi:10.1016/0022-2836(81)90087-5. PubMed 7265238.

| Part | Content | Vault notes |
|---|---|---|
| Problem | Best-matching pair of subsequences between two long sequences | [[Sequence Alignment]] |
| Method | Dynamic programming with scores floored at zero, traceback from the maximum cell | [[Dynamic Programming]], [[Smith-Waterman Algorithm]] |
| Gaps | Arbitrary-length insertions and deletions | [[Gap Penalty]] |

## How to use it

- L2: read after [[Needleman 1970 - Search for Similarities in Amino Acid Sequences]]; implement the local variant by changing the recurrence and traceback.

## Caveats

- Very short: the statistics of local alignment scores came later (Karlin and Altschul).
- Open-access status of the publisher PDF not verified.
