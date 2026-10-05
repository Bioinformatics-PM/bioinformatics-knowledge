---
aliases:
  - EM Spectrum
  - Spectrum of Electromagnetic Radiation
  - Spectre électromagnétique
tags:
  - type/concept
  - domain/physics
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Electromagnetic Wave]]"
  - "[[Logarithm]]"
related:
  - "[[Photon]]"
  - "[[Spectroscopy]]"
  - "[[Beer-Lambert Law]]"
  - "[[Fluorescence]]"
  - "[[Nuclear Magnetic Resonance Spectroscopy]]"
  - "[[X-ray Crystallography]]"
  - "[[Diffraction]]"
  - "[[Microscopy]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[FPbase]]"
  - "[[Chemistry 2e (OpenStax)]]"
---

# Electromagnetic Spectrum

> [!abstract]
> Radio waves, microwaves, infrared, visible light, ultraviolet and X-rays are one kind of wave at different wavelengths; going from radio to X-rays the wavelength shrinks by more than ten orders of magnitude while frequency and photon energy grow, and each range probes a different part of a biological molecule.

## Definition

The **electromagnetic spectrum** is the whole range of [[Electromagnetic Wave|electromagnetic waves]], ordered by wavelength $\lambda$ or, equivalently, by frequency $\nu = c/\lambda$ or photon energy $E = h\nu$. Its named bands, from long to short wavelength, are radio, microwave, infrared (IR), visible, ultraviolet (UV), X-ray and gamma rays; they differ only in wavelength range.[^up165]

## Why it matters

- **Choosing a technique is choosing a band.** NMR uses radio waves, IR spectroscopy bond vibrations, UV absorbance the electrons of bases and aromatic rings, fluorescence microscopy visible light, crystallography X-rays ([[Spectroscopy]], [[X-ray Crystallography]]).
- **Every community has its unit.** NMR speaks MHz, IR spectroscopists cm⁻¹, biochemists nm, crystallographers Å and keV. Comparing or merging their data starts with conversion code like the one below.
- **Data columns are spectral positions.** A260 and A280 in a quantification report ([[Beer-Lambert Law]]), the excitation and emission wavelengths of an imaging channel, the X-ray energy of a diffraction experiment: each places a measurement on this axis.

## Core (L1)

Because $\nu = c/\lambda$ and $E = h\nu = hc/\lambda$ ([[Photon]]), ordering by **decreasing wavelength** is ordering by **increasing frequency** and **increasing photon energy**. Radio photons are the least energetic, X-ray photons the most.

![[electromagnetic-spectrum-log-scale.svg]]

### The bands used in molecular biology

| Band | Example in a biology lab | $\lambda$ | $\nu$ (Hz) | Photon energy (eV) | What it probes |
|---|---|---|---:|---:|---|
| Radio | NMR spectrometer, 600 MHz | 0.50 m | $6.0 \times 10^{8}$ | $2.5 \times 10^{-6}$ | nuclear spins in a strong magnet[^orgchem][^berg] |
| Microwave | (example) | 1 cm | $3.0 \times 10^{10}$ | $1.2 \times 10^{-4}$ | |
| Infrared | IR band at 1700 cm⁻¹ (example) | 5.9 µm | $5.1 \times 10^{13}$ | 0.21 | bond vibrations: IR spectroscopy identifies functional groups[^orgchem] |
| Visible | EGFP excitation and emission, 488 and 507 nm[^fpbase] | 0.4 to 0.7 µm[^alberts] | $6.1 \times 10^{14}$ | 2.5 | fluorescence; light microscopy |
| Ultraviolet | absorbance of nucleic acids at 260 nm, of proteins at 280 nm[^berg][^leh] | 260 to 280 nm | $1.1 \times 10^{15}$ | 4.4 to 4.8 | electrons of bases and aromatic side chains |
| X-ray | diffraction by crystals | about 0.1 nm[^up46] | $3.0 \times 10^{18}$ | $1.2 \times 10^{4}$ | positions of atoms |

(Frequencies and energies computed below with CODATA constants.[^nist]) X-ray wavelengths span roughly $10^{-8}$ to $10^{-12}$ m, and atoms are about 0.1 nm across, which is why X-rays can locate atoms in molecules.[^up46]

Two different rules match a band to a probe:

1. **Energy.** A photon is absorbed only if its energy matches a gap between states of the molecule. Radio photons match nuclear spin states in a magnet, IR photons vibrations, UV and visible photons electronic states ([[Spectroscopy]] works out this ladder).
2. **Size.** To image or diffract from a structure, the wavelength must not be much larger than the structure ([[Diffraction]]). Visible light (0.4 to 0.7 µm) resolves organelles but not molecules ([[Diffraction Limit]]); X-rays, at about 0.1 nm, match the spacing of atoms.[^up46]

## Deeper (L2)

**Units and quick conversions.** UV-vis and microscopy use wavelengths in nm, crystallography in Å ($10^{-10}$ m) and photon energies in keV, NMR frequencies in MHz, IR the wavenumber $\tilde\nu = 1/\lambda$ in cm⁻¹, photochemistry kJ mol⁻¹. From the exact constants $h$, $c$ and $e$,[^nist] three products are worth memorizing (computed below):

$$E\,[\text{eV}] \times \lambda\,[\text{nm}] = 1239.84, \qquad E\,[\text{keV}] \times \lambda\,[\text{Å}] = 12.398, \qquad \tilde\nu\,[\text{cm}^{-1}] = \frac{10^7}{\lambda\,[\text{nm}]}.$$

**A logarithmic axis.** The bands in daily lab use cover more than nine orders of magnitude in wavelength, from 0.1 nm to 0.5 m, so the spectrum is drawn on a $\log_{10}\lambda$ axis ([[Logarithm]]). On that axis the visible range, 400 to 700 nm, is 0.24 decade wide: less than a factor of 2 in wavelength, about 2 % of the 13 decades drawn in the figure. Band limits are conventions: nothing physical changes at 400 nm, and books draw the UV/X-ray and microwave/radio boundaries differently.

## Mathematical representation

- $\lambda\nu = c$, $\tilde\nu = 1/\lambda$, $E = h\nu = hc/\lambda = hc\,\tilde\nu$, molar energy $E_m = N_A\,E$, with $h$ the Planck constant, $c$ the speed of light, $N_A$ the Avogadro constant.[^nist]
- The spectrum is the half-line $\lambda \in (0, \infty)$, mapped one-to-one and order-reversing onto $\nu$ and $E$. Bands are adjacent intervals of $\log_{10}\lambda$.

## Computational representation

A spectral position is stored as one number plus a unit; a converter normalizes everything to the vacuum wavelength in metres, then derives the other scales.

```python
import math

H = 6.62607015e-34        # Planck constant, J s (exact)
C = 299_792_458           # speed of light, m/s (exact)
EV = 1.602176634e-19      # 1 eV in J = elementary charge in C (exact)
N_A = 6.02214076e23       # Avogadro constant, 1/mol (exact)

TO_WAVELENGTH = {         # unit -> function returning the vacuum wavelength in m
    "m": lambda v: v, "nm": lambda v: v * 1e-9, "A": lambda v: v * 1e-10,
    "Hz": lambda v: C / v, "MHz": lambda v: C / (v * 1e6),
    "cm-1": lambda v: 1 / (v * 100), "eV": lambda v: H * C / (v * EV), "keV": lambda v: H * C / (v * 1e3 * EV),
}


def describe(value: float, unit: str) -> dict[str, float]:
    """Wavelength (m), frequency (Hz), wavenumber (cm-1) and photon energy (eV, kJ/mol) of one EM wave."""
    lam = TO_WAVELENGTH[unit](value)
    energy = H * C / lam
    return {"m": lam, "Hz": C / lam, "cm-1": 1 / (lam * 100), "eV": energy / EV, "kJ/mol": energy * N_A / 1e3}


probes = [("NMR spectrometer", 600, "MHz"), ("IR band (example)", 1700, "cm-1"),
          ("EGFP emission", 507, "nm"), ("EGFP excitation", 488, "nm"),
          ("protein absorbance", 280, "nm"), ("nucleic acid absorbance", 260, "nm"),
          ("X-ray beam (example)", 12.4, "keV")]
print(f"{'probe':24} {'lambda (m)':>10} {'nu (Hz)':>10} {'E (eV)':>10}")
for name, value, unit in sorted(probes, key=lambda p: -describe(p[1], p[2])["m"]):
    d = describe(value, unit)
    print(f"{name:24} {d['m']:10.3g} {d['Hz']:10.3g} {d['eV']:10.3g}")
```

```text
probe                    lambda (m)    nu (Hz)     E (eV)
NMR spectrometer                0.5      6e+08   2.48e-06
IR band (example)          5.88e-06    5.1e+13      0.211
EGFP emission              5.07e-07   5.91e+14       2.45
EGFP excitation            4.88e-07   6.14e+14       2.54
protein absorbance          2.8e-07   1.07e+15       4.43
nucleic acid absorbance     2.6e-07   1.15e+15       4.77
X-ray beam (example)          1e-10      3e+18   1.24e+04
```

## Worked example

> [!example] Placing an IR band and an X-ray beam (example values)
> 1. **IR band at 1700 cm⁻¹.** $\lambda = 1/\tilde\nu = 1/(1700 \text{ cm}^{-1}) = 5.88 \times 10^{-4}$ cm $= 5.88$ µm: infrared. $\nu = c/\lambda = 5.10 \times 10^{13}$ Hz. $E = 1239.84/5882 = 0.211$ eV, or 20.3 kJ/mol.
> 2. **X-ray beam of 12.4 keV.** $\lambda = 12.398/12.4 = 1.00$ Å $= 0.100$ nm.
> 3. **Compare and interpret.** The X-ray photon carries $12\,400/0.211 \approx 59\,000$ times the energy of the IR photon, and its wavelength is $59\,000$ times shorter. The IR photon has the energy of a bond vibration; the X-ray photon's wavelength matches interatomic distances, so it is used for diffraction rather than for its energy.

## Common misconceptions

> [!warning] "Radio waves, light and X-rays are different kinds of things"
> They are the same electromagnetic wave at different wavelengths;[^up165] the different names reflect how they are produced, detected and absorbed.

> [!warning] "Visible light is a big part of the spectrum"
> On a logarithmic axis it is a sliver, less than a factor of 2 in wavelength. Most of the spectrum used in the lab (NMR, IR, X-rays) is invisible.

## Exercises

> [!question] Exercise 1 (L1)
> Order by increasing wavelength, then by increasing photon energy: a 260 nm UV lamp, a 600 MHz NMR signal, 0.1 nm X-rays, 10 µm infrared, 507 nm green emission.

> [!success]- Solution
> Wavelength: X-ray (0.1 nm) < UV (260 nm) < green (507 nm) < IR (10 µm) < NMR (0.5 m). Photon energy is the reverse order, since $E = hc/\lambda$.

> [!question] Exercise 2 (L2)
> Without a computer, convert an IR band at 1650 cm⁻¹ to µm and eV, and an X-ray wavelength of 1.0 Å to keV.

> [!success]- Solution
> $\lambda = 10^7/1650 = 6061$ nm $= 6.06$ µm; $E = 1239.84/6061 = 0.205$ eV. $E = 12.398/1.0 = 12.4$ keV.

> [!question] Exercise 3 (L2, Python)
> A C–C single bond is 1.54 Å long.[^c2e] Using `describe` and `probes`, compute $\lambda/d$ for each probe. Which can diffract from features of that size?

> [!success]- Solution
> ```python
> cc = 1.54e-10
> for name, value, unit in probes:
>     print(f"{name:24} lambda/d(C-C) = {describe(value, unit)['m'] / cc:.3g}")
> # NMR 3.24e+09, IR 3.82e+04, EGFP emission 3.29e+03, EGFP excitation 3.17e+03,
> # protein absorbance 1.82e+03, nucleic acid absorbance 1.69e+03, X-ray 0.649 (one line each)
> ```
>
> Only X-rays have $\lambda$ comparable to a bond length; UV light is still about 1700 times too long. NMR and IR do give atomic-level information, but through energy levels (spectroscopy), not through spatial diffraction.

## Mastery checklist

- [ ] 1 Recognized: I can list the bands from radio to X-ray in order of wavelength and of photon energy.
- [ ] 2 Understood: I can explain which band each technique uses (NMR, IR, UV absorbance, fluorescence, X-ray diffraction) and why, by energy or by size.
- [ ] 3 Practiced: I can convert between nm, Hz, cm⁻¹, eV, keV and kJ/mol by hand and with a converter, and place a range on a log axis.
- [ ] 4 Applied: I can read the spectral settings of a real instrument or data file (absorbance wavelengths, laser lines, NMR frequency, X-ray energy) and place them on the spectrum.
- [ ] 5 Explained: I can teach why the same physics underlies all bands, and why band limits are conventions.

## References

[^up165]: [[University Physics (OpenStax)]], Volume 2, §16.5 "The Electromagnetic Spectrum" (categories of EM waves by wavelength or frequency range).
[^up46]: [[University Physics (OpenStax)]], Volume 3, §4.6 "X-Ray Diffraction" (X-ray wavelengths of order $10^{-8}$ to $10^{-12}$ m; atoms about 0.1 nm in size).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA 2022 values, exact in the SI: $h = 6.626\,070\,15 \times 10^{-34}$ J s, $c = 299\,792\,458$ m s⁻¹, $e = 1.602\,176\,634 \times 10^{-19}$ C, $N_A = 6.022\,140\,76 \times 10^{23}$ mol⁻¹.
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of microscopy (wavelengths of visible light, 0.4 to 0.7 µm).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of exploring proteins and nucleic acids (UV absorbance of aromatic amino acids near 280 nm and of bases near 260 nm; NMR spectroscopy of proteins).
[^leh]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of light absorption (absorbance of tryptophan and tyrosine near 280 nm, of nucleotide bases near 260 nm) (chapter numbers not verified).
[^orgchem]: [[Organic Chemistry (OpenStax)]], treatment of structure determination (infrared spectroscopy of bond vibrations and functional groups; nuclear magnetic resonance with radio-frequency energy in a magnetic field) (chapter numbers not verified).
[^fpbase]: [[FPbase]], EGFP entry (excitation maximum 488 nm, emission maximum 507 nm).
[^c2e]: [[Chemistry 2e (OpenStax)]], ch. 7, §7.5 "Strengths of Ionic and Covalent Bonds" (average C–C bond length 1.54 Å).
