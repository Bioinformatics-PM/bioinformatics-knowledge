---
aliases:
  - FBA primer
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Jeffrey D. Orth
  - Ines Thiele
  - Bernhard Ø. Palsson
journal: Nature Biotechnology
year: 2010
url: "https://doi.org/10.1038/nbt.1614"
access: free
---

# Orth 2010 - What Is Flux Balance Analysis

> [!abstract]
> A short primer on flux balance analysis: a metabolic network written as a stoichiometric matrix, the steady-state mass balance $Sv = 0$, and an optimization that picks one flux distribution.

## Why this source

The standard first reading on constraint-based metabolic modeling, by the group that developed many of its genome-scale models. It turns a metabolic map into linear algebra in a few pages, with worked examples and a pointer to software (the COBRA Toolbox).

## Coverage

Citation: Orth JD, Thiele I, Palsson BØ. "What is flux balance analysis?" *Nature Biotechnology* (March 2010). doi:10.1038/nbt.1614. Open author version: PubMed Central PMC3108565.

| Part | Content | Vault notes |
|---|---|---|
| Representation | Stoichiometric matrix $S$ (metabolites by reactions) and flux vector $v$ | [[Stoichiometric Matrix]], [[System of Linear Equations]] |
| Steady state | Mass balance: at steady state, production equals consumption of every compound, $Sv = 0$ | [[System of Linear Equations]], [[Fundamental Theorem of Linear Algebra]] |
| Optimization | Choosing one flux distribution by optimizing an objective under bounds | [[Flux Balance Analysis]], [[Linear Programming]] |

Cited in [[System of Linear Equations]].

## How to use it

- L2: read the representation and steady-state parts while studying $Ax = b$ and null spaces.
- L3: reproduce the worked examples with a toy network, then with a genome-scale model in a constraint-based modeling package.

## Caveats

- A primer: it does not cover dynamic or kinetic models.
- Verified in this pass (web search): authors, title, journal, month and year, DOI, PMC identifier, and the steady-state mass balance $Sv = 0$. Volume and page numbers were not checked; the DOI page was not opened (web fetching blocked).
