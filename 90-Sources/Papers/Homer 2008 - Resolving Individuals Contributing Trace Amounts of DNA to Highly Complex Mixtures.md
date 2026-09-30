---
aliases:
  - Homer attack
tags:
  - type/source
  - domain/scientific-practice
  - domain/bioinformatics
  - level/L3
kind: paper
tier: S
authors:
  - Nils Homer
  - Szabolcs Szelinger
  - et al.
  - David W. Craig
journal: PLoS Genetics
year: 2008
url: "https://doi.org/10.1371/journal.pgen.1000167"
access: free
---

# Homer 2008 - Resolving Individuals Contributing Trace Amounts of DNA to Highly Complex Mixtures

> [!abstract]
> A forensic genomics study showing that high-density SNP genotypes can reveal whether a person's DNA is present in a complex mixture, even at under 0.1% of the total.

## Why this source

Written as a forensic method, it had a larger impact on genomic privacy: the same statistic can test whether an individual belongs to a pool of samples, so aggregate allele frequencies published from genome-wide association studies were no longer considered safe. It is the classic example of "membership inference" from summary data, and a reason why human genomic data sit in controlled-access archives.

## Coverage

Citation: Homer N, Szelinger S, Redman M, Duggan D, Tembe W, et al. "Resolving Individuals Contributing Trace Amounts of DNA to Highly Complex Mixtures Using High-Density SNP Genotyping Microarrays". *PLoS Genetics* 4(8):e1000167 (2008). doi:10.1371/journal.pgen.1000167. Free at PMC2516199.

| Part | Content | Vault notes |
|---|---|---|
| Framework | A test statistic comparing an individual's genotypes with mixture and reference allele frequencies | [[Single Nucleotide Polymorphism]], [[Allele Frequency]] |
| Simulations and experiments | Limits of detection, individuals below 0.1% of a mixture | [[Microarray]] |
| Consequence for data sharing | Summary statistics can identify study participants | [[Re-Identification]], [[Genomic Data Privacy]], [[Controlled-Access Data]], [[Genome-Wide Association Study]] |

Cited in [[Research Ethics]].

## How to use it

- L3: read the introduction and the theoretical framework for item 12 of [[Research Ethics]], then explain in one paragraph why publishing per-SNP allele frequencies of cases can leak membership.
- Read it with [[Gymrek 2013 - Identifying Personal Genomes by Surname Inference]], which attacks individual genomes rather than aggregates.

## Caveats

- The privacy implication was drawn by the community rather than being the paper's stated aim.
- Detection power depends on the number of SNPs and on a reference population of matching ancestry.
- Metadata (title, journal, volume, article number, DOI, PMC record) verified in this pass.
