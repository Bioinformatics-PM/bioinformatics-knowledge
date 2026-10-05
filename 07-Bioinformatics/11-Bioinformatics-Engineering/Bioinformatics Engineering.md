---
aliases:
  - Bioinformatics Pipelines
  - Workflow Engineering
tags:
  - type/moc
  - domain/bioinformatics
  - domain/computer-science
  - domain/scientific-practice
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Computer Systems]]"
  - "[[Software Engineering]]"
  - "[[NGS Data Analysis]]"
  - "[[Reproducibility]]"
  - "[[Research Data Management]]"
projects:
  - "[[10-genomic-pipeline]]"
  - "[[05-sequence-search]]"
  - "[[Bioinformatics Lab]]"
sources:
  - "[[Galaxy Training Network - Training Material]]"
  - "[[MIT - The Missing Semester of Your CS Education]]"
  - "[[Coursera JHU - Genomic Data Science Specialization]]"
  - "[[Galaxy]]"
  - "[[Shanghai Jiao Tong University - BS Bioinformatics]]"
  - "[[ISCB - Bioinformatics Core Competencies]]"
---

# Bioinformatics Engineering

> [!abstract]
> Turning analyses into reliable, reproducible and scalable software: pipelines and workflow managers (Snakemake, Nextflow), containers, reference data, testing, provenance, FAIR workflows and the benchmarking of bioinformatics tools.

## Why it matters for bioinformatics

A result that cannot be rerun is not a result. Real analyses chain dozens of tools over terabytes of data on clusters and clouds; without workflow managers, pinned environments and provenance, they cannot be reproduced, reviewed or scaled. Choosing a tool is itself an empirical question, answered by benchmarking against ground truth. Handling big biological data is a named course of bioinformatics majors,[^sjtu] and genomic data science programs teach command-line tools and workflow platforms as courses of their own.[^jhu]

## Before you start

- [[Computer Systems]]: [[Unix Shell]], [[Shell Script]], [[Container]], [[Parallel Computing]], [[High-Performance Computing]], [[Job Scheduler]].
- [[Software Engineering]]: [[Version Control]], [[Python Packaging]], [[Dependency Management]], [[Unit Testing]], [[Continuous Integration]], [[Benchmarking]], [[Research Software]].
- [[Programming]]: [[Python Programming]], [[Command-Line Interface]], [[Computational Notebook]].
- [[Reproducibility]]: [[Computational Reproducibility]], [[Data Provenance]], [[Research Compendium]].
- [[Research Data Management]]: [[FAIR Principles]], [[Metadata]], [[Persistent Identifier]], [[Data Repository]].
- [[Experimental Design]]: [[Experimental Control]], [[Confounding]]: the design principles behind items 15 and 16; [[Statistical Learning]]: [[Precision and Recall]], [[Receiver Operating Characteristic Curve]] for accuracy metrics.
- [[Discrete Mathematics]]: [[Directed Acyclic Graph]]; [[Algorithms]]: [[Topological Sort]].
- [[NGS Data Analysis]]: the steps a genomic pipeline chains ([[Read Quality Control]], [[Read Mapping]], [[Variant Calling]]).

## Learning path

### Stage 2 - Core (L2)

1. [[Bioinformatics Pipeline]] (L2): decompose an analysis into steps with explicit inputs, outputs, parameters and tool versions.
2. [[Software Environment Management]] (L2): pin tool versions per project with conda and Bioconda environments and lock files, and rebuild them anywhere.
3. [[Graphical Workflow Platform]] (L2): build, run and share a workflow in [[Galaxy]] without code, and know what it trades away.
4. [[Workflow Management System]] (L2): let an engine build the task graph (a DAG), rerun only what changed and recover from failures.
5. [[Snakemake Workflow]] (L2): write rules with wildcards, inputs and outputs, and run them locally and on a cluster.
6. [[Pipeline Configuration]] (L2): separate sample sheets, parameters and reference paths from code so one pipeline serves many projects.

### Stage 3 - Advanced (L3)

7. [[Nextflow Workflow]] (L3): write processes connected by channels (dataflow model) and reuse community pipelines (nf-core).
8. [[Pipeline Containerization]] (L3): run each step in a Docker or Apptainer image (BioContainers) so the pipeline behaves the same everywhere.
9. [[Scatter-Gather Parallelism]] (L3): split work by sample, chromosome or chunk and merge results on a cluster scheduler.
10. [[Reference Data Management]] (L3): version genomes, indexes and annotation bundles so every run names exactly which reference it used.
11. [[Pipeline Testing]] (L3): test a workflow with small test data, expected outputs and continuous integration.
12. [[Workflow Reporting]] (L3): aggregate QC and run statistics into a report (MultiQC-style) that a reviewer can check.
13. [[Workflow Provenance]] (L3): record which data, code, versions and parameters produced each output (Workflow Run RO-Crate).
14. [[FAIR Workflow]] (L3): make a workflow findable, accessible, interoperable and reusable (registries, licenses, metadata).
15. [[Bioinformatics Tool Benchmarking]] (L3): compare tools fairly on accuracy, runtime and memory with a neutral design, run as a rerunnable workflow of tools, datasets and metrics.
16. [[Benchmark Dataset]] (L3): build or choose ground truth (simulated reads, reference truth sets, spike-ins) and know the bias of each.

### Stage 4 - Frontier (M1)

17. [[Common Workflow Language]] (M1): describe tools and workflows in a portable standard (CWL, and its relative WDL).
18. [[Cloud Workflow Execution]] (M1): run workflows on cloud or Kubernetes executors and manage cost, storage and data transfer.

> [!tip]
> Learn one engine well (Snakemake or Nextflow) on [[10-genomic-pipeline]] before comparing them. Items 15 and 16 apply to every Lab project: each one has a `benchmarks/` folder.

## Uses from other domains

- [[Property-Based Testing]] (from [[Software Engineering]]): testing parsers and algorithms against invariants.
- [[Cloud Computing]] (from [[Computer Systems]]): where item 17 runs.
- [[Out-of-Core Computation]] and [[Performance Profiling]] (from [[Scientific Computing]]): processing files larger than memory and sizing jobs.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[Galaxy Training Network - Training Material]] | Galaxy Project | L2-L3 | "FAIR Data, Workflows, and Research" tutorials "FAIR in a nutshell", "RO-Crate - Introduction", "Workflow Run RO-Crate Introduction" (items 13 and 14)[^gtn] |
| [[Coursera JHU - Genomic Data Science Specialization]] | Johns Hopkins | L2 | "Genomic Data Science with Galaxy" and "Command Line Tools for Genomic Data Science"[^jhu] |
| [[MIT - The Missing Semester of Your CS Education]] | MIT | L1-L2 | Shell, version control and Git, packaging and shipping code: the toolbox this syllabus assumes[^missing] |
| Biological Big Data Analysis, in [[Shanghai Jiao Tong University - BS Bioinformatics]] | SJTU | L3 | Named bioinformatics core course[^sjtu] |

## Reference books

No single textbook covers this syllabus. The primary references are the documentation and landmark papers of each workflow tool (Snakemake, Nextflow, CWL, Bioconda, BioContainers), which are planned source notes.

## Lab projects

- [[10-genomic-pipeline]]: workflow manager, containers, reference data, provenance and reporting on real data.
- [[05-sequence-search]]: benchmarking of search strategies from 100 to 1M sequences.
- [[Bioinformatics Lab]]: testing, CI and `benchmarks/` in every repository.

## References

Provenance and FAIR items follow the Galaxy "FAIR Data, Workflows, and Research" training topic;[^gtn] the prerequisite toolbox follows the Missing Semester;[^missing] the ISCB competency framework is the outcome check for this syllabus.[^iscb]

[^gtn]: [[Galaxy Training Network - Training Material]], topic "FAIR Data, Workflows, and Research" (tutorial titles as listed in the table).
[^jhu]: [[Coursera JHU - Genomic Data Science Specialization]], courses "Genomic Data Science with Galaxy" and "Command Line Tools for Genomic Data Science".
[^missing]: [[MIT - The Missing Semester of Your CS Education]], lectures on the shell, version control and Git, and packaging and shipping code.
[^sjtu]: [[Shanghai Jiao Tong University - BS Bioinformatics]]: Biological Big Data Analysis is in the bioinformatics core.
[^iscb]: [[ISCB - Bioinformatics Core Competencies]].
