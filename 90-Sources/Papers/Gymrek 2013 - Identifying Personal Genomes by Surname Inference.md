---
aliases: []
tags:
  - type/source
  - domain/scientific-practice
  - domain/bioinformatics
  - level/L3
kind: paper
tier: S
authors:
  - Melissa Gymrek
  - Amy L. McGuire
  - David Golan
  - Eran Halperin
  - Yaniv Erlich
journal: Science
year: 2013
url: "https://doi.org/10.1126/science.1229566"
access: paid
---

# Gymrek 2013 - Identifying Personal Genomes by Surname Inference

> [!abstract]
> A demonstration that research participants can be re-identified by inferring their surname from Y-chromosome markers and public genealogy databases.

## Why this source

It showed that "de-identified" genomes are not anonymous. Profiling short tandem repeats on the Y chromosome (Y-STRs) and querying recreational genetic genealogy databases recovered surnames, because relatives who share the paternal line had uploaded their data. Combined with metadata such as age and state, the surname pointed to the person. The authors estimated that about 12% of US males could be subject to surname recovery.

## Coverage

Citation: Gymrek M, McGuire AL, Golan D, Halperin E, Erlich Y. "Identifying Personal Genomes by Surname Inference". *Science* 339(6117):321-324 (2013). doi:10.1126/science.1229566.

| Part | Content | Vault notes |
|---|---|---|
| Attack | Y-STR profiling and genealogy database queries to infer surnames | [[Re-Identification]] |
| Triangulation | Surname plus age and state metadata to identify individuals | [[Genomic Data Privacy]], [[Data Anonymization]] |
| Implications | Consent, data release and the familial nature of genomes | [[Informed Consent]], [[Controlled-Access Data]] |

Cited in [[Research Ethics]].

## How to use it

- L3: read it with [[Homer 2008 - Resolving Individuals Contributing Trace Amounts of DNA to Highly Complex Mixtures]] for item 12 of [[Research Ethics]]; list which pieces of metadata made the attack possible.
- Use it to argue why removing names is not enough to anonymize genomic data (item 13).

## Caveats

- Works on males only (Y chromosome) and depends on the coverage of genealogy databases, which has grown a lot since 2013.
- Metadata (authors, journal, volume, issue, pages, DOI) verified in this pass; open-access status not verified.
