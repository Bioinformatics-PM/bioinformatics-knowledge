---
aliases:
  - Inferential Statistics
  - Frequentist Statistics
  - Statistique inférentielle
tags:
  - type/moc
  - domain/statistics
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Probability]]"
  - "[[Descriptive Statistics]]"
  - "[[Calculus]]"
projects:
  - "[[05-sequence-search]]"
  - "[[08-phylogenetic-engine]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[MIT 18.650 - Statistics for Applications]]"
  - "[[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]]"
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[An Introduction to Statistical Learning (James)]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Inferring Phylogenies (Felsenstein)]]"
  - "[[Benjamini 1995 - Controlling the False Discovery Rate]]"
  - "[[MIT 6.047 - Computational Biology]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[ETH Zurich - BSc Biology]]"
  - "[[Tsinghua University - BS Biological Sciences]]"
  - "[[MIT - Course 6-7 Computer Science and Molecular Biology]]"
---

# Statistical Inference

> [!abstract]
> Learning about a population or a mechanism from data: estimation (likelihood, confidence intervals, resampling), hypothesis testing, and the multiple-testing machinery that genomics depends on.

## Why it matters for bioinformatics

- **Estimation by likelihood** is how allele frequencies, mutation rates, evolutionary distances, branch lengths and genotype calls are obtained.
- **Tests** decide whether a gene is differentially expressed, a variant is associated with a disease, a pathway is enriched or a genotype departs from Hardy-Weinberg.
- Genomics tests **tens of thousands of hypotheses at once**: without [[Multiple Testing Correction]] and the [[False Discovery Rate]], most "discoveries" would be noise.

## Before you start

- [[Probability]]: [[Random Variable]], [[Expected Value]], [[Variance]], [[Binomial Distribution]], [[Hypergeometric Distribution]], [[Normal Distribution]], [[Joint Distribution]], [[Law of Large Numbers]], [[Central Limit Theorem]].
- [[Descriptive Statistics]]: [[Sampling]], [[Measure of Dispersion]], [[Contingency Table]].
- [[Calculus]]: [[Extremum]], [[Derivative]]; [[Hessian Matrix]] for Stage 3.

## Learning path

### Stage 1 - Foundations (L1)

1. [[Sampling Distribution]] (L1): describe the distribution of a statistic over repeated samples; compute a standard error. Bio: why the precision of a mean fold change grows with $\sqrt{n}$ replicates.
2. [[Confidence Interval]] (L1): build and interpret intervals for a mean and a proportion. Bio: an interval for an allele frequency estimated from a sample.
3. [[Hypothesis Testing]] (L1): state null and alternative hypotheses, a test statistic, a rejection rule, and type I and type II errors. Bio: is this gene differentially expressed?
4. [[P-Value]] (L1): compute a p-value and say what it does not mean. Bio: reading p-value histograms from a genome-wide screen.
5. [[Student's t-Distribution]] (L1): use the $t$ distribution for means with unknown variance. Bio: experiments with three replicates per condition.
6. [[Student's t-Test]] (L1): run one-sample, two-sample (Welch) and paired tests and check assumptions. Bio: tumor versus matched normal tissue (paired design).
7. [[Chi-Square Distribution]] (L1): relate it to sums of squared standard normals. Bio: the reference distribution of goodness-of-fit and likelihood ratio statistics.
8. [[Chi-Square Test]] (L1): test goodness of fit and independence in contingency tables. Bio: departure from Hardy-Weinberg proportions; allelic association in a case-control study.

### Stage 2 - Core (L2)

9. [[Statistical Model]] (L2): specify a parametric family and its assumptions (independence, identical distribution). Bio: a probabilistic model for read counts.
10. [[Estimator]] (L2): assess bias, variance, mean squared error and consistency. Bio: why the sample variance divides by $n - 1$; estimators of genetic diversity.
11. [[Method of Moments]] (L2): estimate parameters by matching moments. Bio: a quick estimate of negative binomial dispersion from mean and variance.
12. [[Likelihood Function]] (L2): write and plot the likelihood and log-likelihood of data. Bio: the likelihood of an allele frequency given allele counts.
13. [[Maximum Likelihood Estimation]] (L2): derive MLEs analytically and numerically; know their asymptotic properties. Bio: allele frequencies, mutation rates, the Jukes-Cantor distance, branch lengths of a tree.
14. [[Statistical Power]] (L2): compute power and the sample size needed for a target effect. Bio: how many RNA-seq replicates, how many GWAS cases.
15. [[Effect Size]] (L2): report effect sizes (difference, fold change, odds ratio) next to p-values. Bio: the two axes of a volcano plot; odds ratios of risk alleles.
16. [[Sensitivity and Specificity]] (L2): compute sensitivity, specificity and predictive values, and see how prevalence changes them ([[Bayes' Theorem]]). Bio: analytical validation of a clinical genetic test; why screening a rare disease gives many false positives.
17. [[F-Distribution]] (L2): use the ratio of two variance estimates. Bio: the reference distribution of the ANOVA F-test.
18. [[Fisher's Exact Test]] (L2): test a 2x2 table exactly with the hypergeometric distribution. Bio: Gene Ontology term enrichment in a gene list.
19. [[Nonparametric Statistics]] (L2): use rank-based methods that do not assume a distribution. Bio: robustness to outliers and to non-normal expression.
20. [[Wilcoxon Rank-Sum Test]] (L2): compare two groups by ranks (Mann-Whitney U); the signed-rank variant for pairs. Bio: marker genes between single-cell clusters.
21. [[Permutation Test]] (L2): build a null distribution by permuting labels. Bio: sample-label permutations in gene set enrichment; preserving gene-gene correlation.
22. [[Bootstrap]] (L2): estimate standard errors and confidence intervals by resampling. Bio: bootstrap support values on phylogenetic trees.
23. [[Multiple Testing Correction]] (L2): explain why thousands of tests produce false positives and how to adjust. Bio: 20,000 genes tested at once; the $5 \times 10^{-8}$ genome-wide significance threshold.
24. [[Family-Wise Error Rate]] (L2): control the probability of any false positive (Bonferroni, Holm).
25. [[False Discovery Rate]] (L2): control the expected proportion of false discoveries. Bio: the standard criterion in differential expression and peak calling.
26. [[Benjamini-Hochberg Procedure]] (L2): apply the step-up procedure to a vector of p-values. Bio: the "adjusted p-value" column of differential expression tables.

### Stage 3 - Advanced (L3)

27. [[Fisher Information]] (L3): relate the curvature of the log-likelihood to the variance of the MLE (Cramér-Rao bound). Bio: standard errors of estimated rates; choosing informative designs.
28. [[Likelihood Ratio Test]] (L3): compare nested models with Wilks' theorem; relate it to Wald and score tests. Bio: testing a molecular clock; codon models of positive selection; likelihood ratio tests for differential expression.
29. [[Model Selection]] (L3): compare models with likelihood ratio tests, AIC, BIC and cross-validation, and know what each rewards. Bio: choosing a substitution model before building a tree.
30. [[Kolmogorov-Smirnov Test]] (L3): compare distributions through their ECDFs. Bio: the running-sum statistic of gene set enrichment analysis is a weighted KS-type statistic.
31. [[Q-Value]] (L3): estimate the proportion of true nulls and report q-values. Bio: reading the p-value histogram of a screen.
32. [[Mixture Model]] (L3): model data as coming from several component distributions. Bio: copy-number states; null and alternative components of p-values; cell populations.
33. [[Expectation-Maximization Algorithm]] (L3): fit models with latent variables by alternating expectation and maximization. Bio: motif discovery (MEME); haplotype frequency estimation; Baum-Welch training of HMMs.

> [!tip] Order of study
> Stage 1 follows MIT 18.05 or OpenStax (chapters 7 to 9). Stage 2 moves to likelihood with MIT 18.650 and to genomics practice with PH525x. Do not skip items 23 to 26: they are the most used statistics in bioinformatics, and ISL's multiple-testing chapter is the clearest introduction.

## Uses from other domains

- [[Variant Calling]], [[Genotype Likelihood]] ([[NGS Data Analysis]]): likelihood-based genotype calls.
- [[Maximum Likelihood Phylogenetics]], [[Phylogenetic Bootstrap]], [[Substitution Model Selection]] ([[Phylogenetics]]): MLE on trees, bootstrap support, model selection.
- [[Genome-Wide Association Study]] ([[Population Genomics]]): association tests and genome-wide thresholds.
- [[Differential Expression Analysis]] ([[Transcriptomics]]): tests and FDR control on thousands of genes.
- [[Watterson Estimator]] ([[Population Genomics]]): an estimator of genetic diversity.
- [[Clinical Genomics]]: sensitivity, specificity and predictive values of genetic tests.
- [[Monte Carlo Method]] ([[Scientific Computing]]): the computation behind permutation tests and the bootstrap.
- [[Hardy-Weinberg Equilibrium]] ([[Evolution]]): chi-square goodness of fit.
- [[Sequence Motif]] ([[Sequence Analysis]]): EM-based motif discovery.
- [[Baum-Welch Algorithm]] ([[Stochastic Processes]]): EM for hidden Markov models.
- [[Experimental Design]]: power and sample size are decided before the experiment.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 18.05 - Introduction to Probability and Statistics]] | MIT | L1-L2 | Frequentist statistics: hypothesis testing, confidence intervals (Stage 1)[^1805] |
| [[MIT 18.650 - Statistics for Applications]] | MIT | L3 | Parametric inference, maximum likelihood, method of moments, hypothesis testing, goodness of fit (Stages 2-3)[^18650] |
| [[HarvardX PH525x - Data Analysis for the Life Sciences]] | Harvard (edX) | L2-L3 | PH525.1x p-values, confidence intervals, nonparametric statistics; later courses on inference for high-throughput data and multiple testing[^ph525] |
| [[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]] | MIT | L2 | Classical statistical inference, as the end of a probability course[^6041] |
| [[MIT 6.047 - Computational Biology]] | MIT | L3-M1 | EM and Gibbs sampling in motif discovery (item 33)[^6047] |

## Reference books

- [[Introductory Statistics (OpenStax)]]: chapter 7 "The Central Limit Theorem", chapter 8 "Confidence Intervals", chapter 9 "Hypothesis Testing", then two-sample tests, chi-square, F distribution and one-way ANOVA (Stage 1).[^openstax]
- [[An Introduction to Statistical Learning (James)]]: chapter 5 (resampling: cross-validation and the bootstrap) and chapter 13 (multiple testing, FWER and FDR).[^isl]
- [[Modern Statistics for Modern Biology (Holmes)]]: testing and multiple testing, mixture models (items 23-26, 32-33).[^msmb]
- [[Biological Sequence Analysis (Durbin)]]: chapter 1 (probability and inference basics) and chapter 11 (distributions and estimation), for likelihood in sequence models.[^durbin]
- [[Inferring Phylogenies (Felsenstein)]]: bootstrap and statistical tests of trees (items 22, 28).[^felsenstein]

## Lab projects

- [[05-sequence-search]]: significance of search hits and the trade-off between sensitivity and false positives.
- [[08-phylogenetic-engine]]: maximum likelihood estimation of distances and branch lengths; bootstrap support.
- [[10-genomic-pipeline]]: likelihood-based variant calling.

## References

[^1805]: [[MIT 18.05 - Introduction to Probability and Statistics]]: frequentist part (hypothesis testing, confidence intervals) after probability.
[^18650]: [[MIT 18.650 - Statistics for Applications]]: estimation (parametric inference, maximum likelihood, method of moments) then testing (parametric tests, goodness of fit); only lecture 1 is verified by title in the source note.
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.1x and PH525.2x to 4x.
[^6041]: [[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]], inference part.
[^6047]: [[MIT 6.047 - Computational Biology]], networks part (EM and Gibbs sampling, motifs).
[^openstax]: [[Introductory Statistics (OpenStax)]], 2nd ed.
[^isl]: [[An Introduction to Statistical Learning (James)]], Python edition; chapter numbers checked against the official ISLP lab notebooks (Ch05 resampling, Ch13 multiple testing).
[^msmb]: [[Modern Statistics for Modern Biology (Holmes)]].
[^durbin]: [[Biological Sequence Analysis (Durbin)]], chapters 1 and 11.
[^felsenstein]: [[Inferring Phylogenies (Felsenstein)]], part on Bayesian inference, bootstrap and tests of trees.

The FDR and its step-up procedure come from Benjamini and Hochberg.[^bh] Probability and statistics are required in computational programs such as CMU's and UC San Diego's[^cmu][^ucsd] and in biology degrees such as ETH's and Tsinghua's,[^eth][^thu] while statistics is only an elective in MIT 6-7;[^mit67] inference is weighted to L3 here because genomics depends on it (synthesis in [[Curriculum Benchmark]]).

[^bh]: [[Benjamini 1995 - Controlling the False Discovery Rate]].
[^cmu]: [[Carnegie Mellon University - BS Computational Biology]], mathematics and statistics core (one probability or statistical inference course).
[^ucsd]: [[UC San Diego - BS Bioinformatics]], upper-division statistics (MATH 186 Probability and Statistics).
[^eth]: [[ETH Zurich - BSc Biology]], statistics in the first two years.
[^thu]: [[Tsinghua University - BS Biological Sciences]], mathematics block (Probability and Mathematical Statistics).
[^mit67]: [[MIT - Course 6-7 Computer Science and Molecular Biology]], biology restricted electives (7.093 Modern Biostatistics).
