---
aliases:
  - ChIP-Seq paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L3
kind: paper
tier: S
authors:
  - David S. Johnson
  - Ali Mortazavi
  - Richard M. Myers
  - Barbara Wold
journal: Science
year: 2007
url: "https://doi.org/10.1126/science.1141319"
access: paid
---

# Johnson 2007 - Genome-Wide Mapping of in Vivo Protein-DNA Interactions

> [!abstract]
> The paper that introduced ChIP-seq, chromatin immunoprecipitation followed by direct high-throughput sequencing, and used it to map the binding sites of the repressor NRSF (REST) across the human genome.

## Why this source

ChIP-seq made the in vivo binding of a transcription factor a genome-wide sequencing measurement, with enough resolution to find the bound motif inside each peak. Its logic (enrich protein-bound DNA, sequence it, call peaks, search motifs) is the template of most regulatory genomics pipelines.

## Coverage

Citation: Johnson DS, Mortazavi A, Myers RM, Wold B. "Genome-wide mapping of in vivo protein-DNA interactions". *Science* 316(5830):1497-1502 (8 June 2007). doi:10.1126/science.1141319. PMID 17540862.

| Part | Content | Vault notes |
|---|---|---|
| Method | Chromatin immunoprecipitation followed by ultrahigh-throughput DNA sequencing | [[ChIP-Seq]] |
| Result | In vivo binding of NRSF (REST) at 1,946 locations in the human genome, with binding positions resolved to about ±50 bp | [[Transcription Factor]] |
| Motifs | The resolution helped find the canonical NRSF motif and noncanonical motifs | [[Sequence Motif]], [[Motif Finding]] |
| Accuracy | High sensitivity and specificity (ROC area ≥ 0.96) | [[Precision and Recall]] |

Cited in [[Transcription Factor]].

## How to use it

- L3: read after [[Transcription Factor]], as the bridge from motifs to in vivo binding data ([[ChIP-Seq]]).

## Caveats

- 2007 sequencing (short reads, one factor, one cell type); protocols, depth and peak callers have changed since.
- Verified in this pass: authors, title, journal, volume, issue, pages, date, DOI, PMID and the abstract findings.
