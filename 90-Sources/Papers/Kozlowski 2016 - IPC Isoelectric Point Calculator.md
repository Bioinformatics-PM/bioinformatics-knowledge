---
aliases:
  - IPC
  - Isoelectric Point Calculator
tags:
  - type/source
  - domain/bioinformatics
  - domain/chemistry
  - level/L2
  - level/L3
  - level/M1
kind: paper
tier: A
authors:
  - Lukasz P. Kozlowski
journal: Biology Direct
year: 2016
url: "https://pubmed.ncbi.nlm.nih.gov/27769290/"
access: free
---

# Kozlowski 2016 - IPC Isoelectric Point Calculator

> [!abstract]
> A web service and program that predict the isoelectric point of proteins and peptides from sequence with several sets of pKa values, together with a benchmark showing how far such predictions are from measured values.

## Why this source

Sequence-based pI calculators all solve the same equation; they differ in the pKa values they plug in. This paper compares many published pKa sets on measured isoelectric points of proteins and peptides, adds two computationally optimized sets, and reports the size of the remaining errors. It is the reference to cite when a note states how accurate, or inaccurate, a predicted pI is.

## Coverage

Citation: Kozlowski LP. "IPC – Isoelectric Point Calculator". *Biology Direct* 11:55 (October 2016). doi:10.1186/s13062-016-0159-9. PubMed 27769290; preprint on bioRxiv (10.1101/049841).

| Part | Content | Vault notes |
|---|---|---|
| Method | pI predicted from sequence with a choice of pKa sets, including two new computationally optimized sets | [[Isoelectric Point]] |
| Benchmark | The optimized sets outperform previous methods by at least 14.9 % for proteins and 0.9 % for peptides; average errors of about 0.87 pH units for proteins and 0.25 for peptides; fewer large-error outliers | [[Isoelectric Point]] |
| Resources | Web service, standalone program, benchmark datasets and precalculated pI values for the PDB and several proteomes | [[Proteome]] |

Cited in [[Isoelectric Point]].

## How to use it

- **L2**: read the abstract after implementing a pI calculator ([[Isoelectric Point#Computational representation]]), to calibrate how much to trust its output.
- **M1**: study the benchmark design (measured pI datasets, many pKa sets, optimization of the pKa values) as an example of fitting a physical model's parameters to data.

## Caveats

- Verified in this pass: the citation (journal, volume, article number, year, DOI, PubMed record) and the abstract (pKa sets, two optimized sets, improvement margins, average errors, outliers, released datasets). Figures and tables in the body were not re-read.
- Benchmark errors refer to the paper's datasets of measured pI values; nothing guarantees the same accuracy on other proteins, for example modified ones.
