---
aliases:
  - Microbiome Datasets Are Compositional
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L3
  - level/M1
kind: paper
tier: A
authors:
  - Gregory B. Gloor
  - Jean M. Macklaim
  - Vera Pawlowsky-Glahn
  - Juan J. Egozcue
journal: Frontiers in Microbiology
year: 2017
url: "https://doi.org/10.3389/fmicb.2017.02224"
access: free
---

# Gloor 2017 - Microbiome Datasets Are Compositional

> [!abstract]
> A review arguing that sequencing-based microbiome data are compositions, because the instrument imposes an arbitrary total on the counts, and that they should be analyzed as compositions at every stage.

## Why this source

Short and open access, written jointly by microbiome bioinformaticians and statisticians of compositional data. It explains why tools that assume ordinary vectors (correlation, distances, ordination) can mislead on relative abundances, and what to do instead.

## Coverage

Citation: Gloor GB, Macklaim JM, Pawlowsky-Glahn V, Egozcue JJ. "Microbiome datasets are compositional: and this is not optional". *Frontiers in Microbiology* 8:2224 (2017). doi:10.3389/fmicb.2017.02224. Free at PMC5695134 (PMID 29187837).

| Part | Content | Vault notes |
|---|---|---|
| The problem | High-throughput sequencing yields counts whose total is set by the instrument, not by the sample, so only relative information remains | [[Microbiome]], [[Metagenomics]], [[Compositional Data Analysis]] |
| Consequences | Analyses that ignore this constraint can give misleading results | [[Correlation]], [[Compositional Data Analysis]] |
| Guidance | Treat the data as compositions at all stages, with log-ratio methods | [[Compositional Data Analysis]], [[Vector Space]] |

## How to use it

- L3: read the problem statement with [[Vector Space]], which shows why proportions are not closed under ordinary addition and scaling.
- M1: read it in full with [[Compositional Data Analysis]] before analyzing any 16S or shotgun relative-abundance table.

## Caveats

- PubMed lists it as a review; the journal labels it a mini review.
- Verified in this pass (web search of the PubMed, PMC and journal records): authors, title, journal, volume, article number, year, DOI, PMC and PMID, and the central argument (arbitrary total imposed by the instrument; treat the data as compositions at all stages). The specific log-ratio procedures it recommends were not checked line by line.
