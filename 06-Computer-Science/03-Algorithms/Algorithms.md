---
aliases:
  - Design and Analysis of Algorithms
  - Algorithmique
tags:
  - type/moc
  - domain/computer-science
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Mathematical Foundations]]"
  - "[[Discrete Mathematics]]"
  - "[[Programming]]"
  - "[[Data Structures]]"
projects:
  - "[[01-dna-engine]]"
  - "[[04-alignment-engine]]"
  - "[[05-sequence-search]]"
  - "[[08-phylogenetic-engine]]"
  - "[[bio-algorithms]]"
sources:
  - "[[Rosalind]]"
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[MIT 6.042J - Mathematics for Computer Science]]"
  - "[[MIT 6.006 - Introduction to Algorithms]]"
  - "[[MIT 6.046J - Design and Analysis of Algorithms]]"
  - "[[Coursera Stanford - Algorithms Specialization]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[An Introduction to Bioinformatics Algorithms (Jones)]]"
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[MIT - Course 6-7 Computer Science and Molecular Biology]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[Shanghai Jiao Tong University - BS Bioinformatics]]"
---

# Algorithms

> [!abstract]
> How to design an algorithm, prove it correct and bound its cost: analysis and recursion, sorting and searching, divide and conquer, greedy and dynamic programming, graph algorithms, then intractability and the approximations and heuristics used when no efficient exact algorithm exists.

## Why it matters for bioinformatics

Core bioinformatics methods are textbook design paradigms applied to biological data. [[Sequence Alignment]] is dynamic programming on a grid graph ([[Needleman-Wunsch Algorithm]], [[Smith-Waterman Algorithm]]); [[Genome Assembly]] is a path problem in an overlap or [[De Bruijn Graph]]; [[Neighbor Joining]] is a greedy clustering; [[Maximum Parsimony]] and [[Multiple Sequence Alignment]] are NP-hard and solved by heuristics; [[BLAST]] is a heuristic by design. Knowing the paradigm lets you read a methods section, predict a tool's cost on a whole genome, and recognize when a problem has no efficient exact solution. The biology-driven textbooks are organized exactly this way, one design technique per biological problem.[^compeau][^jones] The computational programs of the [[Curriculum Benchmark]] whose course lists were verified all require an algorithms course, which sets the L3 target.[^mit67][^cmu][^ucsd][^sjtu]

## Before you start

- [[Mathematical Foundations]]: [[Proof Techniques]] (induction, contradiction), [[Function]], [[Logarithm]].
- [[Discrete Mathematics]]: [[Combinatorics]], [[Recurrence Relation]], [[Graph]], [[Directed Graph]], [[Directed Acyclic Graph]], [[Connected Component]], [[Tree (Graph Theory)]]. The proofs, graphs and counting material comes before algorithms;[^lehman] the rest runs in parallel with Stage 2.
- [[Probability]]: [[Random Variable]] and [[Expected Value]], for randomized algorithms and hashing (Stage 2).
- [[Data Structures]]: [[Array]], [[Hash Table]], [[Heap]], [[Graph Representation]], [[Disjoint-Set Data Structure]]. Study the two subdomains together.

## Learning path

> [!tip] Order of study
> Stage 1 is enough for [[01-dna-engine]] and [[02-sequence-translation]]. Do Stage 2 before [[04-alignment-engine]]: [[Dynamic Programming]] is the single most important item here, and the order (data structures, graphs, then dynamic programming, then intractability) follows 6.006 and 6.046J.[^mit6006][^mit6046] Implement every algorithm in Python and test it against a brute-force version on small random inputs.

### Stage 1 - Foundations (L1)

1. [[Model of Computation]] (L1): distinguish problem, algorithm and program, and count cost in the word-RAM model where each basic operation takes constant time.
2. [[Loop Invariant]] (L1): prove an iterative algorithm correct with an invariant (initialization, maintenance, termination).
3. [[Big O Notation]] (L1): describe growth with O, Ω and Θ, rank the common growth rates, and derive the worst-case running time of nested loops.
4. [[Space Complexity]] (L1): bound memory as well as time, in bytes for real inputs, and explain why a genome index must fit in RAM.
5. [[Recursion]] (L1): write recursive functions with base cases, trace the call stack, and know Python's recursion limit and when to rewrite iteratively.
6. [[Exhaustive Search]] (L1): enumerate every candidate (all k-mers, all motifs) as a correct baseline and estimate the input size at which it becomes infeasible.
7. [[Binary Search]] (L1): search a sorted array or a monotone predicate in O(log n) with correct boundary invariants.
8. [[Sorting]] (L1): implement insertion sort, merge sort, quicksort and heapsort, compare stability, memory and worst case, and know what Python's built-in sort guarantees.
9. [[Graph Traversal]] (L1): run breadth-first and depth-first search on an adjacency list to find reachable vertices, connected components and unweighted shortest paths.

### Stage 2 - Core (L2)

10. [[Divide and Conquer]] (L2): split, solve, combine: merge sort, Karatsuba multiplication, closest pair of points, linear-time selection.
11. [[Master Theorem]] (L2): solve divide-and-conquer recurrences with substitution, recursion trees and the master theorem.
12. [[Radix Sort]] (L2): beat the Ω(n log n) comparison lower bound with counting sort and radix sort over small alphabets such as {A, C, G, T}.
13. [[Amortized Analysis]] (L2): bound a sequence of operations with aggregate, accounting and potential arguments (dynamic arrays, union-find).
14. [[Randomized Algorithm]] (L2): analyze the expected cost of Las Vegas algorithms (randomized quicksort, quickselect) and the error probability of Monte Carlo algorithms.
15. [[Greedy Algorithm]] (L2): prove a greedy choice optimal with an exchange argument (interval scheduling, Huffman coding) and recognize when greedy fails.
16. [[Topological Sort]] (L2): order the vertices of a directed acyclic graph with depth-first search and detect cycles.
17. [[Shortest Path]] (L2): compute single-source shortest paths by DAG relaxation, Dijkstra and Bellman-Ford, then all-pairs shortest paths, and handle negative weights.
18. [[Minimum Spanning Tree]] (L2): build a minimum spanning tree with Kruskal or Prim, prove the cut property, and relate it to single-linkage clustering.
19. [[Dynamic Programming]] (L2): define subproblems, recurrence, evaluation order and base cases, reconstruct the solution by traceback, and see alignment as a longest path in a grid DAG.

### Stage 3 - Advanced (L3)

20. [[Network Flow]] (L3): compute maximum flow and minimum cut (Ford-Fulkerson, Edmonds-Karp) and reduce bipartite matching to flow.
21. [[Fast Fourier Transform]] (L3): multiply polynomials in O(n log n) by divide and conquer, the trick behind FFT-accelerated sequence correlation.
22. [[External Memory Algorithm]] (L3): analyze cost in block transfers and sort data larger than RAM with external merge sort, as coordinate-sorting a BAM file does.
23. [[NP-Completeness]] (L3): define P, NP and polynomial-time reductions, prove a problem NP-complete, and recognize NP-hard bioinformatics problems (shortest superstring, multiple alignment, maximum parsimony).
24. [[Approximation Algorithm]] (L3): design algorithms with a proven approximation ratio (vertex cover, set cover, greedy superstring) and interpret that ratio.
25. [[Branch and Bound]] (L3): solve NP-hard instances exactly by pruning a search tree with upper and lower bounds.
26. [[Heuristic Algorithm]] (L3): trade guarantees for speed deliberately, and evaluate a heuristic by sensitivity, specificity and runtime on benchmarks.

### Stage 4 - Frontier (M1)

27. [[Parameterized Complexity]] (M1): solve NP-hard problems in f(k)·poly(n) time when a parameter k is small (fixed-parameter tractability).

## Uses from other domains

- [[Eulerian Path]] and [[Hamiltonian Path]] ([[Discrete Mathematics]]): the first is found in linear time, the second is NP-complete; the contrast explains why assemblers moved from overlap graphs to de Bruijn graphs.[^compeau]
- [[Linear Programming]], [[Integer Linear Programming]] and [[Combinatorial Optimization]] ([[Optimization]]): exact formulations of NP-hard problems and the relaxations used to design approximation algorithms.
- [[Hidden Markov Model]] ([[Stochastic Processes]]): the Viterbi and forward algorithms are dynamic programming.
- [[Local Search]] and [[Simulated Annealing]] ([[Optimization]]): neighborhood moves, local optima and randomized escapes, used in phylogeny and structure search.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 6.042J - Mathematics for Computer Science]] | MIT | L1 | Proofs, graphs and counting before 6.006[^mit6042] |
| [[MIT 6.006 - Introduction to Algorithms]] | MIT | L2 | Models and data structures, graph algorithms (lecture 13 "Dijkstra's Algorithm"), dynamic programming (lecture 15, the SRTBOT framework)[^mit6006] |
| [[MIT 6.046J - Design and Analysis of Algorithms]] | MIT | L3 | Divide and conquer, randomization, dynamic programming, greedy algorithms, incremental improvement, complexity[^mit6046] |
| [[Rosalind]] | Rosalind project | L1 to L3 | Automatically checked problems: Bioinformatics Stronghold, and the problems of the Compeau and Pevzner course; practice for the algorithms that bioinformatics uses most[^rosalind] |
| [[Coursera Stanford - Algorithms Specialization]] | Stanford University | L2, L3 | Alternative track: divide and conquer and randomized algorithms; graph search and shortest paths; greedy, MST and dynamic programming (with sequence alignment); NP-completeness and what to do about it[^stanford] |

## Reference books

- [[Introduction to Algorithms (Cormen)]] (4th ed.): the reference for every item; ch. 14 "Dynamic Programming" and ch. 20 "Elementary Graph Algorithms" are the core of Stage 2, the NP-completeness and approximation chapters of Stage 3.[^clrs]
- [[Bioinformatics Algorithms (Compeau)]]: each paradigm motivated by a biological question; "How Do We Assemble Genomes?" (graph algorithms) and "How Do We Compare Biological Sequences?" (dynamic programming).[^compeau]
- [[An Introduction to Bioinformatics Algorithms (Jones)]]: the same material organized by design technique (exhaustive search, greedy, dynamic programming, divide and conquer, graphs).[^jones]
- [[Mathematics for Computer Science (Lehman)]]: proofs, graphs and counting before the analysis of algorithms.[^lehman]

## Lab projects

- [[01-dna-engine]]: linear-time scans and [[Big O Notation]] on sequences.
- [[04-alignment-engine]]: [[Dynamic Programming]] with traceback and linear-space variants.
- [[05-sequence-search]]: complexity and scaling from 100 to 1M sequences; heuristics versus exhaustive search.
- [[08-phylogenetic-engine]]: greedy clustering on distance matrices, then heuristic tree search.
- [[bio-algorithms]]: the shared, benchmarked implementations.

## References

[^clrs]: [[Introduction to Algorithms (Cormen)]], 4th ed., ch. 14 "Dynamic Programming", ch. 20 "Elementary Graph Algorithms"; foundations (growth of functions, divide and conquer, recurrences) come first and NP-completeness and approximation last, which sets the Stage 1 to Stage 3 order here.
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapters "How Do We Assemble Genomes?" (Eulerian paths, de Bruijn graphs) and "How Do We Compare Biological Sequences?" (dynamic programming, edit distance, alignment).
[^jones]: [[An Introduction to Bioinformatics Algorithms (Jones)]], organized by algorithmic idea: exhaustive search, greedy algorithms, dynamic programming, divide and conquer, graph algorithms.
[^lehman]: [[Mathematics for Computer Science (Lehman)]]: the proofs part, then graphs and counting, are the prerequisites for algorithms.
[^mit6042]: [[MIT 6.042J - Mathematics for Computer Science]]: taken before 6.006; priority to proofs, graphs and counting.
[^mit6006]: [[MIT 6.006 - Introduction to Algorithms]], Spring 2020: models and data structures, then graph algorithms, then dynamic programming; a stated prerequisite of MIT 6.047 Computational Biology.
[^mit6046]: [[MIT 6.046J - Design and Analysis of Algorithms]], Spring 2015: the sequel to 6.006 (stated prerequisite), from divide and conquer and randomization to complexity.
[^stanford]: [[Coursera Stanford - Algorithms Specialization]]: four courses, from divide and conquer and randomized algorithms to NP-complete problems and strategies for intractable problems; course 3 treats sequence alignment as dynamic programming.
[^rosalind]: [[Rosalind]]: Python Village, Bioinformatics Stronghold, Bioinformatics Armory, and the problems of the *Bioinformatics Algorithms* online course.
[^mit67]: [[MIT - Course 6-7 Computer Science and Molecular Biology]]: 6.1210 Introduction to Algorithms is part of the required CS foundation, next to the molecular biology core.
[^cmu]: [[Carnegie Mellon University - BS Computational Biology]]: 15-122, 15-251 and an algorithms course (15-451 or 15-351) are required before the computational genomics core.
[^ucsd]: [[UC San Diego - BS Bioinformatics]]: CSE 101 Design and Analysis of Algorithms sits in the same upper division as Molecular Sequence Analysis, so algorithms are learned just before or alongside sequence analysis.
[^sjtu]: [[Shanghai Jiao Tong University - BS Bioinformatics]]: algorithms appear twice, as general "Algorithms and Data Structures" and as "Principles of Algorithms in Bioinformatics"; this vault does the same by linking bioinformatics notes to this syllabus.
