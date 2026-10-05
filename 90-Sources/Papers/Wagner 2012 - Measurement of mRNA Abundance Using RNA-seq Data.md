---
aliases:
  - TPM paper
  - RPKM is inconsistent among samples
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Günter P. Wagner
  - Koryu Kin
  - Vincent J. Lynch
journal: Theory in Biosciences
year: 2012
url: "https://doi.org/10.1007/s12064-012-0162-3"
access: paid
---

# Wagner 2012 - Measurement of mRNA Abundance Using RNA-seq Data

> [!abstract]
> "Measurement of mRNA abundance using RNA-seq data: RPKM measure is inconsistent among samples": a short paper showing that RPKM lacks a basic invariance property and advocating TPM, transcripts per million.

## Why this source

Expression units are definitions, and a definition can be wrong for its purpose. The authors show that RPKM does not respect an invariance property that a measure of relative molar RNA concentration should have (its average over all transcripts changes from sample to sample), and propose a modified measure, TPM, that removes the inconsistency. It is the standard reference for why TPM, not RPKM, is used to express within-sample proportions.

## Coverage

Citation: Wagner GP, Kin K, Lynch VJ. "Measurement of mRNA abundance using RNA-seq data: RPKM measure is inconsistent among samples". *Theory in Biosciences* 131(4):281-285 (2012).

| Part | Content | Vault notes |
|---|---|---|
| Problem | RPKM is not a consistent measure of relative abundance across samples | [[Count Normalization]], [[Gene Expression]] |
| Proposal | TPM: length-normalized counts rescaled to sum to one million | [[Gene Expression]], [[Transcript Quantification]] |

Cited in [[Gene Expression]].

## How to use it

- L2: read it with the units section of [[Gene Expression]] and redo the computation that shows TPM sums to a constant.
- L3: then read why neither RPKM nor TPM is suitable input for differential expression tests ([[Size Factor Estimation]]).

## Caveats

- Five pages, theoretical; it does not address composition effects between samples, which need other normalizations.
- Metadata (authors, title, journal, volume, issue, pages, year) and the main claim verified in this pass.
