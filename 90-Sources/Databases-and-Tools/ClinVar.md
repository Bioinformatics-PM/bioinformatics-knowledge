---
aliases:
  - NCBI ClinVar
tags:
  - type/source
  - domain/bioinformatics
  - domain/industry
  - domain/biology
  - level/L2
  - level/L3
kind: database
tier: A
authors:
  - Melissa J. Landrum
institution: NCBI/NLM/NIH
year:
edition:
url: "https://www.ncbi.nlm.nih.gov/clinvar/"
access: free
---

# ClinVar

> [!abstract]
> NCBI's free public archive of human genetic variants and their relationship to disease, as classified and submitted by laboratories and expert groups around the world.

## Why this source

When a variant has been seen in patients, ClinVar is usually where its classification can be read: each record gives the variant's standard (HGVS) name, identifiers, the classifications submitted and their aggregation. It shows in practice the gap between a molecular consequence ("missense", "stop gained") and a clinical classification, which is exactly the line that [[06-mutation-lab]] does not cross.

## Coverage

Key publication: Landrum MJ et al. "ClinVar: updates to support classifications of both germline and somatic variants". *Nucleic Acids Research* 53(D1) (2025 database issue; published online November 2024). doi:10.1093/nar/gkae1090. At that update: more than 3 million variants submitted by more than 2,800 organizations, and three classification types (germline, oncogenicity, and clinical impact of somatic variants).

| Part | Content | Vault notes |
|---|---|---|
| Variant records | HGVS names, identifiers, submitted and aggregated classifications | [[Variant Classification]], [[Variant Nomenclature]] |
| Germline classifications | Five-tier terms of the ACMG/AMP guidelines | [[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]], [[Genetic Disease]] |
| Somatic classifications | Oncogenicity and clinical impact | [[Somatic Mutation]], [[Li 2017 - Standards and Guidelines for the Interpretation and Reporting of Sequence Variants in Cancer]] |
| Downloads | VCF and tab-delimited files | [[VCF Format]], [[Variant Annotation]] |

Record used in the vault: variation 15333, `NM_000518.5(HBB):c.20A>T (p.Glu7Val)`, rs334, the sickle-cell (Hb S) allele, also known as Glu6Val in the classical numbering of the mature β-globin chain; heterozygosity corresponds to sickle-cell trait and homozygosity to sickle-cell anemia.

Cited in [[Missense Mutation]].

## How to use it

- L2: look up a well-known variant (the sickle-cell allele above), read its HGVS names at DNA and protein level, and compare the protein position with the one in older papers.
- L3: download the ClinVar VCF, intersect it with the output of [[03-genome-diff]] or [[10-genomic-pipeline]], and count how many of your missense variants have a classification (most will not).

## Caveats

- Classifications are submitted by many laboratories and can conflict or change; always read the review status and the date.
- Germline and somatic classifications answer different questions; do not mix them.
- Verified in this pass: the 2025 update (title, journal, DOI, figures and classification types) and the record for variation 15333 (HGVS names, rs334, the alternative name Glu6Val). The launch year and the full author list were not verified; `year` is left empty.
