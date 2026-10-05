---
aliases:
  - ACMG/AMP guidelines
  - ACMG/AMP variant classification
tags:
  - type/source
  - domain/industry
  - domain/bioinformatics
  - level/L3
kind: paper
tier: S
authors:
  - Sue Richards
  - et al. (ACMG and AMP joint workgroup)
journal: Genetics in Medicine
year: 2015
url: "https://doi.org/10.1038/gim.2015.30"
access: free
---

# Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants

> [!abstract]
> The joint ACMG and AMP recommendation that defines the five-tier classification of germline sequence variants used by clinical laboratories.

## Why this source

It is the standard behind almost every clinical germline report: the five terms "pathogenic", "likely pathogenic", "uncertain significance", "likely benign" and "benign" for variants in genes that cause Mendelian disorders, and the evidence criteria and combining rules that assign them. A workgroup with representatives of the ACMG, the AMP and the College of American Pathologists wrote it in 2013 to 2015, replacing earlier ACMG guidance. For a bioinformatician it defines what a variant interpretation pipeline must produce and justify.

## Coverage

Citation: Richards S, Aziz N, Bale S, et al. "Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology". *Genetics in Medicine* 17(5):405-424 (2015). doi:10.1038/gim.2015.30. Free at PMC4544753.

| Part | Content | Vault notes |
|---|---|---|
| Terminology | Five standard terms for variants in Mendelian disease genes | [[Variant Classification]], [[Variant of Uncertain Significance]] |
| Evidence criteria | Population data, computational predictions, functional data, segregation, de novo occurrence, allelic data, databases | [[Allele Frequency]], [[Variant Effect Prediction]], [[Trio Analysis]] |
| Combining rules | Criteria weighted by strength and combined into one of the five classes | [[Variant Classification]] |
| Nomenclature and reporting | Standard variant description and report content | [[Variant Nomenclature]], [[Genomic Test Report]] |

Cited in [[Clinical Genomics]], [[Industry and Innovation]] and [[Mutation]].

## How to use it

- L3: read the terminology and evidence sections first, then classify two or three variants by hand from their population frequency, predicted consequence and segregation, before looking at any automated tool.
- Pair it with [[Li 2017 - Standards and Guidelines for the Interpretation and Reporting of Sequence Variants in Cancer]] to see why somatic variants use a different, tier-based system.
- Use it as the specification when adding classification to [[03-genome-diff]] or [[10-genomic-pipeline]].

## Caveats

- Germline, Mendelian disease only: it does not cover somatic variants, pharmacogenomic variants or common risk alleles.
- Many criteria have since been refined for specific genes and evidence types by expert panels; check for gene-specific specifications before applying the generic rules.
- Metadata (title, journal, volume, pages, DOI, PMC record) verified against PubMed Central in this pass.
