---
aliases:
  - Stokes Drag
  - Stokes Friction Coefficient
  - Loi de Stokes
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Viscosity]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Dimensional Analysis]]"
  - "[[Diffusion]]"
related:
  - "[[Reynolds Number]]"
  - "[[Centrifugation]]"
  - "[[Stokes-Einstein Relation]]"
  - "[[Brownian Motion]]"
  - "[[Boltzmann Distribution]]"
  - "[[Ribosome]]"
  - "[[Langevin Equation]]"
  - "[[Molecular Motor]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Stokes' Law

> [!abstract]
> A small sphere moving slowly through a fluid feels a drag proportional to its speed, $F = 6\pi\eta r v$. The factor $6\pi\eta r$ is its friction coefficient: it sets how fast the sphere sediments and, through Einstein's relation, how fast it diffuses.

## Definition

**Stokes' law** gives the drag force on a sphere of radius $r$ moving at speed $v$ through a fluid of viscosity $\eta$ when inertia is negligible (low [[Reynolds Number]]):[^up64][^pboc12]

$$F_s = 6\pi\eta r v,$$

directed against the velocity. The constant $\gamma = 6\pi\eta r$ (kg/s) is the sphere's **friction coefficient**, so that $\vec F = -\gamma\vec v$. Other texts write it $\zeta$ or $f$ ([[Diffusion]], [[Ribosome]]).

## Why it matters

- **Sedimentation.** How fast cells settle in a tube, and how organelles and macromolecules separate in a centrifuge, is buoyant weight divided by friction ([[Centrifugation]]). The sedimentation coefficients that name ribosomes (70S, 80S) and rRNAs (16S, 23S) are ratios of this kind.[^berg]
- **Sizes from diffusion.** With Einstein's relation, Stokes' law gives $D = k_B T/(6\pi\eta r)$: a size predicts a diffusion coefficient, and a measured diffusion coefficient gives a "hydrodynamic radius" ([[Stokes-Einstein Relation]]).
- **Simulation parameters.** Brownian dynamics and the [[Langevin Equation]] need a friction coefficient for each particle; for a sphere, Stokes' law supplies it.
- **Mass from sedimentation and diffusion together.** Friction depends on shape, which is usually unknown, but it cancels between $s$ and $D$, leaving the mass (Advanced; [[Centrifugation#Advanced (L3)]]).

## Core (L2)

### The law and the friction coefficient

Dimensional analysis alone fixes the form $F \propto \eta r v$ ([[Dimensional Analysis#Exercises|Dimensional Analysis, Exercise 3]]); solving the flow around the sphere gives the factor $6\pi$.[^up64] Two features stand out:

- **Drag grows with the radius, not the cross-section.** At low Reynolds number $F \propto r$; quadratic drag $\frac{1}{2}C\rho A v^2$ for large, fast objects scales with the area $A \propto r^2$ ([[Viscosity]]).
- **Drag depends on viscosity, not on the density of the fluid.** Fluid density enters only through buoyancy and the Reynolds number.

### Sedimentation at terminal velocity

![[stokes-sphere-terminal-velocity.svg]]

A sphere of density $\rho_p$ and volume $V = \frac{4}{3}\pi r^3$ in a fluid of density $\rho_f$ feels its weight $\rho_p V g$, the buoyant force $\rho_f V g$ (Archimedes' principle: the weight of the displaced fluid)[^up14] and the drag. Within a few relaxation times $\tau = m/\gamma$ ([[Viscosity]]) the forces balance, giving the **sedimentation velocity**

$$v_s = \frac{(\rho_p - \rho_f)Vg}{6\pi\eta r} = \frac{2r^2(\rho_p - \rho_f)\,g}{9\eta}.$$

Under gravity in water at 20 °C (computed below, illustrative sizes and densities):

| Particle | Radius | $\rho_p - \rho_f$ | $v_s$ | Time to fall 1 cm |
|---|---:|---:|---:|---:|
| protein | 2.5 nm | 350 kg/m³ | 4.8 × 10⁻¹² m/s | 67 years |
| bacterium | 0.5 µm | 100 kg/m³ | 5.4 × 10⁻⁸ m/s | 2.1 days |
| silica bead | 1 µm | 1000 kg/m³ | 2.2 × 10⁻⁶ m/s | 1.3 h |

Because $v_s \propto r^2$, a bacterium settles slowly and a protein never does. A centrifuge replaces $g$ by a much larger centrifugal acceleration: at 100,000 $g$ the same protein covers 1 cm in 5.8 h ([[Centrifugation]]).

Dividing the velocity by the acceleration removes the apparatus and leaves a property of the particle, the **sedimentation coefficient** $s = v_s/g = m(1 - \bar v\rho)/f$, where $m(1 - \bar v\rho)$ is the buoyant mass, $\bar v$ the partial specific volume of the particle, $\rho$ the solvent density and $f$ its friction coefficient; it is expressed in Svedberg units, 1 S = 10⁻¹³ s.[^berg] For the illustrative protein above, $s = 4.85$ S.

### From friction to diffusion: the Stokes-Einstein estimate

The Einstein relation links the diffusion coefficient to the friction coefficient, $D = k_B T/\gamma$.[^pboc] With Stokes' law:

$$D = \frac{k_B T}{6\pi\eta r}.$$

For the 2.5 nm protein at 20 °C, $D = 86$ µm²/s, the order of magnitude measured for proteins in water (about 100 µm²/s).[^pboc] At constant density $r \propto M^{1/3}$, so $D \propto M^{-1/3}$: a compact protein eight times heavier diffuses only twice as slowly. Read backwards, a measured $D$ defines the **hydrodynamic radius** $r_h = k_B T/(6\pi\eta D)$, the radius of the sphere with the same friction. Tests and limits of this relation are developed in [[Stokes-Einstein Relation]].

### Conditions of validity

- **Low Reynolds number.** Inertia must be negligible; for fast or large objects the drag becomes quadratic in speed ([[Reynolds Number]]).[^up64]
- **A sphere.** The friction coefficient depends on shape as well as size: a compact particle has a smaller friction coefficient than an extended one of the same mass.[^berg]
- **An isolated particle in a continuous fluid.** The derivation assumes a fluid without walls or neighbours, much larger than the solvent molecules; walls, crowding and particles of molecular size make the formula approximate.

## Advanced (L3)

**Why the drag is linear.** Newton's second law written for each small parcel of fluid, the Navier-Stokes equation, has an inertial term and a viscous term; their ratio is the [[Reynolds Number]].[^pboc12] When inertia is negligible what remains is linear in the velocity field: every stress is proportional to the speed and reverses when the motion reverses. Solving these linear equations around a sphere with no slip at its surface gives exactly $6\pi\eta r v$; the drawn streamlines show the consequence, a pattern ahead of the sphere that mirrors the one behind it.

**Shape and the hydrodynamic radius.** For a particle that is not a sphere, $\gamma = 6\pi\eta r_h$ defines $r_h$, and the friction exceeds that of a compact particle of the same mass.[^berg] An elongated protein or a stretch of DNA therefore has a larger $r_h$, a smaller $D$ and a smaller $s$ than a compact sphere of equal mass. A radius computed from $D$ is a friction-equivalent radius, not a geometric one.

**Sedimentation against diffusion.** In a tube at equilibrium, the downward sedimentation flux $v_s c$ is balanced by the upward diffusive flux $-D\,dc/dh$, so the concentration decays with height $h$ as

$$c(h) = c(0)\,e^{-h/\ell_g}, \qquad \ell_g = \frac{D}{v_s} = \frac{k_B T/\gamma}{m_b g/\gamma} = \frac{k_B T}{m_b g},$$

with $m_b$ the buoyant mass. The friction coefficient cancels: the equilibrium profile depends on the buoyant mass alone, as the [[Boltzmann Distribution]] predicts for a potential energy $m_b g h$. For the illustrative protein $\ell_g = 18$ m, for the bacterium 7.9 µm, for the silica bead 0.1 µm (table code below): proteins stay uniformly mixed in any tube, while bacteria and beads end up near the bottom. This cancellation is why sedimentation equilibrium and the combination of $s$ with $D$ measure molar masses without knowing the shape ([[Centrifugation]]).

## Mathematical representation

- **Drag.** $\vec F = -\gamma\vec v$, $\gamma = 6\pi\eta r$, valid for $\mathrm{Re} \ll 1$; $[\gamma] = \text{Pa s m} = \text{kg s}^{-1}$.
- **Terminal velocity.** With $m_b = (\rho_p - \rho_f)V$ the buoyant mass and $a$ the acceleration of the field ($g$, or $\omega^2 r$ in a centrifuge): $v_s = m_b a/\gamma$; for a sphere in gravity $v_s = 2r^2(\rho_p - \rho_f)g/(9\eta)$.
- **Sedimentation coefficient.** $s = v_s/a = m_b/f$, in seconds (1 S = 10⁻¹³ s). For a homogeneous particle $\bar v = 1/\rho_p$, so $m_b = m(1 - \bar v\rho_f)$.
- **Stokes-Einstein.** $D = k_B T/(6\pi\eta r)$; hydrodynamic radius $r_h = k_B T/(6\pi\eta D)$.
- **Sedimentation-diffusion equilibrium.** Zero net flux, $-D\,c'(h) - v_s c(h) = 0$, gives $c(h) = c(0)e^{-h v_s/D}$ with $D/v_s = k_B T/(m_b g)$.

## Computational representation

Sedimentation velocities, Stokes-Einstein diffusion coefficients and the equilibrium length $D/v_s$, with $k_B$ exact and the standard value of $g$:[^nist]

```python
import math

K_B = 1.380649e-23           # J/K, exact (SI 2019)
G = 9.80665                  # m/s^2, standard gravity (exact by convention)
ETA_20 = 1.002e-3            # Pa s, water at 20 C
T_20 = 293.15                # K


def stokes_friction(r: float, eta: float = ETA_20) -> float:
    """Friction coefficient gamma = 6 pi eta r of a sphere, kg/s."""
    return 6 * math.pi * eta * r


def buoyant_mass(r: float, delta_rho: float) -> float:
    """Mass minus displaced fluid: (4/3) pi r^3 (rho_p - rho_f), kg."""
    return 4 / 3 * math.pi * r**3 * delta_rho


def sedimentation_velocity(r: float, delta_rho: float, accel: float = G, eta: float = ETA_20) -> float:
    """Terminal velocity: buoyant weight divided by the friction coefficient, m/s."""
    return buoyant_mass(r, delta_rho) * accel / stokes_friction(r, eta)


def stokes_einstein(r: float, T: float = T_20, eta: float = ETA_20) -> float:
    """Diffusion coefficient D = k_B T / (6 pi eta r), m^2/s."""
    return K_B * T / stokes_friction(r, eta)


def readable(t: float) -> str:
    for unit, s in (("years", 3.156e7), ("days", 86400), ("h", 3600), ("min", 60), ("s", 1)):
        if t >= s:
            return f"{t / s:.2g} {unit}"
    return f"{t:.2g} s"


particles = {                # radius (m), density excess over water (kg/m^3): illustrative round values
    "protein": (2.5e-9, 350.0),
    "bacterium": (0.5e-6, 100.0),
    "silica bead": (1e-6, 1000.0),
}
for name, (r, drho) in particles.items():
    v = sedimentation_velocity(r, drho)
    D = stokes_einstein(r)
    print(f"{name:11s}  v_s = {v:.1e} m/s  falls 1 cm in {readable(0.01 / v):10s}"
          f"  D = {D * 1e12:.3g} um^2/s  D/v_s = {D / v:.2g} m")
```

```text
protein      v_s = 4.8e-12 m/s  falls 1 cm in 67 years    D = 85.7 um^2/s  D/v_s = 18 m
bacterium    v_s = 5.4e-08 m/s  falls 1 cm in 2.1 days    D = 0.429 um^2/s  D/v_s = 7.9e-06 m
silica bead  v_s = 2.2e-06 m/s  falls 1 cm in 1.3 h       D = 0.214 um^2/s  D/v_s = 9.9e-08 m
```

Pass `accel=1e5 * G` to model a centrifuge at 100,000 $g$. Keep SI units inside the functions and convert only when printing: a radius entered in nm instead of m changes $v_s$ by $10^{18}$.

## Worked example

> [!example] From the size of a protein to its D and s
> A compact protein modeled as a sphere of radius 2.5 nm, 350 kg/m³ denser than water (illustrative), in water at 20 °C ($\eta = 1.002$ mPa·s).
> 1. **Friction.** $\gamma = 6\pi\eta r = 4.72 \times 10^{-11}$ kg/s.
> 2. **Diffusion.** $k_B T = 1.380649 \times 10^{-23} \times 293.15 = 4.047 \times 10^{-21}$ J, so $D = k_BT/\gamma = 8.57 \times 10^{-11}$ m²/s $= 86$ µm²/s.
> 3. **Buoyant mass.** $m_b = \frac{4}{3}\pi r^3 \Delta\rho = 6.54 \times 10^{-26} \times 350 = 2.29 \times 10^{-23}$ kg.
> 4. **Sedimentation coefficient.** $s = m_b/\gamma = 4.85 \times 10^{-13}$ s $= 4.85$ S.
> 5. **In a centrifuge.** At 100,000 $g$, $v_s = s \times 10^5 g = 4.8 \times 10^{-7}$ m/s: 1 cm in 5.8 h, against 67 years under gravity.
> 6. **Check.** $D/v_s$ at 1 $g$ is $k_BT/(m_b g) = 18$ m, consistent with the table: friction cancels in this ratio.

## Common misconceptions

> [!warning] "Drag is always proportional to speed"
> Only at low Reynolds number. A falling person or a swimming fish feels a drag that grows as $v^2$ and with the cross-sectional area.[^up64] Applying Stokes' law to them underestimates the drag by orders of magnitude ([[Reynolds Number]]).

> [!warning] "Heavier particles always sediment faster"
> What drives sedimentation is the buoyant mass, and what resists it is the friction. A particle sinks when it is denser than the solvent, floats when it is less dense, and does not move at all when the densities match, however heavy it is.[^berg] Density-gradient centrifugation exploits exactly this ([[Centrifugation]]).

> [!warning] "The Stokes-Einstein radius is the size of the molecule"
> It is the radius of the sphere with the same friction. An extended molecule has more friction than a compact one of the same mass,[^berg] so its hydrodynamic radius overestimates its compact size, and turning $r_h$ into a mass assumes a shape.

## Exercises

> [!question] Exercise 1 (L2)
> What drag acts on a bead of radius 1 µm moving at 10 µm/s through water at 20 °C? Express it in pN.

> [!success]- Solution
> $F = 6\pi \times 1.002 \times 10^{-3} \times 10^{-6} \times 10^{-5} = 1.89 \times 10^{-13}$ N $= 0.19$ pN. Optical-trap forces of piconewtons therefore move such beads at tens of µm/s.

> [!question] Exercise 2 (L2)
> Model a yeast cell as a sphere of radius 2.5 µm, 100 kg/m³ denser than water (illustrative values). How fast does it settle at 20 °C, and how long does a 5 cm culture take to clear? What if the radius doubles?

> [!success]- Solution
> $v_s = 2r^2\Delta\rho g/(9\eta) = 2 \times (2.5 \times 10^{-6})^2 \times 100 \times 9.81/(9 \times 1.002 \times 10^{-3}) = 1.36$ µm/s; 5 cm takes $0.05/1.36 \times 10^{-6} = 3.7 \times 10^4$ s, about 10 h. Doubling the radius multiplies $v_s$ by 4: about 2.5 h.

> [!question] Exercise 3 (L2)
> Estimate the diffusion coefficient of a sphere of radius 5 nm in water at 37 °C ($\eta = 0.6947$ mPa·s), and the time it needs to diffuse 1 µm in one dimension.

> [!success]- Solution
> $D = k_B T/(6\pi\eta r) = 1.380649 \times 10^{-23} \times 310.15/(6\pi \times 0.6947 \times 10^{-3} \times 5 \times 10^{-9}) = 6.54 \times 10^{-11}$ m²/s $= 65$ µm²/s. Time $t = x^2/2D = 10^{-12}/(1.31 \times 10^{-10}) = 7.6$ ms ([[Diffusion]]).

> [!question] Exercise 4 (L3)
> Show that the equilibrium length $\ell_g = D/v_s$ depends neither on the viscosity nor on the shape of the particle. For the illustrative protein ($m_b = 2.29 \times 10^{-23}$ kg) at 20 °C, compute $\ell_g$ and the concentration ratio between the top and the bottom of a 1 cm tube. Conclude.

> [!success]- Solution
> $D = k_BT/\gamma$ and $v_s = m_b g/\gamma$, so $D/v_s = k_BT/(m_b g)$: $\gamma$, which carries $\eta$ and the shape, cancels. $\ell_g = 4.047 \times 10^{-21}/(2.29 \times 10^{-23} \times 9.81) = 18$ m, and $c(1\ \text{cm})/c(0) = e^{-0.01/18} = 0.99945$. Gravity cannot separate proteins; an acceleration $10^5$ times larger brings $\ell_g$ down to 0.18 mm, which is why sedimentation equilibrium of macromolecules needs an ultracentrifuge ([[Centrifugation]]).

> [!question] Exercise 5 (L3, Python)
> A tool reports $D = 60 \pm 6$ µm²/s (invented) for a protein in water at 20 °C. Compute the hydrodynamic radius at $D$ and at both ends of the interval, then the mass of a sphere of that radius with density 1350 kg/m³ (assumed). How does a 10 % error in $D$ propagate to the mass?

> [!success]- Solution
> ```python
> import math
>
> K_B, T_20, ETA_20 = 1.380649e-23, 293.15, 1.002e-3
> D_meas, rel_err = 60e-12, 0.10                       # m^2/s at 20 C, invented, +/- 10 %
> for D in (D_meas * (1 + rel_err), D_meas, D_meas * (1 - rel_err)):
>     r_h = K_B * T_20 / (6 * math.pi * ETA_20 * D)    # hydrodynamic radius
>     m = 4 / 3 * math.pi * r_h**3 * 1350.0            # sphere of density 1350 kg/m^3 (assumed)
>     print(f"D = {D * 1e12:4.0f} um^2/s  r_h = {r_h * 1e9:.2f} nm  M = {m / 1.66053906660e-27 / 1e3:5.0f} kDa")
> ```
> ```text
> D =   66 um^2/s  r_h = 3.25 nm  M =   117 kDa
> D =   60 um^2/s  r_h = 3.57 nm  M =   155 kDa
> D =   54 um^2/s  r_h = 3.97 nm  M =   213 kDa
> ```
> $M \propto r_h^3 \propto D^{-3}$, so ±10 % on $D$ becomes −25 % to +37 % on the mass, before any error from the assumed density and spherical shape. Masses from diffusion alone are rough; combining $D$ with $s$ removes the shape (Exercise 4, [[Centrifugation]]).

## Mastery checklist

- [ ] 1 Recognized: I can state $F = 6\pi\eta r v$, name $\gamma$ the friction coefficient and give the condition of low Reynolds number.
- [ ] 2 Understood: I can derive the sedimentation velocity from a force balance with buoyancy and explain why it scales as $r^2$.
- [ ] 3 Practiced: I compute drag, sedimentation velocities, sedimentation coefficients and Stokes-Einstein diffusion coefficients in SI units, in code.
- [ ] 4 Applied: I estimated a hydrodynamic radius or a diffusion coefficient for a real protein and compared it with a measured value.
- [ ] 5 Explained: I can explain why friction cancels in $D/v_s$, what a hydrodynamic radius means for non-spherical molecules, and when Stokes' law fails.

## References

[^up64]: [[University Physics (OpenStax)]], Volume 1, ch. 6 "Applications of Newton's Laws", §6.4 "Drag Force and Terminal Speed" (drag as a function of speed, quadratic drag $\frac{1}{2}C\rho Av^2$ for larger objects, terminal speed) and the chapter's key equations (Stokes' law $F_s = 6\pi r\eta v$).
[^up14]: [[University Physics (OpenStax)]], Volume 1, ch. 14 "Fluid Mechanics" (Archimedes' principle and buoyancy).
[^pboc12]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), ch. 12 "The Mathematics of Water" (hydrodynamics of water and drag at low Reynolds number).
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), treatment of diffusion: the Einstein relation $D = k_BT/\zeta$ and diffusion coefficients of proteins in water (about 100 µm²/s).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of ultracentrifugation and sedimentation coefficients ($s = m(1 - \bar v\rho)/f$, Svedberg units of 10⁻¹³ s, larger frictional coefficient for extended than for compact particles of the same mass, particles that sink, float or stay according to $\bar v\rho$).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]]: Boltzmann constant $1.380\,649 \times 10^{-23}$ J K⁻¹ (exact since the 2019 SI) and standard acceleration of gravity 9.806 65 m s⁻² (exact, conventional value).
