---
aliases:
  - FASTA program paper
  - Pearson and Lipman 1988
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L1
  - level/L2
kind: paper
tier: S
authors:
  - William R. Pearson
  - David J. Lipman
journal: Proceedings of the National Academy of Sciences of the USA
year: 1988
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC280013"
access: free
---

# Pearson 1988 - Improved Tools for Biological Sequence Comparison

> [!abstract]
> The paper that introduced the FASTA program for searching protein and DNA sequence databases, whose name the ubiquitous FASTA sequence file format carries.

## Why this source

It is the landmark reference for the FASTA family of similarity-search programs, which preceded [[BLAST]] and shaped how sequences were exchanged between tools. For this vault it is the historical anchor of the [[FASTA Format]] note and an early example of heuristic database search, a theme developed in [[Sequence Analysis]].

## Coverage

Citation: Pearson WR, Lipman DJ. "Improved tools for biological sequence comparison". *Proc Natl Acad Sci USA* 85:2444-2448 (April 1988). PMID 3162770; free at PMC280013.

| Part | Content | Vault notes |
|---|---|---|
| Programs | Three programs for comparing protein and DNA sequences: database search, evaluation of similarity scores, detection of periodic structures from local similarity | [[FASTA Format]], [[Sequence Alignment]] |
| FASTA | A more sensitive derivative of FASTP; searches protein or DNA databases, and can compare a protein with a DNA database by translating it during the search | [[BLAST]], [[Genetic Code]] |

## How to use it

- **L1**: read the abstract to see where the name of the file format comes from.
- **L2**: read it next to [[Altschul 1990 - Basic Local Alignment Search Tool]] to compare two heuristic answers to the same database-search problem.

## Caveats

- The paper describes programs, not a file format specification: for the format itself, use the NCBI description cited in [[FASTA Format]].
- Verified in this pass: authors, title, journal, volume, pages, month and year, PubMed and PMC identifiers, and the abstract's content.
