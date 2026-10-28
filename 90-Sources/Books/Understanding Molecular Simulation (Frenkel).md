---
aliases:
  - Frenkel and Smit
  - "Understanding Molecular Simulation: From Algorithms to Applications"
tags:
  - type/source
  - domain/physics
  - domain/chemistry
  - domain/computer-science
  - level/L3
  - level/M1
kind: book
tier: S
authors:
  - Daan Frenkel
  - Berend Smit
institution: Academic Press
year: 2002
edition: "2nd"
url: "https://educate.elsevier.com/book/details/9780122673511"
access: paid
---

# Understanding Molecular Simulation (Frenkel)

> [!abstract]
> The reference textbook on the statistical mechanics behind molecular dynamics and Monte Carlo simulation: which ensemble an algorithm samples, and how to compute averages and free energies from it.

## Why this source

It explains simulation algorithms from the statistical mechanics they must satisfy, rather than as recipes for one software package. It is the place to check what a thermostat, a barostat or a Monte Carlo move actually samples.

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| Part I Basics (chapter numbers not verified) | Statistical mechanics for simulation, Monte Carlo and molecular dynamics basics | [[Statistical Ensemble]], [[Molecular Dynamics Simulation]], [[Monte Carlo Method]] |
| Part II Ensembles: ch. 5 Monte Carlo Simulations in Various Ensembles | Sampling ensembles other than the canonical one | [[Statistical Ensemble]], [[Metropolis-Hastings Algorithm]] |
| Part II Ensembles: ch. 6 Molecular Dynamics in Various Ensembles | Molecular dynamics at constant temperature: the Andersen and Nosé-Hoover thermostats | [[Statistical Ensemble]], [[Molecular Dynamics Simulation]], [[Equipartition Theorem]] |
| Later parts (not verified) | Free energy calculations and advanced sampling | [[Partition Function]], [[Binding Free Energy]] |

## How to use it

- L3: Part II, to know which ensemble a simulation protocol samples.
- M1: the free-energy chapters before running alchemical or binding free energy calculations.

## Caveats

- Paid. Assumes undergraduate statistical mechanics and some programming.
- A 3rd edition (2023, ISBN 978-0-323-90292-2) renumbers the chapters ("Molecular Dynamics in Various Ensembles" becomes ch. 7); vault citations refer to the 2nd edition (2002, ISBN 0-12-267351-4).
- Verified in this pass by web search: authors, edition, publisher, ISBNs, the Part II chapter titles and numbers, and the constant-temperature subsections of ch. 6 (from publisher and bookseller listings). Other chapter numbers were not verified.
