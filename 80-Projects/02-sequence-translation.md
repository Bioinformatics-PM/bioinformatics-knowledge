---
aliases: []
tags:
  - type/project
  - domain/bioinformatics
repository: https://github.com/Bioinformatics-PM/02-sequence-translation
status: planned
prerequisites:
  - "[[Central Dogma]]"
  - "[[Transcription]]"
  - "[[Translation]]"
  - "[[Genetic Code]]"
  - "[[Codon]]"
  - "[[Reading Frame]]"
  - "[[Open Reading Frame]]"
  - "[[Amino Acid]]"
  - "[[Hash Table]]"
sources: []
---
# 02-sequence-translation

> [!abstract]
> From DNA to protein: transcription, codon table, reading frames and ORF detection.

## Objective

Implement the flow of genetic information from DNA to RNA to protein, including the six reading frames and open reading frame detection.

## Concepts required

- [[Central Dogma]]
- [[Transcription]]
- [[Translation]]
- [[Genetic Code]]
- [[Codon]]
- [[Reading Frame]]
- [[Open Reading Frame]]
- [[Amino Acid]]
- [[Hash Table]]

## Four questions

| Lens | Answer |
|---|---|
| Biology: what is modeled? | Transcription and translation; the genetic code and its start and stop codons. |
| Mathematics: which model or algorithm? | A mapping from 64 codons to 21 symbols; frame arithmetic modulo 3. |
| Computer science: how is it implemented efficiently? | Lookup tables, streaming over frames, correct handling of partial codons. |
| Product: how does it become a usable tool? | A visual aligned view of DNA, codons and amino acids. |

## Scope

Standard and alternative genetic codes (NCBI translation tables).

## Status and next step

Planned for [[Curriculum#Stage 1 - Foundations|Stage 1]]. Repository not created yet.
