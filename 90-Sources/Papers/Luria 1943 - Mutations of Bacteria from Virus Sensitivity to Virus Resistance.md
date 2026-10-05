---
aliases:
  - Luria-Delbrück experiment
  - Fluctuation test
tags:
  - type/source
  - domain/biology
  - domain/scientific-practice
  - domain/statistics
  - level/L1
  - level/L2
kind: paper
tier: S
authors:
  - Salvador E. Luria
  - Max Delbrück
journal: Genetics
year: 1943
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC1209226/"
access: free
---

# Luria 1943 - Mutations of Bacteria from Virus Sensitivity to Virus Resistance

> [!abstract]
> The fluctuation test: by comparing the number of phage-resistant bacteria across parallel cultures, Luria and Delbrück showed that resistance arises by spontaneous mutation before contact with the virus, not as a response to it.

## Why this source

A model of how to turn two competing hypotheses into two different quantitative predictions about the same measurement. If resistance were induced by contact with the phage, parallel cultures would contain similar numbers of resistant cells; if it arose by random mutation during growth, an early mutation would produce a large resistant clone in some cultures (a "jackpot"), and counts would fluctuate far more than sampling alone allows. The paper made statistical reasoning a tool of bacterial genetics, and the work contributed to the 1969 Nobel Prize in Physiology or Medicine shared by Luria and Delbrück.

## Coverage

Citation: Luria SE, Delbrück M. "Mutations of Bacteria from Virus Sensitivity to Virus Resistance". *Genetics* 28:491-511 (November 1943). Free at PMC1209226.

| Part | Content | Vault notes |
|---|---|---|
| Question | Is resistance to a bacterial virus induced by exposure, or present beforehand as a heritable mutation? | [[Hypothesis]], [[Mutation]] |
| Design | Many small parallel cultures plated with phage, compared with several samples from one large culture | [[Controlled Experiment]], [[Bacteriophage]] |
| Result | Resistant counts in parallel cultures fluctuate far beyond sampling expectations (variance much larger than the mean) | [[Hypothesis]], [[Variance]] |
| Example data | One series of 20 parallel cultures: 11 with no resistant colony, the others 1, 1, 3, 5, 5, 6, 35, 64 and 107 | [[Hypothesis]] |

Cited in [[Hypothesis]].

## How to use it

- L1: read the introduction for the two hypotheses and their predictions, then look at one table of parallel cultures next to the samples from a single culture.
- L2: simulate both hypotheses (as in [[Hypothesis]]) and compare the variance-to-mean ratio of simulated and observed counts; relate the comparison to the [[Poisson Distribution]].

## Caveats

- The mathematical part (the distribution of mutant numbers) is demanding; later work derived the exact distribution and better estimators of mutation rates.
- The counts listed above were checked against secondary reproductions of the paper's table (a historical review and encyclopedic summaries), not against the original table itself; the order of the cultures is not reproduced.
- Verified in this pass: authors, title, journal, volume, pages, month, free PMC record, and the 1969 Nobel Prize connection.
