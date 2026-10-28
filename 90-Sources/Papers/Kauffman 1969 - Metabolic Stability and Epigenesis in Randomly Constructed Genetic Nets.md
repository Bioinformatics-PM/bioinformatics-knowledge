---
aliases:
  - Kauffman 1969
  - Random Boolean networks (origin)
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - domain/mathematics
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Stuart A. Kauffman
journal: Journal of Theoretical Biology
year: 1969
url: "https://doi.org/10.1016/0022-5193(69)90015-0"
access: paid
---

# Kauffman 1969 - Metabolic Stability and Epigenesis in Randomly Constructed Genetic Nets

> [!abstract]
> The founding paper of random Boolean network models of gene regulation: each gene is a binary on/off element whose next state is a logical function of a few other genes, and the stable cycles of such networks are proposed as models of cell types.

## Why this source

The origin of the Boolean (logical) modeling of genetic regulatory networks that systems biology still uses, and of the idea that attractors of network dynamics correspond to stable cell states. Cite it for the history and the core modeling assumptions, not for current methods.

## Coverage

Citation: Kauffman SA. "Metabolic stability and epigenesis in randomly constructed genetic nets". *Journal of Theoretical Biology* 22(3):437-467 (1969). DOI 10.1016/0022-5193(69)90015-0.

| Part | Content | Vault notes |
|---|---|---|
| Model | Each gene modeled as a binary (on/off) device; large nets built at random, each gene regulated by a few others through a Boolean function | [[Boolean Network]], [[Boolean Algebra]] |
| Dynamics | Nets in which each gene receives two or three inputs behave with great order and stability: they settle into short cycles of states | [[Boolean Network]], [[State Machine]] |
| Interpretation | The distinct modes of behavior (cycles) of one net are compared with the cell types of an organism; differentiation as switching between modes | [[Cell Differentiation]], [[Gene Regulatory Network]] |

Cited in [[Boolean Algebra]].

## How to use it

- L2: read the introduction and the description of the model to see gene regulation written as Boolean functions.
- L3: read it next to [[Boolean Network]] and [[Gene Regulatory Network]]; compare its random wiring with the curated networks of modern logical models.

## Caveats

- Paid article; full text not read in this pass. The bibliographic record (authors, title, journal, volume, issue, pages, DOI) was verified by web search; the content summarized above follows the paper's abstract, whose binary-gene model and claim of order for two or three inputs per gene recur in Kauffman's 1969-1971 follow-up papers.
- Random wiring is a null model: real regulatory networks are not random, and later work fits logical models to specific pathways.
