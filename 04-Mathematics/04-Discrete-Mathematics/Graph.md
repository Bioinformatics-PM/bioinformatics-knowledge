---
aliases:
  - Graph Theory
  - Network
  - Undirected Graph
  - Simple Graph
  - Vertex
  - Node
  - Edge
  - Handshake Lemma
  - Weighted Graph
  - Graphe
tags:
  - type/concept
  - domain/mathematics
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Set]]"
  - "[[Binary Relation]]"
  - "[[Function]]"
  - "[[Binomial Coefficient]]"
related:
  - "[[Graph Traversal]]"
  - "[[Graph Representation]]"
  - "[[Directed Graph]]"
  - "[[Adjacency Matrix]]"
  - "[[Connected Component]]"
  - "[[Bipartite Graph]]"
  - "[[Tree (Graph Theory)]]"
  - "[[Biological Network]]"
  - "[[Protein-Protein Interaction Network]]"
  - "[[Metabolic Network]]"
  - "[[Gene Co-Expression Network]]"
  - "[[De Bruijn Graph]]"
projects:
  - "[[04-alignment-engine]]"
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[MIT 6.042J - Mathematics for Computer Science]]"
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[MIT 6.006 - Introduction to Algorithms]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Barabási 2004 - Network Biology]]"
  - "[[Stuart 2003 - A Gene-Coexpression Network]]"
---

# Graph

> [!abstract]
> A graph is a set of objects (vertices) and a set of pairwise links between them (edges); proteins and their interactions, genes and their co-expression, reads and their overlaps all become graphs, and counting degrees, following paths and finding cycles become questions about the biology.

## Definition

A **(simple, undirected) graph** $G = (V, E)$ consists of a finite non-empty set $V$ of **vertices** (or nodes) and a set $E$ of **edges**, each edge being a set $\{u, v\}$ of two distinct vertices. The edge $\{u, v\}$ **joins** $u$ and $v$, which are **adjacent** (neighbours) and **incident** to the edge. The **degree** $\deg(v)$ is the number of edges incident to $v$.[^lehman][^mcs] Common variants:[^lehman][^clrs]

- **directed graph**: edges are ordered pairs $(u, v)$, from a tail $u$ to a head $v$ ([[Directed Graph]]);
- **weighted graph**: a function $w : E \to \mathbb{R}$ gives each edge a number (cost, distance, similarity, confidence);
- **multigraph**: repeated edges or loops $\{v, v\}$ are allowed (excluded from simple graphs).

## Why it matters

- **Biological networks.** Cellular networks are graphs: proteins linked by physical interactions, metabolites linked by reactions, regulators linked to the genes they control,[^barabasi] genes linked when their expression profiles are correlated across many samples.[^stuart] Network biology studies them with the vocabulary of this note ([[Biological Network]]).
- **Sequence algorithms are graph algorithms.** Genome assembly searches paths in graphs built from reads or k-mers ([[De Bruijn Graph]], [[Eulerian Path]]);[^compeau-asm] pairwise alignment is a longest path through a grid-shaped graph ([[Directed Acyclic Graph]], [[04-alignment-engine]]);[^compeau-align] phylogenies are trees ([[Tree (Graph Theory)]], [[08-phylogenetic-engine]]).
- **Algorithms and storage.** Traversal, shortest paths and components ([[Graph Traversal]], [[Shortest Path]], [[Connected Component]]) are standard algorithms whose cost depends on how the graph is stored ([[Graph Representation]]).[^clrs][^6006]

## Core (L1)

### Vocabulary

- The **neighbourhood** $N(v)$ is the set of vertices adjacent to $v$; in a simple graph $\deg(v) = |N(v)|$.
- A vertex of degree 0 is **isolated**; a vertex of degree 1 is a **leaf** (or pendant vertex).
- In network biology, a **hub** is a vertex of unusually high degree; many cellular networks have a few hubs and many poorly connected vertices.[^barabasi]

![[toy-ppi-network-degrees.svg]]

*Toy protein-protein interaction network (invented data), used throughout this note: 8 proteins, 8 interactions, the degree of each protein under its name.*

### The handshake lemma

$$\sum_{v \in V} \deg(v) = 2\,|E|.$$

**Proof (double counting).** Count the pairs $(v, e)$ with $v$ an endpoint of edge $e$. Grouping by vertex gives $\sum_v \deg(v)$; grouping by edge gives $2|E|$, since every edge has exactly two endpoints. Both count the same set. $\square$[^lehman]

Consequences:

- **The number of odd-degree vertices is even.** The sum of all degrees is even, the even degrees contribute an even amount, so the odd degrees must sum to an even number, which requires an even count of them.
- **Mean degree** $= 2|E|/|V|$.
- **At most $\binom{n}{2}$ edges** on $n$ vertices, one per pair ([[Binomial Coefficient]]); the **density** $|E|/\binom{n}{2}$ is the fraction of possible edges present.

In the toy network: $4 + 2 + 2 + 2 + 2 + 3 + 1 + 0 = 16 = 2 \times 8$; the odd-degree vertices are P6 and P7 (two of them); mean degree $16/8 = 2$; density $8/28 \approx 0.29$.

### Walks, paths, cycles, connectivity

- A **walk** of length $k$ is a sequence $v_0, v_1, \dots, v_k$ with $\{v_{i-1}, v_i\} \in E$ for every $i$. Its length counts edges, not vertices.
- A **path** is a walk with no repeated vertex. A **cycle** is a walk $v_0, \dots, v_k = v_0$ with $k \ge 3$ whose vertices $v_0, \dots, v_{k-1}$ are distinct.[^lehman]
- The **distance** $d(u, v)$ is the length of a shortest path from $u$ to $v$ ($\infty$ if there is none). $G$ is **connected** if every pair of vertices is joined by a path; the maximal connected pieces are its **connected components** ([[Connected Component]]).

In the toy network, P2, P1, P4, P6, P7 is a path of length 4, and it is a shortest one: $d(\text{P2}, \text{P7}) = 4$. P1, P2, P3 is a cycle of length 3 and P1, P4, P6, P5 a cycle of length 4. There are two components, $\{P1, \dots, P7\}$ and $\{P8\}$. Computing distances and components on large graphs is the job of breadth-first and depth-first search ([[Graph Traversal]]).

### Weighted graphs

A weight $w(e)$ can mean a cost (a distance, a reaction's free energy, an evolutionary distance), in which case short paths of small total weight matter ([[Shortest Path]]), or a strength (a correlation, a confidence score), in which case edges below a threshold are often removed. The weight of a path is the sum of its edge weights. Always state what a weight means before running an algorithm on it.

### Bio: four biological networks

| Network | Vertices | An edge means | Kind of graph |
|---|---|---|---|
| Protein-protein interaction | proteins | the two proteins physically interact[^barabasi] | undirected, sometimes weighted by confidence |
| Metabolic | metabolites (and reactions) | a reaction converts one into the other[^barabasi] | directed; bipartite when reactions are vertices too |
| Co-expression | genes | expression profiles correlated across samples[^stuart] | undirected, weighted by correlation |
| Gene regulatory | regulators and target genes | the regulator controls the target's expression[^barabasi] | directed |

Stuart and colleagues built a co-expression network from pairs of genes coexpressed over 3,182 DNA microarrays from humans, flies, worms and yeast, and kept 22,163 coexpression relationships conserved across evolution, as evidence that the linked genes are functionally related.[^stuart] Details of each network type belong to [[Protein-Protein Interaction Network]], [[Metabolic Network]], [[Gene Co-Expression Network]] and [[Gene Regulatory Network]].

## Deeper (L2)

### Directed graphs

Each directed edge $(u, v)$ leaves $u$ and enters $v$, so a vertex has an **out-degree** and an **in-degree**, and the handshake argument gives $\sum_v \deg^+(v) = \sum_v \deg^-(v) = |E|$ (every edge has exactly one tail and one head). In a regulatory network, out-degree counts targets and in-degree counts regulators. Reachability, strongly connected components and acyclicity are developed in [[Directed Graph]] and [[Directed Acyclic Graph]].

### Representations

| Operation | Edge list | Adjacency list | Adjacency matrix |
|---|---|---|---|
| memory | $\Theta(\lvert E \rvert)$ | $\Theta(\lvert V \rvert + \lvert E \rvert)$ | $\Theta(\lvert V \rvert^2)$ |
| is $\{u, v\}$ an edge? | $O(\lvert E \rvert)$ | $O(\deg u)$ | $O(1)$ |
| list the neighbours of $u$ | $O(\lvert E \rvert)$ | $O(\deg u)$ | $O(\lvert V \rvert)$ |

Adjacency lists are preferred for **sparse** graphs, where $|E|$ is much smaller than $|V|^2$, and matrices for dense graphs or when edge queries must be constant-time.[^clrs] In Python, a dictionary of sets combines both advantages for most uses: neighbours in $O(\deg u)$ and edge tests in expected $O(1)$ ([[Hash Table]]). Biological interaction networks are typically sparse: a hypothetical network of 20,000 proteins with 100,000 interactions would fill a 400-million-cell matrix to a density of 0.05 % (Exercise 3). The matrix still matters for theory: it is symmetric with a zero diagonal, its row sums are the degrees, and the entries of $A^k$ count walks of length $k$[^lehman] ([[Adjacency Matrix]]).

### Bipartite graphs

A graph is **bipartite** if $V$ splits into two parts $L$ and $R$ with every edge joining $L$ to $R$. Metabolites and reactions, genes and diseases, reads and the genes they are assigned to form bipartite graphs. A graph is bipartite if and only if it has no cycle of odd length;[^lehman] the toy network is not, because of the triangle P1, P2, P3 (Exercise 4). Projecting a bipartite graph onto one side (two metabolites adjacent when they share a reaction) creates many triangles, a pitfall developed in [[Bipartite Graph]].

### Trees

A **tree** is a connected graph with no cycle. Equivalently, it is connected with exactly $|V| - 1$ edges, or any two of its vertices are joined by exactly one path.[^lehman] Phylogenetic trees put sequences at the leaves and ancestors at the internal vertices ([[Phylogenetic Tree]]). The handshake lemma already says something about every tree: with $|E| = n - 1$ the degrees sum to $2n - 2$, which forces at least two leaves when $n \ge 2$ (Exercise 2). Rooted trees, binary trees and their counts are in [[Tree (Graph Theory)]].

## Advanced (L3)

### Graph problems that are bioinformatics problems

| Problem | Graph | Biological use | Note |
|---|---|---|---|
| path using every edge once | de Bruijn graph of k-mers | genome assembly[^compeau-asm] | [[Eulerian Path]] |
| path visiting every vertex once | overlap graph of reads | earlier assembly formulation[^compeau-asm] | [[Hamiltonian Path]] |
| longest path in an acyclic graph | alignment grid | pairwise alignment[^compeau-align] | [[Directed Acyclic Graph]] |
| shortest path | weighted network | distances between proteins, pathways | [[Shortest Path]] |
| connected components | sequence-similarity graph | protein families | [[Connected Component]] |
| dense subgraphs, cliques | interaction network | candidate protein complexes | [[Clique (Graph Theory)]] |

The first two rows illustrate a central lesson of algorithms: an Eulerian path can be found efficiently, while no efficient algorithm is known for the Hamiltonian path problem, which is why assemblers moved from overlap graphs to de Bruijn graphs.[^compeau-asm] Modelling a biological question as the *right* graph problem decides whether it is tractable ([[NP-Completeness]]).

### Degree distributions and null models

The **degree distribution** $P(k)$ is the fraction of vertices of degree $k$ ([[Degree Distribution]]). Whether a network property is surprising (many triangles, hubs linked to each other) is judged against random graphs with the same number of vertices and edges, or with the same degrees ([[Random Graph]]). The second kind is generated by **degree-preserving edge swaps**: replace edges $\{a, b\}, \{c, d\}$ by $\{a, d\}, \{c, b\}$; each of $a, b, c, d$ loses one edge and gains one, so every degree is unchanged (Exercise 5). This is the graph analogue of the composition-preserving shuffle of a sequence ([[Permutation]]). Claims about network architecture, such as scale-free degree distributions, are discussed critically in [[Scale-Free Network]].

### A network is a measurement

An edge list records what an assay detected or what a threshold kept. A missing edge may be an untested pair, and the edges of a co-expression network change with the correlation cutoff. Record the data source, the version and the threshold with every network, as with any other dataset.

## Mathematical representation

- $G = (V, E)$ with $E \subseteq \{\{u, v\} : u, v \in V,\ u \ne v\}$. Adjacency is a symmetric, irreflexive [[Binary Relation]] on $V$; conversely every such relation defines a simple graph.
- $N(v) = \{u : \{u, v\} \in E\}$, $\deg(v) = |N(v)|$.
- **Handshake lemma.** With $I = \{(v, e) \in V \times E : v \in e\}$: $|I| = \sum_{v} \deg(v)$ and $|I| = \sum_{e} |e| = 2|E|$.
- **Every walk contains a path.** If a walk from $u$ to $v$ repeats a vertex, $v_i = v_j$ with $i < j$, deleting $v_{i+1}, \dots, v_j$ leaves a shorter walk from $u$ to $v$; repeating this terminates with a path. Hence "some walk joins $u$ and $v$" and "some path joins $u$ and $v$" are equivalent.
- **Adjacency matrix.** Number the vertices $1..n$ and set $A_{uv} = 1$ if $\{u, v\} \in E$, else 0. Then $A = A^{\mathsf T}$, $A_{vv} = 0$, $\sum_u A_{vu} = \deg(v)$ and $\sum_{u,v} A_{uv} = 2|E|$.
- **Directed and weighted.** A directed graph has $E \subseteq V \times V$ with $\sum_v \deg^+(v) = \sum_v \deg^-(v) = |E|$; a weighted graph adds $w : E \to \mathbb{R}$, and a path $P$ has weight $w(P) = \sum_{e \in P} w(e)$.

## Computational representation

The adjacency list as a dictionary of sets is the default Python representation; the matrix and the edge list are derived from it as needed.

```python
from collections import Counter

EDGES = [("P1", "P2"), ("P1", "P3"), ("P1", "P4"), ("P1", "P5"),
         ("P2", "P3"), ("P4", "P6"), ("P5", "P6"), ("P6", "P7")]    # invented toy network
VERTICES = [f"P{i}" for i in range(1, 9)]                            # P8 has no partner

def adjacency_list(vertices, edges):
    """Undirected simple graph as a dict: vertex -> set of neighbours."""
    adj = {v: set() for v in vertices}
    for u, v in edges:
        if u == v or v in adj[u]:
            raise ValueError(f"not a simple graph: {u}-{v}")
        adj[u].add(v)
        adj[v].add(u)
    return adj

adj = adjacency_list(VERTICES, EDGES)
deg = {v: len(adj[v]) for v in VERTICES}
print(deg)
print(sum(deg.values()), 2 * len(EDGES), [v for v in VERTICES if deg[v] % 2])
n, m = len(VERTICES), len(EDGES)
print("density", round(m / (n * (n - 1) / 2), 3), "mean degree", 2 * m / n)
print(sorted(Counter(deg.values()).items()))                         # degree distribution

idx = {v: i for i, v in enumerate(VERTICES)}
A = [[0] * n for _ in range(n)]
for u, v in EDGES:
    A[idx[u]][idx[v]] = A[idx[v]][idx[u]] = 1
print([sum(row) for row in A] == list(deg.values()),
      all(A[i][j] == A[j][i] for i in range(n) for j in range(n)))

def is_path(adj, walk):
    """Consecutive vertices adjacent and no vertex repeated."""
    return all(b in adj[a] for a, b in zip(walk, walk[1:])) and len(set(walk)) == len(walk)

def is_cycle(adj, walk):
    """walk = v0 ... v(k-1) with k >= 3 distinct vertices and an edge from v(k-1) back to v0."""
    return len(walk) >= 3 and is_path(adj, walk) and walk[0] in adj[walk[-1]]

print(is_path(adj, ["P2", "P1", "P4", "P6", "P7"]), is_cycle(adj, ["P1", "P4", "P6", "P5"]),
      is_cycle(adj, ["P1", "P2", "P4"]))

W = {("G1", "G2"): 0.91, ("G2", "G3"): 0.84, ("G1", "G3"): 0.62}   # invented correlations
wadj = {}
for (u, v), w in W.items():
    wadj.setdefault(u, {})[v] = w
    wadj.setdefault(v, {})[u] = w
print(wadj["G2"], sum(wadj["G2"].values()))

REG = [("T1", "T2"), ("T1", "g1"), ("T2", "g1"), ("T2", "g2"), ("g2", "T1")]  # invented, directed
out_deg = Counter(u for u, _ in REG)
in_deg = Counter(v for _, v in REG)
print(dict(out_deg), dict(in_deg), sum(out_deg.values()), sum(in_deg.values()))
```

```text
{'P1': 4, 'P2': 2, 'P3': 2, 'P4': 2, 'P5': 2, 'P6': 3, 'P7': 1, 'P8': 0}
16 16 ['P6', 'P7']
density 0.286 mean degree 2.0
[(0, 1), (1, 1), (2, 4), (3, 1), (4, 1)]
True True
True True False
{'G1': 0.91, 'G3': 0.84} 1.75
{'T1': 2, 'T2': 2, 'g2': 1} {'T2': 1, 'g1': 2, 'g2': 1, 'T1': 1} 5 5
```

Reading the output: the handshake lemma holds, the degree distribution has one vertex of each degree 0, 1, 3, 4 and four of degree 2, and the matrix row sums equal the degrees. For a weighted vertex, the sum of its edge weights (here 1.75 for G2) is its **strength**. In the directed example, out-degrees and in-degrees both sum to the 5 edges. Real networks are read from tab-separated edge lists into the same structures, or with a library such as NetworkX once the concepts are clear.

## Worked example

> [!example] Reading the toy interaction network (invented data)
> 1. **Degrees**: P1 4, P6 3, P2 to P5 2 each, P7 1, P8 0. P1 is the hub, P7 a leaf, P8 isolated.
> 2. **Handshake check**: sum 16 $= 2 \times 8$ edges. Odd degrees at P6 (3) and P7 (1): two vertices, an even number as required.
> 3. **Density**: $8/\binom{8}{2} = 8/28 \approx 0.29$. Mean degree $2 \times 8/8 = 2$.
> 4. **Distance from P2 to P7**: P2's neighbours are P1 and P3; from P1, P6 is reachable only through P4 or P5; P7 only through P6. So every path has length at least 4, and P2, P1, P4, P6, P7 achieves it: $d = 4$.
> 5. **Cycles**: the triangle P1, P2, P3 and the square P1, P4, P6, P5. The triangle is an odd cycle, so the network is not bipartite.
> 6. **Components**: $\{P1, \dots, P7\}$ and $\{P8\}$. Removing P1 would leave $\{P2, P3\}$, $\{P4, P5, P6, P7\}$ and $\{P8\}$: removing a hub can disconnect a network, which is why vertex importance measures exist ([[Network Centrality]]).

## Common misconceptions

> [!warning] "The picture is the graph"
> A graph is only $V$ and $E$; two graphs are the same (isomorphic) if a bijection of their vertices maps edges exactly onto edges ([[Function]]). The same graph has infinitely many drawings; a hub drawn in the center, short edges or visual clusters are choices of the layout algorithm, not results.

> [!warning] "Degree is the number of edge ends at a vertex, whatever the graph"
> In a multigraph a loop adds 2 to the degree of its vertex; in a directed graph in- and out-degree differ. State the kind of graph before computing degrees.

> [!warning] "A walk and a path are the same"
> Paths never revisit a vertex. Powers of the adjacency matrix count walks, which include back-and-forth moves, so they overcount paths.

## Exercises

> [!question] Exercise 1 (L1)
> Can a network of 7 proteins have every protein interacting with exactly 3 others? And a network of 8 proteins?

> [!success]- Solution
> 7 proteins: the degrees would sum to $7 \times 3 = 21$, odd, but the sum is $2|E|$, even. Impossible. 8 proteins: the sum is 24, so 12 edges; such graphs exist (for example the corners and edges of a cube). The handshake lemma rules out the first case without drawing anything.

> [!question] Exercise 2 (L2)
> Using that a tree on $n \ge 2$ vertices has $n - 1$ edges and no isolated vertex, prove that it has at least two leaves.

> [!success]- Solution
> The degrees sum to $2(n - 1) = 2n - 2$ and each is at least 1 (a connected graph with $n \ge 2$ vertices has no isolated vertex). If at most one vertex had degree 1, the others would have degree $\ge 2$ and the sum would be at least $1 + 2(n - 1) = 2n - 1 > 2n - 2$. Contradiction. In a phylogeny, the leaves are the sampled sequences.

> [!question] Exercise 3 (L2)
> A hypothetical interaction network has 20,000 proteins and 100,000 interactions. Compare the storage of an adjacency matrix and of adjacency lists, and compute the density.

> [!success]- Solution
> Matrix: $20{,}000^2 = 4 \times 10^8$ cells. Lists: each edge appears in the lists of its two endpoints, $2 \times 10^5$ entries, plus 20,000 list headers. Density: $10^5 / \binom{20{,}000}{2} = 10^5 / 199{,}990{,}000 \approx 5.0 \times 10^{-4}$. More than 99.9 % of the matrix would be zeros.

> [!question] Exercise 4 (L3, Python)
> Test bipartiteness by trying every 2-colouring of the vertices, on the toy network and on the invented metabolite-reaction graph M1, M2 → R1 → M3 → R2 → M4 (edges taken as undirected). Explain the results.

> [!success]- Solution
> ```python
> from itertools import product
>
> def is_bipartite_bruteforce(vertices, edges):
>     """Try all 2^n two-colourings (enumeration, small graphs only)."""
>     for colours in product((0, 1), repeat=len(vertices)):
>         side = dict(zip(vertices, colours))
>         if all(side[u] != side[v] for u, v in edges):
>             return True
>     return False
>
> MR = [("M1", "R1"), ("M2", "R1"), ("R1", "M3"), ("M3", "R2"), ("R2", "M4")]
> print(is_bipartite_bruteforce(VERTICES, EDGES),
>       is_bipartite_bruteforce(["M1", "M2", "M3", "M4", "R1", "R2"], MR))
> ```
> Output: `False True`. The toy network contains the triangle P1, P2, P3: whichever colours P1 and P2 get (they must differ), P3 must differ from both, impossible with two colours. The metabolite-reaction graph has metabolites on one side and reactions on the other. Enumeration costs $2^n$ colourings; a traversal decides bipartiteness in linear time ([[Graph Traversal]]).

> [!question] Exercise 5 (L3, Python)
> Prove that the swap $\{a, b\}, \{c, d\} \to \{a, d\}, \{c, b\}$ preserves every degree, then apply it to the edges P1-P3 and P6-P7 of the toy network. What changes?

> [!success]- Solution
> $a$ loses $b$ and gains $d$; $b$ loses $a$ and gains $c$; similarly for $c$ and $d$: each of the four vertices loses one incident edge and gains one. The swap must be refused if it creates a loop ($a = d$ or $c = b$) or an existing edge.
> ```python
> def swap(edges, i, j):
>     """Degree-preserving swap: (a,b),(c,d) -> (a,d),(c,b), refused if it creates a loop or duplicate."""
>     (a, b), (c, d) = edges[i], edges[j]
>     new = edges[:]
>     new[i], new[j] = (a, d), (c, b)
>     keys = [frozenset(e) for e in new]
>     if a == d or c == b or len(set(keys)) < len(keys):
>         return None
>     return new
>
> new = swap(EDGES, 1, 7)              # (P1,P3),(P6,P7) -> (P1,P7),(P6,P3)
> nadj = adjacency_list(VERTICES, new)
> print(new[1], new[7], {v: len(nadj[v]) for v in VERTICES} == deg, nadj["P3"] == adj["P3"])
> ```
> Output: `('P1', 'P7') ('P6', 'P3') True False`. Every degree is the same, but neighbourhoods changed (P3 now interacts with P6 instead of P1), and the triangle P1, P2, P3 is gone. Repeating many random swaps produces a null model with the observed degrees, against which the number of triangles in the real network can be compared.

## Mastery checklist

- [ ] 1 Recognized: I can define vertex, edge, degree, path, cycle, weighted and directed graph, and name four biological networks with what their edges mean.
- [ ] 2 Understood: I can prove the handshake lemma and its corollaries, and explain the difference between walks and paths and between a graph and its drawing.
- [ ] 3 Practiced: I can build adjacency lists and matrices from an edge list in Python, compute degrees, density and degree distributions, and check paths and cycles.
- [ ] 4 Applied: I loaded a real interaction or co-expression network, reported its size, density and degree distribution with its source and threshold, and used graph structure in [[04-alignment-engine]] or [[08-phylogenetic-engine]].
- [ ] 5 Explained: I can teach representations and their costs, bipartite graphs and trees, degree-preserving null models, and which biological problems become easy or hard graph problems.

## References

[^lehman]: [[Mathematics for Computer Science (Lehman)]], 2017 revision, graphs part: simple graphs and degrees, the handshake lemma, walks and paths, adjacency matrices and walk counting, bipartite graphs, connectivity, trees.
[^mcs]: [[MIT 6.042J - Mathematics for Computer Science]], graphs in the discrete structures third.
[^clrs]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 20 "Elementary Graph Algorithms" (adjacency-list and adjacency-matrix representations, directed and weighted graphs).
[^6006]: [[MIT 6.006 - Introduction to Algorithms]], graph search and shortest paths (Lecture 13: Dijkstra's Algorithm).
[^compeau-asm]: [[Bioinformatics Algorithms (Compeau)]], chapter "How Do We Assemble Genomes?" (overlap and de Bruijn graphs, Hamiltonian and Eulerian paths).
[^compeau-align]: [[Bioinformatics Algorithms (Compeau)]], chapter "How Do We Compare Biological Sequences?" (alignment as a path in a graph).
[^barabasi]: [[Barabási 2004 - Network Biology]], *Nature Reviews Genetics* 5:101-113.
[^stuart]: [[Stuart 2003 - A Gene-Coexpression Network]], *Science* 302:249.
