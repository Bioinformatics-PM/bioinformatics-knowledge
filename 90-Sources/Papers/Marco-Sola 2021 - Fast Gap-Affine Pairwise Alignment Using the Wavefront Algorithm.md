---
aliases:
  - Marco-Sola 2021
  - WFA paper
  - Wavefront Alignment Algorithm
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L3
  - level/M1
kind: paper
tier: A
authors:
  - Santiago Marco-Sola
  - Juan Carlos Moure
  - Miquel Moreto
  - Antonio Espinosa
journal: Bioinformatics
year: 2021
url: "https://doi.org/10.1093/bioinformatics/btaa777"
access: free
---

# Marco-Sola 2021 - Fast Gap-Affine Pairwise Alignment Using the Wavefront Algorithm

> [!abstract]
> The wavefront alignment algorithm (WFA): an exact gap-affine pairwise aligner whose running time grows with the alignment score instead of the product of the sequence lengths, much faster than full dynamic programming on similar sequences.

## Why this source

Classical dynamic programming fills the whole $n \times m$ matrix even when two sequences are nearly identical. WFA computes the same optimal gap-affine alignment while exploiting the similar regions between the sequences: its time is $O(ns)$, with $n$ the read length and $s$ the alignment score (a penalty, small for similar sequences), and its memory $O(s^2)$. The authors report speed-ups of 20 to 300 times over other methods on short Illumina-like sequences and of 10 to 100 times on long noisy reads such as Oxford Nanopore reads. It shows that the textbook quadratic algorithms are the reference, not the end of the story.

## Coverage

Citation: Marco-Sola S, Moure JC, Moreto M, Espinosa A. "Fast gap-affine pairwise alignment using the wavefront algorithm". *Bioinformatics* 37(4):456-463 (2021; published online 11 September 2020). doi:10.1093/bioinformatics/btaa777. Free at PMC8355039.

| Part | Content | Vault notes |
|---|---|---|
| Problem | Exact pairwise alignment with gap-affine penalties | [[Needleman-Wunsch Algorithm]], [[Gotoh Algorithm]], [[Gap Penalty]] |
| Method | Exploits similar regions to avoid computing most of the matrix | [[Dynamic Programming]] |
| Results | $O(ns)$ time, $O(s^2)$ memory; speed-ups on short and long reads | [[Read Mapping]], [[Long-Read Alignment]] |

## How to use it

- L3: after [[Needleman-Wunsch Algorithm]] and [[Gotoh Algorithm]], read the introduction and the complexity analysis.
- M1: compare the running time of WFA and of full dynamic programming as the divergence between two sequences grows.

## Caveats

- Verified in this pass (web search): authors, title, journal, volume, issue, pages, DOI, online date, PMC record, the complexity statements and the reported speed-ups. The details of the method were not checked in the full text.
