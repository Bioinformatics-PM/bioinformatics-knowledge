---
aliases:
  - Spellman yeast cell cycle dataset
  - Yeast cell cycle microarray study
tags:
  - type/source
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Paul T. Spellman
  - Gavin Sherlock
  - Michael Q. Zhang
  - Vishwanath R. Iyer
  - Kirk Anders
  - Michael B. Eisen
  - Patrick O. Brown
  - David Botstein
  - Bruce Futcher
journal: Molecular Biology of the Cell
year: 1998
url: "https://pubmed.ncbi.nlm.nih.gov/9843569/"
access: free
---

# Spellman 1998 - Comprehensive Identification of Cell Cycle-Regulated Genes of the Yeast Saccharomyces cerevisiae

> [!abstract]
> A genome-wide microarray time course of synchronized yeast cultures that identified 800 genes whose transcript levels oscillate with the cell cycle.

## Why this source

One of the first genome-wide expression studies, and a classic dataset of bioinformatics. The authors synchronized yeast cultures by three independent methods (α-factor arrest, elutriation, and arrest of a *cdc15* temperature-sensitive mutant), measured expression over time with DNA microarrays, and used periodicity and correlation algorithms to identify 800 genes that meet an objective minimum criterion for cell cycle regulation. More than half of these genes respond to the G1 cyclin Cln3p or to the B-type cyclin Clb2p. It shows how a cell biology question (which genes are cell-cycle regulated) becomes a time-series analysis problem.

## Coverage

Citation: Spellman PT, Sherlock G, Zhang MQ, Iyer VR, Anders K, Eisen MB, Brown PO, Botstein D, Futcher B. "Comprehensive identification of cell cycle-regulated genes of the yeast *Saccharomyces cerevisiae* by microarray hybridization". *Molecular Biology of the Cell* 9(12):3273-3297 (1998). PMID 9843569. Free full text at PMC25624.

| Part | Content | Vault notes |
|---|---|---|
| Design | Microarray time courses of cultures synchronized by α-factor, elutriation and *cdc15* arrest | [[Microarray]], [[Cell Cycle]] |
| Analysis | Periodicity and correlation algorithms; 800 cell cycle-regulated genes | [[Cell Cycle]], [[Gene Expression]] |
| Regulation | Response of the periodic genes to the cyclins Cln3p and Clb2p | [[Cell Cycle]], [[Gene Regulation]] |

Cited in [[Cell Cycle]].

## How to use it

- L2: read the abstract and the description of the synchronization methods after the Core of [[Cell Cycle]].
- L3: reproduce the idea of a periodicity score on toy data (Exercise in [[Cell Cycle]]), then compare with the paper's criterion.

## Caveats

- Microarray technology of 1998: noisy, relative measurements; later RNA-seq studies and re-analyses revised the list of periodic genes.
- The threshold of 800 genes follows the authors' chosen criterion; other methods give different numbers.
- Verified in this pass (web search): authors, title, journal, volume, issue, pages, PMID, PMC record, the three synchronization methods, the count of 800 genes and the Cln3p and Clb2p result, all from the abstract.
