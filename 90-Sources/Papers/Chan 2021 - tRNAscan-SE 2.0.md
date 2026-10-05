---
aliases:
  - tRNAscan-SE 2.0 paper
  - tRNAscan-SE
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L3
kind: paper
tier: A
authors:
  - Patricia P. Chan
  - Brian Y. Lin
  - Allysia J. Mak
  - Todd M. Lowe
journal: Nucleic Acids Research
year: 2021
url: "https://doi.org/10.1093/nar/gkab688"
access: free
---

# Chan 2021 - tRNAscan-SE 2.0

> [!abstract]
> "tRNAscan-SE 2.0: improved detection and functional classification of transfer RNA genes": the current version of the standard tool that finds tRNA genes in genome sequences.

## Why this source

tRNA genes are short and their sequences vary, but their cloverleaf secondary structure is conserved, so they are found with models that score sequence and base pairing together. This paper describes how tRNAscan-SE 2.0 does it with Infernal 1.1 covariance models, uses nearly one hundred isotype- and clade-specific models to predict which amino acid each gene is charged with (from the anticodon and the best-scoring isotype model), and adds a "high confidence" filter that separates canonical tRNA genes from tRNA-derived repetitive elements. It is the reference for tRNA annotation in [[Gene Annotation]] and the engine behind [[GtRNAdb]].

## Coverage

Citation: Chan PP, Lin BY, Mak AJ, Lowe TM. "tRNAscan-SE 2.0: improved detection and functional classification of transfer RNA genes". *Nucleic Acids Research* 49(16):9077-9096 (2021). Free at PMC8450103.

| Part | Content | Vault notes |
|---|---|---|
| Search models | Covariance models (Infernal 1.1) trained on tRNAs from thousands of genomes | [[Stochastic Context-Free Grammar]], [[RNA Secondary Structure]] |
| Functional classification | Isotype- and clade-specific models; anticodon plus best isotype model | [[Transfer RNA]], [[Genetic Code]] |
| High-confidence filter | Separating canonical tRNAs from tRNA-derived repeats | [[Transposable Element]], [[Gene Annotation]] |

Cited in [[Transfer RNA]].

## How to use it

- L3: read the introduction and the overview of the search strategy after [[Transfer RNA]] and [[RNA Secondary Structure]]; M1: the covariance-model sections, with [[Stochastic Context-Free Grammar]].
- Run the web server or the command-line tool on a small bacterial genome and compare with the organism's page in [[GtRNAdb]].

## Caveats

- Benchmarks and model sets reflect the genomes available around 2019 to 2021; check the current release notes.
- Verified in this pass: authors, title, journal, volume, issue, pages, year, PMC record and the main features listed above.
