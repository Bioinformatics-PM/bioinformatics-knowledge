---
aliases:
  - Boyd and Vandenberghe
tags:
  - type/source
  - domain/mathematics
  - domain/computer-science
  - level/L3
  - level/M1
kind: book
tier: S
authors:
  - Stephen Boyd
  - Lieven Vandenberghe
institution: Cambridge University Press
year: 2004
edition: "1st"
url: "https://web.stanford.edu/~boyd/cvxbook/"
access: free
---

# Convex Optimization (Boyd)

> [!abstract]
> The standard textbook on convex optimization, from convex sets and duality to interior-point algorithms, free as a PDF from the authors' website.

## Why this source

Convexity is what makes an optimization problem reliably solvable: every local minimum is global, and duality gives certificates of optimality. The book teaches how to recognize and formulate convex problems, which covers least squares, regularized regression, support vector machines and many estimation problems in biology. Cambridge University Press allows the authors to keep it on the web, and it is the text of Stanford EE364A and UCLA EE236B.

## Coverage

Coverage is described by the book's three parts; chapter numbers were not verified in this pass.

| Part | Content | Vault notes |
|---|---|---|
| Theory | Convex sets, convex functions, convex optimization problems, duality and optimality conditions | [[Convex Function]], [[Convex Optimization]], [[Karush-Kuhn-Tucker Conditions]], [[Lagrange Multiplier]] |
| Applications | Approximation and fitting, statistical estimation, geometric problems | [[Optimization Problem]], [[Linear Programming]] |
| Algorithms | Unconstrained and constrained minimization, Newton's method, interior-point methods | [[Gradient Descent]], [[Newton's Method]] |

Cited in [[Optimization]].

## How to use it

- L3: read the theory part for items 2, 8 and 9 of [[Optimization]]; do selected exercises, then solve small problems with CVXPY (source code for most examples of the applications part is available in CVX, CVXOPT and CVXPY).
- M1: use the applications part (statistical estimation) to connect with maximum likelihood and regularized models.

## Caveats

- Mathematically demanding: needs linear algebra and multivariable calculus at the level of [[MIT 18.06SC - Linear Algebra]] and [[MIT 18.02SC - Multivariable Calculus]].
- Nonconvex problems, such as training deep networks, are outside its scope.
- Verified in this pass: authors, publisher, year, free PDF on the book website with the publisher's permission, and course websites.
