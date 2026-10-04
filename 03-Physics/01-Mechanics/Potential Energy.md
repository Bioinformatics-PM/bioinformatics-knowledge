---
aliases:
  - Potential Energy Curve
  - Potential Energy Surface
  - PES
  - Énergie potentielle
tags:
  - type/concept
  - domain/physics
  - domain/chemistry
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Work (Physics)]]"
  - "[[Kinetic Energy]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Derivative]]"
related:
  - "[[Conservation of Energy]]"
  - "[[Hooke's Law]]"
  - "[[Harmonic Oscillator]]"
  - "[[Gradient]]"
  - "[[Chemical Bond]]"
  - "[[Intermolecular Force]]"
  - "[[Lennard-Jones Potential]]"
  - "[[Force Field]]"
  - "[[Free Energy Landscape]]"
  - "[[Boltzmann Distribution]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[MIT 8.01SC - Classical Mechanics]]"
  - "[[Intermolecular and Surface Forces (Israelachvili)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Cornell 1995 - A Second Generation Force Field for the Simulation of Proteins, Nucleic Acids, and Organic Molecules]]"
---

# Potential Energy

> [!abstract]
> Potential energy is energy stored in the arrangement of a system; its curve tells you the forces: they push downhill, with a strength equal to the slope, and the system can rest at the bottom of a valley.

## Definition

For a **conservative force**, one whose work between two points does not depend on the path taken, the **potential energy** difference is minus that work: $\Delta U = U_B - U_A = -W_{A \to B}$. Only differences are defined, so the zero of $U$ is a choice. Conversely the force follows from the potential, $F_x = -\,dU/dx$ in one dimension. Gravity and ideal springs are conservative; friction is not.[^up8][^801]

## Why it matters

- **Force fields are potential energies.** A molecular mechanics force field is one function $U(\mathbf r_1, \dots, \mathbf r_N)$ of all atomic coordinates, a sum of bond, angle, torsion, Lennard-Jones and Coulomb terms with parameters fitted to structures, vibrational frequencies and interaction energies.[^cornell] [[Molecular Dynamics Simulation]] obtains every force as minus its gradient, and energy minimization searches for its minima ([[Force Field]]).
- **Bonds are potential energy curves.** Bond length and bond energy are the position and the depth of a minimum ([[Chemical Bond]]); contact distances in a protein core sit at the minimum of a [[Lennard-Jones Potential]] ([[Intermolecular Force]]).
- **The scale is $k_B T$.** A molecular energy matters only relative to the thermal energy $k_B T$, which also sets how often each minimum is occupied ([[Boltzmann Distribution]]).[^pboc] At 310 K, $k_B T = 1.380649 \times 10^{-23} \times 310 = 4.28 \times 10^{-21}$ J $= 4.28$ pN nm.[^nist]
- **Landscapes.** Folding, binding and conformational change are pictured as motion on an energy surface with valleys (states) and passes (barriers); its thermodynamic version is the [[Free Energy Landscape]].

## Core (L1)

**Two potentials to know**, each derived from $\Delta U = -W$ ([[Work (Physics)]]):[^up8]

| System | $U$ | Force $F = -dU/dx$ |
|---|---|---|
| mass $m$ at height $y$ near the ground | $mgy$ | $F_y = -mg$ (downward) |
| spring of stiffness $k$ stretched by $x$ | $\tfrac{1}{2} k x^2$ | $F = -kx$ ([[Hooke's Law]]) |

**Reading a potential energy curve** $U(x)$:[^up84]

1. **The slope gives the force.** $F = -dU/dx$ points downhill; its magnitude is the steepness, not the height. A high but flat region exerts no force.
2. **Equilibria are where the slope is zero**: $dU/dx = 0$ means $F = 0$.
3. **A minimum is stable, a maximum unstable.** Displaced from a minimum, the system feels a force back toward it; displaced from a maximum, a force away from it.
4. **Turning points.** With total energy $E = K + U$ and $K \ge 0$, motion is confined to where $U(x) \le E$; where $U = E$ the speed is zero and the motion reverses ([[Conservation of Energy]]).

![[lennard-jones-harmonic-approximation.svg]]

The figure plots the Lennard-Jones potential between two atoms in contact, in units of its depth $\varepsilon$ and of the position $r_m$ of its minimum: a steep repulsive wall, a minimum, then an attraction that fades to zero ([[Intermolecular Force]]).[^israel] A covalent bond curve reads the same way ([[Chemical Bond]]), with a much deeper well.

**Units.** Potential energy is in joules (J = N m). At the molecular scale use pN nm ($10^{-21}$ J), kJ/mol (multiply by the Avogadro constant) and multiples of $k_B T$.

## Deeper (L2)

**Three dimensions.** For $U(x, y, z)$, the force is minus the [[Gradient]]:[^up8]

$$\mathbf F = -\nabla U = -\left(\frac{\partial U}{\partial x}, \frac{\partial U}{\partial y}, \frac{\partial U}{\partial z}\right).$$

$\mathbf F$ is perpendicular to the contour lines of $U$ and points along the steepest descent. Equilibria satisfy $\nabla U = \mathbf 0$; an equilibrium is a stable minimum when the [[Hessian Matrix]] of second derivatives is positive definite.

**Conservative means path independent.** The work around any closed loop is zero, which is what makes $U$ well defined; Exercise 5 shows a force without a potential.[^up8]

**Every minimum looks like a spring.** Expanding $U$ about a minimum $x^*$ ([[Taylor Series]]), $U'(x^*) = 0$ removes the linear term:

$$U(x) \approx U(x^*) + \tfrac{1}{2} k (x - x^*)^2, \qquad k = U''(x^*) > 0.$$

Small displacements therefore obey [[Hooke's Law]] and oscillate harmonically ([[Harmonic Oscillator]]). For the Lennard-Jones contact $k = 72\varepsilon / r_m^2$ (derived below). The figure shows the limits: the parabola is symmetric and never levels off, whereas the real curve is softer on the stretched side (anharmonic) and lets the atoms separate.

## Advanced (L3)

**Potential energy surfaces.** A molecule of $N$ atoms has a potential energy over $3N$ coordinates, and the force on atom $i$ is $\mathbf F_i = -\nabla_i U$. Force fields build this surface from harmonic bond and angle terms, periodic torsion terms, and Lennard-Jones and Coulomb terms between nonbonded pairs.[^cornell] Each step of a simulation evaluates $-\nabla U$ for every atom; energy minimization follows $-\nabla U$ downhill ([[Gradient Descent]]) and stops in the nearest local minimum, not necessarily the lowest.

**From potential energy to free energy.** At temperature $T$ a molecule does not sit at its minimum: it visits configurations with probability proportional to $e^{-U/k_B T}$ ([[Boltzmann Distribution]]).[^pboc] A wide, shallow valley can then be more populated than a narrow, deep one because it contains more configurations. Projected onto one coordinate, this gives a free energy profile that includes entropy ([[Free Energy Landscape]]); barrier heights in units of $k_B T$ set how often transitions occur ([[Activation Energy]], [[Transition State Theory]]).

**Tilting a landscape.** A constant pulling force $F$ adds $-Fx$ to the potential: the landscape tilts, barriers shrink, and above a critical force a minimum disappears (worked example, Exercise 4). Single-molecule experiments pull on molecules with piconewton forces in exactly this way ([[Optical Tweezers]]).[^pboc]

## Mathematical representation

- Definition: $U(\mathbf r_B) - U(\mathbf r_A) = -\int_{\mathbf r_A}^{\mathbf r_B} \mathbf F \cdot d\mathbf r$, independent of the path for a conservative $\mathbf F$; conversely $\mathbf F = -\nabla U$.
- Equilibrium: $\nabla U(\mathbf r^*) = \mathbf 0$. In one dimension, stable if $U''(x^*) > 0$, unstable if $U''(x^*) < 0$.
- Lennard-Jones potential, in two equivalent forms:[^israel]

$$U(r) = 4\varepsilon\left[\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^{6}\right] = \varepsilon\left[\left(\frac{r_m}{r}\right)^{12} - 2\left(\frac{r_m}{r}\right)^{6}\right], \qquad r_m = 2^{1/6}\sigma,$$

 with $r$ the distance between the atoms (m), $\varepsilon$ the well depth (J), $\sigma$ the distance where $U = 0$.
- Derivation: $U'(r) = \frac{12\varepsilon}{r}\left[\left(\frac{r_m}{r}\right)^{6} - \left(\frac{r_m}{r}\right)^{12}\right]$ vanishes at $r = r_m$, where $U = -\varepsilon$; differentiating again, $U''(r_m) = \frac{\varepsilon}{r_m^2}(156 - 84) = \frac{72\,\varepsilon}{r_m^2}$.
- Reduced units $x = r/r_m$, $u = U/\varepsilon$ make the curve parameter free: $u(x) = x^{-12} - 2x^{-6}$, $u''(1) = 72$.

## Computational representation

A potential is a function; the force is its negative derivative, computed analytically or checked by a central [[Finite Difference]]. Comparing the two is a cheap test of any hand-written force routine.

```python
def lj(x: float) -> float:
    """Lennard-Jones energy in reduced units: x = r / r_m, result in units of the depth epsilon."""
    return x**-12 - 2 * x**-6


def lj_force(x: float) -> float:
    """Analytic force F = -dU/dx in units of epsilon / r_m."""
    return 12 * (x**-13 - x**-7)


def force_numeric(u, x: float, h: float = 1e-6) -> float:
    """Force as minus the central-difference derivative of the potential u."""
    return -(u(x + h) - u(x - h)) / (2 * h)


def harmonic(x: float) -> float:
    """Second-order Taylor expansion of lj about x = 1, with k = U''(1) = 72."""
    return -1 + 0.5 * 72 * (x - 1) ** 2


for x in (0.95, 1.0, 1.2):
    print(f"x = {x:4.2f}  F numeric = {force_numeric(lj, x):+8.4f}  F analytic = {lj_force(x):+8.4f}")

xs = [0.9 + 1e-4 * i for i in range(6001)]          # grid from 0.9 to 1.5
x_min = min(xs, key=lj)
h = 1e-4
k = (lj(x_min + h) - 2 * lj(x_min) + lj(x_min - h)) / h**2
print(f"minimum at x = {x_min:.4f}, U = {lj(x_min):.4f}, curvature U'' = {k:.2f}")

for x in (0.97, 0.99, 1.01, 1.03, 1.10, 1.30):
    print(f"x = {x:4.2f}  LJ = {lj(x):+7.3f}  harmonic = {harmonic(x):+7.3f}")
```

```text
x = 0.95  F numeric =  +6.1926  F analytic =  +6.1926
x = 1.00  F numeric =  +0.0000  F analytic =  +0.0000
x = 1.20  F numeric =  -2.2274  F analytic =  -2.2274
minimum at x = 1.0000, U = -1.0000, curvature U'' = 72.00
x = 0.97  LJ =  -0.960  harmonic =  -0.968
x = 0.99  LJ =  -0.996  harmonic =  -0.996
x = 1.01  LJ =  -0.997  harmonic =  -0.996
x = 1.03  LJ =  -0.974  harmonic =  -0.968
x = 1.10  LJ =  -0.810  harmonic =  -0.640
x = 1.30  LJ =  -0.371  harmonic =  +2.240
```

The force is positive (repulsive) on the wall and negative (attractive) beyond $r_m$. The harmonic model is within 1 % of $\varepsilon$ for displacements of 3 % of $r_m$, already off by 17 % of $\varepsilon$ at 10 %, and absurd at 30 %.

## Worked example

> [!example] A two-state switch as a double well (invented toy model)
> A protein loop switches between two conformations along a coordinate $x$ (nm). Model: $U(x) = \Delta U_b\left[(x/x_0)^2 - 1\right]^2$ with barrier $\Delta U_b = 5\,k_B T$ and $x_0 = 1$ nm, at 310 K ($k_B T = 4.28$ pN nm, so $\Delta U_b = 21.4$ pN nm).
>
> 1. **Equilibria.** $U'(x) = \frac{4\Delta U_b}{x_0}\frac{x}{x_0}\left[\left(\frac{x}{x_0}\right)^2 - 1\right] = 0$ at $x = 0$ and $x = \pm x_0$.
> 2. **Stability.** $U''(x) = \frac{4\Delta U_b}{x_0^2}\left[3\left(\frac{x}{x_0}\right)^2 - 1\right]$: at $\pm x_0$, $U'' = 8\Delta U_b/x_0^2 > 0$ (two stable states); at $0$, $U'' = -4\Delta U_b/x_0^2 < 0$ (the barrier top, unstable).
> 3. **Stiffness of each state.** $k = 8 \times 21.4 = 171$ pN/nm: near each minimum the loop behaves as a spring ([[Hooke's Law]]).
> 4. **Largest force on the way over.** $|F|$ is maximal where $U'' = 0$, at $x = \pm x_0/\sqrt 3$: $|F|_{max} = \frac{8\Delta U_b}{3\sqrt 3\, x_0} = 33$ pN. A pull stronger than this removes the barrier (Exercise 4).
> 5. **Energy scale.** The barrier, 21.4 pN nm $= 2.14 \times 10^{-20}$ J per molecule, is 12.9 kJ/mol; the Boltzmann weight of the barrier top relative to a minimum is $e^{-5} = 1/148$.

## Common misconceptions

> [!warning] "The force is largest where the potential energy is highest"
> The force is the slope, $-dU/dx$. At the top of a barrier the energy is maximal and the force is zero; the largest force is on the steepest flank.

> [!warning] "Potential energy has an absolute value"
> Only differences are physical. Adding a constant to $U$ changes no force and no motion. The zero is a convention (the ground for gravity, infinite separation for Lennard-Jones), and two programs may use different ones.

> [!warning] "A molecule sits at its energy minimum"
> At 310 K it fluctuates around the minimum with energies of order $k_B T$ and occasionally crosses barriers; the occupancy of each valley follows the Boltzmann weights, and entropy can favor a shallow, wide valley ([[Free Energy Landscape]]).

> [!warning] "Energy minimization finds the native structure"
> It follows the gradient into the nearest local minimum of a model potential, which depends on the starting point and ignores entropy unless the model includes it.

## Exercises

> [!question] Exercise 1 (L1)
> A particle moves on a line in the potential $U(x) = 3x^2 - 2x^3$ ($U$ in J, $x$ in m). Find the force, the equilibria and their stability. Up to what energy does a particle starting near $x = 0$ stay trapped?

> [!success]- Solution
> $F = -U'(x) = -6x + 6x^2 = 6x(x - 1)$ N. Equilibria at $x = 0$ and $x = 1$ m. $U''(x) = 6 - 12x$: $U''(0) = 6 > 0$, stable; $U''(1) = -6 < 0$, unstable. The barrier is $U(1) - U(0) = 1$ J: with total energy below 1 J the particle oscillates around $x = 0$, between turning points where $U(x) = E$.

> [!question] Exercise 2 (L1)
> Two atoms interact through the Lennard-Jones potential and have total energy $E = -0.5\varepsilon$. Find the turning points, and compare with the harmonic approximation.

> [!success]- Solution
> Set $y = (r_m/r)^6$: $y^2 - 2y = -0.5$ gives $y = 1 \pm \sqrt{0.5}$, so $r = y^{-1/6} r_m$ = $0.915\,r_m$ and $1.227\,r_m$. Harmonic: $36(x - 1)^2 = 0.5$ gives $x = 1 \pm 0.118$, i.e. $0.882\,r_m$ and $1.118\,r_m$ (open circles in the figure). The real motion extends further on the stretched side, so the average distance grows with energy; the parabola misses this asymmetry.

> [!question] Exercise 3 (L2)
> Derive $r_m = 2^{1/6}\sigma$ from the $\sigma$ form of the Lennard-Jones potential, then compute the stiffness $k = 72\varepsilon/r_m^2$ of a contact with illustrative parameters $\varepsilon = 0.4$ kJ/mol and $r_m = 3.5$ Å. Compare with a C=O bond (about 1190 N/m, [[Harmonic Oscillator]]).

> [!success]- Solution
> $U'(r) = 4\varepsilon\left[-12\sigma^{12}r^{-13} + 6\sigma^6 r^{-7}\right] = 0$ gives $r^6 = 2\sigma^6$, so $r_m = 2^{1/6}\sigma$. Per pair, $\varepsilon = 400 / 6.022 \times 10^{23} = 6.64 \times 10^{-22}$ J, so $k = 72 \times 6.64 \times 10^{-22} / (3.5 \times 10^{-10})^2 = 0.39$ N/m, about 3000 times softer than a covalent C=O stretch. Nonbonded contacts are the soft directions of a molecule.

> [!question] Exercise 4 (L3, Python)
> Tilt the double well of the worked example by a pulling force $F$ toward $+x$: $U_F(x) = U(x) - Fx$. Find numerically the smallest force (to 0.1 pN) at which the left minimum disappears, and compare with $8\Delta U_b / (3\sqrt 3\, x_0)$.

> [!success]- Solution
> ```python
> def has_left_minimum(force_pn: float, barrier_kbt: float = 5.0, x0: float = 1.0, kbt: float = 4.28) -> bool:
>     """True if U(x) - F x still has a local minimum on the left side (energies in pN nm, x in nm)."""
>     def u(x):
>         return barrier_kbt * kbt * ((x / x0) ** 2 - 1) ** 2 - force_pn * x
>     vals = [u(-2 + 0.001 * i) for i in range(2001)]           # x from -2 to 0 nm
>     return any(vals[i] < vals[i - 1] and vals[i] < vals[i + 1] for i in range(1, len(vals) - 1))
>
>
> f = 0.0
> while has_left_minimum(f):
>     f += 0.1
> print(f"left well disappears at F = {f:.1f} pN; analytic {8 * 5 * 4.28 / (3 * 3 ** 0.5):.1f} pN")
> # left well disappears at F = 33.0 pN; analytic 32.9 pN
> ```
>
> The tilted slope $U'(x) - F$ keeps a zero in the left well only while $F$ is below the maximum of $U'$ on the barrier flank, reached at $x = -x_0/\sqrt 3$: the force at which the state disappears is the largest restoring force of step 4 (the grid answer is the first 0.1 pN step above 32.95 pN).

> [!question] Exercise 5 (L3)
> Compute the work of $\mathbf F_1 = (-x, -y)$ and of $\mathbf F_2 = (-y, x)$ (in N, coordinates in m) once around the unit circle, counterclockwise. Which one has a potential energy? Give it.

> [!success]- Solution
> Parametrize $x = \cos t$, $y = \sin t$, $d\mathbf r = (-\sin t, \cos t)\,dt$. For $\mathbf F_1$: $\mathbf F_1 \cdot d\mathbf r = (\cos t \sin t - \sin t \cos t)\,dt = 0$, so $W = 0$; it derives from $U = \tfrac{1}{2}(x^2 + y^2)$ J (an isotropic spring, $\mathbf F_1 = -\nabla U$). For $\mathbf F_2$: $\mathbf F_2 \cdot d\mathbf r = (\sin^2 t + \cos^2 t)\,dt$, so $W = 2\pi$ J $\neq 0$: going around the loop gains energy, so no $U$ exists. Equivalently $\partial F_y / \partial x - \partial F_x / \partial y = 2 \neq 0$.

## Mastery checklist

- [ ] 1 Recognized: I can define potential energy for a conservative force and write $mgy$ and $\tfrac12 kx^2$.
- [ ] 2 Understood: I can read a potential curve: force from the slope, equilibria, stability, turning points.
- [ ] 3 Practiced: I can compute $\mathbf F = -\nabla U$, classify equilibria with $U''$ or the Hessian, derive the Lennard-Jones minimum and stiffness, and check forces numerically.
- [ ] 4 Applied: I can read a force field as a potential energy function and explain what minimization and dynamics do with its gradient.
- [ ] 5 Explained: I can teach the harmonic approximation and its failure, the difference between potential and free energy landscapes, and how a pulling force tilts a landscape.

## References

[^up8]: [[University Physics (OpenStax)]], Volume 1, ch. 8 "Potential Energy and Conservation of Energy" (potential energy of a system, conservative and nonconservative forces, $\mathbf F = -\nabla U$).
[^up84]: [[University Physics (OpenStax)]], Volume 1, §8.4 "Potential Energy Diagrams and Stability".
[^801]: [[MIT 8.01SC - Classical Mechanics]], energy part of the course (conservation of energy).
[^israel]: [[Intermolecular and Surface Forces (Israelachvili)]], 3rd ed. (2011): Lennard-Jones potential.
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), treatment of the Boltzmann distribution, the thermal energy scale $k_B T$ and single-molecule force measurements (chapters not verified).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]]: Boltzmann constant $k_B = 1.380649 \times 10^{-23}$ J/K and Avogadro constant, exact since the 2019 SI.
[^cornell]: [[Cornell 1995 - A Second Generation Force Field for the Simulation of Proteins, Nucleic Acids, and Organic Molecules]], *J. Am. Chem. Soc.* 117:5179-5197: functional form of the force field and fitting of its bonded parameters.
