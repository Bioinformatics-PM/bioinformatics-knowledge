---
aliases:
  - Design of Experiments
  - Plan d'expérience
tags:
  - type/moc
  - domain/scientific-practice
  - domain/statistics
  - domain/bioinformatics
  - level/L2
  - level/L3
prerequisites:
  - "[[Scientific Method]]"
  - "[[Descriptive Statistics]]"
  - "[[Statistical Inference]]"
projects:
  - "[[05-sequence-search]]"
  - "[[07-evolution-simulator]]"
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Experimental Design for Laboratory Biologists (Lazic)]]"
  - "[[Hurlbert 1984 - Pseudoreplication and the Design of Ecological Field Experiments]]"
  - "[[Leek 2010 - Tackling the Widespread and Critical Impact of Batch Effects]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
---

# Experimental Design

> [!abstract]
> Planning a study so that its data can answer the question: what the unit of replication is, how treatments are allocated, what must be controlled, how many samples are needed, and how technical structure (batches, lanes, runs) is kept from masquerading as biology.

## Why it matters for bioinformatics

No analysis can rescue a confounded design: if all cases were sequenced in one batch and all controls in another, the difference is uninterpretable. Bioinformaticians are asked to analyze data after the fact, so they must detect design flaws, and increasingly they are asked to plan sequencing studies (replicates versus depth, multiplexing, randomization of processing order).[^msmb][^leek]

## Before you start

- [[Scientific Method]]: [[Hypothesis]], [[Controlled Experiment]], [[Causality]], [[Measurement Error]].
- [[Descriptive Statistics]] and [[Statistical Inference]]: [[Hypothesis Testing]], [[P-Value]], [[Confidence Interval]], [[Statistical Power]].

## Learning path

### Stage 2 - Core (L2)

1. [[Observational Study]] (L2): tell an observational study (cohort, case-control, cross-sectional) from an experiment and say what each can conclude.[^openstax]
2. [[Experimental Unit]] (L2): identify the entity that is independently assigned to a treatment, which defines the true sample size.[^lazic]
3. [[Experimental Control]] (L2): choose positive, negative, vehicle and spike-in controls and say what each rules out.
4. [[Biological Replicate]] (L2): replicate independent biological samples to measure the variability the conclusion generalizes over.
5. [[Technical Replicate]] (L2): replicate measurements of one sample to measure assay noise, and explain why they do not increase n.
6. [[Pseudoreplication]] (L2): detect analyses that treat non-independent measurements as replicates and inflate significance.[^hurlbert]
7. [[Confounding]] (L2): recognize a variable associated with both treatment and outcome, and remove it by design rather than by hope.
8. [[Selection Bias]] (L2): see how the way samples are recruited or filtered distorts the population studied.
9. [[Randomization]] (L2): allocate treatments and processing order at random to break hidden confounding.
10. [[Blinding]] (L2): hide group labels from experimenters and analysts to prevent conscious and unconscious bias.
11. [[Randomized Block Design]] (L2): block on known nuisance factors (day, operator, flow cell) and randomize within blocks.
12. [[Paired Design]] (L2): pair measurements on the same unit (before and after, tumor and matched normal) to remove between-unit variability.
13. [[Pilot Study]] (L2): run a small study first to test the protocol and estimate the variance needed to plan the main one.

### Stage 3 - Advanced (L3)

14. [[Factorial Design]] (L3): study several factors at once and estimate their interactions with the matching linear model.
15. [[Batch Effect]] (L3): diagnose technical variation from processing batches, prevent it by design, and know the limits of correction.[^leek]
16. [[Sequencing Experiment Design]] (L3): trade sequencing depth against replicates, balance samples across lanes and multiplex without confounding.[^msmb]
17. [[Randomized Controlled Trial]] (L3): read the design of a clinical trial (allocation concealment, blinding, endpoints, intention to treat).

> [!tip]
> Learn items 2 to 7 as one block: most design errors in published omics studies are an experimental unit or confounding problem in disguise.

## Uses from other domains

- [[Statistical Power]], [[Effect Size]], [[Multiple Testing Correction]] ([[Statistical Inference]]): choosing the number of replicates before collecting data, including in omics.
- [[Analysis of Variance]], [[Linear Regression]], [[Generalized Linear Model]] ([[Linear Models]]): the model that matches each design, with block and batch terms.
- [[Principal Component Analysis]] ([[Multivariate Analysis]]): the first diagnostic of batch effects.
- [[Cross-Validation]] and [[Overfitting]] ([[Statistical Learning]]): honest evaluation of predictive models.
- [[Batch Effect Correction]] ([[Transcriptomics]]): what to do when batches could not be avoided.
- [[Bioinformatics Tool Benchmarking]] and [[Benchmark Dataset]] ([[Bioinformatics Engineering]]): experimental design applied to comparing computational methods.
- [[Random Number Generation]] ([[Scientific Computing]]): randomization lists and simulated ground truth.
- [[Next-Generation Sequencing]], [[Sequencing Coverage]], [[Genome-Wide Association Study]], [[Population Structure]]: designs specific to genomics, where ancestry is the classic confounder.
- [[Preregistration]] ([[Reproducibility]]): fixing the design and analysis plan before data collection.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[HarvardX PH525x - Data Analysis for the Life Sciences]] | Harvard University | L2, L3 | Linear models, inference and modeling for high-throughput experiments, high-dimensional data analysis: the analysis side of items 11 to 16[^ph525] |

## Reference books

- [[Experimental Design for Laboratory Biologists (Lazic)]]: experimental units, pseudoreplication, randomization and blocking for lab biology (items 2 to 13).[^lazic]
- [[Modern Statistics for Modern Biology (Holmes)]]: the chapter on the design of high-throughput experiments (items 15, 16).[^msmb]
- [[Introductory Statistics (OpenStax)]]: ch. 1 for items 1 and 8.[^openstax]

## Lab projects

- [[05-sequence-search]]: benchmark search strategies on data with known answers, a small [[Bioinformatics Tool Benchmarking]] with controls and replicates.
- [[07-evolution-simulator]]: replicate simulations with independent seeds and explore parameters with a [[Factorial Design]].

## References

[^openstax]: [[Introductory Statistics (OpenStax)]], ch. 1 "Sampling and Data".
[^lazic]: [[Experimental Design for Laboratory Biologists (Lazic)]].
[^msmb]: [[Modern Statistics for Modern Biology (Holmes)]], chapter on the design of high-throughput experiments.
[^hurlbert]: [[Hurlbert 1984 - Pseudoreplication and the Design of Ecological Field Experiments]], *Ecological Monographs*: the paper that named pseudoreplication.
[^leek]: [[Leek 2010 - Tackling the Widespread and Critical Impact of Batch Effects]], *Nature Reviews Genetics*.
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.2x to 4x.
