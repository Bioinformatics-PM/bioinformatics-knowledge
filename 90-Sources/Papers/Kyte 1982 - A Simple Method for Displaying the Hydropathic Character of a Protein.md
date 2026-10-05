---
aliases:
  - Kyte-Doolittle
  - Kyte and Doolittle 1982
  - Kyte-Doolittle hydropathy scale
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L1
  - level/L2
kind: paper
tier: S
authors:
  - Jack Kyte
  - Russell F. Doolittle
journal: Journal of Molecular Biology
year: 1982
url: "https://pubmed.ncbi.nlm.nih.gov/7108955/"
access: partial
---

# Kyte 1982 - A Simple Method for Displaying the Hydropathic Character of a Protein

> [!abstract]
> The paper that introduced the Kyte-Doolittle hydropathy scale and the moving-window hydropathy plot, the first widely used way to spot membrane-spanning segments from a protein sequence alone.

## Why this source

It gives each of the 20 amino acids a hydropathy value, from 4.5 for isoleucine (most hydrophobic) to -4.5 for arginine (most hydrophilic), and averages these values over a window that slides along the sequence. Hydrophobic stretches long enough to cross a membrane stand out as peaks: with a window of 19 residues, segments averaging above 1.6 flag candidate transmembrane helices. The method is a few lines of code, which makes it the natural first sequence-based predictor to implement before learning the statistical topology predictors that replaced it.

## Coverage

Citation: Kyte J, Doolittle RF. "A simple method for displaying the hydropathic character of a protein". *Journal of Molecular Biology* 157(1):105-132 (1982). PMID 7108955.

| Part | Content | Vault notes |
|---|---|---|
| Hydropathy scale | One value per amino acid side chain, from 4.5 (Ile) to -4.5 (Arg) | [[Amino Acid]], [[Hydrophobic Effect]] |
| Moving-window average | Mean hydropathy of a segment of fixed length, advanced one residue at a time | [[Hydropathy Plot]] |
| Membrane-spanning segments | Window of 19 residues, threshold 1.6 | [[Cell Membrane]], [[Membrane Protein]] |

Cited in [[Cell Membrane]].

## How to use it

- **L1**: read the abstract, then implement the scale and a sliding window on a toy sequence ([[Cell Membrane#Computational representation]]).
- **L2**: plot real membrane and soluble proteins with several window lengths and see how the window trades noise against resolution ([[Hydropathy Plot]]).
- **L3**: compare its predictions with a modern topology predictor and with a structure in the [[RCSB Protein Data Bank]].

## Caveats

- A 1982 heuristic: a single threshold misses short or amphipathic helices and flags hydrophobic segments of soluble proteins (signal peptides, buried cores). Use it to learn the idea, not for final annotation.
- The abstract is free on PubMed; the full text is on the publisher's site, whose access terms were not verified.
- Metadata (authors, journal, volume, pages, year, PMID), the scale's extreme values and the 19-residue window with its 1.6 threshold verified in this pass.
