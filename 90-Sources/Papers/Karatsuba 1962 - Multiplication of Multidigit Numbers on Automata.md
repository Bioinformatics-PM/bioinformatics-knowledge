---
aliases:
  - Karatsuba-Ofman paper
  - Karatsuba multiplication paper
tags:
  - type/source
  - domain/computer-science
  - domain/mathematics
  - level/L2
kind: paper
tier: S
authors:
  - A. Karatsuba
  - Yu. Ofman
journal: Doklady Akademii Nauk SSSR
year: 1962
url: "https://www.mathnet.ru/eng/dan26729"
access: partial
---

# Karatsuba 1962 - Multiplication of Multidigit Numbers on Automata

> [!abstract]
> The two-page note that introduced Karatsuba multiplication: two $n$-digit numbers multiplied with three half-size products instead of four, hence fewer than $n^2$ digit operations.

## Why this source

It is the original statement of the divide-and-conquer trick that every algorithms course uses to show that a clever combine step changes the exponent of a recurrence: $\Theta(n^{\log_2 3})$ instead of $\Theta(n^2)$. Textbooks present the algorithm more clearly; this note is the primary source for its origin.

## Coverage

Citation: Karatsuba A, Ofman Yu. *Doklady Akademii Nauk SSSR* 145(2):293-294 (1962), in Russian. English translation: *Soviet Physics Doklady* 7:595-596 (1963).

| Part | Content | Vault notes |
|---|---|---|
| Method | Splitting each factor in two halves and recovering the middle coefficient from one extra product | [[Divide and Conquer]] |
| Cost | Fewer than $n^2$ digit operations for $n$-digit numbers | [[Master Theorem]], [[Big O Notation]] |

## How to use it

- L2: read the treatment of integer multiplication in [[Coursera Stanford - Algorithms Specialization]] (course 1) first, then use this note as the historical reference when citing the algorithm.

## Caveats

- Verified in this pass: citation metadata (volume 145, issue 2, pages 293-294, 1962; English translation in volume 7, pages 595-596, 1963) on Math-Net.Ru and in lecture notes citing it. One encyclopedia page gives volume 146, which the other sources contradict.
- The English title varies between catalogues ("Multiplication of Multidigit Numbers on Automata", "Multiplication of many-digital numbers by automatic computers").
- Full-text open access of the Russian original was not verified; the translation journal is a paid archive.
