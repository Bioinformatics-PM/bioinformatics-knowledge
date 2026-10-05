---
aliases:
  - EM Wave
  - Electromagnetic Radiation
  - Light Wave
  - Onde électromagnétique
tags:
  - type/concept
  - domain/physics
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Wave]]"
  - "[[Electric Field]]"
  - "[[Magnetic Field]]"
related:
  - "[[Electromagnetic Spectrum]]"
  - "[[Photon]]"
  - "[[Refraction]]"
  - "[[Polarization]]"
  - "[[Electromagnetic Induction]]"
  - "[[Microscopy]]"
  - "[[Spectroscopy]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Electromagnetic Wave

> [!abstract]
> Light, radio waves and X-rays are the same thing: an electric field and a magnetic field oscillating together at right angles, each regenerating the other, travelling through empty space at $c$, with $c = \lambda\nu$ linking wavelength and frequency.

## Definition

An **electromagnetic (EM) wave** is a propagating oscillation of coupled electric and magnetic fields. It needs no medium. In a plane wave in vacuum, the electric field $\vec E$ and the magnetic field $\vec B$ are perpendicular to each other and to the direction of travel (the wave is transverse), oscillate in phase, have amplitudes related by $E_0 = cB_0$, and travel at the speed of light $c$.[^up16em]

## Why it matters

- **Every optical measurement reads EM waves.** Micrographs and absorbance or fluorescence readings all record light ([[Microscopy]], [[Spectroscopy]]). Instruments are specified either by wavelength (a 488 nm laser) or by frequency (a 600 MHz NMR spectrometer); $c = \lambda\nu$ converts one into the other.
- **Detectors see intensity, not fields.** Visible light oscillates about $5 \times 10^{14}$ times per second (computed below), far faster than any camera exposure, so detectors record the average of $E^2$ and lose the phase. Phase-contrast microscopy ([[Interference]]) and crystallographic phasing ([[Diffraction]]) exist to get it back.
- **Light carries energy.** Laser powers and spot sizes in imaging protocols translate into intensities and fields at the sample with the formulas below.[^up16em]

## Core (L1)

### Fields and geometry

For a wave travelling along $+x$, with $\vec E$ along $y$ and $\vec B$ along $z$:[^up16em]

$$E_y(x, t) = E_0\sin(kx - \omega t), \qquad B_z(x, t) = B_0\sin(kx - \omega t), \qquad E_0 = c\,B_0,$$

with $k = 2\pi/\lambda$ and $\omega = 2\pi\nu$ as for any [[Wave]]. The direction of travel is that of $\vec E \times \vec B$. The drawing is a graph of field values along the $x$ axis: nothing moves sideways.

![[electromagnetic-wave-fields.svg]]

### The speed of light and $c = \lambda\nu$

In vacuum all EM waves travel at the same speed, whose value is exact in the SI:[^nist]

$$c = 299\,792\,458 \text{ m s}^{-1},$$

so wavelength $\lambda$ (m) and frequency $\nu$ (Hz) are two descriptions of one wave:

$$c = \lambda\nu.$$

Blue light at 488 nm has $\nu = 6.14 \times 10^{14}$ Hz and a period of 1.63 fs; the 600 MHz radio wave of an NMR spectrometer has $\lambda = 0.50$ m (computed below). The name of the radiation (radio, visible, X-ray) only labels a range of $\lambda$ ([[Electromagnetic Spectrum]]).

**In a material**, light travels at $v = c/n$, where $n \ge 1$ is the refractive index. The frequency, set by the source, is unchanged, so the wavelength shrinks to $\lambda/n$: in water ($n = 1.333$),[^up1] 488 nm light has a wavelength of 366 nm. This is the starting point of [[Refraction]].

**Sources.** Accelerating charges radiate: an alternating current in an antenna emits radio waves at its own frequency.[^up16em] Light from atoms and molecules is emitted when their electrons change energy level, one [[Photon]] at a time ([[Spectroscopy]]). The direction along which $\vec E$ oscillates defines the wave's [[Polarization]].

## Deeper (L2)

### Light as a prediction of Maxwell's equations

Maxwell's equations combine into a wave equation for $\vec E$ and $\vec B$ whose speed is fixed by two constants of electromagnetism, the vacuum permittivity $\varepsilon_0$ and permeability $\mu_0$:[^up16em]

$$c = \frac{1}{\sqrt{\mu_0\,\varepsilon_0}}.$$

That this speed equals the measured speed of light identified light as an electromagnetic wave; Hertz later produced and detected such waves with electric circuits.[^up16em] With the CODATA 2022 values $\varepsilon_0 = 8.854\,187\,8188 \times 10^{-12}$ F m⁻¹ and $\mu_0 = 1.256\,637\,061\,27 \times 10^{-6}$ N A⁻²,[^nist] the code below recovers 299 792 458 m/s. The coupling at work is [[Electromagnetic Induction]]: a changing $\vec B$ creates $\vec E$, and a changing $\vec E$ creates $\vec B$.

### Energy and intensity

The energy density is shared equally by the two fields, and the **intensity** (power per unit area, W m⁻²), averaged over a period, is[^up16em]

$$I = \tfrac12\,c\,\varepsilon_0\,E_0^2 \qquad\Longleftrightarrow\qquad E_0 = \sqrt{\frac{2I}{c\,\varepsilon_0}}.$$

As for every wave, intensity goes as amplitude squared ([[Wave#Deeper (L2)]]). Focusing the same power onto a smaller area raises $I$ as $1/\text{area}$ and $E_0$ as $1/\text{diameter}$ (worked example).

## Mathematical representation

- Plane wave with propagation direction $\hat{\vec k}$: $\vec E(\vec r, t) = \vec E_0 \sin(\vec k\cdot\vec r - \omega t)$, $\vec B = \frac{1}{c}\,\hat{\vec k} \times \vec E$, with $\vec E_0 \cdot \hat{\vec k} = 0$ (transverse), $|\vec k| = 2\pi/\lambda$, $\omega = 2\pi\nu$.
- Dispersion relation in vacuum: $\omega = c\,|\vec k|$, i.e. $c = \lambda\nu$. In a medium of index $n$: $v = c/n$, $\lambda_n = \lambda/n$, $\nu$ unchanged.
- $c = 1/\sqrt{\mu_0\varepsilon_0}$; $E_0 = cB_0$; intensity $I = \frac12 c\varepsilon_0 E_0^2$ (W m⁻²).

## Computational representation

Constants live in one place, with their CODATA year; everything else is a one-line formula. Wavelengths are stored in metres in code and printed in nm.

```python
import math

C = 299_792_458              # speed of light in vacuum, m/s (exact, CODATA 2022)
EPS0 = 8.8541878188e-12      # vacuum electric permittivity, F/m (CODATA 2022)
MU0 = 1.25663706127e-6       # vacuum magnetic permeability, N/A^2 (CODATA 2022)


def frequency(wavelength_m: float) -> float:
    """Frequency (Hz) of an electromagnetic wave of vacuum wavelength lambda: nu = c / lambda."""
    return C / wavelength_m


def e_amplitude(intensity: float) -> float:
    """Peak electric field E0 (V/m) of a plane wave of intensity I (W/m^2): I = c eps0 E0^2 / 2."""
    return math.sqrt(2 * intensity / (C * EPS0))


print(f"1/sqrt(mu0 eps0) = {1 / math.sqrt(MU0 * EPS0):.1f} m/s   (c = {C} m/s)")
for name, lam in (("violet 405 nm", 405e-9), ("blue 488 nm", 488e-9), ("red 640 nm", 640e-9)):
    nu = frequency(lam)
    print(f"{name}: nu = {nu:.3e} Hz, period = {1e15 / nu:.2f} fs")

power = 1e-3                                  # 1 mW beam (example value)
for diameter in (1e-3, 0.5e-6):               # 1 mm beam, then a 0.5 um spot (uniform disk model)
    intensity = power / (math.pi * (diameter / 2) ** 2)
    e0 = e_amplitude(intensity)
    print(f"diameter {diameter:g} m: I = {intensity:.3g} W/m^2, E0 = {e0:.3g} V/m, B0 = {e0 / C:.3g} T")
```

```text
1/sqrt(mu0 eps0) = 299792458.0 m/s   (c = 299792458 m/s)
violet 405 nm: nu = 7.402e+14 Hz, period = 1.35 fs
blue 488 nm: nu = 6.143e+14 Hz, period = 1.63 fs
red 640 nm: nu = 4.684e+14 Hz, period = 2.13 fs
diameter 0.001 m: I = 1.27e+03 W/m^2, E0 = 979 V/m, B0 = 3.27e-06 T
diameter 5e-07 m: I = 5.09e+09 W/m^2, E0 = 1.96e+06 V/m, B0 = 0.00653 T
```

## Worked example

> [!example] From laser power to field strength (example values)
> A 1 mW laser beam of 1 mm diameter is focused by a microscope objective onto a spot 0.5 µm across. Treat both as disks of uniform intensity.
> 1. Beam: $I = P/(\pi r^2) = 10^{-3}/(\pi \times (0.5 \times 10^{-3})^2) = 1.27 \times 10^3$ W m⁻².
> 2. Field: $E_0 = \sqrt{2I/(c\varepsilon_0)} = 979$ V m⁻¹, and $B_0 = E_0/c = 3.3$ µT.
> 3. Spot: the area is $(10^{-3}/0.5 \times 10^{-6})^2 = 4 \times 10^6$ times smaller, so $I = 5.1 \times 10^9$ W m⁻² and $E_0 = 979 \times 2000 = 1.96 \times 10^6$ V m⁻¹.
> 4. Interpretation: the same milliwatt is spread thin over a millimetre and concentrated four million times in a diffraction-limited spot. What molecules at the sample experience is the local intensity, not the laser's rated power ([[Fluorescence Microscopy]], [[Photon]]).

## Common misconceptions

> [!warning] "Light needs a medium to travel in"
> Mechanical waves do; EM waves do not. The oscillating fields sustain each other and cross vacuum at $c$.[^up16em]

> [!warning] "E and B are a quarter period apart, like position and velocity of a spring"
> In a travelling plane wave in vacuum they oscillate **in phase**: both are zero together and maximal together, with $E_0 = cB_0$.[^up16em]

> [!warning] "The sine curve is the path the light follows"
> The curve plots the field values along the line of travel at one instant. Light goes straight along $x$; nothing wiggles sideways.

## Exercises

> [!question] Exercise 1 (L1)
> Give the frequency and period of 600 nm light, and the wavelength of a 600 MHz radio wave. If $E_0 = 100$ V/m, what is $B_0$?

> [!success]- Solution
> $\nu = c/\lambda = 299\,792\,458/(600 \times 10^{-9}) = 5.00 \times 10^{14}$ Hz, $T = 1/\nu = 2.00$ fs. $\lambda = c/\nu = 299\,792\,458/(600 \times 10^6) = 0.4997$ m: half a metre, nine orders of magnitude longer. $B_0 = E_0/c = 3.34 \times 10^{-7}$ T.

> [!question] Exercise 2 (L2)
> Light of 488 nm (vacuum wavelength) enters water ($n = 1.333$). Give its speed, wavelength and frequency in water. Which of the three should a table of absorption bands list, and why?

> [!success]- Solution
> $v = c/n = 2.249 \times 10^8$ m/s; $\lambda_n = 488/1.333 = 366$ nm; $\nu = c/\lambda_0 = 6.143 \times 10^{14}$ Hz, the same as in air. Tables list vacuum wavelength (or frequency), because the frequency is the invariant: the same light has different wavelengths in different media.

> [!question] Exercise 3 (L2, Python)
> Using `e_amplitude`, compute the intensity and peak field for 20 mW focused onto a 0.5 µm spot (example values), and the radiation force $P/c$ if all the light were absorbed.[^up16em]

> [!success]- Solution
> ```python
> p, d = 20e-3, 0.5e-6
> I = p / (math.pi * (d / 2) ** 2)
> print(f"I = {I:.3g} W/m^2, E0 = {e_amplitude(I):.3g} V/m, F = {p / C:.3g} N")
> # I = 1.02e+11 W/m^2, E0 = 8.76e+06 V/m, F = 6.67e-11 N
> ```
>
> Twenty times the power of the worked example gives twenty times the intensity, but only $\sqrt{20} = 4.5$ times the field, since $E_0 \propto \sqrt I$. The force, 67 pN, is the momentum flux of light ($p = U/c$).

## Mastery checklist

- [ ] 1 Recognized: I can state that light is an EM wave with perpendicular $\vec E$ and $\vec B$, travelling at $c$, and write $c = \lambda\nu$.
- [ ] 2 Understood: I can explain why frequency, not wavelength, is conserved across media, and why detectors measure intensity.
- [ ] 3 Practiced: I can convert wavelength and frequency, and compute intensity and field amplitude by hand and in Python.
- [ ] 4 Applied: I can turn a laser power and spot size from an imaging protocol into an intensity at the sample.
- [ ] 5 Explained: I can teach how Maxwell's constants give $c$, how fields, intensity and photons describe the same light, and what a detector actually measures.

## References

[^up16em]: [[University Physics (OpenStax)]], Volume 2, ch. 16 "Electromagnetic Waves" (Maxwell's equations and the prediction of EM waves, Hertz's experiments, plane waves with perpendicular in-phase fields and $E = cB$, $c = 1/\sqrt{\mu_0\varepsilon_0}$, energy and intensity, momentum and radiation pressure, production by accelerating charges and antennas).
[^up1]: [[University Physics (OpenStax)]], Volume 3, §1.3 "Refraction" (index of refraction $n = c/v$; table of indices, water 1.333).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA 2022 values: $c = 299\,792\,458$ m s⁻¹ (exact); $\varepsilon_0 = 8.854\,187\,8188(14) \times 10^{-12}$ F m⁻¹; $\mu_0 = 1.256\,637\,061\,27(20) \times 10^{-6}$ N A⁻².
