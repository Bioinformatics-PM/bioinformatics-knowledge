---
aliases:
  - FASTQ format paper
  - The Sanger FASTQ file format for sequences with quality scores, and the Solexa/Illumina FASTQ variants
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L1
  - level/L2
kind: paper
tier: A
authors:
  - Peter J. A. Cock
  - Christopher J. Fields
  - Naohisa Goto
  - Michael L. Heuer
  - Peter M. Rice
journal: Nucleic Acids Research
year: 2010
url: "https://doi.org/10.1093/nar/gkp1137"
access: free
---

# Cock 2010 - The Sanger FASTQ File Format

> [!abstract]
> The reference description of FASTQ: the original Sanger format with Phred qualities encoded as ASCII characters with an offset of 33, the two incompatible Solexa/Illumina variants, and how to convert between them.

## Why this source

FASTQ became the common exchange format for sequencing reads without any formal definition, and existed in at least three incompatible variants. This paper, written by developers of five open-source toolkits (Biopython, BioPerl, BioRuby, BioJava and EMBOSS), records the conventions they agreed on and the public information available (such as the MAQ documentation). The GA4GH specification repository still points to it as the description of FASTQ.

## Coverage

Citation: Cock PJA, Fields CJ, Goto N, Heuer ML, Rice PM. "The Sanger FASTQ file format for sequences with quality scores, and the Solexa/Illumina FASTQ variants". *Nucleic Acids Research* 38(6):1767-1771 (2010). doi:10.1093/nar/gkp1137. PMID 20015970, free at PMC2847217.

| Part | Content | Vault notes |
|---|---|---|
| Origin | Format introduced at the Wellcome Trust Sanger Institute around 2000 (credited to Jim Mullikin) | [[FASTQ Format]] |
| Record layout | `@` title line, sequence, `+` line (title repetition optional), quality string of the same length; wrapping allowed but discouraged; quality lines may start with `@` or `+` | [[FASTQ Format]] |
| Sanger variant | Phred quality $Q = -10 \log_{10} p$, ASCII offset 33, range 0 to 93 | [[FASTQ Format]], [[Phred Quality Score]] |
| Solexa and Illumina 1.3+ variants | Solexa scores $-10 \log_{10}(p/(1-p))$ with offset 64 (-5 to 62); Illumina 1.3+ Phred with offset 64 (0 to 62); conversions | [[FASTQ Format]], [[Base Calling]] |

Cited in [[FASTQ Format]].

## How to use it

- L1: read the introduction and the section describing the Sanger format, with [[FASTQ Format]].
- L2: read the variants and conversion sections before handling old public datasets, and test your parser against the edge cases the paper describes (wrapped records, quality lines starting with `@`).

## Caveats

- Written before Illumina moved to the Sanger encoding (Illumina 1.8+ writes Phred+33, see [[Galaxy Training Network - Training Material]]); the offset-64 variants now mainly matter for archived data.
- Does not cover later platform conventions (read-name formats, long-read qualities).
- Verified in this pass: authors, journal, volume, issue, pages, DOI, PMID, abstract and the facts in the Coverage table (by search of the paper and its abstract; cross-checked with the Biopython `Bio.SeqIO.QualityIO` documentation by the first author).
