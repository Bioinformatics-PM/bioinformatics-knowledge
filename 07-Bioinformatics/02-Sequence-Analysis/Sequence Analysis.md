---
aliases:
  - Biological Sequence Analysis
  - Molecular Sequence Analysis
tags:
  - type/moc
  - domain/bioinformatics
  - domain/computer-science
  - domain/statistics
  - level/L1
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Bioinformatics Foundations]]"
  - "[[Molecular Biology]]"
  - "[[Genetics]]"
  - "[[Evolution]]"
  - "[[Algorithms]]"
  - "[[String Algorithms]]"
  - "[[Probability]]"
projects:
  - "[[01-dna-engine]]"
  - "[[02-sequence-translation]]"
  - "[[04-alignment-engine]]"
  - "[[05-sequence-search]]"
  - "[[bio-algorithms]]"
  - "[[bio-visualization]]"
sources:
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Algorithms on Strings, Trees, and Sequences (Gusfield)]]"
  - "[[An Introduction to Bioinformatics Algorithms (Jones)]]"
  - "[[Coursera UCSD - Bioinformatics Specialization]]"
  - "[[Peking University - Bioinformatics Introduction and Methods]]"
  - "[[Inria - Bioinformatics Genomes and Algorithms]]"
  - "[[MIT 6.047 - Computational Biology]]"
  - "[[MIT 7.91J - Foundations of Computational and Systems Biology]]"
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[Needleman 1970 - Search for Similarities in Amino Acid Sequences]]"
  - "[[Smith 1981 - Identification of Common Molecular Subsequences]]"
  - "[[Altschul 1990 - Basic Local Alignment Search Tool]]"
  - "[[Rosalind]]"
  - "[[NCBI BLAST]]"
---

# Sequence Analysis

> [!abstract]
> Reading biological meaning out of sequences: composition and motifs, homology, pairwise and multiple alignment, database search and probabilistic sequence models.

## Why it matters for bioinformatics

Sequence analysis is the historical core of the discipline and still its most used toolbox: every genome, transcript and protein is first compared, searched or aligned. It is where biology (homology), algorithms (dynamic programming, indexing) and statistics (scores as log-odds, significance of hits) meet for the first time, which is why bioinformatics programs open their specialist sequence with it[^ucsd] and why introductory courses in the United States, China and France all start from alignment and database search.[^coursera][^pku][^inria]

## Before you start

- [[Bioinformatics Foundations]] Stage 1, especially [[FASTA Format]] and [[IUPAC Nucleotide Code]].
- [[Molecular Biology]]: [[DNA]], [[Base Pairing]], [[DNA Replication]], [[Genetic Code]], [[Reading Frame]], [[Open Reading Frame]]; [[Biochemistry]]: [[Amino Acid]].
- [[Genetics]]: [[Mutation]], [[Indel]]; [[Evolution]]: [[Molecular Evolution]], [[Speciation]], [[Gene Duplication]].
- [[Algorithms]]: [[Big O Notation]], [[Dynamic Programming]], [[Divide and Conquer]], [[Randomized Algorithm]]; [[Data Structures]]: [[Hash Table]].
- [[String Algorithms]]: [[Exact Pattern Matching]], [[Hamming Distance]], [[Edit Distance]], [[Approximate Pattern Matching]]; [[Programming]]: [[Regular Expression]].
- [[Probability]]: [[Conditional Probability]], [[Multinomial Distribution]]; [[Mathematical Foundations]]: [[Logarithm]]. For Stage 3: [[Markov Chain]] and [[Hidden Markov Model]] from [[Stochastic Processes]].

## Learning path

### Stage 1 - Foundations (L1)

1. [[GC Content]] (L1): compute base composition of a sequence or sliding window and relate it to genome biology.
2. [[Reverse Complement]] (L1): produce the opposite strand read 5' to 3' and search both strands.
3. [[K-mer]] (L1): count all substrings of length k and use k-mer frequencies as a sequence signature.
4. [[GC Skew]] (L1): locate a bacterial replication origin from the cumulative G minus C skew.
5. [[Sequence Motif]] (L1): describe a short recurring pattern (consensus, regular expression) and find its occurrences.
6. [[Sequence Homology]] (L1): distinguish homology (shared ancestry, yes or no) from similarity and identity (measured scores).
7. [[Dot Plot]] (L1): compare two sequences visually and read repeats, inversions and indels from the diagonals.
8. [[Sequence Alignment]] (L1): write and score an alignment of two sequences with matches, mismatches and gaps.

### Stage 2 - Core (L2)

9. [[Ortholog]] (L2): recognize homologs separated by speciation and why they tend to keep their function.
10. [[Paralog]] (L2): recognize homologs separated by gene duplication and why they diverge in function.
11. [[Substitution Matrix]] (L2): read PAM and BLOSUM matrices as log-odds scores and choose one for a divergence level.
12. [[Gap Penalty]] (L2): compare linear and affine gap costs and their effect on alignments.
13. [[Needleman-Wunsch Algorithm]] (L2): compute an optimal global alignment by dynamic programming with traceback.
14. [[Smith-Waterman Algorithm]] (L2): compute an optimal local alignment and explain the zero floor.
15. [[Semi-Global Alignment]] (L2): align with free end gaps (fitting and overlap alignment) for reads and overlaps.
16. [[Gotoh Algorithm]] (L2): implement affine-gap alignment with three dynamic programming matrices in O(nm).
17. [[Low-Complexity Region]] (L2): detect and mask repetitive, low-entropy segments that create spurious hits.
18. [[Seed and Extend]] (L2): trade sensitivity for speed by extending exact k-mer seeds into alignments.
19. [[BLAST]] (L2): run and interpret the family of search programs (blastn, blastp, blastx, tblastn) and their parameters with [[NCBI BLAST]].
20. [[E-Value]] (L2): interpret bit scores and E-values from Karlin-Altschul statistics and the effect of database size.
21. [[Multiple Sequence Alignment]] (L2): explain why exact MSA is intractable and how an MSA reveals conserved columns.
22. [[Progressive Alignment]] (L2): build an MSA along a guide tree (the Clustal, MUSCLE and MAFFT family) and know its failure modes.
23. [[Position Weight Matrix]] (L2): turn aligned motif instances into a probabilistic profile and score new sites.
24. [[Sequence Logo]] (L2): display a motif with information content in bits per position.
25. [[Motif Finding]] (L2): find over-represented motifs de novo with greedy, randomized, Gibbs sampling and EM (MEME) approaches.
26. [[Codon Usage Bias]] (L2): measure unequal use of synonymous codons (RSCU, codon adaptation index) and relate it to expression and mutation bias.

### Stage 3 - Advanced (L3)

27. [[CpG Island]] (L3): discriminate CpG islands with two Markov chains, then segment a sequence with an HMM.
28. [[Hirschberg Algorithm]] (L3): compute an optimal alignment in linear space by divide and conquer.
29. [[Spaced Seed]] (L3): explain why non-contiguous seeds increase search sensitivity at equal speed.
30. [[PSI-BLAST]] (L3): iterate searches with a position-specific scoring matrix to detect remote homologs, and recognize profile drift.
31. [[Profile Hidden Markov Model]] (L3): model a sequence family with match, insert and delete states and search with it (HMMER).
32. [[Protein Family]] (L3): classify proteins into families and domains with curated profile libraries (Pfam, InterPro).
33. [[Gene Finding]] (L3): predict genes ab initio with Markov and HMM-based models (GENSCAN-style) and with homology evidence.
34. [[Alignment-Free Sequence Comparison]] (L3): compare sequences through k-mer profiles and sketches when alignment is too slow or meaningless.

### Stage 4 - Frontier (M1)

35. [[Pair Hidden Markov Model]] (M1): recast pairwise alignment as a probabilistic model and compute posterior probabilities of aligned pairs.

> [!tip]
> Implement items 1 to 8 in [[01-dna-engine]], items 11 to 16 in [[04-alignment-engine]] and items 17 to 20 in [[05-sequence-search]] before reading the probabilistic chapters. [[Rosalind]] has automatically checked problems for most of Stages 1 and 2.

## Uses from other domains

- [[Viterbi Algorithm]], [[Forward-Backward Algorithm]] and [[Baum-Welch Algorithm]] (from [[Stochastic Processes]]): the HMM machinery of items 27, 31, 33 and 35.
- [[Expectation-Maximization Algorithm]] (from [[Statistical Inference]]) and [[Gibbs Sampling]] (from [[Bayesian Statistics]]): the engines of item 25.
- [[Shannon Entropy]] and [[Extreme Value Distribution]] (from [[Probability]]): information content (item 24) and score statistics (item 20).
- [[Log-Space Arithmetic]] (from [[Scientific Computing]]): numerically safe probabilities in items 27 to 35.
- [[Minimizer]] and [[MinHash]] (from [[String Algorithms]]): the sketches behind item 34.
- [[Suffix Array]], [[Burrows-Wheeler Transform]] and [[FM-Index]] (from [[String Algorithms]]): the index structures reused in [[NGS Data Analysis]].

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[Coursera UCSD - Bioinformatics Specialization]] | UC San Diego | L2-L3 | I. Finding Hidden Messages in DNA (items 1 to 5, 23 to 25); III. Comparing Genes, Proteins, and Genomes (items 8 to 16)[^coursera] |
| [[Peking University - Bioinformatics Introduction and Methods]] | Peking University | L2-L3 | Needleman-Wunsch and Smith-Waterman alignment, sequence database search, Markov chains and hidden Markov models[^pku] |
| [[Inria - Bioinformatics Genomes and Algorithms]] | Inria (France) | L1-L2 | Pattern searching, sequence comparison, gene prediction with Markov chain models[^inria] |
| [[MIT 6.047 - Computational Biology]] | MIT | L3-M1 | "Genomes" part (alignment, hashing, HMMs, gene finding) and motifs with EM and Gibbs sampling[^mit6047] |
| [[MIT 7.91J - Foundations of Computational and Systems Biology]] | MIT | L3-M1 | Sequence alignment and motif finding[^mit791] |
| BIMM 181 Molecular Sequence Analysis, in [[UC San Diego - BS Bioinformatics]] | UC San Diego | L3 | The dedicated sequence analysis course of the major[^ucsd] |

## Reference books

- [[Bioinformatics Algorithms (Compeau)]]: "Where in the Genome Does DNA Replication Begin?" (items 1 to 4), "Which DNA Patterns Play the Role of Molecular Clocks?" (items 23 to 25), "How Do We Compare Biological Sequences?" (items 8 to 16, 21).[^compeau]
- [[Biological Sequence Analysis (Durbin)]]: ch. 2 (items 11 to 16, 20), ch. 3 (item 27), ch. 4 (item 35), ch. 5 (item 31), ch. 6 (items 21 and 22).[^durbin]
- [[Algorithms on Strings, Trees, and Sequences (Gusfield)]]: inexact matching, alignment and multiple string comparison, for the algorithmic depth of items 13 to 22.[^gusfield]
- [[An Introduction to Bioinformatics Algorithms (Jones)]]: design-technique view of alignment, space-efficient alignment (item 28) and BLAST-like heuristics.[^jones]

## Lab projects

- [[01-dna-engine]]: GC content, reverse complement, motif search.
- [[02-sequence-translation]]: reading frames and ORFs used by gene finding.
- [[04-alignment-engine]]: Needleman-Wunsch, Smith-Waterman, substitution matrices, gap penalties.
- [[05-sequence-search]]: k-mer index, seed and extend, a BLAST-like search, benchmarked.
- [[bio-algorithms]]: the shared implementations; [[bio-visualization]]: alignment views.

## References

The order (composition and motifs, then dynamic programming alignment, then heuristic search, then probabilistic models) follows the chapter progression of the two reference textbooks[^compeau][^durbin] and the course sequences above.[^coursera][^pku] Items 13, 14 and 19 are anchored in their landmark papers.[^nw][^sw][^blast]

[^ucsd]: [[UC San Diego - BS Bioinformatics]]: BIMM 181 Molecular Sequence Analysis opens the named upper-division bioinformatics sequence.
[^coursera]: [[Coursera UCSD - Bioinformatics Specialization]], courses I "Finding Hidden Messages in DNA" and III "Comparing Genes, Proteins, and Genomes".
[^pku]: [[Peking University - Bioinformatics Introduction and Methods]], parts on sequence alignment, database search and Markov models.
[^inria]: [[Inria - Bioinformatics Genomes and Algorithms]], parts on pattern searching, gene prediction and sequence comparison.
[^mit6047]: [[MIT 6.047 - Computational Biology]], "Genomes" and "Networks" parts.
[^mit791]: [[MIT 7.91J - Foundations of Computational and Systems Biology]], sequence analysis part.
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapters "Where in the Genome Does DNA Replication Begin?", "Which DNA Patterns Play the Role of Molecular Clocks?" and "How Do We Compare Biological Sequences?".
[^durbin]: [[Biological Sequence Analysis (Durbin)]], ch. 2 "Pairwise alignment", ch. 3 "Markov chains and hidden Markov models", ch. 4 "Pairwise alignment using HMMs", ch. 5 "Profile HMMs for sequence families", ch. 6 "Multiple sequence alignment methods".
[^gusfield]: [[Algorithms on Strings, Trees, and Sequences (Gusfield)]], parts on inexact matching and on multiple string comparison.
[^jones]: [[An Introduction to Bioinformatics Algorithms (Jones)]].
[^nw]: [[Needleman 1970 - Search for Similarities in Amino Acid Sequences]].
[^sw]: [[Smith 1981 - Identification of Common Molecular Subsequences]].
[^blast]: [[Altschul 1990 - Basic Local Alignment Search Tool]].
