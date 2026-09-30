---
aliases: []
tags:
  - type/project
  - domain/bioinformatics
repository: https://github.com/Bioinformatics-PM/09-genome-browser
status: planned
prerequisites:
  - "[[Genome]]"
  - "[[Gene Annotation]]"
  - "[[FASTA Format]]"
  - "[[GFF Format]]"
  - "[[VCF Format]]"
  - "[[Interval Tree]]"
  - "[[Data Visualization]]"
sources: []
---
# 09-genome-browser

> [!abstract]
> A genome browser loading FASTA, GFF/GTF and VCF, with zoom, pan and search.

## Objective

Display a chromosome with its genes and variants, navigable at every scale.

## Concepts required

- [[Genome]]
- [[Gene Annotation]]
- [[FASTA Format]]
- [[GFF Format]]
- [[VCF Format]]
- [[Interval Tree]]
- [[Data Visualization]]

## Four questions

| Lens | Answer |
|---|---|
| Biology: what is modeled? | Genome organization: genes, exons, variants. |
| Mathematics: which model or algorithm? | Coordinate systems and intervals. |
| Computer science: how is it implemented efficiently? | Interval indexing, level-of-detail rendering. |
| Product: how does it become a usable tool? | The visual centerpiece of the portfolio. |

## Scope

Built on bio-visualization; rendering in biolab-web.

## Status and next step

Planned for [[Curriculum#Stage 3 - Advanced|Stage 3]]. Repository not created yet.
