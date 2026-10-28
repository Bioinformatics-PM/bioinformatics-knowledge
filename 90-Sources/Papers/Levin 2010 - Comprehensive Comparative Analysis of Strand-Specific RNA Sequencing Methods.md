---
aliases:
  - Strand-specific RNA-seq benchmark
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L3
kind: paper
tier: A
authors:
  - Joshua Z. Levin
  - Moran Yassour
  - et al.
journal: Nature Methods
year: 2010
url: "https://doi.org/10.1038/nmeth.1491"
access: partial
---

# Levin 2010 - Comprehensive Comparative Analysis of Strand-Specific RNA Sequencing Methods

> [!abstract]
> A benchmark of seven strand-specific RNA-seq library protocols on the yeast transcriptome, which found dUTP second-strand marking and the Illumina RNA ligation method to perform best.

## Why this source

A standard RNA-seq library loses the strand from which each RNA was transcribed, because both cDNA strands end up sequenced. This paper explains what strand-specific protocols do about it and compares them with explicit criteria, which remain the right questions to ask of any library protocol.

## Coverage

Citation: Levin JZ, Yassour M, et al. "Comprehensive comparative analysis of strand-specific RNA sequencing methods". *Nature Methods* 7(9):709-715 (2010). doi:10.1038/nmeth.1491.

| Part | Content | Vault notes |
|---|---|---|
| Benchmark | Seven strand-specific protocols, published and new, compared on *Saccharomyces cerevisiae* RNA | [[RNA Sequencing]], [[Sequencing Library Preparation]] |
| Criteria | Strand specificity, library complexity, evenness and continuity of coverage, agreement with annotation, accuracy of expression profiling | [[Library Complexity]], [[Transcript Quantification]] |
| Result | dUTP second-strand marking and Illumina RNA ligation were the leading protocols | [[Reverse Transcription]] |

Cited in [[Reverse Transcription]].

## How to use it

- L3: read the comparison with [[Reverse Transcription]] and [[Sequencing Library Preparation]], before choosing the strandedness option of a read-counting tool.

## Caveats

- 2010 protocols and read lengths; commercial kits have changed since, so check the protocol of each dataset.
- The dUTP method was introduced earlier (Parkhomchuk et al., 2009, *Nucleic Acids Research*), mentioned here as reported in search results, not checked.
- An author manuscript is deposited in MIT DSpace; the journal version is paywalled.
- Verified in this pass: title, journal, volume, issue, pages, DOI, first authors and the main result, from the abstract and a Broad Institute news release; the full text was not read.
