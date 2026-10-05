---
aliases:
  - Fluorescent Protein Database
tags:
  - type/source
  - domain/biology
  - domain/physics
  - level/L1
  - level/L2
kind: database
tier: B
authors:
  - Talley J. Lambert
institution: Harvard Medical School
year: 2019
url: "https://www.fpbase.org"
access: free
---

# FPbase

> [!abstract]
> A free, community-editable database of fluorescent proteins: one page per protein with its lineage, mutations, excitation and emission spectra and photophysical properties, each value linked to the primary reference.

## Why this source

Textbooks name GFP and its variants but rarely give their spectra. FPbase gathers the excitation and emission maxima of each fluorescent protein in one place, with the paper each value comes from, which makes it the practical reference for choosing a laser line or a filter set.

## Coverage

Described in Lambert TJ, "FPbase: a community-editable fluorescent protein database", *Nature Methods* (2019).

| Part | Content | Vault notes |
|---|---|---|
| avGFP (wild-type *Aequorea victoria* GFP) | Excitation maximum 395 nm, emission maximum 509 nm | [[Photon]], [[Electromagnetic Spectrum]], [[Fluorescence]] |
| EGFP | Derived from avGFP by the mutations M1_S2insV/F64L/S65T/H231L; excitation maximum 488 nm, emission maximum 507 nm | [[Photon]], [[Electromagnetic Spectrum]], [[Fluorescence Microscopy]] |

Cited in [[Photon]], [[Electromagnetic Spectrum]].

## How to use it

- L1: read the excitation and emission maxima of a protein before computing photon energies or Stokes shifts.
- L2: compare spectra of several proteins to plan multichannel imaging ([[Fluorescence Microscopy]]).

## Caveats

- Community-edited: check the primary reference linked on each protein page before relying on a value.
- Only the avGFP and EGFP values above were verified (through search records of the FPbase pages, October 2026); the Nature Methods volume and pages were not re-checked.
