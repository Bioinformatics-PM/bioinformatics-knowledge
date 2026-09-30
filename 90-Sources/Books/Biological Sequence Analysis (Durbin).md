---
aliases:
  - Durbin et al.
  - Biological Sequence Analysis - Probabilistic Models of Proteins and Nucleic Acids
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - domain/computer-science
  - level/L3
  - level/M1
kind: book
tier: S
authors:
  - Richard Durbin
  - Sean R. Eddy
  - Anders Krogh
  - Graeme Mitchison
institution: Cambridge University Press
year: 1998
edition: "1st"
url: "https://www.cambridge.org/core/books/biological-sequence-analysis/921BB7B78B745198829EF96BC7E0F29D"
access: paid
---

# Biological Sequence Analysis (Durbin)

> [!abstract]
> The classic unified account of probabilistic models for sequence analysis: alignment, hidden Markov models, phylogeny and RNA structure.

## Why this source

Written for molecular biologists, computer scientists and mathematicians alike, with a Bayesian slant. It is the canonical source for HMMs and profile HMMs in biology (the basis of HMMER and Pfam) and for probabilistic alignment.

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| Ch. 1 Introduction | Probability and inference basics | [[Probability]], [[Bayes' Theorem]], [[Maximum Likelihood Estimation]] |
| Ch. 2 Pairwise alignment | Scoring, DP alignment, significance | [[Sequence Alignment]], [[Substitution Matrix]], [[Dynamic Programming]] |
| Ch. 3 Markov chains and hidden Markov models | Viterbi, forward-backward, parameter estimation | [[Markov Chain]], [[Hidden Markov Model]], [[Viterbi Algorithm]] |
| Ch. 4 Pairwise alignment using HMMs | Pair HMMs | [[Hidden Markov Model]] |
| Ch. 5 Profile HMMs for sequence families | Profiles, family search | [[Profile Hidden Markov Model]] |
| Ch. 6 Multiple sequence alignment methods | Progressive and probabilistic MSA | [[Multiple Sequence Alignment]] |
| Ch. 7 Building phylogenetic trees | Distance and parsimony methods | [[Phylogenetic Tree]], [[Maximum Parsimony]] |
| Ch. 8 Probabilistic approaches to phylogeny | Likelihood-based phylogeny | [[Maximum Likelihood Phylogenetics]] |
| Ch. 9 Transformational grammars | Formal grammars for sequences | [[Stochastic Context-Free Grammar]] |
| Ch. 10 RNA structure analysis | RNA secondary structure | [[RNA Secondary Structure]] |
| Ch. 11 Background on probability | Distributions and estimation | [[Probability Distribution]] |

## How to use it

- L3: chapters 1 to 3, then 5; implement Viterbi and forward algorithms in Python.
- M1: chapters 4, 6, 8 to 10.
- Prerequisites: [[Introduction to Probability (Blitzstein)]] level probability and basic dynamic programming.

## Caveats

- 1998: no next-generation sequencing, modern MSA tools or deep learning.
- Paid (Cambridge Core); many university libraries provide access.
