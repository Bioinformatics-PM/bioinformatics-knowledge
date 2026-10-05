---
aliases:
  - Probability Theory
  - Probabilités
tags:
  - type/moc
  - domain/statistics
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Mathematical Foundations]]"
  - "[[Calculus]]"
  - "[[Discrete Mathematics]]"
projects:
  - "[[05-sequence-search]]"
  - "[[06-mutation-lab]]"
  - "[[07-evolution-simulator]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Harvard Stat 110 - Probability]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[MIT 6.042J - Mathematics for Computer Science]]"
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Altschul 1990 - Basic Local Alignment Search Tool]]"
  - "[[Information Theory, Inference, and Learning Algorithms (MacKay)]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[ETH Zurich - BSc Biology]]"
  - "[[Tsinghua University - BS Biological Sciences]]"
  - "[[MIT - Course 6-7 Computer Science and Molecular Biology]]"
---

# Probability

> [!abstract]
> The mathematics of uncertainty: events and conditioning, random variables and the common distributions, joint behavior, limit theorems, and the basics of information theory.

## Why it matters for bioinformatics

- Biological data are **counts of random events**: reads covering a base, mutations in a genome, k-mers in a sequence, genes in a pathway. Their distributions (binomial, Poisson, negative binomial, hypergeometric) are the models behind variant calling, coverage, differential expression and enrichment tests.
- **Conditioning and Bayes' theorem** turn sequencing evidence into genotype calls and test results into diagnoses.
- **Limit theorems** explain why averages and statistical tests work; **information theory** measures the information in a motif, the complexity of a sequence and the coevolution of residues.

## Before you start

- [[Mathematical Foundations]]: [[Set]], [[Function]], [[Summation Notation]], [[Exponential Function]], [[Logarithm]].
- [[Discrete Mathematics]]: [[Combinatorics]], [[Binomial Coefficient]], [[Inclusion-Exclusion Principle]].
- [[Calculus]]: [[Integral]], [[Improper Integral]], [[Infinite Series]]; [[Multiple Integral]] for Stage 2.

## Learning path

### Stage 1 - Foundations (L1)

1. [[Probability Space]] (L1): define outcomes, events and the axioms; compute probabilities by counting. Bio: the probability that a random 8-mer matches a given site.
2. [[Conditional Probability]] (L1): compute $P(A \mid B)$ and use the multiplication rule. Bio: the probability of a sequencing error given a quality score.
3. [[Independence (Probability)]] (L1): test and use independence of events. Bio: sites assumed to evolve independently in likelihood models; linkage breaks independence.
4. [[Law of Total Probability]] (L1): split a probability over a partition. Bio: the probability of observing a base, summed over the possible true genotypes.
5. [[Bayes' Theorem]] (L1): invert conditional probabilities; reason with base rates. Bio: positive predictive value of a screening test; posterior probability of a genotype given reads.
6. [[Random Variable]] (L1): define discrete and continuous random variables and their events. Bio: read depth at a position; number of mutations in a gene.
7. [[Probability Distribution]] (L1): describe a discrete distribution by its probability mass function. Bio: the distribution of counts of a k-mer across genomes.
8. [[Cumulative Distribution Function]] (L1): compute and invert $F(x) = P(X \le x)$; get tail probabilities. Bio: p-values are tail probabilities.
9. [[Expected Value]] (L1): compute means and use linearity of expectation. Bio: expected occurrences of a k-mer in a random sequence, $(n - k + 1)/4^k$.
10. [[Variance]] (L1): compute variance and standard deviation; variance of sums of independent variables. Bio: the mean-variance relationship of count data.
11. [[Bernoulli Distribution]] (L1): model one yes/no trial. Bio: one read carries the alternative allele or not.
12. [[Binomial Distribution]] (L1): count successes in $n$ independent trials. Bio: alternative-allele reads at a heterozygous site, $\mathrm{Bin}(n, 1/2)$; binomial sampling in the Wright-Fisher model.
13. [[Poisson Distribution]] (L1): model counts of rare independent events; use it as a limit of the binomial. Bio: sequencing coverage (Lander-Waterman); new mutations per genome per generation.
14. [[Probability Density Function]] (L1): compute probabilities of continuous variables as integrals of a density. Bio: continuous measurements such as log-intensities.
15. [[Uniform Distribution]] (L1): use discrete and continuous uniform models. Bio: p-values are uniform under the null hypothesis; random positions along a genome.
16. [[Normal Distribution]] (L1): standardize and use normal tables and z-scores. Bio: measurement error; approximate distribution of log-expression.

### Stage 2 - Core (L2)

17. [[Geometric Distribution]] (L2): model the waiting time to a first success. Bio: run lengths; the implicit duration of a state in a hidden Markov model.
18. [[Negative Binomial Distribution]] (L2): model overdispersed counts as a gamma-Poisson mixture. Bio: RNA-seq read counts in differential expression tools.
19. [[Hypergeometric Distribution]] (L2): model sampling without replacement. Bio: over-representation of a pathway among differentially expressed genes (Gene Ontology enrichment).
20. [[Multinomial Distribution]] (L2): model counts over several categories. Bio: nucleotide counts in a column of a position frequency matrix; genotype counts under Hardy-Weinberg.
21. [[Exponential Distribution]] (L2): model memoryless waiting times. Bio: time to the next substitution along a branch; mRNA lifetimes.
22. [[Gamma Distribution]] (L2): model sums of exponential waits and positive skewed quantities. Bio: rate heterogeneity among sites (the "+G" of substitution models).
23. [[Beta Distribution]] (L2): model a proportion. Bio: allele frequencies and methylation levels; the prior of a binomial proportion.
24. [[Joint Distribution]] (L2): work with joint, marginal and conditional distributions of two or more variables. Bio: genotypes at two loci; marginalizing over unobserved genotypes.
25. [[Covariance]] (L2): compute covariance and correlation of random variables and the variance of sums. Bio: co-expression of two genes.
26. [[Law of Large Numbers]] (L2): state the weak law, with Markov's and Chebyshev's inequalities. Bio: why deep coverage gives accurate allele fractions; why simulation estimates converge.
27. [[Central Limit Theorem]] (L2): approximate sums and means by a normal distribution and know when it fails. Bio: normal approximation of large counts; why tests on means work.
28. [[Shannon Entropy]] (L2): compute the entropy of a distribution in bits. Bio: information content of motif positions (sequence logos); low-complexity sequence; Shannon diversity of a microbiome.
29. [[Kullback-Leibler Divergence]] (L2): measure how one distribution differs from another (relative entropy). Bio: information of a motif against the genomic background; relative entropy of substitution matrices.
30. [[Mutual Information]] (L2): measure the dependence between two variables. Bio: coevolving residue pairs and RNA covariation; network inference from expression data.

### Stage 3 - Advanced (L3)

31. [[Conditional Expectation]] (L3): use $E[X \mid Y]$, the law of total expectation and the law of total variance. Bio: splitting variance into biological and technical components.
32. [[Transformation of Random Variables]] (L3): derive the distribution of $g(X)$ with the change-of-variables formula. Bio: the log-normal distribution of expression; distributions of log fold changes.
33. [[Multivariate Normal Distribution]] (L3): use the mean vector and covariance matrix; marginals and conditionals of Gaussians. Bio: correlated traits; the model behind PCA and linear mixed models in GWAS.
34. [[Extreme Value Distribution]] (L3): model maxima of many random variables (Gumbel). Bio: the best random local alignment score, which gives BLAST its E-values.

> [!tip] Order of study
> Stage 1 follows MIT 18.05 (or OpenStax Introductory Statistics for a gentler start); Stage 2 follows Harvard Stat 110 or MIT 6.041SC (take one, use the other for problems). For every distribution, simulate it in Python and compare the histogram with the formula.

## Uses from other domains

- [[Sequencing Coverage]], [[Variant Calling]], [[Phred Quality Score]] ([[NGS Data Analysis]]): Poisson coverage, binomial allele counts, error probabilities, Bayes' theorem.
- [[Lander-Waterman Model]] ([[Genomics]]): the Poisson model of coverage.
- [[BLAST]], [[E-Value]], [[Sequence Motif]], [[Position Weight Matrix]] ([[Sequence Analysis]]): extreme values, entropy and relative entropy.
- [[Hardy-Weinberg Equilibrium]], [[Wright-Fisher Model]] ([[Evolution]]): multinomial and binomial sampling.
- [[Boltzmann Distribution]] ([[Statistical Physics]]) and [[Thermodynamic Entropy]] ([[Thermodynamics]]): the physical counterparts of distributions and entropy.
- [[Random Number Generation]], [[Random Variate Generation]], [[Monte Carlo Method]] ([[Scientific Computing]]): sampling from the distributions above and estimating probabilities by simulation.
- [[Markov Chain]] ([[Stochastic Processes]]): the next step after joint and conditional distributions.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 18.05 - Introduction to Probability and Statistics]] | MIT | L1-L2 | Combinatorics, random variables, distributions (Stage 1)[^1805] |
| [[Harvard Stat 110 - Probability]] | Harvard | L2 | Foundations, named distributions, limit theorems, Markov chains (Stages 1-3)[^stat110] |
| [[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]] | MIT | L2 | Probability models, discrete and continuous random variables, joint distributions, limit theorems[^6041] |
| [[MIT 6.042J - Mathematics for Computer Science]] | MIT | L1-L2 | Discrete probability on finite spaces (items 1-12)[^6042] |

## Reference books

- [[Introduction to Probability (Blitzstein)]]: the Stat 110 textbook; foundations, random variables, joint distributions, limit theorems.[^blitzstein]
- [[Introductory Statistics (OpenStax)]]: chapters 3 to 6 (probability topics, discrete and continuous random variables, the normal distribution) for a non-calculus first pass.[^openstax]
- [[Biological Sequence Analysis (Durbin)]]: chapter 11 (background on probability) for the distributions used in sequence analysis; chapter 2 for the significance of alignment scores (item 34).[^durbin]
- [[Information Theory, Inference, and Learning Algorithms (MacKay)]]: entropy, relative entropy and mutual information (items 28-30).

## Lab projects

- [[05-sequence-search]]: expected number of random k-mer hits; significance of hits.
- [[06-mutation-lab]]: probability of each mutation class under a uniform point-mutation model.
- [[07-evolution-simulator]]: binomial sampling of alleles each generation.
- [[10-genomic-pipeline]]: error models, base qualities and genotype likelihoods.

## References

[^1805]: [[MIT 18.05 - Introduction to Probability and Statistics]]: basic combinatorics, random variables and distributions come first, before Bayesian and frequentist statistics.
[^stat110]: [[Harvard Stat 110 - Probability]]: foundations, distributions, limit theorems, Markov chains.
[^6041]: [[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]]: probability models, random variables, random processes, limit theorems, inference.
[^6042]: [[MIT 6.042J - Mathematics for Computer Science]], discrete probability part.
[^blitzstein]: [[Introduction to Probability (Blitzstein)]], 2nd ed.
[^openstax]: [[Introductory Statistics (OpenStax)]], 2nd ed., chapters 3 to 6.
[^durbin]: [[Biological Sequence Analysis (Durbin)]], chapters 2 and 11.

Scope check (synthesis in [[Curriculum Benchmark]]): probability and statistics are required in computational programs such as CMU's and UC San Diego's[^cmu][^ucsd] and in biology degrees such as ETH's and Tsinghua's;[^eth][^thu] statistics is only an elective in MIT 6-7.[^mit67] Items 31 to 34 go beyond a first course; they are included because likelihood models, PCA, mixed models and BLAST statistics rely on them. The significance of BLAST scores is part of the original method.[^blast]

[^cmu]: [[Carnegie Mellon University - BS Computational Biology]], mathematics and statistics core (one probability or statistical inference course).
[^ucsd]: [[UC San Diego - BS Bioinformatics]], upper-division statistics (MATH 186 Probability and Statistics).
[^eth]: [[ETH Zurich - BSc Biology]], statistics in the first two years.
[^thu]: [[Tsinghua University - BS Biological Sciences]], mathematics block (Probability and Mathematical Statistics).
[^mit67]: [[MIT - Course 6-7 Computer Science and Molecular Biology]], biology restricted electives (7.093 Modern Biostatistics).
[^blast]: [[Altschul 1990 - Basic Local Alignment Search Tool]], statistics of maximal segment pair scores.
