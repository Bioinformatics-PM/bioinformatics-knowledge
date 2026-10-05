---
aliases:
  - Single-Slit Diffraction
  - Diffraction Grating
  - Bragg's Law
  - Airy Pattern
  - Loi de Bragg
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Wave]]"
  - "[[Interference]]"
  - "[[Electromagnetic Spectrum]]"
related:
  - "[[Diffraction Limit]]"
  - "[[Microscopy]]"
  - "[[X-ray Crystallography]]"
  - "[[Protein Structure]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[RCSB Protein Data Bank]]"
  - "[[NobelPrize.org]]"
  - "[[Watson 1953 - Molecular Structure of Nucleic Acids]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Diffraction

> [!abstract]
> A wave that passes through an opening or past an edge spreads out, and the wavelets from different parts of the opening interfere; the dark and bright directions sit at angles set by wavelength divided by size, which blurs every microscope image and lets X-rays measure the distances between atoms in a protein crystal.

## Definition

**Diffraction** is the bending and spreading of a wave as it passes the edges of an opening or an obstacle. By Huygens's principle every point of a wavefront acts as a source of secondary wavelets, and the diffraction pattern is the interference of all of them ([[Interference]]).[^up4] This note treats **Fraunhofer** (far-field) diffraction: the pattern is observed far away, or in the focal plane of a lens, so the rays leaving the opening toward one point of the pattern are parallel.

## Why it matters

- **It limits every light microscope.** The objective is a circular aperture: it turns each point of the specimen into a small disk with rings, so points closer than about 0.2 µm merge, whatever the magnification ([[Microscopy]], [[Diffraction Limit]]).[^alberts]
- **It reads atomic structures.** Atomic structures of proteins have come mainly from X-ray crystallography (and NMR spectroscopy), which measures how a crystal diffracts X-rays ([[X-ray Crystallography]], [[Protein Structure]]).[^berg] Each PDB entry states its experimental method and, for diffraction methods, a resolution in ångströms:[^pdb] that number comes from Bragg's law (below).
- **It separates colours.** A grating sends each wavelength to its own angle,[^up4] so it can pick out the wavelengths used in absorbance and fluorescence measurements ([[Spectroscopy]]).

## Core (L1)

An opening much wider than the wavelength lets light through in a straight beam with a sharp shadow; as the width $a$ approaches $\lambda$, the beam spreads over angles of order $\lambda/a$.[^up4] Visible light (0.4 to 0.7 µm)[^alberts] therefore spreads noticeably only at openings of a few micrometres or less, the scale of the finest details a microscope must render.

### Single slit: where the dark fringes are

Pair each ray from the upper half of a slit of width $a$ with the ray $a/2$ below it. Toward angle $\theta$ the two differ in path by $(a/2)\sin\theta$; if that is $\lambda/2$, every pair cancels and the direction is dark. Dividing the slit into 4, 6, … strips gives the other dark directions:[^up4]

$$a\sin\theta = m\lambda, \qquad m = \pm1, \pm2, \dots \quad \text{(minima)}.$$

Straight ahead ($\theta = 0$) all wavelets are in phase: the bright **central maximum**, bounded by $\sin\theta = \pm\lambda/a$, is twice as wide as the side fringes. A narrower slit gives a wider pattern.

### Diffraction grating

A grating is a large number $N$ of parallel slits at spacing $d$ (gratings are specified in lines per mm, $d = 1/\text{lines per mm}$). Neighbouring slits differ in path by $d\sin\theta$, so all $N$ beams add in phase when[^up4]

$$d\sin\theta = m\lambda, \qquad m = 0, \pm1, \pm2, \dots \quad \text{(principal maxima)}.$$

It is the double-slit condition ([[Interference]]), but with many slits the maxima become narrow, bright lines (L2). Because $\theta$ depends on $\lambda$, each order $m \neq 0$ spreads white light into a spectrum. With 600 lines/mm ($d = 1.667$ µm, example values), the first order sends 450 nm light to 15.7° and 650 nm light to 23.0° (computed below).

### Circular aperture and the Rayleigh criterion

A [[Lens|lens]] or a pinhole is a circular aperture. Its pattern is a bright central disk (the Airy disk) surrounded by faint rings; for diameter $D$ the first dark ring lies at $\sin\theta_1 = 1.22\,\lambda/D$. Two point sources are **just resolved** when the centre of one pattern falls on the first minimum of the other (Rayleigh criterion), at an angular separation of $1.22\,\lambda/D$.[^up45] For a microscope objective this becomes a distance in the specimen, $d_{\min} = 0.61\,\lambda/(n\sin\alpha) = 0.61\,\lambda/\mathrm{NA}$,[^alberts] with $n$ the refractive index in front of the objective, $\alpha$ the half-angle of the cone of light it collects and $\mathrm{NA} = n\sin\alpha$ its numerical aperture. With violet light (0.4 µm) and NA 1.4, $d_{\min}$ is just under 0.2 µm[^alberts] (0.174 µm, computed below). Why 1.22 becomes 0.61, Abbe's form of the limit and the point-spread function are in [[Diffraction Limit]]; the Airy profile of two resolved points is computed in [[Microscopy]].

### Bragg's law: diffraction by crystals

A crystal is a regular three-dimensional array of atoms. X-ray wavelengths range from about $10^{-8}$ to $10^{-12}$ m and atoms are about 0.1 nm across, so X-rays are diffracted by the arrangement of atoms.[^up46] Max von Laue proposed in 1912 that crystals diffract X-rays, experiments confirmed it (Nobel Prize in Physics 1914), and William Henry and William Lawrence Bragg related the wavelength, the angle and the spacing of the atomic layers (Nobel Prize 1915).[^nobel]

Treat the atoms as lying on a family of parallel planes of spacing $d$, each reflecting a small part of the beam at equal angles. The ray reflected by the next plane down travels $d\sin\theta$ further on the way in and $d\sin\theta$ on the way out (red in the figure). All planes reflect in phase when[^up46]

$$2d\sin\theta = n\lambda, \qquad n = 1, 2, 3, \dots$$

This is **Bragg's law**, with $\theta$ the glancing angle measured from the planes; the beam is deflected by $2\theta$. Since $\sin\theta \le 1$, a reflection requires $\lambda \le 2d$: visible light, thousands of times longer than atomic spacings, gives no Bragg reflections, whereas X-rays do.

![[bragg-law-crystal-planes.svg]]

### Bio: X-ray diffraction by protein crystals

In X-ray crystallography a protein is crystallized and the crystal is placed in an X-ray beam; the electrons of its atoms scatter the X-rays into a pattern of discrete spots, whose intensities are measured and turned into an electron-density map, in which an atomic model is built.[^berg] Each spot is a Bragg reflection from one family of planes. Spots far from the beam (large $\theta$) come from closely spaced planes, $d = \lambda/(2\sin\theta)$, and the smallest spacing measured, $d_{\min}$, is the **resolution**: the smaller the number, the finer the detail.[^berg][^pdb] At $\lambda = 1.0$ Å (12.4 keV, example value), a 3 Å reflection appears at $2\theta = 19.2°$ and a 2 Å reflection at 29.0° (computed below). X-ray diffraction also stands behind the double helix: Watson and Crick built their model of [[DNA]] using the diffraction results of Franklin, Wilkins and co-workers.[^watson]

## Deeper (L2)

### The single-slit intensity is a sinc²

Add the wavelets from every point $x \in [-a/2, a/2]$ of the slit. Toward $\theta$ the wavelet from $x$ is ahead in phase by $kx\sin\theta$, with $k = 2\pi/\lambda$ ([[Complex Number|complex amplitudes]]):

$$E(\theta) \propto \int_{-a/2}^{a/2} e^{ikx\sin\theta}\,dx = a\,\frac{\sin\beta}{\beta}, \qquad \beta = \frac{\pi a\sin\theta}{\lambda}, \qquad I(\theta) = I_0\left(\frac{\sin\beta}{\beta}\right)^2.$$

University Physics obtains the same intensity with phasors.[^up4] Zeros at $\beta = m\pi$ recover $a\sin\theta = m\lambda$. The side maxima lie near, not at, $\beta = (m + \tfrac12)\pi$ and are weak: 4.7 %, 1.7 % and 0.8 % of the central peak (computed below), so nearly all the light goes into the central maximum.

### Gratings: interference times diffraction

For $N$ slits of width $a$ at spacing $d$, summing the $N$ slit amplitudes (a geometric series of phasors) gives

$$I(\theta) = I_0\left(\frac{\sin\beta}{\beta}\right)^2\left(\frac{\sin N\gamma}{N\sin\gamma}\right)^2, \qquad \gamma = \frac{\pi d\sin\theta}{\lambda},$$
with $I_0$ the intensity of the central peak, $N^2$ times that of one slit.

- **Sharp lines.** The second factor peaks at $\gamma = m\pi$ ($d\sin\theta = m\lambda$); its nearest zeros are at $N\gamma = Nm\pi \pm \pi$, so each line has a half-width $\Delta(\sin\theta) = \lambda/(Nd)$: more slits, sharper lines.
- **Resolving power.** Wavelengths $\lambda$ and $\lambda + \Delta\lambda$ are just separated in order $m$ when the peak of one falls on the first zero of the other (Rayleigh's criterion again): $m\Delta\lambda/d = \lambda/(Nd)$, so $R = \lambda/\Delta\lambda = mN$.
- **Missing orders.** The single-slit envelope can cancel a principal maximum: with $d = 3a$, orders $m = \pm3, \pm6, \dots$ fall on single-slit zeros and vanish.

### Bragg's law in practice

- **Orders and planes.** $2d\sin\theta = n\lambda$ equals $2(d/n)\sin\theta = \lambda$: the $n$-th order from planes of spacing $d$ cannot be told apart from the first order of planes of spacing $d/n$, so each reflection can be labelled by a single family of planes (indexing is covered in [[X-ray Crystallography]]).
- **Energy and wavelength.** From $E = hc/\lambda$ with the exact SI constants,[^nist] $\lambda\,[\text{Å}] = 12.398/E\,[\text{keV}]$: 1.54 Å is 8.05 keV, 1.0 Å is 12.4 keV ([[Photon]]).
- **Geometry sets resolution.** A flat detector of radius $R$ at distance $L$ from the crystal records scattering angles up to $2\theta_{\max} = \arctan(R/L)$, hence spacings down to $d_{\min} = \lambda/(2\sin\theta_{\max})$. A shorter wavelength or a closer detector reaches finer resolution (worked example).

## Advanced (L3)

**A diffraction pattern is a Fourier transform.** The L2 integral is the Fourier transform of the aperture. For a transmission $t(x)$ and $q = 2\pi\sin\theta/\lambda$, $E(q) \propto \int t(x)\,e^{iqx}\,dx = \hat t(q)$. A slit gives a sinc; a grating is a slit convolved with a comb of $N$ points, so its pattern is the product of their transforms (the convolution theorem), the formula above; a circular aperture gives the Airy pattern. In three dimensions, the X-ray amplitude scattered along the scattering vector $\mathbf{s}$, of length $|\mathbf{s}| = 2\sin\theta/\lambda = 1/d$, is the Fourier transform of the electron density $\rho(\mathbf{r})$.

**A crystal samples the transform.** Repeating the unit cell on a lattice makes the transform zero except at the points of the **reciprocal lattice**, one per family of planes $(hkl)$, at distance $1/d_{hkl}$ from the origin. There it equals the **structure factor**, and the density is the corresponding Fourier series:

$$F_{hkl} = \int_{\text{cell}} \rho(\mathbf{r})\,e^{2\pi i(hx + ky + lz)}\,d\mathbf{r}, \qquad \rho(x, y, z) = \frac{1}{V}\sum_{hkl} F_{hkl}\,e^{-2\pi i(hx + ky + lz)},$$

with $x, y, z$ fractional coordinates in the cell of volume $V$. Evaluating $\rho$ on a grid is a three-dimensional discrete Fourier transform ([[Fast Fourier Transform]]). Exercise 3 shows the one-dimensional version: a periodic density diffracts only at multiples of the number of cells.

**The phase problem.** The detector measures $I_{hkl} \propto |F_{hkl}|^2$; the phase of each $F_{hkl}$ is lost, just as a camera loses the phase of light ([[Interference]]). Yet the phases carry most of the structure: amplitudes of one structure combined with phases of another give a map of the second (Exercise 3). Two consequences follow from the transform: a translated molecule changes only the phases, and because $\rho$ is real, $F_{-h-k-l} = F_{hkl}^*$, so $I_{-h-k-l} = I_{hkl}$ (Friedel's law) and only half the reflections are independent. Recovering the phases is the central problem of [[X-ray Crystallography]].

**How many reflections?** Reciprocal-lattice points fill reciprocal space with density $V$, so the number inside the sphere of radius $1/d_{\min}$ is $N(d_{\min}) \approx \frac{4\pi}{3}\,V/d_{\min}^3$. For an invented 50 × 60 × 70 Å cell this is about 33 000 reflections at 3 Å, 110 000 at 2 Å and 261 000 at 1.5 Å, half of them independent (computed with the formula): halving $d_{\min}$ multiplies the measurements eightfold.

## Mathematical representation

- Single slit of width $a$: minima $a\sin\theta = m\lambda$, $m \neq 0$; $I = I_0(\sin\beta/\beta)^2$, $\beta = \pi a\sin\theta/\lambda$. Grating of $N$ slits at spacing $d$: maxima $d\sin\theta = m\lambda$; line half-width $\Delta(\sin\theta) = \lambda/(Nd)$; resolving power $\lambda/\Delta\lambda = mN$.
- Circular aperture of diameter $D$: first minimum $\sin\theta_1 = 1.22\,\lambda/D$ ($1.22 = 3.8317/\pi$, from the first zero of the Bessel function $J_1$); microscope $d_{\min} = 0.61\,\lambda/\mathrm{NA}$. Bragg: $2d\sin\theta = n\lambda$; deflection $2\theta$; resolution $d_{\min} = \lambda/(2\sin\theta_{\max})$; $|\mathbf{s}| = 1/d$.
- Fourier: $E(q) \propto \hat t(q)$; $I_{hkl} \propto |F_{hkl}|^2$; $N(d_{\min}) \approx \frac{4\pi}{3}V/d_{\min}^3$.

## Computational representation

Intensities depend on one dimensionless variable, $u = a\sin\theta/\lambda$ for a slit; angles come from inverting a sine, and a reflection that cannot exist shows up as an `asin` argument above 1. The plot is logarithmic so that the zeros at integer $u$ and the weak side maxima show.

```python
import math

H, C, E = 6.62607015e-34, 299792458, 1.602176634e-19   # Planck, speed of light, elementary charge (exact SI)


def single_slit(u: float) -> float:
    """I/I0 = (sin b / b)^2 with b = pi u, u = a sin(theta) / wavelength."""
    b = math.pi * u
    return 1.0 if b == 0 else (math.sin(b) / b) ** 2


def log_plot(f, lo: float = -4.0, hi: float = 4.0, cols: int = 81, rows: int = 6, decades: int = 3) -> None:
    """Plot log10 f(u) over [-decades, 0], half a decade per row; zeros of f show as gaps."""
    ys = [math.log10(max(f(lo + (hi - lo) * i / (cols - 1)), 1e-12)) for i in range(cols)]
    for r in range(rows, 0, -1):
        level = decades * ((r - 0.5) / rows - 1)
        print(f"{10 ** (decades * (r / rows - 1)):6.4f} |" + "".join("#" if y >= level else " " for y in ys).rstrip())
    print("       +" + "-" * cols + "\n       " + "".join(f"{t:<10}" for t in range(-4, 5)).rstrip() + "  a sin(theta) / lambda")


def bragg_theta(d: float, wavelength: float, n: int = 1) -> float | None:
    """Glancing angle (degrees) with 2 d sin(theta) = n lambda; None if no reflection exists."""
    s = n * wavelength / (2 * d)
    return math.degrees(math.asin(s)) if s <= 1 else None


log_plot(single_slit)
side = [max((single_slit(m + i / 1000), m + i / 1000) for i in range(1000)) for m in (1, 2, 3)]
print("side maxima (I/I0, u):", [(round(i, 4), round(u, 3)) for i, u in side])
d_grating = 1e6 / 600                                  # 600 lines/mm, spacing in nm
for lam in (450, 650):                                 # example wavelengths, nm
    orders = range(1, int(d_grating // lam) + 1)
    print(f"grating, {lam} nm: orders at", [round(math.degrees(math.asin(m * lam / d_grating)), 1) for m in orders], "deg")
print(f"0.61 lambda / NA with NA 1.4: {0.61 * 0.40 / 1.4:.3f} um at 400 nm, {0.61 * 0.52 / 1.4:.3f} um at 520 nm")
print("X-ray energy (keV):", {lam: round(H * C / (lam * 1e-10) / E / 1e3, 2) for lam in (1.54, 1.0)})   # example, A
for d in (3, 2):
    t = bragg_theta(d, 1.0)
    print(f"d = {d} A at 1.0 A: theta = {t:.2f} deg, 2 theta = {2 * t:.2f} deg")
```

```text
1.0000 |                                    #########
0.3162 |                                  #############
0.1000 |                                 ###############
0.0316 |                       ######   #################   ######
0.0100 |    ####     ######   ######## ################### ########   ######     ####
0.0032 |  #######   ######## ######### ################### ######### ########   #######
       +---------------------------------------------------------------------------------
       -4        -3        -2        -1        0         1         2         3         4  a sin(theta) / lambda
side maxima (I/I0, u): [(0.0472, 1.43), (0.0165, 2.459), (0.0083, 3.471)]
grating, 450 nm: orders at [15.7, 32.7, 54.1] deg
grating, 650 nm: orders at [23.0, 51.3] deg
0.61 lambda / NA with NA 1.4: 0.174 um at 400 nm, 0.227 um at 520 nm
X-ray energy (keV): {1.54: 8.05, 1.0: 12.4}
d = 3 A at 1.0 A: theta = 9.59 deg, 2 theta = 19.19 deg
d = 2 A at 1.0 A: theta = 14.48 deg, 2 theta = 28.96 deg
```

## Worked example

> [!example] What resolution does a detector position give? (example values)
> X-rays of $\lambda = 1.0$ Å, a flat detector of radius 100 mm centred on the direct beam.
> 1. Detector 200 mm from the crystal: its edge is at $2\theta_{\max} = \arctan(100/200) = 26.57°$, so $\theta_{\max} = 13.28°$ and, by Bragg, $d_{\min} = \lambda/(2\sin\theta_{\max}) = 1.0/(2 \times 0.2297) = 2.18$ Å.
> 2. A 2.0 Å reflection has $\sin\theta = 1.0/4.0$, $\theta = 14.48°$, $2\theta = 28.96°$, and lands at $r = 200\tan 28.96° = 110.7$ mm: just off the detector.
> 3. At 150 mm: $2\theta_{\max} = 33.69°$ and $d_{\min} = 1.73$ Å. Moving the detector closer records finer spacings, with the spots closer together on the detector.

## Common misconceptions

> [!warning] "$a\sin\theta = m\lambda$ gives bright fringes, like $d\sin\theta = m\lambda$"
> For a single slit it gives the **dark** fringes, with $a$ the slit width; for a grating the same form gives the **bright** lines, with $d$ the spacing between slits. Same equation, opposite meaning.

> [!warning] "In Bragg's law $\theta$ is measured from the normal, or is the deflection"
> $\theta$ is the glancing angle between the beam and the planes; the beam turns by $2\theta$. Diffraction data are often plotted against $2\theta$: halve it before applying $2d\sin\theta = n\lambda$.

> [!warning] "A diffraction pattern is a magnified picture of the molecule"
> Each spot comes from a family of planes through the whole crystal, and the pattern is the squared modulus of the Fourier transform of the electron density. The phases needed to rebuild an image are not recorded (L3).

## Exercises

> [!question] Exercise 1 (L1)
> Light of 500 nm passes through a slit 2.0 µm wide. Find the angles of the first three dark fringes. What happens with a slit 0.5 µm wide?

> [!success]- Solution
> $\sin\theta = m\lambda/a = m/4$: 14.5°, 30.0°, 48.6°; the central maximum spans 29°. With $a = 0.5$ µm, $\sin\theta = 1$ already for $m = 1$: there is no dark fringe at all and the central maximum fills the whole half-space. An opening of the order of the wavelength spreads light in every direction.

> [!question] Exercise 2 (L1)
> Planes in an invented crystal are 4.0 Å apart. Find the Bragg angles for X-rays of 1.54 Å, and the highest order. Can 500 nm light be Bragg-reflected by these planes?

> [!success]- Solution
> $\sin\theta = n \times 1.54/8.0$: $n = 1$ gives 11.1°, $n = 2$ gives 22.6°, then 35.3°, 50.4° and 74.3° for $n = 5$; $n = 6$ would need $\sin\theta = 1.16$, so 5 is the highest order. For 500 nm, even $n = 1$ needs $\sin\theta = 5000/8 = 625$: impossible, since $\lambda > 2d$.

> [!question] Exercise 3 (L3, Python)
> Model a one-dimensional crystal as an invented 16-point electron density repeated 6 times. (a) Show that its discrete Fourier transform is non-zero only at multiples of 6. (b) Show that shifting the motif leaves the intensities unchanged. (c) Combine the amplitudes of motif A with the phases of a different motif B, transform back, and see which structure appears.

> [!success]- Solution
> ```python
> import cmath
> import math
>
> def dft(f: list, sign: int = -1) -> list[complex]:
>     """Discrete Fourier transform, written out (O(n^2)); sign=+1 gives the inverse without the 1/n factor."""
>     n = len(f)
>     return [sum(v * cmath.exp(sign * 2j * math.pi * k * x / n) for x, v in enumerate(f)) for k in range(n)]
>
> motif_a = [0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0]       # invented: atoms at x = 2, 6, 11
> motif_b = [0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0]       # invented: atoms at x = 4, 9, 14
> crystal = motif_a * 6                                             # 6 unit cells in a row
> print("nonzero intensities at k =", [k for k, F in enumerate(dft(crystal)) if abs(F) ** 2 > 1e-9][:6], "...")
> shifted = motif_a[-3:] + motif_a[:-3]                             # same molecule, moved by 3 grid steps
> print("shifted motif, same intensities:", all(abs(abs(x) - abs(y)) < 1e-9 for x, y in zip(dft(motif_a), dft(shifted))))
> hybrid = [abs(fa) * cmath.exp(1j * cmath.phase(fb)) for fa, fb in zip(dft(motif_a), dft(motif_b))]
> rho = [(v / len(hybrid)).real for v in dft(hybrid, sign=+1)]
> print("amplitudes of A + phases of B: peaks at", sorted(sorted(range(16), key=lambda x: -rho[x])[:3]))
> print("density at A's atoms", [round(rho[x], 2) for x in (2, 6, 11)], "at B's atoms", [round(rho[x], 2) for x in (4, 9, 14)])
> # nonzero intensities at k = [0, 6, 12, 18, 24, 30] ...
> # shifted motif, same intensities: True
> # amplitudes of A + phases of B: peaks at [4, 9, 14]
> # density at A's atoms [0.39, 0.26, -0.28] at B's atoms [0.68, 2.02, 0.68]
> ```
>
> (a) The repeats interfere constructively only at the reciprocal-lattice points $k = 6h$: these are the Bragg reflections, and their values sample the transform of one cell. (b) Translation multiplies each $F$ by a phase factor, invisible in $|F|^2$. (c) The hybrid map shows B's atoms, with B's relative weights, not A's: the phases, which the detector does not record, decide where the atoms are. This is why phasing is the hard step of [[X-ray Crystallography]].

## Mastery checklist

- [ ] 1 Recognized: I can define diffraction and state the single-slit, grating, circular-aperture and Bragg conditions.
- [ ] 2 Understood: I can derive the single-slit minima and Bragg's law from path differences, and explain why the pattern widens as the opening shrinks.
- [ ] 3 Practiced: I can compute fringe and grating angles, Rayleigh distances and Bragg angles by hand and in Python, including the sinc² pattern.
- [ ] 4 Applied: I can read the resolution of a PDB crystal structure as a Bragg spacing and relate it to wavelength and detector geometry.
- [ ] 5 Explained: I can teach diffraction as a Fourier transform, why a crystal samples it at reciprocal-lattice points, and why lost phases make structure determination hard.

## References

[^up4]: [[University Physics (OpenStax)]], Volume 3, ch. 4 "Diffraction" (spreading of waves through openings analysed with Huygens's principle; single-slit minima $D\sin\theta = m\lambda$ with $D$ the slit width; single-slit intensity $I_0(\sin\beta/\beta)^2$ by phasors; diffraction gratings, maxima at $d\sin\theta = m\lambda$, dispersion of light into its wavelengths).
[^up45]: [[University Physics (OpenStax)]], Volume 3, §4.5 "Circular Apertures and Resolution" (first minimum of a circular aperture at $\theta = 1.22\lambda/D$; Rayleigh criterion: two images just resolvable when the centre of one pattern lies on the first minimum of the other).
[^up46]: [[University Physics (OpenStax)]], Volume 3, §4.6 "X-Ray Diffraction" (X-ray wavelengths of order $10^{-8}$ to $10^{-12}$ m, atoms about 0.1 nm; Bragg's law $2d\sin\theta = m\lambda$ for planes of spacing $d$, $\theta$ measured from the planes).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of microscopy (wavelengths of visible light, 0.4 to 0.7 µm; resolution limit $0.61\lambda/(n\sin\theta)$; just under 0.2 µm with violet light of 0.4 µm and a numerical aperture of 1.4).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of protein structure determination (X-ray crystallography and NMR as the sources of atomic structures; protein crystal, X-ray beam, scattering by electrons, diffraction spots, electron-density map, model and resolution).
[^pdb]: [[RCSB Protein Data Bank]], structure entries on RCSB.org (experimental method and resolution of each entry).
[^nobel]: [[NobelPrize.org]], Nobel Prize in Physics 1914 (Max von Laue, "for his discovery of the diffraction of X-rays by crystals"; his 1912 idea confirmed by experiment) and 1915 (William Henry Bragg and William Lawrence Bragg, "for their services in the analysis of crystal structure by means of X-rays").
[^watson]: [[Watson 1953 - Molecular Structure of Nucleic Acids]], *Nature* (the model was built using X-ray diffraction results of Franklin, Wilkins and co-workers, acknowledged in the paper).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA 2022 values, exact in the SI: $h = 6.626\,070\,15 \times 10^{-34}$ J s, $c = 299\,792\,458$ m s⁻¹, $e = 1.602\,176\,634 \times 10^{-19}$ C.
