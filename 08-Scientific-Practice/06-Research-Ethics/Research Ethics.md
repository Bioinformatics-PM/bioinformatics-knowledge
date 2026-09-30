---
aliases:
  - Responsible Conduct of Research
  - Éthique de la recherche
tags:
  - type/moc
  - domain/scientific-practice
  - domain/bioinformatics
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Scientific Method]]"
  - "[[Scientific Literature]]"
  - "[[Research Data Management]]"
  - "[[Genetics]]"
  - "[[Population Genomics]]"
projects:
  - "[[06-mutation-lab]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[On Being a Scientist (National Academies)]]"
  - "[[Coursera Stanford - Writing in the Sciences]]"
  - "[[Homer 2008 - Resolving Individuals Contributing Trace Amounts of DNA to Highly Complex Mixtures]]"
  - "[[Gymrek 2013 - Identifying Personal Genomes by Surname Inference]]"
  - "[[Popejoy 2016 - Genomics Is Failing on Diversity]]"
  - "[[Carroll 2020 - The CARE Principles for Indigenous Data Governance]]"
---

# Research Ethics

> [!abstract]
> The duties that come with doing research: integrity toward the scientific record, respect and protection for the people whose samples and data are studied, fairness toward the communities and countries that provide biological resources, and care about misuse.

## Why it matters for bioinformatics

Genomic data are identifying, shared with relatives and permanent. Researchers showed that individuals can be detected in pooled GWAS summary statistics and that anonymous genomes can be re-identified from public genealogy data,[^homer][^gymrek] so data sharing, consent and access control are part of the bioinformatician's job, not only the clinician's. Computational biology programs include a dedicated ethics course for this reason.[^cmu]

## Before you start

- [[Scientific Method]] and [[Scientific Literature]]: [[Peer Review]], [[Retraction]].
- [[Research Data Management]]: [[Controlled-Access Data]], [[Data License]], [[Metadata]].
- [[Genetics]] and [[Population Genomics]]: [[Single Nucleotide Polymorphism]], [[Genome-Wide Association Study]], [[Population Structure]].

## Learning path

### Stage 2 - Core (L2)

1. [[Research Integrity]] (L2): state the principles of honest and responsible research and where national and European codes of conduct define them.[^obas]
2. [[Research Misconduct]] (L2): define fabrication, falsification and plagiarism, and how image and data manipulation are detected.
3. [[Plagiarism]] (L2): recognize plagiarism and self-plagiarism of text, figures and code, and cite or license reuse correctly.[^sciwrite]
4. [[Authorship]] (L2): apply authorship criteria (ICMJE) and contributor roles (CRediT), and recognize gift and ghost authorship.[^sciwrite]
5. [[Conflict of Interest]] (L2): identify financial and non-financial conflicts and declare them.

### Stage 3 - Advanced (L3)

6. [[Human Subjects Research]] (L3): trace the rules for research on people from the Nuremberg Code to the Declaration of Helsinki and the Belmont Report.
7. [[Research Ethics Committee]] (L3): explain what an ethics committee (IRB in the US) reviews and when a data-only study needs approval.
8. [[Informed Consent]] (L3): list the elements of valid consent and check whether a dataset's consent covers a new use.
9. [[Broad Consent]] (L3): compare specific, broad and dynamic consent for biobanks and future research.
10. [[Ethical, Legal and Social Implications]] (L3): explain the ELSI tradition that accompanied the Human Genome Project and its main questions.
11. [[Genomic Data Privacy]] (L3): explain why genomes are identifying, familial and permanent, and what that implies for sharing.
12. [[Re-Identification]] (L3): describe the attacks on genomic data (membership inference from summary statistics, surname inference, genealogy searches).[^homer][^gymrek]
13. [[Data Anonymization]] (L3): distinguish anonymization from pseudonymization and explain why genomic data are rarely truly anonymous.
14. [[Genetic Discrimination]] (L3): know the risks in insurance and employment and the legal protections (GINA in the US, national laws in Europe).
15. [[Diversity in Genomic Research]] (L3): quantify the European-ancestry bias of genomic studies and its consequences for medicine.[^popejoy]
16. [[Animal Research Ethics]] (L3): apply the 3Rs (replace, reduce, refine) and see where in silico methods replace animals.
17. [[Dual-Use Research of Concern]] (L3): recognize research, data or models that could be misused to cause harm, and the oversight that applies.
18. [[Nagoya Protocol]] (L3): explain access and benefit-sharing for genetic resources and the compliance checks before using foreign samples.

### Stage 4 - Frontier (M1)

19. [[Digital Sequence Information]] (M1): follow the debate on benefit-sharing for sequence data in public databases under the Convention on Biological Diversity.
20. [[Indigenous Data Sovereignty]] (M1): apply the CARE principles next to FAIR when data concern Indigenous peoples.[^care]

> [!tip]
> Study items 11 to 13 with a real case: reproduce, on paper, why a GWAS summary table can reveal membership of an individual.

## Uses from other domains

- [[General Data Protection Regulation]] and [[Health Insurance Portability and Accountability Act]] ([[Regulation and Standards]]): the legal frame of genomic privacy.
- [[Controlled-Access Data]] and [[FAIR Principles]] ([[Research Data Management]]): the technical side of responsible sharing.
- [[Secondary Finding]] and [[Genetic Counseling]] ([[Clinical Genomics]]): ethics in the clinic.
- [[Publication Bias]] and [[Questionable Research Practice]] ([[Reproducibility]]): the grey zone below misconduct.
- [[CRISPR-Cas9]] ([[Biotechnology]]): a technology whose uses raise dual-use and germline questions.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[Carnegie Mellon University - BS Computational Biology]] | Carnegie Mellon University | L2, L3 | 02-135 Ethics in the Practice of Computational Biology (3 units), required[^cmu] |
| [[Coursera Stanford - Writing in the Sciences]] | Stanford University | L2 | Publication module: ethical issues in publishing, plagiarism, authorship (items 2 to 4)[^sciwrite] |

## Reference books

- [[On Being a Scientist (National Academies)]]: responsible conduct of research, from data handling to authorship and misconduct (items 1 to 5).[^obas]

## Lab projects

- [[06-mutation-lab]]: states that it is not a clinical prediction; honest communication of a tool's limits is an ethical requirement.
- [[10-genomic-pipeline]]: run it on openly consented public data and record the dataset's terms of use.

## References

[^cmu]: [[Carnegie Mellon University - BS Computational Biology]], computational biology core.
[^obas]: [[On Being a Scientist (National Academies)]].
[^sciwrite]: [[Coursera Stanford - Writing in the Sciences]], publication module.
[^homer]: [[Homer 2008 - Resolving Individuals Contributing Trace Amounts of DNA to Highly Complex Mixtures]], *PLOS Genetics*.
[^gymrek]: [[Gymrek 2013 - Identifying Personal Genomes by Surname Inference]], *Science*.
[^popejoy]: [[Popejoy 2016 - Genomics Is Failing on Diversity]], *Nature*.
[^care]: [[Carroll 2020 - The CARE Principles for Indigenous Data Governance]], *Data Science Journal*.
