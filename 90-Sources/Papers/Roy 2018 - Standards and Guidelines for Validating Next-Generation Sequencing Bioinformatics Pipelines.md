---
aliases:
  - AMP/CAP pipeline validation guidelines
tags:
  - type/source
  - domain/industry
  - domain/bioinformatics
  - level/L3
kind: paper
tier: S
authors:
  - Somak Roy
  - et al. (AMP working group with CAP representation)
journal: The Journal of Molecular Diagnostics
year: 2018
url: "https://doi.org/10.1016/j.jmoldx.2017.11.003"
access: paid
---

# Roy 2018 - Standards and Guidelines for Validating Next-Generation Sequencing Bioinformatics Pipelines

> [!abstract]
> The AMP and CAP joint recommendation of 17 best practices for designing, validating and operating clinical NGS bioinformatics pipelines.

## Why this source

Before it, laboratories validated their NGS pipelines in very different ways, and a poorly validated pipeline can produce wrong results that reach patients. The Association for Molecular Pathology, with representatives of the College of American Pathologists and the American Medical Informatics Association, wrote 17 consensus recommendations. It is the closest thing to a specification of what "a validated clinical pipeline" means in practice.

## Coverage

Citation: Roy S, Coldren C, Karunamurthy A, Kip NS, Klee EW, Lincoln SE, Leon A, Pullambhatla M, Temple-Smolkin RL, Voelkerding KV, Wang C, Carter AB. "Standards and Guidelines for Validating Next-Generation Sequencing Bioinformatics Pipelines: A Joint Recommendation of the Association for Molecular Pathology and the College of American Pathologists". *The Journal of Molecular Diagnostics*, January 2018 issue. doi:10.1016/j.jmoldx.2017.11.003.

| Part | Content | Vault notes |
|---|---|---|
| Scope | Design, development, validation and operation of clinical NGS pipelines | [[Clinical Pipeline Validation]] |
| Validation by the laboratory | Each laboratory offering NGS testing validates its own pipeline | [[Clinical Pipeline Validation]], [[Clinical Laboratory Improvement Amendments]] |
| Documentation | Pipeline documented according to laboratory accreditation standards | [[Computerized System Validation]], [[Quality Management System]] |
| Sample identity | Identity of each sample preserved through the pipeline, with identifier requirements | [[Data Integrity]], [[Data Provenance]] |
| People | Role of a trained, qualified molecular professional | [[Genomic Test Report]] |

Cited in [[Clinical Genomics]] and [[Regulation and Standards]].

## How to use it

- L3: read the list of 17 recommendations as a checklist, then write a one-page validation plan for [[10-genomic-pipeline]] (reference samples, accuracy metrics, versioning, revalidation triggers).
- Read it with [[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]]: validation covers the pipeline up to the variant call, classification comes after.

## Caveats

- US framework (CLIA, CAP accreditation); in Europe, ISO 15189 accreditation and the IVDR apply, see [[European Union 2017 - In Vitro Diagnostic Medical Devices Regulation]].
- Volume and page numbers, and free-access status, were not verified in this pass; title, authors, journal, issue date and DOI were.
