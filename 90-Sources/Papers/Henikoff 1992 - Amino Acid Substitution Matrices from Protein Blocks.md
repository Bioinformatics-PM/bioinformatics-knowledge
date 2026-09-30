---
aliases:
  - BLOSUM paper
  - BLOSUM62
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Steven Henikoff
  - Jorja G. Henikoff
journal: Proceedings of the National Academy of Sciences USA
year: 1992
url: "https://doi.org/10.1073/pnas.89.22.10915"
access: free
---

# Henikoff 1992 - Amino Acid Substitution Matrices from Protein Blocks

> [!abstract]
> The paper that introduced the BLOSUM amino acid substitution matrices, log-odds scores estimated from conserved blocks of aligned protein segments; BLOSUM62 became the default matrix of protein similarity search.

## Why this source

Earlier matrices (PAM) extrapolated from a small set of closely related sequences. The Henikoffs counted amino acid pairs directly in about 2,000 ungapped blocks of aligned segments characterizing more than 500 groups of related proteins, and turned the counts into a log-odds score for each of the 210 pairs of amino acids. Clustering segments above an identity threshold gives a family of matrices (BLOSUM62 clusters segments that are at least 62 % identical). The matrices gave marked improvements in alignments and in database searches. For a learner it is the clearest example of a scoring table derived from data rather than from chemistry, and a first quantitative view of which missense changes proteins tolerate.

## Coverage

Citation: Henikoff S, Henikoff JG. "Amino acid substitution matrices from protein blocks". *Proceedings of the National Academy of Sciences USA* 89(22):10915-10919 (1992).

| Part | Content | Vault notes |
|---|---|---|
| Data | About 2,000 blocks from more than 500 protein groups (BLOCKS database) | [[Multiple Sequence Alignment]], [[Protein Domain]] |
| Method | Pair counts, clustering by identity, log-odds scores in half-bit units | [[Substitution Matrix]] |
| Evaluation | Better alignments and searches than the matrices of the time | [[BLAST]], [[Sequence Alignment]] |

Cited in [[Missense Mutation]].

## How to use it

- L2: read the method section after the log-odds introduction of [[Biological Sequence Analysis (Durbin)]] (chapter 2), then recompute a few scores by hand from pair frequencies.
- L3: rebuild a small BLOSUM-style matrix from a toy set of blocks in [[04-alignment-engine]], and compare search results with BLOSUM62 and a PAM matrix.

## Caveats

- The matrices average over all positions of many proteins: they say how often a replacement is accepted in general, not at a given site.
- Scores are rounded to integers in half-bit units ($2\log_2$ of the odds ratio).
- Verified in this pass: authors, title, journal, volume, issue, pages and year, the abstract's figures (about 2,000 blocks, more than 500 groups), the 210 pair scores and the half-bit scaling. The BLOSUM62 values used in the vault were checked against the matrix file distributed with Biopython 1.88 (header "BLOSUM Clustered Scoring Matrix in 1/2 Bit Units", cluster percentage at least 62). The DOI link was not opened (web fetching blocked in this pass).
