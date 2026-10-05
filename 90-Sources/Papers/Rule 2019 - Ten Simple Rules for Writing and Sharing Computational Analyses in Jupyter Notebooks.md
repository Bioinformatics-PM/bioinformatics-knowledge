---
aliases: []
tags:
  - type/source
  - domain/scientific-practice
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
kind: paper
tier: A
authors:
  - Adam Rule
  - Fernando Pérez
  - Peter W. Rose
journal: PLoS Computational Biology
year: 2019
url: "https://doi.org/10.1371/journal.pcbi.1007007"
access: free
---

# Rule 2019 - Ten Simple Rules for Writing and Sharing Computational Analyses in Jupyter Notebooks

> [!abstract]
> Ten practical rules, written by notebook users and Jupyter developers, for notebooks that others can read, run and build on: tell a story, document the process, split code into modules and pipelines, record dependencies, version and share.

## Why this source

Where [[Sandve 2013 - Ten Simple Rules for Reproducible Computational Research]] gives rules for any computational analysis, this paper applies them to notebooks specifically, in the same *PLoS Computational Biology* series. It is short, concrete and aimed at computational biologists.

## Coverage

Citation: Rule A, et al. (including Pérez F and Rose PW). "Ten simple rules for writing and sharing computational analyses in Jupyter Notebooks". *PLoS Computational Biology* 15(7):e1007007 (2019). doi:10.1371/journal.pcbi.1007007.

Rule titles paraphrased:

| Rules | Content | Vault notes |
|---|---|---|
| 1-3 | Tell a story for an audience; document the process, not just the results; use cells to make steps clear | [[Computational Notebook]], [[Scientific Writing]] |
| 4 | Modularize code | [[Computational Notebook]], [[Python Packaging]] |
| 5, 6 | Record dependencies; use version control | [[Dependency Management]], [[Version Control]] |
| 7 | Build a pipeline | [[Workflow Management System]] |
| 8-10 | Share and explain the data; make notebooks readable, runnable and explorable; support open, reproducible research | [[Open Science]], [[Computational Reproducibility]] |

## How to use it

- L1: read it with [[Computational Notebook]] before sharing a first analysis notebook.
- L2: apply rules 4, 5 and 7 when moving notebook code into a Lab package and a workflow.

## Caveats

- Guidance, not measurement: pair it with [[Pimentel 2019 - A Large-Scale Study About Quality and Reproducibility of Jupyter Notebooks]] for evidence of what goes wrong.
- Tool recommendations in the paper date from 2019.
- Verified in this pass: title, journal, volume, issue, article number, year, DOI and the list of the ten rules (wording varies between summaries; titles above are paraphrased). The full author list was not checked.
