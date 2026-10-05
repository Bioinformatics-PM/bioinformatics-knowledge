---
aliases: []
tags:
  - type/source
  - domain/scientific-practice
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - John P. A. Ioannidis
journal: PLoS Medicine
year: 2005
url: "https://doi.org/10.1371/journal.pmed.0020124"
access: free
---

# Ioannidis 2005 - Why Most Published Research Findings Are False

> [!abstract]
> The essay that modeled the probability that a published "significant" finding is true, and argued that in many fields it is below one half.

## Why this source

A founding text of metascience and of the reproducibility debate. It shows with simple algebra that the probability a claimed finding is true depends on statistical power, bias, the number of teams testing the same question, and the pre-study odds that a tested relationship is real. Small studies, small effects, many tested relationships, flexible designs and "hot" fields all push that probability down, a direct warning for high-throughput biology.

## Coverage

Citation: Ioannidis JPA. "Why Most Published Research Findings Are False". *PLoS Medicine* 2(8):e124 (2005). doi:10.1371/journal.pmed.0020124.

| Part | Content | Vault notes |
|---|---|---|
| Model | Positive predictive value of a claimed finding from power, significance level and pre-study odds | [[Statistical Power]], [[P-Value]], [[Bayes' Theorem]] |
| Bias | How bias and multiple independent teams inflate false findings | [[Publication Bias]], [[P-Hacking]], [[Analytical Flexibility]] |
| Corollaries | Conditions under which findings are less likely to be true | [[Reproducibility Crisis]], [[Effect Size]] |

Cited in [[Reproducibility]].

## How to use it

- L2: after [[Hypothesis Testing]] and [[Statistical Power]], recompute the positive predictive value for a few power and prior values in a spreadsheet or a short script.
- L3: relate the "many relationships probed" corollary to genome-wide testing and to [[Multiple Testing Correction]].

## Caveats

- A model and an argument, not an empirical measurement of how many findings are false; its assumptions have been debated.
- Written for biomedical research in general; the numbers in its scenarios are illustrative.
- Metadata (author, journal, volume, article number, DOI) verified in this pass; the journal is open access.
