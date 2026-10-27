---
aliases:
  - Re
  - Low Reynolds Number
  - Nombre de Reynolds
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Viscosity]]"
  - "[[Stokes' Law]]"
  - "[[Dimensional Analysis]]"
  - "[[Newton's Laws of Motion]]"
related:
  - "[[Momentum]]"
  - "[[Diffusion]]"
  - "[[Bacteria]]"
  - "[[Molecular Motor]]"
  - "[[Order-of-Magnitude Estimation]]"
  - "[[Gel Electrophoresis]]"
  - "[[Langevin Equation]]"
  - "[[ATP]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[Purcell 1977 - Life at Low Reynolds Number]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
---

# Reynolds Number

> [!abstract]
> The Reynolds number compares inertial and viscous forces in a flow. It is huge for a swimming human and tiny for bacteria and proteins, which live in a world without momentum: motion stops as soon as the push stops.

## Definition

The **Reynolds number** of a flow is the dimensionless ratio

$$\mathrm{Re} = \frac{\rho v L}{\eta},$$

with $\rho$ the density of the fluid, $v$ a typical speed, $L$ a characteristic length (the diameter of a tube, the size of a moving object) and $\eta$ the [[Viscosity]].[^up147] It measures the importance of inertial forces relative to viscous forces.[^pboc12] For flow in a tube, experiments show laminar flow below about 2000, turbulent flow above about 3000, and an unstable flow in between.[^up147]

## Why it matters

- **Choosing the model.** When $\mathrm{Re} \ll 1$, drop inertia: velocity is proportional to force, drag follows [[Stokes' Law]], and Brownian dynamics or the overdamped [[Langevin Equation]] apply. When $\mathrm{Re} \gg 1$, keep inertia and use quadratic drag. Like every dimensionless ratio, it says which term of a model can be dropped ([[Order-of-Magnitude Estimation]]).
- **Swimming cells.** Bacteria and other microorganisms move under low-Reynolds rules: no coasting, and a stroke that is simply reversed gets nowhere.[^purcell] Models of motility and chemotaxis of [[Bacteria]] start from these rules.
- **Drift in fields.** A charged molecule in water reaches its terminal drift velocity within picoseconds, so its velocity, not its acceleration, is proportional to the electric force: the basis of electrophoretic mobility ([[Gel Electrophoresis]], [[Electric Field]]).
- **Microfluidics.** Flows in narrow channels are laminar: two streams flow side by side and mix only by [[Diffusion]] (Advanced).

## Core (L2)

### Two forces, one ratio

An order-of-magnitude estimate for an object of size $L$ moving at speed $v$ ([[Dimensional Analysis]]):

- **Inertial force**: the fluid set in motion each second carries momentum. Mass flowing past per second $\sim \rho v L^2$, times velocity $v$: $F_\text{inertial} \sim \rho v^2 L^2$ ([[Momentum]]).
- **Viscous force**: shear stress $\sim \eta v/L$ acting over an area $L^2$: $F_\text{viscous} \sim \eta v L$.

Their ratio is $\rho v^2 L^2/(\eta v L) = \rho v L/\eta = \mathrm{Re}$. The two drag laws give the same ratio: for a sphere, quadratic drag over Stokes drag is $\frac{1}{2}C\rho\pi r^2v^2/(6\pi\eta r v) = \frac{C}{24}\cdot\frac{2\rho r v}{\eta}$, so for a drag coefficient $C$ of order one, Stokes drag wins exactly when the Reynolds number built on the diameter is small.[^up64]

### Reynolds numbers of the living world

![[reynolds-number-scale.svg]]

In water at 20 °C ($\rho = 1000$ kg/m³, $\eta = 1.002$ mPa·s; computed below):

| System | Size $L$ | Speed $v$ | Re |
|---|---:|---:|---:|
| protein pulled by a motor | 5 nm | 1 µm/s | 5 × 10⁻⁹ |
| *E. coli* swimming | 1 µm | 30 µm/s[^pboc12] | 3 × 10⁻⁵ |
| protein at its thermal speed | 5 nm | 7 m/s | 0.035 |
| microfluidic channel | 50 µm | 1 mm/s | 0.05 |
| human swimmer | 2 m | 1 m/s | 2 × 10⁶ |

Sizes and speeds are illustrative, except the *E. coli* speed; 7 m/s is the one-dimensional thermal speed $\sqrt{k_BT/m}$ of a 50 kDa protein ([[Kinetic Energy]]). Even at its thermal speed, which it keeps for about a picosecond, a protein has $\mathrm{Re} < 0.1$. The same water that is "thin" for a swimmer is, for a bacterium, a medium where inertia is about 30,000 times weaker than friction.

### No coasting

After the force stops, a sphere glides a distance $d = v\tau$ with $\tau = m/\gamma = 2\rho_p r^2/(9\eta)$ ([[Viscosity]]). Measured in its own size:

$$\frac{d}{r} = \frac{2}{9}\,\frac{\rho_p}{\rho}\,\frac{\rho v r}{\eta},$$

the Reynolds number built on the radius, times a factor of order one: **Re is how far you coast, in body sizes**. Modeling *E. coli* as a sphere of radius 1 µm at 30 µm/s gives $\tau = 0.22$ µs and $d = 0.07$ Å. A protein at its thermal speed stops within about 0.1 Å, in about a picosecond. Purcell made the point for microorganisms: they cannot coast; when the motor stops, the cell stops.[^purcell] A protein stops as soon as the force stops, not because motion needs a force, but because drag cancels its velocity at once ([[Newton's Laws of Motion#Common misconceptions]]).

### Swimming without inertia

At $\mathrm{Re} \ll 1$ the flow at each instant is set by the current motion of the swimmer's surface, with no memory of the past (Advanced). If a sequence of shapes is run backwards, the swimmer retraces its path exactly, and running it faster or slower changes nothing. Hence Purcell's **scallop theorem**: a body with a single hinge, which can only open and close, does not advance, even if it closes faster than it opens.[^purcell] Swimming needs a cycle of shapes that is not its own reverse; Purcell's minimal example is a three-link body with two hinges.[^purcell]

Bacteria solve the problem by rotation. *E. coli* turns helical flagella with rotary motors at their base: counterclockwise rotation gives smooth swimming (a run), clockwise rotation a tumble that reorients the cell, and chemotaxis tunes how often runs end.[^alberts] Rotation in one direction is never undone, so it propels continuously. The motor runs on a proton gradient rather than on ATP.[^pboc12] The cost is small: in the sphere model the drag is $\gamma v = 0.57$ pN and the power $\gamma v^2 = 1.7 \times 10^{-17}$ W, about 4200 $k_BT$ per second, or some 210 ATP equivalents per second at about 20 $k_BT$ per ATP.[^pboc12]

## Advanced (L3)

**Where Re comes from.** The Navier-Stokes equation, Newton's second law per unit volume of fluid with velocity field $\vec u$ and pressure $p$, reads $\rho(\partial_t\vec u + (\vec u\cdot\nabla)\vec u) = -\nabla p + \eta\nabla^2\vec u$, with $\nabla\cdot\vec u = 0$ for water.[^pboc12] Measure lengths in units of $L$, velocities in $U$, times in $L/U$ and pressures in $\eta U/L$:

$$\mathrm{Re}\left(\partial_{t'}\vec u' + (\vec u'\cdot\nabla')\vec u'\right) = -\nabla' p' + \nabla'^2\vec u'.$$

All inertia sits on the left, multiplied by Re. As $\mathrm{Re} \to 0$ what remains, $\eta\nabla^2\vec u = \nabla p$, is linear and contains no time derivative: the flow follows the boundaries instantly, doubles when their speed doubles and reverses when they reverse. This is the root of Stokes drag ([[Stokes' Law#Advanced (L3)]]) and of the scallop theorem. At large Re the inertial terms dominate, and in pipes the flow becomes turbulent above about 2000 to 3000.[^up147]

**Swimming does not stir.** Small molecules that a bacterium feeds on diffuse with $D \approx 500$ µm²/s.[^pboc12] Swimming at $v$ beats diffusion only beyond the crossover distance $x^* = 2D/v$ ([[Diffusion]]): $2 \times 500/30 = 33$ µm, many body lengths, covered in 1.1 s either way. Near the cell, diffusion brings food faster than swimming could; swimming pays only over longer distances, to reach better surroundings, which is what chemotaxis does. The ratio $vL/D$ plays for transport the role Re plays for forces.

**Laminar microchannels.** In a 50 µm channel at 1 mm/s ($\mathrm{Re} = 0.05$), two streams injected side by side do not mix by turbulence. Mixing across the channel takes about $w^2/2D = (50\ \text{µm})^2/(2 \times 500\ \text{µm}^2/\text{s}) = 2.5$ s for such small molecules, during which the fluid travels 2.5 mm: microfluidic devices are designed around this diffusion-limited mixing.

## Mathematical representation

- $\mathrm{Re} = \rho v L/\eta$: dimensionless, $[\rho v L/\eta] = (\text{M L}^{-3})(\text{L T}^{-1})(\text{L})/(\text{M L}^{-1}\text{T}^{-1}) = 1$.
- Force ratio: $F_\text{inertial}/F_\text{viscous} \sim \rho v^2 L^2/(\eta v L) = \mathrm{Re}$. Drag ratio for a sphere: $F_\text{quad}/F_\text{Stokes} = (C/24)\,\mathrm{Re}_d$ with $\mathrm{Re}_d = 2\rho r v/\eta$.
- Coasting of a sphere: $d = v\tau$, $\tau = 2\rho_p r^2/(9\eta)$, so $d/r = \frac{2}{9}(\rho_p/\rho)\,\mathrm{Re}_r$ with $\mathrm{Re}_r = \rho v r/\eta$.
- Dimensionless Navier-Stokes: $\mathrm{Re}(\partial_t\vec u + (\vec u\cdot\nabla)\vec u) = -\nabla p + \nabla^2\vec u$; the limit $\mathrm{Re} \to 0$ gives the linear, time-independent Stokes equations.
- Tube flow: laminar for $\mathrm{Re} \lesssim 2000$, turbulent for $\mathrm{Re} \gtrsim 3000$, with $L$ the diameter.

## Computational representation

```python
import math

RHO_WATER = 1000.0           # kg/m^3, rounded
ETA_20 = 1.002e-3            # Pa s, water at 20 C
K_B, T_20 = 1.380649e-23, 293.15


def reynolds(speed: float, length: float, rho: float = RHO_WATER, eta: float = ETA_20) -> float:
    """Re = rho v L / eta: inertial over viscous forces (dimensionless)."""
    return rho * speed * length / eta


def coasting_distance(speed: float, radius: float, rho_p: float = RHO_WATER, eta: float = ETA_20) -> float:
    """Distance a sphere glides after the force stops: v * tau, tau = 2 rho_p r^2 / (9 eta)."""
    return speed * 2 * rho_p * radius**2 / (9 * eta)


cases = {                    # (speed m/s, size m); illustrative values except the E. coli speed
    "protein, motor-driven": (1e-6, 5e-9),
    "protein, thermal speed": (7.0, 5e-9),
    "E. coli swimming": (30e-6, 1e-6),
    "microfluidic channel": (1e-3, 50e-6),
    "human swimmer": (1.0, 2.0),
}
for name, (v, L) in cases.items():
    print(f"{name:23s} Re = {reynolds(v, L):8.1e}")

v, r = 30e-6, 1e-6                                    # E. coli as a sphere of radius 1 um
d = coasting_distance(v, r)
tau = 2 * RHO_WATER * r**2 / (9 * ETA_20)
print(f"E. coli coasts {d * 1e10:.2f} angstrom in tau = {tau * 1e6:.2f} us; d/r = {d / r:.1e}")
gamma = 6 * math.pi * ETA_20 * r
power = gamma * v**2                                  # drag force times speed
print(f"drag {gamma * v * 1e12:.2f} pN, power {power:.1e} W = {power / (K_B * T_20):.0f} kT/s")
```

```text
protein, motor-driven   Re =  5.0e-09
protein, thermal speed  Re =  3.5e-02
E. coli swimming        Re =  3.0e-05
microfluidic channel    Re =  5.0e-02
human swimmer           Re =  2.0e+06
E. coli coasts 0.07 angstrom in tau = 0.22 us; d/r = 6.7e-06
drag 0.57 pN, power 1.7e-17 W = 4200 kT/s
```

The sphere is a crude model of a rod-shaped cell with flagella; it gets orders of magnitude right, which is all these conclusions need.

## Worked example

> [!example] Why *E. coli* cannot glide
> *E. coli* modeled as a sphere of radius $r = 1$ µm swimming at 30 µm/s in water at 20 °C.
> 1. **Reynolds number.** $\mathrm{Re} = \rho v L/\eta = 1000 \times 30 \times 10^{-6} \times 10^{-6}/1.002 \times 10^{-3} = 3.0 \times 10^{-5}$: viscous forces dominate by more than four orders of magnitude.
> 2. **Relaxation time.** $\tau = 2\rho r^2/(9\eta) = 2 \times 1000 \times 10^{-12}/(9 \times 1.002 \times 10^{-3}) = 2.2 \times 10^{-7}$ s.
> 3. **Coasting distance.** $d = v\tau = 30 \times 10^{-6} \times 2.2 \times 10^{-7} = 6.7 \times 10^{-12}$ m, less than a tenth of an ångström: $d/r = 6.7 \times 10^{-6}$, of the order of Re.
> 4. **Force and power.** Drag $\gamma v = 6\pi\eta r v = 0.57$ pN; power $\gamma v^2 = 1.7 \times 10^{-17}$ W, about 4200 $k_BT$/s at 20 °C.
> 5. **Consequence.** The cell moves only while its flagella turn, and only because rotation is not a reciprocal motion.[^purcell]

## Common misconceptions

> [!warning] "The Reynolds number is a property of the fluid"
> It combines the fluid ($\rho$, $\eta$) with the size and speed of the object. The same water gives $\mathrm{Re} = 3 \times 10^{-5}$ for a bacterium and $2 \times 10^6$ for a swimmer.

> [!warning] "A microorganism can glide between strokes"
> A bacterium that stops its flagella stops within a fraction of a microsecond, after less than a tenth of an ångström. There is no gliding at low Re.[^purcell]

> [!warning] "A fast power stroke and a slow recovery stroke make a swimmer advance"
> At low Re the displacement depends on the sequence of shapes, not on the speed at which it is run. A reciprocal stroke, fast one way and slow the other, gives zero net motion: the scallop theorem.[^purcell]

## Exercises

> [!question] Exercise 1 (L2)
> Compute Re in water at 20 °C for *E. coli* (1 µm, 30 µm/s) and for a 2 m swimmer at 1 m/s. By what factor do they differ, and which drag law applies to each?

> [!success]- Solution
> *E. coli*: $1000 \times 3 \times 10^{-5} \times 10^{-6}/1.002 \times 10^{-3} = 3.0 \times 10^{-5}$. Swimmer: $1000 \times 1 \times 2/1.002 \times 10^{-3} = 2.0 \times 10^6$. Ratio about $7 \times 10^{10}$. Stokes (linear) drag for the bacterium, quadratic drag for the swimmer.

> [!question] Exercise 2 (L2)
> Water at 20 °C flows at 0.5 m/s through a tube of 2 mm diameter. Is the flow laminar? Between which speeds does it become unstable, then turbulent?

> [!success]- Solution
> $\mathrm{Re} = 1000 \times 0.5 \times 2 \times 10^{-3}/1.002 \times 10^{-3} = 998$: laminar. $\mathrm{Re} = 2000$ at $v = 2000\eta/(\rho L) = 1.0$ m/s and 3000 at 1.5 m/s: unstable between 1.0 and 1.5 m/s, turbulent above.

> [!question] Exercise 3 (L2)
> Starting from $d = v\tau$ and $\tau = m/(6\pi\eta r)$, show that the coasting distance of a sphere in units of its radius is $\frac{2}{9}(\rho_p/\rho)\mathrm{Re}_r$. Evaluate it for *E. coli* and for a protein of radius 2.5 nm at 7 m/s (density of water).

> [!success]- Solution
> $m = \frac{4}{3}\pi r^3\rho_p$, so $\tau = 2\rho_p r^2/(9\eta)$ and $d/r = 2\rho_p v r/(9\eta) = \frac{2}{9}\frac{\rho_p}{\rho}\frac{\rho v r}{\eta}$. *E. coli*: $\mathrm{Re}_r = 3.0 \times 10^{-5}$, $d/r = 6.7 \times 10^{-6}$, $d = 0.07$ Å. Protein: $\tau = 1.4$ ps, $d = 7 \times 1.4 \times 10^{-12} = 1.0 \times 10^{-11}$ m, about 0.1 Å.

> [!question] Exercise 4 (L3)
> At low Re a swimmer's velocity is linear in the rates of change of its shape: with one hinge angle $\theta$, $V = f(\theta)\,\dot\theta$. (a) Show that any stroke that opens from $\theta_1$ to $\theta_2$ and closes back gives zero net displacement, whatever the speeds. (b) With two hinges, $V = f_1(\theta_1,\theta_2)\dot\theta_1 + f_2(\theta_1,\theta_2)\dot\theta_2$. Why can a cycle now produce net motion?

> [!success]- Solution
> (a) $X = \int V\,dt = \int f(\theta)\,\dot\theta\,dt = \int f(\theta)\,d\theta$: time drops out (only the path in shape space matters). Opening and closing traverse the same interval in opposite directions, so $X = \int_{\theta_1}^{\theta_2} f\,d\theta + \int_{\theta_2}^{\theta_1} f\,d\theta = 0$. (b) Now $X = \oint (f_1\,d\theta_1 + f_2\,d\theta_2)$ around a loop in the $(\theta_1, \theta_2)$ plane. By Green's theorem this equals $\iint (\partial f_2/\partial\theta_1 - \partial f_1/\partial\theta_2)\,d\theta_1\,d\theta_2$ over the enclosed area, nonzero in general: a non-reciprocal cycle encloses area, a reciprocal one does not. This is why Purcell's swimmer needs two hinges.[^purcell]

> [!question] Exercise 5 (L3, Python)
> Assume, as a rough illustrative rule, that every swimmer moves at 10 body lengths per second. Compute Re for body lengths from 1 µm to 1 m, the length at which Re = 1, and the coasting distance in body lengths where drag is still linear (sphere of diameter $L$).

> [!success]- Solution
> ```python
> import math
>
> RHO_WATER, ETA_20 = 1000.0, 1.002e-3
>
>
> def reynolds(speed, length, rho=RHO_WATER, eta=ETA_20):
>     return rho * speed * length / eta
>
>
> def coasting_distance(speed, radius, rho_p=RHO_WATER, eta=ETA_20):
>     return speed * 2 * rho_p * radius**2 / (9 * eta)
>
>
> for L in (1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.0):  # every swimmer at 10 body lengths per second
>     Re = reynolds(10 * L, L)
>     coast = f"{coasting_distance(10 * L, L / 2) / L:.1e} body lengths" if Re < 1 else "drag no longer linear"
>     print(f"L = {L:7.0e} m  Re = {Re:8.1e}  coast: {coast}")
> print(f"Re = 1 at L = {math.sqrt(ETA_20 / (10 * RHO_WATER)) * 1e3:.2f} mm")
> ```
> ```text
> L =   1e-06 m  Re =  1.0e-05  coast: 5.5e-07 body lengths
> L =   1e-05 m  Re =  1.0e-03  coast: 5.5e-05 body lengths
> L =   1e-04 m  Re =  1.0e-01  coast: 5.5e-03 body lengths
> L =   1e-03 m  Re =  1.0e+01  coast: drag no longer linear
> L =   1e-02 m  Re =  1.0e+03  coast: drag no longer linear
> L =   1e-01 m  Re =  1.0e+05  coast: drag no longer linear
> L =   1e+00 m  Re =  1.0e+07  coast: drag no longer linear
> Re = 1 at L = 0.32 mm
> ```
> With $v = 10L$, $\mathrm{Re} = 10\rho L^2/\eta \propto L^2$: each factor 10 in size is a factor 100 in Re. Under this rule the viscous world ends near a third of a millimetre. Where drag is linear, the coasting distance stays a small fraction of the body, falling with $L^2$.

## Mastery checklist

- [ ] 1 Recognized: I can write $\mathrm{Re} = \rho vL/\eta$, say what it compares, and quote the 2000 to 3000 transition for pipe flow.
- [ ] 2 Understood: I can derive Re as a ratio of forces and explain why bacteria and proteins cannot coast.
- [ ] 3 Practiced: I compute Re, relaxation times and coasting distances for molecules, cells and channels, and pick the right drag law.
- [ ] 4 Applied: I used a Reynolds-number estimate to justify an overdamped (Brownian or Langevin) model, or to design or interpret a microfluidic or motility experiment.
- [ ] 5 Explained: I can teach the scallop theorem, why rotating flagella escape it, and how the Navier-Stokes equation reduces to the Stokes equations at low Re.

## References

[^up147]: [[University Physics (OpenStax)]], Volume 1, ch. 14 "Fluid Mechanics", §14.7 "Viscosity and Turbulence" (Reynolds number for flow in a tube and for an object moving through a fluid; laminar below about 2000, turbulent above about 3000, unstable in between).
[^up64]: [[University Physics (OpenStax)]], Volume 1, ch. 6 "Applications of Newton's Laws", §6.4 "Drag Force and Terminal Speed" (quadratic drag $\frac{1}{2}C\rho Av^2$) and the chapter's key equations (Stokes' law).
[^pboc12]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), ch. 12 "The Mathematics of Water" (Navier-Stokes equation, Reynolds number as the ratio of inertial to viscous forces, swimming bacteria; end-of-chapter problems: *E. coli* swimming at about 30 µm/s, food molecules diffusing at about 500 µm²/s, a flagellar motor driven by a proton gradient, about 20 $k_BT$ per ATP).
[^purcell]: [[Purcell 1977 - Life at Low Reynolds Number]], *American Journal of Physics* 45(1):3-11 (no coasting at low Reynolds number, the scallop theorem, the three-link swimmer).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of bacterial chemotaxis (helical flagella turned by rotary motors; counterclockwise rotation gives smooth swimming, clockwise rotation tumbling).
