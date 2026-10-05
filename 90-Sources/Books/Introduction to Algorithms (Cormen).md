---
aliases:
  - CLRS
tags:
  - type/source
  - domain/computer-science
  - level/L2
  - level/L3
  - level/M1
kind: book
tier: S
authors:
  - Thomas H. Cormen
  - Charles E. Leiserson
  - Ronald L. Rivest
  - Clifford Stein
institution: MIT Press
year: 2022
edition: "4th"
url: "https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/"
access: paid
---

# Introduction to Algorithms (Cormen)

> [!abstract]
> "CLRS", the leading university algorithms textbook and standard reference, 4th edition (2022).

## Why this source

Broad and rigorous: every algorithm comes with pseudocode, a correctness argument and a complexity analysis, in self-contained chapters. It is the reference for the algorithmic backbone of bioinformatics: dynamic programming, graphs, string matching.

## Coverage

Seven parts: Foundations; Sorting and Order Statistics; Data Structures; Advanced Design and Analysis Techniques; Advanced Data Structures; Graph Algorithms; Selected Topics.

| Part | Content | Vault notes |
|---|---|---|
| Foundations | Analysis of algorithms, growth of functions, divide and conquer, recurrences | [[Algorithms\|Algorithm]], [[Big O Notation\|Asymptotic Notation]], [[Divide and Conquer]], [[Recurrence Relation]] |
| Sorting and data structures | Sorting algorithms, hash tables, search trees | [[Sorting\|Sorting Algorithm]], [[Hash Table]], [[Binary Search Tree]] |
| Ch. 14 Dynamic Programming | Optimal substructure, memoization, classic DP problems | [[Dynamic Programming]] |
| Advanced design | Greedy algorithms, amortized analysis | [[Greedy Algorithm]] |
| Ch. 20 Elementary Graph Algorithms, and later graph chapters | BFS, DFS, shortest paths, spanning trees, flows, bipartite matching | [[Graph\|Graph Theory]], [[Graph Traversal\|Breadth-First Search]], [[Graph Traversal\|Depth-First Search]], [[Shortest Path]] |
| Ch. 32 String Matching | Exact pattern matching algorithms | [[Exact Pattern Matching\|String Matching]] |
| Selected topics | NP-completeness, approximation, online algorithms, machine learning (new in 4th ed.) | [[NP-Completeness]] |

## How to use it

- L2: foundations, sorting, basic data structures, dynamic programming, elementary graph algorithms.
- L3: string matching and advanced graph chapters, then NP-completeness.
- Implement each algorithm in Python after reading; the book gives pseudocode only.

## Caveats

- Paid and long; treat it as a reference, not cover-to-cover reading.
- Chapter numbers changed between the 3rd and 4th editions (e.g. dynamic programming is ch. 14 in the 4th); cite the edition.
- Only chapters 14, 20 and 32 were verified by number; part names were not verified in this pass.
