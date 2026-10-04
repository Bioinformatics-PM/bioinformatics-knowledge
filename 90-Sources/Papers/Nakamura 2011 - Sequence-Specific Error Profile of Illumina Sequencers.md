---
aliases:
  - Sequence-specific error (SSE)
tags:
  - type/source
  - domain/bioinformatics
  - domain/scientific-practice
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Nakamura K
  - Oshima T
  - Morimoto T
  - et al.
journal: Nucleic Acids Research
year: 2011
url: "https://doi.org/10.1093/nar/gkr344"
access: free
---

# Nakamura 2011 - Sequence-Specific Error Profile of Illumina Sequencers

> [!abstract]
> The paper that showed Illumina Genome Analyzer reads contain sequence-specific errors: runs of miscalls that start at particular sequence contexts, mainly GGC motifs and inverted repeats.

## Why this source

Base-calling errors are often modelled as independent events with a probability given by the Phred quality. This paper documents a class of errors that is not independent of the sequence: the same context triggers miscalls in many reads. Such errors behave as systematic error, so extra depth does not remove them, which matters for variant calling, coverage-based methods and assembly.

## Coverage

Citation: Nakamura K, Oshima T, Morimoto T, et al. "Sequence-specific error profile of Illumina sequencers". *Nucleic Acids Research* 39:e90 (2011). doi:10.1093/nar/gkr344.

| Part | Content | Vault notes |
|---|---|---|
| Error profile | Sequence-specific starting positions of consecutive miscalls in mapped Genome Analyzer reads | [[Measurement Error]], [[Phred Quality Score]] |
| Triggers | Two main patterns: inverted repeats and GGC sequences | [[Measurement Error]] |
| Mechanism | Proposed sequence-specific interference with base elongation that favours dephasing | [[Next-Generation Sequencing]] |
| Consequences | A major cause of coverage variability and of bias in population-targeted methods such as RNA-seq and ChIP-seq | [[Sequencing Coverage]] |

## How to use it

- L2: read the abstract and the description of the miscall patterns, after [[Phred Quality Score]].
- L3: relate it to [[Base Quality Score Recalibration]] and to strand and context filters in [[Variant Calling]].

## Caveats

- Studied on the Illumina Genome Analyzer; later instruments and chemistries have different error profiles, so the specific motifs are a historical example of a general phenomenon.
- Verified in this pass: title, first three authors, journal, volume, article number e90, year, DOI, and the abstract's statements on triggers, mechanism and coverage bias. The journal is open access.
