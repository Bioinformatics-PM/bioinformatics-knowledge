---
aliases:
  - Gusfield
tags:
  - type/source
  - domain/computer-science
  - domain/bioinformatics
  - level/L3
  - level/M1
kind: book
tier: S
authors:
  - Dan Gusfield
institution: Cambridge University Press
year: 1997
edition: "1st"
url: "https://www.cambridge.org/core/books/algorithms-on-strings-trees-and-sequences/F0B095049C7E6EF5356F0A26686C20D3"
access: paid
---

# Algorithms on Strings, Trees, and Sequences (Gusfield)

> [!abstract]
> The reference text on string algorithms, with extensive discussion of biological problems cast as string problems.

## Why this source

The deepest treatment of exact matching, suffix trees and alignment algorithms, with over 400 exercises. It explains the data structures that underlie read mappers, genome indexes and alignment tools.

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| Exact string matching | Classical exact matching algorithms | [[Exact Pattern Matching\|String Matching]], [[Knuth-Morris-Pratt Algorithm]] |
| Suffix trees (incl. Ch. 7 First Applications of Suffix Trees, Ch. 9 More Applications of Suffix Trees) | Construction and uses | [[Suffix Tree]], [[Suffix Array]] |
| Inexact matching, alignment, dynamic programming (incl. Ch. 12 Refining Core String Edits and Alignments, Ch. 13 Extending the Core Problems) | Edit distance, alignment variants | [[Edit Distance]], [[Sequence Alignment]], [[Dynamic Programming]] |
| Multiple string comparison | Multiple alignment | [[Multiple Sequence Alignment]] |
| Currents, Cousins, and Cameos (incl. Ch. 17 Strings and Evolutionary Trees) | Database search, sequencing, trees | [[Phylogenetic Tree]], [[BLAST]] |

## How to use it

- L3: suffix-tree part, after exact matching in [[Introduction to Algorithms (Cormen)]].
- M1: alignment refinements and the evolutionary-trees chapter; use the exercises.

## Caveats

- 1997: predates the Burrows-Wheeler/FM-index era of read mapping; pair with the pattern-matching chapter of [[Bioinformatics Algorithms (Compeau)]].
- Paid (Cambridge Core). Only chapters 7, 9, 12, 13 and 17 were verified by number.
