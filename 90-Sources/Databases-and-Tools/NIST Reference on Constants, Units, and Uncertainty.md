---
aliases:
  - CODATA
  - CODATA Recommended Values
  - NIST Fundamental Physical Constants
tags:
  - type/source
  - domain/physics
  - domain/chemistry
  - level/L1
  - level/L2
kind: database
tier: A
authors: []
institution: NIST Physical Measurement Laboratory
year: 2022
edition: "CODATA 2022 adjustment"
url: "https://physics.nist.gov/constants"
access: free
---

# NIST Reference on Constants, Units, and Uncertainty

> [!abstract]
> NIST's online reference for the CODATA recommended values of the fundamental physical constants, with their units and uncertainties, also distributed as printable "wallet cards" and full adjustment reports.

## Why this source

- The authoritative value of any constant a calculation needs (gas constant, Avogadro, Boltzmann, Faraday), with its uncertainty and the year of the adjustment.
- Since the 2019 revision of the SI, the Avogadro constant and the Boltzmann constant are exact by definition, so the molar gas constant $R = N_A k$ is exact too: code can hard-code all its digits.

## Coverage

Values checked (October 2026) on the CODATA 2022 and 2018 listings.

| Constant | Value | Vault notes |
|---|---|---|
| Molar gas constant $R$ | 8.314 462 618... J mol⁻¹ K⁻¹ (exact), $R = N_A k$ | [[Gibbs Free Energy]], [[Chemical Equilibrium]], [[Ideal Gas Law]] |
| Earlier values of $R$ | 8.314 4598(48) (2014), 8.314 472(15) (1998) J mol⁻¹ K⁻¹ | |

Cited in [[Enthalpy]], [[Gibbs Free Energy]], [[Chemical Equilibrium]], [[Le Chatelier's Principle]].

## How to use it

- Look up a constant by name on the site and copy the value with its units; cite the adjustment year.
- In code, keep constants in one place with a comment naming the CODATA adjustment.

## Caveats

- Values change between adjustments for constants that are not exact; record the year.
- The Avogadro constant (6.022 140 76 × 10²³ mol⁻¹) and the Boltzmann constant (1.380 649 × 10⁻²³ J K⁻¹) are fixed by the 2019 SI definition; only the gas constant's listing was checked on the NIST pages in this pass.
