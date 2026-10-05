---
aliases:
  - NIST isotopic compositions
  - Atomic Weights and Isotopic Compositions with Relative Atomic Masses
tags:
  - type/source
  - domain/chemistry
  - domain/physics
  - level/L1
  - level/L2
kind: database
tier: A
authors: []
institution: NIST Physical Measurement Laboratory
year:
edition:
url: "https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions-relative-atomic-masses"
access: free
---

# NIST Atomic Weights and Isotopic Compositions

> [!abstract]
> NIST's reference table of the relative atomic mass and natural isotopic composition of every isotope, with the standard atomic weight of each element (elements 1 to 118).

## Why this source

- The values that mass spectrometry software uses for monoisotopic and average masses, in one free table per element, with uncertainties.
- Traceable: atomic weights from the IUPAC report *Atomic Weights of the Elements 2013* (Meija et al.) and isotopic compositions from *Isotopic Compositions of the Elements 2009* (Berglund and Wieser), as stated by the database.
- Relative atomic masses are on the scale $A_r(^{12}\text{C}) = 12$ exactly, for a neutral atom in its ground state.

## Coverage

Values checked (October 2026) for the elements of life; uncertainty on the last digits in parentheses.

| Isotope | Relative atomic mass | Isotopic composition (mole fraction) | Vault notes |
|---|---|---|---|
| ¹H | 1.00782503223(9) | 0.999885(70) | [[Isotope]], [[Monoisotopic Mass]] |
| ²H | 2.01410177812(12) | 0.000115(70) | [[Isotope]] |
| ¹²C | 12 (exact, by definition) | 0.9893(8) | [[Isotope]], [[Atom]] |
| ¹³C | 13.00335483507(23) | 0.0107(8) | [[Isotope]], [[Mass Spectrometry]] |
| ¹⁴N | 14.00307400443(20) | 0.99636(20) | [[Isotope]] |
| ¹⁵N | 15.00010889888(64) | 0.00364(20) | [[Isotope]], [[DNA Replication]] |
| ¹⁶O | 15.99491461957(17) | 0.99757(16) | [[Isotope]] |
| ¹⁷O | 16.99913175650(69) | 0.00038(1) | [[Isotope]] |
| ¹⁸O | 17.99915961286(76) | 0.00205(14) | [[Isotope]] |
| ³¹P | 30.97376199842(70) | 1 | [[Isotope]] |
| ³²S | 31.9720711744(14) | 0.9499(26) | [[Isotope]] |
| ³³S | 32.9714589098(15) | 0.0075(2) | [[Isotope]] |
| ³⁴S | 33.967867004(47) | 0.0425(24) | [[Isotope]] |
| ³⁶S | 35.96708071(20) | 0.0001(1) | [[Isotope]] |

Standard atomic weight of hydrogen: interval [1.00784, 1.00811].

## How to use it

- L1: read one element page to see that an element is a mixture of isotopes ([[Isotope]]).
- L2: take monoisotopic masses from the "Relative Atomic Mass" column and abundances from the "Isotopic Composition" column when coding [[Monoisotopic Mass]] or isotope envelope calculators.

## Caveats

- Isotopic compositions are "representative" values: natural abundances vary between sources (hence the IUPAC intervals for the standard atomic weights of H, C, N, O and S). Do not treat the fourth decimal of an average mass as a constant of nature.
- The site (physics.nist.gov) could not be fetched from the verification environment; the values above were cross-checked through search-engine extracts of the element pages, not by downloading the full table. Standard atomic weight intervals were verified for hydrogen only.
- Authors and edition (version number) of the database not verified.
