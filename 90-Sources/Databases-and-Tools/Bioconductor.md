---
aliases: []
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - domain/computer-science
  - level/L2
  - level/L3
kind: tool
tier: C
authors:
  - Robert C. Gentleman
  - Wolfgang Huber
  - et al. (Bioconductor community)
institution: Bioconductor Project (open-source community)
year:
edition:
url: "https://www.bioconductor.org"
access: free
---

# Bioconductor

> [!abstract]
> An open-source, open-development project of interoperable R packages for the analysis and comprehension of high-throughput genomic and molecular biology data.

## Why this source

Bioconductor is the R counterpart of the Python bioinformatics ecosystem, and the home of standard tools for expression, sequencing and annotation data. Its packages share data structures, undergo a formal initial review and are continuously tested, which makes them more interoperable than isolated scripts. In this vault it is the toolkit used by the R-based courses; like any tool documentation it is tier C and never backs a concept claim alone.

## Coverage

Key publications: Gentleman RC, et al. "Bioconductor: open software development for computational biology and bioinformatics". *Genome Biology* 5:R80 (2004). Huber W, et al. "Orchestrating high-throughput genomic analysis with Bioconductor". *Nature Methods* 12:115-121 (2015).

| Part | Content | Vault notes |
|---|---|---|
| Project goals | Collaborative development, lower barriers to interdisciplinary research, reproducibility | [[R Programming]], [[Computational Reproducibility]] |
| Package ecosystem | Packages for statistics and bioinformatics of high-throughput data | [[Transcriptomics]] |
| Quality | Initial review and continuous automated testing of packages | [[Continuous Integration]] |
| Teaching | Vignettes and course material from the community | [[Coursera JHU - Genomic Data Science Specialization]], [[HarvardX PH525x - Data Analysis for the Life Sciences]], [[Modern Statistics for Modern Biology (Holmes)]] |

Cited in [[Coursera JHU - Genomic Data Science Specialization]] and [[HarvardX PH525x - Data Analysis for the Life Sciences]].

## How to use it

- L2: install it when a course reaches its Bioconductor module; read the vignette of each package before using it.
- L3: use it for differential expression and annotation in transcriptomics projects, after implementing the underlying statistics once by hand.

## Caveats

- Releases are tied to R versions; pin both in each project.
- Package quality and maintenance vary despite review; check the build status and last update.
- Verified in this pass: project description and the two key publications (journals, volumes, pages); package counts change with each release and are not quoted here.
