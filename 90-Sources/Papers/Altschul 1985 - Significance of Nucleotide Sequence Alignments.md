---
aliases:
  - Altschul-Erickson shuffle
  - Dinucleotide-preserving shuffle
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Stephen F. Altschul
  - Bruce W. Erickson
journal: Molecular Biology and Evolution
year: 1985
url: "https://doi.org/10.1093/oxfordjournals.molbev.a040370"
access: partial
---

# Altschul 1985 - Significance of Nucleotide Sequence Alignments

> [!abstract]
> The paper that made shuffled sequences a careful null model: alignment scores are judged against scores of randomly permuted sequences that keep the dinucleotide and codon usage of the originals.

## Why this source

The classic reference for permutation-based significance in sequence comparison, and for the point that *what a shuffle preserves* defines the null hypothesis.

## Coverage

Citation: Altschul SF, Erickson BW. "Significance of nucleotide sequence alignments: a method for random sequence permutation that conserves dinucleotide and codon usage". *Molecular Biology and Evolution* 2(6):526-538 (1985). doi:10.1093/oxfordjournals.molbev.a040370.

| Part | Content | Vault notes |
|---|---|---|
| Problem | Assessing alignment significance by comparison with randomly permuted sequences | [[Permutation]], [[Sequence Alignment]], [[Permutation Test]] |
| Method | Random permutations that conserve dinucleotide and codon usage | [[Permutation]], [[K-mer]] |

Cited in [[Permutation]].

## How to use it

- L2: read the introduction after [[Permutation]] to see why a plain shuffle can be the wrong null model.
- L3: implement a dinucleotide-preserving shuffle and compare score distributions.

## Caveats

- Precedes the extreme-value statistics used by BLAST ([[Altschul 1990 - Basic Local Alignment Search Tool]]); shuffling remains useful when analytic statistics do not apply.
- Verified in this pass: authors, title, journal, volume, issue, pages and DOI. Open-access status not verified (abstract on PubMed).
