---
aliases:
  - Numerical Methods
  - Calcul scientifique
tags:
  - type/moc
  - domain/computer-science
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Programming]]"
  - "[[Algorithms]]"
  - "[[Calculus]]"
  - "[[Linear Algebra]]"
  - "[[Probability]]"
projects:
  - "[[07-evolution-simulator]]"
  - "[[08-phylogenetic-engine]]"
  - "[[bio-simulation]]"
sources:
  - "[[Python for Data Analysis (McKinney)]]"
  - "[[MIT 18.03SC - Differential Equations]]"
  - "[[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[Stanford University - BS Biomedical Computation]]"
---

# Scientific Computing

> [!abstract]
> Computing with real numbers on real machines: how integers and floating-point numbers are stored and where they fail, numerical stability and conditioning, vectorized array computation, linear algebra libraries, random numbers and Monte Carlo, numerical integration, stiff ODE solvers, and measuring and improving performance.

## Why it matters for bioinformatics

Statistical genomics, phylogenetics and systems biology are numerical computations, and their bugs are silent. The likelihood of a tree or of a hidden Markov model underflows to zero unless it is computed in [[Log-Space Arithmetic|log space]]; a 32-bit integer overflows on genome coordinates; a population simulation is only reproducible with seeded [[Random Number Generation|random numbers]]; a kinetic model is solved by an ODE solver whose step control you must understand; a Python loop over a count matrix is replaced by [[Vectorization]]. Computational biology programs pair calculus and differential equations with simulation courses,[^cmu] and Stanford's program has a dedicated Simulation track.[^stanford]

## Before you start

- [[Programming]]: [[N-Dimensional Array]], [[Array Indexing]], [[Broadcasting]].
- [[Calculus]]: [[Derivative]], [[Integral]], [[Taylor Series]] (error analysis).
- [[Linear Algebra]]: [[Matrix]], [[Matrix Multiplication]], [[Inverse Matrix]], [[LU Decomposition]], [[QR Decomposition]], [[Least Squares]], [[Positive Definite Matrix]] (Cholesky), [[Eigenvalues and Eigenvectors]], [[Singular Value Decomposition]].
- [[Differential Equations]]: [[Ordinary Differential Equation]], [[Euler Method]] and [[Runge-Kutta Method]]. The explicit solvers are taught there, as in MIT 18.03SC;[^mit1803] this syllabus adds stability, stiffness and implicit solvers.
- [[Probability]]: [[Probability Distribution]], [[Law of Large Numbers]], [[Central Limit Theorem]] (Monte Carlo error).
- [[Algorithms]]: [[Big O Notation]].

## Learning path

> [!tip] When to study it
> The [[Curriculum]] places this subdomain in Stage 3, but read Stage 1 here as soon as you start computing with NumPy: floating-point and integer surprises appear in the first project. Measure before optimizing: [[Performance Profiling]] comes before every speed-up technique.

### Stage 1 - Foundations (L1)

1. [[Integer Representation]] (L1): choose fixed-width integer dtypes (8-bit codes for bases, 64-bit genome coordinates) and predict the silent overflow of NumPy integers, which Python integers never have.
2. [[Floating-Point Arithmetic]] (L1): read an IEEE 754 double (sign, exponent, significand), know machine epsilon, NaN and infinity, and compare floats with tolerances, never with `==`.
3. [[Vectorization]] (L1): replace Python loops by whole-array operations and universal functions, and measure the speed-up.

### Stage 2 - Core (L2)

4. [[Performance Profiling]] (L2): time code with `timeit`, find hot spots with a profiler (cProfile, line_profiler, py-spy), and track peak memory, before changing anything.
5. [[Rounding Error]] (L2): propagate absolute and relative errors and spot catastrophic cancellation when subtracting nearly equal numbers.
6. [[Numerical Stability]] (L2): tell stable from unstable algorithms with forward and backward error (two-pass versus naive variance, compensated summation).
7. [[Log-Space Arithmetic]] (L2): multiply tiny probabilities as sums of logarithms and add them with the log-sum-exp trick, as HMM and phylogenetic likelihoods require.
8. [[Condition Number]] (L2): quantify how much a problem amplifies input perturbations and recognize ill-conditioned matrices that no algorithm can rescue.
9. [[Numerical Linear Algebra]] (L2): call the factorizations of [[Linear Algebra]] (LU, QR, Cholesky, SVD) through LAPACK and BLAS from NumPy and SciPy, solve instead of inverting, and predict cost, accuracy and multithreading.
10. [[Sparse Matrix]] (L2): store mostly-zero matrices in COO, CSR or CSC form and compute on them efficiently, as single-cell count matrices require.
11. [[Root Finding]] (L2): solve f(x) = 0 by bisection, Newton-Raphson and Brent's method, and know their convergence rates and failure modes.
12. [[Finite Difference]] (L2): approximate derivatives numerically and choose the step size that balances truncation error against rounding error.
13. [[Numerical Integration]] (L2): integrate with the trapezoidal rule, Simpson's rule and adaptive Gaussian quadrature, and estimate the error.
14. [[Random Number Generation]] (L2): use seeded pseudo-random generators (NumPy `Generator`), spawn independent streams for parallel runs, and make every stochastic result reproducible.
15. [[Random Variate Generation]] (L2): sample from arbitrary distributions by inverse transform and rejection sampling, and from binomial and multinomial laws for Wright-Fisher simulation.
16. [[Monte Carlo Method]] (L2): estimate integrals, probabilities and p-values by simulation, with an error that shrinks as 1/√N.

### Stage 3 - Advanced (L3)

17. [[Stiff Differential Equation]] (L3): recognize stiffness in kinetic models with widely separated time scales, see why explicit solvers crawl, and switch to implicit solvers (BDF, Radau) with error control.
18. [[Array Memory Layout]] (L3): reason about row-major versus column-major order, strides and contiguity, and their effect on cache use and speed.
19. [[Just-In-Time Compilation]] (L3): compile loop-heavy kernels that do not vectorize (dynamic programming, agent-based simulations) with Numba.
20. [[Out-of-Core Computation]] (L3): process arrays and tables larger than RAM by chunking, memory mapping and lazy task graphs (Dask, Zarr).

### Stage 4 - Frontier (M1)

21. [[Automatic Differentiation]] (M1): obtain exact gradients of numerical programs (JAX, PyTorch) for likelihood optimization and machine learning.

## Uses from other domains

- [[Gradient Descent]] and [[Newton's Method]] ([[Optimization]]): optimizers built on the numerical tools of this syllabus; Newton's method shares its convergence analysis with [[Root Finding]].
- [[Markov Chain Monte Carlo]] ([[Bayesian Statistics]]): sampling that relies on [[Random Number Generation]] and [[Log-Space Arithmetic]].
- [[Permutation Test]] and [[Bootstrap]] ([[Statistical Inference]]): Monte Carlo resampling applied to inference.
- [[Lotka-Volterra Model]] and [[Compartmental Model]] ([[Mathematical Modeling]]): ODE models solved with these solvers; [[Gillespie Algorithm]] ([[Stochastic Processes]]) is their exact stochastic counterpart, built on [[Random Number Generation]].
- [[Principal Component Analysis]] ([[Multivariate Analysis]]): computed through [[Singular Value Decomposition]] in LAPACK.
- [[Parallel Computing]] and [[Memory Hierarchy]] ([[Computer Systems]]): the hardware model behind vectorization and memory layout.
- [[Benchmarking]] ([[Software Engineering]]): how a speed-up is measured and reported.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 18.03SC - Differential Equations]] | MIT | L2 | Unit I includes Euler's method, the entry point to numerical ODE solving[^mit1803] |
| [[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]] | MIT | L3 | Matrix factorizations (lecture 6, singular value decomposition) and stochastic gradient descent, the computational side of linear algebra[^mit18065] |
| [[Carnegie Mellon University - BS Computational Biology]] | Carnegie Mellon University | L3 | 02-512 Computational Methods for Biological Modeling and Simulation[^cmu] |

## Reference books

- [[Python for Data Analysis (McKinney)]] (3rd ed.): NumPy arrays and vectorized computation, for Stage 1.[^mckinney]

## Lab projects

- [[07-evolution-simulator]]: [[Vectorization]] of population updates, [[Random Number Generation]] with reproducible seeds, [[Random Variate Generation]] for binomial sampling.
- [[08-phylogenetic-engine]]: [[Log-Space Arithmetic]] for tree likelihoods.
- [[bio-simulation]]: the shared simulation engine.

## References

[^cmu]: [[Carnegie Mellon University - BS Computational Biology]]: 21-120 and 21-122 (calculus, integration, differential equations and approximation) in the mathematics core and 02-512 Computational Methods for Biological Modeling and Simulation in the computational biology core.
[^stanford]: [[Stanford University - BS Biomedical Computation]]: the major splits into four tracks, one of which is Simulation.
[^mckinney]: [[Python for Data Analysis (McKinney)]], 3rd ed.: NumPy arrays and vectorized computation.
[^mit1803]: [[MIT 18.03SC - Differential Equations]], unit I: direction fields and Euler's method.
[^mit18065]: [[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]]: lecture 6 "Singular Value Decomposition", lecture 25 "Stochastic Gradient Descent".
