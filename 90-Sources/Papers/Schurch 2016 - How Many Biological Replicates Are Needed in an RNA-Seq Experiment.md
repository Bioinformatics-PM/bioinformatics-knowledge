---
aliases:
  - Schurch et al. 2016
  - How many biological replicates are needed in an RNA-seq experiment and which differential expression tool should you use
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Nicholas J. Schurch
  - et al.
journal: RNA
year: 2016
url: "https://doi.org/10.1261/rna.053959.115"
access: free
---

# Schurch 2016 - How Many Biological Replicates Are Needed in an RNA-Seq Experiment

> [!abstract]
> "How many biological replicates are needed in an RNA-seq experiment and which differential expression tool should you use?": an RNA-seq experiment with 48 biological replicates in each of two conditions, subsampled to measure how the number of replicates and the choice of tool change what is detected.

## Why this source

Most power calculations rest on a model; this study measured power empirically, by treating the comparison of all 48 replicates as a reference and asking how much of it smaller subsets recover. With three replicates, nine of the eleven tools tested found only 20 to 40 % of the significantly differentially expressed genes. The authors recommend at least six biological replicates, rising to at least twelve when it matters to find differentially expressed genes at all fold changes; recovering more than 85 % of them at every fold change needed more than 20 replicates.

## Coverage

Citation: Schurch NJ, et al. "How many biological replicates are needed in an RNA-seq experiment and which differential expression tool should you use?". *RNA* 22(6):839-851 (2016). doi:10.1261/rna.053959.115. Free full text at PMC4878611.

| Part | Content | Vault notes |
|---|---|---|
| Design | 48 biological replicates per condition; subsets compared with the full-data reference | [[Biological Replicate]], [[Statistical Power]] |
| Replicates | Fraction of significantly differentially expressed genes recovered against replicate number and fold change; recommendations of at least 6, or at least 12 | [[Statistical Power]], [[Sequencing Experiment Design]] |
| Tools | Eleven differential expression tools compared on true and false positives; edgeR and DESeq2 lead below twelve replicates; most tools control the false discovery rate | [[Differential Expression Analysis]], [[False Discovery Rate]] |

## How to use it

- L2: read the abstract and the replicate figures with [[Statistical Power]], and compare them with model-based power curves.
- L3: read the tool comparison with [[Differential Expression Analysis]].

## Caveats

- One experimental system and the tool versions of 2016; the number of replicates needed depends on the biological variability of the system studied.
- The early online abstract says eight of the eleven tools found 20 to 40 % of the genes with three replicates; the published version says nine.
- Verified in this pass: title, journal, volume, issue, pages, year, DOI, PMCID, the 48-replicate design, the replicate recommendations and the tool ranking stated in the abstract.
