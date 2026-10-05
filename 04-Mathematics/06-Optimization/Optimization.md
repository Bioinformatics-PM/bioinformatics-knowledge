---
aliases:
  - Mathematical Optimization
  - Optimisation
tags:
  - type/moc
  - domain/mathematics
  - domain/computer-science
  - level/L2
  - level/L3
prerequisites:
  - "[[Calculus]]"
  - "[[Linear Algebra]]"
projects:
  - "[[04-alignment-engine]]"
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]]"
  - "[[MIT 6.036 - Introduction to Machine Learning]]"
  - "[[Introduction to Linear Algebra (Strang)]]"
  - "[[Convex Optimization (Boyd)]]"
  - "[[MIT - Course 6-7 Computer Science and Molecular Biology]]"
---

# Optimization

> [!abstract]
> Finding the best parameters or structures under constraints: continuous optimization (gradients, Newton, Lagrange, convexity), linear and integer programming, and heuristics for the combinatorial problems that biology is full of.

## Why it matters for bioinformatics

- **Fitting is optimizing.** Maximum likelihood, least squares, regularized regression and neural-network training are all minimizations of an objective function.
- **Linear programming** is [[Flux Balance Analysis]]: maximize biomass production subject to steady-state and capacity constraints.
- **Many core problems are NP-hard** (maximum parsimony, multiple alignment, assembly variants): knowing exact methods, heuristics and their guarantees tells you what a tool's output really means.

## Before you start

- [[Calculus]]: [[Extremum]], [[Gradient]], [[Hessian Matrix]].
- [[Linear Algebra]]: [[Least Squares]], [[Positive Definite Matrix]].
- [[Algorithms]]: [[Greedy Algorithm]], [[Dynamic Programming]], [[NP-Completeness]].

## Learning path

### Stage 2 - Core (L2)

1. [[Optimization Problem]] (L2): state objective, decision variables, constraints and feasible set; tell local from global optima. Bio: an alignment score, a tree likelihood and a model's squared error are all objectives.
2. [[Convex Function]] (L2): test convexity and use the fact that a local minimum is global. Bio: the negative log-likelihood of logistic regression and of most GLMs is convex, so fitting them is reliable.
3. [[Gradient Descent]] (L2): minimize by stepping against the gradient; choose a learning rate; diagnose divergence. Bio: fitting logistic regression and training neural networks on omics data.
4. [[Newton's Method]] (L2): use first and second derivatives for fast local convergence (Newton-Raphson). Bio: iteratively reweighted least squares for GLMs; optimizing branch lengths in maximum likelihood phylogenetics.
5. [[Lagrange Multiplier]] (L2): optimize under equality constraints. Bio: the maximum likelihood nucleotide frequencies are the observed proportions (constraint: they sum to 1); maximum entropy distributions.
6. [[Linear Programming]] (L2): formulate linear objectives with linear constraints and read the solution geometrically. Bio: [[Flux Balance Analysis]] of a metabolic network.

### Stage 3 - Advanced (L3)

7. [[Stochastic Gradient Descent]] (L3): optimize on mini-batches; use momentum and adaptive steps. Bio: training deep models on millions of sequences or cells.
8. [[Convex Optimization]] (L3): recognize convex programs (least squares, quadratic programs, lasso) and their guarantees. Bio: support vector machines and sparse regression for biomarker selection.
9. [[Karush-Kuhn-Tucker Conditions]] (L3): write optimality conditions with inequality constraints; read dual variables. Bio: support vectors of an SVM; shadow prices of metabolites in flux balance analysis.
10. [[Simplex Algorithm]] (L3): follow vertices of the feasible polytope to the optimum. Bio: what LP solvers do inside flux balance analysis.
11. [[Nonlinear Least Squares]] (L3): fit nonlinear models with Gauss-Newton and Levenberg-Marquardt; handle starting values. Bio: estimating $V_{max}$ and $K_M$ from enzyme velocity data; fitting growth curves.
12. [[Integer Linear Programming]] (L3): model yes/no decisions with integer variables; know it is NP-hard in general. Bio: exact formulations of haplotype phasing, pathway selection and protein design of modest size.
13. [[Combinatorial Optimization]] (L3): recognize optimization over discrete structures and choose between exact, approximate and heuristic methods. Bio: maximum parsimony tree search, multiple sequence alignment.
14. [[Local Search]] (L3): improve a solution by neighborhood moves (hill climbing), and understand local optima and restarts. Bio: nearest-neighbor interchange and subtree pruning-regrafting moves in phylogenetic search.
15. [[Simulated Annealing]] (L3): accept worse moves with a decreasing probability to escape local optima. Bio: protein structure prediction and phylogeny search; a cousin of [[Markov Chain Monte Carlo]].

> [!tip] How to study it
> Implement items 3, 4 and 11 by hand on a one- or two-parameter likelihood before using `scipy.optimize`. Do items 6, 9 and 10 together with [[Flux Balance Analysis]] in [[Systems Biology]], and items 13 to 15 together with [[Phylogenetics]].

## Uses from other domains

- [[Maximum Likelihood Estimation]], [[Expectation-Maximization Algorithm]] ([[Statistical Inference]]): likelihood maximization.
- [[Neural Network]], [[Support Vector Machine]], [[Lasso]] ([[Statistical Learning]]): trained by the methods above.
- [[Stoichiometric Matrix]], [[Flux Balance Analysis]] ([[Systems Biology]]): linear programming.
- [[Maximum Parsimony]], [[Maximum Likelihood Phylogenetics]], [[Phylogenetic Tree Search]] ([[Phylogenetics]]): combinatorial and continuous optimization over trees.
- [[Multiple Sequence Alignment]] ([[Sequence Analysis]]): an NP-hard optimization solved heuristically.
- [[Dynamic Programming]], [[Approximation Algorithm]], [[Network Flow]] ([[Algorithms]]): exact optimization when the problem decomposes, guarantees when it does not.
- [[Root Finding]] ([[Scientific Computing]]): Newton's method for equations, the twin of item 4.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]] | MIT | L3 | Optimization part, lecture 25 "Stochastic Gradient Descent" (items 3, 7)[^18065] |
| [[MIT 6.036 - Introduction to Machine Learning]] | MIT | L3 | Learning as optimization; gradient-based training of classifiers and neural networks (items 3, 7)[^6036] |

## Reference books

- [[Introduction to Linear Algebra (Strang)]]: final chapters on optimization and learning from data (items 1-3).[^strang]
- [[Convex Optimization (Boyd)]]: convex sets and functions, duality and KKT conditions, algorithms (items 2, 8, 9).

## Lab projects

- [[04-alignment-engine]]: optimal alignment as the maximization of a score, solved exactly by dynamic programming.
- [[08-phylogenetic-engine]]: branch-length optimization and tree search for likelihood methods.

## References

[^18065]: [[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]], optimization part; lecture 25 verified by title.
[^6036]: [[MIT 6.036 - Introduction to Machine Learning]]: formulation of learning problems, supervised learning, neural networks.
[^strang]: [[Introduction to Linear Algebra (Strang)]], 6th ed., final chapters.

Scope check: MIT's joint Computer Science and Molecular Biology degree pairs linear algebra with optimization in one required course (6.C06[J] Linear Algebra and Optimization).[^mit67] The scope here is targeted at L2/L3: the methods behind likelihood fitting, machine learning, flux balance analysis and tree search, not a full operations-research course.

[^mit67]: [[MIT - Course 6-7 Computer Science and Molecular Biology]], mathematics and introductory CS block.
