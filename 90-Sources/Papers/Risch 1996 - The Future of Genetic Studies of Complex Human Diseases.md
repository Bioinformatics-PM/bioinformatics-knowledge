---
aliases:
  - Risch and Merikangas 1996
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Neil Risch
  - Kathleen Merikangas
journal: Science
year: 1996
url: "https://pubmed.ncbi.nlm.nih.gov/8801636/"
access: paid
---

# Risch 1996 - The Future of Genetic Studies of Complex Human Diseases

> [!abstract]
> A two-page Perspective arguing that linkage studies lack the power to find genes of modest effect in complex diseases, that association studies are far more powerful, and that a genome-wide association screen would need a very stringent significance level: the origin of the $5 \times 10^{-8}$ threshold.

## Why this source

It framed genome-wide association studies as a power problem a decade before they became feasible. For genes conferring moderate relative risks, allele-sharing linkage methods (such as affected sib pairs) would need enormous samples, while association designs need far fewer subjects. Its Bonferroni-type correction for the number of tests in a gene-based genome-wide screen gave $5 \times 10^{-8}$, which later became the conventional genome-wide significance threshold of common-variant GWAS.

## Coverage

Citation: Risch N, Merikangas K. "The future of genetic studies of complex human diseases". *Science* 273(5281):1516-1517 (13 September 1996). PMID 8801636.

| Part | Content | Vault notes |
|---|---|---|
| Linkage versus association | Low power of allele-sharing linkage methods for modest effects; much greater power of association designs | [[Statistical Power]], [[Genome-Wide Association Study]] |
| Significance level | A stringent threshold, $5 \times 10^{-8}$, correcting for the number of tests of a genome-wide screen | [[Multiple Testing Correction]], [[Family-Wise Error Rate]] |

## How to use it

- L2: read it with [[Statistical Power]] to see why association studies need thousands of subjects.
- L3: with [[Multiple Testing Correction]], compare its gene-centric count of tests with later estimates of the number of independent common variants.

## Caveats

- A perspective without a methods section: recompute power figures rather than quoting them.
- Verified in this pass: authors, title, journal, volume, issue, pages, date and PMID; the main argument and the origin of the $5 \times 10^{-8}$ threshold, through two independent secondary accounts (the full text was not accessible). The accounts differ on the exact count behind the threshold (about $10^5$ genes with a few variants each, around $10^6$ tests); the later justification by about one million independent common variants comes from HapMap-era work, not from this paper.
