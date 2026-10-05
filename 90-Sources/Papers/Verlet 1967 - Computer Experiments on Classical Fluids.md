---
aliases:
  - Verlet 1967
  - "Computer \"Experiments\" on Classical Fluids. I. Thermodynamical Properties of Lennard-Jones Molecules"
tags:
  - type/source
  - domain/physics
  - domain/bioinformatics
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Loup Verlet
journal: Physical Review
year: 1967
url: "https://doi.org/10.1103/PhysRev.159.98"
access: paid
---

# Verlet 1967 - Computer Experiments on Classical Fluids

> [!abstract]
> The founding molecular dynamics paper that simulated Lennard-Jones particles by integrating Newton's equations with the scheme now called Verlet integration.

## Why this source

Landmark of computer simulation: the integration scheme it introduced (and the neighbor list now named after Verlet) is the ancestor of the integrators used in molecular dynamics of proteins and nucleic acids.

## Coverage

Citation: Verlet L. "Computer 'Experiments' on Classical Fluids. I. Thermodynamical Properties of Lennard-Jones Molecules." *Physical Review* 159:98-103 (1967). doi:10.1103/PhysRev.159.98

| Part | Content | Vault notes |
|---|---|---|
| Method | Step-by-step integration of Newton's equations of motion for interacting particles | [[Newton's Laws of Motion]], [[Molecular Dynamics Simulation]] |
| System | Particles interacting through a Lennard-Jones potential | [[Lennard-Jones Potential]] |

## How to use it

- L2: cite it for the origin of the Verlet integrator; learn the algorithm itself from [[Newton's Laws of Motion]] and the [[Euler Method]] comparison.
- L3: read it as history of molecular simulation before [[Molecular Dynamics Simulation]].

## Caveats

- Paywalled (American Physical Society).
- Details beyond the title, the method and the system (number of particles, state points) were not verified in this pass.
