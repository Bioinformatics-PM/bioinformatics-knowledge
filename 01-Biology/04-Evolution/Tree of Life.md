---
aliases:
  - Universal Tree of Life
  - Three-Domain System
  - Three Domains of Life
  - Arbre du vivant
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Common Descent]]"
  - "[[Speciation]]"
  - "[[Prokaryote]]"
  - "[[Eukaryote]]"
related:
  - "[[Phylogenetic Tree]]"
  - "[[Horizontal Gene Transfer]]"
  - "[[16S Ribosomal RNA]]"
  - "[[Archaea]]"
projects:
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Woese 1977 - Phylogenetic Structure of the Prokaryotic Domain]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Microbiology (OpenStax)]]"
  - "[[Evolution (Futuyma)]]"
  - "[[Hug 2016 - A New View of the Tree of Life]]"
---

# Tree of Life

> [!abstract]
> The history of all living things can be drawn as one branching tree, rooted in a universal common ancestor and split into three domains (Bacteria, Archaea, Eukarya), except where genes jump between branches.

## Definition

The **tree of life** is the genealogy of all organisms drawn as a branching tree whose root is the universal common ancestor and whose tips are living lineages. Molecular phylogenies divide it into three **domains**: **Bacteria**, **Archaea** and **Eukarya**.[^os20][^woese] Horizontal gene transfer and endosymbiosis connect branches, so parts of this history form a network rather than a strict tree.[^os20]

## Why it matters

- **Marker genes.** Ribosomal RNA revealed the three domains,[^woese] and the small-subunit rRNA gene is still the standard marker for identifying prokaryotes and surveying communities ([[16S Ribosomal RNA]], [[Metagenomics]]).
- **Classifying sequences.** Assigning reads or genomes to taxa places them on this tree ([[Taxonomic Classification]], [[Microbial Taxonomy]]).
- **Conflicting gene trees.** In prokaryotes, different genes can have different histories, which matters for orthology inference and for annotating genomes ([[Horizontal Gene Transfer]], [[Ortholog]]).

## Core (L1)

**Reading a tree** ([[Phylogenetic Tree]]).[^os20]

- The **root** is the common ancestor of everything in the tree; **tips** are present-day lineages; each **branch point** (node) is a common ancestor where one lineage split into two.
- **Sister taxa** share an immediate common ancestor; a **clade** is an ancestor with all its descendants.
- Branches can be rotated around any node without changing the tree: order of the tips carries no information.
- Relatedness is measured by how recent the common ancestor is, not by which tips are drawn side by side. No living tip is more "evolved" than another: all have evolved for the same time since the root.

**Three domains.** In 1977 Woese and Fox compared ribosomal RNA across organisms and found three primary lines of descent, not two: the archaebacteria were as distinct from typical bacteria as from the lineage of the eukaryotic cytoplasm.[^woese] Bacteria and Archaea both lack a nucleus ([[Prokaryote]]), but at the molecular level archaea resemble eukaryotes in their machinery for replication, transcription and translation.[^alberts] "Prokaryote" therefore names a type of cell, not a branch of the tree ([[Archaea]], [[Bacteria]], [[Eukaryote]]).

![[three-domain-tree-of-life.svg]]

## Deeper (L2)

**Where is the root?** Comparing rRNA from the three domains gives their relationships, not the position of the root. The usual picture roots the tree between Bacteria and an Archaea-plus-Eukarya branch, consistent with the shared information machinery of archaea and eukaryotes;[^alberts] where the root lies and how eukaryotes arose relative to archaea remain research questions.[^futuyma]

**Endosymbiosis merges branches.** Mitochondria descend from bacteria taken up by an ancestral eukaryotic cell, and plastids (chloroplasts) from photosynthetic bacteria taken up later.[^alberts] A eukaryotic cell thus contains lineages from two domains ([[Mitochondrion]]).

**Horizontal gene transfer crosses branches.** Prokaryotes acquire genes from other cells by transformation, transduction and conjugation, including across species boundaries.[^micro11] Each transferred gene has its own history, so trees built from different genes can disagree. Models of the history of life that allow such exchanges draw it as a web or a ring rather than a tree.[^os20]

## Advanced (L3)

**Genome-scale trees.** Modern trees of life concatenate many genes present in all domains. Hug and colleagues built one from 16 ribosomal proteins in 3,083 genomes, 1,011 of them newly reconstructed from environmental DNA by metagenomics; most of the branching diversity was bacterial and much of it came from organisms never grown in culture, notably the candidate phyla radiation.[^hug] Ribosomal genes are used because every cell has them, the same choice Woese made with rRNA.[^woese][^hug]

**Tree or network?** A tree is the right model for vertical descent; transfers and endosymbioses add edges that make the genealogy a directed acyclic graph ([[Phylogenetic Network]]). In practice a "tree of life" is the dominant vertical signal of widely shared genes, with known reticulations laid over it; which genes carry that signal best is part of [[Phylogenomics]].

## Mathematical representation

A **rooted tree** on a leaf set $X$ is a connected acyclic graph with one root, in which every non-root node has exactly one parent; it is **binary** if every internal node has two children. With $n$ leaves, a rooted binary tree has $n - 1$ internal nodes and $2n - 2$ edges.

**Counting trees.** A new leaf can be attached to the middle of any of the $2m - 2$ edges of a rooted binary tree with $m$ leaves, or above its root: $2m - 1$ choices. Starting from the single tree on 2 leaves,

$$T(n) = \prod_{m=2}^{n-1} (2m - 1) = 1 \cdot 3 \cdot 5 \cdots (2n - 3) = (2n - 3)!!$$

rooted binary trees on $n$ labelled leaves.

## Computational representation

Trees are stored as nested structures or parent pointers and exchanged as [[Newick Format]] strings: `(A,(B,C));` reads "A is sister to the clade of B and C".

```python
# 1. The three-domain tree as nested tuples, written in Newick format
TREE = ("Bacteria", ("Archaea", "Eukarya"))

def newick(node) -> str:
    return node if isinstance(node, str) else "(" + ",".join(newick(c) for c in node) + ")"

print(newick(TREE) + ";")

# 2. How many rooted binary trees for n labelled leaves? (2n - 3)!! = 1 * 3 * 5 * ... * (2n - 3)
def n_rooted_trees(n: int) -> int:
    count = 1
    for k in range(1, 2 * n - 2, 2):
        count *= k
    return count

for n in (3, 4, 10, 20):
    print(n, n_rooted_trees(n))

# 3. Endosymbiosis turns the genealogy into a network: one node has two parents (toy)
PARENTS = {
    "bacterial stem": ["root"], "archaeal-eukaryotic stem": ["root"],
    "Bacteria": ["bacterial stem"], "mitochondrial ancestor": ["bacterial stem"],
    "Archaea": ["archaeal-eukaryotic stem"],
    "Eukarya": ["archaeal-eukaryotic stem", "mitochondrial ancestor"],
}

def all_ancestors(node: str) -> set[str]:
    found, stack = set(), [node]
    while stack:
        for parent in PARENTS.get(stack.pop(), []):
            if parent not in found:
                found.add(parent)
                stack.append(parent)
    return found

print(sorted(all_ancestors("Eukarya")))
print(sorted(all_ancestors("Archaea")))
```

Output:

```text
(Bacteria,(Archaea,Eukarya));
3 3
4 15
10 34459425
20 8200794532637891559375
['archaeal-eukaryotic stem', 'bacterial stem', 'mitochondrial ancestor', 'root']
['archaeal-eukaryotic stem', 'root']
```

With 20 taxa there are already about $8 \times 10^{21}$ rooted trees. In the network, Eukarya has ancestors in both stems, while Archaea has a single line of ancestors.

## Worked example

> [!example] Who is closer to whom?
> Tree `(Bacteria,(Archaea,Eukarya));`, as in the figure.
>
> 1. **Common ancestors.** Archaea and Eukarya meet at the archaeal-eukaryotic stem; Archaea and Bacteria meet only at the root.
> 2. **Recency.** The archaeal-eukaryotic ancestor is younger than the root, so Archaea are more closely related to Eukarya than to Bacteria, although Archaea and Bacteria share the prokaryotic cell plan.
> 3. **Groups.** {Archaea, Eukarya} is a clade; {Bacteria, Archaea} ("prokaryotes") is not, because it leaves out a descendant (Eukarya) of their common ancestor, the root.

## Common misconceptions

> [!warning] "Archaea are a kind of bacteria"
> They form a separate primary line of descent,[^woese] and share their information machinery with eukaryotes.[^alberts] The old name "archaebacteria" is misleading.

> [!warning] "Horizontal transfer means there is no tree"
> Transfers make some gene histories conflict, but trees built from widely shared genes such as ribosomal proteins still recover the major groups,[^hug] and models of the history of life combine a tree-like backbone with reticulations.[^os20]

## Exercises

> [!question] Exercise 1 (L1)
> For the tree `((A,B),(C,(D,E)));`: name the sister of D; say whether C is closer to D or to A; and say whether swapping A and B changes the tree.

> [!success]- Solution
> D's sister is E. C shares a more recent ancestor with (D, E) than with A, so C is closer to D. Swapping A and B is a rotation around their node: same tree.

> [!question] Exercise 2 (L2, Python)
> With `n_rooted_trees`, compute the number of rooted binary trees for 5, 10, 20 and 50 taxa. What does it imply for building a tree of 50 species?

> [!success]- Solution
> ```python
> for n in (5, 10, 20, 50):
>     print(n, f"{n_rooted_trees(n):.3e}")
> # 5 1.050e+02
> # 10 3.446e+07
> # 20 8.201e+21
> # 50 2.753e+76
> ```
>
> With 50 taxa there are about $2.8 \times 10^{76}$ trees, so scoring them all is impossible: practical methods search tree space heuristically ([[Phylogenetic Tree Search]]).

> [!question] Exercise 3 (L2)
> In a gene tree, the sequence from one archaeal genome falls inside a group of bacterial sequences, while its ribosomal genes place the organism among archaea. Give the most likely explanation and two checks.

> [!success]- Solution
> Horizontal transfer of that gene from a bacterium to the archaeal lineage.[^micro11] Checks: the gene's composition or codon usage may differ from the rest of the genome; neighbouring genes may share the bacterial affinity (a transferred block); and the gene should be absent from close archaeal relatives. Also rule out contamination or misassembly by confirming that the gene sits on a contig carrying archaeal genes.

> [!question] Exercise 4 (L3)
> Using `PARENTS` and `all_ancestors`, explain why "the ancestor of eukaryotes" is ambiguous in a network, and add a hypothetical plastid edge to make a plant lineage descend also from a "cyanobacterial ancestor".

> [!success]- Solution
> In a tree each node has one line of ancestors; in a network a node with two parents has ancestors along two paths, here the archaeal-eukaryotic stem and the mitochondrial ancestor. Which ancestor matters depends on the gene: nuclear information-processing genes point one way, mitochondrial genes the other.
>
> ```python
> PARENTS["cyanobacterial ancestor"] = ["bacterial stem"]
> PARENTS["plants"] = ["Eukarya", "cyanobacterial ancestor"]
> print(sorted(all_ancestors("plants")))
> # ['Eukarya', 'archaeal-eukaryotic stem', 'bacterial stem', 'cyanobacterial ancestor', 'mitochondrial ancestor', 'root']
> ```

## Mastery checklist

- [ ] 1 Recognized: I can name the three domains and the parts of a tree (root, node, tip, clade, sister taxa).
- [ ] 2 Understood: I can read relatedness from nodes, explain why archaea are a separate domain, and how endosymbiosis and transfer blur the tree.
- [ ] 3 Practiced: I can write and read Newick strings, count trees, and compute ancestors in a network in Python.
- [ ] 4 Applied: in [[08-phylogenetic-engine]], I root, draw and interpret trees, and flag genes whose history conflicts with the species tree.
- [ ] 5 Explained: I can teach how rRNA and ribosomal proteins built the tree of life, what metagenomics changed, and why the root is uncertain.

## References

[^os20]: [[Biology 2e (OpenStax)]], ch. 20 "Phylogenies and the History of Life" (reading phylogenetic trees; domains; horizontal gene transfer and web and ring models of the history of life).
[^woese]: [[Woese 1977 - Phylogenetic Structure of the Prokaryotic Domain]], *PNAS* 74:5088-5090.
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), ch. 1 "Cells and Genomes" (archaea compared with bacteria and eukaryotes) and ch. 14 "Energy Conversion: Mitochondria and Chloroplasts" (endosymbiotic origin of mitochondria and plastids).
[^micro11]: [[Microbiology (OpenStax)]], ch. 11 "Mechanisms of Microbial Genetics" (horizontal gene transfer: transformation, transduction, conjugation).
[^futuyma]: [[Evolution (Futuyma)]], 5th ed. (2023), the history of life and the tree of life (chapter numbers not verified).
[^hug]: [[Hug 2016 - A New View of the Tree of Life]], *Nature Microbiology* 1:16048.
