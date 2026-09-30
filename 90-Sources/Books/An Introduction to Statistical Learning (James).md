---
aliases:
  - ISLP
  - ISL
tags:
  - type/source
  - domain/statistics
  - domain/computer-science
  - level/L2
  - level/L3
kind: book
tier: S
authors:
  - Gareth James
  - Daniela Witten
  - Trevor Hastie
  - Robert Tibshirani
  - Jonathan Taylor
institution: Springer
year: 2023
edition: "1st Python edition (ISLP)"
url: "https://statlearning.com/"
access: free
---

# An Introduction to Statistical Learning (James)

> [!abstract]
> The standard introduction to statistical learning, in its 2023 Python edition (ISLP), free to read online.

## Why this source

Explains the core statistical and machine-learning methods with minimal mathematics and complete labs. The Python edition matches this vault's language choice. Its multiple-testing chapter is directly relevant to genomics.

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| Regression | Linear regression, resampling | [[Linear Regression]], [[Cross-Validation]], [[Bootstrap]] |
| Classification | Classification methods | [[Classification]], [[Logistic Regression]] |
| Model selection | Shrinkage approaches | [[Regularization]] |
| Nonlinear methods | Tree-based methods, support vector machines, deep learning | [[Decision Tree]], [[Support Vector Machine]], [[Neural Network]] |
| Unsupervised learning | Clustering, PCA | [[Clustering]], [[Principal Component Analysis]] |
| Special topics | Survival analysis, multiple testing | [[Survival Analysis]], [[Multiple Testing Correction\|Multiple Testing]], [[False Discovery Rate]] |

## How to use it

- L2: regression, classification and resampling chapters, with the Python labs (the `ISLP` package).
- L3: trees, SVM, unsupervised learning, multiple testing.
- The R edition (ISLR) covers the same material with R labs.

## Caveats

- Intuition-first; for derivations see the more advanced *The Elements of Statistical Learning*.
- Chapter numbers not verified here; topic list from the publisher description.
