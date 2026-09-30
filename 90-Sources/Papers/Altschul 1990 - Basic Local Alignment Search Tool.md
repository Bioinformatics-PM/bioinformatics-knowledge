---
aliases:
  - BLAST paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Stephen F. Altschul
  - Warren Gish
  - Webb Miller
  - Eugene W. Myers
  - David J. Lipman
journal: Journal of Molecular Biology
year: 1990
url: "https://doi.org/10.1016/S0022-2836(05)80360-2"
access: paid
---

# Altschul 1990 - Basic Local Alignment Search Tool

> [!abstract]
> The original BLAST paper: a fast heuristic for finding locally similar sequences in large databases, with a statistical measure of significance.

## Why this source

BLAST made database similarity search practical at genome scale and became one of the most used tools in biology. It shows the classic trade-off of bioinformatics: give up the guarantee of [[Smith-Waterman Algorithm|exact local alignment]] for orders-of-magnitude speed, and quantify the risk statistically.

## Coverage

Citation: Altschul SF, Gish W, Miller W, Myers EW, Lipman DJ. *J Mol Biol* 215(3):403-410 (1990). doi:10.1016/S0022-2836(05)80360-2

| Part | Content | Vault notes |
|---|---|---|
| Heuristic | Seed on short word matches scoring above a threshold, then extend them into high-scoring segment pairs | [[BLAST]], [[Seed and Extend\|Seed-and-Extend]], [[k-mer]] |
| Scoring | Substitution matrices for proteins | [[Substitution Matrix]] |
| Statistics | Significance of maximal segment pair scores | [[E-value]], [[Sequence Alignment\|Local Alignment]] |

## How to use it

- L2: read the method section when writing [[BLAST]]; run a BLAST search yourself alongside.
- L3: compare with gapped BLAST and BLAST+ (later papers) and with exact [[Smith 1981 - Identification of Common Molecular Subsequences|Smith-Waterman]].

## Caveats

- The 1990 version found ungapped alignments; gapped BLAST and PSI-BLAST came in later papers.
- Metadata cross-checked against multiple published bibliographic records; open-access status not verified.
