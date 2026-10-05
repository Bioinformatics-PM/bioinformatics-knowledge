---
aliases:
  - Capacitor
  - Membrane Capacitance
  - Specific Membrane Capacitance
  - Capacité électrique
  - Condensateur
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Electric Charge]]"
  - "[[Electric Field]]"
  - "[[Electric Potential]]"
related:
  - "[[Dielectric Constant]]"
  - "[[Gauss's Law]]"
  - "[[RC Circuit]]"
  - "[[Electric Current]]"
  - "[[Ohm's Law]]"
  - "[[Membrane Potential]]"
  - "[[Lipid Bilayer]]"
  - "[[Cell Membrane]]"
  - "[[Order-of-Magnitude Estimation]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Phillips 2018 - Membranes by the Numbers]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Anatomy and Physiology 2e (OpenStax)]]"
---

# Capacitance

> [!abstract]
> A capacitor is two conductors separated by an insulator, and its capacitance is the charge it holds per volt; a cell membrane is one, a 5 nm insulating film between two salt solutions that stores about 1 µF per cm².

## Definition

A **capacitor** is a pair of conductors carrying equal and opposite charges $+Q$ and $-Q$. Its **capacitance** is the ratio of that charge to the potential difference $V$ between the conductors, $C = Q/V$, measured in farads ($1\ \text{F} = 1\ \text{C/V}$). It depends only on the geometry of the conductors and on the insulating material (dielectric) between them, not on $Q$ or $V$.[^up]

## Why it matters

- **A membrane is a capacitor.** The lipid bilayer is an insulator between two conducting ionic solutions, cytosol and extracellular fluid ([[Cell Membrane]]); its measured capacitance per area is typically about 1 µF/cm².[^phillips] It is a parameter of every electrical model of a cell ([[RC Circuit]], [[Hodgkin-Huxley Model]]).
- **Sanity checks on membrane potentials.** Capacitance converts a voltage into a number of ions moved. The count for a resting potential is tiny compared with the ions in the cell, which is why concentrations in the [[Nernst Equation]] do not change when the potential does ([[Membrane Potential]], [[Order-of-Magnitude Estimation]]).
- **Currents in recordings.** Whenever the membrane voltage changes, a capacitive current $C\,dV/dt$ flows in addition to the current through [[Ion Channel|ion channels]] (derived below); membrane models add the two.

## Core (L1)

**Charging.** Moving a charge $Q$ from one conductor to the other leaves $+Q$ on one and $-Q$ on the other: the capacitor as a whole stays neutral. The charge grows linearly with the voltage, $Q = CV$. One farad is enormous; practical capacitors are measured in µF, nF and pF.[^up]

**Parallel-plate capacitor.** Two plates of area $A$ a distance $d$ apart, with $d$ small compared with the plates, carry surface charge densities $\pm\sigma = \pm Q/A$. Between them the field is uniform, $E = \sigma/\varepsilon_0$ (a consequence of [[Gauss's Law]]), so the voltage is $V = Ed$ ([[Electric Field]], [[Electric Potential]]).[^up] Then

$$C = \frac{Q}{V} = \frac{\sigma A}{\sigma d/\varepsilon_0} = \frac{\varepsilon_0 A}{d}.$$

Filling the gap with an insulator of dielectric constant $\kappa$ reduces the field by the factor $\kappa$ at fixed charge, so $C = \kappa\varepsilon_0 A/d$ ([[Dielectric Constant]]).[^up] The vacuum permittivity is $\varepsilon_0 = 8.854\,187\,8188(14) \times 10^{-12}$ F m⁻¹.[^nist] Large plates, a thin gap and a polarizable insulator give a large capacitance.

![[capacitor-membrane-analogy.svg]]

**Energy.** Carrying a small charge $dq$ across the voltage $q/C$ already present costs $dW = (q/C)\,dq$. Summing from $0$ to $Q$:

$$U = \int_0^Q \frac{q}{C}\,dq = \frac{Q^2}{2C} = \frac{1}{2}CV^2 = \frac{1}{2}QV.$$

The factor $\tfrac12$ appears because the first charges cross a small voltage and only the last ones cross the full $V$.[^up]

## Deeper (L2)

**The bilayer as a parallel-plate capacitor.** The bilayer is about 5 nm thick,[^alberts] and the dielectric constant of its oily interior is about 2.[^phillips] Per unit area, $c_m = \kappa\varepsilon_0/d = 2 \times 8.854 \times 10^{-12}/(5 \times 10^{-9}) = 3.5 \times 10^{-3}$ F/m² $= 0.35$ µF/cm², against a measured value of about 1 µF/cm².[^phillips] The estimate has the right order of magnitude and is low by a factor of about 3. The formula says why: $c_m \propto 1/d$, and only the oily core is a low-$\kappa$ insulator, while the polar head groups on each face are hydrated ([[Lipid Bilayer]]).[^alberts] With $\kappa = 2$, an insulating layer of 1.8 nm would give the measured value (Exercise 3). Useful conversions: $1\ \mu\text{F/cm}^2 = 10^{-2}$ F/m² $= 0.01$ pF/µm².

**How many ions make a membrane potential?** A neuron at rest sits near $-70$ mV.[^ap] The charge per area on each face is $\sigma = c_m |V| = 10^{-2} \times 0.070 = 7 \times 10^{-4}$ C/m², that is $7 \times 10^{-16}$ C per µm², or $7 \times 10^{-16}/1.602 \times 10^{-19} \approx 4.4 \times 10^3$ monovalent ions per µm² (elementary charge from CODATA[^nist]). For a spherical cell of radius 10 µm (area $1.26 \times 10^{-9}$ m²), about $5.5 \times 10^6$ ions. The same cell holds about $3.5 \times 10^{11}$ K⁺ ions at the typical cytosolic 140 mM:[^alberts] charging the membrane moves about **1 ion in 60,000**. The bulk solutions stay electroneutral, the excess charge sits in thin layers against each face, and the concentrations are unchanged for all practical purposes ([[Membrane Potential]]). The field across the bilayer is large, though: $E = V/d = 0.070/(5 \times 10^{-9}) = 1.4 \times 10^7$ V/m.

**Capacitive current.** Differentiating $Q = CV$ gives $I = dQ/dt = C\,dV/dt$ ([[Electric Current]]). No charge crosses the insulator: charges pile up on one face while equal charges leave the other. At constant voltage this current is zero. Put in parallel with the conductance of channels ([[Ohm's Law]]), it makes the membrane an RC circuit with time constant $\tau = RC$ ([[RC Circuit]]).

**Combining capacitors.** In parallel the capacitances add, $C = \sum_i C_i$: membrane patches side by side add their areas, so a cell's capacitance is $c_m$ times its area. In series the inverses add, $1/C = \sum_i 1/C_i$: stacked layers, such as the head-group and core layers of a bilayer.[^up]

## Mathematical representation

$$C = \frac{Q}{V}, \qquad c_m = \frac{C}{A} = \frac{\kappa\varepsilon_0}{d}, \qquad U = \frac{1}{2}CV^2, \qquad I = C\,\frac{dV}{dt}, \qquad \frac{1}{c_\text{series}} = \sum_i \frac{d_i}{\kappa_i\varepsilon_0}$$

$Q$: charge on the positive conductor (C); $V$: potential difference (V); $C$: capacitance (F); $A$: area (m²); $d$: thickness of the insulator (m); $\kappa$: dielectric constant (dimensionless); $\varepsilon_0$: vacuum permittivity (F/m); $c_m$: capacitance per area (F/m²); $U$: stored energy (J); $I$: current (A).

**Ions moved.** Charging area $A$ to $|V|$ with ions of valence $z$ moves $N = c_m |V| A / (|z| e)$ ions (units: (F/m²)(V) = C/m², divided by C and multiplied by m², a pure number). For a sphere of radius $r$ holding an ion at concentration $c$ (mol/m³), the fraction moved is

$$\frac{N}{c\,N_A \cdot \frac{4}{3}\pi r^3} = \frac{3\,c_m |V|}{|z|\,e\,c\,N_A\,r} \propto \frac{1}{r}.$$

## Computational representation

```python
import math

EPS0 = 8.8541878188e-12   # F/m, vacuum electric permittivity (CODATA 2022)
E = 1.602176634e-19       # C, elementary charge (exact)
N_A = 6.02214076e23       # 1/mol, Avogadro constant (exact)


def c_per_area(kappa: float, d: float) -> float:
    """Parallel-plate capacitance per unit area, F/m^2 (d in m)."""
    return kappa * EPS0 / d


def uf_per_cm2(c: float) -> float:
    """Convert F/m^2 to uF/cm^2 (1 uF/cm^2 = 1e-2 F/m^2)."""
    return c / 1e-2


def ions_needed(c: float, v: float, area: float, z: int = 1) -> float:
    """Number of ions of valence z that charge `area` (m^2) to |v| volts."""
    return c * abs(v) * area / (abs(z) * E)


for d_nm in (5, 3, 2):
    print(f"kappa = 2, d = {d_nm} nm: {uf_per_cm2(c_per_area(2, d_nm * 1e-9)):.2f} uF/cm^2")
print(f"d giving 1 uF/cm^2 at kappa = 2: {2 * EPS0 / 1e-2 * 1e9:.2f} nm")

C_M, V = 1e-2, -0.070                      # measured 1 uF/cm^2; resting potential -70 mV
print(f"ions per um^2: {ions_needed(C_M, V, 1e-12):.0f}")
r = 10e-6                                  # spherical cell of radius 10 um (illustrative)
area, volume = 4 * math.pi * r**2, 4 / 3 * math.pi * r**3
n_moved = ions_needed(C_M, V, area)
n_k = 0.140 * volume * 1e3 * N_A           # 140 mM K+, volume converted to litres
print(f"moved {n_moved:.2e}, K+ inside {n_k:.2e}, fraction {n_moved / n_k:.1e}")
print(f"energy {0.5 * C_M * area * V**2:.2e} J, field {abs(V) / 5e-9:.1e} V/m")
```

```text
kappa = 2, d = 5 nm: 0.35 uF/cm^2
kappa = 2, d = 3 nm: 0.59 uF/cm^2
kappa = 2, d = 2 nm: 0.89 uF/cm^2
d giving 1 uF/cm^2 at kappa = 2: 1.77 nm
ions per um^2: 4369
moved 5.49e+06, K+ inside 3.53e+11, fraction 1.6e-05
energy 3.08e-14 J, field 1.4e+07 V/m
```

## Worked example

> [!example] Charging a spherical cell to −70 mV (radius 10 µm, illustrative)
> 1. **Area**: $A = 4\pi r^2 = 4\pi (10^{-5})^2 = 1.26 \times 10^{-9}$ m².
> 2. **Capacitance**: $C = c_m A = 10^{-2} \times 1.26 \times 10^{-9} = 1.26 \times 10^{-11}$ F $= 12.6$ pF.
> 3. **Charge**: $Q = C|V| = 1.26 \times 10^{-11} \times 0.070 = 8.8 \times 10^{-13}$ C, that is $8.8 \times 10^{-13}/1.602 \times 10^{-19} = 5.5 \times 10^6$ monovalent ions.
> 4. **Energy**: $U = \frac12 CV^2 = \frac12 \times 1.26 \times 10^{-11} \times 0.070^2 = 3.1 \times 10^{-14}$ J.
> 5. **Compare**: volume $4.19 \times 10^{-15}$ m³ $= 4.19 \times 10^{-12}$ L, times 0.140 mol/L times $N_A$: $3.5 \times 10^{11}$ K⁺. Fraction moved: $1.6 \times 10^{-5}$.

## Common misconceptions

> [!warning] "A charged capacitor contains charge"
> Its net charge is zero: $+Q$ on one conductor, $-Q$ on the other. What it stores is separated charge, hence energy $\frac12 CV^2$.

> [!warning] "At −70 mV the inside of the cell is negatively charged"
> Only a thin layer against the inner face carries excess anions, matched by excess cations outside. The bulk cytosol is electroneutral to about one part in $10^5$ (computed above).

> [!warning] "A higher voltage increases the capacitance"
> $C$ is fixed by geometry and material. A higher voltage stores more charge, $Q = CV$, with the same $C$.

> [!warning] "The stored energy is $QV$"
> It is $\frac12 QV$, because the voltage grows from 0 to $V$ during charging. When a battery charges a capacitor through a resistor, the battery supplies $QV$ and half of it is dissipated as heat.

## Exercises

> [!question] Exercise 1 (L1)
> A 10 µF capacitor is charged to 5.0 V. Find its charge and stored energy.

> [!success]- Solution
> $Q = CV = 10^{-5} \times 5.0 = 5.0 \times 10^{-5}$ C $= 50$ µC. $U = \frac12 CV^2 = \frac12 \times 10^{-5} \times 25 = 1.25 \times 10^{-4}$ J $= 125$ µJ.

> [!question] Exercise 2 (L1)
> Two plates of 1.0 cm² face each other 0.10 mm apart in air ($\kappa \approx 1$). Compute $C$, then $C$ after doubling the gap, and the field at 5.0 V in the first case.

> [!success]- Solution
> $C = \varepsilon_0 A/d = 8.854 \times 10^{-12} \times 10^{-4}/10^{-4} = 8.85 \times 10^{-12}$ F $= 8.85$ pF. Doubling $d$ halves it: 4.43 pF. $E = V/d = 5.0/10^{-4} = 5.0 \times 10^4$ V/m.

> [!question] Exercise 3 (L2)
> Model a bilayer as three layers in series: a hydrocarbon core of 3 nm with $\kappa = 2$ between two head-group layers of 1 nm with $\kappa = 20$ (invented values). Compute $c_m$ with and without the head groups, and the core thickness that alone gives 1 µF/cm².

> [!success]- Solution
> Series: $1/c = \sum d_i/(\kappa_i\varepsilon_0)$. Core alone: $d/\kappa = 1.5$ nm, $c = \varepsilon_0/1.5\ \text{nm} = 5.9 \times 10^{-3}$ F/m² $= 0.59$ µF/cm². With heads: $1.5 + 2 \times 0.05 = 1.6$ nm, $c = 0.55$ µF/cm². High-$\kappa$ layers add little "equivalent thickness": the low-$\kappa$ core dominates. For 1 µF/cm²: $d = \kappa\varepsilon_0/c = 2 \times 8.854 \times 10^{-12}/10^{-2} = 1.77$ nm.

> [!question] Exercise 4 (L2)
> During the rising phase of an action potential a membrane depolarizes by about 100 mV in 1 ms (round numbers). Compute the capacitive current per µm², then for a cell of 1000 µm², and compare with single-channel currents of a few pA.

> [!success]- Solution
> $I/A = c_m\,dV/dt = 10^{-2} \times (0.1/10^{-3}) = 1$ A/m² $= 10^{-12}$ A/µm² $= 1$ pA/µm². For 1000 µm²: 1 nA, the current of hundreds of open channels carrying a few pA each ([[Electric Current]], [[Action Potential]]).

> [!question] Exercise 5 (L3, Python)
> Using the fraction formula of the Mathematical representation, compute the fraction of K⁺ (140 mM) moved to charge spheres of radius 0.5, 5, 10 and 50 µm to 70 mV. Which compartments come closest to depleting their ions?

> [!success]- Solution
> ```python
> E, N_A = 1.602176634e-19, 6.02214076e23
>
> def fraction_moved(r, c_m=1e-2, v=0.070, conc=140.0):
>     """Fraction of ions (conc in mol/m^3) moved to charge a sphere of radius r (m)."""
>     return 3 * c_m * v / (r * E * conc * N_A)
>
> for r_um in (0.5, 5, 10, 50):
>     print(f"r = {r_um:>4} um: fraction {fraction_moved(r_um * 1e-6):.1e}")
> ```
> Output: `3.1e-04`, `3.1e-05`, `1.6e-05`, `3.1e-06`. The fraction scales as $1/r$ (area over volume), so the smallest compartments, such as thin processes and bacterium-sized cells, are the most sensitive, yet even at 0.5 µm only 0.03 % of the K⁺ moves.

## Mastery checklist

- [ ] 1 Recognized: I can define capacitance, its unit, and say that a membrane has about 1 µF/cm².
- [ ] 2 Understood: I can derive $C = \kappa\varepsilon_0 A/d$ and $U = \frac12 CV^2$, and explain why the bulk cytosol stays neutral.
- [ ] 3 Practiced: I can compute membrane capacitance, ions moved and capacitive currents with SI units, by hand and in Python.
- [ ] 4 Applied: I used the membrane capacitance to check a membrane potential or an action potential model ([[Hodgkin-Huxley Model]]).
- [ ] 5 Explained: I can teach why the parallel-plate estimate falls short of 1 µF/cm² and why the ion count is small yet the field is huge.

## References

[^up]: [[University Physics (OpenStax)]], Volume 2, treatment of capacitance (definition, parallel-plate capacitor, series and parallel combinations, stored energy, dielectrics) (chapter number not verified).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA 2022 values: vacuum electric permittivity $\varepsilon_0 = 8.854\,187\,8188(14) \times 10^{-12}$ F m⁻¹; elementary charge $e = 1.602\,176\,634 \times 10^{-19}$ C and Avogadro constant, both exact since the 2019 SI.
[^phillips]: [[Phillips 2018 - Membranes by the Numbers]], electrical properties of membranes (parallel-plate estimate with $d \approx 5$ nm and dielectric constant about 2; measured capacitance about 1 µF/cm²).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of membrane structure (bilayer about 5 nm thick, hydrophilic heads and hydrophobic tails) and ch. 11, Table 11-1 (cytosolic K⁺ about 140 mM in a typical mammalian cell).
[^ap]: [[Anatomy and Physiology 2e (OpenStax)]], treatment of the neuron's resting membrane potential (about −70 mV) (chapter not verified).
