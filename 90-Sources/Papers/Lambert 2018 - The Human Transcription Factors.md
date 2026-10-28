---
aliases:
  - Human TF census
tags:
  - type/source
  - domain/biology
  - domain/bioinformatics
  - level/L3
  - level/M1
kind: paper
tier: A
authors:
  - Samuel A. Lambert
  - Arttu Jolma
  - Laura F. Campitelli
  - Pratyush K. Das
  - Yimeng Yin
  - Mihai Albu
  - Xiaoting Chen
  - Jussi Taipale
  - Timothy R. Hughes
  - Matthew T. Weirauch
journal: Cell
year: 2018
url: "https://doi.org/10.1016/j.cell.2018.01.029"
access: paid
---

# Lambert 2018 - The Human Transcription Factors

> [!abstract]
> A review built around a curated catalogue of more than 1,600 likely human transcription factors, with binding motifs known for about two-thirds of them.

## Why this source

It answers the first quantitative questions a bioinformatician asks about transcription factors: how many there are in the human genome, and for how many a DNA-binding motif is known. The catalogue is the usual starting list for motif scanning, enrichment analysis and regulatory network studies.

## Coverage

Citation: Lambert SA, Jolma A, Campitelli LF, Das PK, Yin Y, Albu M, Chen X, Taipale J, Hughes TR, Weirauch MT. "The Human Transcription Factors". *Cell* 172(4):650-665 (2018). doi:10.1016/j.cell.2018.01.029. Review.

| Part | Content | Vault notes |
|---|---|---|
| Catalogue | More than 1,600 likely human transcription factors | [[Transcription Factor]] |
| Motifs | Binding motifs for about two-thirds of them | [[Sequence Motif]], [[Position Weight Matrix]] |

Cited in [[Transcription Factor]].

## How to use it

- L3: read the introduction and the catalogue criteria after [[Transcription Factor]].
- M1: use the catalogue as the list of regulators in motif enrichment or network inference ([[Motif Finding]], [[Gene Regulatory Network Inference]]).

## Caveats

- Catalogues change as evidence accumulates: record the version used. The authors maintain a browsable "Human TFs" website at the University of Toronto.
- Verified in this pass: authors, title, journal, volume, issue, pages, DOI and the abstract figures. The exact count and the breakdown by DNA-binding domain family were not checked against the full text.
