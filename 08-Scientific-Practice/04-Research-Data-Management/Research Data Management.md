---
aliases:
  - RDM
  - Data Stewardship
  - Gestion des données de recherche
tags:
  - type/moc
  - domain/scientific-practice
  - domain/bioinformatics
  - level/L2
  - level/L3
prerequisites:
  - "[[Bioinformatics Foundations]]"
  - "[[Experimental Design]]"
  - "[[Databases]]"
projects:
  - "[[10-genomic-pipeline]]"
  - "[[Bioinformatics Lab]]"
sources:
  - "[[ELIXIR RDMkit]]"
  - "[[Wilkinson 2016 - The FAIR Guiding Principles for Scientific Data Management and Stewardship]]"
  - "[[Brazma 2001 - Minimum Information About a Microarray Experiment]]"
  - "[[Galaxy Training Network - Training Material]]"
  - "[[European Nucleotide Archive]]"
  - "[[NCBI GenBank]]"
---

# Research Data Management

> [!abstract]
> Everything that happens to research data from planning to reuse: organizing, documenting with metadata, protecting, depositing in the right repository with the right license, and making it findable and reusable by people and machines (FAIR).

## Why it matters for bioinformatics

Bioinformatics runs on other people's data. Public archives such as GEO, SRA and ENA only work because submitters provide standardized metadata, stable identifiers and clear terms of reuse. Funders and journals now require data management plans and deposition in public repositories, and a bioinformatician is often the person in the lab who does it.[^rdmkit][^fair]

## Before you start

- [[Bioinformatics Foundations]]: [[Biological Database]], [[Accession Number]], [[FASTQ Format]], [[Biological Ontology]].
- [[Experimental Design]]: the design is the core of the metadata ([[Biological Replicate]], [[Batch Effect]]).
- [[Databases]]: tables, keys and schemas.

## Learning path

### Stage 2 - Core (L2)

1. [[Research Data Life Cycle]] (L2): name the stages (plan, collect, process, analyze, preserve, share, reuse) and what is decided at each.[^rdmkit]
2. [[Data Management Plan]] (L2): write a funder-style plan covering data types, volumes, formats, storage, sharing and costs.
3. [[Computational Project Organization]] (L2): lay out a project so raw data, code, results and notes are separated and dated.
4. [[Electronic Lab Notebook]] (L2): record what was done, when and why, in a form that others can audit.
5. [[Data Integrity]] (L2): keep raw data read-only and verify files with checksums; later, the ALCOA+ principles of regulated work.
6. [[Data Backup]] (L2): apply the 3-2-1 rule and know the difference between a backup, a sync and an archive.
7. [[Metadata]] (L2): describe data (who, what, how, when) with descriptive, structural and administrative metadata and controlled vocabularies.
8. [[Persistent Identifier]] (L2): use DOIs, ORCID iDs and database accessions so that data, software and people stay citable.
9. [[FAIR Principles]] (L2): apply the fifteen guiding principles that make data Findable, Accessible, Interoperable and Reusable.[^fair]
10. [[Data Repository]] (L2): choose between domain archives (GEO, SRA, ENA, PRIDE, PDB) and generalist repositories (Zenodo) for each data type.

### Stage 3 - Advanced (L3)

11. [[Minimum Information Standard]] (L3): explain the "minimum information" family (MIBBI) and what each checklist guarantees about reuse.
12. [[Minimum Information About a Microarray Experiment]] (L3): list the MIAME elements, the early reporting standard that became the model for functional genomics.[^miame]
13. [[Minimum Information About a Next-Generation Sequencing Experiment]] (L3): apply MINSEQE, the sequencing counterpart of MIAME, to an RNA-seq submission.
14. [[Data Submission]] (L3): submit raw reads and processed data to SRA or ENA and GEO with sample metadata, and cite the accessions in a paper.
15. [[Controlled-Access Data]] (L3): explain why human genomic data sit in controlled-access archives (dbGaP, EGA) and how data access committees work.
16. [[Data License]] (L3): choose between CC0, CC BY and database licenses, and read the reuse terms of a dataset before using it.
17. [[Software License]] (L3): choose between permissive (MIT, BSD, Apache) and copyleft (GPL) licenses, check compatibility with dependencies, and know what no license means.
18. [[Data Preservation]] (L3): plan retention periods, open archival formats and the difference between storage and long-term preservation.
19. [[Laboratory Information Management System]] (L3): explain how a LIMS tracks samples, runs and results, and where it meets the analysis pipeline.

## Uses from other domains

- [[Biological Database]], [[Accession Number]], [[Biological Ontology]] ([[Bioinformatics Foundations]]): the archive side of submission and reuse.
- [[Microarray]] and [[Next-Generation Sequencing]] ([[Biotechnology]]): the technologies MIAME and MINSEQE describe.
- [[Tidy Data]] ([[Descriptive Statistics]]): one observation per row and one variable per column, the shape of well-organized tables.
- [[Version Control]] and [[Research Software]] ([[Software Engineering]]): versioning and maintaining the code that goes with the data.
- [[Data Provenance]] ([[Reproducibility]]): the link from data to results.
- [[Informed Consent]] and [[Genomic Data Privacy]] ([[Research Ethics]]), [[General Data Protection Regulation]] ([[Regulation and Standards]]): legal and ethical limits on sharing human data.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[ELIXIR RDMkit]] | ELIXIR | L2, L3 | Data life cycle stages, tools and national guidance for life-science data[^rdmkit] |
| [[Galaxy Training Network - Training Material]] | Galaxy Training Network | L2, L3 | Using Galaxy and managing your data: histories, datasets, workflows[^gtn] |

## Reference books

No textbook needed: the RDMkit, the FAIR paper and the archives' own documentation cover the syllabus.

- [[European Nucleotide Archive]]: metadata of studies and samples, and submission services (items 7, 10, 14).[^ena]
- [[NCBI GenBank]]: the Submission Portal with BioProject and BioSample records, and daily exchange with ENA and DDBJ (items 8, 14).[^genbank]

## Lab projects

- [[10-genomic-pipeline]]: download public data by accession, keep raw data read-only with checksums, and record metadata and provenance.
- [[Bioinformatics Lab]]: every repository has a LICENSE and a README, the minimum of [[Software License]] and [[Metadata]] practice.

## References

[^rdmkit]: [[ELIXIR RDMkit]].
[^fair]: [[Wilkinson 2016 - The FAIR Guiding Principles for Scientific Data Management and Stewardship]], *Scientific Data*.
[^miame]: [[Brazma 2001 - Minimum Information About a Microarray Experiment]], *Nature Genetics*.
[^gtn]: [[Galaxy Training Network - Training Material]], topic "Using Galaxy and Managing your Data".
[^ena]: [[European Nucleotide Archive]].
[^genbank]: [[NCBI GenBank]], submission.
