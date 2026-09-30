---
aliases:
  - Rule of five paper
  - Lipinski's rule of five
tags:
  - type/source
  - domain/industry
  - domain/chemistry
  - level/L3
kind: paper
tier: S
authors:
  - Christopher A. Lipinski
  - Franco Lombardo
  - Beryl W. Dominy
  - Paul J. Feeney
journal: Advanced Drug Delivery Reviews
year: 1997
url: "https://doi.org/10.1016/S0169-409X(96)00423-1"
access: paid
---

# Lipinski 1997 - Experimental and Computational Approaches to Estimate Solubility and Permeability

> [!abstract]
> The paper that introduced the "rule of 5", a simple computational filter flagging compounds likely to have poor oral absorption or permeation.

## Why this source

The most cited heuristic of medicinal chemistry. From the properties of compounds that reached clinical development, the authors derived that poor absorption or permeation is more likely when a molecule has more than 5 hydrogen-bond donors, more than 10 hydrogen-bond acceptors, a molecular weight above 500, or a calculated log P above 5. It showed how cheap computed descriptors can steer chemistry before expensive experiments.

## Coverage

Citation: Lipinski CA, Lombardo F, Dominy BW, Feeney PJ. "Experimental and computational approaches to estimate solubility and permeability in drug discovery and development settings". *Advanced Drug Delivery Reviews* 23:3-25 (1997). doi:10.1016/S0169-409X(96)00423-1.

| Part | Content | Vault notes |
|---|---|---|
| Experimental approaches | Measuring solubility and permeability in discovery and development | [[ADMET]] |
| Computational approaches | Estimating solubility and permeability from structure | [[ADMET]], [[Quantitative Structure-Activity Relationship]] |
| Rule of 5 | Four property thresholds for poor absorption or permeation | [[Lead Optimization]] |

Cited in [[Drug Discovery]].

## How to use it

- L3: read the rule-of-5 section for item 13 of [[Drug Discovery]]; then compute the four properties for a few approved drugs with a cheminformatics library and find the exceptions.
- Use it as an example of a descriptor-based filter before studying full [[Quantitative Structure-Activity Relationship]] models.

## Caveats

- A heuristic for oral absorption, not a law of drug-likeness: many approved drugs (for example natural products and compounds taken up by transporters) break it, as the authors themselves noted for some compound classes.
- The paper was reprinted later in the same journal; check which version a text cites.
- Metadata (authors, title, journal, volume, pages, publisher identifier) verified in this pass.
