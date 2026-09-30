---
aliases: []
tags:
  - type/project
  - domain/bioinformatics
repository: https://github.com/Bioinformatics-PM/04-alignment-engine
status: planned
prerequisites:
  - "[[Sequence Alignment]]"
  - "[[Hamming Distance]]"
  - "[[Edit Distance]]"
  - "[[Dynamic Programming]]"
  - "[[Needleman-Wunsch Algorithm]]"
  - "[[Smith-Waterman Algorithm]]"
  - "[[Substitution Matrix]]"
  - "[[Gap Penalty]]"
  - "[[Sequence Homology]]"
sources: []
---
# 04-alignment-engine

> [!abstract]
> Pairwise sequence alignment from Hamming distance to Smith-Waterman, with the dynamic programming matrix made visible.

## Objective

Implement Hamming, Levenshtein, Needleman-Wunsch and Smith-Waterman, with traceback and a visualization of the dynamic programming matrix.

## Concepts required

- [[Sequence Alignment]]
- [[Hamming Distance]]
- [[Edit Distance]]
- [[Dynamic Programming]]
- [[Needleman-Wunsch Algorithm]]
- [[Smith-Waterman Algorithm]]
- [[Substitution Matrix]]
- [[Gap Penalty]]
- [[Sequence Homology]]

## Four questions

| Lens | Answer |
|---|---|
| Biology: what is modeled? | Homology and why aligned positions share ancestry. |
| Mathematics: which model or algorithm? | Optimal alignment as a longest path in a grid graph; scoring schemes. |
| Computer science: how is it implemented efficiently? | O(nm) dynamic programming, traceback, linear-space variants. |
| Product: how does it become a usable tool? | Matrix and path visualization in biolab-web. |

## Scope

Pairwise alignment; multiple alignment is a later extension.

## Status and next step

Planned for [[Curriculum#Stage 2 - Core|Stage 2]]. Repository not created yet.
