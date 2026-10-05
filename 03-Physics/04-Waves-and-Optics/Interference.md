---
aliases:
  - Constructive Interference
  - Destructive Interference
  - Young's Double-Slit Experiment
  - Optical Path Difference
  - Interférences
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Wave]]"
  - "[[Electromagnetic Wave]]"
  - "[[Refraction]]"
related:
  - "[[Diffraction]]"
  - "[[Microscopy]]"
  - "[[Complex Number]]"
  - "[[Polarization]]"
  - "[[Laser]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[NobelPrize.org]]"
---

# Interference

> [!abstract]
> When two coherent light waves overlap, they reinforce where their paths differ by a whole number of wavelengths and cancel where they differ by a half; this turns invisible differences of path, such as light slowed slightly by a transparent cell, into visible differences of brightness.

## Definition

**Interference** is the superposition of two or more coherent waves, producing a stable pattern of intensity set by their phase differences: **constructive** where they arrive in phase, **destructive** where they arrive half a period apart.[^up3][^up165] Waves are **coherent** when their phase difference stays constant in time; only then is the pattern stable.[^up3]

## Why it matters

- **Seeing living cells without stains.** Most cell components are transparent: they shift the phase of light without absorbing it. Phase-contrast and differential-interference-contrast (DIC) microscopes use interference to turn these phase shifts into brightness, so living, unlabeled cells can be watched.[^alberts]
- **Diffraction is interference of many waves.** The same path-difference rule explains gratings, the blur of a microscope and the spots of a crystal diffraction pattern ([[Diffraction]]).
- **Phase is what detectors miss.** A camera records only intensity ([[Electromagnetic Wave]]); interference is the standard way to encode phase into intensity before detection.

## Core (L1)

### Path difference sets the phase

Two waves of wavelength $\lambda$ from a common source that travel paths differing by $\Delta$ reach a point with a phase difference

$$\delta = 2\pi\,\frac{\Delta}{\lambda}.$$

- **Constructive:** $\Delta = m\lambda$, $m = 0, \pm1, \pm2, \dots$
- **Destructive:** $\Delta = (m + \tfrac12)\lambda$.

In a material of refractive index $n$ the phase accumulates $n$ times faster, so the relevant quantity is the **optical path length** $nL$ ([[Refraction]]). A transparent object of thickness $t$ and index $n_{\text{obj}}$ in a medium $n_{\text{med}}$ delays light by the **optical path difference** $\Delta = (n_{\text{obj}} - n_{\text{med}})\,t$.

### Intensity of two beams

Adding the two waves as phasors ([[Wave#Deeper (L2)]]) gives

$$I = I_1 + I_2 + 2\sqrt{I_1 I_2}\,\cos\delta, \qquad \text{and for } I_1 = I_2:\; I = 4I_1\cos^2\frac{\delta}{2}.$$

The intensity swings between 0 and $4I_1$, averaging $2I_1$: interference redistributes energy, it does not create or destroy it. If $\delta$ fluctuates randomly (incoherent sources, such as two separate lamps), $\cos\delta$ averages to zero and intensities simply add.

### Young's double slit

In 1801 Thomas Young passed light from one source through two narrow slits and saw bright and dark fringes on a screen, a pattern only waves can produce.[^up31] Splitting one wavefront into two keeps the two beams coherent. For slits a distance $d$ apart, the paths to a distant point at angle $\theta$ differ by $d\sin\theta$, so[^up31]

$$\text{bright: } d\sin\theta = m\lambda, \qquad \text{dark: } d\sin\theta = \left(m + \tfrac12\right)\lambda.$$

On a screen at distance $L \gg d$, bright fringes are spaced by $\Delta y \approx \lambda L/d$. With $\lambda = 550$ nm, $d = 0.10$ mm and $L = 1.0$ m (example values), $\Delta y = 5.5$ mm (computed below): a sub-micrometre wavelength made visible to the eye.

![[double-slit-path-difference.svg]]

### Bio: phase contrast and DIC

A thin, transparent region of a cell with $n_{\text{obj}} - n_{\text{med}} = 0.0175$ and $t = 1$ µm (invented values) delays green light (550 nm) by 17.5 nm, a phase of 0.2 rad. It absorbs nothing, so in an ordinary bright-field microscope the intensity, $|e^{i\varphi}|^2 = 1$, is the same as in the background: the region is invisible. **Phase-contrast** and **DIC** microscopes make such differences in refractive index visible as differences in brightness.[^alberts] Frits Zernike received the 1953 Nobel Prize in Physics for the phase-contrast method.[^nobel]

## Deeper (L2)

### How phase contrast works: a weak-phase model

Write the wave after a weakly phase-shifting object as $e^{i\varphi(x)} \approx 1 + i\varphi(x)$ for small $\varphi$: a strong undiffracted **background** (the 1) plus a weak **scattered** wave ($i\varphi$) a quarter period out of phase with it. The intensity $|1 + i\varphi|^2 = 1 + \varphi^2 \approx 1$ shows no first-order contrast. If the background alone is delayed by a quarter period (multiplied by $i$), the two parts are brought into phase:

$$|i + i\varphi|^2 = (1 + \varphi)^2 \approx 1 + 2\varphi.$$

Brightness now varies **linearly** with the phase, so regions of higher optical path stand out. In the instrument the background and scattered light travel through different parts of the objective, which is where the phase shift can be applied to one and not the other. The code below applies this model to a phase bump: the bright field stays at 1.000 everywhere, while phase contrast shows the bump about 1.7 times brighter than the background.

### DIC: a two-beam model

Interfering the wave with a copy of itself displaced by a small shear $s$ and offset by a phase bias $\psi$ gives

$$I(x) = \tfrac12\Big[1 + \cos\big(\varphi(x + \tfrac{s}{2}) - \varphi(x - \tfrac{s}{2}) - \psi\big)\Big] \approx \tfrac12\big[1 + \sin(s\,\varphi'(x))\big] \quad (\psi = \pi/2).$$

Brightness follows the **gradient** of optical path: one flank of an object is brighter, the other darker, like a relief lit from the side. This simplified model (the polarization optics of the instrument are left out, [[Polarization]]) shows why DIC outlines edges and does not report absolute phase.

## Mathematical representation

- Phase difference $\delta = 2\pi\Delta/\lambda$, with $\Delta$ the difference of optical path lengths $\sum_j n_j L_j$.
- Two-beam intensity $I = I_1 + I_2 + 2\sqrt{I_1I_2}\cos\delta$; fringe visibility $(I_{\max} - I_{\min})/(I_{\max} + I_{\min}) = 2\sqrt{I_1I_2}/(I_1 + I_2)$.
- Double slit: maxima at $d\sin\theta = m\lambda$; small-angle spacing $\lambda L/d$.
- Weak phase object: transmitted field $e^{i\varphi(x)}$; phase contrast $I \approx 1 + 2\varphi$; DIC $I \approx \frac12[1 + \sin(s\varphi')]$.

## Computational representation

Fields are complex numbers ([[Complex Number]]); intensities are squared moduli. A one-dimensional "cell" is a phase profile $\varphi(x)$ on a grid.

```python
import cmath
import math


def two_beam(i1: float, i2: float, delta_phi: float) -> float:
    """Intensity of two coherent beams with phase difference delta_phi (radians)."""
    return i1 + i2 + 2 * math.sqrt(i1 * i2) * math.cos(delta_phi)


def phase_difference(path_difference: float, wavelength: float) -> float:
    """delta_phi = 2 pi * path difference / wavelength (same length unit for both)."""
    return 2 * math.pi * path_difference / wavelength


for frac in (0, 0.25, 0.5, 1.0, 1.5):
    print(f"path difference {frac} lambda: I/I1 = {two_beam(1, 1, phase_difference(frac, 1)):.2f}")

lam, d, L = 550e-9, 0.10e-3, 1.0                       # Young's experiment, example values (m)
print(f"fringe spacing {lam * L / d * 1e3:.1f} mm; first bright fringe at {math.degrees(math.asin(lam / d)):.3f} deg")

# A transparent 'cell' (invented values): phase bump phi(x) = 0.3 exp(-x^2 / 2), x in um
phi = lambda x: 0.3 * math.exp(-x * x / 2)
xs = [i / 100 for i in range(-1000, 1001)]
background = sum(cmath.exp(1j * phi(x)) for x in xs) / len(xs)        # undiffracted (mean) wave
def bright_field(x): return abs(cmath.exp(1j * phi(x))) ** 2
def phase_contrast(x): return abs(cmath.exp(1j * phi(x)) - background + 1j * background) ** 2
def dic(x, shear=0.2, bias=math.pi / 2):
    return abs(cmath.exp(1j * phi(x + shear / 2)) + cmath.exp(1j * (phi(x - shear / 2) + bias))) ** 2 / 4
for x in (-1.0, 0.0, 1.0, 5.0):
    print(f"x = {x:4} um: bright field {bright_field(x):.3f}, phase contrast {phase_contrast(x):.3f}, DIC {dic(x):.3f}")
```

```text
path difference 0 lambda: I/I1 = 4.00
path difference 0.25 lambda: I/I1 = 2.00
path difference 0.5 lambda: I/I1 = 0.00
path difference 1.0 lambda: I/I1 = 4.00
path difference 1.5 lambda: I/I1 = 0.00
fringe spacing 5.5 mm; first bright fringe at 0.315 deg
x = -1.0 um: bright field 1.000, phase contrast 1.301, DIC 0.518
x =  0.0 um: bright field 1.000, phase contrast 1.579, DIC 0.500
x =  1.0 um: bright field 1.000, phase contrast 1.301, DIC 0.482
x =  5.0 um: bright field 1.000, phase contrast 0.920, DIC 0.500
```

Bright field shows nothing. Phase contrast shows the bump bright (1.579) on a darker background (0.920). DIC is brighter on the rising flank, darker on the falling flank, and flat (0.500) at the top and far away, where the gradient is zero.

## Worked example

> [!example] How far is the first bright fringe? (example values)
> Two slits $d = 0.20$ mm apart, light $\lambda = 500$ nm, screen at $L = 1.5$ m.
> 1. First maximum: $\sin\theta_1 = \lambda/d = 500 \times 10^{-9}/0.20 \times 10^{-3} = 2.5 \times 10^{-3}$, $\theta_1 = 0.143°$.
> 2. On the screen: $y_1 = L\tan\theta_1 \approx L\lambda/d = 1.5 \times 2.5 \times 10^{-3} = 3.75$ mm.
> 3. First dark fringe: $d\sin\theta = \lambda/2$, at half that distance, 1.9 mm.
> 4. Halving $d$ doubles the spacing: closer sources give wider fringes, the inverse relation that diffraction will generalize ([[Diffraction]]).

## Common misconceptions

> [!warning] "Destructive interference destroys light energy"
> The energy missing from dark fringes is found in the bright ones, which reach four times the intensity of one beam; on average the intensity is $I_1 + I_2$.

> [!warning] "Any two light beams interfere"
> A stable pattern needs a constant phase difference. Two independent lamps change their relative phase far too fast, so their intensities just add; Young obtained coherent beams by splitting one source.[^up31]

> [!warning] "Phase contrast shows how thick or dense a structure is"
> It responds to the optical path difference $(n_{\text{obj}} - n_{\text{med}})t$, which mixes thickness and refractive index, and only linearly for weak phase shifts (Exercise 4). Brightness in such images is contrast, not a measurement of mass or volume.

## Exercises

> [!question] Exercise 1 (L1)
> Two coherent beams of equal intensity $I_1$ meet with path differences of $2\lambda$, $1.5\lambda$ and $0.25\lambda$. Give the resulting intensity in each case.

> [!success]- Solution
> $\delta = 2\pi\Delta/\lambda$ = $4\pi$, $3\pi$, $\pi/2$, so $I = 4I_1\cos^2(\delta/2)$ = $4I_1$ (constructive), $0$ (destructive) and $2I_1$ (the beams add as if incoherent).

> [!question] Exercise 2 (L1)
> In a Young experiment with $d = 0.20$ mm and $L = 1.5$ m, what fringe spacing does 500 nm light give? And 650 nm?

> [!success]- Solution
> $\Delta y = \lambda L/d$ = 3.75 mm for 500 nm and 4.9 mm for 650 nm: red fringes are wider, since spacing is proportional to wavelength.

> [!question] Exercise 3 (L2)
> A cell region (invented values: $n = 1.3525$, thickness 1 µm) sits in medium of index 1.335. Compute the optical path difference and phase shift at 550 nm, and the intensity predicted in bright field and in phase contrast (weak-phase model).

> [!success]- Solution
> $\Delta = 0.0175 \times 1000$ nm $= 17.5$ nm, $\varphi = 2\pi \times 17.5/550 = 0.200$ rad. Bright field: $|e^{i\varphi}|^2 = 1$, no contrast. Phase contrast: $I \approx 1 + 2\varphi = 1.40$, a 40 % brighter region.

> [!question] Exercise 4 (L2, Python)
> Repeat the phase-contrast model for peak phases $\varphi_0 = 0.1$, 0.3 and 1.0 rad, and compare the ratio of the peak to the background with the weak-phase prediction $1 + 2\varphi_0$.

> [!success]- Solution
> ```python
> for phi0 in (0.1, 0.3, 1.0):
>     phi = lambda x: phi0 * math.exp(-x * x / 2)
>     bg = sum(cmath.exp(1j * phi(x)) for x in xs) / len(xs)
>     pc = lambda x: abs(cmath.exp(1j * phi(x)) - bg + 1j * bg) ** 2
>     print(f"phi0 = {phi0}: centre/background = {pc(0.0) / pc(9.9):.3f}, weak-phase 1 + 2 phi0 = {1 + 2 * phi0:.3f}")
> # phi0 = 0.1: centre/background = 1.213, weak-phase 1 + 2 phi0 = 1.200
> # phi0 = 0.3: centre/background = 1.716, weak-phase 1 + 2 phi0 = 1.600
> # phi0 = 1.0: centre/background = 4.350, weak-phase 1 + 2 phi0 = 3.000
> ```
>
> The linear prediction holds for small phases and fails for 1 rad, where brightness no longer scales with optical path. Intensities in phase-contrast images are therefore not proportional to thickness for thick or dense objects.

## Mastery checklist

- [ ] 1 Recognized: I can state the conditions for constructive and destructive interference and what coherence means.
- [ ] 2 Understood: I can derive the two-beam intensity, explain Young's experiment and why a transparent object is invisible in bright field.
- [ ] 3 Practiced: I can compute phase and optical path differences, fringe positions, and phase-contrast and DIC model images in Python.
- [ ] 4 Applied: I can interpret a phase-contrast or DIC image of living cells, knowing which features reflect optical path and which reflect gradients.
- [ ] 5 Explained: I can teach how interference turns phase into intensity, with the limits of the weak-phase model.

## References

[^up3]: [[University Physics (OpenStax)]], Volume 3, ch. 3 "Interference" (coherent sources, path difference, constructive and destructive interference of light).
[^up165]: [[University Physics (OpenStax)]], Volume 1, §16.5 "Interference of Waves" (superposition of two waves differing by a phase shift).
[^up31]: [[University Physics (OpenStax)]], Volume 3, §3.1 "Young's Double-Slit Interference" (Young's 1801 experiment; fringes as evidence for the wave nature of light; $d\sin\theta = m\lambda$ for maxima, $(m + \frac12)\lambda$ for minima).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of microscopy (most cell components are transparent; phase-contrast and DIC microscopes exploit interference to turn refractive-index differences into brightness differences, so living unstained cells can be observed).
[^nobel]: [[NobelPrize.org]], Nobel Prize in Physics 1953 (Frits Zernike, "for his demonstration of the phase contrast method, especially for his invention of the phase contrast microscope").
