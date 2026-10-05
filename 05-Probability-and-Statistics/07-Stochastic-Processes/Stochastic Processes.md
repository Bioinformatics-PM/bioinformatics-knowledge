---
aliases:
  - Random Processes
  - Markov Models
  - Processus stochastiques
tags:
  - type/moc
  - domain/statistics
  - domain/mathematics
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Probability]]"
  - "[[Linear Algebra]]"
projects:
  - "[[07-evolution-simulator]]"
  - "[[bio-simulation]]"
sources:
  - "[[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]]"
  - "[[Harvard Stat 110 - Probability]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[MIT 6.047 - Computational Biology]]"
  - "[[Molecular Evolution (Yang)]]"
  - "[[Felsenstein 1981 - Evolutionary Trees from DNA Sequences]]"
  - "[[Kimura 1968 - Evolutionary Rate at the Molecular Level]]"
  - "[[MIT 8.591J - Systems Biology]]"
---

# Stochastic Processes

> [!abstract]
> Random quantities that evolve in time or along a sequence: random walks, Markov chains in discrete and continuous time, Poisson and branching processes, and hidden Markov models with their dynamic-programming algorithms.

## Why it matters for bioinformatics

- **Hidden Markov models** annotate sequences: CpG islands, genes, protein domains (profile HMMs), copy-number segments, chromatin states. Viterbi, forward-backward and Baum-Welch are core bioinformatics algorithms.
- **Continuous-time Markov chains** are the substitution models of phylogenetics ($P(t) = e^{Qt}$); **absorbing Markov chains** give fixation probabilities under drift; the **coalescent** runs these processes backward in time.
- **Poisson and branching processes** model mutations along lineages, read starts along a genome, crossovers along a chromosome, and the early fate of new mutations or outbreaks.

## Before you start

- [[Probability]]: [[Conditional Probability]], [[Joint Distribution]], [[Geometric Distribution]], [[Exponential Distribution]], [[Poisson Distribution]].
- [[Linear Algebra]]: [[Matrix Multiplication]], [[Eigenvalues and Eigenvectors]], [[Perron-Frobenius Theorem]], [[Matrix Exponential]].
- [[Algorithms]]: [[Dynamic Programming]] (before items 14 to 16).
- [[Statistical Physics]]: [[Detailed Balance]], [[Brownian Motion]] (before items 10 and 17).

## Learning path

### Stage 2 - Core (L2)

1. [[Stochastic Process]] (L2): define a process indexed by time or position; distinguish discrete and continuous time and state. Bio: a DNA sequence read base by base; an allele frequency across generations.
2. [[Bernoulli Process]] (L2): model independent trials in sequence, with geometric gaps between successes. Bio: mutated versus unmutated sites along an alignment.
3. [[Random Walk]] (L2): analyze sums of independent steps, drift and hitting probabilities. Bio: the running score of BLAST extensions and of gene set enrichment; molecular diffusion.
4. [[Markov Chain]] (L2): use the Markov property to compute probabilities of paths. Bio: DNA sequence models where each base depends on the previous one; the Wright-Fisher model of allele counts.
5. [[Transition Matrix]] (L2): estimate a transition matrix from data and compute $n$-step probabilities with matrix powers (Chapman-Kolmogorov). Bio: dinucleotide transition frequencies; PAM matrices as powers of a one-step matrix.
6. [[Stationary Distribution]] (L2): find the long-run distribution and state the conditions for convergence (irreducible, aperiodic). Bio: equilibrium base composition of a substitution model.
7. [[Absorbing Markov Chain]] (L2): compute absorption probabilities and expected times to absorption. Bio: fixation or loss of an allele under genetic drift; a neutral allele fixes with probability equal to its initial frequency.
8. [[Poisson Process]] (L2): use exponential inter-arrival times, splitting and merging. Bio: mutations along a lineage; read starts along a genome; crossovers along a chromosome (Haldane's map function).

### Stage 3 - Advanced (L3)

9. [[Higher-Order Markov Chain]] (L3): condition on the previous $k$ symbols and fit the model by counting $(k+1)$-mers. Bio: background models for motif search; coding-region models in prokaryotic gene finders.
10. [[Continuous-Time Markov Chain]] (L3): work with a rate matrix $Q$, transition probabilities $e^{Qt}$ and time-reversibility ([[Detailed Balance]]). Bio: the Jukes-Cantor, HKY and GTR substitution models behind likelihood phylogenetics.
11. [[Birth-Death Process]] (L3): model populations that grow and shrink by single events. Bio: speciation-extinction models of phylogenies; gene family size evolution.
12. [[Branching Process]] (L3): compute extinction probabilities of a Galton-Watson process with generating functions. Bio: survival of a new beneficial mutation; whether an outbreak dies out; stochastic PCR amplification.
13. [[Hidden Markov Model]] (L3): define hidden states, transition and emission probabilities; compute the joint probability of a path and a sequence. Bio: CpG islands, gene structure, protein-family profiles, copy-number and chromatin-state segmentation.
14. [[Viterbi Algorithm]] (L3): find the most probable state path by dynamic programming in log space. Bio: annotating the most likely gene structure or island boundaries.
15. [[Forward-Backward Algorithm]] (L3): compute the probability of a sequence (forward) and posterior state probabilities at each position (posterior decoding). Bio: scoring a sequence against a profile HMM; confidence of each annotated base.
16. [[Baum-Welch Algorithm]] (L3): train HMM parameters from unlabeled sequences, as an instance of expectation-maximization. Bio: learning a gene or domain model without annotated examples.

### Stage 4 - Frontier (M1)

17. [[Diffusion Approximation]] (M1): approximate a discrete Markov chain by a diffusion, the mathematical form of [[Brownian Motion]]. Bio: Kimura's fixation probability of a selected allele; trait evolution along a phylogeny.
18. [[Gillespie Algorithm]] (M1): simulate chemical reaction systems exactly event by event. Bio: noise and bursting in gene expression.

> [!tip] Order of study
> Items 1 to 8 follow the random-processes part of MIT 6.041SC or the Markov chain chapter of Stat 110. For items 13 to 16, read Durbin chapter 3 and implement Viterbi and forward-backward in Python on the CpG island example before touching profile HMMs.

## Uses from other domains

- [[Wright-Fisher Model]], [[Moran Model]], [[Genetic Drift]], [[Fixation Probability]] ([[Evolution]]): Markov chains with absorbing states.
- [[Coalescent Theory]] ([[Population Genomics]]): genealogies as a continuous-time process backward in time.
- [[Nucleotide Substitution Model]], [[General Time-Reversible Model]], [[Maximum Likelihood Phylogenetics]] ([[Phylogenetics]]): continuous-time Markov chains on trees.
- [[Profile Hidden Markov Model]], [[Pair Hidden Markov Model]], [[Gene Finding]] ([[Sequence Analysis]]): HMMs applied to sequence families, alignments and genomes.
- [[Sequencing Coverage]] ([[NGS Data Analysis]]) and [[Lander-Waterman Model]] ([[Genomics]]): Poisson placement of reads.
- [[Stochastic Gene Expression]] ([[Systems Biology]]): simulated with the [[Gillespie Algorithm]].
- [[Markov Chain Monte Carlo]] ([[Bayesian Statistics]]): Markov chains designed to sample posteriors.
- [[Random Number Generation]], [[Monte Carlo Method]] ([[Scientific Computing]]): simulating every process above.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]] | MIT | L2 | Random processes: Bernoulli and Poisson processes, Markov chains (items 1-8)[^6041] |
| [[Harvard Stat 110 - Probability]] | Harvard | L2 | Markov chains and their long-run behavior (items 4-7)[^stat110] |
| [[MIT 6.047 - Computational Biology]] | MIT | L3-M1 | Hidden Markov models and gene finding (items 13-16)[^6047] |
| [[MIT 8.591J - Systems Biology]] | MIT | L3 | "Causes and Consequences of Stochastic Gene Expression" (item 18)[^8591] |

## Reference books

- [[Biological Sequence Analysis (Durbin)]]: chapter 3 "Markov chains and hidden Markov models" (Viterbi, forward-backward, parameter estimation), chapter 5 on profile HMMs (items 4, 9, 13-16).[^durbin]
- [[Introduction to Probability (Blitzstein)]]: Markov chains, after joint distributions and limit theorems (items 4-7).[^blitzstein]
- [[Molecular Evolution (Yang)]]: nucleotide, amino-acid and codon substitution models as Markov chains (item 10).[^yang]

## Lab projects

- [[07-evolution-simulator]]: Wright-Fisher as a Markov chain; fixation probabilities (items 4, 7).
- [[bio-simulation]]: the shared simulation engine for Markov and branching processes.

## References

[^6041]: [[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]], random-processes part.
[^stat110]: [[Harvard Stat 110 - Probability]], Markov chains part.
[^6047]: [[MIT 6.047 - Computational Biology]], genomes part (hidden Markov models, gene finding).
[^8591]: [[MIT 8.591J - Systems Biology]], verified lecture title.
[^durbin]: [[Biological Sequence Analysis (Durbin)]], chapters 3 and 5.
[^blitzstein]: [[Introduction to Probability (Blitzstein)]], 2nd ed.
[^yang]: [[Molecular Evolution (Yang)]], models of sequence evolution.

Landmarks: continuous-time substitution models and likelihood on trees were brought together by Felsenstein;[^f81] the fixation probability $1/N$ of a new neutral mutation is the key step of the neutral theory.[^kimura]

[^f81]: [[Felsenstein 1981 - Evolutionary Trees from DNA Sequences]].
[^kimura]: [[Kimura 1968 - Evolutionary Rate at the Molecular Level]].
