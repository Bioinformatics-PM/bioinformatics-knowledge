---
aliases:
  - LAPACK
  - LAPACK User's Guide
  - LUG
tags:
  - type/source
  - domain/computer-science
  - domain/mathematics
  - level/L2
  - level/L3
kind: book
tier: A
authors:
  - E. Anderson
  - Z. Bai
  - C. Bischof
  - S. Blackford
  - J. Demmel
  - J. Dongarra
  - J. Du Croz
  - A. Greenbaum
  - S. Hammarling
  - A. McKenney
  - D. Sorensen
institution: SIAM
year: 1999
edition: "3rd"
url: "https://www.netlib.org/lapack/lug/"
access: free
---

# LAPACK Users' Guide (Anderson)

> [!abstract]
> The manual of LAPACK, the standard library of dense linear algebra routines (linear systems, least squares, eigenvalues, singular values), written by its developers.

## Why this source

NumPy and SciPy document the LAPACK routines that their linear algebra functions call (for example `gesv` for `numpy.linalg.solve`, `getrf` for `scipy.linalg.lu_factor`). This guide is the reference for what those routines compute: the naming scheme, the driver routines (one call solves a whole problem) and the computational routines (one factorization or one solve), and how block algorithms built on the BLAS make them fast. The HTML edition is free on netlib.

## Coverage

Citation: Anderson E, Bai Z, Bischof C, Blackford S, Demmel J, Dongarra J, Du Croz J, Greenbaum A, Hammarling S, McKenney A, Sorensen D. *LAPACK Users' Guide*, 3rd ed. Society for Industrial and Applied Mathematics, Philadelphia (1999), series Software, Environments, and Tools. ISBN 0-89871-447-8.

| Part | Content | Vault notes |
|---|---|---|
| Linear equations | `xGETRF`: LU factorization $A = PLU$ of a general matrix with partial pivoting and row interchanges ($L$ unit lower triangular, its diagonal not stored); `xGETRS`: solve with the stored factors; `xGESV`: driver doing both for several right-hand sides; `xPOTRF`: Cholesky factorization | [[LU Decomposition]], [[Positive Definite Matrix]], [[Numerical Linear Algebra]] |
| Accuracy | Condition estimation, iterative refinement and error bounds for computed solutions | [[Floating-Point Arithmetic]], [[Numerical Linear Algebra]] |
| Performance | Block algorithms that do most of their work in Level 3 BLAS (matrix-matrix) calls | [[Numerical Linear Algebra]], [[Memory Hierarchy]] |

## How to use it

- L2: read the description of the linear-equation routines with [[LU Decomposition]], then map NumPy and SciPy functions to the routines their docstrings name.
- L3: the accuracy and performance material with [[Numerical Linear Algebra]].

## Caveats

- The 1999 edition describes LAPACK 3.0; later releases added routines. The reference documentation distributed with LAPACK describes the current version.
- Verified in this pass (web search): authors, publisher, year, edition, series, ISBN, and the reference documentation of `xGETRF` (factorization $A = P L U$ with partial pivoting and row interchanges, $L$ unit lower triangular). The netlib pages could not be opened (web fetching blocked), so section titles and numbers are not given; the other coverage rows are cited at book level.
