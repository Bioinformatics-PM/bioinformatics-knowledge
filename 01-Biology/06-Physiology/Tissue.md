---
aliases:
  - Tissues
  - Tissu
  - Animal Tissue
  - Histology
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Cell]]"
  - "[[Eukaryote]]"
  - "[[Gene Expression]]"
related:
  - "[[Organ System]]"
  - "[[Cell Type]]"
  - "[[Cell Differentiation]]"
  - "[[Blood]]"
  - "[[Neuron]]"
  - "[[Cell-Type Deconvolution]]"
  - "[[Expression Quantitative Trait Locus]]"
projects: []
sources:
  - "[[Anatomy and Physiology 2e (OpenStax)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[GTEx Portal]]"
---

# Tissue

> [!abstract]
> A tissue is a group of similar cells working together with the material around them; four tissue types (epithelial, connective, muscle, nervous) combine to build every organ of the body.

## Definition

A **tissue** is a group of cells of similar structure and function, together with the extracellular material they produce, that performs a common function. Animal tissues fall into four types: **epithelial**, **connective**, **muscle** and **nervous**. An **organ** is a structure built from two or more tissue types.[^ap][^bio7]

## Why it matters

- **Tissue is the first metadata column.** Expression atlases are organized by tissue: the [[GTEx Portal]] V8 release holds 17,382 RNA-seq samples from 54 tissues (including 2 cell lines) of 948 post-mortem donors.[^gtex] "Is this gene tissue-specific?" is one of the first questions asked of a new gene ([[Gene Expression]]).
- **Genetic effects are tissue-dependent.** GTEx maps variants that change expression ([[Expression Quantitative Trait Locus|eQTLs]]) tissue by tissue, which links disease variants to the tissue where they act.[^gtex]
- **A bulk tissue sample is a mixture of cell types.** The GTEx atlas found cell type composition to be a key factor in interpreting tissue expression;[^gtex] separating composition from regulation is the job of [[Cell-Type Deconvolution]] and [[Single-Cell RNA Sequencing]] ([[Cell Type]]).

## Core (L1)

All cells of a body carry the same genome; tissues differ because their cells express different sets of genes ([[Cell Differentiation]]).[^alberts]

| Tissue type | Organization | Main functions | Examples |
|---|---|---|---|
| Epithelial | Sheets of tightly joined cells on a basement membrane, little extracellular material | Covers surfaces, lines cavities and tubes, forms glands; protection, absorption, secretion | Epidermis, lining of the gut, kidney tubules |
| Connective | Cells scattered in an abundant extracellular matrix (protein fibers and ground substance) | Support, binding, protection, transport | Tendon, fat, cartilage, bone, [[Blood]] |
| Muscle | Elongated cells packed with contractile proteins | Movement and force | Skeletal, cardiac and smooth muscle |
| Nervous | [[Neuron\|Neurons]] and supporting glial cells | Fast signaling and integration | Brain, spinal cord, nerves |

Sources for the table: [^ap][^bio7].

- **Epithelia** are named by cell shape (squamous: flat; cuboidal; columnar: tall) and number of layers (simple: one; stratified: several; pseudostratified: one layer that looks like several).[^ap]
- **Connective tissue** ranges from loose and dense connective tissue proper to supportive tissues (cartilage, bone) and fluid tissues: blood is a fluid connective tissue whose matrix is plasma.[^ap][^ap18]
- **Muscle**: skeletal (striated, voluntary), cardiac (striated, involuntary, heart only), smooth (not striated, involuntary, walls of hollow organs and vessels).[^ap]

**From tissues to organs.** An organ combines tissues. The stomach wall has an epithelial lining that secretes, connective tissue carrying vessels, layers of smooth muscle that mix the contents, and nerves that coordinate them; the skin pairs an epithelium (epidermis) with connective tissue (dermis).[^ap] Organs then group into [[Organ System|organ systems]].

```mermaid
flowchart LR
    C["Cells<br/>(one genome, different expression)"] --> T["Tissues<br/>epithelial, connective, muscle, nervous"]
    T --> O["Organs<br/>two or more tissue types"]
    O --> S["Organ systems"]
```

## Deeper (L2)

- **Embryonic origin.** The tissues derive from three embryonic germ layers (ectoderm, mesoderm, endoderm); for instance nervous tissue comes from ectoderm and muscle and most connective tissue from mesoderm.[^ap]
- **Extracellular matrix.** Connective tissue properties come mostly from its matrix: collagen fibers give tensile strength, mineral makes bone rigid, plasma makes blood fluid.[^ap][^alberts]
- **Tissue versus cell type.** A tissue is an anatomical unit; a [[Cell Type]] is a class of cells. One tissue contains several cell types (the stomach lining alone has several secretory cell types), and one cell type, such as a macrophage, is found in many tissues.[^ap]
- **Renewal.** Tissues differ in turnover: epithelia that face wear are renewed constantly from stem cells, whereas most neurons are not replaced ([[Stem Cell]]).[^ap]

## Advanced (L3)

- **Tissue specificity in data.** In an atlas, a gene expressed in one tissue only is tissue-specific; a gene expressed similarly everywhere is broadly expressed (often housekeeping). Specificity scores summarize this per gene (see Mathematical representation).
- **Composition confounds.** If a disease changes the proportion of cell types in a tissue, bulk expression changes even when no cell changes its expression (Exercise 3). Interpreting tissue differences therefore needs composition estimates or single-cell data.[^gtex]

## Mathematical representation

Let $\mu_{gc}$ be the mean expression of gene $g$ in cell type $c$ and $\pi_c$ the fraction of mRNA contributed by cell type $c$ in a tissue sample ($\pi_c \ge 0$, $\sum_c \pi_c = 1$). A simple mixture model of bulk tissue expression is

$$x_g = \sum_c \pi_c\, \mu_{gc}.$$

For tissue specificity, with $x_{gt} \ge 0$ the expression of gene $g$ in tissue $t$, one simple score (used here for illustration) is the share of the top tissue,

$$s_g = \frac{\max_t x_{gt}}{\sum_t x_{gt}} \in \Big[\tfrac{1}{T}, 1\Big],$$

where $T$ is the number of tissues: $s_g = 1/T$ for perfectly uniform expression, $s_g = 1$ for a single-tissue gene.

## Computational representation

An atlas is a gene × sample matrix plus a sample table giving each sample's tissue. Averaging per tissue gives a gene × tissue matrix:

```python
# Invented TPM values (not real data): genes x tissues
TISSUES = ["liver", "brain", "muscle", "blood"]
TPM = {
    "G1": [950.0, 2.0, 5.0, 3.0],
    "G2": [40.0, 45.0, 38.0, 42.0],
    "G3": [1.0, 120.0, 0.5, 0.2],
    "G4": [10.0, 12.0, 300.0, 280.0],
}


def top_share(values: list[float]) -> tuple[int, float]:
    """Index of the highest tissue and its share of the gene's summed expression."""
    top = max(range(len(values)), key=values.__getitem__)
    return top, values[top] / sum(values)


for gene, values in TPM.items():
    top, share = top_share(values)
    label = "specific" if share >= 0.8 else "broad" if share <= 0.4 else "intermediate"
    print(gene, TISSUES[top], round(share, 2), label)
```

```text
G1 liver 0.99 specific
G2 brain 0.27 broad
G3 brain 0.99 specific
G4 muscle 0.5 intermediate
```

The thresholds are arbitrary choices. G4 shows the score's blind spot: a gene shared by two tissues looks "intermediate".

## Worked example

> [!example] Which tissues build the small intestine wall?
> 1. **Lining**: a simple columnar epithelium absorbs nutrients and secretes mucus (epithelial).[^ap]
> 2. **Beneath it**: connective tissue carries blood and lymph vessels that take up absorbed nutrients (connective; blood is itself connective tissue).
> 3. **Around it**: layers of smooth muscle move the contents along (muscle).
> 4. **Throughout**: nerve networks coordinate secretion and movement (nervous).
>
> All four tissue types cooperate in one organ, so a bulk RNA-seq sample of intestine mixes epithelial, immune, muscle and nerve cell signals.

## Common misconceptions

> [!warning] "Blood is not a tissue"
> Blood is a connective tissue: cells suspended in a fluid extracellular matrix, the plasma.

> [!warning] "A tissue difference in expression means cells regulate the gene differently"
> It can be a difference in composition: more of the cell type that expresses the gene.

## Exercises

> [!question] Exercise 1 (L1)
> Assign each to a tissue type: (a) bone; (b) the lining of the trachea; (c) the heart wall's contractile cells; (d) glial cells; (e) adipose tissue.

> [!success]- Solution
> (a) connective (supportive); (b) epithelial; (c) muscle (cardiac); (d) nervous; (e) connective.

> [!question] Exercise 2 (L2)
> Name an organ that contains all four tissue types and give the role of each.

> [!success]- Solution
> The stomach: epithelium secretes and protects, connective tissue carries vessels, smooth muscle mixes the contents, nerves coordinate. The skin also qualifies (epidermis, dermis, small muscles of hair follicles, sensory nerves).

> [!question] Exercise 3 (L3, Python)
> A marker gene is expressed at 200 (invented units) in cell type A and 10 in cell type B. A bulk sample reads 105. Estimate the fraction of A. Then compute the bulk value if the fraction of A rises to 0.7 with no change inside either cell type.

> [!success]- Solution
> From $x = f\mu_A + (1-f)\mu_B$: $f = (x - \mu_B)/(\mu_A - \mu_B)$.
>
> ```python
> mu_a, mu_b, bulk = 200.0, 10.0, 105.0
> print((bulk - mu_b) / (mu_a - mu_b))        # 0.5
> for fa in (0.5, 0.7):
>     print(fa, fa * mu_a + (1 - fa) * mu_b)  # 105.0, then 143.0
> ```
>
> Bulk expression rises by 36 % (105 → 143) with no regulatory change: a composition shift. This is why tissue-level comparisons need [[Cell-Type Deconvolution]] or single-cell data.

## Mastery checklist

- [ ] 1 Recognized: I can name the four tissue types and give an example of each.
- [ ] 2 Understood: I can explain how tissues differ in organization and function and how they combine into organs.
- [ ] 3 Practiced: I can compute tissue-specificity scores and mixture values from an expression table in Python.
- [ ] 4 Applied: I can query a tissue expression atlas such as GTEx for a gene and interpret its tissue profile.
- [ ] 5 Explained: I can teach why bulk tissue expression confounds composition with regulation, and how deconvolution and single-cell data address it.

## References

[^ap]: [[Anatomy and Physiology 2e (OpenStax)]], tissue level of organization: the four tissue types, epithelial classification, connective tissue, muscle tissue, embryonic origin.
[^ap18]: [[Anatomy and Physiology 2e (OpenStax)]], ch. 18 "The Cardiovascular System: Blood" (blood as a fluid connective tissue).
[^bio7]: [[Biology 2e (OpenStax)]], Unit 7 "Animal Structure and Function".
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of cell differentiation by differential gene expression and of the extracellular matrix.
[^gtex]: [[GTEx Portal]]: V8 release counts; The GTEx Consortium, *Science* 369(6509) (2020), on tissue-specific regulatory effects and cell type composition.
