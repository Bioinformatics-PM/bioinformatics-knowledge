---
aliases:
  - Deduction
  - Logical Validity
  - Modus Tollens
  - Raisonnement déductif
tags:
  - type/concept
  - domain/scientific-practice
  - domain/mathematics
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Propositional Logic]]"
related:
  - "[[Inductive Reasoning]]"
  - "[[Hypothesis]]"
  - "[[Falsifiability]]"
  - "[[Hypothetico-Deductive Method]]"
projects: []
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[The Logic of Scientific Discovery (Popper)]]"
  - "[[Meselson 1958 - The Replication of DNA in Escherichia coli]]"
---

# Deductive Reasoning

> [!abstract]
> Deductive reasoning derives what must be true if the premises are true: it is how a hypothesis is turned into a precise, testable prediction, and how a failed prediction counts against it.

## Definition

**Deductive reasoning** draws conclusions that follow necessarily from premises; in science it uses a general principle to forecast specific results.[^os1] An argument is **valid** when no assignment of truth values makes all its premises true and its conclusion false; logic texts call such an inference rule sound.[^lehman] An argument is **sound**, in the usual philosophical sense, when it is valid *and* its premises are true. Validity concerns form, not content.

## Why it matters

- **Tests start with a deduction.** "If this gene is essential, a clean knockout will not grow" is a deduced prediction; a vague deduction gives a vague test ([[Hypothesis]]).
- **Reading papers and code.** "The model predicts X; we observe X; so the model is right" is the most common invalid argument in results sections (affirming the consequent, below); a unit test, in turn, checks a consequence deduced by hand.

## Core (L1)

### Valid and invalid forms

With $H$ a hypothesis and $P$ a prediction deduced from it ("if $H$ then $P$"):

| Form | Premises | Conclusion | Valid? |
|---|---|---|---|
| Modus ponens | $H \to P$, $H$ | $P$ | yes |
| Modus tollens | $H \to P$, $\neg P$ | $\neg H$ | yes |
| Affirming the consequent | $H \to P$, $P$ | $H$ | **no** |
| Denying the antecedent | $H \to P$, $\neg H$ | $\neg P$ | **no** |

Modus tollens is the logic of refutation; affirming the consequent is why a confirmed prediction does not prove a hypothesis: another hypothesis may predict the same thing ([[Falsifiability]]).[^popper]

### Deducing predictions: Meselson and Stahl (1958)

Premises: *E. coli* DNA is first fully labelled with heavy nitrogen (¹⁵N); the cells are then grown in ¹⁴N, so new strands are light; DNA density in a cesium chloride gradient reflects its ¹⁵N content.[^meselson] Add one replication model and the band pattern of each generation follows by deduction:

![[meselson-stahl-model-predictions.svg]]

The observed results were one hybrid band after one generation, hybrid and light bands after two.[^meselson] Two applications of modus tollens follow:

1. If replication were conservative, generation 1 would show heavy and light bands. It showed one hybrid band. So it is not conservative.
2. If replication were dispersive, generation 2 would show a single band between hybrid and light. It showed hybrid and light bands. So it is not dispersive.

Generation 1 alone would not do: "if semiconservative, then one hybrid band; one hybrid band; so semiconservative" affirms the consequent, because the dispersive model predicts the same band. The second generation is where the two surviving models differ. The experiment itself is told in [[DNA Replication]].

## Deeper (L2)

### Auxiliary assumptions

A prediction rarely follows from $H$ alone: it needs auxiliary assumptions $A$ (density reflects ¹⁵N content, the gradient resolves the bands, the DNA was not broken or contaminated). The valid conclusion of a failed prediction is then

$$\big((H \land A) \to P\big),\ \neg P \ \vDash\ \neg(H \land A) \equiv \neg H \lor \neg A,$$

"the hypothesis or an auxiliary assumption is false". Popper discussed how auxiliary hypotheses can be used to protect a theory from refutation, and required that they be testable themselves.[^popper] Controls exist largely to test auxiliaries ([[Controlled Experiment]]).

## Mathematical representation

An argument with premises $P_1, \dots, P_n$ and conclusion $C$ is valid, written $P_1, \dots, P_n \vDash C$, iff the formula $(P_1 \land \dots \land P_n) \to C$ is a tautology, true in every row of its truth table. Equivalently, no row makes every $P_i$ true and $C$ false; such a row is a **counterexample** to the form.[^lehman] For modus tollens, $\big((H \to P) \land \neg P\big) \to \neg H$ is a tautology (the contrapositive, [[Propositional Logic#Deeper (L2)]]); for affirming the consequent, the row $H = F$, $P = T$ makes both premises true and the conclusion false.

## Computational representation

A brute-force validity checker, applied to the four forms and to the conservative model with its auxiliary assumption:

```python
from itertools import product

def implies(p: bool, q: bool) -> bool:
    return (not p) or q

def counterexamples(premises, conclusion, atoms):
    """Rows of the truth table where every premise is true and the conclusion false (none = valid)."""
    rows = []
    for values in product([True, False], repeat=len(atoms)):
        v = dict(zip(atoms, values))
        if all(f(v) for f in premises) and not conclusion(v):
            rows.append(v)
    return rows

rule = lambda v: implies(v["H"], v["P"])                   # if H then P
forms = {
    "modus ponens":             ([rule, lambda v: v["H"]],     lambda v: v["P"]),
    "modus tollens":            ([rule, lambda v: not v["P"]], lambda v: not v["H"]),
    "affirming the consequent": ([rule, lambda v: v["P"]],     lambda v: v["H"]),
    "denying the antecedent":   ([rule, lambda v: not v["H"]], lambda v: not v["P"]),
}
for name, (premises, conclusion) in forms.items():
    bad = counterexamples(premises, conclusion, ["H", "P"])
    print(f"{name:25s}", "valid" if not bad else f"invalid, e.g. {bad[0]}")

# C: conservative model, A: auxiliary assumption (density reflects 15N content), T: two bands at gen 1
premises = [lambda v: implies(v["C"] and v["A"], v["T"]), lambda v: not v["T"]]
print("not C:      ", counterexamples(premises, lambda v: not v["C"], ["C", "A", "T"]))
print("not (C, A): ", counterexamples(premises, lambda v: not (v["C"] and v["A"]), ["C", "A", "T"]))
```

Output:

```text
modus ponens              valid
modus tollens             valid
affirming the consequent  invalid, e.g. {'H': False, 'P': True}
denying the antecedent    invalid, e.g. {'H': False, 'P': True}
not C:       [{'C': True, 'A': False, 'T': False}]
not (C, A):  []
```

Rejecting $C$ alone is invalid (the counterexample has a false auxiliary $A$); rejecting the conjunction $C \land A$ is valid.

## Worked example

> [!example] Repairing a results section
> A paper argues: "Our model predicts that knockout mice gain weight. They gained weight. Therefore our model is correct."
> 1. **Form**: $H \to P$, $P$, so $H$: affirming the consequent, invalid.
> 2. **Why it matters**: a rival $K$ (the knockout reduces activity, or the cage was changed) also predicts $P$. With $H \to P$, $K \to P$ and $P$, even "$H$ or $K$" does not follow (Exercise 3).
> 3. **Repair**: deduce a prediction on which $H$ and $K$ disagree (for instance, food intake rises under $H$ and not under $K$), measure it, and apply modus tollens to whichever hypothesis fails.

## Common misconceptions

> [!warning] "A confirmed prediction proves the hypothesis"
> That is affirming the consequent. Confirmation counts as support only to the extent that rival hypotheses predicted otherwise ([[Empirical Evidence]]).

> [!warning] "A failed prediction refutes the hypothesis"
> It refutes the hypothesis *together with* its auxiliary assumptions. Check the assay, the controls and the analysis before discarding the idea.

## Exercises

> [!question] Exercise 1 (L1)
> Name the form and say whether it is valid. (a) If the variant creates a stop codon, the protein is truncated; the protein is not truncated; so the variant does not create a stop codon. (b) If a strain carries the resistance gene, it grows on the antibiotic; it grows; so it carries the gene. (c) If the sample is contaminated, the negative control shows a band; the sample is not contaminated; so the control shows no band.

> [!success]- Solution
> (a) Modus tollens, valid (whether its first premise is true is a separate question). (b) Affirming the consequent, invalid: another mechanism could allow growth. (c) Denying the antecedent, invalid: the control could show a band for another reason, such as contaminated reagents.

> [!question] Exercise 2 (L2, Python)
> With `counterexamples`, check (a) the chain "$H \to P$, $P \to Q$, $\neg Q$, therefore $\neg H$"; (b) "$H \to P$, $K \to P$, $P$, therefore $H \lor K$".

> [!success]- Solution
> ```python
> chain = [lambda v: implies(v["H"], v["P"]), lambda v: implies(v["P"], v["Q"]), lambda v: not v["Q"]]
> print(counterexamples(chain, lambda v: not v["H"], ["H", "P", "Q"]))      # []
> rivals = [lambda v: implies(v["H"], v["P"]), lambda v: implies(v["K"], v["P"]), lambda v: v["P"]]
> print(counterexamples(rivals, lambda v: v["H"] or v["K"], ["H", "K", "P"]))
> # [{'H': False, 'K': False, 'P': True}]
> ```
> (a) is valid: modus tollens applied twice. (b) is invalid: $P$ can hold for a reason neither hypothesis names, so observing $P$ does not even show that one of them is right.

## Mastery checklist

- [ ] 1 Recognized: I can define deduction, validity and soundness.
- [ ] 2 Understood: I can name modus ponens, modus tollens and the two classic fallacies, and explain the Meselson-Stahl deductions with them.
- [ ] 3 Practiced: I can check an argument's validity with a truth-table program, including arguments with auxiliary assumptions.
- [ ] 4 Applied: before an experiment or benchmark, I write the deduced prediction and its auxiliary assumptions, and spot affirming the consequent in papers I read.
- [ ] 5 Explained: I can teach why refutation hits hypothesis plus auxiliaries, and why a statistical rejection is not a modus tollens ([[P-Value]]).

## References

[^os1]: [[Biology 2e (OpenStax)]], ch. 1 "The Study of Life", section 1.1 "The Science of Biology" (deductive reasoning in hypothesis-based science).
[^lehman]: [[Mathematics for Computer Science (Lehman)]], 2017 revision, Part I "Proofs" (logical deductions and inference rules, modus ponens, sound rules; valid formulas).
[^popper]: [[The Logic of Scientific Discovery (Popper)]], part on testing theories (refutation by deduced consequences; auxiliary hypotheses).
[^meselson]: [[Meselson 1958 - The Replication of DNA in Escherichia coli]], Meselson M, Stahl FW, *PNAS* 44(7):671-682.
