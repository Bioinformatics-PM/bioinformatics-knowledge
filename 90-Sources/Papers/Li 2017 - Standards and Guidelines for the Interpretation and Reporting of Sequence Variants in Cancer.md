---
aliases:
  - AMP/ASCO/CAP somatic variant guidelines
tags:
  - type/source
  - domain/industry
  - domain/bioinformatics
  - level/L3
kind: paper
tier: S
authors:
  - Marilyn M. Li
  - et al. (AMP, ASCO and CAP working group)
journal: The Journal of Molecular Diagnostics
year: 2017
url: "https://doi.org/10.1016/j.jmoldx.2016.10.002"
access: free
---

# Li 2017 - Standards and Guidelines for the Interpretation and Reporting of Sequence Variants in Cancer

> [!abstract]
> The joint AMP, ASCO and CAP recommendation that classifies somatic variants in cancer into four tiers of clinical significance and standardizes how they are reported.

## Why this source

With NGS cancer testing in routine use, laboratories needed a shared way to interpret and report tumor variants. A multidisciplinary working group chaired by Marilyn Li proposed standard conventions for classification, annotation, interpretation and reporting. It is the somatic counterpart of [[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]], and it explains why "pathogenic" is the wrong question for a tumor variant: the question is clinical actionability.

## Coverage

Citation: Li MM, Datto M, Duncavage EJ, Kulkarni S, Lindeman NI, Roy S, Tsimberidou AM, Vnencak-Jones CL, Wolff DJ, Younes A, Nikiforova MN. "Standards and Guidelines for the Interpretation and Reporting of Sequence Variants in Cancer: A Joint Consensus Recommendation of the Association for Molecular Pathology, American Society of Clinical Oncology, and College of American Pathologists". *The Journal of Molecular Diagnostics* 19(1):4-23 (2017). doi:10.1016/j.jmoldx.2016.10.002. Free at PMC5707196.

| Part | Content | Vault notes |
|---|---|---|
| Tier I | Variants of strong clinical significance | [[Somatic Variant Classification]], [[Precision Oncology]] |
| Tier II | Variants of potential clinical significance | [[Somatic Variant Classification]], [[Biomarker]] |
| Tier III | Variants of unknown clinical significance | [[Somatic Variant Classification]] |
| Tier IV | Benign or likely benign variants | [[Somatic Variant Classification]] |
| Reporting | Standard conventions for annotation and reports | [[Genomic Test Report]], [[Somatic Mutation]] |

Cited in [[Clinical Genomics]].

## How to use it

- L3: after [[Variant Classification]], read the tier definitions and classify a few well-known tumor alterations; compare with a germline classification of the same gene.
- Use it when reading the output of [[Somatic Variant Calling]] pipelines: the tier is the step between a call and a treatment decision.

## Caveats

- Actionability depends on current drug approvals and trials, so tier assignments of specific variants change over time even if the framework does not.
- Germline findings in tumor sequencing fall back under germline rules.
- Metadata (authors, journal, volume, pages, DOI, PMC record) verified in this pass.
