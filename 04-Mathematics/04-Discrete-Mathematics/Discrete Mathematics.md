---
aliases:
  - Discrete Math
  - Combinatorics and Graph Theory
  - Mathématiques discrètes
tags:
  - type/moc
  - domain/mathematics
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Mathematical Foundations]]"
projects:
  - "[[01-dna-engine]]"
  - "[[02-sequence-translation]]"
  - "[[04-alignment-engine]]"
  - "[[05-sequence-search]]"
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[MIT 6.042J - Mathematics for Computer Science]]"
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[MIT - Course 6-7 Computer Science and Molecular Biology]]"
  - "[[Stanford University - BS Biomedical Computation]]"
---

# Discrete Mathematics

> [!abstract]
> Counting, modular arithmetic, recurrences and graphs: the mathematics of finite objects, which is the mathematics of sequences, trees and networks.

## Why it matters for bioinformatics

- **Sequences are discrete.** There are $4^k$ possible k-mers and $\binom{n+m}{n}$ monotone paths through an $n \times m$ alignment grid; counting tells you whether an exhaustive search is possible.
- **Graphs are the data structure of biology**: phylogenies are trees, genome assembly is an [[Eulerian Path]] in a de Bruijn graph, protein interactions and gene regulation are networks, the Gene Ontology is a directed acyclic graph.
- **Recurrences** are the mathematical form of dynamic programming (alignment, RNA folding) and of counting problems (how many trees on $n$ leaves?).

## Before you start

- [[Mathematical Foundations]]: [[Set]], [[Function]], [[Binary Relation]], [[Proof Techniques]], [[Mathematical Induction]].
- For items 10 and 21: [[Matrix]] and [[Eigenvalues and Eigenvectors]] from [[Linear Algebra]].

## Learning path

### Stage 1 - Foundations (L1)

1. [[Combinatorics]] (L1): apply the sum and product rules to count configurations. Bio: $4^n$ DNA sequences of length $n$, $20^n$ peptides; why a 12-mer is not unique in a 3 Gb genome but a 20-mer usually is.
2. [[Permutation]] (L1): count arrangements with and without repetition; compose permutations. Bio: shuffled sequences as null models; permutation tests; genome rearrangements as signed permutations.
3. [[Binomial Coefficient]] (L1): count subsets, use Pascal's rule and the binomial theorem; multinomial coefficients. Bio: ways to place $k$ mutations among $n$ sites; the number of monotone lattice paths through an alignment grid.
4. [[Pigeonhole Principle]] (L1): prove that some box must hold two objects. Bio: a read with $e$ errors split into $e + 1$ pieces has one exact piece, the basis of seed-based read mapping.
5. [[Inclusion-Exclusion Principle]] (L1): count unions of overlapping sets. Bio: genes hit by at least one of several screens; probability that at least one site mutates.
6. [[Modular Arithmetic]] (L1): compute with congruences and residues. Bio: reading frames as positions modulo 3; coordinates on a circular genome; rolling hashes of k-mers.
7. [[Graph]] (L1): define vertices, edges, degree, paths, cycles and weights; use the handshake lemma. Bio: protein-protein interaction, metabolic and co-expression networks.

### Stage 2 - Core (L2)

8. [[Recurrence Relation]] (L2): set up and solve linear recurrences; recognize the recurrence behind an algorithm. Bio: Fibonacci's rabbits (Rosalind FIB); the alignment and RNA-folding recurrences of [[Dynamic Programming]].
9. [[Directed Graph]] (L2): work with in- and out-degree, reachability and strongly connected components. Bio: who regulates whom in a gene regulatory network; pathways.
10. [[Adjacency Matrix]] (L2): represent a graph as a matrix and count walks with its powers; compare with adjacency lists. Bio: network data in matrix form.
11. [[Connected Component]] (L2): find the components of a graph. Bio: protein families as components of a sequence-similarity graph.
12. [[Bipartite Graph]] (L2): recognize two-part graphs and their properties. Bio: gene-disease and reaction-metabolite networks; reads assigned to genes.
13. [[Tree (Graph Theory)]] (L2): characterize trees ($n - 1$ edges, unique paths), rooted and unrooted, binary trees. Bio: phylogenies; there are $(2n-5)!!$ unrooted binary topologies on $n$ leaves, which is why tree search is heuristic.
14. [[Directed Acyclic Graph]] (L2): recognize DAGs and order them topologically. Bio: the Gene Ontology; workflow dependency graphs; the alignment grid as a DAG whose longest path is the best alignment.
15. [[Eulerian Path]] (L2): state Euler's degree condition and find a path using every edge once. Bio: genome assembly in a de Bruijn graph.
16. [[Hamiltonian Path]] (L2): define a path visiting every vertex once and see why it is hard. Bio: assembly in an overlap graph, and why assemblers moved to de Bruijn graphs.
17. [[State Machine]] (L2): model a process by states and transitions; prove properties with invariants. Bio: the automaton behind [[Knuth-Morris-Pratt Algorithm|KMP]] and regular-expression motifs (PROSITE); the state diagram of a hidden Markov model.

### Stage 3 - Advanced (L3)

18. [[Generating Function]] (L3): encode a sequence as a power series to count and solve recurrences. Bio: probability generating functions give the extinction probability of a branching process.
19. [[Catalan Number]] (L3): count non-crossing structures. Bio: the number of RNA secondary structures (non-crossing base pairings) and of binary tree shapes.
20. [[Clique (Graph Theory)]] (L3): define cliques and dense subgraphs; know that maximum clique is NP-hard. Bio: protein complexes as dense modules of interaction networks.
21. [[Graph Laplacian]] (L3): build $L = D - A$ and read its spectrum. Bio: spectral clustering of networks; network propagation of disease genes; smoothing on cell-cell neighbor graphs.
22. [[Random Graph]] (L3): generate Erdős-Rényi graphs and compare degree distributions with real networks. Bio: null models for biological networks.
23. [[De Bruijn Sequence]] (L3): construct a cyclic sequence containing every k-mer exactly once. Bio: the origin of de Bruijn graphs; protein-binding microarrays that cover all k-mers.

> [!tip] Order of study
> Items 1 to 7 fit in curriculum Stage 1 alongside [[Programming]]; items 8 to 17 belong to Stage 2, just before [[String Algorithms]] and [[Sequence Analysis]]. Implement each graph concept in Python (adjacency lists first) as soon as you learn it.

## Uses from other domains

- [[De Bruijn Graph]], [[Genome Assembly]] ([[Genomics]]): Eulerian paths.
- [[Phylogenetic Tree]] ([[Phylogenetics]]): trees and their counts.
- [[Biological Network]], [[Gene Regulatory Network]], [[Protein-Protein Interaction Network]], [[Metabolic Network]], [[Degree Distribution]], [[Scale-Free Network]], [[Network Centrality]] ([[Systems Biology]]): graphs, directed graphs, cliques, Laplacians, random-graph null models.
- [[Graph Traversal]], [[Shortest Path]], [[Minimum Spanning Tree]], [[Dynamic Programming]], [[NP-Completeness]] ([[Algorithms]]): algorithms on these structures.
- [[Tree (Data Structure)]], [[Graph Representation]] ([[Data Structures]]): how trees and graphs are stored.
- [[RNA Secondary Structure]]: non-crossing structures counted by the [[Catalan Number]].
- [[Seed and Extend]] ([[Sequence Analysis]]): the pigeonhole argument behind seeds.
- [[Biological Ontology]] ([[Bioinformatics Foundations]]) and [[Workflow Management System]] ([[Bioinformatics Engineering]]): DAGs.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 6.042J - Mathematics for Computer Science]] | MIT | L1-L2 | Discrete structures (graphs, state machines, modular arithmetic) and counting[^mcs] |

## Reference books

- [[Mathematics for Computer Science (Lehman)]]: structures part (number theory and modular arithmetic, graphs, state machines, counting).[^lehman]
- [[Bioinformatics Algorithms (Compeau)]]: "How Do We Assemble Genomes?" (Eulerian paths, de Bruijn graphs) as the biological motivation for items 14 to 16.[^compeau]
- [[Introduction to Algorithms (Cormen)]]: graph representations and algorithms, for the algorithmic side of items 7 to 14.

## Lab projects

- [[01-dna-engine]]: strings over $\{A, C, G, T\}$, counting and frequencies.
- [[02-sequence-translation]]: frame arithmetic modulo 3.
- [[04-alignment-engine]]: alignment as a longest path in a grid-shaped DAG.
- [[05-sequence-search]]: k-mer counts and the pigeonhole argument for seeds.
- [[08-phylogenetic-engine]]: trees and their enumeration.

## References

[^mcs]: [[MIT 6.042J - Mathematics for Computer Science]]: fundamental concepts, then discrete structures (graphs, state machines, modular arithmetic, counting), then discrete probability.
[^lehman]: [[Mathematics for Computer Science (Lehman)]], structures part.
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "How Do We Assemble Genomes?".

Scope check: discrete mathematics is part of the core of computational programs (MIT 6-7 requires Mathematics for Computer Science;[^mit67] Stanford's Biomedical Computation requires CS 103 Mathematical Foundations of Computing[^stanford]). Graph theory is given L3 depth here because assembly, phylogenetics and systems biology all rely on it.

[^mit67]: [[MIT - Course 6-7 Computer Science and Molecular Biology]], mathematics and introductory CS block.
[^stanford]: [[Stanford University - BS Biomedical Computation]], mathematics block.
