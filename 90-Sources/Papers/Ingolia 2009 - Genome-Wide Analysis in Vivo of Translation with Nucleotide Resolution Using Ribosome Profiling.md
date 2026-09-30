---
aliases:
  - Ribosome profiling paper
  - Ribo-seq
tags:
  - type/source
  - domain/biology
  - domain/bioinformatics
  - level/L3
kind: paper
tier: S
authors:
  - Nicholas T. Ingolia
  - Sina Ghaemmaghami
  - John R. S. Newman
  - Jonathan S. Weissman
journal: Science
year: 2009
url: "https://doi.org/10.1126/science.1168978"
access: paid
---

# Ingolia 2009 - Genome-Wide Analysis in Vivo of Translation with Nucleotide Resolution Using Ribosome Profiling

> [!abstract]
> The paper that introduced ribosome profiling: deep sequencing of the mRNA fragments protected by ribosomes, which maps translation genome-wide with subcodon resolution.

## Why this source

Sequencing ribosome-protected fragments tells, for every mRNA, where ribosomes sit and how many there are, so it measures the translation layer of [[Gene Expression]] with the same counting logic as [[RNA Sequencing]]. The authors applied it to budding yeast in rich medium and under starvation.

## Coverage

Citation: Ingolia NT, Ghaemmaghami S, Newman JRS, Weissman JS. "Genome-wide analysis in vivo of translation with nucleotide resolution using ribosome profiling". *Science* 324(5924):218-223 (10 April 2009). PMID 19213877.

| Part | Content | Vault notes |
|---|---|---|
| Method | Nuclease digestion, isolation and deep sequencing of ribosome-protected mRNA fragments | [[Ribosome]], [[Next-Generation Sequencing]] |
| Resolution | Footprint positions map ribosomes with subcodon resolution | [[Ribosome]], [[Reading Frame]] |
| Application | Translation in yeast under rich and starvation conditions | [[Gene Expression]], [[Translation]] |

Cited in [[Ribosome]] and [[Gene Expression]].

## How to use it

- L3: read the abstract and the first figure after [[Ribosome]]; then redo the toy footprint mapping of the Ribosome note.
- M1: with a public dataset, compute ribosome density per coding sequence and compare with mRNA levels.

## Caveats

- The protocol has been adapted since 2009; check the methods of each dataset before comparing studies.
- Metadata (authors, journal, volume, issue, pages, date, PMID) and the abstract content verified in this pass.
