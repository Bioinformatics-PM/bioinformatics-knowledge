---
aliases:
  - BDA3
  - BDA
tags:
  - type/source
  - domain/statistics
  - level/L2
  - level/L3
  - level/M1
kind: book
tier: S
authors:
  - Andrew Gelman
  - John B. Carlin
  - Hal S. Stern
  - David B. Dunson
  - Aki Vehtari
  - Donald B. Rubin
institution: CRC Press
year: 2013
edition: "3rd"
url: "https://sites.stat.columbia.edu/gelman/book/"
access: free
---

# Bayesian Data Analysis (Gelman)

> [!abstract]
> The leading reference on applied Bayesian statistics, from single-parameter models to hierarchical models, model checking and computation; the PDF is free for non-commercial use.

## Why this source

It teaches Bayesian inference as a practical workflow: build a model, fit it, check it against the data, and improve it. Its treatment of hierarchical models and posterior predictive checking is the standard reference, and its computation part covers Markov chain Monte Carlo in depth. The third edition added chapters on nonparametric modeling. The authors make the PDF available from the book's homepage for non-commercial purposes.

## Coverage

Coverage is described by topic; chapter numbers were not verified in this pass.

| Part | Content | Vault notes |
|---|---|---|
| Fundamentals | Bayesian inference, priors, posteriors, conjugate models | [[Bayesian Inference]], [[Prior Distribution]], [[Posterior Distribution]], [[Conjugate Prior]] |
| Hierarchical models | Partial pooling across groups | [[Bayesian Hierarchical Model]], [[Empirical Bayes]] |
| Model checking | Posterior predictive checks, model comparison | [[Posterior Predictive Distribution]], [[Bayes Factor]] |
| Computation | MCMC, Metropolis and Gibbs sampling, Hamiltonian Monte Carlo, approximations | [[Markov Chain Monte Carlo]], [[Metropolis-Hastings Algorithm]], [[Gibbs Sampling]], [[Hamiltonian Monte Carlo]], [[Variational Inference]] |

Cited in [[Bayesian Statistics]].

## How to use it

- L2: start with the first chapters (single-parameter and multiparameter models) after [[Introduction to Probability (Blitzstein)]].
- L3: the reference for Stage 3 of [[Bayesian Statistics]]; work through the hierarchical model examples and fit them with a probabilistic programming language.
- M1: computation and advanced models for Stage 4.

## Caveats

- Assumes calculus, probability and some statistical modeling; not a first introduction.
- Verified in this pass: authors, publisher, edition, date (October 2013) and free PDF for non-commercial use.
