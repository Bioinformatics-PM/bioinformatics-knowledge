---
aliases:
  - PSORTb
  - PSORTb 3.0
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Nancy Y. Yu
  - James R. Wagner
  - Matthew R. Laird
  - et al.
  - Fiona S. L. Brinkman
journal: Bioinformatics
year: 2010
url: "https://academic.oup.com/bioinformatics/article/26/13/1608/201357"
access: free
---

# Yu 2010 - PSORTb 3.0

> [!abstract]
> "PSORTb 3.0: improved protein subcellular localization prediction with refined localization subcategories and predictive capabilities for all prokaryotes": a widely used predictor of where a bacterial or archaeal protein ends up in the cell.

## Why this source

It shows how cell envelope architecture becomes a parameter of a bioinformatics tool: the predictor uses separate localization sites for Gram-negative bacteria, Gram-positive bacteria and archaea.

## Coverage

Citation: Yu NY, Wagner JR, Laird MR, et al., Brinkman FSL. *Bioinformatics* 26(13):1608-1615 (2010).

| Part | Content | Vault notes |
|---|---|---|
| Localization sites | 13 support vector machines, one per site: 5 Gram-negative, 4 Gram-positive and 4 archaeal sites | [[Bacteria]], [[Archaea]], [[Protein Targeting]] |
| Scope | Predictions for archaea and for bacteria with atypical membrane or cell wall topologies | [[Bacteria]] |

Cited in [[Bacteria]].

## How to use it

- L2: read the introduction for the list of prokaryotic compartments.
- L3: compare the predictor's output categories with an annotated proteome ([[Gene Annotation]]).

## Caveats

- Version 3.0 (2010); check the current release and documentation before using the tool.
- Metadata and the counts of localization sites verified in this pass; the author list is abbreviated.
