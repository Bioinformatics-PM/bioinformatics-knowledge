---
aliases:
  - Structures de données
tags:
  - type/moc
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Programming]]"
  - "[[Mathematical Foundations]]"
projects:
  - "[[01-dna-engine]]"
  - "[[02-sequence-translation]]"
  - "[[05-sequence-search]]"
  - "[[08-phylogenetic-engine]]"
  - "[[09-genome-browser]]"
  - "[[bio-core]]"
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[MIT 6.006 - Introduction to Algorithms]]"
  - "[[Coursera Stanford - Algorithms Specialization]]"
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[Shanghai Jiao Tong University - BS Bioinformatics]]"
---

# Data Structures

> [!abstract]
> How to organize data so that the operations an algorithm needs are fast: sequences, hash-based sets and maps, trees and priority queues, graph and interval structures, then the compact and probabilistic structures that make genome-scale indexes fit in memory.

## Why it matters for bioinformatics

The right structure turns an infeasible analysis into a routine one. A codon table and a k-mer counter are [[Hash Table|hash tables]]; a phylogeny is a [[Tree (Data Structure)|tree]]; a genome browser answers overlap queries with an [[Interval Tree]]; assemblers store millions of k-mers in [[Bloom Filter|Bloom filters]] and [[Graph Representation|compact graphs]]; the [[FM-Index]] of a read mapper is built on [[Succinct Data Structure|rank and select bit vectors]]. Computational biology and bioinformatics majors require a data-structures course before or next to their sequence analysis courses.[^ucsd][^cmu][^sjtu]

## Before you start

- [[Programming]]: [[Python Programming]] and the [[Python Object Model]] (references, mutability, memory cost of objects).
- [[Mathematical Foundations]]: [[Set]], [[Function]], [[Logarithm]].
- [[Algorithms]]: [[Big O Notation]] and [[Recursion]], studied in parallel; [[Amortized Analysis]] for Stage 2.
- [[Probability]]: [[Expected Value]] and [[Conditional Probability]], for hashing and the false-positive rates of Stage 3.

## Learning path

> [!tip] Order of study
> You already use lists and dicts daily: in Stage 1, focus on the cost model behind them, not on the API. Implement each structure once by hand, then use the library version (`dict`, `collections.deque`, `heapq`, `bisect`).

### Stage 1 - Foundations (L1)

1. [[Abstract Data Type]] (L1): separate an interface (sequence, set, map, priority queue) from its implementation, and choose an implementation by the operations you need.
2. [[Array]] (L1): exploit contiguous memory for O(1) indexing and explain the amortized O(1) append of a dynamic array such as a Python list.
3. [[Linked List]] (L1): implement singly and doubly linked lists and explain why they rarely beat arrays on modern caches.
4. [[Stack]] (L1): use last-in first-out order to parse nested structures (Newick trees, brackets) and to replace recursion.
5. [[Queue]] (L1): use first-in first-out order and double-ended queues for breadth-first search and sliding windows over a sequence.
6. [[String]] (L1): treat a sequence as a string over an alphabet; know `str` versus `bytes`, immutability, the cost of slicing and concatenation, and when a byte array is better.
7. [[Hash Function]] (L1): state what makes a good hash (uniform, fast, deterministic), tell non-cryptographic hashes from checksums, and meet universal hashing.
8. [[Hash Table]] (L1): implement a map with chaining or open addressing, reason about load factor and expected O(1) operations, and use `dict`, `set` and `Counter` for codon tables and k-mer counts.

### Stage 2 - Core (L2)

9. [[Tree (Data Structure)]] (L2): represent rooted trees with child lists or parent pointers, traverse them in pre-, in- and post-order, and serialize them.
10. [[Binary Search Tree]] (L2): support ordered-set operations (search, insert, delete, predecessor, range query) in O(h).
11. [[Balanced Binary Search Tree]] (L2): keep the height in O(log n) with AVL rotations or red-black rules, and augment nodes with subtree data (sizes, maxima).
12. [[Heap]] (L2): keep a binary heap in an array, build it in O(n), and use it as a priority queue (Dijkstra, merging sorted files, top-k hits).
13. [[Graph Representation]] (L2): store a graph as adjacency lists, an adjacency matrix or compressed sparse rows, and choose by density and memory for graphs with millions of nodes.
14. [[Disjoint-Set Data Structure]] (L2): implement union-find with union by rank and path compression, for connected components, Kruskal's algorithm and clustering.
15. [[Trie]] (L2): store a set of strings in a prefix tree for prefix queries; the keyword tree behind Aho-Corasick and the ancestor of the suffix tree.
16. [[Interval Tree]] (L2): answer overlap queries on genomic intervals in O(log n + k), and compare with a sorted array plus binary search.

### Stage 3 - Advanced (L3)

17. [[B-Tree]] (L3): keep a balanced tree of wide nodes sized to disk or cache blocks; the structure behind database indexes.
18. [[Range Minimum Query]] (L3): answer range minima in O(1) after preprocessing (sparse table), and reduce lowest common ancestor queries on trees to it.
19. [[Bloom Filter]] (L3): test set membership in little memory with a tunable false-positive rate and no false negatives, as k-mer indexes do.[^stanford]
20. [[Count-Min Sketch]] (L3): estimate item frequencies (k-mer counts) in sublinear memory, with one-sided error, in a single streaming pass.
21. [[Succinct Data Structure]] (L3): support rank and select on bit vectors with o(n) extra bits, the building block of FM-index occurrence tables and wavelet trees.

## Uses from other domains

- [[Graph]], [[Adjacency Matrix]] and [[Tree (Graph Theory)]] ([[Discrete Mathematics]]): the mathematical objects that [[Graph Representation]] and [[Tree (Data Structure)]] implement.
- [[Newick Format]] ([[Bioinformatics Foundations]]): the text serialization of a tree, parsed with a [[Stack]].
- [[BED Format]], [[GFF Format]], [[Genomic Coordinate System]] and [[Genomic Interval Arithmetic]] ([[Bioinformatics Foundations]]): the interval data and operations that [[Interval Tree]] accelerates.
- [[Data Integrity]] ([[Research Data Management]]): file checksums, a cryptographic use of [[Hash Function|hash functions]].

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 6.006 - Introduction to Algorithms]] | MIT | L2 | Data structures part of the course, including lecture 4 "Hashing"[^mit6006] |
| [[Coursera Stanford - Algorithms Specialization]] | Stanford University | L2 | Course 2: heaps, search trees, hash tables and Bloom filters[^stanford] |
| [[UC San Diego - BS Bioinformatics]] | UC San Diego | L2 | CSE 100 Advanced Data Structures, required in the bioinformatics major[^ucsd] |

## Reference books

- [[Introduction to Algorithms (Cormen)]] (4th ed.): hash tables and search trees, then the advanced data structures; the standard reference for proofs and complexity.[^clrs]

## Lab projects

- [[01-dna-engine]]: [[String]] as an immutable, validated sequence type.
- [[02-sequence-translation]]: [[Hash Table]] as the codon lookup table.
- [[05-sequence-search]]: [[Hash Table]] as the k-mer index; [[Bloom Filter]] as an extension.
- [[08-phylogenetic-engine]]: [[Tree (Data Structure)]] for phylogenies and their serialization.
- [[09-genome-browser]]: [[Interval Tree]] for annotation and variant tracks.
- [[bio-core]]: the typed domain objects built on these structures.

## References

[^clrs]: [[Introduction to Algorithms (Cormen)]], 4th ed.: hash tables and binary search trees in the sorting and data-structures parts; to be read with the algorithms that use them.
[^mit6006]: [[MIT 6.006 - Introduction to Algorithms]], Spring 2020: data structures before graph algorithms and dynamic programming; lecture 4 "Hashing".
[^stanford]: [[Coursera Stanford - Algorithms Specialization]], course 2 "Graph Search, Shortest Paths, and Data Structures": heaps, search trees, hash tables, Bloom filters.
[^ucsd]: [[UC San Diego - BS Bioinformatics]]: CSE 100 Advanced Data Structures is required in the upper division, alongside the sequence analysis course.
[^cmu]: [[Carnegie Mellon University - BS Computational Biology]]: 15-122 Principles of Imperative Computation is part of the required computer science core.
[^sjtu]: [[Shanghai Jiao Tong University - BS Bioinformatics]]: "Algorithms and Data Structures" is part of the computer science core of the major.
