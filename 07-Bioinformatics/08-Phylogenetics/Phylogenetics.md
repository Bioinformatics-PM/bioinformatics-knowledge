---
aliases:
  - Molecular Phylogenetics
  - Phylogenetic Inference
tags:
  - type/moc
  - domain/bioinformatics
  - domain/biology
  - domain/statistics
  - domain/computer-science
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Sequence Analysis]]"
  - "[[Evolution]]"
  - "[[Stochastic Processes]]"
  - "[[Statistical Inference]]"
  - "[[Bayesian Statistics]]"
  - "[[Discrete Mathematics]]"
projects:
  - "[[08-phylogenetic-engine]]"
  - "[[bio-algorithms]]"
  - "[[bio-visualization]]"
sources:
  - "[[Inferring Phylogenies (Felsenstein)]]"
  - "[[Molecular Evolution (Yang)]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Saitou 1987 - The Neighbor-Joining Method]]"
  - "[[Felsenstein 1981 - Evolutionary Trees from DNA Sequences]]"
  - "[[Coursera UCSD - Bioinformatics Specialization]]"
  - "[[Inria - Bioinformatics Genomes and Algorithms]]"
  - "[[Galaxy Training Network - Training Material]]"
  - "[[MIT 6.047 - Computational Biology]]"
---

# Phylogenetics

> [!abstract]
> Reconstructing evolutionary trees from sequences: models of sequence evolution, distance, parsimony, likelihood and Bayesian methods, measures of support, and molecular dating.

## Why it matters for bioinformatics

Trees are the frame in which sequences are compared: they date outbreaks, classify microbes, trace gene families and give comparative genomics its statistical power. Phylogenetics is also the cleanest example in the discipline of the progression from combinatorial algorithms (parsimony) to explicit probabilistic models (likelihood, Bayesian inference), a progression shared by its reference texts.[^felsenstein][^durbin]

## Before you start

- [[Evolution]]: [[Common Descent]], [[Tree of Life]], [[Molecular Evolution]], [[Speciation]], [[Gene Duplication]], [[Positive Selection]], [[Purifying Selection]].
- [[Sequence Analysis]]: [[Sequence Homology]], [[Multiple Sequence Alignment]], [[Ortholog]], [[Paralog]].
- [[Discrete Mathematics]]: [[Tree (Graph Theory)]], [[Combinatorics]]; [[Data Structures]]: [[Tree (Data Structure)]].
- [[Multivariate Analysis]]: [[Distance Matrix]], [[Hierarchical Clustering]].
- [[Stochastic Processes]]: [[Markov Chain]], [[Continuous-Time Markov Chain]], [[Poisson Process]]; [[Linear Algebra]]: [[Eigenvalues and Eigenvectors]] (matrix exponential).
- [[Statistical Inference]]: [[Maximum Likelihood Estimation]], [[Bootstrap]]; [[Bayesian Statistics]]: [[Markov Chain Monte Carlo]].
- [[Bioinformatics Foundations]]: [[Newick Format]].

## Learning path

### Stage 2 - Core (L2)

1. [[Phylogenetic Tree]] (L2): read rooted and unrooted trees, clades, branch lengths and topologies, and count possible topologies.
2. [[Tree Rooting]] (L2): root a tree with an outgroup or the midpoint and see what changes in its interpretation.
3. [[Evolutionary Distance]] (L2): compute p-distances and explain why multiple hits make them underestimate divergence.
4. [[Nucleotide Substitution Model]] (L2): model nucleotide substitution as a continuous-time Markov chain with a rate matrix and stationary frequencies.
5. [[Jukes-Cantor Model]] (L2): derive the JC69 distance correction from equal rates.
6. [[Kimura Two-Parameter Model]] (L2): separate transitions from transversions (K80) and compute its distance.
7. [[UPGMA]] (L2): build an ultrametric tree by average-linkage clustering and recognize when the clock assumption fails.
8. [[Neighbor Joining]] (L2): build an additive tree without a clock using the neighbor-joining criterion.
9. [[Maximum Parsimony]] (L2): score a tree by the minimum number of changes and state the small and large parsimony problems.
10. [[Fitch Algorithm]] (L2): solve small parsimony on a binary tree by dynamic programming.

### Stage 3 - Advanced (L3)

11. [[Additive Phylogeny]] (L3): reconstruct a tree exactly from an additive matrix and test additivity with the four-point condition.
12. [[Sankoff Algorithm]] (L3): solve weighted small parsimony with a cost matrix.
13. [[Phylogenetic Tree Search]] (L3): explore tree space with NNI, SPR and TBR moves and branch and bound, since the large problem is NP-hard.
14. [[Long-Branch Attraction]] (L3): explain how parsimony and poor models group long branches wrongly.
15. [[General Time-Reversible Model]] (L3): use the GTR family, its special cases (HKY, F81) and its parameters.
16. [[Among-Site Rate Variation]] (L3): model rate heterogeneity with a discrete gamma distribution and invariant sites.
17. [[Protein Substitution Model]] (L3): use empirical amino acid matrices (Dayhoff, JTT, WAG, LG) for protein trees.
18. [[Maximum Likelihood Phylogenetics]] (L3): estimate tree and parameters by maximizing the likelihood of the alignment (RAxML, IQ-TREE).
19. [[Felsenstein Pruning Algorithm]] (L3): compute a tree likelihood efficiently by dynamic programming from leaves to root.
20. [[Substitution Model Selection]] (L3): choose a model with likelihood ratio tests, AIC or BIC.
21. [[Phylogenetic Bootstrap]] (L3): assess branch support by resampling alignment columns and interpret bootstrap values correctly.
22. [[Bayesian Phylogenetics]] (L3): sample trees from the posterior with MCMC (MrBayes, BEAST) and read posterior probabilities and priors.
23. [[Consensus Tree]] (L3): summarize a set of trees with strict and majority-rule consensus.
24. [[Robinson-Foulds Distance]] (L3): compare two topologies by their bipartitions.
25. [[Molecular Clock]] (L3): test a strict clock, use relaxed clocks and calibrations to date divergences.

### Stage 4 - Frontier (M1)

26. [[Codon Substitution Model]] (M1): model evolution at the codon level and estimate dN/dS (omega) to detect selection (PAML-style).
27. [[Ancestral Sequence Reconstruction]] (M1): infer ancestral states by parsimony, marginal and joint likelihood.
28. [[Phylogenomics]] (M1): build species trees from hundreds of genes by concatenation or summary methods.
29. [[Incomplete Lineage Sorting]] (M1): explain gene tree discordance under the multispecies coalescent.
30. [[Gene Tree Reconciliation]] (M1): map a gene tree onto a species tree to infer duplications, losses and transfers.
31. [[Phylogenetic Network]] (M1): represent reticulate evolution (recombination, hybridization, horizontal transfer).

> [!tip]
> Do the distance methods (items 3 to 8) with [[08-phylogenetic-engine]] first, then implement items 18 and 19 on a four-taxon tree by hand: after that, likelihood software stops being a black box.

## Uses from other domains

- [[Matrix Exponential]] (from [[Linear Algebra]]): transition probabilities $P(t) = e^{Qt}$ of substitution models.
- [[Model Selection]] and [[Likelihood Ratio Test]] (from [[Statistical Inference]]): the general theory behind item 20.
- [[Branch and Bound]] and [[Heuristic Algorithm]] (from [[Algorithms]]), [[Local Search]] (from [[Optimization]]): the search strategies of item 13.
- [[Log-Space Arithmetic]] (from [[Scientific Computing]]): numerically safe likelihoods in items 18 and 19.
- [[Coalescent Theory]] (from [[Population Genomics]]): the population-level process behind item 29.
- [[Horizontal Gene Transfer]] (from [[Microbiology]]): a cause of item 31.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[Coursera UCSD - Bioinformatics Specialization]] | UC San Diego | L2-L3 | IV. Molecular Evolution (evolutionary trees)[^coursera] |
| [[Inria - Bioinformatics Genomes and Algorithms]] | Inria (France) | L2 | Phylogenetic tree reconstruction[^inria] |
| [[Galaxy Training Network - Training Material]] | Galaxy Project | L2-L3 | "Evolution" tutorial "Phylogenetics - Back to basics"[^gtn] |
| [[MIT 6.047 - Computational Biology]] | MIT | L3-M1 | "Evolution" part: gene and species trees, phylogenomics, coalescent (items 28 to 30)[^mit6047] |

## Reference books

- [[Inferring Phylogenies (Felsenstein)]]: parsimony, distance, models and likelihood, Bayesian inference and bootstrap material for items 1 to 25.[^felsenstein]
- [[Molecular Evolution (Yang)]]: nucleotide, amino acid and codon models, likelihood, Bayesian methods, clocks and selection (items 15 to 26).[^yang]
- [[Biological Sequence Analysis (Durbin)]]: ch. 7 "Building phylogenetic trees" and ch. 8 "Probabilistic approaches to phylogeny".[^durbin]
- [[Felsenstein 1981 - Evolutionary Trees from DNA Sequences]]: the F81 model and the pruning algorithm, source of items 18 and 19.[^f81]
- [[Bioinformatics Algorithms (Compeau)]]: "Which Animal Gave Us SARS?" for distance-based phylogeny and neighbor joining (items 3 to 8, 11).[^compeau]

## Lab projects

- [[08-phylogenetic-engine]]: distances, UPGMA, neighbor joining, then likelihood; Newick output.
- [[bio-algorithms]]: shared distance matrix and tree algorithms; [[bio-visualization]]: tree drawing.

## References

The order (trees and distances, then parsimony, then explicit models, likelihood and Bayesian inference, then support and dating) follows the reference texts;[^felsenstein][^yang][^durbin] neighbor joining and likelihood on trees are anchored in their original papers.[^nj][^f81]

[^felsenstein]: [[Inferring Phylogenies (Felsenstein)]], parsimony, distance, likelihood, Bayesian and bootstrap material.
[^yang]: [[Molecular Evolution (Yang)]], models of sequence evolution, phylogenetic inference, Bayesian methods, selection and clocks.
[^durbin]: [[Biological Sequence Analysis (Durbin)]], ch. 7 "Building phylogenetic trees" and ch. 8 "Probabilistic approaches to phylogeny".
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "Which Animal Gave Us SARS?".
[^nj]: [[Saitou 1987 - The Neighbor-Joining Method]].
[^gtn]: [[Galaxy Training Network - Training Material]], topic "Evolution".
[^f81]: [[Felsenstein 1981 - Evolutionary Trees from DNA Sequences]].
[^coursera]: [[Coursera UCSD - Bioinformatics Specialization]], course IV "Molecular Evolution".
[^inria]: [[Inria - Bioinformatics Genomes and Algorithms]], part on phylogenetic trees.
[^mit6047]: [[MIT 6.047 - Computational Biology]], "Evolution" part.
