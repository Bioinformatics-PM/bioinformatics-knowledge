---
aliases:
  - Regulatory Affairs
  - Réglementation et normes
tags:
  - type/moc
  - domain/industry
  - domain/scientific-practice
  - domain/bioinformatics
  - level/L3
  - level/M1
prerequisites:
  - "[[Research Ethics]]"
  - "[[Research Data Management]]"
  - "[[Clinical Genomics]]"
  - "[[Drug Discovery]]"
  - "[[Software Engineering]]"
projects:
  - "[[06-mutation-lab]]"
  - "[[10-genomic-pipeline]]"
  - "[[Bioinformatics Lab]]"
sources:
  - "[[European Union 2017 - In Vitro Diagnostic Medical Devices Regulation]]"
  - "[[European Union 2016 - General Data Protection Regulation]]"
  - "[[IMDRF 2013 - Software as a Medical Device Key Definitions]]"
  - "[[Roy 2018 - Standards and Guidelines for Validating Next-Generation Sequencing Bioinformatics Pipelines]]"
---

# Regulation and Standards

> [!abstract]
> The rules that apply when biological data and software leave research: medicines and device regulation (FDA, EMA, MDR, IVDR), clinical laboratory quality (CLIA, ISO 15189), good practices (GxP), software as a medical device, health data protection (GDPR, HIPAA) and the technical standards for exchanging genomic and clinical data.

## Why it matters for bioinformatics

A variant-calling pipeline used to report results to patients is part of a regulated test, and analysis software with a medical purpose can itself be a medical device. In the EU, in vitro diagnostics fall under the IVDR, and genetic data are a special category of personal data under the GDPR.[^ivdr][^gdpr] Internationally, regulators share a definition of software as a medical device based on intended purpose.[^imdrf] Professional guidelines translate these rules into concrete validation work for bioinformatics pipelines.[^roy]

## Before you start

- [[Research Ethics]]: [[Informed Consent]], [[Genomic Data Privacy]], [[Re-Identification]], [[Data Anonymization]].
- [[Research Data Management]]: [[Data Integrity]], [[Metadata]], [[Controlled-Access Data]].
- [[Clinical Genomics]]: [[Clinical Pipeline Validation]], [[Genomic Test Report]].
- [[Drug Discovery]]: [[Clinical Trial]], [[Drug Approval]].
- [[Software Engineering]]: [[Version Control]], [[Unit Testing]], [[Continuous Integration]].

## Learning path

### Stage 3 - Advanced (L3)

1. [[Regulatory Agency]] (L3): know the roles of the FDA (drug, biologic and device centers), the EMA with the European Commission, national competent authorities, notified bodies and ICH harmonization.
2. [[GxP]] (L3): explain good laboratory, clinical and manufacturing practice and why they require documented, traceable work.
3. [[Quality Management System]] (L3): describe a QMS (procedures, document control, training, corrective and preventive action, audits) as in ISO 9001 and ISO 13485.
4. [[Computerized System Validation]] (L3): validate software used in regulated work and meet electronic record rules (21 CFR Part 11 in the US, EU GMP Annex 11).
5. [[Medical Device Regulation]] (L3): explain the EU MDR, device risk classes and the role of notified bodies.
6. [[In Vitro Diagnostic Regulation]] (L3): explain the EU IVDR, its risk classes A to D, performance evaluation and the exemption for in-house tests of health institutions.[^ivdr]
7. [[Software as a Medical Device]] (L3): decide from the intended purpose whether analysis software is a medical device, and how its risk is categorized.[^imdrf]
8. [[Companion Diagnostic]] (L3): explain tests essential for the safe and effective use of a drug and their co-development with it.
9. [[Clinical Laboratory Improvement Amendments]] (L3): know how CLIA certification and CAP accreditation govern US clinical laboratories.
10. [[Laboratory-Developed Test]] (L3): define tests designed and used within one laboratory, and follow the regulatory debate over them in the US and the EU.
11. [[ISO 15189]] (L3): know the international standard for quality and competence of medical laboratories and how accreditation to it works.
12. [[General Data Protection Regulation]] (L3): apply the GDPR to genetic data (special category, legal bases, research provisions, international transfers).[^gdpr]
13. [[Health Insurance Portability and Accountability Act]] (L3): know the HIPAA Privacy Rule, covered entities and its two de-identification methods.
14. [[Genomic Data Standard]] (L3): use GA4GH standards (file formats, Phenopackets, Beacon, the Data Use Ontology) for interoperable genomic data sharing.

### Stage 4 - Frontier (M1)

15. [[IEC 62304]] (M1): apply the medical device software life cycle standard (software safety classes, development, maintenance, problem resolution).
16. [[Fast Healthcare Interoperability Resources]] (M1): exchange clinical and genomic data with HL7 FHIR resources.
17. [[Artificial Intelligence Act]] (M1): know how the EU AI Act treats AI in medical devices as high risk and what it adds to the MDR and IVDR.
18. [[European Health Data Space]] (M1): follow the EU framework for primary and secondary use of health data, including for research.
19. [[Real-World Evidence]] (M1): know how regulators use evidence from health records, registries and claims data in decisions.
20. [[Health Technology Assessment]] (M1): explain how assessment bodies judge added value and cost after approval, and the EU joint clinical assessment.

> [!tip]
> Always read the primary legal text next to any summary: regulations are amended often (transition periods, delegated acts), and dates in secondary sources go stale quickly.

## Uses from other domains

- [[Data Integrity]] ([[Research Data Management]]): ALCOA+ principles behind GxP records.
- [[Data Provenance]] ([[Reproducibility]]) and [[Dependency Management]] ([[Software Engineering]]): the technical basis of traceability and validation.
- [[VCF Format]], [[SAM Format]] ([[Bioinformatics Foundations]]): file formats maintained as community standards.
- [[Biological Ontology]] ([[Bioinformatics Foundations]]): the vocabularies that standards reuse.
- [[Randomized Controlled Trial]] ([[Experimental Design]]): the evidence standard for approval.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| No verified course note yet | | | Use the primary legal texts and guidelines below |

## Reference books

Primary texts rather than books:

- [[European Union 2017 - In Vitro Diagnostic Medical Devices Regulation]]: Regulation (EU) 2017/746 (item 6).[^ivdr]
- [[European Union 2016 - General Data Protection Regulation]]: Regulation (EU) 2016/679 (item 12).[^gdpr]
- [[IMDRF 2013 - Software as a Medical Device Key Definitions]]: the international definition used by regulators (item 7).[^imdrf]
- [[Roy 2018 - Standards and Guidelines for Validating Next-Generation Sequencing Bioinformatics Pipelines]]: validation in a CLIA and CAP setting (items 4, 9).[^roy]

## Lab projects

- [[06-mutation-lab]]: its stated intended purpose ("not a clinical prediction") is what keeps it outside [[Software as a Medical Device]].
- [[10-genomic-pipeline]]: versioned, traceable and tested, the technical prerequisites of [[Computerized System Validation]].
- [[Bioinformatics Lab]]: tests, CI and documented repositories are the software half of a [[Quality Management System]].

## References

[^ivdr]: [[European Union 2017 - In Vitro Diagnostic Medical Devices Regulation]], Regulation (EU) 2017/746.
[^gdpr]: [[European Union 2016 - General Data Protection Regulation]], Regulation (EU) 2016/679, Article 9 on special categories of personal data.
[^imdrf]: [[IMDRF 2013 - Software as a Medical Device Key Definitions]], International Medical Device Regulators Forum.
[^roy]: [[Roy 2018 - Standards and Guidelines for Validating Next-Generation Sequencing Bioinformatics Pipelines]], *Journal of Molecular Diagnostics*.
