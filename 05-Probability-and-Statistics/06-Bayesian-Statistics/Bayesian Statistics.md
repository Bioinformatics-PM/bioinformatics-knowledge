---
aliases:
  - Bayesian Inference Methods
  - Statistique bayésienne
tags:
  - type/moc
  - domain/statistics
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Probability]]"
  - "[[Statistical Inference]]"
projects:
  - "[[10-genomic-pipeline]]"
sources:
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[MIT 18.650 - Statistics for Applications]]"
  - "[[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]]"
  - "[[MIT 6.047 - Computational Biology]]"
  - "[[Bayesian Data Analysis (Gelman)]]"
  - "[[Molecular Evolution (Yang)]]"
  - "[[Inferring Phylogenies (Felsenstein)]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
---

# Bayesian Statistics

> [!abstract]
> Inference as updating beliefs with data: priors, posteriors and conjugacy, credible intervals and model comparison, hierarchical and empirical Bayes models, and the Monte Carlo methods that compute posteriors in practice.

## Why it matters for bioinformatics

- **Genotype calling, Bayesian phylogenetics and population-structure inference** are Bayesian: they report posterior probabilities of genotypes, clades and ancestries.
- **Shrinkage** by empirical Bayes is what makes differential expression work with three replicates: gene-wise variances and fold changes borrow strength from all genes.
- **MCMC** (Metropolis-Hastings, Gibbs sampling) is the engine of Bayesian tree inference, molecular dating and classic motif finders.

## Before you start

- [[Probability]]: [[Bayes' Theorem]], [[Joint Distribution]], [[Beta Distribution]], [[Gamma Distribution]], [[Multinomial Distribution]].
- [[Statistical Inference]]: [[Likelihood Function]], [[Maximum Likelihood Estimation]], [[Confidence Interval]].
- [[Stochastic Processes]]: [[Markov Chain]], [[Stationary Distribution]] (before item 14).

## Learning path

### Stage 2 - Core (L2)

1. [[Bayesian Inference]] (L2): combine a prior and a likelihood into a posterior; compare with frequentist reasoning. Bio: calling a genotype from reads with a prior on heterozygosity.
2. [[Prior Distribution]] (L2): encode prior knowledge or ignorance as a distribution. Bio: population allele frequencies as priors; priors on branch lengths.
3. [[Posterior Distribution]] (L2): compute and summarize posteriors (mean, median, mode). Bio: the posterior probability of a clade or a genotype.
4. [[Conjugate Prior]] (L2): update beta-binomial, gamma-Poisson and normal-normal models in closed form. Bio: the gamma-Poisson mixture behind negative binomial counts.
5. [[Beta-Binomial Model]] (L2): model a proportion with uncertainty and overdispersion. Bio: allele fractions and methylation levels estimated from read counts.
6. [[Credible Interval]] (L2): compute equal-tailed and highest-density intervals and contrast them with confidence intervals. Bio: intervals on divergence times in molecular dating.
7. [[Maximum A Posteriori Estimation]] (L2): find the posterior mode and relate it to regularized likelihood. Bio: pseudocounts in position weight matrices are a MAP estimate.

### Stage 3 - Advanced (L3)

8. [[Posterior Predictive Distribution]] (L3): predict new data and check a model against observed data.
9. [[Dirichlet Distribution]] (L3): use the conjugate prior of the multinomial. Bio: priors on nucleotide or amino-acid frequencies in profiles and profile HMMs.
10. [[Noninformative Prior]] (L3): use flat and Jeffreys priors and know their pitfalls. Bio: seemingly flat priors on branch lengths that are informative about tree length.
11. [[Bayes Factor]] (L3): compare models by marginal likelihood. Bio: comparing clock models or selection models.
12. [[Bayesian Hierarchical Model]] (L3): share information across groups with hyperpriors. Bio: gene-level parameters drawn from a genome-wide distribution.
13. [[Empirical Bayes]] (L3): estimate the prior from the data and shrink estimates. Bio: moderated t-statistics and shrunken dispersions and fold changes in differential expression.
14. [[Markov Chain Monte Carlo]] (L3): sample a posterior with a Markov chain; check burn-in, mixing and convergence. Bio: Bayesian phylogenetics and molecular dating; population-structure inference.
15. [[Metropolis-Hastings Algorithm]] (L3): propose, accept or reject; tune proposals. Bio: tree-rearrangement moves in Bayesian phylogenetics.
16. [[Gibbs Sampling]] (L3): sample each variable from its full conditional. Bio: the Gibbs motif sampler; admixture models.

### Stage 4 - Frontier (M1)

17. [[Hamiltonian Monte Carlo]] (M1): use gradients to propose distant moves efficiently.
18. [[Variational Inference]] (M1): approximate a posterior by optimization. Bio: scalable probabilistic models of single-cell data.
19. [[Approximate Bayesian Computation]] (M1): infer parameters by simulation when the likelihood is intractable. Bio: demographic history in population genetics.
20. [[Probabilistic Programming]] (M1): write custom models in a probabilistic language (Stan, PyMC) and fit them.

> [!tip] Order of study
> Start with the discrete Bayesian updating tables of MIT 18.05, then conjugate models by hand. Learn MCMC only after [[Markov Chain]] and [[Stationary Distribution]]: an MCMC sampler is a Markov chain built to have the posterior as its stationary distribution.

## Uses from other domains

- [[Variant Calling]], [[Genotype Likelihood]] ([[NGS Data Analysis]]): genotype posteriors.
- [[Bayesian Phylogenetics]], [[Molecular Clock]] ([[Phylogenetics]]): Bayesian tree inference and dating.
- [[Population Structure]] ([[Population Genomics]]): admixture models fit by MCMC.
- [[Sequence Motif]], [[Position Weight Matrix]], [[Profile Hidden Markov Model]] ([[Sequence Analysis]]): Gibbs sampling; Dirichlet priors and pseudocounts.
- [[Dispersion Estimation]] ([[Transcriptomics]]): empirical Bayes shrinkage.
- [[Bayesian Network]] ([[Statistical Learning]]): the graphical-model extension of these ideas.
- [[Coalescent Theory]], [[Demographic Inference]] ([[Population Genomics]]): ABC with coalescent simulations.
- [[Detailed Balance]] ([[Statistical Physics]]): the condition that makes Metropolis-Hastings sample the right distribution.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 18.05 - Introduction to Probability and Statistics]] | MIT | L1-L2 | Bayesian inference side by side with frequentist statistics (items 1-7)[^1805] |
| [[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]] | MIT | L2 | Bayesian statistical inference (items 1-3, 7)[^6041] |
| [[MIT 18.650 - Statistics for Applications]] | MIT | L3 | Bayesian statistics: priors and posteriors (items 1-4, 10)[^18650] |
| [[MIT 6.047 - Computational Biology]] | MIT | L3-M1 | EM and Gibbs sampling for motifs (item 16)[^6047] |

## Reference books

- [[Bayesian Data Analysis (Gelman)]]: the reference text for hierarchical models, model checking and MCMC (Stage 3).
- [[Molecular Evolution (Yang)]]: Bayesian methods and MCMC in phylogenetics, expanded to three chapters in the 2nd edition (items 9-16).[^yang]
- [[Inferring Phylogenies (Felsenstein)]]: Bayesian inference of trees.[^felsenstein]
- [[Biological Sequence Analysis (Durbin)]]: probabilistic sequence models written with a Bayesian slant.[^durbin]

## Lab projects

- [[10-genomic-pipeline]]: genotype likelihoods and posteriors in variant calling.

## References

[^1805]: [[MIT 18.05 - Introduction to Probability and Statistics]]: Bayesian and frequentist statistics taught side by side.
[^6041]: [[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]], inference part.
[^18650]: [[MIT 18.650 - Statistics for Applications]], Bayesian statistics part.
[^6047]: [[MIT 6.047 - Computational Biology]], networks part.
[^yang]: [[Molecular Evolution (Yang)]], Bayesian methods chapters.
[^felsenstein]: [[Inferring Phylogenies (Felsenstein)]], part on Bayesian inference and statistical tests.
[^durbin]: [[Biological Sequence Analysis (Durbin)]].
