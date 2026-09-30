---
aliases:
  - Analysis
  - Analyse
tags:
  - type/moc
  - domain/mathematics
  - level/L1
  - level/L2
prerequisites:
  - "[[Mathematical Foundations]]"
projects: []
sources:
  - "[[MIT 18.01SC - Single Variable Calculus]]"
  - "[[MIT 18.02SC - Multivariable Calculus]]"
  - "[[MIT 18.03SC - Differential Equations]]"
  - "[[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]]"
  - "[[Calculus (OpenStax)]]"
  - "[[MIT - Course 6-7 Computer Science and Molecular Biology]]"
  - "[[Tsinghua University - BS Biological Sciences]]"
---

# Calculus

> [!abstract]
> Rates of change and accumulation: single-variable differentiation, integration and series (L1), then functions of several variables up to the gradient, Jacobian and Hessian (L2).

## Why it matters for bioinformatics

- **Derivatives** are rates: growth rates, reaction velocities, mutation accumulation. Setting a derivative to zero is how a maximum likelihood estimate is found by hand.
- **Integrals** turn densities into probabilities; every continuous distribution in [[Probability]] is an integral.
- **Series** give the approximations bioinformaticians use without noticing ($e^{x} \approx 1 + x$ for small rates, the Poisson normalization $\sum_k \lambda^k / k! = e^{\lambda}$).
- **Multivariable calculus** is the engine of model fitting: gradients drive [[Gradient Descent]] and neural-network training, Jacobians decide the stability of gene circuits and epidemics, Hessians give the standard errors of likelihood estimates.

## Before you start

- [[Mathematical Foundations]]: [[Function]], [[Exponential Function]], [[Logarithm]], [[Summation Notation]].
- For Stage 2 only: [[Vector]] and [[Matrix]] from [[Linear Algebra]].

## Learning path

### Stage 1 - Foundations (L1)

1. [[Limit]] (L1): compute limits of sequences and functions, including $(1 + 1/n)^n \to e$. Bio: the binomial-to-Poisson limit for rare events (mutations, read starts).
2. [[Continuity]] (L1): use the intermediate value theorem to prove a root exists. Bio: existence of a steady state between two concentrations.
3. [[Derivative]] (L1): interpret $f'(x)$ as a rate and a slope; differentiate from the definition. Bio: growth rate $dN/dt$, reaction velocity $d[P]/dt$.
4. [[Differentiation Rules]] (L1): apply sum, product, quotient and chain rules; differentiate $e^x$, $\ln x$ and powers. Bio: differentiating a log-likelihood.
5. [[Linear Approximation]] (L1): replace a function by its tangent line and bound the error. Bio: $\ln(1 + x) \approx x$ for small rates; propagating measurement error.
6. [[Extremum]] (L1): find and classify local and global maxima and minima. Bio: the maximum likelihood estimate $\hat p = k/n$ of a binomial proportion (GC fraction, allele frequency).
7. [[Antiderivative]] (L1): invert differentiation; solve $y' = f(t)$. Bio: recovering a quantity from its rate of production.
8. [[Integral]] (L1): define the definite integral as a limit of Riemann sums; interpret it as area and accumulation. Bio: probability as the area under a density; area under the ROC curve; drug exposure (AUC).
9. [[Fundamental Theorem of Calculus]] (L1): link derivatives and integrals. Bio: a cumulative distribution function is the integral of its density.
10. [[Integration by Substitution]] (L1): change variables in an integral. Bio: standardizing a normal variable; log-transforming a density.
11. [[Integration by Parts]] (L1): integrate products. Bio: the mean of an exponential waiting time; the gamma function.
12. [[Improper Integral]] (L1): integrate over infinite ranges and decide convergence. Bio: normalizing the normal density; expected values of continuous random variables.
13. [[Infinite Series]] (L1): sum geometric series and test convergence. Bio: the mean length of a geometric run (CpG island or HMM state duration); Poisson probabilities summing to 1.
14. [[Taylor Series]] (L1): approximate functions by polynomials and control the remainder. Bio: Jukes-Cantor distance close to the raw mismatch proportion at small divergence; the delta method for variances.

### Stage 2 - Core (L2)

15. [[Multivariable Function]] (L2): read surfaces and contour plots of $f(x, y)$. Bio: a likelihood surface over two parameters.
16. [[Partial Derivative]] (L2): differentiate with respect to one variable at a time. Bio: sensitivity of a model output to one parameter.
17. [[Gradient]] (L2): compute $\nabla f$, directional derivatives and steepest ascent. Bio: joint maximum likelihood of several parameters; the step of gradient descent.
18. [[Multivariable Chain Rule]] (L2): differentiate compositions of multivariable functions. Bio: backpropagation in a [[Neural Network]] is the chain rule applied layer by layer.
19. [[Jacobian Matrix]] (L2): linearize a vector-valued function; use $|\det J|$ in a change of variables. Bio: stability of a steady state of a gene circuit or an SIR epidemic.
20. [[Hessian Matrix]] (L2): classify critical points with second derivatives; read curvature. Bio: curvature of the log-likelihood gives standard errors (Fisher information); Newton's method.
21. [[Multiple Integral]] (L2): integrate over regions in the plane and space, with change of variables. Bio: probabilities from a joint density; normalizing the bivariate normal.

> [!tip] What to skip
> Vector calculus (line and surface integrals, Green and Stokes theorems) is not needed on this path; skim it in 18.02SC. Spend the time on the gradient, the Jacobian and the Hessian, and on integrals of densities.

## Uses from other domains

- [[Probability Density Function]], [[Cumulative Distribution Function]], [[Expected Value]] ([[Probability]]): integrals of densities.
- [[Maximum Likelihood Estimation]] ([[Statistical Inference]]): maximize with [[Derivative]], [[Gradient]] and [[Hessian Matrix]].
- [[Reaction Kinetics]] ([[Physical Chemistry]]) and [[Michaelis-Menten Kinetics]] ([[Biochemistry]]): rates as derivatives.
- [[Numerical Integration]] ([[Scientific Computing]]): what to do when an [[Integral]] has no closed form.
- [[Neural Network]] ([[Statistical Learning]]): trained with the [[Multivariable Chain Rule]].

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 18.01SC - Single Variable Calculus]] | MIT | L1 | Differentiation, integration, infinite series (Stage 1)[^1801] |
| [[MIT 18.02SC - Multivariable Calculus]] | MIT | L1-L2 | Partial derivatives, gradient, multiple integrals (Stage 2); vector calculus optional[^1802] |
| [[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]] | MIT | L3 | Gradients in optimization (lecture 25, stochastic gradient descent), to see Stage 2 in use[^18065] |

## Reference books

- [[Calculus (OpenStax)]]: Volume 1 (limits, derivatives, integration), Volume 2 (techniques of integration, sequences and series), Volume 3 (functions of several variables, multiple integration).[^openstax]

## Lab projects

No Lab project is built on calculus alone. It enters through likelihood maximization in [[08-phylogenetic-engine]] and through the dynamic models of [[Mathematical Modeling]].

## References

[^1801]: [[MIT 18.01SC - Single Variable Calculus]]: differentiation, integration, then a brief treatment of infinite series; this sets the order of Stage 1.
[^1802]: [[MIT 18.02SC - Multivariable Calculus]]: differential calculus of several variables (partial derivatives, gradient), multiple integrals, vector calculus.
[^18065]: [[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]], lecture 25 "Stochastic Gradient Descent".
[^openstax]: [[Calculus (OpenStax)]], coverage by volume.

Scope check: calculus is required wherever course titles were verified in the [[Curriculum Benchmark]], typically over two semesters: 18.01 and 18.02 in MIT's science core,[^mit67] Calculus B(1) and B(2) at Tsinghua.[^thu] The Jacobian and Hessian are included at a basic level because [[MIT 18.03SC - Differential Equations]] Unit IV (autonomous 2x2 systems, phase portraits) and likelihood-based inference rely on them.[^1803]

[^mit67]: [[MIT - Course 6-7 Computer Science and Molecular Biology]], GIR science core.
[^thu]: [[Tsinghua University - BS Biological Sciences]], mathematics block.
[^1803]: [[MIT 18.03SC - Differential Equations]], Unit IV "First Order Systems".
