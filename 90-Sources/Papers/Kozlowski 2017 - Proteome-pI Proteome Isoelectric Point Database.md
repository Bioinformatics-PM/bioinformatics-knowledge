---
aliases:
  - Proteome-pI
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L3
  - level/M1
kind: paper
tier: A
authors:
  - Lukasz P. Kozlowski
journal: Nucleic Acids Research
year: 2017
url: "https://academic.oup.com/nar/article/45/D1/D1112/2333931"
access: free
---

# Kozlowski 2017 - Proteome-pI Proteome Isoelectric Point Database

> [!abstract]
> A database of predicted isoelectric points for the proteins of thousands of proteomes, computed with many prediction methods, with virtual two-dimensional gels.

## Why this source

It turns the isoelectric point from a single-protein number into a proteome-wide statistic: predicted pI values for every protein of thousands of proteomes, several methods side by side, and tools to draw virtual 2D-PAGE maps (pI against molecular weight) or to select proteome fractions by pI and mass. Its discussion states the well-known observation that pI distributions of proteomes are bimodal, the starting point for comparative studies of protein charge across organisms.

## Coverage

Citation: Kozlowski LP. "Proteome-pI: proteome isoelectric point database". *Nucleic Acids Research* 45(D1):D1112-D1116 (Database issue, January 2017; published online in 2016). doi:10.1093/nar/gkw978. Free at PMC5210655.

| Part | Content | Vault notes |
|---|---|---|
| Content | Predicted pI for the proteins of 5,029 proteomes, with 18 methods | [[Isoelectric Point]], [[Proteome]] |
| Tools | Virtual 2D-PAGE plots; custom proteome fractions by pI and molecular weight | [[Isoelectric Point]], [[Gel Electrophoresis]] |
| Discussion | The distribution of protein isoelectric points in proteomes is bimodal | [[Isoelectric Point]] |

Cited in [[Isoelectric Point]].

## How to use it

- **L3**: download the predicted pI values of one proteome and plot their histogram; compare with your own calculator on the same sequences ([[Isoelectric Point#Frontier (M1)]]).
- **M1**: compare the pI distributions of organisms from different environments, and test whether the shape survives a change of prediction method.

## Caveats

- Verified in this pass: the citation (journal, volume, issue, pages, DOI, PMC record) and the database content (5,029 proteomes, 18 methods, virtual 2D-PAGE, fractions by pI and molecular weight), plus the statement that proteome pI distributions are bimodal. The rest of the discussion was not re-read.
- Values are predictions from sequence, not measurements: they inherit the errors of the pKa sets ([[Kozlowski 2016 - IPC Isoelectric Point Calculator]]) and ignore modifications and folding.
- An update (Proteome-pI 2.0, 2021) extends the database to more proteomes and methods; its figures were not checked here.
