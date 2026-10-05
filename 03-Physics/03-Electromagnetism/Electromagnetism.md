---
aliases:
  - Électromagnétisme
  - Electricity and Magnetism
tags:
  - type/moc
  - domain/physics
  - level/L1
  - level/L2
prerequisites:
  - "[[Mechanics]]"
  - "[[Calculus]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[MIT - Course 7 Biology]]"
---

# Electromagnetism

> [!abstract]
> Charges, fields, potentials and circuits, restricted to what explains membranes and ions in water, and the instruments that move charged molecules (electrophoresis, mass spectrometry) or read nuclear spins (NMR).

## Why it matters for bioinformatics

- **A membrane is an RC circuit.** The lipid bilayer is a [[Capacitance|capacitor]] and [[Ion Channel|ion channels]] are resistors: [[Membrane Potential]], [[Action Potential|action potentials]] and patch-clamp traces are circuit physics.
- **Electrostatics drives recognition.** [[Coulomb's Law]] interactions, screened by water ([[Dielectric Constant]]) and by salt ([[Debye Length]]), shape binding and DNA-protein contacts.
- **Separations use fields.** [[Gel Electrophoresis]] and capillary sequencers move DNA in an [[Electric Field]] ([[Electrophoretic Mobility]]).
- **Mass spectrometers steer ions.** [[Mass Spectrometry]] separates ions by mass-to-charge ratio with electric and magnetic forces ([[Lorentz Force]]).
- **NMR detects spins.** Nuclear magnetization precessing in a strong [[Magnetic Field]] induces the measured signal ([[Electromagnetic Induction]]).

## Before you start

- [[Mechanics]]: [[Newton's Laws of Motion]], [[Work (Physics)]], [[Potential Energy]].
- [[Calculus]]: [[Integral]], [[Gradient]]; [[Vector]].

## Learning path

> [!tip] What to skip compared with a full physics licence
> Maxwell's equations in full differential form and the derivation of electromagnetic waves (light is treated phenomenologically in [[Waves and Optics]]), Biot-Savart and Ampère calculations, inductance and AC circuits, electronics, magnetic materials, boundary-value problems and multipole expansions, and the link with relativity.

### Stage 1 - Foundations (L1)

1. [[Electric Charge]] (L1): use the elementary charge, conservation and quantization of charge; convert moles of charge with the Faraday constant. Bio: charges of ions, phosphates and side chains.
2. [[Coulomb's Law]] (L1): compute the force and the energy between point charges. Bio: salt bridges; repulsion between phosphates of the DNA backbone.
3. [[Electric Field]] (L1): compute and draw fields, including the uniform field between two plates. Bio: the field across an electrophoresis gel; ion acceleration in a mass spectrometer.
4. [[Electric Potential]] (L1): relate potential to field and potential energy ($qV$), use volts and electronvolts. Bio: membrane potentials in millivolts; $k_B T / e \approx 25$ mV at room temperature.
5. [[Electric Current]] (L1): define current as moving charge, including ionic currents in solution. Bio: currents through single channels, in picoamperes.
6. [[Ohm's Law]] (L1): relate current, voltage and resistance or conductance; combine resistors. Bio: single-channel conductance.
7. [[Capacitance]] (L1): compute charge and energy stored in a capacitor. Bio: the lipid bilayer as a capacitor of about 1 µF/cm².
8. [[Magnetic Field]] (L1): describe the sources and units (tesla) of magnetic fields. Bio: the superconducting magnets of NMR and MRI.
9. [[Lorentz Force]] (L1): compute the force on a moving charge and its circular motion in a magnetic field. Bio: mass analyzers separate ions by mass-to-charge ratio.

### Stage 2 - Core (L2)

10. [[Dielectric Constant]] (L2): explain screening by a polarizable medium; compare water with the low-polarity protein interior. Bio: why burying a charge inside a protein is costly.
11. [[Gauss's Law]] (L2): relate the flux of the field to the enclosed charge, and its differential form, the Poisson equation. Bio: the basis of continuum electrostatics ([[Poisson-Boltzmann Equation]]).
12. [[RC Circuit]] (L2): solve charging and discharging with the time constant $\tau = RC$. Bio: the passive response and time constant of a membrane.
13. [[Electrophoretic Mobility]] (L2): balance the electric force against drag to get a drift velocity $v = \mu E$. Bio: gel and capillary electrophoresis; why DNA separates by size only in a sieving gel.
14. [[Electromagnetic Induction]] (L2): apply Faraday's law of induction. Bio: how precessing nuclear magnetization produces the NMR signal.

## Uses from other domains

- [[Membrane Potential]], [[Ion Channel]], [[Goldman-Hodgkin-Katz Equation]], [[Hodgkin-Huxley Model]], [[Debye Length]] ([[Biophysics]]).
- [[Nernst Equation]] and [[Reduction Potential]] ([[Physical Chemistry]]): electrochemistry.
- [[Gel Electrophoresis]] and [[Mass Spectrometry]] ([[Biotechnology]]): separation by charge and by mass-to-charge ratio.
- [[Nuclear Magnetic Resonance Spectroscopy]] ([[Biophysics]]): spins in a magnetic field.

## Reference courses

No course source note yet for this subdomain; [[University Physics (OpenStax)]] Volume 2 covers it. MIT's corresponding subject is 8.02, part of its science core.[^mit7]

## Reference books

- [[University Physics (OpenStax)]]: Volume 2, electricity and magnetism part.[^up]

## Lab projects

No Lab project implements electromagnetism directly.

## References

Scope: MIT's science core pairs mechanics (8.01) with a second physics subject, 8.02; the other programs with a physics requirement are listed in [[Physics]].[^mit7] This MOC keeps the electrostatics and circuits needed by membranes and ions in solution and the magnetic forces used by mass spectrometry and NMR.

[^up]: [[University Physics (OpenStax)]], Volume 2: thermodynamics, electricity and magnetism.
[^mit7]: [[MIT - Course 7 Biology]]: GIR physics 8.01 and 8.02.
