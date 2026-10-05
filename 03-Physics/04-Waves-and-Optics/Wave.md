---
aliases:
  - Waves
  - Traveling Wave
  - Sinusoidal Wave
  - Superposition Principle
  - Onde
tags:
  - type/concept
  - domain/physics
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Harmonic Oscillator]]"
  - "[[Function]]"
  - "[[Derivative]]"
related:
  - "[[Electromagnetic Wave]]"
  - "[[Interference]]"
  - "[[Diffraction]]"
  - "[[Refraction]]"
  - "[[Complex Number]]"
  - "[[Fast Fourier Transform]]"
  - "[[Partial Derivative]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Wave

> [!abstract]
> A wave is a pattern that travels: each point of the medium (or of the field) only oscillates in place, but the shape moves on and carries energy, and two waves at the same place simply add.

## Definition

A **wave** is a disturbance that propagates from place to place, carrying energy without carrying the medium along. Mechanical waves (on a string, sound) need a medium; electromagnetic waves do not ([[Electromagnetic Wave]]). In a **transverse** wave the disturbance is perpendicular to the direction of travel; in a **longitudinal** wave it is parallel to it.[^up16]

## Why it matters

- **Light is a wave.** Microscopy, spectroscopy and crystallography read biological samples with light or X-rays, and their limits (which molecules absorb, what can be resolved) are stated in wave quantities: wavelength, frequency, phase ([[Electromagnetic Spectrum]], [[Diffraction Limit]]).
- **Detectors lose the phase.** Cameras record intensity, the square of an amplitude. Recovering phase is what phase-contrast microscopy does optically ([[Interference]]) and what crystallographers must solve ([[Diffraction]]).
- **Superposition is linearity.** Adding waves is adding functions; splitting a signal into sines is the idea behind the [[Fast Fourier Transform]], applied to images, periodic signals and diffraction data.

## Core (L1)

### Describing a sinusoidal wave

A harmonic wave travelling toward $+x$ has the **wave function**[^up16]

$$y(x, t) = A \sin(kx - \omega t + \phi).$$

| Quantity | Symbol (SI unit) | Meaning |
|---|---|---|
| Amplitude | $A$ (unit of the disturbance: m on a string, V/m for an electric field) | maximum displacement from equilibrium |
| Wavelength, wave number | $\lambda$ (m); $k = 2\pi/\lambda$ (rad m⁻¹) | distance between neighbouring crests |
| Period | $T$ (s) | duration of one oscillation at a fixed point |
| Frequency, angular frequency | $f = 1/T$ (Hz = s⁻¹); $\omega = 2\pi f$ (rad s⁻¹) | oscillations per second |
| Phase constant | $\phi$ (rad) | state of the wave at $x = 0$, $t = 0$ |
| Wave speed | $v = \lambda f = \omega/k$ (m s⁻¹) | speed of the pattern |

The whole argument $kx - \omega t + \phi$ is the **phase** (spectroscopy writes the frequency $\nu$ instead of $f$). **Why $v = \omega/k$.** Follow a crest: its phase is constant, $kx - \omega t = \text{const}$. Differentiating with respect to $t$ gives $k\,\frac{dx}{dt} = \omega$, so the crest moves at $\frac{dx}{dt} = \frac{\omega}{k} = \frac{2\pi f}{2\pi/\lambda} = \lambda f$: in one period, the wave advances one wavelength. With $kx + \omega t$, it moves toward $-x$.

### Superposition

Where two waves overlap, the resulting disturbance is the algebraic sum of the individual ones, $y = y_1 + y_2$ (**superposition principle**); each wave continues unchanged afterwards.[^up165] For two waves of equal amplitude, wavelength and frequency that differ only by a phase shift $\phi$, the identity $\sin a + \sin b = 2\cos\frac{a-b}{2}\sin\frac{a+b}{2}$ gives[^up165]

$$y_1 + y_2 = \underbrace{2A\cos\tfrac{\phi}{2}}_{\text{resultant amplitude}}\;\sin\!\left(kx - \omega t + \tfrac{\phi}{2}\right).$$

The sum is again a wave with the same $k$ and $\omega$. Its amplitude goes from $2A$ (**constructive**, $\phi = 0, 2\pi, \dots$) to $0$ (**destructive**, $\phi = \pi, 3\pi, \dots$). This is the root of [[Interference]] and [[Diffraction]].

![[wave-superposition-sines.svg]]

## Deeper (L2)

### The wave equation

A wave that keeps its shape while moving at speed $v$ depends on $x$ and $t$ only through $u = x - vt$: $y = g(x - vt)$. The chain rule gives $\partial^2 y/\partial x^2 = g''(u)$ and $\partial^2 y/\partial t^2 = v^2 g''(u)$, hence the **linear wave equation**, shared by strings, sound and light:[^up16]

$$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\,\frac{\partial^2 y}{\partial t^2}.$$

It is linear: if $y_1$ and $y_2$ solve it, so does $y_1 + y_2$. Superposition is a property of the equation, valid as long as the medium responds linearly ([[Partial Derivative]]).

### Energy goes as amplitude squared

The time-averaged power carried by a wave on a string is $P = \tfrac12 \mu A^2 \omega^2 v$, with $\mu$ the mass per unit length: proportional to $A^2$.[^up16] For light, intensity is likewise proportional to the squared field amplitude ([[Electromagnetic Wave]]). Two equal waves in phase therefore give twice the amplitude and **four times** the intensity of one; in antiphase, zero. Energy is not lost: it is redistributed in space, into bright and dark fringes ([[Interference]]).

### Phasors: unequal amplitudes

Write $A\sin(\theta + \phi) = \operatorname{Im}[A e^{i\phi} e^{i\theta}]$ ([[Complex Number]]). Waves of one frequency share the factor $e^{i\theta}$, so their sum is set by the sum of the **phasors** $A_j e^{i\phi_j}$. For two waves,

$$A_R^2 = \left|A_1 e^{i\phi_1} + A_2 e^{i\phi_2}\right|^2 = A_1^2 + A_2^2 + 2A_1A_2\cos(\phi_2 - \phi_1).$$

The last term, the **interference term**, makes the intensity $I \propto A_R^2$ differ from $I_1 + I_2$. With $A_1 = A_2 = A$ it gives back $A_R = 2A|\cos(\Delta\phi/2)|$. If the phase difference fluctuates randomly, $\cos$ averages to zero and intensities simply add: the waves are **incoherent**.

## Advanced (L3)

**Every wave is a superposition of sines.** A periodic signal of period $L$ is a sum of sines and cosines of wavelengths $L, L/2, L/3, \dots$ (a Fourier series). A square wave of amplitude 1 and period $2\pi$ is

$$s(x) = \frac{4}{\pi}\sum_{n=0}^{\infty}\frac{\sin\big((2n+1)x\big)}{2n+1}.$$

Superposition run backwards is analysis: a sampled signal is split into frequency components by the [[Fast Fourier Transform]], and a far-field diffraction pattern is such a decomposition of the object that scattered the light ([[Diffraction#Advanced (L3)]]). Near a jump, partial sums overshoot by about 9 % of the jump, however many terms are kept (Exercise 5): sharp edges need many components, the reason why an optical system that passes only low spatial frequencies blurs edges ([[Diffraction Limit]]).

**Dispersion.** When the speed depends on wavelength, the medium is **dispersive**: in glass the refractive index depends on wavelength, so a prism separates colours ([[Refraction]]).[^up1] A pulse made of several wavelengths then spreads, and its envelope moves at the group velocity $v_g = d\omega/dk$, not at the phase velocity $\omega/k$.

## Mathematical representation

- Wave function $y(x, t) = A\sin(kx - \omega t + \phi)$, with amplitude $A \ge 0$, $k = 2\pi/\lambda$, $\omega = 2\pi f$, $f = 1/T$, $v = \lambda f = \omega/k$.
- Superposition: $y = \sum_j y_j$. For one frequency, the complex amplitude $\tilde A = \sum_j A_j e^{i\phi_j}$ gives $y = \operatorname{Im}[\tilde A\, e^{i(kx - \omega t)}]$, resultant amplitude $|\tilde A|$ and phase $\arg \tilde A$.
- Wave equation $\partial_x^2 y = v^{-2}\,\partial_t^2 y$; general 1D solution $g(x - vt) + h(x + vt)$. Intensity $I \propto \langle y^2\rangle_t = A^2/2$ (average over a period).

## Computational representation

A wave is sampled on a grid of positions or times and stored as an array of floats; a superposition is an element-wise sum. Phasor arithmetic with complex numbers gives amplitude and phase without sampling.

```python
import cmath
import math


def wave(x: float, t: float, amp: float, k: float, omega: float, phase: float = 0.0) -> float:
    """y(x, t) = A sin(kx - wt + phase): a sinusoidal wave moving toward +x."""
    return amp * math.sin(k * x - omega * t + phase)


def resultant(waves: list[tuple[float, float]]) -> tuple[float, float]:
    """Amplitude and phase of a sum of same-frequency sines, given as (A_j, phi_j): add phasors."""
    z = sum(a * cmath.exp(1j * p) for a, p in waves)
    return abs(z), cmath.phase(z)


lam, f = 1.0, 2.0                                    # toy wave: wavelength 1 m, frequency 2 Hz
k, omega = 2 * math.pi / lam, 2 * math.pi * f
print("speed omega/k =", round(omega / k, 6), "m/s; lambda * f =", lam * f, "m/s")

xs = [i / 1000 for i in range(1001)]                 # one wavelength, sampled at t = 0
for phi in (0.0, 2 * math.pi / 3, math.pi):
    sampled = max(abs(wave(x, 0, 1, k, omega) + wave(x, 0, 1, k, omega, phi)) for x in xs)
    print(f"phi = {phi:.3f} rad: max|y1 + y2| = {sampled:.3f}, 2A|cos(phi/2)| = {abs(2 * math.cos(phi / 2)):.3f}")

amp, ph = resultant([(1.0, 0.0), (0.6, math.pi / 2)])
print(f"A1 = 1, A2 = 0.6, phase difference pi/2: amplitude {amp:.3f}, phase {math.degrees(ph):.1f} deg")
```

```text
speed omega/k = 2.0 m/s; lambda * f = 2.0 m/s
phi = 0.000 rad: max|y1 + y2| = 2.000, 2A|cos(phi/2)| = 2.000
phi = 2.094 rad: max|y1 + y2| = 1.000, 2A|cos(phi/2)| = 1.000
phi = 3.142 rad: max|y1 + y2| = 0.000, 2A|cos(phi/2)| = 0.000
A1 = 1, A2 = 0.6, phase difference pi/2: amplitude 1.166, phase 31.0 deg
```

The sampled maxima match $2A|\cos(\phi/2)|$, and the unequal pair gives $\sqrt{1 + 0.36} = 1.166$, as the phasor formula predicts.

## Worked example

> [!example] Reading a wave function (toy values)
> A wave on a string is $y(x, t) = 0.020 \sin(3.0\,x - 12\,t)$, all in SI units.
> 1. Amplitude $A = 0.020$ m; $k = 3.0$ rad/m, so $\lambda = 2\pi/k = 2.09$ m.
> 2. $\omega = 12$ rad/s, so $f = \omega/2\pi = 1.91$ Hz and $T = 1/f = 0.524$ s.
> 3. Speed $v = \omega/k = 4.0$ m/s, toward $+x$ (the signs of $kx$ and $\omega t$ differ). Check: $\lambda f = 2.09 \times 1.91 = 4.0$ m/s.
> 4. Add an identical wave shifted by $\phi = 2\pi/3$: the amplitude is $2A\cos(\pi/3) = A = 0.020$ m. The pair is no taller than one wave, and carries the intensity of one, not two.
> 5. The same relations hold for light: with $c = 299\,792\,458$ m/s,[^nist] a 500 nm wave in vacuum has $f = c/\lambda = 6.00 \times 10^{14}$ Hz and $T = 1.67$ fs ([[Electromagnetic Wave]]).

## Common misconceptions

> [!warning] "The medium travels with the wave"
> Each piece of string, or the field at each point, only oscillates about equilibrium; the pattern and the energy travel.[^up16] A crest moving at 4 m/s does not mean the string moves at 4 m/s.

> [!warning] "Two waves add their intensities"
> Amplitudes add, with their phases; intensity follows the square. Two equal waves give between 0 and 4 times the intensity of one. Intensities add only for incoherent waves, whose phase difference varies randomly.

> [!warning] "The frequency changes when a wave enters a new medium"
> The source sets the frequency. When the speed changes, the wavelength changes, $\lambda = v/f$ ([[Refraction]]).

## Exercises

> [!question] Exercise 1 (L1)
> A wave is $y = 0.5\sin(0.2\pi x - 4\pi t)$, with $y$ and $x$ in cm and $t$ in s. Give $A$, $\lambda$, $f$, $v$ and the direction of travel.

> [!success]- Solution
> $A = 0.5$ cm. $k = 0.2\pi$ rad/cm, so $\lambda = 2\pi/k = 10$ cm. $\omega = 4\pi$ rad/s, so $f = 2$ Hz. $v = \lambda f = 20$ cm/s, toward $+x$ because $kx$ and $\omega t$ have opposite signs.

> [!question] Exercise 2 (L1)
> Two waves of equal amplitude $A$ and frequency overlap. Which phase difference gives a resultant amplitude of $\sqrt2 A$? Of $A$? What is the intensity relative to one wave in each case?

> [!success]- Solution
> $2A|\cos(\phi/2)| = \sqrt2 A$ gives $\cos(\phi/2) = \sqrt2/2$, so $\phi = \pi/2$: intensity $(\sqrt2)^2 = 2$ times one wave, exactly the sum of the two. Amplitude $A$: $\cos(\phi/2) = 1/2$, $\phi = 2\pi/3$, intensity equal to one wave alone.

> [!question] Exercise 3 (L2)
> Two waves of the same frequency have amplitudes 3 and 4 (any unit). Find the resultant amplitude and intensity ($A_R^2$) for phase differences $0$, $\pi/2$ and $\pi$, and compare with $I_1 + I_2$.

> [!success]- Solution
> $A_R^2 = 9 + 16 + 24\cos\Delta\phi$: $\Delta\phi = 0$ gives $A_R = 7$, $I = 49$; $\pi/2$ gives $5$, $25$; $\pi$ gives $1$, $1$. $I_1 + I_2 = 25$ is reached only at $\pi/2$, where the interference term vanishes. Even unequal waves cannot cancel completely: the minimum is $|A_1 - A_2| = 1$.

> [!question] Exercise 4 (L2, Python)
> Show that $y = A\sin(kx - \omega t)$ solves the wave equation with $v = \omega/k$. Check it numerically with central finite differences for $A = 1$, $k = 2$, $\omega = 6$ at $x = 0.4$, $t = 0.1$.

> [!success]- Solution
> $\partial_x^2 y = -k^2 y$ and $\partial_t^2 y = -\omega^2 y$, so $\partial_x^2 y = (k^2/\omega^2)\,\partial_t^2 y = v^{-2}\,\partial_t^2 y$. Central differences with $h = 10^{-3}$ and the `wave` function above give $-0.79468$ for $\partial_x^2 y$ and $-0.79467$ for $v^{-2}\partial_t^2 y$: both equal $-k^2\sin(0.2) = -0.7947$ to the accuracy of the finite differences ($O(h^2)$).

> [!question] Exercise 5 (L3, Python)
> Compute the partial Fourier sums of the square wave with 1, 5 and 50 terms, at $x = \pi/2$ and at their maximum on $(0, \pi)$. What happens to the overshoot?

> [!success]- Solution
> ```python
> import math
>
> def square_partial(x: float, n_terms: int) -> float:
>     """Partial Fourier sum (4/pi) * sum_{n < n_terms} sin((2n+1)x) / (2n+1) of a unit square wave."""
>     return 4 / math.pi * sum(math.sin((2 * n + 1) * x) / (2 * n + 1) for n in range(n_terms))
>
> grid = [i * math.pi / 20000 for i in range(1, 20000)]
> for n_terms in (1, 5, 50):
>     print(n_terms, round(square_partial(math.pi / 2, n_terms), 4), round(max(square_partial(x, n_terms) for x in grid), 4))
> # 1 1.2732 1.2732
> # 5 1.0631 1.1823
> # 50 0.9936 1.179
> ```
>
> At $x = \pi/2$ the sums converge to 1. The maximum does not: it stays near 1.179, an overshoot of 0.179 on a jump of 2, about 9 %, that only moves closer to the edge as terms are added (the Gibbs phenomenon). Truncating high frequencies, as any finite aperture does, leaves ringing at sharp edges.

## Mastery checklist

- [ ] 1 Recognized: I can name amplitude, wavelength, frequency, period, speed and phase, and state $v = \lambda f$.
- [ ] 2 Understood: I can explain why $kx - \omega t$ describes a moving pattern, and why two equal waves give between 0 and 4 times the intensity of one.
- [ ] 3 Practiced: I can read a wave function, add waves with phasors by hand and in Python, and check the wave equation numerically.
- [ ] 4 Applied: I can convert between the wave quantities used in instrument specifications (nm, Hz, rad/s) and use them in the optics notes ([[Interference]], [[Diffraction]]).
- [ ] 5 Explained: I can teach superposition as linearity, the meaning of phase and coherence, and how Fourier decomposition connects waves to signal and image analysis.

## References

[^up16]: [[University Physics (OpenStax)]], Volume 1, ch. 16 "Waves" (transverse and longitudinal waves; amplitude, wavelength, period, frequency and speed; the wave function and wave number; the linear wave equation; energy and power of a wave on a string).
[^up165]: [[University Physics (OpenStax)]], Volume 1, §16.5 "Interference of Waves" (superposition; resultant of two identical sinusoidal waves that differ only by a phase shift).
[^up1]: [[University Physics (OpenStax)]], Volume 3, Unit 1 "Optics", ch. 1 "The Nature of Light" (dispersion: the refractive index depends on wavelength).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA 2022 values: speed of light in vacuum $c = 299\,792\,458$ m s⁻¹ (exact).
