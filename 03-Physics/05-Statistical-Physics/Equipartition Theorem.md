---
aliases:
  - Equipartition of Energy
  - Equipartition
  - Théorème d'équipartition
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Boltzmann Distribution]]"
  - "[[Partition Function]]"
  - "[[Temperature]]"
  - "[[Kinetic Energy]]"
  - "[[Harmonic Oscillator]]"
  - "[[Normal Distribution]]"
related:
  - "[[Heat Capacity]]"
  - "[[Ideal Gas Law]]"
  - "[[Molecular Dynamics Simulation]]"
  - "[[Statistical Ensemble]]"
  - "[[Optical Tweezers]]"
  - "[[Brownian Motion]]"
  - "[[Langevin Equation]]"
  - "[[Hooke's Law]]"
  - "[[Force Field]]"
  - "[[Gamma Distribution]]"
  - "[[Covariance Matrix]]"
  - "[[Hessian Matrix]]"
  - "[[Molecular Motor]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[Neuman 2004 - Optical Trapping]]"
  - "[[Understanding Molecular Simulation (Frenkel)]]"
  - "[[Svoboda 1994 - Force and Velocity Measured for Single Kinesin Molecules]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Equipartition Theorem

> [!abstract]
> In thermal equilibrium, every independent quadratic term of a classical energy, such as $\frac12 mv_x^2$ or $\frac12\kappa x^2$, holds on average $\frac12 k_BT$, whatever the mass or the stiffness. Counting these terms gives heat capacities, the temperature of a molecular dynamics simulation, and the stiffness of an optical trap from the jiggling of a bead.

## Definition

For a classical system in equilibrium at temperature $T$, each independent coordinate or momentum $q$ that enters the energy only through a quadratic term $aq^2$ has mean energy
$$\langle a q^2\rangle = \tfrac12 k_BT,$$
independent of $a$. A molecule with $f$ such terms has mean energy $\frac f2 k_BT$ and contributes $\frac f2 k_B$ to the heat capacity.[^up2]

## Why it matters

- **Temperature in molecular dynamics.** A simulation has no thermometer: its temperature is computed from the kinetic energy and the number of degrees of freedom, which constraints change ([[Molecular Dynamics Simulation]]).[^frenkel]
- **Calibrating an optical trap.** The thermal motion of a trapped bead gives the trap stiffness, $\kappa = k_BT/\langle x^2\rangle$, and with it every force measured on a motor or an unfolding protein ([[Optical Tweezers]]).[^neuman]
- **The size of thermal motions.** Any coordinate held by an effective spring of stiffness $\kappa$ fluctuates by $\sqrt{k_BT/\kappa}$: a bead, a cantilever, or the softest collective motions of a protein (Advanced).
- **Heat capacities**, and why stiff bond vibrations do not contribute at room temperature ([[Heat Capacity]], [[Harmonic Oscillator#Deeper (L2)]]).

## Core (L2)

### Where one half kT comes from

Take one coordinate with energy $aq^2$. Its [[Boltzmann Distribution]] is $p(q) \propto e^{-aq^2/k_BT}$, a [[Normal Distribution]] with variance $\sigma^2 = k_BT/2a$. Hence
$$\langle aq^2\rangle = a\sigma^2 = \tfrac12 k_BT.$$
The stiffness cancels: a stiff spring has a smaller amplitude ($\sigma \propto a^{-1/2}$) but exactly the same mean energy. With $\beta = 1/k_BT$, the same result follows from the [[Partition Function]] $Z = \int e^{-\beta aq^2}dq = \sqrt{\pi/\beta a}$: $\langle aq^2\rangle = -\partial_\beta\ln Z = \frac{1}{2\beta}$. Independent terms add, so energy is shared equally among all quadratic degrees of freedom: hence "equipartition".

### Counting quadratic degrees of freedom

| System | Quadratic terms | Mean energy | $C_V$ per molecule |
|---|---|---|---|
| Atom of a gas (translation) | $\frac12 mv_x^2, \frac12 mv_y^2, \frac12 mv_z^2$ | $\frac32 k_BT$ | $\frac32 k_B$ |
| Rigid diatomic molecule | 3 translations + 2 rotations | $\frac52 k_BT$ | $\frac52 k_B$ |
| Rigid nonlinear molecule (rigid water model) | 3 translations + 3 rotations | $3k_BT$ | $3k_B$ |
| Classical harmonic vibration | kinetic + potential | $k_BT$ | $k_B$ |
| Atom in a harmonic solid | 3 kinetic + 3 potential | $3k_BT$ | $3k_B$ |
| Bead in a trap, one axis | $\frac12 mv_x^2 + \frac12\kappa x^2$ | $k_BT$ | $k_B$ |

The gas rows are the kinetic-theory heat capacities, per mole $\frac32 R$ and $\frac52 R$;[^up2] the translational row is the definition of temperature for a dilute gas ([[Temperature#Core (L1)]]).

### When it fails

- **Quantum freezing.** Equipartition assumes the energy levels are closely spaced compared with $k_BT$. A bond stretch has a quantum $hf$ several times $k_BT$ and stays in its ground state, contributing nothing to $C_V$ ([[Harmonic Oscillator#Deeper (L2)]]). Low-frequency motions (torsions, collective modes, a trapped bead) are classical.
- **Non-quadratic energies.** A torsion with barriers, a hard wall or an anharmonic well do not hold $\frac12 k_BT$; the generalized theorem (Advanced) gives the correct average.
- **Out of equilibrium.** A driven system (a motor consuming ATP, a bead dragged through the fluid) need not share its energy equally ([[Nonequilibrium Steady State]]).

### Bio: temperature in molecular dynamics

A simulation knows only velocities. With $N$ atoms, $N_c$ holonomic constraints (fixed bond lengths, rigid water) and a conserved total momentum, the number of quadratic kinetic degrees of freedom is $N_{df} = 3N - N_c - 3$, and equipartition defines the **instantaneous kinetic temperature**[^frenkel]
$$T_{\text{inst}} = \frac{2K}{N_{df}\,k_B}, \qquad K = \sum_i \tfrac12 m_i\lVert\mathbf v_i\rVert^2.$$
Its average is the temperature; its fluctuations, $\sqrt{2/N_{df}}$ in relative terms, are part of the canonical ensemble ([[Statistical Ensemble]], and for unconstrained atoms [[Temperature#Advanced (L3)]]). Counting $N_{df}$ wrongly biases every reported temperature: with rigid water, three of the nine atomic coordinates of each molecule are removed (Worked example).

### Bio: calibrating an optical trap

![[optical-trap-equipartition.svg]]

A focused laser holds a dielectric bead near its focus with a restoring force that is linear for small displacements, $F = -\kappa x$: a harmonic potential $\frac12\kappa x^2$ on each axis ([[Hooke's Law]]).[^neuman] Recording the thermal positions of the bead and applying equipartition gives the stiffness without knowing the laser power, the bead size or the viscosity:
$$\tfrac12\kappa\langle x^2\rangle = \tfrac12 k_BT \quad\Rightarrow\quad \kappa = \frac{k_BT}{\langle x^2\rangle}.$$
Forces then follow from displacements, $F = \kappa x$. The method needs a position detector calibrated in nanometers: because $\kappa \propto 1/\langle x^2\rangle$, a 10 % error in the detector gain becomes a 21 % error in $\kappa$, and anything that removes variance (a detector that low-pass filters the signal) or adds it (drift, noise) biases $\kappa$ (Computational representation). The complementary power-spectrum method uses the dynamics of the bead as well ([[Langevin Equation]], [[Brownian Motion]]).[^neuman]

## Advanced (L3)

- **Generalized equipartition.** For any coordinate $x_i$ whose Boltzmann weight vanishes at the ends of its range, integration by parts gives $\langle x_i\,\partial E/\partial x_j\rangle = \delta_{ij}k_BT$. For $E = aq^2$ this is $\langle 2aq^2\rangle = k_BT$, the usual result; for a quartic well $E = ax^4$ it gives $\langle E\rangle = \frac14 k_BT$; for a linear potential $E = mgz$ above a floor, $\langle E\rangle = k_BT$ (Exercise 3). Summed over all coordinates, the same identity is the virial theorem.
- **Many coupled coordinates.** Near a minimum, $E \approx \frac12\mathbf x^{\mathsf T}\mathbf K\mathbf x$ with $\mathbf K$ the [[Hessian Matrix]] of the energy. The Boltzmann distribution is then a multivariate normal with [[Covariance Matrix]] $\langle\mathbf x\mathbf x^{\mathsf T}\rangle = k_BT\,\mathbf K^{-1}$: each normal mode (eigenvector of $\mathbf K$, [[Eigenvalues and Eigenvectors]]) holds $\frac12 k_BT$ of potential energy, so the softest modes, with the smallest eigenvalues, dominate the fluctuations. This is the logic of any harmonic (normal-mode) description of a flexible molecule (Exercise 5).
- **A diagnostic for simulations.** At equilibrium every degree of freedom holds $\frac12 k_BT$ of kinetic energy, so the kinetic temperatures of any subsets of atoms (protein and solvent, light and heavy atoms) must agree. A persistent difference signals a thermostat, constraint or integration artifact.
- **Kinetic energy is gamma-distributed.** $K/k_BT$ is a sum of $N_{df}$ independent squared normals divided by two, a [[Gamma Distribution]] with shape $N_{df}/2$: mean $N_{df}/2$, variance $N_{df}/2$, hence the relative fluctuation $\sqrt{2/N_{df}}$ of $T_{\text{inst}}$.

## Mathematical representation

- Energy $E = \sum_{k=1}^{f} a_k q_k^2 + E'$, with $E'$ independent of the $q_k$: $\langle a_kq_k^2\rangle = \frac12 k_BT$ for each $k$, so $\langle E - E'\rangle = \frac f2 k_BT$ and $C_V = \frac f2 k_B$.
- Generalized: $\langle x_i\,\partial_{x_j}E\rangle = \delta_{ij}\,k_BT$.
- Harmonic trap, one axis: $\langle x^2\rangle = k_BT/\kappa$; $p(x) = \mathcal N(0, k_BT/\kappa)$.
- Quadratic form: $E = \frac12\mathbf x^{\mathsf T}\mathbf K\mathbf x$ gives $\langle\mathbf x\mathbf x^{\mathsf T}\rangle = k_BT\,\mathbf K^{-1}$.
- MD: $T_{\text{inst}} = 2K/(N_{df}k_B)$, $N_{df} = 3N - N_c - 3$; $K/k_BT \sim \text{Gamma}(N_{df}/2, 1)$, relative fluctuation $\sqrt{2/N_{df}}$.

## Computational representation

A trapped bead is simulated with the exact update of a particle diffusing in a harmonic well (an Ornstein-Uhlenbeck process, see [[Langevin Equation]]), sampled every 0.02 ms, then calibrated by equipartition; the detector errors of the Core section are added one at a time:

```python
import random
from math import exp, sqrt

kT = 4.116                      # pN nm at 25 C
kappa = 0.05                    # true trap stiffness, pN/nm (invented)
tau, dt = 0.2e-3, 0.02e-3       # bead relaxation time and sampling interval, s (invented)
sd = sqrt(kT / kappa)           # equilibrium standard deviation of x, nm
rng = random.Random(7)
a = exp(-dt / tau)
x, xs = 0.0, []
for _ in range(200_000):        # exact update of a bead diffusing in a harmonic trap
    x = a * x + sd * sqrt(1 - a * a) * rng.gauss(0, 1)
    xs.append(x)


def stiffness(positions):
    """Equipartition: kappa = kT / <x^2>, with the variance about the mean position."""
    m = sum(positions) / len(positions)
    var = sum((p - m) ** 2 for p in positions) / (len(positions) - 1)
    return kT / var


print(f"true {kappa}, estimated {stiffness(xs):.4f} pN/nm")
print(f"detector gain 10 % too high: {stiffness([1.1 * p for p in xs]):.4f}")
for tau_f in (0.02e-3, 0.2e-3):            # first-order low-pass filter in the detector
    b = exp(-dt / tau_f)
    y, ys = 0.0, []
    for p in xs:
        y = b * y + (1 - b) * p
        ys.append(y)
    print(f"filter {tau_f * 1e3:.2f} ms: {stiffness(ys):.4f}")
drift = [p + 5.0 * i / len(xs) for i, p in enumerate(xs)]   # slow 5 nm drift added
print(f"5 nm drift: {stiffness(drift):.4f}")
```

```text
true 0.05, estimated 0.0508 pN/nm
detector gain 10 % too high: 0.0420
filter 0.02 ms: 0.0551
filter 0.20 ms: 0.1021
5 nm drift: 0.0495
```

The clean estimate is 1.6 % high although 200,000 positions were recorded: consecutive samples are correlated over the relaxation time, so they are worth far fewer independent ones (Exercise 4). A filter as slow as the bead itself halves the variance and doubles $\kappa$; drift adds variance and lowers it. The constant 4.116 pN nm is $k_BT$ at 25 °C from the exact Boltzmann constant.[^nist]

## Worked example

> [!example] Two calibrations by equipartition (invented numbers)
> **Trap.** A bead's position along $x$ has standard deviation 8.0 nm at 22 °C.
> 1. $k_BT = 1.380649\times 10^{-23} \times 295.15 = 4.075\times 10^{-21}$ J $= 4.075$ pN nm.[^nist]
> 2. $\kappa = k_BT/\langle x^2\rangle = 4.075/64 = 0.0637$ pN/nm.
> 3. A 50 nm displacement means a force of $0.0637 \times 50 = 3.2$ pN. Kinesin moves against loads up to 5-6 pN,[^svoboda] which this trap reaches at displacements of 79 to 94 nm: the linear-force assumption must be checked over that range.
> 4. Precision: the relative standard error of a variance from $M$ independent samples is $\sqrt{2/M}$, so a 1 % calibration needs about 20,000 samples spaced by more than the bead's relaxation time.
>
> **Simulation.** 1000 rigid water molecules (3000 atoms, 3 constraints each) at 300 K.
> 1. $N_{df} = 3 \times 3000 - 3000 - 3 = 5997$, i.e. 6 per molecule: 3 translations and 3 rotations.
> 2. Dividing $2K/k_B$ by $3N = 9000$ instead would report $300 \times 5997/9000 = 200$ K: a 100 K error from bookkeeping alone.
> 3. Expected fluctuation of $T_{\text{inst}}$: $\sqrt{2/5997} = 1.83\,\%$, about $\pm 5.5$ K.

## Common misconceptions

> [!warning] "Each atom gets one half kT"
> Each quadratic **degree of freedom** does: an atom's translation alone holds $\frac32 k_BT$, and a classical vibration $k_BT$ (kinetic plus potential).

> [!warning] "A stiffer spring stores more thermal energy"
> It stores exactly $\frac12 k_BT$, like a soft one; it fluctuates less. That is why the variance of a bead measures the stiffness.

> [!warning] "Equipartition applies to every bond at room temperature"
> Bond stretches are quantum oscillators frozen in their ground state ([[Harmonic Oscillator]]); classical force fields that constrain them lose nothing, and equipartition must not count them.

> [!warning] "The thermostat setting is the simulation's temperature"
> The reported temperature is computed from velocities with an assumed $N_{df}$; miscounting constraints gives a systematically wrong value, and a correct thermostat setting does not fix it.

## Exercises

> [!question] Exercise 1 (L2)
> Compute the mean translational kinetic energy and the root-mean-square speed of a 50 kDa protein at 37 °C ($1\ \text{Da} = 1.660539\times 10^{-27}$ kg[^nist]). Does the result depend on the protein's shape?

> [!success]- Solution
> $\langle K\rangle = \frac32 k_BT = 1.5 \times 4.282\times 10^{-21} = 6.42\times 10^{-21}$ J. $m = 50{,}000 \times 1.6605\times 10^{-27} = 8.30\times 10^{-23}$ kg, so $v_{\text{rms}} = \sqrt{3k_BT/m} = 12.4$ m/s. No: equipartition depends only on mass and temperature. The protein does not travel at that speed for long: collisions randomize its velocity constantly, and its displacement grows by diffusion ([[Brownian Motion]]).

> [!question] Exercise 2 (L2)
> A trap has $\kappa = 0.05$ pN/nm at 25 °C. What is the thermal standard deviation of the bead position? Which displacement corresponds to the 6 pN upper load of a kinesin motor?[^svoboda]

> [!success]- Solution
> $\sigma = \sqrt{k_BT/\kappa} = \sqrt{4.116/0.05} = 9.07$ nm. $x = F/\kappa = 6/0.05 = 120$ nm, thirteen thermal standard deviations: the force signal stands far above thermal noise.

> [!question] Exercise 3 (L3)
> Prove the generalized equipartition theorem $\langle x\,\partial E/\partial x\rangle = k_BT$ for one coordinate, then compute $\langle E\rangle$ for $E = ax^4$ and for $E = mgz$ with $z \ge 0$.

> [!success]- Solution
> $\int x\,E'(x)\,e^{-\beta E}dx = -k_BT\int x\,d(e^{-\beta E}) = -k_BT\big[x e^{-\beta E}\big] + k_BT\int e^{-\beta E}dx$; the bracket vanishes (the weight is zero at infinity, and $x = 0$ at the floor), so dividing by $Z$ gives $k_BT$. For $ax^4$: $xE' = 4E$, so $\langle E\rangle = k_BT/4$. For $mgz$: $zE' = E$, so $\langle E\rangle = k_BT$, the mean of the exponential (barometric) distribution. Only quadratic terms give exactly $\frac12 k_BT$.

> [!question] Exercise 4 (L3, Python)
> Repeat an equipartition calibration 300 times with $M = 100$, 1000 and 10,000 independent positions ($\kappa = 0.05$ pN/nm). Compare the relative spread of the estimates with $\sqrt{2/M}$.

> [!success]- Solution
> ```python
> import random
> from math import sqrt
> from statistics import mean, stdev
>
> kT, kappa = 4.116, 0.05
> sd = sqrt(kT / kappa)
> rng = random.Random(3)
> for m in (100, 1_000, 10_000):
>     estimates = []
>     for _ in range(300):                       # 300 repeated calibrations
>         xs = [rng.gauss(0, sd) for _ in range(m)]
>         estimates.append(kT / (sum(v * v for v in xs) / m))
>     print(m, round(mean(estimates), 4), round(stdev(estimates) / mean(estimates), 4), round(sqrt(2 / m), 4))
> ```
>
> ```text
> 100 0.051 0.1552 0.1414
> 1000 0.05 0.0472 0.0447
> 10000 0.05 0.0148 0.0141
> ```
>
> The spread follows $\sqrt{2/M}$, the relative standard error of a variance; with 100 samples the estimate is also biased upward (0.051), because $1/\langle x^2\rangle$ is a convex function of a noisy variance. Correlated samples count less than independent ones, as in the Computational representation.

> [!question] Exercise 5 (L3)
> Two beads, each attached to a wall by a spring $\kappa$ and to each other by a spring $\kappa$, move along one axis: $E = \frac{\kappa}{2}\left[x_1^2 + (x_2 - x_1)^2 + x_2^2\right]$. Find $\langle x_1^2\rangle$ and $\langle x_1x_2\rangle$, and the mean potential energy of each normal mode.

> [!success]- Solution
> $E = \frac12\mathbf x^{\mathsf T}\mathbf K\mathbf x$ with $\mathbf K = \kappa\begin{pmatrix}2 & -1\\ -1 & 2\end{pmatrix}$, so $\langle\mathbf x\mathbf x^{\mathsf T}\rangle = k_BT\,\mathbf K^{-1} = \frac{k_BT}{3\kappa}\begin{pmatrix}2 & 1\\ 1 & 2\end{pmatrix}$: $\langle x_1^2\rangle = \frac{2k_BT}{3\kappa}$ and $\langle x_1x_2\rangle = \frac{k_BT}{3\kappa}$, positively correlated. The normal modes are $x_1 + x_2$ (in phase, eigenvalue $\kappa$) and $x_1 - x_2$ (out of phase, $3\kappa$); each holds $\frac12 k_BT$ of potential energy, and the softer in-phase mode contributes three times more to the fluctuations.

## Mastery checklist

- [ ] 1 Recognized: I can state that each quadratic degree of freedom holds $\frac12 k_BT$ and give $\frac32 k_BT$ for translation.
- [ ] 2 Understood: I can derive the result from a Gaussian integral, count degrees of freedom for molecules and solids, and say when equipartition fails.
- [ ] 3 Practiced: I can calibrate a simulated trap from bead positions and compute $N_{df}$ and $T_{\text{inst}}$ for a constrained simulation.
- [ ] 4 Applied: I can check the temperature log of a real simulation and estimate the stiffness, the force scale and the calibration error of an optical trap dataset.
- [ ] 5 Explained: I can teach the generalized theorem, the covariance $k_BT\,\mathbf K^{-1}$ of coupled coordinates, and the detector pitfalls of equipartition calibration.

## References

[^up2]: [[University Physics (OpenStax)]], Volume 2, ch. 2 "The Kinetic Theory of Gases" (heat capacity and equipartition of energy; heat capacities of monatomic and diatomic gases).
[^frenkel]: [[Understanding Molecular Simulation (Frenkel)]], 2nd ed. (2002), treatment of molecular dynamics (instantaneous temperature from the kinetic energy and the number of degrees of freedom).
[^neuman]: [[Neuman 2004 - Optical Trapping]], *Review of Scientific Instruments* 75(9):2787-2809 (calibration of trap stiffness from thermal motion: equipartition and power spectrum).
[^svoboda]: [[Svoboda 1994 - Force and Velocity Measured for Single Kinesin Molecules]], *Cell* 77(5):773-784 (kinesin moves against loads up to 5-6 pN).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA values of the Boltzmann constant (exact) and of the atomic mass constant.
