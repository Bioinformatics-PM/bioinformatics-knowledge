---
aliases:
  - Genomic Medicine
  - Clinical Bioinformatics
  - Génomique clinique
tags:
  - type/moc
  - domain/industry
  - domain/bioinformatics
  - domain/biology
  - level/L3
  - level/M1
prerequisites:
  - "[[Genetics]]"
  - "[[NGS Data Analysis]]"
  - "[[Genomics]]"
  - "[[Population Genomics]]"
  - "[[Research Ethics]]"
  - "[[Industry Landscape]]"
projects:
  - "[[03-genome-diff]]"
  - "[[06-mutation-lab]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]]"
  - "[[Li 2017 - Standards and Guidelines for the Interpretation and Reporting of Sequence Variants in Cancer]]"
  - "[[Relling 2011 - Clinical Pharmacogenetics Implementation Consortium]]"
  - "[[Roy 2018 - Standards and Guidelines for Validating Next-Generation Sequencing Bioinformatics Pipelines]]"
  - "[[UCSC Genome Browser]]"
---

# Clinical Genomics

> [!abstract]
> The use of genome sequencing and genotyping in patient care: choosing the test, turning variants into a classified and reported result, and the main applications (rare disease diagnosis, pharmacogenomics, precision oncology, newborn and prenatal screening).

## Why it matters for bioinformatics

In a clinical laboratory, the bioinformatics pipeline is part of a medical test: its output is a report that changes a diagnosis or a treatment. The work follows shared standards, such as the ACMG/AMP five-tier classification of germline variants, the AMP/ASCO/CAP tiers for somatic variants in cancer, CPIC dosing guidelines and professional standards for validating NGS pipelines.[^acmg][^amp][^cpic][^roy]

## Before you start

- [[Genetics]]: [[Mendelian Inheritance]], [[Pedigree Analysis]], [[Genetic Disease]], [[Mutation]], [[Missense Mutation]], [[Nonsense Mutation]], [[Frameshift Mutation]], [[Structural Variant]], [[Somatic Mutation]].
- [[NGS Data Analysis]]: [[Read Mapping]], [[Sequencing Coverage]], [[Variant Calling]], [[Variant Filtering]].
- [[Genomics]]: [[Genetic Variant]], [[Variant Normalization]], [[Variant Annotation]], [[Variant Effect Prediction]], [[VCF Format]].
- [[Population Genomics]]: [[Allele Frequency]], [[Population Structure]].
- [[Research Ethics]]: [[Informed Consent]], [[Genomic Data Privacy]].

## Learning path

### Stage 3 - Advanced (L3)

1. [[Genetic Testing]] (L3): distinguish diagnostic, predictive, carrier, prenatal and pharmacogenetic tests and who orders them.
2. [[Clinical Validity]] (L3): separate analytical validity, clinical validity and clinical utility when judging a test.
3. [[Diagnostic Yield]] (L3): compare the yield, blind spots and costs of gene panels, exomes and genomes for rare disease diagnosis.
4. [[Variant Nomenclature]] (L3): write and parse HGVS descriptions at DNA, RNA and protein level on the right transcript.
5. [[Variant Classification]] (L3): apply the ACMG/AMP criteria to classify a germline variant as pathogenic, likely pathogenic, uncertain, likely benign or benign.[^acmg]
6. [[Variant of Uncertain Significance]] (L3): explain why most rare variants are VUS, how they are reported and how they get reclassified.
7. [[Variant Prioritization]] (L3): filter and rank variants by frequency, consequence, inheritance model and phenotype match.
8. [[Trio Analysis]] (L3): use parent-child sequencing to find de novo, compound heterozygous and recessive variants.
9. [[Clinical Pipeline Validation]] (L3): validate a bioinformatics pipeline for clinical use (accuracy, reference materials, versioning, revalidation).[^roy]
10. [[Genomic Test Report]] (L3): read and draft a clinical report (result, classification, evidence, limitations, recommendations).
11. [[Secondary Finding]] (L3): explain how actionable findings unrelated to the indication are handled and why the ACMG keeps a gene list.
12. [[Genetic Counseling]] (L3): know what counselors do before and after testing and why results need them.
13. [[Pharmacogenomics]] (L3): translate a genotype into a drug and dose recommendation with CPIC guidelines.[^cpic]
14. [[Star Allele]] (L3): call and name pharmacogene haplotypes (CYP2D6, CYP2C19) and derive a metabolizer phenotype.
15. [[Precision Oncology]] (L3): match tumor alterations to targeted therapies and trials.
16. [[Somatic Variant Classification]] (L3): classify somatic variants in the four AMP/ASCO/CAP tiers of clinical significance.[^amp]
17. [[Newborn Screening]] (L3): explain biochemical newborn screening and the current studies of genomic newborn screening.
18. [[Non-Invasive Prenatal Testing]] (L3): explain how cell-free DNA in maternal blood is used to screen for fetal aneuploidy, and its limits.
19. [[Direct-to-Consumer Genetic Testing]] (L3): compare consumer tests with clinical tests (validity, privacy, confirmation).
20. [[National Genomic Medicine Initiative]] (L3): know the national programs that bring genome sequencing into health systems and how they share data.

### Stage 4 - Frontier (M1)

21. [[Tumor Mutational Burden]] (M1): compute tumor mutational burden and understand its use and limits as a predictive biomarker.
22. [[Liquid Biopsy]] (M1): detect circulating tumor DNA and explain sensitivity limits at low tumor fraction.

> [!tip]
> Do items 4 to 8 on real public cases (ClinVar records) with the output of [[10-genomic-pipeline]]: classification is learned by practice, and disagreements between laboratories are instructive.

## Uses from other domains

- [[Whole-Genome Sequencing]], [[Exome Sequencing]] and [[Amplicon Sequencing]] ([[Biotechnology]]): the test technologies behind genomes, exomes and gene panels.
- [[Somatic Variant Calling]] ([[NGS Data Analysis]]) and [[Cancer]] ([[Cell Biology]]): the basis of precision oncology.
- [[Polygenic Risk Score]] ([[Population Genomics]]): risk prediction beyond monogenic variants.
- [[Bayes' Theorem]] ([[Probability]]): Bayesian adaptations of the variant classification framework.
- [[Sensitivity and Specificity]] ([[Statistical Inference]]): analytical validation metrics.
- [[Mass Spectrometry]] ([[Biotechnology]]): the technique of biochemical newborn screening.
- [[Biomarker]] ([[Drug Discovery]]): predictive markers in oncology.
- [[Companion Diagnostic]], [[ISO 15189]], [[Clinical Laboratory Improvement Amendments]], [[In Vitro Diagnostic Regulation]] ([[Regulation and Standards]]): the rules of clinical testing.
- [[Genetic Discrimination]] and [[Broad Consent]] ([[Research Ethics]]).

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[UCSC Genome Browser]] | UC Santa Cruz | L3 | Browser tutorials, including a Clinical Genetics tutorial; public variation tracks such as gnomAD next to your own calls (items 4 to 8)[^ucsc] |

## Reference books

The standards themselves are the reference texts:

- [[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]]: germline classification (items 5, 6).[^acmg]
- [[Li 2017 - Standards and Guidelines for the Interpretation and Reporting of Sequence Variants in Cancer]]: somatic tiers (item 16).[^amp]
- [[Relling 2011 - Clinical Pharmacogenetics Implementation Consortium]]: the consortium behind pharmacogenomic guidelines (items 13, 14).[^cpic]
- [[Roy 2018 - Standards and Guidelines for Validating Next-Generation Sequencing Bioinformatics Pipelines]]: pipeline validation (item 9).[^roy]

## Lab projects

- [[03-genome-diff]]: variant detection and consequence, the input of [[Variant Nomenclature]] and [[Variant Classification]].
- [[06-mutation-lab]]: molecular consequence only; the gap between "missense" and "pathogenic" is exactly what this subdomain fills.
- [[10-genomic-pipeline]]: calling and annotation; add a validation report to practice [[Clinical Pipeline Validation]].

## References

[^acmg]: [[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]], ACMG and AMP joint consensus, *Genetics in Medicine*.
[^amp]: [[Li 2017 - Standards and Guidelines for the Interpretation and Reporting of Sequence Variants in Cancer]], AMP, ASCO and CAP joint consensus, *Journal of Molecular Diagnostics*.
[^cpic]: [[Relling 2011 - Clinical Pharmacogenetics Implementation Consortium]], *Clinical Pharmacology and Therapeutics*.
[^ucsc]: [[UCSC Genome Browser]], tutorials and 2025 update.
[^roy]: [[Roy 2018 - Standards and Guidelines for Validating Next-Generation Sequencing Bioinformatics Pipelines]], AMP and CAP joint recommendation, *Journal of Molecular Diagnostics*.
