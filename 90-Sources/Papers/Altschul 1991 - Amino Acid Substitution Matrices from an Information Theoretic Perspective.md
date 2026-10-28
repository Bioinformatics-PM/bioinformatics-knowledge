---
aliases:
  - Altschul 1991
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Stephen F. Altschul
journal: Journal of Molecular Biology
year: 1991
url: "https://doi.org/10.1016/0022-2836(91)90193-A"
access: paid
---

# Altschul 1991 - Amino Acid Substitution Matrices from an Information Theoretic Perspective

> [!abstract]
> The paper that showed that every amino acid substitution matrix is implicitly a log-odds matrix with its own target distribution of aligned residue pairs, and used information theory (scores in bits) to explain why different matrices suit different purposes.

## Why this source

It turns the choice of a scoring matrix from habit into a question with an answer. Any substitution matrix is implicitly a log-odds matrix with a specific target distribution for aligned pairs of amino acids; information theory expresses its scores in bits and shows that different matrices are better adapted to different purposes. At the time the PAM250 matrix was the most widely used; the paper argues that for database searches PAM120 is generally more appropriate, while a matrix for a larger evolutionary distance suits the comparison of two specific proteins suspected to be distantly related.

## Coverage

Citation: Altschul SF. "Amino acid substitution matrices from an information theoretic perspective". *Journal of Molecular Biology* 219(3):555-565 (1991). doi:10.1016/0022-2836(91)90193-A. PubMed 2051488.

| Part | Content | Vault notes |
|---|---|---|
| Log-odds view | Any matrix implies a target distribution of aligned pairs | [[Substitution Matrix]], [[Logarithm]] |
| Information | Scores in bits; matrices compared by the information they carry | [[Kullback-Leibler Divergence]], [[Shannon Entropy]] |
| Choice of matrix | PAM120 generally for database searches; a more divergent PAM matrix for two specific, distantly related proteins | [[Substitution Matrix]], [[BLAST]] |

## How to use it

- L2: read the abstract with [[Substitution Matrix]].
- L3: read the derivation of the implied target frequencies after [[Kullback-Leibler Divergence]]; it prepares the statistics of [[E-Value]].

## Caveats

- Paid (Elsevier); a course-hosted copy exists but was not opened.
- Verified in this pass (web search): citation, DOI, PubMed number and the abstract's main claims (implicit log-odds matrices with a target distribution, scores in bits, different matrices for different purposes, PAM120 for database searches, PAM250 as the most widely used matrix at the time). The PAM number recommended for comparing two specific proteins could not be read reliably in the retrieved text (PAM200 or PAM250), and the paper's own term for the information per position was not confirmed.
