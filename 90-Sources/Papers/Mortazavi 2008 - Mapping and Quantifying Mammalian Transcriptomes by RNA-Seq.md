---
aliases:
  - RPKM paper
  - Mortazavi et al. 2008
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Ali Mortazavi
  - Brian A. Williams
  - Kenneth McCue
  - Lorian Schaeffer
  - Barbara Wold
journal: Nature Methods
year: 2008
url: "https://doi.org/10.1038/nmeth.1226"
access: paid
---

# Mortazavi 2008 - Mapping and Quantifying Mammalian Transcriptomes by RNA-Seq

> [!abstract]
> One of the founding RNA-Seq papers: deep sequencing of mouse transcriptomes, counting how often each gene is represented, and the RPKM unit to compare genes and samples.

## Why this source

The authors sequenced poly(A)-selected RNA from adult mouse brain, liver and skeletal muscle (41 to 52 million mapped 25-bp reads per tissue) and recorded how frequently each gene was represented. This gives a digital measure of the presence and prevalence of transcripts, from known and previously unknown genes. To compare genes of different lengths and libraries of different depths they reported expression as **RPKM**, reads per kilobase of exon model per million mapped reads, a unit whose limits were discussed later ([[Wagner 2012 - Measurement of mRNA Abundance Using RNA-seq Data]]).

## Coverage

Citation: Mortazavi A, Williams BA, McCue K, Schaeffer L, Wold B. "Mapping and quantifying mammalian transcriptomes by RNA-Seq". *Nature Methods* 5(7):621-628 (July 2008). PMID 18516045.

| Part | Content | Vault notes |
|---|---|---|
| Data | Poly(A) RNA from three mouse tissues, tens of millions of short reads each | [[RNA Sequencing]], [[Transcriptome]] |
| Quantification | Read counts per gene as a digital expression measure; RPKM | [[Gene Expression]], [[Count Normalization]] |
| Discovery | Transcripts from previously unknown genes | [[Gene Annotation]] |

Cited in [[Gene Expression]].

## How to use it

- L2: read the abstract and the definition of RPKM with the units section of [[Gene Expression]].
- L3: compare with [[Wagner 2012 - Measurement of mRNA Abundance Using RNA-seq Data]] and explain why TPM replaced RPKM for within-sample proportions.

## Caveats

- 2008 technology (25-bp reads); read lengths, depth and quantification methods have changed completely.
- Metadata (authors, journal, volume, issue, pages, date, PMID) and the abstract figures verified in this pass; the RPKM definition is quoted as it is usually cited, not checked against the full text.
