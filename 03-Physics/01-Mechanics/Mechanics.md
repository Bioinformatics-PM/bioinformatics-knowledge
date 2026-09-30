---
aliases:
  - Mécanique
  - Classical Mechanics
tags:
  - type/moc
  - domain/physics
  - level/L1
  - level/L2
prerequisites:
  - "[[Calculus]]"
projects: []
sources:
  - "[[MIT 8.01SC - Classical Mechanics]]"
  - "[[University Physics (OpenStax)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[Meselson 1958 - The Replication of DNA in Escherichia coli]]"
---

# Mechanics

> [!abstract]
> The minimal classical mechanics for biology: units and estimates, Newton's laws, energy and potential energy, springs and oscillators, then motion in viscous fluids and centrifugation, where molecules and cells actually live.

## Why it matters for bioinformatics

- **Simulations integrate Newton's laws.** [[Molecular Dynamics Simulation|Molecular dynamics]] moves every atom with [[Newton's Laws of Motion]]; forces are minus the gradient of a [[Potential Energy]].
- **Springs are everywhere.** [[Hooke's Law]] and the [[Harmonic Oscillator]] model bond stretching in force fields, molecular vibrations and optical traps.
- **Cells live in syrup.** At low [[Reynolds Number]] inertia is negligible and drag dominates ([[Stokes' Law]]): this sets how proteins diffuse and bacteria swim.
- **Centrifuges prepare samples.** Cell fractionation, density gradients and sedimentation coefficients (70S and 80S ribosomes) are mechanics.
- **Units catch bugs.** [[Dimensional Analysis]] detects errors in any quantitative pipeline.

## Before you start

- [[Calculus]] Stage 1: [[Derivative]], [[Integral]]; [[Gradient]] for item 7 at L2.
- [[Vector]] at the level of components and dot product (from [[Linear Algebra]] or Calculus Volume 3).

## Learning path

> [!tip] What to skip compared with a full physics licence
> Rotational dynamics (torque, moment of inertia, angular momentum), gravitation and orbits, projectile problems, non-inertial frames beyond centrifugation, statics of rigid bodies, Lagrangian and Hamiltonian mechanics, special relativity, and most of fluid mechanics (Bernoulli, turbulence). Come back to Hamiltonian mechanics only if you use Hamiltonian Monte Carlo.

### Stage 1 - Foundations (L1)

1. [[Dimensional Analysis]] (L1): carry SI units through every calculation, convert units and check an equation by its dimensions. Bio: nM and µM, pN, nm, energies in units of $k_B T$.
2. [[Kinematics]] (L1): describe position, velocity and acceleration as derivatives of one another. Bio: speeds of motors and polymerases.
3. [[Newton's Laws of Motion]] (L1): draw free-body diagrams and solve $F = ma$ problems. Bio: the equations integrated by molecular dynamics.
4. [[Momentum]] (L1): use conservation of momentum in collisions and impulse. Bio: molecular collisions behind gas pressure.
5. [[Work (Physics)]] (L1): compute work as force times displacement, including work against pressure. Bio: work done by a molecular motor per step.
6. [[Kinetic Energy]] (L1): relate kinetic energy to speed and to work (work-energy theorem). Bio: temperature measures the average kinetic energy of molecules.
7. [[Potential Energy]] (L1): read potential energy curves, get the force as minus the gradient, find equilibria at minima. Bio: bond potentials and energy landscapes.
8. [[Conservation of Energy]] (L1): solve problems by energy conservation and account for dissipation as heat.
9. [[Hooke's Law]] (L1): model a spring with $F = -kx$ and energy $\frac{1}{2}kx^2$. Bio: bond stretching terms in force fields; optical-trap stiffness.
10. [[Harmonic Oscillator]] (L1): solve simple and damped harmonic motion; frequency from stiffness and mass. Bio: molecular vibrations seen by infrared spectroscopy; normal modes of proteins.
11. [[Pressure]] (L1): define pressure as force per area; hydrostatic pressure. Bio: osmotic and turgor pressure, blood pressure.

### Stage 2 - Core (L2)

12. [[Viscosity]] (L2): define viscosity and the drag force it produces on a moving object. Bio: why friction dominates at the molecular scale.
13. [[Stokes' Law]] (L2): compute the drag on a sphere, $F = 6\pi\eta r v$, and a friction coefficient. Bio: sedimentation, and the Stokes-Einstein estimate of diffusion coefficients.
14. [[Reynolds Number]] (L2): compare inertial and viscous forces; reason about life at low Reynolds number. Bio: bacterial swimming; a protein stops as soon as the force stops.
15. [[Centrifugation]] (L2): compute centrifugal acceleration (g-force from speed and radius) and interpret sedimentation coefficients in Svedberg units. Bio: cell fractionation, density-gradient separation of DNA,[^meselson] 70S and 80S ribosomes.

## Uses from other domains

- [[Molecular Dynamics Simulation]] and [[Force Field]] ([[Structural Bioinformatics]]): Newton's laws, potential energy, springs.
- [[Stokes-Einstein Relation]] and [[Molecular Motor]] ([[Biophysics]]): drag and work at low Reynolds number.
- [[Thermodynamics]]: work, energy conservation and pressure are its starting point.
- [[Density Gradient Centrifugation]] ([[Biotechnology]]): the lab technique built on [[Centrifugation]].

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 8.01SC - Classical Mechanics]] | MIT | L1 | Kinematics, forces, energy and momentum conservation (items 2 to 8); torque and angular momentum are skippable here[^801] |

## Reference books

- [[University Physics (OpenStax)]]: Volume 1 (mechanics and oscillations) for Stage 1.[^up]
- [[Physical Biology of the Cell (Phillips)]]: ch. 1 "Why: Biology by the Numbers" for the estimation habit behind item 1.[^pboc]

## Lab projects

No Lab project implements mechanics directly.

## References

Scope: introductory mechanics is part of the first physics course of every program with a physics requirement in the benchmark (see [[Physics]]); 8.01SC teaches both the force route and the conservation-law route, and for bioinformatics the energy and momentum parts matter most, as the entry point to statistical physics.[^801] Stage 2 is a choice of this vault: it keeps only the fluid mechanics that molecules and cells need.

[^801]: [[MIT 8.01SC - Classical Mechanics]]: course description (kinematics, forces, momentum, energy, torque and angular momentum) and study advice.
[^up]: [[University Physics (OpenStax)]], Volume 1: mechanics, sound, oscillations and waves.
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed., ch. 1 "Why: Biology by the Numbers".
[^meselson]: [[Meselson 1958 - The Replication of DNA in Escherichia coli]]: DNA separated by density in a cesium chloride gradient by ultracentrifugation.
