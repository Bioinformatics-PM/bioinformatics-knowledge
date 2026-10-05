---
aliases:
  - Thin Lens
  - Thin-Lens Equation
  - Focal Length
  - Lentille
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Refraction]]"
related:
  - "[[Microscopy]]"
  - "[[Diffraction Limit]]"
  - "[[Diffraction]]"
  - "[[Fluorescence Microscopy]]"
  - "[[Matrix Multiplication]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
---

# Lens

> [!abstract]
> A lens bends light by refraction so that rays leaving one point of an object meet again at one point of an image; one equation, $1/d_o + 1/d_i = 1/f$, says where the image forms and how large it is, and two lenses in a row make a microscope, whose magnification is not the same thing as its resolution.

## Definition

A **lens** is a transparent object with curved surfaces that refracts light to form an image. A **converging** lens (thicker at the centre) brings rays parallel to its axis to a focus at the **focal point** $F'$, at the **focal length** $f > 0$ from the lens; a **diverging** lens makes them spread as if from a point in front of it ($f < 0$). A lens is **thin** when its thickness is small compared with $f$.[^up24]

## Why it matters

- **A microscope is two lenses.** The objective forms an enlarged real image; an eyepiece or a camera records it.[^up28] Its magnification sets the scale of every micrograph.
- **Pixel size is a lens calculation.** The size of one camera pixel at the sample equals the physical pixel size divided by the magnification. Every length, area or density measured on an image depends on that number, and it must be small enough to sample the finest resolvable detail (Exercise 3).
- **Magnification is not resolution.** Enlarging the image does not reveal detail that diffraction at the objective has blurred; resolution depends on the wavelength and the numerical aperture ([[Diffraction Limit]], [[Microscopy]]).[^alberts]

## Core (L1)

### Three rays and two equations

Three rays from the tip of an object locate its image (figure):[^up24]

1. a ray parallel to the axis leaves through the focal point $F'$ on the far side;
2. a ray through the centre of the lens goes straight on;
3. a ray through the near focal point $F$ leaves parallel to the axis.

With $d_o$ the object distance, $d_i$ the image distance and $h_o$, $h_i$ the object and image heights, the **thin-lens equation** and the **magnification** are[^up24]

$$\frac{1}{d_o} + \frac{1}{d_i} = \frac{1}{f}, \qquad m = \frac{h_i}{h_o} = -\frac{d_i}{d_o}.$$

Sign convention: $d_i > 0$ for a real image on the far side, $d_i < 0$ for a virtual image on the object side; $m < 0$ means inverted. The optical **power** $1/f$ is measured in dioptres (m⁻¹). The focal length follows from the shape and index of the lens through the **lensmaker's equation** $1/f = (n - 1)(1/R_1 - 1/R_2)$, with $R_1$, $R_2$ the radii of curvature of its surfaces.[^up24]

![[thin-lens-ray-diagram.svg]]

### Where the image forms

Solving for $d_i = \left(1/f - 1/d_o\right)^{-1}$ (with $f = 10$ cm, computed below):

| Object position | Example | Image | Used in |
|---|---|---|---|
| $d_o > 2f$ | $d_o = 30$ cm: $d_i = 15$ cm, $m = -0.5$ | real, inverted, reduced | camera, eye |
| $f < d_o < 2f$ | $d_o = 15$ cm: $d_i = 30$ cm, $m = -2$ | real, inverted, enlarged | microscope objective |
| $d_o < f$ | $d_o = 5$ cm: $d_i = -10$ cm, $m = +2$ | virtual, upright, enlarged | magnifier, eyepiece |

### Bio: objective and eyepiece

In a compound microscope the specimen sits just beyond the focal point of the **objective**, which forms a real, inverted, enlarged image of magnification $m_{\text{obj}} = -d_i/d_o$. The **eyepiece** is used as a magnifier on that intermediate image; with the final image at infinity, its angular magnification is $M_{\text{eye}} = 25 \text{ cm}/f_{\text{eye}}$, 25 cm being the near point of a typical eye. The total magnification is the product[^up28]

$$M = m_{\text{obj}}\,M_{\text{eye}}.$$

A 40× objective with a 10× eyepiece gives 400×. Whatever the product, two points closer than about $0.61\lambda/\mathrm{NA}$, roughly 0.2 µm with the best oil objectives, stay merged into one blur.[^alberts] Magnification only needs to be large enough for that blur to be seen or sampled; more makes the image bigger, not sharper.

## Deeper (L2)

### Deriving the thin-lens equation

Ray 2 (through the centre) gives similar triangles on both sides of the lens: $h_i/h_o = -d_i/d_o$. Ray 1 (parallel, then through $F'$) gives similar triangles on the image side, between the lens and $F'$ and between $F'$ and the image: $h_i/h_o = -(d_i - f)/f$. Equating, $d_i f = d_o d_i - d_o f$; dividing by $d_o d_i f$ gives $1/d_o + 1/d_i = 1/f$.

### Ray-transfer matrices

In the paraxial approximation a ray is described by its height $y$ and angle $\alpha$ to the axis, and each optical element acts linearly on $(y, \alpha)$ ([[Matrix Multiplication]]):

$$T(d) = \begin{pmatrix} 1 & d \\ 0 & 1 \end{pmatrix} \text{ (travel over } d\text{)}, \qquad L(f) = \begin{pmatrix} 1 & 0 \\ -1/f & 1 \end{pmatrix} \text{ (thin lens)}.$$

The system from object to image plane is $S = T(d_i)\,L(f)\,T(d_o)$. Its upper-right entry is $B = d_o + d_i - d_o d_i/f$. All rays from one object point meet at one image point when the image height does not depend on the ray angle, $B = 0$, which is exactly the thin-lens equation; the upper-left entry is then the magnification $A = 1 - d_i/f = -d_i/d_o$. Two thin lenses in contact multiply to $L(f_2)L(f_1) = L(f)$ with $1/f = 1/f_1 + 1/f_2$: powers add. Any sequence of thin lenses and gaps is described the same way, by one product of matrices.

## Mathematical representation

- Thin lens: $d_o^{-1} + d_i^{-1} = f^{-1}$; $m = -d_i/d_o$; power $P = 1/f$ (dioptres); lensmaker $1/f = (n-1)(1/R_1 - 1/R_2)$.
- Microscope: $M = m_{\text{obj}} \times (25\text{ cm}/f_{\text{eye}})$. Paraxial optics: ray $\binom{y}{\alpha} \mapsto S\binom{y}{\alpha}$ with $S \in \mathbb{R}^{2\times 2}$, $\det S = 1$ between media of equal index; imaging condition $S_{12} = 0$, magnification $S_{11}$.
- Sampling: pixel size at the sample $p_{\text{sample}} = p_{\text{camera}}/M$.

## Computational representation

```python
def thin_lens(f: float, d_o: float) -> tuple[float, float]:
    """Image distance and lateral magnification: 1/d_o + 1/d_i = 1/f, m = -d_i/d_o (real-is-positive)."""
    d_i = 1 / (1 / f - 1 / d_o)
    return d_i, -d_i / d_o


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def travel(d: float) -> list[list[float]]:
    """Ray-transfer matrix of free propagation over a distance d."""
    return [[1.0, d], [0.0, 1.0]]


def lens(f: float) -> list[list[float]]:
    """Ray-transfer matrix of a thin lens of focal length f."""
    return [[1.0, 0.0], [-1 / f, 1.0]]


for f, d_o in ((10, 15), (10, 30), (10, 5)):               # cm
    d_i, m = thin_lens(f, d_o)
    print(f"f = {f} cm, d_o = {d_o} cm: d_i = {d_i:.1f} cm, m = {m:.2f}")

d_i, m_obj = thin_lens(4.0, 4.2)                           # objective, mm (example values)
m_eye = 250 / 25                                           # eyepiece f = 25 mm, near point 250 mm
print(f"objective: d_i = {d_i:.0f} mm, m = {m_obj:.0f}; eyepiece {m_eye:.0f}x; total {m_obj * m_eye:.0f}x")
```

```text
f = 10 cm, d_o = 15 cm: d_i = 30.0 cm, m = -2.00
f = 10 cm, d_o = 30 cm: d_i = 15.0 cm, m = -0.50
f = 10 cm, d_o = 5 cm: d_i = -10.0 cm, m = 2.00
objective: d_i = 84 mm, m = -20; eyepiece 10x; total -200x
```

## Worked example

> [!example] A two-lens microscope (example values)
> Objective $f = 4.0$ mm, specimen at $d_o = 4.2$ mm; eyepiece $f = 25$ mm.
> 1. Objective image: $1/d_i = 1/4.0 - 1/4.2 = 0.0119$ mm⁻¹, so $d_i = 84$ mm, real.
> 2. Objective magnification: $m = -84/4.2 = -20$: inverted, 20 times larger.
> 3. Eyepiece: $M_{\text{eye}} = 250 \text{ mm}/25 \text{ mm} = 10$.
> 4. Total: $M = -20 \times 10 = -200$: the final image is inverted, as in any compound microscope with two converging lenses. Moving the specimen to 4.1 mm puts the image at $d_i = 164$ mm and $m = -40$: small changes near $f$ move the image a lot, which is why focusing a microscope needs fine adjustment.

## Common misconceptions

> [!warning] "More magnification shows more detail"
> Detail is limited by diffraction at the objective, set by wavelength and numerical aperture. Beyond the magnification that makes the smallest resolvable spacing visible, the image grows without new information.[^alberts]

> [!warning] "Covering half of a lens removes half of the image"
> Every part of the lens receives light from every point of the object, so each image point is formed by the whole lens. Covering half of it keeps the whole image, dimmer (and with slightly worse resolution, since the aperture is smaller).

## Exercises

> [!question] Exercise 1 (L1)
> A converging lens has $f = 10$ cm. Find the image distance and magnification for an object at 15 cm and at 5 cm, and describe each image.

> [!success]- Solution
> $d_o = 15$: $1/d_i = 1/10 - 1/15 = 1/30$, $d_i = 30$ cm, $m = -2$: real, inverted, twice larger. $d_o = 5$: $1/d_i = 1/10 - 1/5 = -1/10$, $d_i = -10$ cm, $m = +2$: virtual, upright, on the object side, as in a magnifying glass.

> [!question] Exercise 2 (L2, Python)
> Without using `thin_lens`, find the image distance of the worked example's objective by solving $B(d_i) = 0$ for the system matrix with bisection, and read the magnification from $A$.

> [!success]- Solution
> ```python
> d_o, f = 4.2, 4.0
> def b_of(di): return matmul(travel(di), matmul(lens(f), travel(d_o)))[0][1]
> lo, hi = 10.0, 1000.0
> for _ in range(60):
>     mid = (lo + hi) / 2
>     lo, hi = (lo, mid) if b_of(lo) * b_of(mid) <= 0 else (mid, hi)
> print("bisection d_i:", round(lo, 4), "A =", round(matmul(travel(lo), matmul(lens(f), travel(d_o)))[0][0], 3))
> # bisection d_i: 84.0 A = -20.0
> ```
>
> The imaging condition reproduces $d_i = 84$ mm and $m = -20$. The same approach works for systems of many elements, where no closed formula is at hand.

> [!question] Exercise 3 (L2)
> A camera with 6.5 µm pixels (example value) is used with a 20× NA 0.75, a 60× NA 1.4 and a 100× NA 1.4 objective, in green light (520 nm). For each, compare the pixel size at the sample with half the Rayleigh distance $0.61\lambda/\mathrm{NA}$.[^alberts] Which combinations sample the resolution?

> [!success]- Solution
> Pixel at the sample: 325, 108 and 65 nm. Rayleigh distance: 423 nm (NA 0.75) and 227 nm (NA 1.4), half of it 211 and 113 nm. Only the 60× and 100× objectives give pixels below half the resolvable distance, so that two resolved points can fall on two pixels with a dimmer one between. The 20× image is under-sampled: the camera, not the optics, limits it. The 100× adds no resolution over 60× at the same NA, only smaller pixels and a smaller field of view.

## Mastery checklist

- [ ] 1 Recognized: I can define focal length, real and virtual images, and state the thin-lens and magnification equations.
- [ ] 2 Understood: I can trace the three principal rays, derive the thin-lens equation and explain why magnification and resolution differ.
- [ ] 3 Practiced: I can solve thin-lens and microscope problems by hand and with ray-transfer matrices in Python.
- [ ] 4 Applied: I can compute the pixel size of a real microscope-camera setup and decide whether it samples the optical resolution.
- [ ] 5 Explained: I can teach how objective, eyepiece and camera combine, and why choosing an objective by magnification alone is a mistake.

## References

[^up24]: [[University Physics (OpenStax)]], Volume 3, §2.4 "Thin Lenses" (converging and diverging lenses, focal length, ray tracing rules, thin-lens equation, magnification, lensmaker's equation, power in dioptres).
[^up28]: [[University Physics (OpenStax)]], Volume 3, §2.8 "Microscopes and Telescopes" (compound microscope: objective forms a real enlarged image, eyepiece acts as a magnifier with $M = 25\text{ cm}/f$; net magnification as a product).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of microscopy (magnification versus resolution; resolution limit $0.61\lambda/(n\sin\theta)$, about 0.2 µm for light microscopes).
