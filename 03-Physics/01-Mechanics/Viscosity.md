---
aliases:
  - Dynamic Viscosity
  - Shear Viscosity
  - Viscous Drag
  - Viscosité
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Newton's Laws of Motion]]"
  - "[[Dimensional Analysis]]"
  - "[[Kinematics]]"
  - "[[Pressure]]"
related:
  - "[[Stokes' Law]]"
  - "[[Reynolds Number]]"
  - "[[Centrifugation]]"
  - "[[Diffusion]]"
  - "[[Stokes-Einstein Relation]]"
  - "[[Langevin Equation]]"
  - "[[Harmonic Oscillator]]"
  - "[[Blood]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[Svoboda 1994 - Force and Velocity Measured for Single Kinesin Molecules]]"
---

# Viscosity

> [!abstract]
> Viscosity measures how strongly a fluid resists being sheared. It is the source of the drag on anything that moves through a liquid, and at the scale of molecules and cells this drag is so strong that motion stops almost as soon as the push stops.

## Definition

Take a fluid layer of thickness $L$ between two parallel plates of area $A$, the bottom one fixed. The fluid touching each plate moves with that plate (no slip), so the layer is sheared. Keeping the top plate moving at speed $v$ takes a force

$$F = \eta\,\frac{vA}{L},$$

which defines the **viscosity** $\eta$ of the fluid (also called dynamic viscosity), in pascal-seconds, Pa·s.[^up147] An object moving through a fluid shears the fluid around it and feels a **drag force** opposing its velocity. For small, slow objects the drag is proportional to the speed, $\vec F_\text{drag} = -\gamma \vec v$, with a **friction coefficient** $\gamma$ in kg/s; for large, fast objects it grows as $v^2$.[^up64]

## Why it matters

- **Molecules and cells live in an overdamped world.** In water a protein loses its velocity in about a picosecond (Core), so its motion follows the forces acting now, not their history. Brownian dynamics and the [[Langevin Equation]] put this friction explicitly into the equations of motion that [[Molecular Dynamics Simulation|molecular dynamics]] integrates ([[Newton's Laws of Motion#Advanced (L3)]]).
- **Sizes from mobility.** The friction coefficient converts a measured [[Diffusion]] coefficient, sedimentation coefficient or drift velocity into the size of a molecule ([[Stokes' Law]], [[Stokes-Einstein Relation]], [[Centrifugation]]). Every such conversion needs the viscosity of the solvent at the temperature of the measurement.
- **Temperature corrections.** Water is 31 % less viscous at 37 °C than at 20 °C, so the same protein diffuses about 1.5 times faster (Computational representation). Comparing diffusion or sedimentation values measured at different temperatures without this correction is a classic error.
- **Flow in vessels and channels.** Flow through a tube scales with the fourth power of its radius and inversely with viscosity (Advanced): the physics of [[Blood]] flow, pipette tips and microfluidic chips.

## Core (L2)

### Shear and the viscosity coefficient

![[viscosity-shear-and-drag.svg]]

Between the plates the velocity grows linearly from 0 at the fixed plate to $v$ at the moving one (panel a). Each layer drags the next one along, and the force per area is proportional to the **shear rate** $v/L$, the velocity gradient across the layer. Dimensions: $[\eta] = [FL/(vA)] = \text{M L}^{-1}\text{T}^{-1}$, so 1 Pa·s = 1 kg m⁻¹ s⁻¹ ([[Dimensional Analysis]]).

Viscosity differs between fluids by orders of magnitude, and liquids become less viscous when heated. Values in mPa·s (10⁻³ Pa·s):[^up147]

| Fluid | 0 °C | 20 °C | 37 °C | 100 °C |
|---|---:|---:|---:|---:|
| water | 1.792 | 1.002 | 0.6947 | 0.282 |
| blood plasma |  | 1.810 | 1.257 |  |
| whole blood |  | 3.015 | 2.084 |  |

Water at 37 °C is 31 % less viscous than at 20 °C, and 6.4 times less viscous at 100 °C than at 0 °C. At 37 °C whole blood is 1.66 times as viscous as its plasma: the suspended cells add resistance to shear.

### Drag on a moving object

An object moving through a fluid shears it, so it feels a force opposite to its velocity, in one of two regimes:[^up64]

- **Linear (viscous) drag**, $F = \gamma v$, for small or slow objects. For a sphere of radius $r$, dimensions force $\gamma \propto \eta r$ ([[Dimensional Analysis#Exercises|Dimensional Analysis, Exercise 3]]) and hydrodynamics gives $\gamma = 6\pi\eta r$: [[Stokes' Law]].
- **Quadratic drag**, $F = \frac{1}{2}C\rho A v^2$, for large or fast objects, with $\rho$ the density of the fluid, $A$ the cross-sectional area and $C$ a dimensionless drag coefficient.

The [[Reynolds Number]] decides which regime applies.

### Velocity follows force

With linear drag, Newton's second law for an object of mass $m$ pushed by a constant force $F$ is $m\,dv/dt = F - \gamma v$ ([[Newton's Laws of Motion]]). Starting from $v_0$,

$$v(t) = \frac{F}{\gamma} + \left(v_0 - \frac{F}{\gamma}\right)e^{-t/\tau}, \qquad \tau = \frac{m}{\gamma}.$$

The velocity relaxes to the **terminal velocity** $v_t = F/\gamma$ with time constant $\tau$; when the force stops it decays to zero with the same $\tau$ (panel b). After a few $\tau$, velocity, not acceleration, is proportional to force.

### Why friction dominates at the molecular scale

For a sphere of density $\rho_p$, mass grows as $r^3$ but Stokes friction only as $r$:

$$\tau = \frac{m}{\gamma} = \frac{\frac{4}{3}\pi r^3 \rho_p}{6\pi\eta r} = \frac{2\rho_p r^2}{9\eta} \propto r^2.$$

An object ten times smaller forgets its velocity a hundred times faster. In water at 20 °C, giving every object the density of water (round illustrative radii; computed below):

| Radius | Scale | Friction $\gamma$ | $\tau$ |
|---|---|---:|---:|
| 2.5 nm | a protein | 4.7 × 10⁻¹¹ kg/s | 1.4 ps |
| 1 µm | a bacterium | 1.9 × 10⁻⁸ kg/s | 0.22 µs |
| 100 µm | a large cell | 1.9 × 10⁻⁶ kg/s | 2.2 ms |
| 1 mm | (linear drag assumed) | 1.9 × 10⁻⁵ kg/s | 0.22 s |

A protein is pushed by solvent collisions and by its partners, and every push is forgotten within picoseconds. On any timescale much longer than that, its velocity is set by the forces acting at that moment: it has no momentum to carry it on. Viscous drag, not inertia, is the right starting point for the physics of molecules and cells in water.[^pboc12]

## Advanced (L3)

**Flow through a tube (Poiseuille's law).** For laminar flow through a tube of radius $R$ and length $\ell$, a pressure difference $\Delta p$ drives the volume flow rate[^up147]

$$Q = \frac{\pi R^4\,\Delta p}{8\eta\ell}, \qquad \text{resistance } \mathcal{R} = \frac{\Delta p}{Q} = \frac{8\eta\ell}{\pi R^4}.$$

Narrowing a vessel by 20 % multiplies its resistance by 2.4 (Exercise 4), and the exponent 4 follows from dimensions alone (same exercise). The same law governs capillaries, pipette tips and microfluidic channels, where flow is laminar ([[Reynolds Number]]); the [[Pressure]] differences that drive [[Blood]] flow work against this resistance.

**Friction and thermal noise are the same collisions.** Drag is the average effect of solvent molecules striking a moving object harder on its front than on its back; the fluctuations around that average are the random kicks of [[Brownian Motion]]. The two are tied by the Einstein relation $D = k_B T/\gamma$, with $D$ the [[Diffusion]] coefficient.[^pboc] With $\gamma = 6\pi\eta r$ it becomes the [[Stokes-Einstein Relation]]. For the same reason the friction term and the random force of the [[Langevin Equation]] cannot be chosen independently: both must come from the same $\gamma$ and $T$ for the simulated particle to reach the right temperature.

**The cytoplasm is not water.** Crowded with macromolecules, it slows the diffusion of a protein about tenfold compared with water.[^pboc] A size computed from an intracellular $D$ with the viscosity of water would therefore come out about ten times too large: the viscosity entering $\gamma$ must describe the medium the molecule actually moves in.

## Mathematical representation

- **Shear stress.** For a flow $v_x(y)$ parallel to a wall, the force per area between layers is $\sigma = \eta\,dv_x/dy$; the plate geometry is the case $dv_x/dy = v/L$. Units: $\eta$ in Pa·s $= \text{kg m}^{-1}\text{s}^{-1}$.
- **Linear drag.** $\vec F_\text{drag} = -\gamma\vec v$ with $\gamma = c\,\eta\,\ell$ for an object of size $\ell$ and dimensionless shape factor $c$; a sphere has $c = 6\pi$, $\ell = r$.
- **Motion with drag.** $m\dot v = F - \gamma v$ gives $v(t) = v_t + (v_0 - v_t)e^{-t/\tau}$, $v_t = F/\gamma$, $\tau = m/\gamma$. After the force stops, the distance coasted is $\int_0^\infty v_0 e^{-t/\tau}\,dt = v_0\tau$.
- **Dissipation.** At terminal velocity the pushing force delivers power $P = F v_t = \gamma v_t^2$, all converted to heat in the fluid ([[Conservation of Energy]]).
- **Poiseuille.** $Q = \pi R^4\Delta p/(8\eta\ell)$, so $Q \propto R^4$ at fixed $\Delta p$.

## Computational representation

Friction coefficients, relaxation times, the exact $v(t)$, and the temperature correction of a diffusion coefficient, with the table values of water:

```python
import math

WATER_ETA = {0: 1.792e-3, 20: 1.002e-3, 37: 0.6947e-3, 40: 0.653e-3, 100: 0.282e-3}  # Pa s, Table 14.4


def sphere_friction(radius: float, eta: float) -> float:
    """Linear drag coefficient gamma = 6 pi eta r of a sphere (Stokes' law), kg/s."""
    return 6 * math.pi * eta * radius


def relaxation_time(radius: float, eta: float, density: float = 1000.0) -> float:
    """tau = m / gamma: time for drag to cut a sphere's velocity by a factor e."""
    mass = 4 / 3 * math.pi * radius**3 * density
    return mass / sphere_friction(radius, eta)


def velocity(t: float, v0: float, force: float, gamma: float, tau: float) -> float:
    """Solution of m dv/dt = F - gamma v: relaxes from v0 to F/gamma with time constant tau."""
    v_terminal = force / gamma
    return v_terminal + (v0 - v_terminal) * math.exp(-t / tau)


eta = WATER_ETA[20]
for r in (2.5e-9, 1e-6, 100e-6, 1e-3):              # radii in m, density of water assumed
    print(f"r = {r:.1e} m   gamma = {sphere_friction(r, eta):.2e} kg/s   tau = {relaxation_time(r, eta):.1e} s")

r, F = 1e-6, 1e-12                                   # a 1 um sphere pushed by 1 pN from rest
g, tau = sphere_friction(r, eta), relaxation_time(r, eta)
print(f"v_t = {F / g * 1e6:.1f} um/s;",
      ", ".join(f"v({k} tau)/v_t = {velocity(k * tau, 0.0, F, g, tau) / (F / g):.3f}" for k in (1, 3, 10)))

t20, t37 = 293.15, 310.15                            # same particle: D = k_B T / gamma, proportional to T / eta
print(f"D(37 C)/D(20 C) = {(t37 / t20) * (WATER_ETA[20] / WATER_ETA[37]):.3f}"
      f" = {t37 / t20:.3f} (T) x {WATER_ETA[20] / WATER_ETA[37]:.3f} (viscosity)")
```

```text
r = 2.5e-09 m   gamma = 4.72e-11 kg/s   tau = 1.4e-12 s
r = 1.0e-06 m   gamma = 1.89e-08 kg/s   tau = 2.2e-07 s
r = 1.0e-04 m   gamma = 1.89e-06 kg/s   tau = 2.2e-03 s
r = 1.0e-03 m   gamma = 1.89e-05 kg/s   tau = 2.2e-01 s
v_t = 52.9 um/s; v(1 tau)/v_t = 0.632, v(3 tau)/v_t = 0.950, v(10 tau)/v_t = 1.000
D(37 C)/D(20 C) = 1.526 = 1.058 (T) x 1.442 (viscosity)
```

The 1 µm sphere reaches 95 % of its terminal speed in $3\tau$, less than a microsecond. Keep viscosities in a table keyed by temperature, in Pa·s, and never mix them with mPa·s values in one formula.

## Worked example

> [!example] How fast does a protein forget a push?
> A globular protein of radius 2.5 nm (illustrative), in water at 20 °C, given the density of water.
> 1. **Friction.** $\gamma = 6\pi\eta r = 6\pi \times 1.002 \times 10^{-3} \times 2.5 \times 10^{-9} = 4.72 \times 10^{-11}$ kg/s.
> 2. **Mass.** $m = \frac{4}{3}\pi r^3 \rho = \frac{4}{3}\pi (2.5 \times 10^{-9})^3 \times 1000 = 6.5 \times 10^{-23}$ kg, about 39 kDa.
> 3. **Relaxation time.** $\tau = m/\gamma = 1.4 \times 10^{-12}$ s.
> 4. **Force for a given speed.** Dragging it at 1 µm/s takes $\gamma v = 4.7 \times 10^{-17}$ N $= 4.7 \times 10^{-5}$ pN, a hundred-thousandth of the 5-6 pN loads a kinesin motor works against.[^svoboda] In absolute terms the drag is tiny; it dominates because inertia is even tinier.
> 5. **Conclusion.** Any force acting for more than a few picoseconds produces a velocity $F/\gamma$, not a growing acceleration.

## Common misconceptions

> [!warning] "Viscous means dense"
> Density is mass per volume (kg/m³); viscosity is resistance to shear (Pa·s). Stokes drag depends on $\eta$ alone, not on the density of the fluid, and heating water from 0 to 100 °C divides its viscosity by 6.4 (table above).

> [!warning] "Small things move fast because they are light"
> Being light means having little momentum to lose: drag removes it in $\tau \propto r^2$. A protein's thermal velocity is meters per second, but it is randomized every picosecond, so the protein makes no progress at that speed ([[Diffusion]]).

> [!warning] "Warm molecules diffuse faster because they move faster"
> For the same protein, $D = k_B T/\gamma$ grows by a factor 1.53 from 20 to 37 °C. The temperature itself contributes only 1.06; the remaining 1.44 is the drop in the viscosity of water, through $\gamma$.

## Exercises

> [!question] Exercise 1 (L2)
> Water at 20 °C fills a 0.1 mm gap between two plates of area 1 cm². What force keeps the top plate moving at 1 cm/s? Check that $\eta v A/L$ has the unit of a force.

> [!success]- Solution
> $F = \eta vA/L = 1.002 \times 10^{-3} \times 0.01 \times 10^{-4} / 10^{-4} = 1.0 \times 10^{-5}$ N. Units: (kg m⁻¹ s⁻¹)(m s⁻¹)(m²)/(m) = kg m s⁻², a newton.

> [!question] Exercise 2 (L2)
> A silica bead of radius 0.5 µm (density 2000 kg/m³, illustrative) is pulled through water at 20 °C by a constant 1 pN force. Find its friction coefficient, terminal speed and relaxation time. How far does it coast once the force is switched off at full speed?

> [!success]- Solution
> $\gamma = 6\pi \times 1.002 \times 10^{-3} \times 0.5 \times 10^{-6} = 9.44 \times 10^{-9}$ kg/s, so $v_t = F/\gamma = 106$ µm/s. Mass $m = \frac{4}{3}\pi r^3 \times 2000 = 1.05 \times 10^{-15}$ kg, so $\tau = m/\gamma = 1.1 \times 10^{-7}$ s. Coasting distance $v_t \tau = 1.2 \times 10^{-11}$ m, about a tenth of an ångström: the bead stops on the spot.

> [!question] Exercise 3 (L2)
> A protein has $D = 90$ µm²/s in water at 20 °C (invented value). Predict $D$ at 37 °C, and say which factor dominates the change.

> [!success]- Solution
> $D \propto T/\eta$, so $D_{37} = 90 \times \frac{310.15}{293.15} \times \frac{1.002}{0.6947} = 90 \times 1.058 \times 1.442 = 137$ µm²/s. The viscosity factor (1.44) dominates the temperature factor (1.06).

> [!question] Exercise 4 (L3)
> (a) The flow $Q$ through a tube depends only on the pressure gradient $\Delta p/\ell$, the viscosity $\eta$ and the radius $R$. Find the form of $Q$ by dimensional analysis. (b) An arteriole narrows by 20 % at constant pressure difference. By what factor does its flow change, and by what factor must $\Delta p$ rise to restore it?

> [!success]- Solution
> (a) $[Q] = \text{L}^3\text{T}^{-1}$, $[\Delta p/\ell] = \text{M L}^{-2}\text{T}^{-2}$, $[\eta] = \text{M L}^{-1}\text{T}^{-1}$. Write $Q = C(\Delta p/\ell)^a\eta^b R^c$. Mass: $a + b = 0$; time: $-2a - b = -1$, so $a = 1$, $b = -1$; length: $-2a - b + c = 3$, so $c = 4$. Hence $Q = C\,R^4\Delta p/(\eta\ell)$; hydrodynamics gives $C = \pi/8$. (b) $Q \propto R^4$: $0.8^4 = 0.41$, the flow drops to 41 %; restoring it needs $\Delta p$ multiplied by $1/0.41 = 2.44$.

> [!question] Exercise 5 (L3, Python)
> Fit $\ln\eta = a + b/T$ by least squares to the five water values of the table (0, 20, 37, 40, 100 °C; the 40 °C entry is 0.653 mPa·s[^up147]). How good is the fit? Estimate $\eta$ at 25 °C with the global fit and with the same law through the 20 and 37 °C points only. Which would you use?

> [!success]- Solution
> ```python
> import math
>
> WATER_ETA = {0: 1.792e-3, 20: 1.002e-3, 37: 0.6947e-3, 40: 0.653e-3, 100: 0.282e-3}  # Pa s
> x = [1 / (t + 273.15) for t in WATER_ETA]            # 1/T in K^-1
> y = [math.log(e) for e in WATER_ETA.values()]
> n = len(x)
> mx, my = sum(x) / n, sum(y) / n
> b = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / sum((xi - mx) ** 2 for xi in x)
> a = my - b * mx                                      # least squares fit of ln(eta) = a + b/T
> for t, e in WATER_ETA.items():
>     fit = math.exp(a + b / (t + 273.15))
>     print(f"{t:3d} C  table {e * 1e3:.3f}  fit {fit * 1e3:.3f} mPa s  ({100 * (fit / e - 1):+.0f} %)")
>
>
> def local(t: float, t1: int = 20, t2: int = 37) -> float:
>     """Same law through the two nearest table points only."""
>     w = (1 / (t + 273.15) - 1 / (t1 + 273.15)) / (1 / (t2 + 273.15) - 1 / (t1 + 273.15))
>     return math.exp(math.log(WATER_ETA[t1]) + w * (math.log(WATER_ETA[t2]) - math.log(WATER_ETA[t1])))
>
>
> print(f"25 C: global fit {math.exp(a + b / 298.15) * 1e3:.3f} mPa s, local {local(25) * 1e3:.3f} mPa s")
> ```
> ```text
>   0 C  table 1.792  fit 1.649 mPa s  (-8 %)
>  20 C  table 1.002  fit 1.036 mPa s  (+3 %)
>  37 C  table 0.695  fit 0.732 mPa s  (+5 %)
>  40 C  table 0.653  fit 0.691 mPa s  (+6 %)
> 100 C  table 0.282  fit 0.266 mPa s  (-6 %)
> 25 C: global fit 0.932 mPa s, local 0.896 mPa s
> ```
> The residuals change sign systematically (negative at both ends, positive in the middle): $\ln\eta$ is curved against $1/T$, so a single exponential is off by up to 8 %. Use the local value, 0.896 mPa·s, which interpolates between close measurements; extrapolating a global fit would carry a systematic error into every diffusion or sedimentation estimate.

## Mastery checklist

- [ ] 1 Recognized: I can define viscosity with the two-plate picture, give its SI unit and the viscosity of water (about 1 mPa·s at 20 °C).
- [ ] 2 Understood: I can explain linear versus quadratic drag, the terminal velocity, $\tau = m/\gamma$, and why $\tau \propto r^2$ makes molecules overdamped.
- [ ] 3 Practiced: I compute friction coefficients, relaxation times and temperature corrections of $D$, and apply Poiseuille's law.
- [ ] 4 Applied: I corrected a diffusion or sedimentation value from a paper or a dataset to another temperature with the viscosity of water.
- [ ] 5 Explained: I can explain why friction and thermal noise are linked (Einstein relation) and the limits of using the viscosity of water inside cells.

## References

[^up147]: [[University Physics (OpenStax)]], Volume 1, ch. 14 "Fluid Mechanics", §14.7 "Viscosity and Turbulence" (viscosity defined with a fluid between two parallel plates, no slip at the plates, Table 14.4 of viscosities in 10⁻³ Pa·s, Poiseuille's law for flow and resistance).
[^up64]: [[University Physics (OpenStax)]], Volume 1, ch. 6 "Applications of Newton's Laws", §6.4 "Drag Force and Terminal Speed" (drag as a function of speed, quadratic drag $\frac{1}{2}C\rho Av^2$ and terminal speed) and the chapter's key equations (Stokes' law $F_s = 6\pi r\eta v$).
[^pboc12]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), ch. 12 "The Mathematics of Water" (hydrodynamics of water; viscous drag dominates the motion of swimming bacteria).
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), treatment of diffusion: the Einstein relation $D = k_B T/\zeta$, and protein diffusion about tenfold slower in the cytoplasm than in water.
[^svoboda]: [[Svoboda 1994 - Force and Velocity Measured for Single Kinesin Molecules]], *Cell* 77:773-784 (loads up to 5-6 pN).
