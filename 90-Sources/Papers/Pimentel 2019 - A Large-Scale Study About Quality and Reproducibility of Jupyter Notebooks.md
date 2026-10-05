---
aliases: []
tags:
  - type/source
  - domain/computer-science
  - domain/scientific-practice
  - level/L1
  - level/L2
kind: paper
tier: A
authors:
  - João Felipe Pimentel
  - Leonardo Murta
  - Vanessa Braganholo
  - Juliana Freire
journal: "MSR 2019, IEEE/ACM International Conference on Mining Software Repositories"
year: 2019
url: "https://2019.msrconf.org/details/msr-2019-papers/36/A-Large-scale-Study-about-Quality-and-Reproducibility-of-Jupyter-Notebooks"
access: paid
---

# Pimentel 2019 - A Large-Scale Study About Quality and Reproducibility of Jupyter Notebooks

> [!abstract]
> An empirical study that collected about 1.4 million Jupyter notebooks from GitHub and tried to re-run them: only about a quarter ran without errors and a few percent reproduced their stored results.

## Why this source

It replaces anecdotes about "notebooks are not reproducible" with measurements on a very large public corpus, and names the causes (missing dependencies, hidden state and out-of-order execution, inaccessible data). It is the evidence behind the notebook hygiene rules taught in [[Computational Notebook]].

## Coverage

Citation: Pimentel JF, Murta L, Braganholo V, Freire J. "A Large-scale Study about Quality and Reproducibility of Jupyter Notebooks". *MSR 2019*, the 16th International Conference on Mining Software Repositories (2019).

| Part | Content | Vault notes |
|---|---|---|
| Corpus | About 1.4 million notebooks collected from GitHub | [[Computational Notebook]] |
| Reproduction | Re-execution: about 24 % ran without errors, about 4 % produced the same results | [[Computational Notebook]], [[Computational Reproducibility]] |
| Causes | Missing dependencies, hidden states and out-of-order executions, data accessibility | [[Computational Notebook]], [[Dependency Management]] |

## How to use it

- L1: read the abstract and results with [[Computational Notebook]]; use the causes as a checklist before sharing a notebook.
- L2: compare with the rules of [[Rule 2019 - Ten Simple Rules for Writing and Sharing Computational Analyses in Jupyter Notebooks]] and [[Sandve 2013 - Ten Simple Rules for Reproducible Computational Research]].

## Caveats

- Public GitHub notebooks include many tutorials and student exercises; rates for curated research notebooks may differ.
- The percentages refer to the notebooks the authors attempted to re-execute, not to every notebook collected.
- Verified in this pass: title, authors, venue and year (conference page), corpus size, the two headline percentages and the list of failure causes. Page numbers and DOI not verified.
