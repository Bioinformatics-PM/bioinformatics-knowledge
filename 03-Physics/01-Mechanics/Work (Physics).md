---
aliases:
  - Work
  - Mechanical Work
  - Pressure-Volume Work
  - PV Work
  - Travail (physique)
tags:
  - type/concept
  - domain/physics
  - domain/chemistry
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Newton's Laws of Motion]]"
  - "[[Dot Product]]"
  - "[[Integral]]"
related:
  - "[[Kinetic Energy]]"
  - "[[Potential Energy]]"
  - "[[Conservation of Energy]]"
  - "[[Hooke's Law]]"
  - "[[Pressure]]"
  - "[[Ideal Gas Law]]"
  - "[[Laws of Thermodynamics]]"
  - "[[Enthalpy]]"
  - "[[Molecular Motor]]"
  - "[[ATP]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[MIT 8.01SC - Classical Mechanics]]"
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Svoboda 1994 - Force and Velocity Measured for Single Kinesin Molecules]]"
  - "[[Schnitzer 1997 - Kinesin Hydrolyses One ATP per 8-nm Step]]"
---

# Work (Physics)

> [!abstract]
> Work is the energy a force transfers to an object by moving it: force times the displacement along the force. A motor protein doing an 8-nm step against a load does work, and so does a gas pushing back its surroundings as it expands.

## Definition

The **work** done by a constant force $\vec F$ on an object whose point of application moves by $\vec d$ is the [[Dot Product]]

$$W = \vec F \cdot \vec d = F d\cos\theta,$$

where $\theta$ is the angle between force and displacement. For a force that varies along a path $C$, $W = \int_C \vec F \cdot d\vec r$. Work is a scalar, measured in joules (1 J = 1 N·m), and can be positive, zero or negative.[^up7][^801]

## Why it matters

- **Motors and machines.** The mechanical output of a [[Molecular Motor]] per step is a work, $F \times d$, to be compared with the free energy of the [[ATP]] it consumes; the ratio is its efficiency (Worked example).
- **Thermodynamics starts here.** The first law splits energy changes into heat and work ([[Laws of Thermodynamics]]), and the work of a gas expanding against a pressure is the $P\,\Delta V$ term that distinguishes [[Enthalpy]] from internal energy.[^chem]

## Core (L1)

**Sign and angle.**[^up7]

| Situation | $\theta$ | Work |
|---|---|---|
| force along the motion (motor pulling cargo forward) | 0° | $+Fd$ |
| force perpendicular to the motion (normal force on a sliding block) | 90° | 0 |
| force against the motion (load on a motor, friction) | 180° | $-Fd$ |

**Work against a load.** When a motor moves a distance $d$ against a constant opposing load $F$, the load does work $-Fd$ on it, and the motor must supply at least $+Fd$. For kinesin, which advances 8 nm per ATP,[^schnitzer] against a 6 pN load, near its 5-6 pN stall force:[^svoboda]

$$W = 6\ \text{pN} \times 8\ \text{nm} = 48\ \text{pN·nm} = 4.8 \times 10^{-20}\ \text{J} \approx 11.7\ k_BT.$$

![[work-area-force-and-pv.svg]]

**Variable force: work is an area.** In one dimension, $W = \int_{x_1}^{x_2} F(x)\,dx$, the area under the force-displacement curve ([[Integral]]). Stretching a spring of stiffness $k$ from 0 to $x$ requires $W = \int_0^x kx'\,dx' = \frac{1}{2}kx^2$ ([[Hooke's Law]]).[^up7]

**Work against pressure.** A gas at pressure $P$ pushing a piston of area $A$ through $dx$ does work $dW = PA\,dx = P\,dV$. The work done **by** the gas over an expansion is[^up]

$$W_{\text{by}} = \int_{V_1}^{V_2} P\,dV,$$

positive when the gas expands. At constant external pressure it is simply $P\,\Delta V$.

## Deeper (L2)

**Sign conventions differ.** Physics texts often write the first law as $\Delta U = Q - W$ with $W$ the work done **by** the system,[^up] while chemistry texts write $\Delta U = q + w$ with $w = -P\Delta V$ the work done **on** the system.[^chem] Both describe the same physics; check which one a formula uses before plugging in numbers ([[Laws of Thermodynamics]]).

**Isothermal expansion of an ideal gas.** With $P = nRT/V$ at constant $T$ ([[Ideal Gas Law]]):

$$W_{\text{by}} = \int_{V_1}^{V_2}\frac{nRT}{V}\,dV = nRT\ln\frac{V_2}{V_1}.$$

Doubling the volume of 1 mol at 298.15 K gives $RT\ln 2 = 1718$ J, with $R = 8.314\,462\,618$ J mol⁻¹ K⁻¹ (exact).[^nist] The logarithm reappears in the free energy of concentration changes, $RT\ln(c_2/c_1)$ per mole ([[Gibbs Free Energy]]).

**Path dependence.** Moving a box around a closed loop on a floor costs work against friction every time; lifting and lowering it in gravity costs nothing net. Forces whose work around any closed path is zero are **conservative**; only they have a potential energy, with $W = -\Delta U$ ([[Potential Energy]], [[Conservation of Energy]]).[^up8]

## Mathematical representation

For a path $\vec r(s)$, $s \in [a, b]$, from $\vec r_1$ to $\vec r_2$,

$$W = \int_C \vec F \cdot d\vec r = \int_a^b \vec F(\vec r(s)) \cdot \frac{d\vec r}{ds}\,ds,$$

a line integral; in one dimension it reduces to $\int_{x_1}^{x_2} F(x)\,dx$. Dimension: $[F][L] = \text{M L}^2\text{T}^{-2}$, an energy ([[Dimensional Analysis]]). For a fluid, $W_{\text{by}} = \int P\,dV$ with $[P][V] = (\text{M L}^{-1}\text{T}^{-2})(\text{L}^3)$, again an energy. A force is conservative if and only if $\oint_C \vec F \cdot d\vec r = 0$ for every closed path $C$, equivalently $\vec F = -\nabla U$ for some function $U$.

## Computational representation

Work is an integral, so a numerical quadrature computes it from any force law or from a measured force-extension table ([[Numerical Integration]]).

```python
import math

def work(force, a, b, n=1000):
    """W = integral of force(x) dx from a to b, trapezoidal rule with n slices."""
    h = (b - a) / n
    return h * (0.5 * force(a) + sum(force(a + i * h) for i in range(1, n)) + 0.5 * force(b))

KT = 4.116                                   # k_B T at 298 K, pN nm
STEP, DG_ATP = 8.0, 94.7                     # nm per step; pN nm per ATP in a cell

# 1. Motor: one 8-nm step against a constant load, one ATP per step
for load in (0.0, 2.0, 4.0, 6.0):           # pN
    w = work(lambda x: load, 0.0, STEP)
    print(f"load {load:.0f} pN: W = {w:5.1f} pN nm = {w / KT:4.1f} kT, efficiency {w / DG_ATP:.0%}")

# 2. Stretching a trap spring (kappa = 0.05 pN/nm, illustrative) from 0 to 100 nm
kappa = 0.05
print(f"spring: {work(lambda x: kappa * x, 0.0, 100.0):.2f} pN nm, exact {0.5 * kappa * 100**2:.2f}")

# 3. Isothermal expansion of 1 mol of ideal gas from 24.8 L to 49.6 L at 298.15 K
R, T, n = 8.314462618, 298.15, 1.0           # J/(mol K)
V1 = 0.0248                                  # m^3
W_by = work(lambda V: n * R * T / V, V1, 2 * V1)
print(f"gas: W_by = {W_by:.1f} J, exact nRT ln 2 = {n * R * T * math.log(2):.1f} J")
```

```text
load 0 pN: W =   0.0 pN nm =  0.0 kT, efficiency 0%
load 2 pN: W =  16.0 pN nm =  3.9 kT, efficiency 17%
load 4 pN: W =  32.0 pN nm =  7.8 kT, efficiency 34%
load 6 pN: W =  48.0 pN nm = 11.7 kT, efficiency 51%
spring: 250.00 pN nm, exact 250.00
gas: W_by = 1718.3 J, exact nRT ln 2 = 1718.3 J
```

## Worked example

> [!example] How efficient is a kinesin step?
> 1. **Energy in.** ATP hydrolysis in a living cell releases about 57 kJ/mol.[^os64] Per molecule: $57\,000 / 6.022 \times 10^{23} = 9.47 \times 10^{-20}$ J = 94.7 pN·nm ≈ 23 $k_BT$ ([[Dimensional Analysis]]).
> 2. **Coupling.** One ATP per 8-nm step.[^schnitzer]
> 3. **Work out.** Against a load $F$, $W = F \times 8$ nm: 16 pN·nm at 2 pN, 48 pN·nm at 6 pN, close to the stall force of 5-6 pN.[^svoboda]
> 4. **Efficiency** $\eta = W/\Delta G_{\text{ATP}}$: about 51 % at 6 pN. The motor cannot exceed 100 %, so its stall force is bounded by $\Delta G_{\text{ATP}}/d = 94.7 / 8 \approx 12$ pN; the measured stall force is about half that.
> 5. **Where the rest goes.** The unused free energy is dissipated as heat in the surrounding water, which is why motors are irreversible machines ([[Conservation of Energy]]).

## Common misconceptions

> [!warning] "$P\,\Delta V$ always has the same sign"
> Physics books often count work done by the gas, chemistry books work done on the system, and the two have opposite signs. Write which one you mean every time.

> [!warning] "The work done equals the fuel consumed"
> A motor's mechanical work is only part of the free energy it uses; at low load it does almost no work per ATP (efficiency near 0 %), yet still consumes one ATP per step.

## Exercises

> [!question] Exercise 1 (L1)
> A 50 N force pulls a crate 4.0 m along a floor at 30° above the horizontal. How much work does it do? How much does the weight do?

> [!success]- Solution
> $W = 50 \times 4.0 \times \cos 30° = 173$ J. The weight is perpendicular to the displacement: 0 J.

> [!question] Exercise 2 (L1)
> A kinesin takes 100 steps of 8 nm against a constant 3 pN load. What total work does it do, in pN·nm, joules and $k_BT$ ($k_BT = 4.116$ pN·nm)?

> [!success]- Solution
> Distance 800 nm: $W = 3 \times 800 = 2400$ pN·nm $= 2.4 \times 10^{-18}$ J $\approx 583\ k_BT$, about 5.8 $k_BT$ per step.

> [!question] Exercise 3 (L2)
> An optical trap of stiffness 0.05 pN/nm (illustrative) pulls back on a bead. How much work must a motor do to move the bead from the trap center to 100 nm? Why is it not $F_{\max} \times 100$ nm?

> [!success]- Solution
> $W = \int_0^{100} 0.05\,x\,dx = \frac{1}{2} \times 0.05 \times 100^2 = 250$ pN·nm. The force grows from 0 to 5 pN, so the area is a triangle, half of $5 \times 100 = 500$ pN·nm.

> [!question] Exercise 4 (L2)
> One mole of gas is produced by a reaction at 298.15 K against the constant pressure of the atmosphere (101 325 Pa). How much work does it do on the surroundings, and why is this the difference between $\Delta H$ and $\Delta U$ for that reaction?

> [!success]- Solution
> The gas occupies $V = RT/P = 8.314 \times 298.15 / 101\,325 = 0.0245$ m³ (24.5 L), so $W_{\text{by}} = P\,\Delta V = RT = 2.48$ kJ. At constant pressure, $\Delta H = \Delta U + P\Delta V$, so the enthalpy change counts this expansion work ([[Enthalpy]]).

> [!question] Exercise 5 (L2, Python)
> A toy force-extension law (invented) $F(x) = 0.2\,(e^{x/50} - 1)$ pN, with $x$ in nm, describes a tether. Compute the work to stretch it from 0 to 150 nm with `work` and compare with the exact integral.

> [!success]- Solution
> ```python
> F = lambda x: 0.2 * (math.exp(x / 50) - 1)
> exact = 0.2 * (50 * (math.exp(3) - 1) - 150)
> for n in (10, 100, 1000):
>     print(n, round(work(F, 0, 150, n), 3), round(exact, 3))
> # 10 162.285 160.855
> # 100 160.87 160.855
> # 1000 160.856 160.855
> ```
>
> About 161 pN·nm, 39 $k_BT$. The trapezoidal error falls 100-fold for each 10-fold increase of $n$ (error $\propto h^2$); the curve is convex, so the trapezoids overestimate.

## Mastery checklist

- [ ] 1 Recognized: I can define work, its unit and its sign.
- [ ] 2 Understood: I can explain why perpendicular forces do no work, why work is an area, and the two sign conventions of $P\,dV$ work.
- [ ] 3 Practiced: I compute work for constant, spring and pressure forces, analytically and by numerical integration.
- [ ] 4 Applied: I computed the work per step and the efficiency of a real motor from published force and step data.
- [ ] 5 Explained: I can relate path independence to potential energy and explain where a motor's unused free energy goes.

## References

[^up7]: [[University Physics (OpenStax)]], Volume 1, ch. 7 "Work and Kinetic Energy".
[^up8]: [[University Physics (OpenStax)]], Volume 1, ch. 8 "Potential Energy and Conservation of Energy".
[^up]: [[University Physics (OpenStax)]], Volume 2: work done by a gas, $\int P\,dV$, and the first law written with the work done by the system.
[^801]: [[MIT 8.01SC - Classical Mechanics]]: energy.
[^chem]: [[Chemistry 2e (OpenStax)]]: pressure-volume work $w = -P\Delta V$ and the first law $\Delta U = q + w$; enthalpy.
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]]: molar gas constant $R$ (exact).
[^os64]: [[Biology 2e (OpenStax)]], section 6.4 "ATP: Adenosine Triphosphate" (about −57 kJ/mol for ATP hydrolysis in a living cell).
[^svoboda]: [[Svoboda 1994 - Force and Velocity Measured for Single Kinesin Molecules]], *Cell* 77:773-784 (loads up to 5-6 pN).
[^schnitzer]: [[Schnitzer 1997 - Kinesin Hydrolyses One ATP per 8-nm Step]], *Nature* 388:386-390.
