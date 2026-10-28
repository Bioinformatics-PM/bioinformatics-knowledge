---
aliases:
  - Skew algorithm paper
  - DC3 paper
tags:
  - type/source
  - domain/computer-science
  - domain/bioinformatics
  - level/L3
  - level/M1
kind: paper
tier: S
authors:
  - Juha Kärkkäinen
  - Peter Sanders
journal: "Automata, Languages and Programming (ICALP 2003), Lecture Notes in Computer Science 2719"
year: 2003
url: "https://doi.org/10.1007/3-540-45061-0_73"
access: partial
---

# Kärkkäinen 2003 - Simple Linear Work Suffix Array Construction

> [!abstract]
> The paper of the skew algorithm: a suffix array built in linear time by recursively sorting two thirds of the suffixes, sorting the last third with that information, and merging, with integer (radix) sorting as the only nontrivial subroutine.

## Why this source

It is the simplest linear-time suffix array construction, and a textbook case of an unbalanced divide and conquer whose recurrence $T(n) = T(2n/3) + O(n)$ solves to $O(n)$. Its only tool besides recursion is [[Radix Sort]] on small integer tuples, which makes it a natural bridge between algorithm design and genome indexing.

## Coverage

Citation: Kärkkäinen J, Sanders P. "Simple linear work suffix array construction". In: *Automata, Languages and Programming* (ICALP 2003), Lecture Notes in Computer Science 2719:943-955, Springer (2003). doi:10.1007/3-540-45061-0_73.

| Part | Content | Vault notes |
|---|---|---|
| Algorithm | Step 1: recursively sort the suffixes starting at positions $i \bmod 3 \neq 0$; step 2: sort the other suffixes using that order; step 3: merge the two sorted lists | [[Suffix Array Construction]], [[Divide and Conquer]] |
| Analysis | Linear time over integer alphabets; integer sorting as the only nontrivial subroutine | [[Radix Sort]], [[Master Theorem]] |
| Context | Suffix arrays as the compact alternative to suffix trees | [[Suffix Array]], [[Suffix Tree]] |

## How to use it

- L3: read after [[Suffix Array]] and [[Radix Sort]]; implement the three steps on small strings and test against naive suffix sorting.
- M1: compare with induced sorting (SA-IS) and prefix doubling in [[Suffix Array Construction]].

## Caveats

- Verified in this pass: citation metadata (ICALP 2003, LNCS 2719, pages 943-955, DOI) and the three-step description with linear running time. A later journal version with Stefan Burkhardt names the algorithm DC3 (difference cover modulo 3); it was not read in this pass.
- The publisher version is paywalled; an author copy circulates on the authors' institutional pages (not checked for identity with the published text).
