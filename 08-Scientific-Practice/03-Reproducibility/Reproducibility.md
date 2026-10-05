---
aliases:
  - Reproducible Research
  - Reproductibilité
tags:
  - type/moc
  - domain/scientific-practice
  - domain/computer-science
  - domain/bioinformatics
  - level/L2
  - level/L3
prerequisites:
  - "[[Scientific Method]]"
  - "[[Experimental Design]]"
  - "[[Scientific Literature]]"
  - "[[Statistical Inference]]"
  - "[[Software Engineering]]"
projects:
  - "[[10-genomic-pipeline]]"
  - "[[07-evolution-simulator]]"
  - "[[Bioinformatics Lab]]"
sources:
  - "[[Reproducibility and Replicability in Science (National Academies)]]"
  - "[[Ioannidis 2005 - Why Most Published Research Findings Are False]]"
  - "[[Sandve 2013 - Ten Simple Rules for Reproducible Computational Research]]"
  - "[[The Turing Way]]"
  - "[[MIT - The Missing Semester of Your CS Education]]"
  - "[[Galaxy Training Network - Training Material]]"
---

# Reproducibility

> [!abstract]
> A result is reproducible when the same data and the same code give the same result; it is replicable when new data collected to answer the same question support the same conclusion. This note is both the concept and the syllabus of how to achieve it.

## Why it matters for bioinformatics

A bioinformatics result is the output of data, code, parameters, software versions and reference files. Change any one silently and the result changes. Beyond the computation, the literature itself has a replication problem: selective reporting and underpowered studies make many published findings less reliable than their p-values suggest.[^ioannidis] The fix is partly statistical and partly engineering, which is why this subdomain links [[Statistical Inference]] and [[Software Engineering]].[^sandve]

## Before you start

- [[Scientific Method]] and [[Experimental Design]]: [[Hypothesis]], [[Biological Replicate]], [[Confounding]], [[Batch Effect]].
- [[Scientific Literature]]: [[Peer Review]], [[Preprint]].
- [[Statistical Inference]]: [[P-Value]], [[Statistical Power]], [[Multiple Testing Correction]], [[False Discovery Rate]].
- [[Software Engineering]]: [[Version Control]], [[Unit Testing]].

## Learning path

### Stage 2 - Core (L2)

1. [[Replicability]] (L2): distinguish reproducibility, replicability, robustness and generalizability, and say which one a given study tested.[^nasem]
2. [[Reproducibility Crisis]] (L2): summarize the evidence of low replication rates and Ioannidis's argument from low power, low prior probability and bias.[^ioannidis]
3. [[Publication Bias]] (L2): explain how the file-drawer effect distorts the literature and inflates published effect sizes.
4. [[P-Hacking]] (L2): recognize analysis choices made until p < 0.05, and their effect on the false positive rate.
5. [[Questionable Research Practice]] (L2): name HARKing, selective reporting, optional stopping and outcome switching, and why they are not misconduct but still harmful.
6. [[Open Science]] (L2): explain open data, open code, open access and open peer review as reproducibility tools.
7. [[Computational Reproducibility]] (L2): apply the rules that make an analysis rerunnable: scripted steps, no manual edits, recorded versions and seeds.[^sandve]

### Stage 3 - Advanced (L3)

8. [[Data Provenance]] (L3): record which inputs, code, parameters and versions produced each result, down to the file checksum.
9. [[Analytical Flexibility]] (L3): measure how pipeline choices change conclusions (garden of forking paths, multiverse analysis).
10. [[Preregistration]] (L3): fix hypotheses and analysis plans before seeing the data, including registered reports.
11. [[Reporting Guideline]] (L3): use EQUATOR-network checklists (ARRIVE, CONSORT, STROBE) and journal reporting summaries to report what others need to reproduce.
12. [[Research Compendium]] (L3): package the data, code, environment and narrative of one study so that others can rerun it, and archive it with a DOI.

> [!tip]
> Items 7, 8 and 12 are learned by doing: make [[10-genomic-pipeline]] rerun from a clean clone with one command before reading more about them.

## Uses from other domains

- [[Version Control]], [[Unit Testing]], [[Continuous Integration]], [[Dependency Management]], [[Research Software]] ([[Software Engineering]]): the everyday tools of computational reproducibility, and code treated as a research output.
- [[Computational Notebook]] ([[Programming]]): exploration without hidden state.
- [[Container]] ([[Computer Systems]]): a frozen software environment.
- [[Workflow Management System]], [[Software Environment Management]], [[Workflow Provenance]], [[FAIR Workflow]] ([[Bioinformatics Engineering]]): the same principles applied to pipelines.
- [[Random Number Generation]] and [[Floating-Point Arithmetic]] ([[Scientific Computing]]): seeds, and why bitwise identity is not always possible.
- [[Metadata]], [[FAIR Principles]], [[Data Integrity]], [[Persistent Identifier]], [[Software License]] ([[Research Data Management]]): the data side of reproducibility.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[The Turing Way]] | The Alan Turing Institute (community handbook) | L2, L3 | Guide for reproducible research: version control, environments, testing, workflows[^turing] |
| [[MIT - The Missing Semester of Your CS Education]] | MIT | L1, L2 | Shell, Git, and packaging and shipping code (item 7)[^missing] |
| [[Galaxy Training Network - Training Material]] | Galaxy Training Network | L2, L3 | Using Galaxy and managing your data: histories and workflows as recorded, rerunnable analyses[^gtn] |

## Reference books

- [[Reproducibility and Replicability in Science (National Academies)]]: definitions of reproducibility and replicability and the state of the evidence (items 1, 2).[^nasem]

## Lab projects

- [[10-genomic-pipeline]]: the capstone of this subdomain; provenance, containers and a pipeline that reruns end to end.
- [[07-evolution-simulator]]: reproducible random seeds; the same seed must give the same trajectory.
- [[Bioinformatics Lab]]: tests from day one, CI and a standard repository layout in every project.

## References

[^nasem]: [[Reproducibility and Replicability in Science (National Academies)]].
[^ioannidis]: [[Ioannidis 2005 - Why Most Published Research Findings Are False]], *PLOS Medicine*.
[^sandve]: [[Sandve 2013 - Ten Simple Rules for Reproducible Computational Research]], *PLOS Computational Biology*.
[^turing]: [[The Turing Way]].
[^missing]: [[MIT - The Missing Semester of Your CS Education]], lectures on version control and on packaging and shipping code.
[^gtn]: [[Galaxy Training Network - Training Material]], topic "Using Galaxy and Managing your Data".
