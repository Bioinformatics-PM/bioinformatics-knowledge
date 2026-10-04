---
aliases:
  - Spring Constant
  - Stiffness
  - Force Constant
  - Loi de Hooke
tags:
  - type/concept
  - domain/physics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Newton's Laws of Motion]]"
  - "[[Work (Physics)]]"
  - "[[Potential Energy]]"
related:
  - "[[Harmonic Oscillator]]"
  - "[[Conservation of Energy]]"
  - "[[Force Field]]"
  - "[[Optical Tweezers]]"
  - "[[Equipartition Theorem]]"
  - "[[Boltzmann Distribution]]"
  - "[[Lennard-Jones Potential]]"
  - "[[Worm-Like Chain]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[Cornell 1995 - A Second Generation Force Field for the Simulation of Proteins, Nucleic Acids, and Organic Molecules]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Hooke's Law

> [!abstract]
> Pull a spring a little and it pulls back in proportion: $F = -kx$. This linear law, with its stored energy $\frac{1}{2}kx^2$, describes every system near a stable equilibrium, from chemical bonds to a bead held by a laser.

## Definition

**Hooke's law**: for small displacements $x$ from its rest position, a spring exerts a **restoring force** proportional to the displacement and opposite to it,

$$F = -kx,$$

where $k > 0$ is the **stiffness** or **force constant**, in N/m.[^up151] The work done to stretch it is stored as elastic potential energy $U = \tfrac{1}{2} k x^2$.[^up8]

## Why it matters

- **Force fields are made of springs.** Biomolecular force fields model bond stretching and angle bending with harmonic terms $K(r - r_{eq})^2$, whose parameters were fitted to vibrational frequencies and structures.[^cornell] A [[Molecular Dynamics Simulation]] of a protein integrates thousands of such springs ([[Force Field]]).
- **Optical traps are springs.** A bead held in a focused laser beam is pulled back toward the trap center in proportion to its displacement, so once the stiffness is known, measuring a displacement in nm measures a force in pN ([[Optical Tweezers]]).[^pboc]
- **Stiffness from fluctuations.** In thermal equilibrium a spring's fluctuations satisfy $\langle x^2 \rangle = k_B T / k$, which calibrates traps and links stiffness to statistics ([[Equipartition Theorem]]).

## Core (L1)

**Reading the law.** The minus sign says the force is opposite to the displacement: stretched ($x > 0$), the spring pulls back ($F < 0$); compressed ($x < 0$), it pushes ($F > 0$). Doubling the displacement doubles the force and quadruples the energy.

**Stored energy, derived.** Stretching slowly from 0 to $x$, you apply $+kx'$ at each extension $x'$; your work is $\int_0^x k x'\,dx' = \tfrac12 k x^2$, stored as potential energy ([[Work (Physics)]], [[Potential Energy]]). Conversely $F = -dU/dx = -kx$.

**Units at the molecular scale.** $1 \text{ pN/nm} = 10^{-12}\text{ N} / 10^{-9}\text{ m} = 10^{-3}$ N/m; energies in pN nm $= 10^{-21}$ J, compared with $k_B T = 4.28$ pN nm at 310 K.[^nist]

**Combining springs** (derivations). In **parallel** both springs share the displacement and the forces add: $k = k_1 + k_2$. In **series** they share the force and the extensions add: $x = F/k_1 + F/k_2$, so $1/k = 1/k_1 + 1/k_2$, and the softer spring dominates. A bead held by a trap and pulled through a soft molecular tether is a series combination.

## Deeper (L2)

**Hooke's law is the first term of any restoring force.** Near a minimum $x^*$ of a smooth potential, $F(x) = -U'(x) \approx -U''(x^*)(x - x^*)$: the stiffness is the curvature of the potential ([[Potential Energy]], [[Taylor Series]]). The figure shows how far this holds for an atomic contact described by a [[Lennard-Jones Potential]].

![[hookes-law-force-extension.svg]]

Within 1 % of the equilibrium distance the linear law is within about 10 %; beyond, the real attraction is weaker than predicted. The restoring force is largest, $2.69\,\varepsilon/r_m$, at $r = 1.109\,r_m$: a pull stronger than that has no equilibrium left, and the contact breaks. A spring never breaks; a bond does.

**The force field convention.** Force fields write the bond energy as $K_r(r - r_{eq})^2$, without the $\tfrac12$:[^cornell] the spring constant is $k = 2K_r$. Parameters are usually given in kcal mol⁻¹ Å⁻²; with 1 kcal = 4184 J and $N_A = 6.02214076 \times 10^{23}$ mol⁻¹,[^nist] $1$ kcal mol⁻¹ Å⁻² $= 0.6948$ N/m per bond (computed below).

**Thermal fluctuations.** At temperature $T$ the displacement of a spring has the Boltzmann density $p(x) \propto e^{-kx^2 / 2k_B T}$ ([[Boltzmann Distribution]]), a normal distribution of variance

$$\langle x^2 \rangle = \frac{k_B T}{k}, \qquad \text{equivalently} \qquad \left\langle \tfrac12 k x^2 \right\rangle = \tfrac12 k_B T.$$

Stiff springs barely move, soft ones wander. Inverting gives the **equipartition calibration** $k = k_B T / \langle x^2 \rangle$: record a trapped bead's positions, compute their variance, divide.

## Advanced (L3)

**Many coordinates.** Near a minimum of $U(\mathbf r_1, \dots, \mathbf r_N)$, the restoring forces are linear in all displacements, $\mathbf F = -\mathbf K\,\Delta\mathbf r$, where the stiffness matrix $\mathbf K$ is the [[Hessian Matrix]] of $U$. Its eigenvectors are independent directions of motion with stiffness given by the eigenvalues: the starting point of normal modes ([[Harmonic Oscillator#Advanced (L3)]]).

**Precision of a calibration.** The equipartition estimate inherits the sampling error of a variance: for $n$ independent normal samples, its relative standard deviation is close to $\sqrt{2/n}$ (Exercise 4). Successive positions of a real bead are correlated in time, so the number of independent samples is smaller than the number of recorded frames.

**Entropic springs.** A flexible polymer pulled by its ends loses conformational entropy; at small extension the restoring force is linear in the extension, with a stiffness proportional to $k_B T$, so it stiffens when heated, unlike a metal spring.[^pboc] The force-extension laws are the subject of [[Freely Jointed Chain]] and [[Worm-Like Chain]].

## Mathematical representation

- 1D: $F = -k(x - x_0)$, $U = \tfrac12 k (x - x_0)^2$, with $x_0$ the rest position (m), $k$ the stiffness (N/m), $F$ in N, $U$ in J; from any potential, $k = U''(x_0)$ at a minimum $x_0$.
- Thermal equilibrium: $x \sim \mathcal N(x_0, k_B T / k)$, $k_B = 1.380649 \times 10^{-23}$ J/K exact.[^nist]
- Several coordinates: $\mathbf F = -\mathbf K (\mathbf r - \mathbf r_0)$, $U = \tfrac12 (\mathbf r - \mathbf r_0)^\top \mathbf K (\mathbf r - \mathbf r_0)$, with $\mathbf K$ symmetric positive definite.

## Computational representation

The code simulates the positions of a trapped bead (invented data drawn from the Boltzmann distribution of an assumed trap), recovers the stiffness by equipartition, and applies the series and parallel rules.

```python
import math
import random

KB = 1.380649e-23                 # J/K, exact since the 2019 SI
KBT = KB * 310.0 / 1e-21          # thermal energy at 310 K in pN nm (1 pN nm = 1e-21 J)


def series(*ks: float) -> float:
    """Stiffness of springs joined end to end: 1/k = sum of 1/k_i."""
    return 1 / sum(1 / k for k in ks)


def parallel(*ks: float) -> float:
    """Stiffness of springs side by side: k = sum of k_i."""
    return sum(ks)


kappa_true = 0.05                 # pN/nm, assumed trap stiffness (illustrative)
sd = math.sqrt(KBT / kappa_true)  # Boltzmann: bead positions are Gaussian with variance kBT/kappa
rng = random.Random(1)
xs = [rng.gauss(0.0, sd) for _ in range(10_000)]          # simulated bead positions (invented data)
mean = sum(xs) / len(xs)
var = sum((x - mean) ** 2 for x in xs) / (len(xs) - 1)
print(f"kBT = {KBT:.2f} pN nm, rms excursion = {sd:.1f} nm")
print(f"estimated stiffness = kBT / var = {KBT / var:.4f} pN/nm (true {kappa_true})")
x = 20.0                          # nm
print(f"at x = {x:.0f} nm: F = {-kappa_true * x:.2f} pN, U = {0.5 * kappa_true * x**2:.1f} pN nm = {0.5 * kappa_true * x**2 / KBT:.2f} kBT")
print(f"series(0.05, 0.05) = {series(0.05, 0.05):.3f}, parallel(0.05, 0.05) = {parallel(0.05, 0.05):.3f} pN/nm")
print(f"1 kcal/mol/A^2 = {4184 / 6.02214076e23 / 1e-20:.4f} N/m")
```

```text
kBT = 4.28 pN nm, rms excursion = 9.3 nm
estimated stiffness = kBT / var = 0.0508 pN/nm (true 0.05)
at x = 20 nm: F = -1.00 pN, U = 10.0 pN nm = 2.34 kBT
series(0.05, 0.05) = 0.025, parallel(0.05, 0.05) = 0.100 pN/nm
1 kcal/mol/A^2 = 0.6948 N/m
```

## Worked example

> [!example] Reading a force from a trapped bead (assumed trap)
> A bead sits in a trap of stiffness $\kappa = 0.05$ pN/nm (assumed). A motor attached to it pulls it 20 nm from the center and holds it there.
>
> 1. **Force.** At rest the motor's pull balances the trap: $|F| = \kappa x = 0.05 \times 20 = 1.0$ pN ([[Newton's Laws of Motion]]).
> 2. **Energy stored in the trap.** $\tfrac12 \kappa x^2 = \tfrac12 \times 0.05 \times 400 = 10$ pN nm $= 10^{-20}$ J $= 2.3\,k_B T$ at 310 K.
> 3. **Thermal noise.** Without the motor the bead wanders with rms $\sqrt{k_B T/\kappa} = \sqrt{4.28/0.05} = 9.3$ nm. The 20 nm signal is about twice the noise: single readings are unreliable, averaging is required.
> 4. **Trade-off.** A stiffer trap reduces the noise ($\propto \kappa^{-1/2}$) but also the displacement produced by a given force ($\propto \kappa^{-1}$), so the force signal-to-noise ratio $\kappa x / \sqrt{\kappa k_B T} = F / \sqrt{\kappa\,k_B T}$ falls as the trap stiffens.

## Common misconceptions

> [!warning] "The force field constant is the spring constant"
> Force fields write $K_r (r - r_{eq})^2$ without the $\tfrac12$, so $k = 2K_r$.[^cornell] Mixing conventions gives frequencies off by $\sqrt 2$.

> [!warning] "A stiffer spring always stores more energy"
> At equal displacement, yes ($\tfrac12 kx^2$). At equal force, no: $U = F^2 / 2k$, so the softer spring stores more. In a series chain under tension, the softest element holds most of the energy.

## Exercises

> [!question] Exercise 1 (L1)
> A bead is held by a trap (0.05 pN/nm) and also tethered to the coverslip by a taut molecule (0.2 pN/nm), both assumed. (a) What stiffness resists a small displacement of the bead? (b) If you instead move the trap center and record the force at the anchor, what is the stiffness of the chain trap, bead, tether, anchor?

> [!success]- Solution
> (a) Moving the bead stretches both springs by the same amount: parallel, $0.05 + 0.2 = 0.25$ pN/nm. (b) The chain transmits one force through both elements and their extensions add: series, $1/(1/0.05 + 1/0.2) = 0.04$ pN/nm, below the softer element.

> [!question] Exercise 2 (L2)
> A force field lists a bond with $K_r = 500$ kcal mol⁻¹ Å⁻² (illustrative). Give the spring constant in N/m and the energy, in kJ/mol, of a 0.05 Å stretch.

> [!success]- Solution
> $k = 2K_r = 1000 \times 0.6948 = 695$ N/m. Energy $K_r \Delta r^2 = 500 \times 0.05^2 = 1.25$ kcal/mol $= 5.23$ kJ/mol, about $2\,RT$ at 310 K: thermal motion only stretches covalent bonds by hundredths of an ångström.

> [!question] Exercise 3 (L2)
> Using $\langle x^2 \rangle = k_B T / k$ at 310 K, compare the classical rms fluctuation of a 0.05 pN/nm trap and of a 1188 N/m C=O bond.

> [!success]- Solution
> Trap: $\sqrt{4.28 \times 10^{-21} / 5 \times 10^{-5}} = 9.3 \times 10^{-9}$ m $= 9.3$ nm. Bond: $\sqrt{4.28 \times 10^{-21} / 1188} = 1.9 \times 10^{-12}$ m $= 1.9$ pm, about 0.2 % of its length. The bond figure is only classical: its vibration is quantized and essentially frozen in the ground state at 310 K ([[Harmonic Oscillator#Deeper (L2)]]).

> [!question] Exercise 4 (L3, Python)
> How many independent position samples are needed to calibrate a trap to about 1 %? Simulate 200 calibrations for $n = 100$, 1000 and 10 000 samples and compare the relative spread of the estimates with $\sqrt{2/n}$.

> [!success]- Solution
> ```python
> import math
> import random
> import statistics
>
> KBT = 1.380649e-23 * 310.0 / 1e-21          # pN nm
>
>
> def estimate_kappa(n: int, kappa: float, rng: random.Random) -> float:
>     """Stiffness estimated as kBT / variance from n simulated bead positions (invented data)."""
>     xs = [rng.gauss(0.0, math.sqrt(KBT / kappa)) for _ in range(n)]
>     return KBT / statistics.variance(xs)
>
>
> rng = random.Random(2)
> for n in (100, 1000, 10000):
>     estimates = [estimate_kappa(n, 0.05, rng) for _ in range(200)]
>     cv = statistics.stdev(estimates) / statistics.mean(estimates)
>     print(f"n = {n:5d}: relative spread of the estimate = {cv:.3f}  (sqrt(2/n) = {math.sqrt(2 / n):.3f})")
> # n =   100: relative spread of the estimate = 0.149  (sqrt(2/n) = 0.141)
> # n =  1000: relative spread of the estimate = 0.045  (sqrt(2/n) = 0.045)
> # n = 10000: relative spread of the estimate = 0.013  (sqrt(2/n) = 0.014)
> ```
>
> The spread follows $\sqrt{2/n}$, so 1 % needs about 20 000 independent samples. Since successive frames of a real recording are correlated, the recording must be longer still.

## Mastery checklist

- [ ] 1 Recognized: I can write $F = -kx$ and $U = \tfrac12 kx^2$ and give the units of $k$ in N/m and pN/nm.
- [ ] 2 Understood: I can derive the stored energy, the series and parallel rules, and explain why every stable minimum obeys Hooke's law for small displacements.
- [ ] 3 Practiced: I can convert force-field constants to N/m, compute thermal fluctuations and calibrate a simulated trap by equipartition in Python.
- [ ] 4 Applied: I can read the bond and angle terms of a real force field file and estimate the stretch thermal motion produces.
- [ ] 5 Explained: I can teach the limits of the linear law (anharmonicity, rupture), the noise trade-off in force measurement, and the difference between energetic and entropic springs.

## References

[^up151]: [[University Physics (OpenStax)]], Volume 1, §15.1 "Simple Harmonic Motion" (restoring force proportional to the displacement, force constant $k$).
[^up8]: [[University Physics (OpenStax)]], Volume 1, ch. 8 "Potential Energy and Conservation of Energy" (elastic potential energy of a spring).
[^cornell]: [[Cornell 1995 - A Second Generation Force Field for the Simulation of Proteins, Nucleic Acids, and Organic Molecules]], *J. Am. Chem. Soc.* 117:5179-5197: harmonic bond and angle terms written $K(r - r_{eq})^2$; bonded parameters fitted to vibrational frequencies and structures.
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), treatment of optical traps as springs for force measurement and of the entropic elasticity of polymers (chapters not verified).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]]: Boltzmann constant $k_B = 1.380649 \times 10^{-23}$ J/K and Avogadro constant $N_A = 6.02214076 \times 10^{23}$ mol⁻¹, exact since the 2019 SI.
