---
aliases:
  - Foundations of Mathematics
  - Logic and Proofs
  - Fondements mathématiques
tags:
  - type/moc
  - domain/mathematics
  - level/L1
  - level/L2
prerequisites: []
projects:
  - "[[02-sequence-translation]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[MIT 6.042J - Mathematics for Computer Science]]"
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.03SC - Differential Equations]]"
  - "[[Stanford University - BS Biomedical Computation]]"
  - "[[University of Cambridge - Natural Sciences Tripos]]"
---

# Mathematical Foundations

> [!abstract]
> The language every other mathematical subject is written in: logic, sets, functions and relations, the exponential and logarithm, and how to read and write a proof.

## Why it matters for bioinformatics

- The genetic code is a [[Function]] from 64 codons to 21 symbols; gene sets, k-mer sets and Venn diagrams of hits are [[Set|sets]]; the Gene Ontology is a partial order ([[Binary Relation]]).
- The [[Logarithm]] is everywhere in data: log2 fold changes, Phred quality scores ($Q = -10 \log_{10} p$), log-likelihoods, information in bits.
- Algorithms (alignment, assembly, tree building) come with correctness arguments; reading them needs [[Proof Techniques]] and [[Mathematical Induction]].

## Before you start

Secondary-school algebra: manipulating expressions, solving equations, powers. No prerequisite MOC.

## Learning path

### Stage 1 - Foundations (L1)

1. [[Propositional Logic]] (L1): evaluate and, or, not, implication and equivalence with truth tables; negate a statement correctly. Bio: Boolean queries on databases (Entrez `AND`/`OR`/`NOT`), variant filters.
2. [[Predicate Logic]] (L1): read and write statements with "for all" and "there exists", and negate them. Bio: reading precise definitions (an open reading frame is a frame such that every codon before the stop...).
3. [[Set]] (L1): use union, intersection, complement, difference, Cartesian product and power set. Bio: overlaps of gene lists, shared k-mers between genomes.
4. [[Binary Relation]] (L1): recognize reflexive, symmetric, transitive relations; equivalence classes; partial orders. Bio: orthology groups as equivalence classes; the Gene Ontology `is_a` hierarchy as a partial order.
5. [[Function]] (L1): define domain, codomain, image; decide injective, surjective, bijective; compose and invert. Bio: the genetic code is surjective but not injective (degeneracy); reverse complement is a bijection that is its own inverse.
6. [[Summation Notation]] (L1): read and manipulate $\sum$ and $\prod$, index shifts, double sums. Bio: GC content, likelihoods as products over sites, log-likelihoods as sums.
7. [[Exponential Function]] (L1): use $e^x$ and $a^x$, their rules and graphs; recognize doubling and half-life. Bio: bacterial growth, PCR amplification ($2^n$ copies after $n$ cycles), mRNA decay.
8. [[Logarithm]] (L1): convert between bases, linearize exponentials, reason on log scales. Bio: log2 fold change, Phred scores, pH, bits of information.
9. [[Mathematical Proof]] (L1): tell a definition, theorem, lemma and proof apart; follow a proof line by line.
10. [[Proof Techniques]] (L1): write direct proofs, proofs by contrapositive, by contradiction and by cases. Bio: arguing that a greedy or dynamic-programming algorithm is correct.
11. [[Mathematical Induction]] (L1): prove statements for all $n$ with ordinary and strong induction. Bio: the number of edges of a tree, correctness of recursive algorithms, the number of unrooted binary trees.

### Stage 2 - Core (L2)

12. [[Boolean Algebra]] (L2): simplify logical expressions with algebraic laws and normal forms. Bio: Boolean network models of gene regulation.
13. [[Complex Number]] (L2): compute with $a + bi$, polar form and Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$. Bio: complex eigenvalues signal oscillations (gene circuits, predator-prey cycles); the Fourier transform in signal processing.

> [!tip] Order of study
> Do items 1 to 8 in the first weeks of Stage 1, in parallel with [[Calculus]]. Items 9 to 11 are best learned from the first third of MIT 6.042J with its problem sets, before [[Discrete Mathematics]] and [[Algorithms]].

## Uses from other domains

- [[Genetic Code]], [[Codon]] ([[Molecular Biology]]): the standard example of a non-injective [[Function]].
- [[Reverse Complement]] ([[Sequence Analysis]]): a bijection and an involution.
- [[Biological Ontology]] ([[Bioinformatics Foundations]]): partial orders and directed acyclic graphs.
- [[FASTQ Format]] ([[Bioinformatics Foundations]]) and [[Phred Quality Score]] ([[NGS Data Analysis]]): a [[Logarithm]] of error probabilities.
- [[Recursion]] ([[Algorithms]]): proved correct by [[Mathematical Induction]].
- [[Boolean Network]] ([[Systems Biology]]): gene regulation written in [[Boolean Algebra]].

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 6.042J - Mathematics for Computer Science]] | MIT | L1-L2 | First third: definitions, proofs, sets, functions, relations[^mcs] |
| [[MIT 18.03SC - Differential Equations]] | MIT | L2 | Unit II (characteristic equation), where complex numbers become necessary[^ode] |

## Reference books

- [[Mathematics for Computer Science (Lehman)]]: proofs part (definitions, proofs, induction, sets, functions, relations).[^lehman]
- [[Calculus (OpenStax)]]: Volume 1 opening material on functions, for exponential and logarithmic functions.[^openstax]

## Lab projects

- [[02-sequence-translation]]: the codon table as a function; frame arithmetic modulo 3.
- [[10-genomic-pipeline]]: Phred qualities and log-scaled likelihoods.

## References

[^mcs]: [[MIT 6.042J - Mathematics for Computer Science]]: the course opens with fundamental concepts (definitions, proofs, sets, functions, relations) before discrete structures, which sets the order of Stage 1.
[^lehman]: [[Mathematics for Computer Science (Lehman)]], proofs part: definitions, proofs, induction, sets, functions, relations.
[^openstax]: [[Calculus (OpenStax)]], Volume 1: functions, limits, derivatives, integration.
[^ode]: [[MIT 18.03SC - Differential Equations]], Unit II: modes and the characteristic equation.

Scope check: proof-based discrete mathematics is part of the mathematics minimum of computational programs such as Stanford's Biomedical Computation major (CS 103 Mathematical Foundations of Computing),[^stanford] and first-year mathematics for biologists starts from algebra.[^cam]

[^stanford]: [[Stanford University - BS Biomedical Computation]], mathematics block.
[^cam]: [[University of Cambridge - Natural Sciences Tripos]], Part IA Mathematical Biology (algebra, differential equations, modeling, matrix algebra, probability and statistics).
