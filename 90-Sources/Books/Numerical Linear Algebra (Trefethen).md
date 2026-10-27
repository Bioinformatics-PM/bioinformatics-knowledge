---
aliases:
  - Trefethen and Bau
  - Trefethen & Bau
tags:
  - type/source
  - domain/mathematics
  - domain/computer-science
  - level/L3
  - level/M1
kind: book
tier: S
authors:
  - Lloyd N. Trefethen
  - David Bau III
institution: SIAM
year: 1997
edition: "1st"
url: "https://doi.org/10.1137/1.9780898719574"
access: paid
---

# Numerical Linear Algebra (Trefethen)

> [!abstract]
> A graduate textbook in 40 short lectures on the algorithms of numerical linear algebra and on why they are, or are not, accurate in floating point.

## Why this source

The standard first graduate text on the subject. Each lecture develops one idea in a few pages, and conditioning and stability are treated as carefully as the algorithms themselves: the right companion for anyone who relies on library solvers and wants to know when to trust them.

## Coverage

Citation: Trefethen LN, Bau D III. *Numerical Linear Algebra*. Society for Industrial and Applied Mathematics, Philadelphia (1997). ISBN 978-0-89871-361-9. doi:10.1137/1.9780898719574.

| Part | Content | Vault notes |
|---|---|---|
| Lectures 20-23 | "Gaussian Elimination", "Pivoting", "Stability of Gaussian Elimination" (growth factor; partial pivoting can let entries grow by $2^{m-1}$ yet is stable in practice), "Cholesky Factorization" | [[LU Decomposition]], [[Gaussian Elimination]], [[Positive Definite Matrix]] |
| Other lectures (by topic) | QR factorization and least squares, conditioning and stability, eigenvalue algorithms, iterative methods | [[QR Decomposition]], [[Least Squares]], [[Singular Value Decomposition]], [[Numerical Linear Algebra]] |

## How to use it

- L3: lectures 20-23 right after [[LU Decomposition]]; the QR and least-squares lectures with [[QR Decomposition]].
- M1: conditioning, stability and iterative methods with [[Numerical Linear Algebra]].

## Caveats

- Paid. Assumes a first course in linear algebra and comfort with norms.
- Verified in this pass (web search): authors, publisher, year, DOI, ISBN, the 40-lecture structure, the titles of lectures 20-23, and the growth-factor result discussed in lecture 22 (bound $2^{m-1}$ for partial pivoting, large growth rare in practice). Titles of the other lectures were not checked; that row is by topic.
