---
aliases:
  - Magnetic Force on a Moving Charge
  - Cyclotron Motion
  - Cyclotron Frequency
  - Force de Lorentz
tags:
  - type/concept
  - domain/physics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Magnetic Field]]"
  - "[[Electric Field]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Vector]]"
related:
  - "[[Mass Spectrometry]]"
  - "[[Electric Potential]]"
  - "[[Kinetic Energy]]"
  - "[[Electromagnetic Induction]]"
  - "[[Fast Fourier Transform]]"
  - "[[Tandem Mass Spectrometry]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Aebersold 2003 - Mass Spectrometry-Based Proteomics]]"
---

# Lorentz Force

> [!abstract]
> A magnetic field pushes a moving charge sideways, at right angles to its motion, so the charge circles at a radius and a frequency set by its mass-to-charge ratio: this is how mass spectrometers tell ions apart.

## Definition

The **Lorentz force** on a charge $q$ moving with velocity $\vec v$ through an electric field $\vec E$ and a magnetic field $\vec B$ is

$$\vec F = q\left(\vec E + \vec v \times \vec B\right).$$

Its magnetic part, $q\,\vec v \times \vec B$, has magnitude $qvB\sin\theta$ ($\theta$ the angle between $\vec v$ and $\vec B$) and is perpendicular to both. Some textbooks reserve the name for the magnetic part alone.[^up11]

## Why it matters

- **Mass spectrometry measures $m/z$.** A mass spectrometer is an ion source, a mass analyser that measures the mass-to-charge ratio of the ions, and a detector.[^aebersold] In magnetic analysers the Lorentz force is the analyser: the radius or the frequency of an ion's circle gives its $m/z$ ([[Mass Spectrometry]]).[^up11]
- **Why spectra are plotted against $m/z$.** The trajectory depends on $m$ and $q$ only through $m/q$ (derived below): a peptide of 1000 Da carrying two charges lands exactly where one of 500 Da carrying one charge does. Every proteomics tool that matches spectra to peptides starts from this ([[Tandem Mass Spectrometry]], [[Mass Spectrum]]).
- **Mass from a frequency.** Fourier-transform ion cyclotron resonance (FT-ICR) analysers turn the cyclotron frequency into $m/z$ (L3).[^aebersold]

## Core (L1)

**Direction.** $\vec v \times \vec B$ follows the right-hand rule: fingers along $\vec v$, curl toward $\vec B$, thumb gives the force on a positive charge; a negative charge feels the opposite force ([[Vector]]). The force vanishes for a charge at rest or moving parallel to $\vec B$, and is largest, $qvB$, for motion perpendicular to it.[^up11]

**No work.** The magnetic force is always perpendicular to the velocity, so its power $\vec F \cdot \vec v = 0$: it changes the direction of motion, never the speed or the [[Kinetic Energy]]. Speeding ions up is the job of an electric field ([[Electric Potential]]).[^up11]

**Circular motion.** For $\vec v \perp \vec B$ uniform, a force of constant magnitude $qvB$ always perpendicular to $\vec v$ is a centripetal force. Newton's second law ([[Newton's Laws of Motion]]) with centripetal acceleration $v^2/r$:

$$qvB = \frac{mv^2}{r} \quad\Longrightarrow\quad r = \frac{mv}{qB}, \qquad T = \frac{2\pi r}{v} = \frac{2\pi m}{qB}, \qquad f = \frac{1}{T} = \frac{qB}{2\pi m}.$$

The **cyclotron frequency** $f$ does not depend on the speed: a faster ion runs a proportionally larger circle in the same time. If $\vec v$ has a component along $\vec B$, that component is unaffected and the path is a helix.[^up11]

![[ion-circular-motion-magnetic-sector.svg]]

## Deeper (L2)

**Accelerate, then bend: the magnetic sector.** An ion of mass $m$ and charge $q$ starting at rest and accelerated through a potential difference $V$ gains $qV = \frac12 mv^2$ ([[Electric Potential]]), so $v = \sqrt{2qV/m}$. In the field,

$$r = \frac{mv}{qB} = \frac{1}{B}\sqrt{\frac{2Vm}{q}} \quad\Longleftrightarrow\quad \frac{m}{q} = \frac{B^2 r^2}{2V}.$$

Measuring where the ion lands (at $2r$ from the entrance) gives $m/q$; this is the mass spectrometer of physics textbooks.[^up11] Because $r \propto \sqrt{m/q}$, two ions of nearby mass land close together: resolving them needs a narrow beam and a stable field.

**Units of $m/z$.** Mass spectrometry writes $m$ in daltons and $z$ as the number of elementary charges, so $m/z$ in Da per charge. With the atomic mass constant $m_u = 1\ \text{Da} = 1.660\,539\,068\,92(52) \times 10^{-27}$ kg and $e = 1.602\,176\,634 \times 10^{-19}$ C,[^nist] $m/q = (m/z)\,m_u/e$.

**Velocity selector.** In crossed fields, with $\vec E$ perpendicular to $\vec B$ and both perpendicular to $\vec v$, the electric and magnetic forces cancel when $qE = qvB$: only ions with $v = E/B$ pass straight through, whatever their mass or charge. Placed before a magnetic sector, it fixes $v$ so that $r = (m/q)\,v/B$ is proportional to $m/q$.[^up11]

## Advanced (L3)

**Fourier-transform ion cyclotron resonance (FT-ICR).** Since $f = qB/(2\pi m)$ is independent of speed, a cloud of ions held in a strong uniform field circles at frequencies that encode their $m/z$ values. The orbiting ions induce a small oscillating signal in detection plates ([[Electromagnetic Induction]]); its [[Fast Fourier Transform|Fourier transform]] splits the record into frequencies, hence into $m/z$, for all ions at once. FT-ICR instruments are among the mass analysers used in proteomics.[^aebersold] Frequency resolution grows with the length of the record (about $1/T_\text{obs}$, Exercise 5): the longer the ions keep circling coherently, the finer the $m/z$ differences that can be separated. Mass analysers, ionization and peptide identification belong to [[Mass Spectrometry]] and [[Proteomics]]; this note supplies only the force.

## Mathematical representation

$$\vec F = q(\vec E + \vec v \times \vec B), \qquad r = \frac{mv_\perp}{|q|B}, \qquad f_c = \frac{|q|B}{2\pi m}, \qquad \frac{m}{z} = \frac{e\,B^2 r^2}{2\,V\,m_u}$$

$\vec F$: force (N); $q = ze$: charge (C), $z$ the charge number; $\vec v$: velocity (m/s) and $v_\perp$ its component perpendicular to $\vec B$; $\vec E$: electric field (V/m); $\vec B$: magnetic field (T); $m$: mass (kg); $r$: radius (m); $f_c$: cyclotron frequency (Hz); $V$: accelerating voltage (V); $m/z$: in Da per elementary charge; $m_u$: atomic mass constant (kg). **Units.** $mv/(qB)$: (kg·m/s)/(C·T) with $1\ \text{T} = 1\ \text{kg}\,\text{C}^{-1}\,\text{s}^{-1}$ gives metres; $qB/m$ gives s⁻¹.

**Only $m/q$ matters.** Every expression above, once $v$ is fixed by acceleration ($v = \sqrt{2qV/m}$), depends on $m$ and $q$ through $m/q$ alone. In Cartesian components with $\vec B = B\hat z$, $\ddot x = (qB/m)\,\dot y$ and $\ddot y = -(qB/m)\,\dot x$: the equations of motion themselves contain only $q/m$.

## Computational representation

```python
import math

E = 1.602176634e-19        # C, elementary charge (exact)
M_U = 1.66053906892e-27    # kg, atomic mass constant, 1 Da (CODATA 2022)


def sector_radius(mass_da: float, z: int, b: float, volts: float) -> float:
    """Radius (m) of an ion (mass in Da, charge z e) accelerated from rest through volts, in field b (T)."""
    m, q = mass_da * M_U, z * E
    v = math.sqrt(2 * q * volts / m)       # q V = m v^2 / 2
    return m * v / (q * b)                 # q v B = m v^2 / r


def cyclotron_frequency(mass_da: float, z: int, b: float) -> float:
    """Cyclotron frequency (Hz), f = q B / (2 pi m): independent of speed and radius."""
    return z * E * b / (2 * math.pi * mass_da * M_U)


def mz_from_sector(b: float, r: float, volts: float) -> float:
    """m/z (Da per elementary charge) from a measured radius: m/q = B^2 r^2 / (2 V)."""
    return E * (b * r) ** 2 / (2 * volts * M_U)


B, V = 0.500, 3000.0                       # illustrative sector settings
for mass, z in ((500, 1), (1000, 2), (502, 1)):
    r = sector_radius(mass, z, B, V)
    print(f"mass {mass} Da, z = {z}: r = {100 * r:.3f} cm -> m/z = {mz_from_sector(B, r, V):.1f}")
for mass, z in ((500, 1), (1000, 2), (1000, 1)):
    print(f"mass {mass} Da, z = {z}, 7 T: f = {cyclotron_frequency(mass, z, 7.0) / 1e3:.2f} kHz")
```

```text
mass 500 Da, z = 1: r = 35.266 cm -> m/z = 500.0
mass 1000 Da, z = 2: r = 35.266 cm -> m/z = 500.0
mass 502 Da, z = 1: r = 35.337 cm -> m/z = 502.0
mass 500 Da, z = 1, 7 T: f = 214.99 kHz
mass 1000 Da, z = 2, 7 T: f = 214.99 kHz
mass 1000 Da, z = 1, 7 T: f = 107.49 kHz
```

The 1000 Da, 2+ ion is indistinguishable from the 500 Da, 1+ ion in both analysers: the instrument sees $m/z$, and deciding $z$ is a separate step of spectrum interpretation.

## Worked example

> [!example] Two singly charged ions in a magnetic sector (settings illustrative)
> Ions of $m/z$ 500 and 502, accelerated through $V = 3.00$ kV, enter $B = 0.500$ T.
> 1. **Mass**: $m = 500 \times 1.6605 \times 10^{-27} = 8.303 \times 10^{-25}$ kg.
> 2. **Speed**: $v = \sqrt{2qV/m} = \sqrt{2 \times 1.602 \times 10^{-19} \times 3000 / 8.303 \times 10^{-25}} = 3.40 \times 10^4$ m/s.
> 3. **Radius**: $r = mv/(qB) = 8.303 \times 10^{-25} \times 3.40 \times 10^4/(1.602 \times 10^{-19} \times 0.500) = 0.3527$ m.
> 4. **Neighbour**: $r \propto \sqrt{m/z}$, so $r_{502} = 0.3527\sqrt{502/500} = 0.3534$ m. The landing points, at $2r$, differ by $2 \times 0.71$ mm $= 1.4$ mm.
> 5. **Check**: $m/z = eB^2r^2/(2Vm_u)$ with $r = 0.3527$ m returns 500.

## Common misconceptions

> [!warning] "A magnetic field speeds up or slows down charges"
> The magnetic force is perpendicular to the velocity and does no work. It bends paths; electric fields change speeds.

> [!warning] "A mass spectrometer measures mass"
> It measures $m/z$. An ion of 1000 Da with charge 2+ appears at $m/z$ 500, exactly where a 500 Da ion with charge 1+ appears.

> [!warning] "Faster ions circle faster"
> They circle on larger radii in the same period: the cyclotron frequency $qB/(2\pi m)$ does not depend on speed (until relativistic speeds, far from mass-spectrometry conditions).

> [!warning] "All charges curve the same way"
> The sign of $q$ flips the force: in the same field, cations and electrons circle in opposite senses.

## Exercises

> [!question] Exercise 1 (L1)
> A singly charged cation moves at $\vec v = 2.0 \times 10^5\,\hat x$ m/s in $\vec B = 0.50\,\hat z$ T. Give $\vec F$. What changes for an electron?

> [!success]- Solution
> $\vec F = q\,\vec v \times \vec B = e\,vB\,(\hat x \times \hat z) = -e\,vB\,\hat y$, since $\hat x \times \hat z = -\hat y$. Magnitude $1.602 \times 10^{-19} \times 2.0 \times 10^5 \times 0.50 = 1.6 \times 10^{-14}$ N, along $-\hat y$. An electron at the same velocity feels $+1.6 \times 10^{-14}$ N along $+\hat y$.

> [!question] Exercise 2 (L1)
> Show that a uniform magnetic field cannot change an ion's kinetic energy.

> [!success]- Solution
> $dK/dt = \vec F \cdot \vec v = q(\vec v \times \vec B) \cdot \vec v = 0$, because $\vec v \times \vec B$ is perpendicular to $\vec v$. So $K = \frac12 mv^2$ and the speed stay constant.

> [!question] Exercise 3 (L2)
> A velocity selector has $E = 1.0 \times 10^5$ V/m and $B = 0.10$ T. Which ions pass undeflected? Does it matter whether they carry 1 or 2 charges?

> [!success]- Solution
> $qE = qvB \Rightarrow v = E/B = 1.0 \times 10^6$ m/s. The charge cancels: any ion at that speed passes, whatever $m$ and $q$.

> [!question] Exercise 4 (L2)
> An electron with 1.0 eV of kinetic energy moves perpendicular to the Earth's field, $5 \times 10^{-5}$ T. Find its speed, radius and cyclotron frequency ($m_e = 9.109 \times 10^{-31}$ kg[^nist]).

> [!success]- Solution
> $v = \sqrt{2 \times 1.602 \times 10^{-19}/9.109 \times 10^{-31}} = 5.93 \times 10^5$ m/s. $r = m_e v/(eB) = 9.109 \times 10^{-31} \times 5.93 \times 10^5/(1.602 \times 10^{-19} \times 5 \times 10^{-5}) = 0.067$ m. $f = eB/(2\pi m_e) = 1.40 \times 10^6$ Hz. Even a weak field bends a light, slow particle on a centimetre scale.

> [!question] Exercise 5 (L3, Python)
> In a 7.0 T FT-ICR magnet, compute the cyclotron frequencies of ions at $m/z$ 1000.0 and 1000.1, their difference, and the minimum recording time to separate them if the frequency resolution of a record of length $T_\text{obs}$ is about $1/T_\text{obs}$.

> [!success]- Solution
> ```python
> import math
>
> E, M_U = 1.602176634e-19, 1.66053906892e-27
>
>
> def cyclotron_frequency(mz: float, b: float) -> float:
>     """f (Hz) for an ion of given m/z (Da per elementary charge) in field b (T)."""
>     return E * b / (2 * math.pi * mz * M_U)
>
>
> f1, f2 = cyclotron_frequency(1000.0, 7.0), cyclotron_frequency(1000.1, 7.0)
> print(f"f = {f1:.1f} Hz and {f2:.1f} Hz, difference {f1 - f2:.2f} Hz")
> print(f"record for at least {1 / (f1 - f2):.3f} s")
> ```
> Output: `f = 107492.8 Hz and 107482.1 Hz, difference 10.75 Hz`, then `record for at least 0.093 s`. Since $f \propto 1/(m/z)$, $\Delta f/f = \Delta(m/z)/(m/z) = 10^{-4}$. A tenth of a second of coherent signal separates them; a longer record resolves finer differences ([[Fast Fourier Transform]]).

## Mastery checklist

- [ ] 1 Recognized: I can write $\vec F = q(\vec E + \vec v \times \vec B)$ and say that a magnetic field bends but does not accelerate charges.
- [ ] 2 Understood: I can derive $r = mv/(qB)$ and $f = qB/(2\pi m)$ and explain why analysers measure $m/z$, not $m$.
- [ ] 3 Practiced: I can compute forces with the right-hand rule, radii, frequencies and $m/z$ from sector data, by hand and in Python.
- [ ] 4 Applied: I converted a real spectrum's peaks between $m/z$ and neutral mass for different charge states ([[Mass Spectrum]]).
- [ ] 5 Explained: I can teach how a magnetic sector and an FT-ICR analyser turn the same force into a radius and into a frequency.

## References

[^up11]: [[University Physics (OpenStax)]], Volume 2, ch. 11 "Magnetic Forces and Fields", §11.3 "Motion of a Charged Particle in a Magnetic Field" (circular and helical motion, radius and period) and §11.7 "Applications of Magnetic Forces and Fields" (mass spectrometer, cyclotron); force on a moving charge and its direction in the same chapter.
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA 2022: atomic mass constant $m_u = 1.660\,539\,068\,92(52) \times 10^{-27}$ kg; elementary charge $e = 1.602\,176\,634 \times 10^{-19}$ C (exact); electron mass $9.109 \times 10^{-31}$ kg (rounded).
[^aebersold]: [[Aebersold 2003 - Mass Spectrometry-Based Proteomics]], *Nature* 422:198-207 (parts of a mass spectrometer; mass analysers used in proteomics, including FT-ICR).
