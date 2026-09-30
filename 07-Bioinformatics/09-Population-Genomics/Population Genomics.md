---
aliases:
  - Population Genetics and Genomics
  - Statistical Genetics
tags:
  - type/moc
  - domain/bioinformatics
  - domain/biology
  - domain/statistics
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Evolution]]"
  - "[[Genetics]]"
  - "[[NGS Data Analysis]]"
  - "[[Phylogenetics]]"
  - "[[Stochastic Processes]]"
  - "[[Linear Models]]"
  - "[[Multivariate Analysis]]"
projects:
  - "[[07-evolution-simulator]]"
  - "[[bio-simulation]]"
sources:
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[Molecular Evolution (Yang)]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[MIT 6.047 - Computational Biology]]"
  - "[[Kimura 1968 - Evolutionary Rate at the Molecular Level]]"
---

# Population Genomics

> [!abstract]
> Genome-wide variation within species: how diversity, linkage disequilibrium and structure arise under the coalescent, how selection leaves signatures, and how genotype-phenotype associations are mapped (GWAS).

## Why it matters for bioinformatics

Population genomics turns large variant datasets into answers about history, adaptation and disease: it underlies human genetics (GWAS, polygenic scores), conservation genomics, crop breeding and pathogen surveillance. It is also where the stochastic models of [[Evolution]] (drift, Wright-Fisher) meet real genome data, and computational biology programs teach it as quantitative genetic analysis.[^cmu]

## Before you start

- [[Evolution]]: [[Allele Frequency]], [[Hardy-Weinberg Equilibrium]], [[Heterozygosity]], [[Genetic Drift]], [[Effective Population Size]], [[Gene Flow]], [[Inbreeding]], [[Wright-Fisher Model]], [[Neutral Theory of Molecular Evolution]], [[Positive Selection]], [[Balancing Selection]].
- [[Genetics]]: [[Genetic Recombination]], [[Genetic Linkage]], [[Single Nucleotide Polymorphism]], [[Haplotype]], [[Quantitative Trait]], [[Heritability]], [[Quantitative Trait Locus]].
- [[NGS Data Analysis]]: [[Variant Calling]], [[Joint Genotyping]]; [[Bioinformatics Foundations]]: [[VCF Format]].
- [[Stochastic Processes]]: [[Markov Chain]], [[Poisson Process]]; [[Probability]]: [[Binomial Distribution]].
- [[Linear Models]]: [[Linear Regression]], [[Logistic Regression]], [[Linear Mixed Model]]; [[Multivariate Analysis]]: [[Principal Component Analysis]].
- [[Statistical Inference]]: [[Multiple Testing Correction]].

## Learning path

### Stage 2 - Core (L2)

1. [[Nucleotide Diversity]] (L2): measure sequence diversity as the average number of pairwise differences per site ($\pi$).
2. [[Linkage Disequilibrium]] (L2): quantify non-random association of alleles ($D$, $D'$, $r^2$) and its decay with recombination.
3. [[Fixation Index]] (L2): measure differentiation between populations with $F_{ST}$ and interpret its values.
4. [[Population Structure]] (L2): detect subpopulations and clines with PCA of genotypes and explain why structure matters.

### Stage 3 - Advanced (L3)

5. [[Coalescent Theory]] (L3): model the genealogy of a sample backward in time and derive expected coalescence times.
6. [[Infinite Sites Model]] (L3): place mutations on the genealogy and relate segregating sites to $\theta = 4N_e\mu$.
7. [[Watterson Estimator]] (L3): estimate $\theta$ from the number of segregating sites.
8. [[Site Frequency Spectrum]] (L3): summarize allele counts across sites and predict its neutral shape.
9. [[Tajima's D]] (L3): compare estimators of $\theta$ to detect departures from neutrality and demographic equilibrium.
10. [[Coalescent Simulation]] (L3): simulate genealogies and genomes with recombination (msprime) to test hypotheses.
11. [[Haplotype Phasing]] (L3): infer haplotypes from unphased genotypes with statistical and read-based methods.
12. [[Genotype Imputation]] (L3): predict untyped variants from a reference panel using shared haplotypes.
13. [[Identity by Descent]] (L3): detect segments shared from a recent common ancestor and estimate relatedness.
14. [[Ancestry Inference]] (L3): estimate admixture proportions of individuals (STRUCTURE, ADMIXTURE models).
15. [[Genome-Wide Association Study]] (L3): test millions of variants for association with a trait and read Manhattan and QQ plots.
16. [[Population Stratification]] (L3): recognize confounding by ancestry and correct it with principal components and mixed models.
17. [[Selective Sweep]] (L3): describe the footprint of positive selection on diversity, the SFS and LD around a site.
18. [[Selection Scan]] (L3): scan genomes for selection with diversity, differentiation and frequency-spectrum statistics.

### Stage 4 - Frontier (M1)

19. [[Extended Haplotype Homozygosity]] (M1): detect recent incomplete sweeps with haplotype statistics (iHS, XP-EHH).
20. [[McDonald-Kreitman Test]] (M1): contrast polymorphism and divergence at synonymous and nonsynonymous sites.
21. [[Demographic Inference]] (M1): infer population size history and splits from the SFS or from single genomes (PSMC).
22. [[Ancestral Recombination Graph]] (M1): represent genealogies along a recombining genome and infer them at scale.
23. [[Fine-Mapping]] (M1): narrow an association signal to credible sets of causal variants accounting for LD.
24. [[Expression Quantitative Trait Locus]] (M1): map variants that affect gene expression and link GWAS hits to genes.
25. [[Polygenic Risk Score]] (M1): build and evaluate a polygenic score and know its limits across ancestries.

> [!tip]
> Extend [[07-evolution-simulator]] with items 5 to 10: simulate a neutral sample, compute $\pi$, Watterson's $\theta$ and Tajima's D, then add a sweep and watch the statistics move.

## Uses from other domains

- [[Codon Substitution Model]] (from [[Phylogenetics]]): the between-species counterpart of item 20.
- [[Hidden Markov Model]] (from [[Stochastic Processes]]): phasing, imputation and PSMC are HMMs.
- [[Clinical Genomics]] (from [[Industry and Innovation]]): where polygenic scores and GWAS results are applied.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| 03-221 Genomes, Evolution, and Disease: Introduction to Quantitative Genetic Analysis, in [[Carnegie Mellon University - BS Computational Biology]] | CMU | L2-L3 | Required quantitative genetics course of the biological core[^cmu] |
| [[MIT 6.047 - Computational Biology]] | MIT | L3-M1 | "Evolution" part: coalescent, personal and population genomics, human ancestry, recent selection, disease mapping[^mit6047] |

## Reference books

- [[Principles of Population Genetics (Hartl)]]: population structure and F-statistics, linkage disequilibrium and molecular population genetics, coalescent material (items 1 to 9).[^hartl]
- [[Molecular Evolution (Yang)]]: coalescent and multispecies coalescent chapter, detecting natural selection (items 5, 17 to 20).[^yang]

## Lab projects

- [[07-evolution-simulator]]: Wright-Fisher simulation, the forward-time counterpart of the coalescent; the natural place for diversity statistics and sweeps.
- [[bio-simulation]]: the shared simulation engine.

## References

The order (diversity and LD, then the coalescent and neutrality tests, then association mapping and selection scans) follows the reference texts, which move from population genetic variation to linkage disequilibrium and the coalescent, and treat selection after the neutral model;[^hartl][^yang] the neutral theory is the null model behind the neutrality tests and selection scans.[^kimura] The M1 items (ancestry, recent selection, disease mapping) match the evolution part of MIT 6.047.[^mit6047]

[^cmu]: [[Carnegie Mellon University - BS Computational Biology]]: 03-221 Genomes, Evolution, and Disease: Introduction to Quantitative Genetic Analysis is in the biological core.
[^hartl]: [[Principles of Population Genetics (Hartl)]], material on population structure, linkage disequilibrium, molecular population genetics and the coalescent.
[^yang]: [[Molecular Evolution (Yang)]], chapters on the coalescent and on detecting natural selection.
[^kimura]: [[Kimura 1968 - Evolutionary Rate at the Molecular Level]].
[^mit6047]: [[MIT 6.047 - Computational Biology]], "Evolution" part.
