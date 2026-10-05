---
aliases:
  - Karlin and Burge 1995
  - Genomic signature paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Samuel Karlin
  - Chris Burge
journal: Trends in Genetics
year: 1995
url: "https://doi.org/10.1016/S0168-9525(00)89076-9"
access: paid
---

# Karlin 1995 - Dinucleotide Relative Abundance Extremes

> [!abstract]
> The paper that introduced the "genomic signature": the profile of dinucleotide relative abundances, similar within a genome and different between genomes.

## Why this source

It showed that the frequency of each dinucleotide, compared with the expectation from the frequencies of its two bases, forms a profile characteristic of an organism: samples of DNA from the same genome have more similar profiles than samples from different organisms. This is the founding idea of comparing and classifying sequences by short-word composition, without alignment.

## Coverage

Citation: Karlin S, Burge C. "Dinucleotide relative abundance extremes: a genomic signature". *Trends in Genetics* 11(7):283-290 (1995). doi:10.1016/S0168-9525(00)89076-9. PubMed 7482779.

| Part | Content | Vault notes |
|---|---|---|
| Measure | Dinucleotide relative abundance (observed over expected from base composition) | [[K-mer]], [[GC Content]] |
| Result | The set of relative abundance values as a genomic signature, more similar within than between organisms | [[Alignment-Free Sequence Comparison]], [[Metagenomic Binning]] |

Cited in [[K-mer]].

## How to use it

- L2: after computing k-mer counts, compute the 16 dinucleotide relative abundances of two bacterial genomes and compare them.
- L3: read it as the starting point of alignment-free comparison and composition-based binning.

## Caveats

- A short review-style paper; later work extended signatures to longer words (for example tetranucleotides).
- Verified in this pass: citation metadata and the main concept; the table of organisms and values was not checked.
