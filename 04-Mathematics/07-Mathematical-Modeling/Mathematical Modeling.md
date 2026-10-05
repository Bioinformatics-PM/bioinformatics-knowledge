---
aliases:
  - Mathematical Biology
  - Biological Modeling
  - Modélisation mathématique
tags:
  - type/moc
  - domain/mathematics
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Calculus]]"
  - "[[Differential Equations]]"
  - "[[Linear Algebra]]"
projects:
  - "[[07-evolution-simulator]]"
sources:
  - "[[Mathematical Biology (Murray)]]"
  - "[[Nonlinear Dynamics and Chaos (Strogatz)]]"
  - "[[MIT 8.591J - Systems Biology]]"
  - "[[MIT 18.03SC - Differential Equations]]"
  - "[[University of Cambridge - Natural Sciences Tripos]]"
  - "[[Université Paris-Saclay - Licence Double Diplôme Mathématiques Sciences de la Vie]]"
---

# Mathematical Modeling

> [!abstract]
> Turning a biological question into equations and back: the classic deterministic models of growth, interaction, epidemics and regulation, and the craft of calibrating, simplifying and testing a model against data.

## Why it matters for bioinformatics

- Models turn data into mechanism: a growth curve gives a doubling time, a time course gives kinetic constants, an epidemic curve gives $R_0$.
- The same few models recur everywhere: exponential and [[Logistic Growth]] (cultures, tumors, PCR), [[Lotka-Volterra Model|Lotka-Volterra]] (microbial communities), [[Compartmental Model|compartmental models]] (epidemics, pharmacokinetics), [[Hill Function|Hill-type input functions]] (gene regulation).
- Calibration, sensitivity and identifiability decide whether fitted parameters mean anything, which is the question behind every systems-biology result.

## Before you start

- [[Mathematical Foundations]]: [[Exponential Function]], [[Logarithm]]; [[Calculus]]: [[Derivative]].
- [[Differential Equations]]: [[Ordinary Differential Equation]], [[Fixed Point]], [[Linear Stability Analysis]], [[Euler Method]].
- [[Linear Algebra]]: [[Eigenvalues and Eigenvectors]] (for item 11).
- [[Optimization]]: [[Nonlinear Least Squares]] (for item 14).
- From other domains: [[Order-of-Magnitude Estimation]] ([[Biophysics]]) for item 1, [[Cooperativity]] ([[Biochemistry]]) for item 8, [[Steady-State Approximation]] ([[Physical Chemistry]]) for item 9, [[Dimensional Analysis]] ([[Mechanics]]) for item 13.

## Learning path

### Stage 1 - Foundations (L1)

1. [[Mathematical Model]] (L1): go from a question to assumptions, variables, parameters and equations, then to predictions that can be tested; tell deterministic from stochastic and discrete from continuous models.
2. [[Exponential Growth]] (L1): model unconstrained growth, compute doubling times and fit on a log scale. Bio: bacteria in log phase; PCR (one qPCR cycle of delay means half the starting template).

### Stage 2 - Core (L2)

3. [[Power Law]] (L2): recognize $y = a x^b$ on a log-log plot and estimate the exponent. Bio: allometric scaling of metabolic rate; heavy-tailed degree distributions of networks.
4. [[Discrete-Time Model]] (L2): iterate $x_{t+1} = f(x_t)$, find fixed points, use cobweb diagrams; see chaos in the logistic map. Bio: populations with non-overlapping generations; the deterministic selection recursion for allele frequencies.
5. [[Logistic Growth]] (L2): add a carrying capacity, solve and fit the logistic equation. Bio: growth curves from plate readers; tumor growth.
6. [[Lotka-Volterra Model]] (L2): analyze predator-prey and competition models. Bio: predator-prey cycles; generalized Lotka-Volterra models of microbiome dynamics.
7. [[Compartmental Model]] (L2): write mass-balance equations between compartments. Bio: one- and two-compartment pharmacokinetics; epidemic compartments.
8. [[Hill Function]] (L2): model cooperative, switch-like responses with $x^n / (K^n + x^n)$. Bio: transcription-factor input functions of gene regulation.

### Stage 3 - Advanced (L3)

9. [[Quasi-Steady-State Approximation]] (L3): generalize the chemical steady-state approximation into a model-reduction method based on separated time scales. Bio: deriving [[Michaelis-Menten Kinetics]] from mass action; mRNA equilibrating faster than protein.
10. [[SIR Model]] (L3): analyze susceptible-infected-recovered dynamics, final size and herd-immunity threshold. Bio: epidemic curves of real outbreaks.
11. [[Basic Reproduction Number]] (L3): compute $R_0$ and read the epidemic threshold. Bio: vaccination coverage needed to stop transmission, $1 - 1/R_0$.
12. [[Matrix Population Model]] (L3): build a Leslie matrix; read the growth rate and stable age structure from its dominant eigenpair. Bio: structured populations in ecology and conservation.
13. [[Nondimensionalization]] (L3): rescale variables to reveal the few dimensionless groups that control behavior.
14. [[Model Calibration]] (L3): estimate model parameters from time-course data and quantify their uncertainty. Bio: fitting kinetic or epidemic models to measurements.
15. [[Sensitivity Analysis]] (L3): measure how outputs respond to parameters, locally and globally. Bio: which rate constants control a pathway; robustness of gene circuits.
16. [[Parameter Identifiability]] (L3): decide whether parameters can be determined from the available data (structural and practical identifiability).

### Stage 4 - Frontier (M1)

17. [[Agent-Based Model]] (M1): simulate individuals following local rules and compare with mean-field equations. Bio: tumor growth, epidemics on contact networks, individual-based population genetics.

> [!tip] How to study it
> Build every model three times: on paper (fixed points, stability), in Python (numerical solution), and against data (calibration). Pair items 5 to 10 with the corresponding chapters of Murray or Strogatz, and item 8 with [[Systems Biology]].

## Uses from other domains

- [[Michaelis-Menten Kinetics]] ([[Biochemistry]]): the classic result of item 9.
- [[Scientific Model]] ([[Scientific Method]]): what a model is for, epistemologically.
- [[Wright-Fisher Model]], [[Hardy-Weinberg Equilibrium]] ([[Evolution]]): discrete-time and stochastic models of allele frequencies.
- [[Biochemical Kinetic Model]], [[Gene Regulatory Network]], [[Flux Balance Analysis]] ([[Systems Biology]]): modeling of cellular networks.
- [[Markov Chain]], [[Gillespie Algorithm]] ([[Stochastic Processes]]): stochastic versions of these models.
- [[Model Selection]] ([[Statistical Inference]]): comparing competing models.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 8.591J - Systems Biology]] | MIT | L3 | "Input Function, Michaelis-Menten Kinetics, and Cooperativity" (items 8, 9); gene circuits and population dynamics as small models[^8591] |
| [[MIT 18.03SC - Differential Equations]] | MIT | L2 | Unit I: modeling with first-order equations[^1803] |

## Reference books

- [[Mathematical Biology (Murray)]]: population models (continuous and discrete), biochemical oscillators and reaction kinetics, epidemic models (items 4-7, 9-10).[^murray]
- [[Nonlinear Dynamics and Chaos (Strogatz)]]: one- and two-dimensional flows with biological examples (SIR, glycolytic oscillations), chaos in iterated maps (items 4, 10).[^strogatz]

## Lab projects

- [[07-evolution-simulator]]: a stochastic population model compared with its deterministic counterpart (item 4).

## References

[^8591]: [[MIT 8.591J - Systems Biology]], verified lecture titles; every lecture turns a biological question into a small dynamical model.
[^1803]: [[MIT 18.03SC - Differential Equations]], Unit I "First Order Differential Equations" (modeling physical systems).
[^murray]: [[Mathematical Biology (Murray)]], 3rd ed., Volume I.
[^strogatz]: [[Nonlinear Dynamics and Chaos (Strogatz)]], 3rd ed.

Scope check: modeling is taught to biologists from the first year, at Cambridge (mathematical modeling in Part IA Mathematical Biology)[^cam] and at Paris-Saclay (a supervised bio-mathematics project in L1).[^psmsv] Hence items 1 and 2 at L1, before formal courses on differential equations.

[^cam]: [[University of Cambridge - Natural Sciences Tripos]], Part IA Mathematical Biology.
[^psmsv]: [[Université Paris-Saclay - Licence Double Diplôme Mathématiques Sciences de la Vie]], L1 structure.
