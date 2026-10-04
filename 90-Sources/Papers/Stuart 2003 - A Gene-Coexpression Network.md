---
aliases:
  - Gene-coexpression network across species
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Joshua M. Stuart
  - Eran Segal
  - Daphne Koller
  - Stuart K. Kim
journal: Science
year: 2003
url: "https://doi.org/10.1126/science.1087447"
access: paid
---

# Stuart 2003 - A Gene-Coexpression Network

> [!abstract]
> A landmark co-expression network: genes linked when their expression profiles are correlated across thousands of microarrays, with links conserved across humans, flies, worms and yeast.

## Why this source

A clear example of building a graph from data rather than from direct physical measurements: vertices are genes, edges are statistically supported co-expression, and conservation across species is used as evidence of functional relationship.

## Coverage

Citation: Stuart JM, Segal E, Koller D, Kim SK. "A gene-coexpression network for global discovery of conserved genetic modules". *Science* 302(5643):249 (2003). doi:10.1126/science.1087447.

| Part | Content | Vault notes |
|---|---|---|
| Data | Coexpressed gene pairs across 3,182 DNA microarrays from humans, flies, worms and yeast | [[Gene Co-Expression Network]], [[Gene Expression]] |
| Network | 22,163 coexpression relationships conserved across evolution | [[Graph]], [[Network Module]] |
| Interpretation | Conserved coexpression as evidence of functional relationship | [[Biological Network]] |

Cited in [[Graph]].

## How to use it

- L2: read the abstract and the network construction as an example of a weighted, thresholded graph.
- L3: compare with modern co-expression methods in [[Gene Co-Expression Network]].

## Caveats

- Microarray era; current co-expression networks are mostly built from RNA-seq and single-cell data.
- Verified in this pass: authors, title, journal, volume, issue, first page, DOI and the abstract figures quoted above.
