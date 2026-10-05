---
aliases:
  - Méthode scientifique
tags:
  - type/moc
  - domain/scientific-practice
  - level/L1
  - level/L2
  - level/L3
prerequisites: []
projects:
  - "[[07-evolution-simulator]]"
  - "[[05-sequence-search]]"
sources:
  - "[[Stanford University - BS Biomedical Computation]]"
  - "[[Shanghai Jiao Tong University - BS Bioinformatics]]"
  - "[[Université Paris-Saclay - Licence Double Diplôme Informatique Sciences de la Vie]]"
  - "[[The Logic of Scientific Discovery (Popper)]]"
  - "[[Platt 1964 - Strong Inference]]"
---

# Scientific Method

> [!abstract]
> How a question becomes knowledge: observation, hypothesis, deduced prediction, controlled test and revision, and the reasoning rules that separate a supported claim from an opinion.

## Why it matters for bioinformatics

Omics data make it easy to find patterns and hard to know which ones are real. A bioinformatician must turn a pattern into a falsifiable hypothesis, design the computational or wet-lab test that could refute it, and say how strong the evidence is. Degree programs teach this through research requirements and practical projects rather than a lecture course.[^stanford][^sjtu][^psisv]

## Before you start

No prerequisite: this is a Stage 1 subject. Read it alongside [[Probability]] (Stage 1) and [[Descriptive Statistics]].

## Learning path

### Stage 1 - Foundations (L1)

1. [[Empirical Evidence]] (L1): tell observation, data, evidence and opinion apart, and say what makes a claim empirical.
2. [[Inductive Reasoning]] (L1): generalize from observations and explain why induction never proves a general claim.
3. [[Deductive Reasoning]] (L1): derive testable consequences from premises and check whether an argument is valid.
4. [[Hypothesis]] (L1): state a testable hypothesis with an explicit prediction, distinct from the null hypothesis of a statistical test.
5. [[Falsifiability]] (L1): apply Popper's criterion to decide whether a claim can be tested, and spot claims that cannot fail.
6. [[Controlled Experiment]] (L1): change one factor, hold the others constant and compare with a control to support a causal claim.
7. [[Measurement Error]] (L1): distinguish random from systematic error, and accuracy from precision.
8. [[Confirmation Bias]] (L1): recognize how expectations bias observation and interpretation, and name countermeasures such as blinding.
9. [[Scientific Theory]] (L1): distinguish hypothesis, law and theory, and explain why evolution or cell theory are theories in the strong sense.

### Stage 2 - Core (L2)

10. [[Hypothetico-Deductive Method]] (L2): run the full cycle of hypothesis, deduced prediction, test and revision on a biological question.
11. [[Abductive Reasoning]] (L2): infer the best explanation among competing hypotheses, as in diagnosis or gene function prediction.
12. [[Occam's Razor]] (L2): prefer the simplest adequate explanation and relate the principle to parsimony and model selection.
13. [[Causality]] (L2): separate correlation from causation with counterfactual reasoning and the Bradford Hill criteria.
14. [[Hierarchy of Evidence]] (L2): rank anecdotes, observational studies, randomized trials and meta-analyses by strength of evidence.
15. [[Scientific Model]] (L2): treat a model as a deliberate simplification judged by its predictions, not by its realism.
16. [[In Silico Experiment]] (L2): design a computational experiment with a stated hypothesis, controls and a known ground truth.

### Stage 3 - Advanced (L3)

17. [[Strong Inference]] (L3): apply Platt's method of multiple competing hypotheses and crucial experiments that exclude some of them.[^platt]
18. [[Paradigm Shift]] (L3): explain Kuhn's normal science, anomalies and revolutions, and judge when the term is deserved.
19. [[Data-Driven Research]] (L3): contrast hypothesis-driven and data-driven (omics) research, and treat exploratory findings as hypotheses to confirm.

> [!tip]
> Items 1 to 9 take a few hours in Stage 1. Come back to items 10 to 16 when [[Statistical Inference]] starts, and to 17 to 19 when you first read research papers.

## Uses from other domains

- [[Hypothesis Testing]], [[P-Value]] and [[Conditional Probability]] ([[Probability and Statistics]]): the statistical form of testing a hypothesis.
- [[Bayes' Theorem]]: updating belief in a hypothesis from evidence.
- [[Random Number Generation]] ([[Scientific Computing]]): controlled, repeatable in silico experiments.
- [[Experimental Design]] and [[Reproducibility]]: where controls, replication and bias become operational.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[Stanford University - BS Biomedical Computation]] | Stanford University | L3 | Six units of directed research with a faculty member[^stanford] |
| [[Shanghai Jiao Tong University - BS Bioinformatics]] | Shanghai Jiao Tong University | L2, L3 | Comprehensive bioinformatics experiments, practice and a final-year project[^sjtu] |
| [[Université Paris-Saclay - Licence Double Diplôme Informatique Sciences de la Vie]] | Université Paris-Saclay | L1 to L3 | Research-based complementary block each year[^psisv] |

## Reference books

- [[The Logic of Scientific Discovery (Popper)]]: falsifiability as the criterion of empirical science (items 4, 5, 10).[^popper]

## Lab projects

- [[07-evolution-simulator]]: every run is an [[In Silico Experiment]]; vary one parameter at a time with fixed seeds, as in a [[Controlled Experiment]].
- [[05-sequence-search]]: state a hypothesis about speed and accuracy before benchmarking, then test it.

## References

[^stanford]: [[Stanford University - BS Biomedical Computation]], research requirement.
[^sjtu]: [[Shanghai Jiao Tong University - BS Bioinformatics]], practice block and undergraduate project.
[^psisv]: [[Université Paris-Saclay - Licence Double Diplôme Informatique Sciences de la Vie]], complementary block.
[^popper]: [[The Logic of Scientific Discovery (Popper)]].
[^platt]: [[Platt 1964 - Strong Inference]], *Science*.
