---
aliases:
  - Simple Harmonic Motion
  - SHM
  - Damped Harmonic Oscillator
  - Oscillateur harmonique
tags:
  - type/concept
  - domain/physics
  - domain/chemistry
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Hooke's Law]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Conservation of Energy]]"
  - "[[Derivative]]"
related:
  - "[[Potential Energy]]"
  - "[[Second-Order Linear Differential Equation]]"
  - "[[Complex Number]]"
  - "[[Spectroscopy]]"
  - "[[Eigenvalues and Eigenvectors]]"
  - "[[Hessian Matrix]]"
  - "[[Force Field]]"
  - "[[Reynolds Number]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[MIT 18.03SC - Differential Equations]]"
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[NIST Atomic Weights and Isotopic Compositions]]"
---

# Harmonic Oscillator

> [!abstract]
> A mass on a spring oscillates at a frequency set only by stiffness and mass, $\omega_0 = \sqrt{k/m}$; add friction and the oscillation decays or disappears. The same equation describes vibrating bonds, seen by infrared spectroscopy, and the small motions of whole proteins.

## Definition

A **harmonic oscillator** is a mass $m$ subject to a linear restoring force $F = -kx$ ([[Hooke's Law]]). Newton's second law gives $m\ddot x = -kx$, whose solutions are **simple harmonic motion**, $x(t) = A\cos(\omega_0 t + \varphi)$ with angular frequency $\omega_0 = \sqrt{k/m}$, period $T = 2\pi\sqrt{m/k}$ and frequency $f = 1/T$, all independent of the amplitude $A$.[^up151] With a friction force $-b\dot x$ the oscillator is **damped**; for weak damping it oscillates at $\omega = \sqrt{\omega_0^2 - (b/2m)^2}$ with a decaying amplitude.[^up155]

## Why it matters

- **Infrared spectra.** A chemical bond vibrates like two masses joined by a spring; its frequency $\propto \sqrt{k/\mu}$ falls in the infrared, and characteristic absorption bands identify functional groups: about 1715 cm⁻¹ for the C=O of a saturated ketone, 2850 to 2960 cm⁻¹ for alkane C–H.[^orgchem] Inverting the formula turns a band position into a bond stiffness ([[Spectroscopy]]).
- **Normal modes.** Around an energy minimum every molecule is a set of coupled springs; diagonalizing the stiffness matrix splits its small motions into independent oscillators, the normal modes, whose lowest frequencies are the softest directions of the [[Force Field]] (L3).
- **Oscillate or creep.** Whether a system rings or relaxes depends on damping versus stiffness and mass; for molecules and beads in water, that comparison is the subject of [[Reynolds Number]] and [[Stokes' Law]].
- **The archetypal ODE**, model problem of [[Second-Order Linear Differential Equation|second-order linear equations]][^1803] and test case for integrators ([[Conservation of Energy]]).

## Core (L1)

**Solving it.** Substitute $x = A\cos(\omega t + \varphi)$ into $m\ddot x + kx = 0$: $(-m\omega^2 + k)A\cos(\omega t + \varphi) = 0$ for all $t$, so $\omega = \omega_0 = \sqrt{k/m}$. The two constants come from the initial conditions: $x(0) = A\cos\varphi$, $v(0) = -A\omega_0\sin\varphi$.

**Frequency from stiffness and mass.** A stiffer spring oscillates faster, a heavier mass slower, and the period does not depend on the amplitude: small and large swings take the same time, as long as the force stays linear.[^up151]

**Energy.** $E = \tfrac12 m v^2 + \tfrac12 k x^2 = \tfrac12 k A^2$: all potential at $x = \pm A$, all kinetic at $x = 0$, where $v_{max} = \omega_0 A$ ([[Conservation of Energy]]).

**Two atoms on a spring.** For masses $m_1$ and $m_2$ joined by a bond of stiffness $k$, subtracting the two equations of motion gives, for the stretch $x = (x_2 - x_1) - r_0$,

$$\ddot x = -k\left(\frac{1}{m_1} + \frac{1}{m_2}\right)x \quad\Rightarrow\quad \mu\ddot x = -kx, \qquad \mu = \frac{m_1 m_2}{m_1 + m_2}.$$

The bond is one oscillator with the **reduced mass** $\mu$. Spectroscopists quote the wavenumber $\tilde\nu = 1/\lambda = f/c$, in cm⁻¹, so

$$\tilde\nu = \frac{1}{2\pi c}\sqrt{\frac{k}{\mu}}, \qquad k = \mu\,(2\pi c\,\tilde\nu)^2.$$

A light partner gives a high frequency: alkane C–H stretches lie at 2850 to 2960 cm⁻¹, C=O near 1700 cm⁻¹ although the C=O bond is stiffer (computed below).

## Deeper (L2)

**Damping.** With $F = -kx - b\dot x$, divide by $m$ and set $\gamma = b/2m$ (s⁻¹):

$$\ddot x + 2\gamma\dot x + \omega_0^2 x = 0.$$

Trying $x = e^{rt}$ gives the characteristic equation $r^2 + 2\gamma r + \omega_0^2 = 0$, so $r = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$ ([[Complex Number]] roots when $\gamma < \omega_0$).[^1803] Three regimes:[^up155]

| Regime | Condition | Solution | Behavior |
|---|---|---|---|
| underdamped | $\gamma < \omega_0$ | $A e^{-\gamma t}\cos(\omega_d t + \varphi)$, $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$ | oscillates inside a decaying envelope |
| critically damped | $\gamma = \omega_0$ | $(C_1 + C_2 t)\,e^{-\gamma t}$ | fastest return without overshoot |
| overdamped | $\gamma > \omega_0$ | $C_1 e^{r_+ t} + C_2 e^{r_- t}$ | no oscillation, slow creep back |

![[damped-oscillator-regimes.svg]]

**Quality factor.** The energy of a weakly damped oscillator decays as $e^{-2\gamma t}$; the quality factor $Q = \omega_0 / 2\gamma$ counts, up to a factor $2\pi$, how many oscillations it makes before losing most of its energy. **Strong damping**: for $\gamma \gg \omega_0$ the slow root is $r_+ \approx -\omega_0^2/2\gamma$, so the system relaxes with time constant $2\gamma/\omega_0^2 = b/k$, friction over stiffness, and the mass no longer matters (Exercise 5).

**Quantized vibrations.** A quantum harmonic oscillator has evenly spaced energy levels $E_n = (n + \tfrac12)hf$, $n = 0, 1, 2, \dots$; absorbing a photon of frequency $f$ lifts a vibration by one level, which is what an infrared band measures.[^up3][^orgchem] At 310 K, $k_B T / hc = 215.5$ cm⁻¹ (with exact $h$, $c$, $k_B$[^nist]): a 1715 cm⁻¹ vibration has $hc\tilde\nu / k_B T = 8.0$, so its excited levels are almost empty and bond stretches are essentially frozen in their ground state ([[Boltzmann Distribution]]); classical equipartition does not apply to them.

## Advanced (L3)

**Normal modes.** Near a minimum of $U(\mathbf r_1, \dots, \mathbf r_N)$, write the $3N$ displacements as a vector $\mathbf x$, the masses as a diagonal matrix $\mathbf M$ and the [[Hessian Matrix]] of $U$ as $\mathbf K$. Newton's law becomes $\mathbf M\ddot{\mathbf x} = -\mathbf K\mathbf x$. Trying $\mathbf x = \mathbf a\cos(\omega t)$:

$$\mathbf K\mathbf a = \omega^2\,\mathbf M\mathbf a \quad\Leftrightarrow\quad \left(\mathbf M^{-1/2}\mathbf K\mathbf M^{-1/2}\right)\mathbf b = \omega^2\,\mathbf b, \qquad \mathbf b = \mathbf M^{1/2}\mathbf a.$$

The mass-weighted Hessian is symmetric, so its eigenvectors are orthogonal and its eigenvalues $\omega_i^2$ real ([[Eigenvalues and Eigenvectors]]). Each eigenvector is a **normal mode**: all atoms move at one frequency with fixed relative amplitudes, and any small motion is a superposition of modes. For a free molecule in 3D, six eigenvalues are zero: rigid translations and rotations cost no energy. Normal mode analysis of a protein applies this to the force-field Hessian at a minimum; the lowest-frequency modes are its softest directions, and the analysis is only valid for small amplitudes around that minimum, without the friction of the solvent. Exercise 4 works the two-mass case.

## Mathematical representation

- Simple: $m\ddot x + kx = 0$, $x(t) = A\cos(\omega_0 t + \varphi)$, $\omega_0 = \sqrt{k/m}$ (rad/s), $f = \omega_0/2\pi$ (Hz), $E = \tfrac12 kA^2$ (J). Diatomic: $\tilde\nu = \sqrt{k/\mu}\,/\,2\pi c$, with $\tilde\nu$ in m⁻¹ in SI (multiply cm⁻¹ by 100).
- Damped: $\ddot x + 2\gamma\dot x + \omega_0^2 x = 0$, $\gamma = b/2m$, roots $r_\pm = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$; $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$; $Q = \omega_0/2\gamma$.
- Underdamped solution with $x(0) = x_0$, $\dot x(0) = 0$: $x(t) = x_0 e^{-\gamma t}\left[\cos\omega_d t + \frac{\gamma}{\omega_d}\sin\omega_d t\right]$.
- Quantum: $E_n = (n + \tfrac12)hf$, adjacent-level population ratio $e^{-hf/k_B T}$. Normal modes: $\mathbf K\mathbf a = \omega^2\mathbf M\mathbf a$.

## Computational representation

The code converts infrared band positions into force constants, then integrates the damped oscillator with a fourth-order [[Runge-Kutta Method]] and checks it against the exact solution.

```python
import math

C = 299_792_458.0             # m/s, exact
H = 6.62607015e-34            # J s, exact
KB = 1.380649e-23             # J/K, exact
U = 1.66053907e-27            # kg, atomic mass constant (CODATA, rounded)
MASS = {"H": 1.00782503223, "D": 2.01410177812, "C": 12.0, "O": 15.99491461957}   # u, NIST


def reduced_mass(a: str, b: str) -> float:
    """Reduced mass of a diatomic oscillator, in kg."""
    ma, mb = MASS[a] * U, MASS[b] * U
    return ma * mb / (ma + mb)


def force_constant(wavenumber_cm: float, mu: float) -> float:
    """k = mu * omega^2 with omega = 2 pi c nu~ (wavenumber in cm^-1, converted to m^-1)."""
    omega = 2 * math.pi * C * wavenumber_cm * 100
    return mu * omega**2


for bond, a, b, nu in (("C=O ketone", "C", "O", 1715), ("C-H alkane", "C", "H", 2850), ("C-H alkane", "C", "H", 2960)):
    k = force_constant(nu, reduced_mass(a, b))
    print(f"{bond:11s} {nu} cm^-1  k = {k:6.0f} N/m   h c nu~ / kBT(310 K) = {H * C * nu * 100 / (KB * 310):.1f}")


def damped_rk4(x0, v0, omega0, gamma, dt, n):
    """Integrate x'' + 2 gamma x' + omega0^2 x = 0 with fourth-order Runge-Kutta; return x at each step."""
    def f(x, v):
        return v, -2 * gamma * v - omega0**2 * x
    x, v, out = x0, v0, [x0]
    for _ in range(n):
        k1 = f(x, v)
        k2 = f(x + dt / 2 * k1[0], v + dt / 2 * k1[1])
        k3 = f(x + dt / 2 * k2[0], v + dt / 2 * k2[1])
        k4 = f(x + dt * k3[0], v + dt * k3[1])
        x += dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        v += dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        out.append(x)
    return out


def underdamped_exact(t, omega0, gamma):
    """Solution with x(0) = 1, v(0) = 0 when gamma < omega0."""
    wd = math.sqrt(omega0**2 - gamma**2)
    return math.exp(-gamma * t) * (math.cos(wd * t) + gamma / wd * math.sin(wd * t))


omega0, gamma, dt, n = 1.0, 0.1, 0.01, 3000          # reduced units, t from 0 to 30
xs = damped_rk4(1.0, 0.0, omega0, gamma, dt, n)
err = max(abs(x - underdamped_exact(i * dt, omega0, gamma)) for i, x in enumerate(xs))
print(f"RK4 vs exact: max error {err:.1e};  Q = omega0 / (2 gamma) = {omega0 / (2 * gamma):.0f}")
for g in (0.1, 1.0, 3.0):
    regime = "underdamped" if g < omega0 else "critically damped" if g == omega0 else "overdamped"
    print(f"gamma = {g}: {regime:17s} x(10) = {damped_rk4(1.0, 0.0, omega0, g, dt, 1000)[-1]:+.4f}")
```

```text
C=O ketone  1715 cm^-1  k =   1188 N/m   h c nu~ / kBT(310 K) = 8.0
C-H alkane  2850 cm^-1  k =    445 N/m   h c nu~ / kBT(310 K) = 13.2
C-H alkane  2960 cm^-1  k =    480 N/m   h c nu~ / kBT(310 K) = 13.7
RK4 vs exact: max error 3.1e-10;  Q = omega0 / (2 gamma) = 5
gamma = 0.1: underdamped       x(10) = -0.3369
gamma = 1.0: critically damped x(10) = +0.0005
gamma = 3.0: overdamped        x(10) = +0.1853
```

The C=O bond is more than twice as stiff as C–H, yet vibrates at a lower wavenumber because its reduced mass is seven times larger. At $t = 10/\omega_0$ the critically damped oscillator is back at equilibrium while the overdamped one is still at 19 % of its start.

## Worked example

> [!example] Bond stiffness from an infrared band
> A saturated ketone absorbs at $\tilde\nu = 1715$ cm⁻¹ (C=O stretch).[^orgchem] Masses: ¹²C = 12 u exactly, ¹⁶O = 15.9949 u;[^nistaw] $1\text{ u} = 1.66054 \times 10^{-27}$ kg.[^nist]
>
> 1. **Reduced mass.** $\mu = \frac{12 \times 15.9949}{27.9949} = 6.856$ u $= 1.1385 \times 10^{-26}$ kg.
> 2. **Angular frequency.** $\tilde\nu = 1715$ cm⁻¹ $= 1.715 \times 10^5$ m⁻¹; $\omega = 2\pi c\tilde\nu = 2\pi \times 2.998 \times 10^8 \times 1.715 \times 10^5 = 3.230 \times 10^{14}$ rad/s.
> 3. **Stiffness.** $k = \mu\omega^2 = 1.1385 \times 10^{-26} \times (3.230 \times 10^{14})^2 = 1188$ N/m. Units: kg s⁻² = N/m.
> 4. **Period.** $T = 1/(c\tilde\nu) = 19.4$ fs: bonds vibrate on the femtosecond scale, so a simulation that resolves bond vibrations needs time steps well below 19 fs ([[Molecular Dynamics Simulation]]).
> 5. **Thermal check.** $hc\tilde\nu/k_B T = 7.96$ at 310 K: the excited level holds a fraction $e^{-7.96} \approx 3.5 \times 10^{-4}$ of the ground-state population. The bond vibrates with its quantum zero-point motion, not with thermal energy.

## Common misconceptions

> [!warning] "More damping always brings the system back faster"
> Return is fastest at critical damping. Beyond it, more friction slows the return: the relaxation time grows as $b/k$.

> [!warning] "The stiffest bond has the highest frequency"
> Frequency depends on $k/\mu$. C–H vibrates near 2900 cm⁻¹ with $k \approx 450$ N/m because hydrogen is light; C=O, with $k \approx 1190$ N/m, vibrates near 1700 cm⁻¹.

> [!warning] "Each bond vibrates with $\frac{1}{2}k_B T$ of potential energy at room temperature"
> Equipartition is classical. Bond stretches have quanta several times $k_B T$ and stay in their ground state; only low-frequency motions (hundreds of cm⁻¹ or less) are thermally excited.

## Exercises

> [!question] Exercise 1 (L1)
> Replacing H by deuterium (D) leaves the bond's stiffness unchanged. Predict the C–D stretch from a C–H stretch at 2900 cm⁻¹, using the masses of the code.

> [!success]- Solution
> $\tilde\nu \propto \mu^{-1/2}$, so $\tilde\nu_{CD} = \tilde\nu_{CH}\sqrt{\mu_{CH}/\mu_{CD}}$. With $\mu_{CH} = 0.930$ u and $\mu_{CD} = 1.725$ u, the ratio $\sqrt{\mu_{CD}/\mu_{CH}} = 1.362$ and $\tilde\nu_{CD} = 2900/1.362 = 2129$ cm⁻¹. The 770 cm⁻¹ shift makes the two bonds easy to tell apart.

> [!question] Exercise 2 (L2)
> A 0.5 kg mass on a 200 N/m spring has damping coefficient $b = 2$ kg/s. Classify the motion, give $\omega_d$ and $Q$, and say after how many oscillations the amplitude has halved.

> [!success]- Solution
> $\omega_0 = 20$ rad/s, $\gamma = b/2m = 2$ s⁻¹ $< \omega_0$: underdamped. $\omega_d = \sqrt{400 - 4} = 19.9$ rad/s, $Q = 20/4 = 5$. The amplitude $e^{-\gamma t}$ halves at $t = \ln 2/\gamma = 0.347$ s, and one period is $2\pi/\omega_d = 0.316$ s: about 1.1 oscillations.

> [!question] Exercise 3 (L2)
> At 310 K, compare the population of the first excited level, relative to the ground level, for the 1715 cm⁻¹ C=O stretch and for a 200 cm⁻¹ low-frequency mode.

> [!success]- Solution
> Ratio $e^{-hc\tilde\nu/k_BT}$ with $k_BT/hc = 215.5$ cm⁻¹: C=O, $e^{-7.96} = 3.5 \times 10^{-4}$; 200 cm⁻¹, $e^{-0.93} = 0.40$. Low-frequency motions are thermally excited; stiff bond stretches are not.

> [!question] Exercise 4 (L3)
> Two equal masses $m$ sit between two walls, linked wall–mass–mass–wall by three equal springs $k$. Find the normal modes.

> [!success]- Solution
> $m\ddot x_1 = -kx_1 - k(x_1 - x_2)$, $m\ddot x_2 = -kx_2 - k(x_2 - x_1)$, so $\mathbf M^{-1}\mathbf K = \frac{k}{m}\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$, with eigenvalues $\frac{k}{m}(2 \mp 1)$. Mode 1: $\omega = \sqrt{k/m}$, eigenvector $(1, 1)$, the masses move together and the middle spring is never stretched. Mode 2: $\omega = \sqrt{3k/m}$, eigenvector $(1, -1)$, they move in opposition. Starting with only $x_1 \neq 0$ excites both modes; since $\sqrt 3$ is irrational, the superposition never exactly repeats.

> [!question] Exercise 5 (L3, Python)
> With `damped_rk4` from the code, release an overdamped oscillator ($\omega_0 = 1$, $\gamma = 10$, reduced units) from $x = 1$ and find when $x$ first falls below $1/e$. Compare with $2\gamma/\omega_0^2$ and with $1/|r_+|$.

> [!success]- Solution
> ```python
> gamma, omega0, dt = 10.0, 1.0, 0.01
> xs = damped_rk4(1.0, 0.0, omega0, gamma, dt, 10000)
> t_e = next(i * dt for i, x in enumerate(xs) if x < math.exp(-1))
> print(t_e, 2 * gamma / omega0**2, round(1 / (gamma - math.sqrt(gamma**2 - omega0**2)), 2))
> # 20.01 20.0 19.95
> ```
>
> The relaxation time is $b/k = 2\gamma/\omega_0^2 = 20$, twenty times the oscillation period scale $1/\omega_0$: a strongly damped spring simply creeps back, at a rate set by friction over stiffness. Whether a trapped bead or a protein domain in water is in this regime is decided by its drag ([[Stokes' Law]], [[Reynolds Number]]).

## Mastery checklist

- [ ] 1 Recognized: I can write $m\ddot x = -kx$, its solution and $\omega_0 = \sqrt{k/m}$.
- [ ] 2 Understood: I can explain the reduced mass, the three damping regimes, $Q$, and why bond vibrations are quantized and frozen at room temperature.
- [ ] 3 Practiced: I can convert an infrared wavenumber into a force constant, solve the damped equation with its characteristic roots, and integrate it numerically against the exact solution.
- [ ] 4 Applied: I can read an infrared spectrum or a normal mode calculation and relate band positions or mode frequencies to stiffness and mass.
- [ ] 5 Explained: I can teach normal modes as an eigenvalue problem, the overdamped limit $b/k$, and the limits of the harmonic picture (anharmonicity, quantization, solvent friction).

## References

[^up151]: [[University Physics (OpenStax)]], Volume 1, §15.1 "Simple Harmonic Motion" ($\omega = \sqrt{k/m}$, $T = 2\pi\sqrt{m/k}$, $x(t) = A\cos(\omega t + \varphi)$).
[^up155]: [[University Physics (OpenStax)]], Volume 1, §15.5 "Damped Oscillations" (underdamped, critically damped and overdamped motion; $\omega = \sqrt{\omega_0^2 - (b/2m)^2}$).
[^up3]: [[University Physics (OpenStax)]], Volume 3, Unit 2 "Modern Physics" (quantum harmonic oscillator, molecular vibrational levels).
[^1803]: [[MIT 18.03SC - Differential Equations]], Unit II "Second Order Constant Coefficient Linear Equations" (characteristic equation, damped oscillators).
[^orgchem]: [[Organic Chemistry (OpenStax)]], ch. 12 "Structure Determination: Mass Spectrometry and Infrared Spectroscopy", §12.7 "Interpreting Infrared Spectra" and §12.8 "Infrared Spectra of Some Common Functional Groups" (saturated ketone C=O at 1715 cm⁻¹; alkane C–H at 2850 to 2960 cm⁻¹).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]]: speed of light, Planck and Boltzmann constants (exact since the 2019 SI) and atomic mass constant (CODATA).
[^nistaw]: [[NIST Atomic Weights and Isotopic Compositions]]: relative atomic masses of ¹H, ²H, ¹²C and ¹⁶O.
