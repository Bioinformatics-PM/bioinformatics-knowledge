---
aliases: []
tags:
  - type/project
  - domain/bioinformatics
repository: https://github.com/Bioinformatics-PM/03-genome-diff
status: planned
prerequisites:
  - "[[Mutation]]"
  - "[[Single Nucleotide Polymorphism]]"
  - "[[Indel]]"
  - "[[Genetic Variant]]"
  - "[[VCF Format]]"
  - "[[Edit Distance]]"
  - "[[Genetic Code]]"
sources: []
---
# 03-genome-diff

> [!abstract]
> A `git diff` for biological sequences: SNPs, insertions and deletions, and their consequence on the protein.

## Objective

Compare a reference and a sample sequence, report variants, and propagate each variant to its codon and protein consequence.

## Concepts required

- [[Mutation]]
- [[Single Nucleotide Polymorphism]]
- [[Indel]]
- [[Genetic Variant]]
- [[VCF Format]]
- [[Edit Distance]]
- [[Genetic Code]]

## Four questions

| Lens | Answer |
|---|---|
| Biology: what is modeled? | Point mutations and indels; how they change codons and proteins. |
| Mathematics: which model or algorithm? | Edit operations and their minimal sequence (edit distance). |
| Computer science: how is it implemented efficiently? | Diff algorithms, variant normalization, VCF output. |
| Product: how does it become a usable tool? | An interactive diff view: variant, codon, protein consequence. |

## Scope

Pairwise comparison; multi-sample comparison is out of scope.

## Status and next step

Planned for [[Curriculum#Stage 2 - Core|Stage 2]]. Repository not created yet.
