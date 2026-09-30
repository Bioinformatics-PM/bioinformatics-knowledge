---
aliases:
  - Felsenstein 1981
  - F81 paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - domain/biology
  - level/L3
  - level/M1
kind: paper
tier: S
authors:
  - Joseph Felsenstein
journal: Journal of Molecular Evolution
year: 1981
url: "https://doi.org/10.1007/BF01734359"
access: paid
---

# Felsenstein 1981 - Evolutionary Trees from DNA Sequences

> [!abstract]
> "Evolutionary trees from DNA sequences: a maximum likelihood approach": the paper that made maximum likelihood phylogenetics on DNA sequences computationally practical.

## Why this source

It introduced a way to compute the likelihood of a tree from aligned DNA sequences under an explicit substitution model, the foundation of modern likelihood and Bayesian phylogenetics (RAxML, IQ-TREE, MrBayes, BEAST). The substitution model it used is known as F81.

## Coverage

Citation: Felsenstein J. *J Mol Evol* 17(6):368-376 (1981). doi:10.1007/BF01734359

| Part | Content | Vault notes |
|---|---|---|
| Model | Substitution model with unequal base frequencies (F81) | [[Nucleotide Substitution Model\|Substitution Model]], [[Markov Chain]] |
| Likelihood on a tree | Recursive computation from the tips to the root (the "pruning" algorithm) | [[Maximum Likelihood Phylogenetics]], [[Felsenstein Pruning Algorithm]], [[Maximum Likelihood Estimation]] |
| Tree search | Searching for the maximum-likelihood tree | [[Phylogenetic Tree]] |

## How to use it

- L3: read after [[Dynamic Programming]] and [[Nucleotide Substitution Model|substitution models]]; implement the pruning algorithm on a 4-taxon tree.
- M1: continue with [[Inferring Phylogenies (Felsenstein)]] and [[Molecular Evolution (Yang)]].

## Caveats

- Modern analyses use richer models (GTR, rate variation among sites) built on the same framework.
- Metadata cross-checked against multiple published bibliographic records; open-access status not verified.
