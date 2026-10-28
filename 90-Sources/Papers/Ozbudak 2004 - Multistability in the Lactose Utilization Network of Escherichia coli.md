---
aliases:
  - Lac operon bistability
tags:
  - type/source
  - domain/biology
  - level/L3
  - level/M1
kind: paper
tier: A
authors:
  - Ertugrul M. Ozbudak
  - Mukund Thattai
  - Han N. Lim
  - Boris I. Shraiman
  - Alexander van Oudenaarden
journal: Nature
year: 2004
url: "https://doi.org/10.1038/nature02298"
access: paid
---

# Ozbudak 2004 - Multistability in the Lactose Utilization Network of Escherichia coli

> [!abstract]
> Single-cell measurements and a model showing that the lactose utilization network of *E. coli* is bistable and hysteretic, because the permease LacY imports an inducer that induces more LacY.

## Why this source

The classic quantitative test of a positive-feedback switch in a natural gene circuit. It turns the lac operon of textbooks into a dynamical system with a phase diagram, and shows how the same circuit can be turned from a hysteretic switch into a graded response.

## Coverage

Citation: Ozbudak EM, Thattai M, Lim HN, Shraiman BI, van Oudenaarden A. "Multistability in the lactose utilization network of *Escherichia coli*". *Nature* 427:737-740 (19 February 2004). doi:10.1038/nature02298.

| Part | Content | Vault notes |
|---|---|---|
| Experiment | Fluorescent reporters of the lac promoter (GFP) and of the gat promoter (HcRed) in single cells, over concentrations of glucose and of TMG, a non-metabolizable inducer | [[Operon]], [[Stochastic Gene Expression]] |
| Feedback | LacY catalyses the uptake of TMG, which induces more LacY: a positive feedback loop | [[Feedback Loop]], [[Bistability]] |
| Result | Phase diagram of the bistable network, a model of uptake and regulation, and conversion of the hysteretic response into a graded one | [[Bistability]], [[Operon]] |

Cited in [[Operon]].

## How to use it

- L3: read after the lac operon section of [[Operon]] and the input functions of [[Gene Regulation]].
- M1: reproduce the bistability with a one-variable positive-feedback model ([[Bistability]]).

## Caveats

- The experiments used TMG, a gratuitous inducer that the cell does not metabolize: do not transpose the result to growth on lactose without checking later work.
- Verified in this pass: authors, title, journal, volume, pages, date, DOI and the abstract findings; the growth conditions were not checked in the full text.
