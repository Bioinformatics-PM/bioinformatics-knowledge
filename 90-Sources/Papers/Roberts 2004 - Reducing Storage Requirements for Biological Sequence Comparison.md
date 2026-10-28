---
aliases:
  - Minimizers paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L3
kind: paper
tier: S
authors:
  - M. Roberts
  - W. Hayes
  - B. R. Hunt
  - S. M. Mount
  - J. A. Yorke
journal: Bioinformatics
year: 2004
url: "https://doi.org/10.1093/bioinformatics/bth408"
access: partial
---

# Roberts 2004 - Reducing Storage Requirements for Biological Sequence Comparison

> [!abstract]
> The paper that introduced minimizers to sequence comparison: instead of storing every k-mer seed of a sequence, store only the smallest k-mer of each window of consecutive k-mers, which shrinks seed catalogues while missing few matches.

## Why this source

Seed-and-extend comparison needs a catalogue of seeds that can be too large for one computer's memory. This paper proposes keeping only a small fraction of the seeds, the minimizers. Because the choice depends only on the window's content, two sequences that share an exact match spanning a whole window also share that window's minimizer (a consequence of the definition). Computing minimizers is a sliding-window minimum.

## Coverage

Citation: Roberts M, Hayes W, Hunt BR, Mount SM, Yorke JA. "Reducing storage requirements for biological sequence comparison". *Bioinformatics* 20(18):3363-3369 (2004). doi:10.1093/bioinformatics/bth408. PubMed 15256412.

| Part | Content | Vault notes |
|---|---|---|
| Problem | Seed catalogues too large for main memory in seed-and-extend comparison | [[Seed and Extend]], [[K-mer]] |
| Method | Minimizers: store only the minimal k-mer of each window of consecutive k-mers | [[Minimizer]] |
| Trade-off | Large speed-up and memory saving for a small loss of matches | [[Amortized Analysis]], [[Randomized Algorithm]] |

## How to use it

- L3: read the abstract and the definition of minimizers with [[Minimizer]]; implement the sliding-window minimum ([[Amortized Analysis]]) and measure the fraction of k-mers kept.

## Caveats

- Verified in this pass: citation metadata, PubMed identifier and the abstract's claims (seed catalogues too large for RAM; storing a small fraction of seeds, called minimizers; faster matching at the cost of a small fraction of missed matches).
- The density analysis of minimizer orders (random versus lexicographic) was developed in later work, not covered by this note.
- Full-text open access not verified.
