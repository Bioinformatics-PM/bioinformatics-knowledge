---
aliases:
  - Abbas blood deconvolution
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L3
kind: paper
tier: A
authors:
  - Alexander R. Abbas
  - Kristen Wolslegel
  - Dhaya Seshasayee
  - Zora Modrusan
  - Hilary F. Clark
journal: PLoS ONE
year: 2009
url: "https://doi.org/10.1371/journal.pone.0006098"
access: free
---

# Abbas 2009 - Deconvolution of Blood Microarray Data Identifies Cellular Activation Patterns in Systemic Lupus Erythematosus

> [!abstract]
> An early demonstration that the expression profile of a mixed blood sample can be deconvolved into the contributions of immune cell types, validated on real blood samples and on mixtures of immune cell lines.

## Why this source

Bulk expression data mix many cell types; this paper shows that expression deconvolution, a linear-algebra problem, recovers those contributions accurately, and uses it to find cell-type-specific activation in a disease. It is a concrete biological reason to learn $Ax = b$ and least squares.

## Coverage

Citation: Abbas AR, Wolslegel K, Seshasayee D, Modrusan Z, Clark HF. "Deconvolution of blood microarray data identifies cellular activation patterns in systemic lupus erythematosus". *PLoS ONE* 4(7):e6098 (July 2009). doi:10.1371/journal.pone.0006098. Open access, PubMed Central PMC2699551.

| Part | Content | Vault notes |
|---|---|---|
| Method | Deconvolution of microarray expression into immune cell-type contributions | [[System of Linear Equations]], [[Least Squares]] |
| Validation | Accurate quantification of constituents of real blood samples and of mixtures of immune-derived cell lines | [[Gene Expression]] |
| Application | Systemic lupus erythematosus: expansion and activation of monocytes, NK cells and T helper cells partly underlie the interferon signature | [[Transcriptomics]] |

Cited in [[System of Linear Equations]].

## How to use it

- L3: read after [[Least Squares]]; rebuild the idea on a toy signature matrix, then compare with later deconvolution methods.

## Caveats

- Microarray era; single-cell reference profiles and newer methods have since changed how signature matrices are built.
- Verified in this pass (web search of the PubMed Central record): authors, title, journal, date, DOI and the abstract's claims above. Details of the fitting procedure were not checked; the vault uses the paper only for the deconvolution idea and its validation.
