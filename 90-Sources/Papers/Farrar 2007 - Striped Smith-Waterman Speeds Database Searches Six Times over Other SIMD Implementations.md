---
aliases:
  - Farrar 2007
  - Striped Smith-Waterman
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L3
  - level/M1
kind: paper
tier: A
authors:
  - Michael Farrar
journal: Bioinformatics
year: 2007
url: "https://doi.org/10.1093/bioinformatics/btl582"
access: paid
---

# Farrar 2007 - Striped Smith-Waterman Speeds Database Searches Six Times over Other SIMD Implementations

> [!abstract]
> The "striped" vectorization of the Smith-Waterman algorithm: a SIMD layout that made exact local alignment several times faster on ordinary processors.

## Why this source

Exact Smith-Waterman is quadratic, which is why heuristics such as BLAST exist. Farrar laid the query out in stripes across SIMD vector registers so that one processor instruction updates several cells of the dynamic programming matrix. The abstract reports a 2 to 8 times improvement over other SIMD-based Smith-Waterman implementations and more than 3.0 billion cell updates per second on a 2.0 GHz Xeon Core 2 Duo processor. It is the entry point to the hardware side of exact alignment.

## Coverage

Citation: Farrar M. "Striped Smith-Waterman speeds database searches six times over other SIMD implementations". *Bioinformatics* 23(2):156-161 (15 January 2007). doi:10.1093/bioinformatics/btl582.

| Part | Content | Vault notes |
|---|---|---|
| Problem | Speeding up exact local alignment for database search | [[Smith-Waterman Algorithm]], [[BLAST]] |
| Method | Striped layout of the query in SIMD registers | [[Smith-Waterman Algorithm]] |
| Results | 2 to 8 times faster than other SIMD implementations; over 3 billion cell updates per second | [[Smith-Waterman Algorithm]] |

## How to use it

- M1: after implementing [[Smith-Waterman Algorithm]], read the description of the striped layout and compare it with the parallelism along anti-diagonals of the recurrence.

## Caveats

- The title's "six times" differs from the abstract's "2 to 8 times"; quote the abstract.
- Verified in this pass (web search): citation, DOI, issue date and the abstract's performance figures; Rognes (2011, *BMC Bioinformatics*, the SWIPE paper) described Farrar's method as the fastest SIMD approach of its time. The method details were not checked in the full text, and the open-access status was not verified.
