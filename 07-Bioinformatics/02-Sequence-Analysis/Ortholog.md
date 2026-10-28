---
aliases:
  - Orthologue
  - Orthologous Gene
  - Orthology
  - Gène orthologue
tags:
  - type/concept
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Sequence Homology]]"
  - "[[Speciation]]"
  - "[[Gene Duplication]]"
  - "[[Phylogenetic Tree]]"
related:
  - "[[Paralog]]"
  - "[[Orthology Inference]]"
  - "[[Gene Tree Reconciliation]]"
  - "[[Comparative Genomics]]"
  - "[[Functional Annotation]]"
  - "[[Gene Ontology Annotation]]"
  - "[[Phylogenomics]]"
  - "[[Synteny]]"
  - "[[Horizontal Gene Transfer]]"
  - "[[BLAST]]"
projects: []
sources:
  - "[[Fitch 1970 - Distinguishing Homologous from Analogous Proteins]]"
  - "[[Koonin 2005 - Orthologs, Paralogs, and Evolutionary Genomics]]"
  - "[[Altenhoff 2012 - Resolving the Ortholog Conjecture]]"
---

# Ortholog

> [!abstract]
> Orthologs are homologous genes in different species that descend from a single gene of their last common ancestor: they were separated by a speciation, so each copy usually keeps doing the job its ancestor did.

## Definition

Fitch (1970) divided homology according to the event that separated two genes: when the homology results from **speciation**, the genes are **orthologous**; when it results from **gene duplication**, they are **paralogous** ([[Paralog]]).[^fitch] His examples: the α-hemoglobins of human and mouse are orthologs, α- and β-hemoglobin are paralogs.[^fitch] In a gene tree, two genes are orthologs when the node of their last common ancestor is a speciation, and orthologs evolve by vertical descent from a single ancestral gene.[^koonin] Like homology itself ([[Sequence Homology]]), orthology is a statement about history: it is defined neither by similarity nor by function.

## Why it matters

- **Function transfer.** Most genes of a new genome are annotated by transfer from characterized homologs, and a clear distinction between orthologs and paralogs is critical for reliable functional annotation of new genomes and for an evolutionary classification of genes.[^koonin] Orthologs are the preferred donors ([[Functional Annotation]], [[Gene Ontology Annotation]]).
- **Reach.** Genome comparisons establish orthologs in taxonomically distant species for the majority of the genes of each sequenced genome,[^koonin] which is what makes experiments in yeast, flies or mice informative about human genes.
- **Species trees.** If every split of a gene tree is a speciation, the gene tree has, in the simplest case, the shape of the species tree. Species phylogenies are therefore built from orthologous genes ([[Phylogenomics]]); a paralog slipped into the data dates a duplication, not a speciation. The sequences given to [[08-phylogenetic-engine]] must be orthologs.
- **Comparative genomics.** Gene gain and loss, conserved gene order ([[Synteny]]) and rates of change ([[Molecular Evolution]]) are measured on sets of orthologs ([[Comparative Genomics]]).

## Core (L2)

### The test: which event is at the last common ancestor?

![[ortholog-paralog-gene-tree.svg]]

The figure embeds Fitch's globin example in the species tree. A duplication (D) in an ancestor of human and mouse produced the α and β genes; the later speciation (S) that separated the human and mouse lineages split each of them. For any pair of genes, follow both lineages back to the node where they meet:

| Pair | Last common ancestor | Relation |
|---|---|---|
| α human, α mouse | S | orthologs |
| β human, β mouse | S | orthologs |
| α human, β human | D | paralogs |
| α human, β mouse | D | paralogs, although in different species |

The last row is the trap: being in two different species is necessary for orthology, not sufficient.

### One-to-one, one-to-many, many-to-many

When a gene duplicates in one lineage after a speciation, a single gene of the other species gains several orthologs. These **co-orthologs** are all orthologous to that gene and paralogous to each other.[^koonin] Orthology is therefore a relation between groups of genes: one-to-one (1:1), one-to-many (1:n) or many-to-many (n:m), depending on the duplications in each lineage since the speciation. In the toy tree of the Computational representation, an invented mouse-specific duplication makes human β one-to-two orthologous to mouse β1 and β2.

### Why orthologs tend to keep their function

At a speciation, each daughter species inherits one copy of the gene, which keeps the role it had in the ancestor. No redundant copy covers for it, so [[Purifying Selection|purifying selection]] keeps removing changes that damage the function. After a duplication, by contrast, one copy can change while the other keeps the ancestral role ([[Paralog]], [[Gene Duplication]]). This expectation is the **ortholog conjecture**, or standard model of phylogenomics: protein function changes rapidly after duplication, leading to paralogs with different functions, while orthologs retain the ancestral function.[^altenhoff] It is a tendency, not a law: orthologs in distant species also accumulate changes, so a transferred annotation remains a hypothesis.

### Finding orthologs in practice (preview)

The definition needs the gene tree, which nobody hands you. The main approaches, detailed in [[Orthology Inference]], approximate it:[^koonin]

- **Similarity-based**: genes $a$ (species A) and $b$ (species B) are candidate orthologs when each is the other's best hit in a similarity search ([[BLAST]]), the **reciprocal best hit** criterion. Fast and genome-wide, but it returns at most one partner per gene (Exercise 5).
- **Tree-based**: build the gene tree, label each internal node as a speciation or a duplication, then read the relation of every pair ([[Gene Tree Reconciliation]]).

## Advanced (L3)

- **Orthology is not transitive.** In the toy tree, mouse β1 and human β are orthologs, human β and mouse β2 are orthologs, but mouse β1 and β2 are paralogs (Exercise 4). Genome-scale analyses therefore group genes into **orthogroups**, the genes descended from one gene of the last common ancestor of the species considered, instead of chaining pairs ([[Orthology Inference]]).
- **Differential loss creates false orthologs.** If, after a duplication, species P keeps one copy and species Q only the other, each survivor is the other's only homolog in the two genomes and looks one-to-one orthologous, although the pair is paralogous: **pseudo-orthologs**.[^koonin] Any method that sees only these two genomes is fooled; a third genome that kept both copies exposes them (Worked example), and so can conserved gene order ([[Synteny]]).
- **Horizontal transfer.** A gene acquired from another species by [[Horizontal Gene Transfer]] (a **xenolog**) follows a history that departs from the species tree, which breaks the comparison of gene and species trees.[^koonin]
- **Orthology depends on the species compared.** A mouse-specific duplication makes human-mouse orthology one-to-two but leaves human-chicken orthology one-to-one: relation types are always stated for a pair of lineages (Exercise 3).

## Frontier (M1)

**Is the ortholog conjecture true?** Altenhoff and colleagues tested it on experimentally supported Gene Ontology annotations of homologs from 13 genomes.[^altenhoff] A naive comparison is biased in several ways they controlled: authorship bias (genes characterized in the same study share annotation habits), variation of GO term frequency among species, variation of background similarity among species pairs, and propagated annotations that are not independent evidence.[^altenhoff] After these controls, orthologs generally have more similar functional annotations than paralogs, a weak but significant effect, especially strong for subcellular localization.[^altenhoff] The conjecture survives as a statistical tendency, which is how annotation pipelines should use it: an annotation transferred from an ortholog is a prior to weigh against domain architecture, expression data and experiments ([[Functional Annotation]], [[Gene Ontology Annotation]]).

## Mathematical representation

Let $G$ be a rooted binary gene tree with leaf set $L$ (genes), $\sigma : L \to S$ the map from genes to species, and $\tau$ the labelling of internal nodes by an event, speciation or duplication. For distinct genes $x, y$ with last common ancestor $\mathrm{lca}(x, y)$:

$$x, y \text{ orthologs} \iff \tau(\mathrm{lca}(x, y)) = \text{speciation}, \qquad x, y \text{ paralogs} \iff \tau(\mathrm{lca}(x, y)) = \text{duplication}.$$

- **Species-overlap rule.** For a node $v$ with children $v_1, v_2$ and leaf sets $L(v_1), L(v_2)$: if $\sigma(L(v_1)) \cap \sigma(L(v_2)) \neq \emptyset$, some species has copies on both sides, so $v$ must be a duplication. The rule is sufficient, not necessary: a duplication followed by complementary losses leaves no overlap and is mislabelled as a speciation (pseudo-orthologs).
- **Relation type.** For orthologs $x \in L(v_1)$ and $y \in L(v_2)$ with $v = \mathrm{lca}(x, y)$, let $n_x = |\{g \in L(v_1) : \sigma(g) = \sigma(x)\}|$ and $n_y = |\{g \in L(v_2) : \sigma(g) = \sigma(y)\}|$; the relation is $n_x : n_y$.
- **Non-transitivity.** The orthology relation $O$ is symmetric but not transitive: $(x, y) \in O$ and $(y, z) \in O$ do not imply $(x, z) \in O$ when $\mathrm{lca}(x, z)$ is a duplication below $\mathrm{lca}(x, y) = \mathrm{lca}(y, z)$.

## Computational representation

A gene tree as nested tuples, with leaves named `species:gene`. The code labels each node with the species-overlap rule and classifies every pair of genes once, at the node where they meet.

```python
# Toy gene tree after Fitch's globin example; the mouse beta duplication is invented.
TREE = (("human:alpha", "mouse:alpha"), ("human:beta", ("mouse:beta1", "mouse:beta2")))


def leaves(node) -> list[str]:
    return [node] if isinstance(node, str) else [g for child in node for g in leaves(child)]


def species(gene: str) -> str:
    return gene.split(":")[0]


def event(node) -> str:
    """Species-overlap rule: if both sides of a split contain the same species, it was a duplication."""
    left, right = ({species(g) for g in leaves(child)} for child in node)
    return "duplication" if left & right else "speciation"


def relations(node):
    """Yield (x, y, relation, type) for every pair of genes, judged at their last common ancestor."""
    if isinstance(node, str):
        return
    for child in node:
        yield from relations(child)
    left, right = (leaves(child) for child in node)
    for x in left:
        for y in right:
            if event(node) == "duplication":
                yield x, y, "paralogs", ""
            else:   # co-orthologs: copies of each species on each side of the speciation
                n_x = sum(species(g) == species(x) for g in left)
                n_y = sum(species(g) == species(y) for g in right)
                yield x, y, "orthologs", f"{n_x}:{n_y}"


for x, y, rel, kind in relations(TREE):
    print(f"{x:12s} {y:12s} {rel:9s} {kind}")
```

```text
human:alpha  mouse:alpha  orthologs 1:1
mouse:beta1  mouse:beta2  paralogs
human:beta   mouse:beta1  orthologs 1:2
human:beta   mouse:beta2  orthologs 1:2
human:alpha  human:beta   paralogs
human:alpha  mouse:beta1  paralogs
human:alpha  mouse:beta2  paralogs
mouse:alpha  human:beta   paralogs
mouse:alpha  mouse:beta1  paralogs
mouse:alpha  mouse:beta2  paralogs
```

Ten pairs for five genes, $\binom{5}{2}$, each decided at a single node. Real tools add a species tree, branch lengths and support values, but the decision rule is the same ([[Gene Tree Reconciliation]]).

## Worked example

> [!example] Differential loss hides a duplication (invented genes)
> 1. An ancestral gene duplicates into X1 and X2, then species P and Q separate. P keeps only X1, Q keeps only X2.
> 2. With only P and Q, the gene tree is the single split (P:X1, Q:X2). No species appears on both sides, so the species-overlap rule calls it a speciation, and a reciprocal best hit search pairs the two genes as well, since each is the other's only homolog.
> 3. Add species R, which kept both copies: the tree becomes ((P:X1, R:X1), (Q:X2, R:X2)). R appears on both sides of the root, which is now labelled a duplication, and P:X1 and Q:X2 are reported as paralogs.
> ```python
> print(event(("P:X1", "Q:X2")))                              # P lost X2, Q lost X1
> print(event((("P:X1", "R:X1"), ("Q:X2", "R:X2"))))          # R kept both copies
> for x, y, rel, kind in relations((("P:X1", "R:X1"), ("Q:X2", "R:X2"))):
>     if {species(x), species(y)} == {"P", "Q"}:
>         print(x, y, rel)
> ```
> ```text
> speciation
> duplication
> P:X1 Q:X2 paralogs
> ```
> 4. Lesson: an orthology call depends on the genomes compared; a pair that looks one-to-one can be a pair of pseudo-orthologs.[^koonin]

## Common misconceptions

> [!warning] "Orthologs are genes with the same function in different species"
> Orthology is defined by the event that separated the genes, a speciation, not by their function.[^fitch] Keeping the function is a frequent consequence, to be tested; a function-based definition would make the ortholog conjecture true by definition.

> [!warning] "Genes in different species are orthologs, genes in the same species are paralogs"
> Human α-globin and mouse β-globin live in different species and are paralogs, separated by the α/β duplication.[^fitch] Two genes of one species can only be paralogs, but two genes of different species can be either.

> [!warning] "The best BLAST hit in the other genome is the ortholog"
> The best hit can be a paralog when the true ortholog was lost (Worked example), and a single best hit misses co-orthologs (Exercise 5). Similarity is evidence of homology, not of the kind of homology.

> [!warning] "Orthology is one-to-one"
> Lineage-specific duplications produce one-to-many and many-to-many relations, and all the co-orthologs are orthologs of the gene in the other species.[^koonin]

## Exercises

> [!question] Exercise 1 (L2)
> Using the figure, classify (a) β human and β mouse, (b) α mouse and β mouse, (c) β human and α mouse, naming the event at each last common ancestor.

> [!success]- Solution
> (a) S: orthologs. (b) D: paralogs (same species, so orthology was impossible anyway). (c) D: paralogs, although in different species, because their lineages split at the α/β duplication.[^fitch]

> [!question] Exercise 2 (L2)
> A human gene has two orthologs in zebrafish. Give the simplest history that explains it and the relation between the two zebrafish genes.

> [!success]- Solution
> A duplication in the fish lineage after the human-fish speciation. The two zebrafish genes are co-orthologs of the human gene (a 1:2 relation) and paralogs of each other.[^koonin]

> [!question] Exercise 3 (L2, Python)
> Run `relations` on `((("human:x1", "human:x2"), "mouse:x"), "chicken:x")`. Which relations are one-to-one, and why are the others 2:1?

> [!success]- Solution
> ```python
> for x, y, rel, kind in relations(((("human:x1", "human:x2"), "mouse:x"), "chicken:x")):
>     print(f"{x:10s} {y:10s} {rel:9s} {kind}")
> ```
> ```text
> human:x1   human:x2   paralogs
> human:x1   mouse:x    orthologs 2:1
> human:x2   mouse:x    orthologs 2:1
> human:x1   chicken:x  orthologs 2:1
> human:x2   chicken:x  orthologs 2:1
> mouse:x    chicken:x  orthologs 1:1
> ```
> Only mouse-chicken is one-to-one. The duplication happened in the human lineage after the human-mouse split, so both human copies are orthologs of the single mouse gene and of the single chicken gene.

> [!question] Exercise 4 (L3)
> Show with the toy tree of the Computational representation that orthology is not transitive. Which node makes it fail?

> [!success]- Solution
> Mouse β1 and human β are orthologs (they meet at the β speciation), human β and mouse β2 too, but mouse β1 and β2 meet at the invented mouse duplication, so they are paralogs. Transitivity fails because $\mathrm{lca}(\beta_1, \beta_2)$ is a duplication below the speciation $\mathrm{lca}(\beta_1, \beta_{\text{human}})$. This is why genome-scale methods build orthogroups instead of chaining pairs.

> [!question] Exercise 5 (L3, Python)
> Invented similarity scores between the human and mouse genes of the toy tree:
> ```python
> score = {("human:beta", "mouse:beta1"): 410, ("human:beta", "mouse:beta2"): 395,
>          ("human:beta", "mouse:alpha"): 120, ("human:alpha", "mouse:alpha"): 380,
>          ("human:alpha", "mouse:beta1"): 115, ("human:alpha", "mouse:beta2"): 112}
> ```
> Compute the reciprocal best hits. Which true orthology relation is missed, and why?

> [!success]- Solution
> ```python
> human = {h for h, _ in score}
> mouse = {m for _, m in score}
> best_m = {h: max(mouse, key=lambda m: score[h, m]) for h in human}
> best_h = {m: max(human, key=lambda h: score[h, m]) for m in mouse}
> print(sorted((h, m) for h, m in best_m.items() if best_h[m] == h))
> ```
> Output: `[('human:alpha', 'mouse:alpha'), ('human:beta', 'mouse:beta1')]`. Human β and mouse β2 are orthologs (1:2), but human β's best mouse hit is β1, so the pair is not reciprocal. Reciprocal best hits give at most one partner per gene and can only find one-to-one relations; co-orthologs need tree-based or clustering methods ([[Orthology Inference]]).

> [!question] Exercise 6 (M1)
> You want to test whether orthologs are more similar in function than paralogs using GO annotations. List four biases that distort a naive comparison and, for one of them, explain in which direction it pushes the result.

> [!success]- Solution
> Altenhoff and colleagues controlled authorship bias, variation of GO term frequency among species, variation of background similarity among species pairs, and propagated annotation bias.[^altenhoff] Direction of the first one: paralogs live in the same species, so they are more often characterized in the same study, with the same assays and vocabulary, than orthologs in two species studied by different groups. Shared authorship makes paralog annotations look more alike than the underlying functions are, which biases a naive test against the ortholog conjecture.

## Mastery checklist

- [ ] 1 Recognized: I can define orthologs by speciation and give Fitch's globin example.
- [ ] 2 Understood: I can classify any pair of genes in a gene tree, explain co-orthologs and why orthologs tend to keep their function.
- [ ] 3 Practiced: I can label a gene tree with the species-overlap rule in code and derive 1:1, 1:n and n:m relations.
- [ ] 4 Applied: I selected one-to-one orthologs of a real gene family across several genomes and built a species tree from them in [[08-phylogenetic-engine]].
- [ ] 5 Explained: I can explain pseudo-orthologs, xenologs, non-transitivity, and the evidence for and the limits of the ortholog conjecture.

## References

[^fitch]: [[Fitch 1970 - Distinguishing Homologous from Analogous Proteins]], *Systematic Zoology* 19(2):99-113.
[^koonin]: [[Koonin 2005 - Orthologs, Paralogs, and Evolutionary Genomics]], *Annual Review of Genetics* 39:309-338.
[^altenhoff]: [[Altenhoff 2012 - Resolving the Ortholog Conjecture]], *PLoS Computational Biology* 8(5):e1002514.
