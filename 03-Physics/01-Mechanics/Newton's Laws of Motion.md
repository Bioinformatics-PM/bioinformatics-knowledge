---
aliases:
  - Newton's Laws
  - F = ma
  - Newton's Second Law
  - Free-Body Diagram
  - Lois de Newton
  - Principe fondamental de la dynamique
tags:
  - type/concept
  - domain/physics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Kinematics]]"
  - "[[Vector]]"
  - "[[Derivative]]"
related:
  - "[[Momentum]]"
  - "[[Work (Physics)]]"
  - "[[Potential Energy]]"
  - "[[Hooke's Law]]"
  - "[[Harmonic Oscillator]]"
  - "[[Euler Method]]"
  - "[[Molecular Dynamics Simulation]]"
  - "[[Langevin Equation]]"
  - "[[Reynolds Number]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[MIT 8.01SC - Classical Mechanics]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Svoboda 1994 - Force and Velocity Measured for Single Kinesin Molecules]]"
  - "[[Verlet 1967 - Computer Experiments on Classical Fluids]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
---

# Newton's Laws of Motion

> [!abstract]
> Forces change motion: an object keeps its velocity unless a net force acts, the net force equals mass times acceleration, and every force comes paired with an equal and opposite one on another object. Molecular dynamics is these three sentences integrated for every atom.

## Definition

**Newton's three laws**, valid in an inertial frame of reference:[^up5][^801]

1. **First law (inertia).** A body at rest stays at rest, and a body in motion keeps a constant velocity, unless a net external force acts on it.
2. **Second law.** The net external force on a body equals its mass times its acceleration: $\vec F_{\text{net}} = \sum \vec F = m\vec a$.
3. **Third law.** If body A exerts a force $\vec F_{AB}$ on body B, then B exerts $\vec F_{BA} = -\vec F_{AB}$ on A. The two forces act on **different** bodies.

The SI unit of force is the **newton**, 1 N = 1 kg m s⁻² ([[Dimensional Analysis]]).[^up5]

## Why it matters

- **Molecular dynamics.** A simulation of a protein computes the force on every atom from a [[Force Field]], divides by the mass and steps positions and velocities forward in time ([[Molecular Dynamics Simulation]]). The integrator it uses descends from the one Verlet introduced in 1967 for simulated fluids.[^verlet]
- **Single-molecule force measurements.** An optical trap measures the force of a motor or the strength of a bond by balancing it against a calibrated restoring force ([[Optical Tweezers]]); the analysis is a free-body diagram.[^svoboda]

## Core (L1)

**Free-body diagrams.** The method for any force problem:[^up6]

1. Isolate **one** object.
2. Draw every external force acting **on** it (weight, normal force, tension, friction, spring force, applied forces), not the forces it exerts on others.
3. Choose axes, often along the motion.
4. Write $\sum F_x = m a_x$ and $\sum F_y = m a_y$ and solve.

![[free-body-diagram-incline-optical-trap.svg]]

**Common forces.**[^up5][^up6]

| Force | Magnitude and direction |
|---|---|
| weight | $w = mg$, downward; near Earth's surface $g \approx 9.8$ m s⁻² (standard value 9.806 65 m s⁻², exact by convention)[^nist] |
| normal force | perpendicular to a contact surface, as large as needed to prevent penetration |
| spring force | $-kx$, toward the rest length ([[Hooke's Law]]) |

**Example: incline.** For the block of panel (a), the axes along and perpendicular to the slope give $N - mg\cos\theta = 0$ and $mg\sin\theta = ma$: the block slides with $a = g\sin\theta$, whatever its mass.

**Equilibrium.** If $\vec a = 0$ (at rest, or moving at constant velocity), the forces sum to zero. This is the case of panel (b): a bead held still by an optical trap while a kinesin motor pulls on it.

## Deeper (L2)

**Newton's law is a differential equation.** With $v = dx/dt$ ([[Kinematics]]), the second law becomes the first-order system

$$\frac{dx}{dt} = v, \qquad \frac{dv}{dt} = \frac{F(x, v, t)}{m},$$

which a computer integrates in small time steps $\Delta t$ ([[Ordinary Differential Equation]]).

**Euler's method** ([[Euler Method]]) uses the values at the start of the step: $x_{n+1} = x_n + v_n\Delta t$, $v_{n+1} = v_n + a_n \Delta t$. Its global error is $O(\Delta t)$, and for an oscillator it adds energy at every step.

**Velocity Verlet.** Taylor-expand $x(t + \Delta t) = x + v\Delta t + \frac{1}{2}a\Delta t^2 + O(\Delta t^3)$ and average the old and new accelerations for the velocity:

$$x_{n+1} = x_n + v_n \Delta t + \tfrac{1}{2} a_n \Delta t^2, \qquad a_{n+1} = \frac{F(x_{n+1})}{m}, \qquad v_{n+1} = v_n + \tfrac{1}{2}(a_n + a_{n+1})\Delta t.$$

It costs one force evaluation per step, like Euler, but its global error is $O(\Delta t^2)$, it is time-reversible, and its energy error oscillates instead of drifting (Computational representation). Eliminating $v$ gives the original position form, $x_{n+1} = 2x_n - x_{n-1} + a_n \Delta t^2$.

## Advanced (L3)

- **Molecular dynamics.** For $N$ atoms, $m_i \ddot{\vec r}_i = \vec F_i = -\nabla_i U(\vec r_1, \dots, \vec r_N)$: $3N$ coupled equations, with forces from the gradient of a [[Potential Energy]] function. Verlet's 1967 simulation of particles interacting through a [[Lennard-Jones Potential]] used this step-by-step integration.[^verlet]
- **The time step is set by the fastest motion.** For a harmonic oscillator of angular frequency $\omega$, the Verlet recurrence $x_{n+1} = (2 - \omega^2\Delta t^2)x_n - x_{n-1}$ has solutions $\lambda^n$ with $\lambda^2 - (2 - \omega^2\Delta t^2)\lambda + 1 = 0$; both roots stay on the unit circle only if $\omega\Delta t \le 2$ (Exercise 4). The stiffest vibration in a molecule (bond stretching, [[Harmonic Oscillator]]) therefore caps the step, and accuracy demands many steps per period.
- **Third law, momentum and checks.** Internal forces come in opposite pairs, so they cancel in the total force and the total momentum of an isolated simulation is constant ([[Momentum]]). Monitoring total momentum and energy is the standard sanity check of an integrator (Exercise 5).
- **Overdamped limit.** When drag $-\gamma v$ dominates, $m\dot v = F - \gamma v$ relaxes almost instantly to $v = F/\gamma$: velocity, not acceleration, is proportional to force. Adding a random thermal force gives the [[Langevin Equation]] used in Brownian dynamics.[^pboc]

## Mathematical representation

For a particle of mass $m$ at position $\vec r(t) \in \mathbb{R}^3$:

$$m \frac{d^2 \vec r}{dt^2} = \sum_k \vec F_k(\vec r, \dot{\vec r}, t),$$

a second-order ODE whose solution is fixed by the initial position and velocity. For an isolated system of particles with pair forces $\vec F_{ij} = -\vec F_{ji}$, summing the equations gives $\frac{d}{dt}\sum_i m_i \dot{\vec r}_i = \sum_i\sum_{j \ne i} \vec F_{ij} = 0$. An integrator is a map $(x_n, v_n) \mapsto (x_{n+1}, v_{n+1})$; its **order** $p$ means a global error $O(\Delta t^p)$ over a fixed time: $p = 1$ for Euler, $p = 2$ for velocity Verlet.

## Computational representation

A mass on a spring in reduced units ($m = k = 1$, so $\omega = 1$ and the period is $2\pi$), released from $x = 1$ at rest, integrated for $t = 100$ (about 16 periods) with $\Delta t = 0.1$:

```python
import math

def force(x, k=1.0):
    """Spring force F = -k x (reduced units: m = k = 1, so omega = 1)."""
    return -k * x

def energy(x, v, m=1.0, k=1.0):
    return 0.5 * m * v * v + 0.5 * k * x * x

def euler(x, v, dt, steps, m=1.0):
    for _ in range(steps):
        x, v = x + v * dt, v + force(x) / m * dt      # both updates use old values
    return x, v

def velocity_verlet(x, v, dt, steps, m=1.0):
    a = force(x) / m
    for _ in range(steps):
        x = x + v * dt + 0.5 * a * dt * dt           # position with current a
        a_new = force(x) / m                          # one force call per step
        v = v + 0.5 * (a + a_new) * dt               # velocity with mean of old and new a
        a = a_new
    return x, v

x0, v0, dt, steps = 1.0, 0.0, 0.1, 1000              # t = 100, about 16 periods
E0 = energy(x0, v0)
for name, method in (("Euler", euler), ("Verlet", velocity_verlet)):
    x, v = method(x0, v0, dt, steps)
    print(f"{name:6s} x(100) = {x:9.4f}  exact {math.cos(100):.4f}  E/E0 = {energy(x, v) / E0:.6f}")

for dt in (0.1, 0.05, 0.025):                        # error at t = 10 versus step size
    n, exact = round(10 / dt), math.cos(10)
    print(dt, f"{abs(euler(1.0, 0.0, dt, n)[0] - exact):.2e}",
          f"{abs(velocity_verlet(1.0, 0.0, dt, n)[0] - exact):.2e}")
```

```text
Euler  x(100) =   94.2012  exact 0.8623  E/E0 = 20959.155638
Verlet x(100) =    0.8827  exact 0.8623  E/E0 = 0.999448
0.1 5.70e-01 2.28e-03
0.05 2.44e-01 5.67e-04
0.025 1.13e-01 1.42e-04
```

Euler multiplies the energy by exactly $1 + \omega^2\Delta t^2 = 1.01$ per step, hence $1.01^{1000} \approx 2 \times 10^4$. Halving $\Delta t$ halves Euler's error (order 1) and quarters Verlet's (order 2).

## Worked example

> [!example] Measuring a motor's force with an optical trap
> A silica bead (radius 0.25 µm; density taken as 2000 kg m⁻³, a round illustrative value) carries one kinesin. The trap acts as a spring of stiffness $\kappa = 0.05$ pN/nm (illustrative). The motor walks, pulls the bead off the trap center, and stops when the bead is 100 nm away.
> 1. **Object and forces.** On the bead: motor force $F_m$ (forward, through the tether), trap force $-\kappa x$ (back toward the center), weight and buoyancy (vertical), and drag while it moves.
> 2. **Is gravity relevant?** $m = \rho \cdot \frac{4}{3}\pi r^3 = 2000 \times 6.5 \times 10^{-20} = 1.3 \times 10^{-16}$ kg, so $mg = 1.3 \times 10^{-15}$ N = 0.0013 pN, a thousand times below the forces of interest. Ignore it.
> 3. **Stall is equilibrium.** At stall the bead does not move: $a = 0$, no drag, so $F_m - \kappa x = 0$ and $F_m = 0.05 \times 100 = 5$ pN, in the 5-6 pN range measured for single kinesins.[^svoboda]
> 4. **Third law.** The bead pulls back on the motor with 5 pN through the tether; that is the load the motor works against ([[Work (Physics)]]).

## Common misconceptions

> [!warning] "Motion needs a force"
> A net force changes velocity; constant velocity needs no net force (first law). In water a protein stops as soon as the push stops, not because motion needs force, but because drag is a real force that cancels the velocity almost instantly.

> [!warning] "Action and reaction cancel"
> The two forces of a third-law pair act on different bodies, so they never cancel in the free-body diagram of one body. Forces that cancel on one body (weight and normal force on a cup) are not a third-law pair.

> [!warning] "A small enough time step makes any integrator fine"
> Euler's energy error grows step after step; a smaller step only delays the drift, at the cost of more steps. Symplectic, time-reversible schemes such as velocity Verlet keep energy bounded over long simulations.

## Exercises

> [!question] Exercise 1 (L1)
> A 2.0 kg box is pulled across a floor by a horizontal 10 N force against 4.0 N of friction. Draw its free-body diagram and find its acceleration and the normal force.

> [!success]- Solution
> Forces: 10 N forward, 4 N friction backward, weight $2.0 \times 9.8 = 19.6$ N down, normal force up. Vertical: $N = 19.6$ N. Horizontal: $10 - 4 = 2.0\,a$, so $a = 3.0$ m s⁻².

> [!question] Exercise 2 (L1)
> A 1.0 kg block slides down a frictionless 30° incline. Find its acceleration and the normal force ($g = 9.80665$ m s⁻²).

> [!success]- Solution
> $a = g\sin 30° = 4.90$ m s⁻²; $N = mg\cos 30° = 8.49$ N. The mass cancels in $a$, not in $N$.

> [!question] Exercise 3 (L2)
> With the trap of the Worked example ($\kappa = 0.05$ pN/nm), a motor stalls at 5.5 pN. How far from the trap center is the bead? If the trap were twice as stiff, how would the stall position and force change?

> [!success]- Solution
> $x = F/\kappa = 5.5 / 0.05 = 110$ nm. A trap twice as stiff gives 55 nm for the same force: the stall force is a property of the motor, the displacement depends on the trap.

> [!question] Exercise 4 (L2)
> Show that velocity Verlet applied to $\ddot x = -\omega^2 x$ is stable only if $\omega \Delta t \le 2$, and check numerically with $\Delta t = 1.9$ and $2.1$ (200 steps, $\omega = 1$).

> [!success]- Solution
> The position form gives $x_{n+1} = (2 - \omega^2\Delta t^2)x_n - x_{n-1}$. Trying $x_n = \lambda^n$: $\lambda^2 - b\lambda + 1 = 0$ with $b = 2 - \omega^2\Delta t^2$. The roots' product is 1; if $|b| \le 2$ they are complex conjugates on the unit circle (bounded oscillation), if $|b| > 2$ one root has $|\lambda| > 1$ and grows. $|2 - \omega^2\Delta t^2| \le 2 \iff \omega\Delta t \le 2$. With `velocity_verlet(1.0, 0.0, dt, 200)`: $|x|$ is 0.209 for $\Delta t = 1.9$ and $2.55 \times 10^{54}$ for $\Delta t = 2.1$.

> [!question] Exercise 5 (L3, Python)
> Two atoms of masses 1 and 2 (reduced units) on a line are joined by a spring ($k = 1$, rest length 1), starting at positions 0 and 1.3 with velocities 0.1 and 0. Integrate 10,000 velocity-Verlet steps of 0.05 and compare total momentum and energy at start and end. Why is one conserved to all printed digits and the other only approximately?

> [!success]- Solution
> ```python
> m1, m2, k, r0 = 1.0, 2.0, 1.0, 1.0
>
> def forces(x1, x2):
>     f = -k * ((x2 - x1) - r0)        # force on atom 2; atom 1 gets the opposite (third law)
>     return -f, f
>
> def totals(x1, x2, v1, v2):
>     p = m1 * v1 + m2 * v2
>     E = 0.5 * m1 * v1**2 + 0.5 * m2 * v2**2 + 0.5 * k * ((x2 - x1) - r0) ** 2
>     return p, E
>
> x1, x2, v1, v2, dt = 0.0, 1.3, 0.1, 0.0, 0.05
> f1, f2 = forces(x1, x2)
> print("start p = %.12f, E = %.6f" % totals(x1, x2, v1, v2))
> for _ in range(10_000):
>     x1 += v1 * dt + 0.5 * f1 / m1 * dt**2
>     x2 += v2 * dt + 0.5 * f2 / m2 * dt**2
>     g1, g2 = forces(x1, x2)
>     v1 += 0.5 * (f1 + g1) / m1 * dt
>     v2 += 0.5 * (f2 + g2) / m2 * dt
>     f1, f2 = g1, g2
> print("end   p = %.12f, E = %.6f" % totals(x1, x2, v1, v2))
> # start p = 0.100000000000, E = 0.050000
> # end   p = 0.100000000000, E = 0.050002
> ```
>
> Each step changes the momenta by $\frac{1}{2}(f_1 + g_1)\Delta t$ and $\frac{1}{2}(f_2 + g_2)\Delta t$, which are exactly opposite because the code applies the third law: total momentum is conserved up to rounding. Energy is conserved only up to the integrator's $O(\Delta t^2)$ error, which oscillates without drifting.

## Mastery checklist

- [ ] 1 Recognized: I can state the three laws and the unit of force.
- [ ] 2 Understood: I can draw a correct free-body diagram, tell third-law pairs from balancing forces, and say when inertia is negligible.
- [ ] 3 Practiced: I solve $F = ma$ problems with components and implement Euler and velocity Verlet, measuring their order.
- [ ] 4 Applied: I simulated a small molecular system with velocity Verlet and checked momentum and energy conservation.
- [ ] 5 Explained: I can explain why molecular dynamics uses Verlet-type integrators, what limits the time step, and how the overdamped limit leads to Brownian dynamics.

## References

[^up5]: [[University Physics (OpenStax)]], Volume 1, ch. 5 "Newton's Laws of Motion".
[^up6]: [[University Physics (OpenStax)]], Volume 1, ch. 6 "Applications of Newton's Laws".
[^801]: [[MIT 8.01SC - Classical Mechanics]]: force-based approach to motion.
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]]: standard acceleration of gravity $g_n = 9.806\,65$ m s⁻² (exact, adopted value).
[^svoboda]: [[Svoboda 1994 - Force and Velocity Measured for Single Kinesin Molecules]], *Cell* 77:773-784 (optical trapping interferometry with calibrated pN forces; loads up to 5-6 pN).
[^verlet]: [[Verlet 1967 - Computer Experiments on Classical Fluids]], *Physical Review* 159:98-103.
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012): dominance of viscous drag over inertia for macromolecules and cells in water.
