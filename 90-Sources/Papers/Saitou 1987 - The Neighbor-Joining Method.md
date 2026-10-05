---
aliases:
  - Neighbor-joining paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Naruya Saitou
  - Masatoshi Nei
journal: Molecular Biology and Evolution
year: 1987
url: "https://doi.org/10.1093/oxfordjournals.molbev.a040454"
access: paid
---

# Saitou 1987 - The Neighbor-Joining Method

> [!abstract]
> "The neighbor-joining method: a new method for reconstructing phylogenetic trees": a fast distance-based algorithm that builds a tree by successively joining pairs of neighbors.

## Why this source

Neighbor joining is still one of the most used tree-building methods, fast enough for thousands of sequences and a common starting tree for likelihood searches. It is the standard example of a distance-based phylogeny algorithm in textbooks such as [[Bioinformatics Algorithms (Compeau)]].

## Coverage

Citation: Saitou N, Nei M. *Mol Biol Evol* 4:406-425 (1987). doi:10.1093/oxfordjournals.molbev.a040454

| Part | Content | Vault notes |
|---|---|---|
| Input | Matrix of evolutionary distances between sequences | [[Distance Matrix]], [[Nucleotide Substitution Model\|Substitution Model]] |
| Algorithm | Iteratively join the pair of taxa that minimizes total branch length, then update distances | [[Neighbor Joining\|Neighbor-Joining Algorithm]] |
| Output | Unrooted tree with branch lengths | [[Phylogenetic Tree]] |

## How to use it

- L2: implement neighbor joining from a textbook, then read the paper's principle and simulations.
- L3: compare with [[Felsenstein 1981 - Evolutionary Trees from DNA Sequences|maximum likelihood]].

## Caveats

- Quality depends on the distance correction used; NJ does not model sequences directly.
- Metadata cross-checked against multiple published bibliographic records; open-access status not verified.
