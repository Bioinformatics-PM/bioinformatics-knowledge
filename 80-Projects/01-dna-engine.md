---
aliases: []
tags:
  - type/project
  - domain/bioinformatics
repository: https://github.com/Bioinformatics-PM/01-dna-engine
status: planned
prerequisites:
  - "[[Nucleotide]]"
  - "[[DNA]]"
  - "[[Base Pairing]]"
  - "[[GC Content]]"
  - "[[Reverse Complement]]"
  - "[[Sequence Motif]]"
  - "[[FASTA Format]]"
  - "[[String]]"
  - "[[Big O Notation]]"
  - "[[Unit Testing]]"
sources: []
---
# 01-dna-engine

> [!abstract]
> Core primitives to validate, measure and transform DNA sequences.

## Objective

Learn to manipulate a biological sequence as a typed domain object rather than a string: validation, length, base counts, GC content, complement, reverse complement, motif search.

## Concepts required

- [[Nucleotide]]
- [[DNA]]
- [[Base Pairing]]
- [[GC Content]]
- [[Reverse Complement]]
- [[Sequence Motif]]
- [[FASTA Format]]
- [[String]]
- [[Big O Notation]]
- [[Unit Testing]]

## Four questions

| Lens | Answer |
|---|---|
| Biology: what is modeled? | DNA as an oriented polymer of four nucleotides; base pairing and strand orientation (5'→3'). |
| Mathematics: which model or algorithm? | Strings over the alphabet {A, C, G, T}; counting, frequencies, pattern matching. |
| Computer science: how is it implemented efficiently? | Linear-time scans, input validation, immutable value objects, property-based tests. |
| Product: how does it become a usable tool? | A CLI and Python API; later the DNA Engine card of biolab-web. |

## Scope

Python package built on bio-core. No external bioinformatics library for the core functions.

## Status and next step

Planned for [[Curriculum#Stage 1 - Foundations|Stage 1]]. Repository not created yet.
