---
aliases:
  - Linear Momentum
  - Impulse
  - Conservation of Momentum
  - Quantité de mouvement
tags:
  - type/concept
  - domain/physics
  - domain/chemistry
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Newton's Laws of Motion]]"
  - "[[Integral]]"
related:
  - "[[Kinetic Energy]]"
  - "[[Pressure]]"
  - "[[Ideal Gas Law]]"
  - "[[Conservation of Energy]]"
  - "[[Brownian Motion]]"
  - "[[Molecular Dynamics Simulation]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[MIT 8.01SC - Classical Mechanics]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
---

# Momentum

> [!abstract]
> Momentum is mass times velocity; forces change it by delivering impulses, and in any collision between objects free of outside forces the total momentum is the same before and after. Countless molecular impulses on a wall are what we call gas pressure.

## Definition

The **linear momentum** of a body of mass $m$ and velocity $\vec v$ is $\vec p = m\vec v$, unit kg m s⁻¹. The **impulse** of a force over a time interval is $\vec J = \int_{t_1}^{t_2} \vec F\,dt$, and it equals the change of momentum, $\vec J = \Delta\vec p$ (impulse-momentum theorem). Newton's second law in its general form reads $\vec F_{\text{net}} = d\vec p/dt$. For a system on which the net external force is zero, the total momentum $\sum_i m_i\vec v_i$ is **conserved**.[^up9][^801]

## Why it matters

- **Pressure from collisions.** The pressure of a gas is the time-averaged momentum that molecules deliver to the walls per unit area and time; this kinetic picture leads to the [[Ideal Gas Law]] and to the meaning of temperature ([[Kinetic Energy]]).[^up2]
- **Thermal kicks.** A protein in water is struck by solvent molecules from all sides; each collision transfers a tiny, random impulse, the microscopic picture behind [[Brownian Motion]].[^pboc]
- **A check for simulations.** With only internal forces, total momentum is constant, so a drift of momentum in a [[Molecular Dynamics Simulation]] flags a bug or an external force ([[Newton's Laws of Motion#Advanced (L3)]]).

## Core (L1)

**Impulse.** A large force for a short time or a small force for a long time can give the same impulse: $J = F_{\text{avg}}\,\Delta t$ is the area under $F(t)$ ([[Integral]]). Catching a ball with a moving hand lengthens $\Delta t$ and reduces the average force for the same $\Delta p$.[^up9]

**Conservation.** For two bodies interacting only with each other, the third law gives $\vec F_{12} = -\vec F_{21}$ at every instant, so the impulses are equal and opposite and $\Delta\vec p_1 = -\Delta\vec p_2$: the total momentum does not change, whatever the details of the force ([[Newton's Laws of Motion]]).[^up9]

**Collisions.**[^up9]

| Type | Momentum | Kinetic energy | Example |
|---|---|---|---|
| elastic | conserved | conserved | idealized gas molecules hitting each other or a wall |
| inelastic | conserved | partly converted (heat, deformation) | most macroscopic collisions |
| perfectly inelastic | conserved | maximal loss compatible with momentum | the bodies stick together |

In one dimension, a perfectly inelastic collision gives a common final velocity $v_f = \frac{m_1 v_1 + m_2 v_2}{m_1 + m_2}$. For an elastic head-on collision with body 2 initially at rest, conserving both momentum and [[Kinetic Energy]] gives (Exercise 3)

$$v_1' = \frac{m_1 - m_2}{m_1 + m_2}\,v_1, \qquad v_2' = \frac{2m_1}{m_1 + m_2}\,v_1.$$

Equal masses exchange velocities; a light body bouncing off a very heavy one simply reverses ($v_1' \approx -v_1$).

**Gas pressure from momentum.** A molecule bouncing elastically off a smooth wall reverses its normal velocity component $v_x$, so the wall receives an impulse $2mv_x$ per hit:[^up2]

![[gas-molecule-wall-momentum-transfer.svg]]

In a box of length $L$, the molecule returns to the same wall every $2L/v_x$, so its time-averaged force is $\frac{2mv_x}{2L/v_x} = \frac{m v_x^2}{L}$. Summing over $N$ molecules and dividing by the wall area $A$ (with $V = AL$):

$$P = \frac{N m \langle v_x^2\rangle}{V} = \frac{1}{3}\frac{N}{V}\,m\langle v^2\rangle,$$

because random directions give $\langle v_x^2\rangle = \langle v_y^2\rangle = \langle v_z^2\rangle = \langle v^2\rangle/3$. Comparing with $PV = Nk_BT$ is how kinetic theory links temperature to molecular motion ([[Kinetic Energy]], [[Pressure]]).[^up2]

## Deeper (L2)

**Center of mass.** The center of mass $\vec R = \sum_i m_i\vec r_i / M$ (with $M = \sum_i m_i$) moves as if all external forces acted on a single particle of mass $M$: $M\ddot{\vec R} = \vec F_{\text{ext}}$. Internal forces, however violent, cannot move it.[^up9] Seen from the center-of-mass frame, the total momentum is zero and a collision only redistributes velocities.

**Light on heavy: thermal kicks.** In a head-on elastic collision of a water molecule ($m_1 = 18.015$ u) with a 50 kDa protein at rest, $v_2' = \frac{2m_1}{m_1 + m_2}v_1 \approx 7.2 \times 10^{-4}\,v_1$.[^chem] With $v_1 \approx 645$ m/s, a typical thermal speed of water at 300 K ([[Kinetic Energy]]), the protein recoils at about 0.46 m/s per hit. In liquid water such hits come from all directions and are immediately damped, so the protein performs a random walk instead of flying off: [[Brownian Motion]], whose systematic part is the drag of [[Stokes' Law]].[^pboc] The same split, a random impulse plus friction, defines the [[Langevin Equation]].

**Momentum versus energy.** Momentum is a vector and is conserved in every collision of an isolated system; kinetic energy is a scalar and is conserved only in elastic collisions. Problems with two unknowns need both laws (elastic) or momentum plus a sticking condition (perfectly inelastic) ([[Conservation of Energy]]).

## Mathematical representation

For particles $i = 1, \dots, N$ with masses $m_i$ and velocities $\vec v_i$, the total momentum is $\vec P = \sum_i m_i\vec v_i$. With internal pair forces $\vec F_{ij} = -\vec F_{ji}$ and external forces $\vec F_i^{\text{ext}}$,

$$\frac{d\vec P}{dt} = \sum_i \vec F_i^{\text{ext}} + \sum_i\sum_{j \ne i}\vec F_{ij} = \sum_i \vec F_i^{\text{ext}},$$

since the double sum cancels pair by pair. Integrating over $[t_1, t_2]$ gives $\Delta\vec P = \int_{t_1}^{t_2}\sum_i \vec F_i^{\text{ext}}\,dt$, the impulse-momentum theorem; $\vec P$ is constant when the external force vanishes.

## Computational representation

Kinetic theory can be checked by brute force. The script counts every hit of a toy one-dimensional gas (reduced units, invented velocities) on the right wall of a box, adds up the impulses $2m|v|$ and compares the time-averaged force with the prediction $N m\langle v^2\rangle / L$. A particle's hits are counted exactly by "unfolding" its bouncing path into a straight line.

```python
import random


def right_wall_hits(x0, v, L, t):
    """Number of hits on the wall at x = L in time t, for a particle bouncing elastically in [0, L]."""
    first = (L - x0) if v > 0 else (x0 + L)        # distance travelled before the first hit
    travelled = abs(v) * t
    return 0 if travelled < first else int((travelled - first) // (2 * L)) + 1


random.seed(3)
m, L, t, N = 1.0, 1.0, 1000.0, 500                   # reduced units (toy gas)
gas = [(random.uniform(0, L), random.gauss(0, 1)) for _ in range(N)]

impulse = sum(right_wall_hits(x0, v, L, t) * 2 * m * abs(v) for x0, v in gas)
measured = impulse / t                               # time-averaged force on the wall
predicted = sum(m * v * v for _, v in gas) / L       # N m <v^2> / L
print(f"force from counted collisions: {measured:.2f}")
print(f"kinetic-theory prediction    : {predicted:.2f}")
```

```text
force from counted collisions: 493.56
kinetic-theory prediction    : 493.57
```

The tiny difference comes from the incomplete last round trip of each particle; it shrinks as $t$ grows.

## Worked example

> [!example] How many molecular hits make one atmosphere?
> Nitrogen at 300 K presses on a wall with $P = 1$ atm $= 101\,325$ Pa.[^nist] Take a molecule with $v_x = 300$ m/s, a typical value at this temperature.
> 1. **Mass.** $M(\mathrm{N_2}) = 2 \times 14.007 = 28.014$ g/mol,[^chem] so $m = \frac{0.028014\ \text{kg mol}^{-1}}{6.022 \times 10^{23}\ \text{mol}^{-1}} = 4.65 \times 10^{-26}$ kg.[^nist]
> 2. **Impulse per hit.** $2mv_x = 2 \times 4.65 \times 10^{-26} \times 300 = 2.79 \times 10^{-23}$ N·s.
> 3. **Force on 1 cm².** $101\,325\ \text{Pa} \times 10^{-4}\ \text{m}^2 = 10.13$ N.
> 4. **Hits needed.** $10.13 / 2.79 \times 10^{-23} \approx 3.6 \times 10^{23}$ hits per second on each square centimetre: pressure feels steady because the impulses are so many and so small.
> 5. **Consistency.** The number density is $n = P/(k_BT) = 2.45 \times 10^{25}$ m⁻³ ([[Ideal Gas Law]]), so about 25 million molecules share a cubic micrometre.

## Common misconceptions

> [!warning] "Kinetic energy is conserved in every collision"
> Only momentum is conserved in every collision of an isolated system. Kinetic energy is conserved only in elastic collisions; in a perfectly inelastic one it is partly converted to heat even though momentum is untouched.

> [!warning] "The molecule's momentum is conserved when it bounces off the wall"
> It is not: it reverses. The conserved quantity is the momentum of molecule plus wall (and container); the wall's share is the impulse $2mv_x$ that becomes pressure.

> [!warning] "Gas pressure comes from molecules repelling each other or from their weight"
> In the kinetic picture of an ideal gas, molecules exert force on the wall only when they hit it; pressure is momentum flux. Interactions between molecules are what makes real gases deviate from the ideal law.

> [!warning] "A force and an impulse are the same"
> An impulse is a force integrated over time (N·s = kg m s⁻¹, a momentum), not a force (N). Two collisions with the same impulse can have very different peak forces.

## Exercises

> [!question] Exercise 1 (L1)
> A 0.15 kg ball moving at 20 m/s is caught and brought to rest in 0.05 s. What impulse does the hand deliver, and what is the average force?

> [!success]- Solution
> $J = \Delta p = 0 - 0.15 \times 20 = -3.0$ N·s (opposite to the motion). $F_{\text{avg}} = J/\Delta t = -60$ N. Stopping it in 0.5 s would need only 6 N.

> [!question] Exercise 2 (L1)
> A 2.0 kg cart at 3.0 m/s hits a 1.0 kg cart at rest and they stick. Find the final velocity and the fraction of kinetic energy lost.

> [!success]- Solution
> $v_f = \frac{2.0 \times 3.0}{3.0} = 2.0$ m/s. Kinetic energy: before $\frac{1}{2} \times 2 \times 9 = 9$ J, after $\frac{1}{2} \times 3 \times 4 = 6$ J: one third is lost as heat and deformation; momentum, 6 kg m/s, is unchanged.

> [!question] Exercise 3 (L2)
> Derive the final velocities of a one-dimensional elastic collision of $m_1$ (velocity $v_1$) with $m_2$ at rest.

> [!success]- Solution
> Momentum: $m_1 v_1 = m_1 v_1' + m_2 v_2'$. Energy: $m_1 v_1^2 = m_1 v_1'^2 + m_2 v_2'^2$. Rewrite them as $m_1(v_1 - v_1') = m_2 v_2'$ and $m_1(v_1 - v_1')(v_1 + v_1') = m_2 v_2'^2$; dividing gives $v_1 + v_1' = v_2'$. Substituting back: $v_1' = \frac{m_1 - m_2}{m_1 + m_2}v_1$ and $v_2' = \frac{2m_1}{m_1 + m_2}v_1$.

> [!question] Exercise 4 (L2)
> Using the pressure formula, show that doubling the absolute temperature of an ideal gas at fixed volume doubles its pressure, given that $\langle v^2 \rangle$ is proportional to $T$.

> [!success]- Solution
> $P = \frac{1}{3}\frac{N}{V}m\langle v^2\rangle$ with $N$, $V$, $m$ fixed: $P \propto \langle v^2\rangle \propto T$. Each hit carries $\sqrt 2$ times more momentum and hits are $\sqrt 2$ times more frequent, a factor 2 in total.

> [!question] Exercise 5 (L2, Python)
> Rerun the wall simulation after multiplying every velocity by $\sqrt 2$ (which doubles $\langle v^2 \rangle$), then with twice as many molecules. Predict both results before running.

> [!success]- Solution
> ```python
> hot = [(x0, v * 2 ** 0.5) for x0, v in gas]
> dense = gas + [(random.uniform(0, L), random.gauss(0, 1)) for _ in range(N)]
> for name, g in (("hot", hot), ("dense", dense)):
>     F = sum(right_wall_hits(x0, v, L, t) * 2 * m * abs(v) for x0, v in g) / t
>     print(name, round(F, 1), round(sum(m * v * v for _, v in g) / L, 1))
> # hot 987.1 987.1
> # dense 976.7 976.7
> ```
>
> Faster molecules double the force (987.1 ≈ 2 × 493.6), as Exercise 4 predicts. Doubling $N$ roughly doubles it (976.7 rather than 987.1, because the 500 new random velocities have a slightly smaller $\langle v^2 \rangle$). Pressure is proportional to $N\langle v^2\rangle$, the total kinetic energy per volume.

## Mastery checklist

- [ ] 1 Recognized: I can define momentum and impulse with their units.
- [ ] 2 Understood: I can derive momentum conservation from the third law and explain why kinetic energy is conserved only in elastic collisions.
- [ ] 3 Practiced: I solve 1D elastic and perfectly inelastic collisions and impulse problems, and I can simulate wall collisions in Python.
- [ ] 4 Applied: I checked total momentum conservation in a simulation I wrote ([[Newton's Laws of Motion]] Exercise 5).
- [ ] 5 Explained: I can derive gas pressure from molecular impulses and explain thermal kicks on a protein as the origin of Brownian motion.

## References

[^up9]: [[University Physics (OpenStax)]], Volume 1, ch. 9 "Linear Momentum and Collisions".
[^up2]: [[University Physics (OpenStax)]], Volume 2, ch. 2 "The Kinetic Theory of Gases", section 2.2 "Pressure, Temperature, and RMS Speed".
[^801]: [[MIT 8.01SC - Classical Mechanics]]: conservation of momentum.
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]]: Avogadro and Boltzmann constants (exact), standard atmosphere 101 325 Pa.
[^chem]: [[Chemistry 2e (OpenStax)]]: atomic masses (N 14.007 u) and the molar mass of water (18.015 g/mol).
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012): Brownian motion of macromolecules driven by collisions with solvent molecules.
