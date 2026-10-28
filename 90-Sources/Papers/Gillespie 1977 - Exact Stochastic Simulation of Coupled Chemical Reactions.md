---
aliases:
  - Gillespie algorithm paper
  - Stochastic simulation algorithm
  - SSA
tags:
  - type/source
  - domain/chemistry
  - domain/computer-science
  - level/L3
  - level/M1
kind: paper
tier: A
authors:
  - Daniel T. Gillespie
journal: The Journal of Physical Chemistry
year: 1977
url: "https://doi.org/10.1021/j100540a008"
access: paid
---

# Gillespie 1977 - Exact Stochastic Simulation of Coupled Chemical Reactions

> [!abstract]
> The paper that made the stochastic simulation algorithm (the Gillespie algorithm) widely known: exact simulation of a well-mixed chemical system, drawing the waiting time to the next reaction from an exponential distribution and choosing which reaction fires in proportion to its propensity.

## Why this source

It is the primary reference for simulating reaction networks one molecular event at a time, as needed to study [[Stochastic Gene Expression]] and other systems with small copy numbers. The paper contrasts deterministic rate equations with the stochastic (master-equation) description of a spatially homogeneous system, argues that the stochastic view has the firmer physical basis, and notes that rate equations can miss fluctuations when molecule numbers are small. Its algorithm generates statistically exact trajectories of the underlying continuous-time Markov jump process.

## Coverage

Citation: Gillespie DT. "Exact stochastic simulation of coupled chemical reactions". *The Journal of Physical Chemistry* 81(25):2340-2361 (1977).

| Part | Content | Vault notes |
|---|---|---|
| Context | Deterministic rate equations versus the stochastic master equation for a well-mixed system | [[Reaction Kinetics]], [[Rate Law]] |
| Algorithm | Time step $\tau = (1/a_0)\ln(1/r_1)$ from the total propensity $a_0$ (an exponential waiting time); a second random number $r_2$ selects the reaction | [[Gillespie Algorithm]], [[Exponential Distribution]] |
| Output | Exact sample trajectories of a continuous-time Markov jump process | [[Continuous-Time Markov Chain]], [[Monte Carlo Method]] |

## How to use it

- L3: read the description of the algorithm with [[Exponential Distribution]] open, then implement a birth-death model of mRNA synthesis and decay and compare its stationary mean and variance.
- M1: compare stochastic trajectories with the deterministic rate equations at low and high copy numbers ([[Stochastic Gene Expression]]).

## Caveats

- An earlier paper by the same author (1976) is also cited for the method; it was not checked here.
- Verified in this pass: author, title, journal, volume, issue, pages, year, the contrast between rate equations and the master equation, and the algorithm's exponential time step and reaction selection (from a course-hosted copy of the paper). The DOI is consistent with the journal's records (volume 81, issue 25, first page 2340) but was not displayed verbatim by the sources checked.
