---
aliases:
  - Stringology
  - Combinatorial Pattern Matching
  - Algorithmique du texte
tags:
  - type/moc
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Algorithms]]"
  - "[[Data Structures]]"
projects:
  - "[[01-dna-engine]]"
  - "[[03-genome-diff]]"
  - "[[04-alignment-engine]]"
  - "[[05-sequence-search]]"
  - "[[bio-algorithms]]"
sources:
  - "[[Inria - Bioinformatics Genomes and Algorithms]]"
  - "[[Rosalind]]"
  - "[[Algorithms on Strings, Trees, and Sequences (Gusfield)]]"
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[An Introduction to Bioinformatics Algorithms (Jones)]]"
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[Coursera JHU - Genomic Data Science Specialization]]"
  - "[[Coursera UCSD - Bioinformatics Specialization]]"
  - "[[MIT 6.006 - Introduction to Algorithms]]"
  - "[[MIT 6.047 - Computational Biology]]"
---

# String Algorithms

> [!abstract]
> Algorithms and indexes for strings: exact matching in linear time, distances and approximate matching, suffix trees and suffix arrays, the Burrows-Wheeler transform and FM-index, and the hashing and sampling schemes (rolling hashes, minimizers, sketches) that make genome-scale search possible.

## Why it matters for bioinformatics

A genome, a read and a protein are strings, and the hardest engineering in sequence bioinformatics is string engineering. [[Read Mapping]] tools index the reference with an [[FM-Index]] or with [[Minimizer|minimizers]]; homology search starts from exact [[K-mer]] seeds found in an [[Inverted Index]] ([[Seed and Extend]], [[BLAST]]); [[Sequence Alignment]] generalizes [[Edit Distance]]; [[Genome Assembly]] was first modeled as a [[Shortest Common Superstring]]; genome distances are estimated from [[MinHash]] sketches. Gusfield's reference text casts biological problems as string problems,[^gusfield] and the pattern-matching chapter of Compeau and Pevzner leads from suffix trees to the Burrows-Wheeler transform used by read mappers.[^compeau]

## Before you start

- [[Algorithms]]: [[Big O Notation]], [[Binary Search]], [[Sorting]], [[Radix Sort]], [[Dynamic Programming]], [[NP-Completeness]] (for Stage 3).
- [[Data Structures]]: [[String]], [[Array]], [[Hash Function]], [[Hash Table]], [[Tree (Data Structure)]], [[Trie]]; for Stage 3, [[Range Minimum Query]] and [[Succinct Data Structure]].
- [[Molecular Biology]]: [[DNA]] and [[Base Pairing]], to know why every search runs on both strands.

## Learning path

> [!tip] Order of study
> Implement the naive algorithm first and keep it as the test oracle: every faster method must return exactly the same occurrences on random DNA. Stage 2 is needed for [[04-alignment-engine]] and [[05-sequence-search]]; the Stage 3 index structures are what [[Read Mapping]] tools are made of.

### Stage 1 - Foundations (L1)

1. [[Exact Pattern Matching]] (L1): state the problem precisely (all occurrences, overlapping, both strands) and implement the naive O(nm) algorithm as the reference for every faster method.
2. [[Hamming Distance]] (L1): count mismatches between equal-length strings and find occurrences with at most k mismatches by brute force.

### Stage 2 - Core (L2)

3. [[Z-Algorithm]] (L2): compute the Z-values of a string in linear time and use them for exact matching; the fundamental preprocessing step behind the classical methods.
4. [[Knuth-Morris-Pratt Algorithm]] (L2): build the failure function and match in O(n + m) worst case without moving back in the text.
5. [[Boyer-Moore Algorithm]] (L2): skip alignments with the bad-character and good-suffix rules, and understand why it is sublinear on large alphabets but gains less on DNA.
6. [[Aho-Corasick Algorithm]] (L2): match a whole set of patterns (primers, adapters, barcodes) in one pass with a keyword trie and failure links.
7. [[Rolling Hash]] (L2): update the hash of a sliding window in O(1) and hash every k-mer of a genome, including canonical k-mers that merge both strands.
8. [[Rabin-Karp Algorithm]] (L2): match by comparing rolling hashes, verify candidates, and bound the cost of false positives.
9. [[Inverted Index]] (L2): map each k-mer to its positions, query it in expected O(1) per k-mer, and measure its memory on a real genome.
10. [[Edit Distance]] (L2): define Levenshtein distance, compute it by dynamic programming in O(nm) with traceback, and reduce memory to linear space.
11. [[Longest Common Subsequence]] (L2): solve it by dynamic programming and relate it to edit distance and to line-based diff tools.
12. [[Approximate Pattern Matching]] (L2): find occurrences within k edits by dynamic programming with a free start in the text, and filter candidates with the pigeonhole principle (exact seeds, then verification).
13. [[Suffix Tree]] (L2): build a suffix trie naively, compact it into a suffix tree of O(n) size, and answer substring, repeat and longest-common-substring queries.
14. [[Suffix Array]] (L2): sort all suffixes, find a pattern in O(m log n) by binary search, and compare memory with a suffix tree.
15. [[Burrows-Wheeler Transform]] (L2): compute the BWT from the suffix array, invert it with the last-to-first mapping, and explain why it compresses repetitive sequences.

### Stage 3 - Advanced (L3)

16. [[Ukkonen's Algorithm]] (L3): build a suffix tree online in linear time with suffix links and the skip-and-count trick.
17. [[Longest Common Prefix Array]] (L3): compute the LCP array in linear time (Kasai) and use it to emulate suffix-tree traversals on a suffix array.
18. [[Suffix Array Construction]] (L3): build suffix arrays by prefix doubling, then in linear time by induced sorting (SA-IS) or the skew algorithm.
19. [[FM-Index]] (L3): count and locate a pattern by backward search over the BWT with C and Occ tables and a sampled suffix array; the index inside BWA and Bowtie.
20. [[Bit-Parallel String Matching]] (L3): pack dynamic programming columns into machine words (Shift-And, Myers' bit-vector edit distance) for word-size speedups.
21. [[Minimizer]] (L3): keep one k-mer per window of w consecutive k-mers by minimum hash, compute the density, and see how it shrinks indexes for long-read mapping and metagenomic classification.
22. [[MinHash]] (L3): estimate the Jaccard similarity of two k-mer sets from small sketches and convert it into an evolutionary distance.
23. [[Data Compression]] (L3): relate entropy to compressibility, compare Huffman coding, LZ77 (gzip) and BWT-based compression, and see why reference-based compression wins on sequencing reads.
24. [[Shortest Common Superstring]] (L3): model assembly as the shortest common superstring, prove it NP-hard, and analyze the greedy merging heuristic.

### Stage 4 - Frontier (M1)

25. [[Run-Length Burrows-Wheeler Transform]] (M1): index highly repetitive collections such as pangenomes in space proportional to the number of BWT runs (r-index).
26. [[Wheeler Graph]] (M1): generalize the BWT and FM-index from strings to graphs, the idea behind pangenome graph indexes.

## Uses from other domains

- [[K-mer]] and [[Reverse Complement]] ([[Sequence Analysis]]): the unit indexed by inverted indexes, minimizers and sketches, and the reason for canonical k-mers.
- [[Pigeonhole Principle]] ([[Discrete Mathematics]]): the argument behind seed filtration in approximate matching.
- [[Modular Arithmetic]] and [[State Machine]] ([[Discrete Mathematics]]): the arithmetic of rolling hashes, and the automaton view of Knuth-Morris-Pratt and Aho-Corasick.
- [[Alignment-Free Sequence Comparison]] ([[Sequence Analysis]]) and [[Long-Read Alignment]] ([[NGS Data Analysis]]): where sketches and minimizers are applied.
- [[Shannon Entropy]] ([[Probability]]): the lower bound that data compression approaches.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[Inria - Bioinformatics Genomes and Algorithms]] | Inria | L1 | Pattern searching in genomic sequences with executable Python notebooks, in French or English; a gentle start for Stage 1[^inria] |
| [[Coursera JHU - Genomic Data Science Specialization]] | Johns Hopkins University | L2 | Course "Algorithms for DNA Sequencing": algorithms and data structures for analyzing DNA sequencing data (read mapping, assembly)[^jhu] |
| [[Coursera UCSD - Bioinformatics Specialization]] | UC San Diego | L2, L3 | Companion of Compeau and Pevzner: k-mers in course I, read mapping in course VI "Finding Mutations in DNA and Proteins"[^ucsdmooc] |
| [[Rosalind]] | Rosalind project | L1 to L3 | Stronghold problems and the problems of the Compeau and Pevzner course, including its pattern-matching chapter, checked automatically[^rosalind] |
| [[MIT 6.006 - Introduction to Algorithms]] | MIT | L2 | Hashing (lecture 4) and dynamic programming (lecture 15 onward), used throughout Stage 2[^mit6006] |
| [[MIT 6.047 - Computational Biology]] | MIT | L3 | Genomes part: sequence alignment and hashing for database search[^mit6047] |
| [[UC San Diego - BS Bioinformatics]] | UC San Diego | L3 | BIMM 181 Molecular Sequence Analysis, after CSE 100 and CSE 101[^ucsd] |

## Reference books

- [[Algorithms on Strings, Trees, and Sequences (Gusfield)]]: the reference for Stages 2 and 3. Exact matching part, then the suffix-tree part (ch. 7 "First Applications of Suffix Trees", ch. 9 "More Applications of Suffix Trees"), then inexact matching (ch. 12, ch. 13).[^gusfield]
- [[Introduction to Algorithms (Cormen)]] (4th ed.), ch. 32 "String Matching": the classical exact-matching algorithms with correctness proofs and complexity analysis.[^clrs]
- [[Bioinformatics Algorithms (Compeau)]], chapter "How Do We Locate Disease-Causing Mutations?": suffix trees, suffix arrays and the Burrows-Wheeler transform, motivated by read mapping.[^compeau]
- [[An Introduction to Bioinformatics Algorithms (Jones)]]: combinatorial pattern matching, exact and approximate, and BLAST-like heuristics.[^jones]

> [!info] Gap in the classic texts
> Gusfield (1997) predates the FM-index era of read mapping, and Jones and Pevzner (2004) predate next-generation sequencing indexes.[^gusfield][^jones] Stage 3 items from the FM-index onward rely on the Compeau and Pevzner chapter and on the original papers.

## Lab projects

- [[01-dna-engine]]: [[Exact Pattern Matching]] for motif search on both strands.
- [[03-genome-diff]]: [[Edit Distance]] and [[Longest Common Subsequence]] as the model of a sequence diff.
- [[04-alignment-engine]]: [[Hamming Distance]] and [[Edit Distance]] before scored alignment.
- [[05-sequence-search]]: naive search, then [[Inverted Index]] of k-mers, then seeds; later an [[FM-Index]] or [[Minimizer]] index as an extension.
- [[bio-algorithms]]: shared implementations of the distances and indexes.

## References

[^gusfield]: [[Algorithms on Strings, Trees, and Sequences (Gusfield)]]: exact matching, then suffix trees (ch. 7, ch. 9), then inexact matching and dynamic programming (ch. 12 "Refining Core String Edits and Alignments", ch. 13 "Extending the Core Problems"); the book casts biological problems as string problems and predates the Burrows-Wheeler and FM-index era.
[^clrs]: [[Introduction to Algorithms (Cormen)]], 4th ed., ch. 32 "String Matching".
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "How Do We Locate Disease-Causing Mutations?" (suffix trees, suffix arrays, Burrows-Wheeler transform, read mapping).
[^jones]: [[An Introduction to Bioinformatics Algorithms (Jones)]]: combinatorial pattern matching (exact and approximate matching, BLAST-like heuristics); published 2004, before next-generation sequencing indexes.
[^ucsd]: [[UC San Diego - BS Bioinformatics]]: CSE 100 Advanced Data Structures and CSE 101 Design and Analysis of Algorithms precede or accompany BIMM 181 Molecular Sequence Analysis.
[^inria]: [[Inria - Bioinformatics Genomes and Algorithms]]: the first part, on DNA and genomic sequences, covers pattern searching, with the algorithms run in Python notebooks.
[^jhu]: [[Coursera JHU - Genomic Data Science Specialization]]: the course "Algorithms for DNA Sequencing" covers algorithms and data structures for analyzing DNA sequencing data.
[^ucsdmooc]: [[Coursera UCSD - Bioinformatics Specialization]]: course I "Finding Hidden Messages in DNA" and course VI "Finding Mutations in DNA and Proteins"; companion textbook [[Bioinformatics Algorithms (Compeau)]].
[^rosalind]: [[Rosalind]]: the Bioinformatics Stronghold and the problems of the *Bioinformatics Algorithms* online course, whose textbook is [[Bioinformatics Algorithms (Compeau)]].
[^mit6006]: [[MIT 6.006 - Introduction to Algorithms]], Spring 2020: lecture 4 "Hashing", lecture 15 "Dynamic Programming, Part 1".
[^mit6047]: [[MIT 6.047 - Computational Biology]], Fall 2015: the Genomes part covers sequence alignment and hashing; 6.006 is a stated prerequisite.
