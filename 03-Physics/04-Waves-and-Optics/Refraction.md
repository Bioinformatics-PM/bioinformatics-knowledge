---
aliases:
  - Snell's Law
  - Refractive Index
  - Total Internal Reflection
  - TIR
  - Réfraction
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
related:
  - "[[Lens]]"
  - "[[Microscopy]]"
  - "[[Diffraction Limit]]"
  - "[[Fluorescence Microscopy]]"
  - "[[Interference]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Axelrod 1981 - Cell-Substrate Contacts Illuminated by Total Internal Reflection Fluorescence]]"
---

# Refraction

> [!abstract]
> Light bends when it passes from one material into another in which it travels at a different speed; Snell's law gives the new direction, and beyond a critical angle light cannot leave a dense medium at all, a trap that oil-immersion objectives avoid and TIRF microscopy exploits.

## Definition

**Refraction** is the change of direction of light crossing the boundary between two media in which it travels at different speeds. Each medium has a **refractive index** $n = c/v \ge 1$, the ratio of the speed of light in vacuum to its speed in the medium, and the angles from the normal on both sides obey **Snell's law**:[^up13]

$$n_1\sin\theta_1 = n_2\sin\theta_2.$$

## Why it matters

- **Every lens works by refraction**, the objective of a microscope included ([[Lens]]).
- **Resolution depends on the medium.** The resolving power of an objective grows with its numerical aperture $\mathrm{NA} = n\sin\theta$, which contains the refractive index of the medium between specimen and lens; immersion oil raises it ([[Diffraction Limit]], [[Microscopy]]).[^alberts]
- **TIRF images only the bottom of the cell.** Total internal reflection at the coverslip leaves a thin evanescent field that excites only fluorophores near the surface, where cells contact the substrate.[^axelrod]
- **Small index differences are contrast.** Organelles differ slightly in refractive index from their surroundings; phase-contrast and DIC microscopes turn this into brightness ([[Interference]]).[^alberts]

## Core (L1)

**Refractive index.** Typical values are 1.000293 for air, 1.333 for water and 1.52 for crown glass.[^up13] In a medium the frequency of light is unchanged and its wavelength becomes $\lambda_0/n$, with $\lambda_0$ the vacuum wavelength ([[Electromagnetic Wave]]).

### Snell's law from wavefronts

Let a plane wave cross a flat interface. Along the interface, the crests on both sides must coincide, otherwise the wave would be torn apart at the boundary. The spacing of crests measured along the interface is $\lambda_1/\sin\theta_1$ in medium 1 and $\lambda_2/\sin\theta_2$ in medium 2, so

$$\frac{\lambda_1}{\sin\theta_1} = \frac{\lambda_2}{\sin\theta_2} \quad\Longrightarrow\quad \frac{\lambda_0/n_1}{\sin\theta_1} = \frac{\lambda_0/n_2}{\sin\theta_2} \quad\Longrightarrow\quad n_1\sin\theta_1 = n_2\sin\theta_2.$$

Entering a medium of higher index, light bends **toward** the normal; entering a lower index, **away** from it. At normal incidence ($\theta_1 = 0$) it does not bend.

### Total internal reflection

Going from high to low index ($n_1 > n_2$), $\theta_2$ reaches 90° when $\sin\theta_1 = n_2/n_1$. Beyond this **critical angle**[^up14]

$$\theta_c = \arcsin\frac{n_2}{n_1}$$

no refracted ray exists and all the light is reflected: **total internal reflection** (TIR). From glass, $\theta_c = 41.2°$ into air and $61.3°$ into water (computed below). From air into glass there is no critical angle.

![[refraction-snell-total-internal-reflection.svg]]

### Bio: immersion objectives

An objective collects a cone of light of half-angle $\theta$ in a medium of index $n$; its numerical aperture is $\mathrm{NA} = n\sin\theta$.[^alberts] With air between coverslip and lens, $n \approx 1$ caps the NA below 1. Refraction shows where the light is lost: a ray leaving the specimen at more than 41.2° inside the glass coverslip is totally reflected at the glass-air surface and never reaches the lens. Filling the gap with an oil whose index matches the glass (taken here as 1.52) removes that interface, and objectives reach NA 1.4,[^alberts] a half-angle of $\arcsin(1.4/1.52) = 67°$ in the oil.

## Deeper (L2)

### The evanescent wave and TIRF

Under total internal reflection the field does not stop dead at the interface. The component of the wave vector normal to the interface in medium 2 is $k_z = \frac{2\pi}{\lambda_0}\sqrt{n_2^2 - n_1^2\sin^2\theta}$. Beyond $\theta_c$ the square root is imaginary, $k_z = i\kappa$ with $\kappa = \frac{2\pi}{\lambda_0}\sqrt{n_1^2\sin^2\theta - n_2^2}$, so the field decays as $e^{-\kappa z}$ and the intensity as $e^{-2\kappa z} = e^{-z/d}$, with

$$d = \frac{\lambda_0}{4\pi\sqrt{n_1^2\sin^2\theta - n_2^2}}.$$

This **evanescent wave** carries no energy away but can excite molecules. For glass to water at 488 nm, $d$ falls from 249 nm at 62° to 69 nm at 72° (Exercise 4). Axelrod used it in 1981 to excite fluorescence only from molecules within about one wavelength of the substrate, imaging the contacts between cultured cells and their substrate: **total internal reflection fluorescence (TIRF)** microscopy.[^axelrod] Ordinary illumination, which crosses the whole cell, would add the fluorescence of everything above.

**Through the objective.** If the TIR beam is sent through the objective, the largest angle it can reach in the glass satisfies $n_1\sin\theta_{\max} = \mathrm{NA}$. TIR at a glass-water interface needs $n_1\sin\theta > n_2 = 1.333$, so the objective must have $\mathrm{NA} > 1.333$. Since $\mathrm{NA} \le n$, this requires an immersion medium of index above that of water, such as oil.

## Mathematical representation

- $n = c/v$; in a medium $\lambda_n = \lambda_0/n$, frequency unchanged.
- Snell: $n_1\sin\theta_1 = n_2\sin\theta_2$, angles from the normal; equivalently, the components of $n_1\hat{\vec k}_1$ and $n_2\hat{\vec k}_2$ (unit vectors along the rays) parallel to the interface are equal.
- Critical angle $\theta_c = \arcsin(n_2/n_1)$ for $n_1 > n_2$; TIR for $\theta > \theta_c$.
- Evanescent intensity $I(z) = I_0\,e^{-z/d}$, $d = \lambda_0 / \big(4\pi\sqrt{n_1^2\sin^2\theta - n_2^2}\big)$; numerical aperture $\mathrm{NA} = n\sin\theta \le n$.

## Computational representation

A refraction step returns either an angle or "no transmitted ray"; `None` makes total internal reflection explicit instead of letting `math.asin` raise an error.

```python
import math

N_AIR, N_WATER, N_GLASS = 1.000293, 1.333, 1.52      # University Physics, Vol. 3, table of indices


def snell(n1: float, n2: float, theta1_deg: float) -> float | None:
    """Refraction angle (degrees) from n1 sin(theta1) = n2 sin(theta2); None if totally reflected."""
    s = n1 * math.sin(math.radians(theta1_deg)) / n2
    return math.degrees(math.asin(s)) if s <= 1 else None


def critical_angle(n1: float, n2: float) -> float | None:
    """Critical angle (degrees) for light going from n1 into n2; None if n1 <= n2 (no TIR)."""
    return math.degrees(math.asin(n2 / n1)) if n1 > n2 else None


def penetration_depth_nm(wavelength_nm: float, n1: float, n2: float, theta_deg: float) -> float:
    """1/e depth of the evanescent intensity beyond the interface, for theta above the critical angle."""
    s = (n1 * math.sin(math.radians(theta_deg))) ** 2 - n2 ** 2
    return wavelength_nm / (4 * math.pi * math.sqrt(s))


print("air -> water at 45 deg:", round(snell(N_AIR, N_WATER, 45), 1))
print("glass -> water at 40 deg:", round(snell(N_GLASS, N_WATER, 40), 1), "| at 70 deg:", snell(N_GLASS, N_WATER, 70))
print("critical angles: glass/air", round(critical_angle(N_GLASS, N_AIR), 1),
      "glass/water", round(critical_angle(N_GLASS, N_WATER), 1), "air/glass", critical_angle(N_AIR, N_GLASS))
print(f"TIRF at 488 nm, 70 deg: d = {penetration_depth_nm(488, N_GLASS, N_WATER, 70):.0f} nm")
```

```text
air -> water at 45 deg: 32.0
glass -> water at 40 deg: 47.1 | at 70 deg: None
critical angles: glass/air 41.2 glass/water 61.3 air/glass None
TIRF at 488 nm, 70 deg: d = 76 nm
```

## Worked example

> [!example] Setting up TIRF at a glass-water interface (example objective)
> Coverslip $n_1 = 1.52$, aqueous medium $n_2 = 1.333$, laser 488 nm, objective NA 1.45 (example value).
> 1. Critical angle: $\theta_c = \arcsin(1.333/1.52) = 61.3°$.
> 2. Largest angle the objective can deliver in the glass: $\arcsin(1.45/1.52) = 72.5°$. TIR is possible between 61.3° and 72.5°.
> 3. Depth at 70°: $n_1^2\sin^2\theta - n_2^2 = 2.040 - 1.777 = 0.263$, $d = 488/(4\pi \times 0.513) = 76$ nm.
> 4. Interpretation: the excitation falls to $1/e$ within 76 nm and to 5 % within $3d \approx 230$ nm, a thin slice compared with the size of a cell ([[Cell]]); only the region facing the coverslip lights up.
> 5. Raising $\theta$ toward 72.5° thins the slice only slightly (69 nm at 72°): close to $\theta_c$, small angle changes matter much more.

## Common misconceptions

> [!warning] "Total internal reflection can happen whenever light hits a surface obliquely"
> Only when going from a higher to a lower index. Light going from air into glass is always partly transmitted.[^up14]

> [!warning] "Under total internal reflection, no light enters the second medium"
> No energy is transmitted on average, but an evanescent field extends about 100 nm into it, enough to excite fluorophores; TIRF is built on that field.[^axelrod]

## Exercises

> [!question] Exercise 1 (L1)
> Light passes from air into water at 30° from the normal. Find the refraction angle. Does it bend toward or away from the normal?

> [!success]- Solution
> $\sin\theta_2 = 1.000293 \times \sin 30° / 1.333 = 0.375$, $\theta_2 = 22.0°$: toward the normal, since water has the higher index.

> [!question] Exercise 2 (L1)
> Give the critical angle from glass ($n = 1.52$) into water and into air. Which interface traps more light?

> [!success]- Solution
> $\arcsin(1.333/1.52) = 61.3°$ and $\arcsin(1.000293/1.52) = 41.2°$. Glass-air traps every ray steeper than 41.2°, so it traps more; the larger the index contrast, the smaller the escape cone.

> [!question] Exercise 3 (L2)
> Show that an objective working in air cannot have NA above 1. What half-angle does an air objective of NA 0.95 need, and an oil objective of NA 1.4 ($n = 1.52$)?

> [!success]- Solution
> $\mathrm{NA} = n\sin\theta$ with $n = 1.0003$ and $\sin\theta \le 1$, so $\mathrm{NA} \le 1$; equivalently, rays steeper than 41.2° in the coverslip never cross the glass-air surface. NA 0.95 in air needs $\theta = \arcsin 0.95 = 71.8°$, already close to the limit; NA 1.4 in oil needs $\arcsin(1.4/1.52) = 67.1°$.

> [!question] Exercise 4 (L2, Python)
> With `penetration_depth_nm`, compute $d$ at 62°, 65°, 70° and 72° for 488 nm and 640 nm light (glass to water). How do angle and wavelength change the optical section?

> [!success]- Solution
> ```python
> for lam in (488, 640):
>     print(lam, [round(penetration_depth_nm(lam, N_GLASS, N_WATER, t)) for t in (62, 65, 70, 72)])
> # 488 [249, 112, 76, 69]
> # 640 [327, 146, 99, 91]
> ```
>
> $d$ diverges as $\theta \to \theta_c$ and levels off at larger angles; it scales linearly with wavelength, so a red channel samples a section about $640/488 = 1.31$ times thicker than a blue one at the same angle. Two-colour TIRF images therefore do not probe exactly the same layer.

## Mastery checklist

- [ ] 1 Recognized: I can state Snell's law, define the refractive index and the critical angle.
- [ ] 2 Understood: I can derive Snell's law from matching wavefronts, and explain why oil immersion increases the NA.
- [ ] 3 Practiced: I can compute refraction angles, critical angles and evanescent depths by hand and in Python, handling the TIR case.
- [ ] 4 Applied: I can check whether a given objective, coverslip and medium allow TIRF, and estimate the thickness of the excited layer.
- [ ] 5 Explained: I can teach how refraction limits and enables microscopy: light trapped by TIR, immersion media, evanescent fields and index contrast in living cells.

## References

[^up13]: [[University Physics (OpenStax)]], Volume 3, §1.3 "Refraction" (index of refraction $n = c/v$; table of indices: air 1.000293, water 1.333, crown glass 1.52; Snell's law).
[^up14]: [[University Physics (OpenStax)]], Volume 3, §1.4 "Total Internal Reflection" (critical angle $\theta_c = \sin^{-1}(n_2/n_1)$ for $n_1 > n_2$).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of microscopy (numerical aperture $n\sin\theta$ with the refractive index of the medium, air or immersion oil; NA 1.4 oil objectives; phase-contrast and DIC microscopy of refractive-index differences).
[^axelrod]: [[Axelrod 1981 - Cell-Substrate Contacts Illuminated by Total Internal Reflection Fluorescence]], *Journal of Cell Biology* 89(1):141-145 (evanescent wave of a totally internally reflected laser beam excites only fluorophores within one wavelength or less of the substrate; cell-substrate contacts).
