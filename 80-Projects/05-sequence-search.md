---
aliases: []
tags:
  - type/project
  - domain/bioinformatics
repository: https://github.com/Bioinformatics-PM/05-sequence-search
status: planned
prerequisites:
  - "[[Exact Pattern Matching]]"
  - "[[K-mer]]"
  - "[[Inverted Index]]"
  - "[[Seed and Extend]]"
  - "[[BLAST]]"
  - "[[Hash Table]]"
  - "[[Big O Notation]]"
  - "[[Benchmarking]]"
sources: []
---
# 05-sequence-search

> [!abstract]
> A small sequence search engine, from naive search to k-mer indexes and seed-and-extend, benchmarked from 100 to 1M sequences.

## Objective

Build successive search strategies and measure runtime, memory and accuracy as the database grows.

## Concepts required

- [[Exact Pattern Matching]]
- [[K-mer]]
- [[Inverted Index]]
- [[Seed and Extend]]
- [[BLAST]]
- [[Hash Table]]
- [[Big O Notation]]
- [[Benchmarking]]

## Four questions

| Lens | Answer |
|---|---|
| Biology: what is modeled? | Finding homologous sequences in large databases. |
| Mathematics: which model or algorithm? | k-mer statistics, sensitivity versus specificity. |
| Computer science: how is it implemented efficiently? | Indexing, hashing, heuristics, scalability. |
| Product: how does it become a usable tool? | A search interface with ranked hits and alignments. |

## Scope

Nucleotide search; protein search as an extension.

## Status and next step

Planned for [[Curriculum#Stage 2 - Core|Stage 2]]. Repository not created yet.
