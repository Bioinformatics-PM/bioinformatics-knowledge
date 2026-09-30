---
aliases:
  - Das and Dai 2007
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L1
  - level/L2
kind: paper
tier: A
authors:
  - Modan K. Das
  - Ho-Kwok Dai
journal: BMC Bioinformatics
year: 2007
url: "https://doi.org/10.1186/1471-2105-8-S7-S21"
access: free
---

# Das 2007 - A Survey of DNA Motif Finding Algorithms

> [!abstract]
> An open-access review that defines DNA sequence motifs and surveys the algorithms used to discover transcription factor binding sites.

## Why this source

A short, freely available review with a clear working definition of a DNA motif: a nucleic acid pattern of biological significance, such as a binding site for a regulatory protein, usually 5 to 20 bp long, that recurs in different genes or several times within a gene. It also names the special shapes of motifs (palindromic, spaced dyad) and organizes discovery methods, which makes it a good bridge from [[Sequence Motif]] to [[Motif Finding]].

## Coverage

Citation: Das MK, Dai HK. "A survey of DNA motif finding algorithms". *BMC Bioinformatics* 8(Suppl 7):S21 (2007). doi:10.1186/1471-2105-8-S7-S21. Free at PMC2099490.

| Part | Content | Vault notes |
|---|---|---|
| Background | Definition of a DNA motif; palindromic motifs (e.g. `CACGTG`) and spaced dyad (gapped) motifs | [[Sequence Motif]], [[Transcription Factor]] |
| Algorithms | Discovery from promoters of co-regulated genes (statistically over-represented motifs) and from orthologous sequences (phylogenetic footprinting) | [[Motif Finding]], [[Position Weight Matrix]] |

Cited in [[Sequence Motif]].

## How to use it

- L1: read the background section with [[Sequence Motif]].
- L2: use the survey of algorithms as a map before the detailed chapters on motif finding in [[Bioinformatics Algorithms (Compeau)]].

## Caveats

- 2007: predates deep-learning models of binding and high-throughput binding assays as routine data sources.
- Verified in this pass: citation metadata, the definition and the motif shapes; the per-algorithm details were not checked.
