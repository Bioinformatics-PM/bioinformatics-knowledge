---
aliases:
  - Delta-delta Ct method
  - 2^-ddCt method
  - Livak and Schmittgen 2001
tags:
  - type/source
  - domain/biology
  - domain/bioinformatics
  - level/L2
kind: paper
tier: A
authors:
  - Kenneth J. Livak
  - Thomas D. Schmittgen
journal: Methods
year: 2001
url: "https://doi.org/10.1006/meth.2001.1262"
access: paid
---

# Livak 2001 - Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR

> [!abstract]
> "Analysis of relative gene expression data using real-time quantitative PCR and the 2^(-ΔΔCT) method": the derivation, assumptions and use of the standard formula for relative expression from qPCR threshold cycles.

## Why this source

Reverse transcription followed by quantitative PCR is the usual way to measure the expression of a few genes, and to validate RNA-seq results. This paper derives the 2^(-ΔΔCT) formula, which compares the threshold cycle (CT) of a target gene with that of a reference gene, in a treated sample relative to a calibrator sample, and states the assumptions it rests on (amplification efficiencies close to 100 % and similar for target and reference, and a reference gene whose expression does not change with the treatment). It also presents two variations of the method.

## Coverage

Citation: Livak KJ, Schmittgen TD. "Analysis of relative gene expression data using real-time quantitative PCR and the 2(-Delta Delta C(T)) method". *Methods* 25(4):402-408 (2001). PMID 11846609.

| Part | Content | Vault notes |
|---|---|---|
| Derivation | Exponential amplification, threshold cycle, the 2^(-ΔΔCT) formula | [[Quantitative Polymerase Chain Reaction]], [[Gene Expression]] |
| Assumptions | Efficiency near 100 %; stable reference (internal control) gene | [[Experimental Control]], [[Gene Expression]] |
| Variations | Two variants of the method for other designs | [[Quantitative Polymerase Chain Reaction]] |

Cited in [[Gene Expression]].

## How to use it

- L2: read the derivation and the assumptions; redo the qPCR exercise of [[Gene Expression]] with an efficiency below 100 % to see how the answer changes.
- Pair with the technique note [[Quantitative Polymerase Chain Reaction]] for the chemistry.

## Caveats

- The formula is only as good as its assumptions: check efficiencies with a dilution series and validate the reference gene.
- Metadata (authors, journal, volume, issue, pages, year, PMID) and the scope of the paper verified in this pass; the list of assumptions follows the paper as it is usually summarized, not a full-text check.
