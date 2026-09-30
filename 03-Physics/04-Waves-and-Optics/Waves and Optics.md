---
aliases:
  - Ondes et optique
  - Optics
tags:
  - type/moc
  - domain/physics
  - level/L1
  - level/L2
prerequisites:
  - "[[Mechanics]]"
  - "[[Electromagnetism]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
---

# Waves and Optics

> [!abstract]
> Light as a wave and as photons: interference and diffraction, lenses and microscopes, the diffraction limit and the fluorescence, confocal and super-resolution methods that work around it, and the photon noise that limits every optical measurement.

## Why it matters for bioinformatics

- **Many data sets are images.** Microscopy, spatial transcriptomics, high-content screens and the cluster images of fluorescence-based [[Next-Generation Sequencing|sequencers]] are optical measurements: resolution, fluorescence and photon counting set what the data can show.
- **Diffraction solves structures.** The same physics that limits a microscope ([[Diffraction]]) is how [[X-ray Crystallography]] reads atomic positions.
- **Photon counts are Poisson.** [[Shot Noise]] is a physical origin of the [[Poisson Distribution]] in imaging and fluorescence data.
- **Spectroscopy needs light.** [[Spectroscopy]], [[Beer-Lambert Law|absorbance]] and [[Fluorescence]] ([[Physical Chemistry]]) start from the [[Photon]] and the [[Electromagnetic Spectrum]].

## Before you start

- [[Mechanics]]: [[Harmonic Oscillator]].
- [[Electromagnetism]] Stage 1: [[Electric Field]], [[Magnetic Field]].
- [[Cell Biology]]: [[Microscopy]] (what each kind of microscope shows); this MOC adds the physics behind it.
- [[Physical Chemistry]]: [[Fluorescence]] before item 12.
- [[Calculus]]; [[Complex Number]] (optional, for phases); [[Fast Fourier Transform|Fourier Transform]] (optional, for image formation at L2).

## Learning path

> [!tip] What to skip compared with a full physics licence
> Sound and acoustics, the Doppler effect, standing waves on strings, mirrors and multi-lens optical design, aberration theory, thin-film calculations, holography, relativity, quantum optics and the quantum mechanics chapters beyond the photon's energy.

### Stage 1 - Foundations (L1)

1. [[Wave]] (L1): describe amplitude, wavelength, frequency, speed and phase, and add waves by superposition.
2. [[Electromagnetic Wave]] (L1): describe light as oscillating electric and magnetic fields travelling at $c = \lambda \nu$.
3. [[Electromagnetic Spectrum]] (L1): order radio, microwave, infrared, visible, ultraviolet and X-ray radiation by wavelength and energy. Bio: NMR (radio), infrared spectroscopy, UV absorbance at 260 and 280 nm, visible fluorescence, X-ray diffraction.
4. [[Photon]] (L1): use $E = h\nu = hc/\lambda$ and wave-particle duality. Bio: why UV damages DNA and blue light excites GFP.
5. [[Refraction]] (L1): apply Snell's law, refractive index and total internal reflection. Bio: immersion objectives, TIRF microscopy.
6. [[Lens]] (L1): use the thin-lens equation, focal length and magnification. Bio: objective and eyepiece of a light microscope; magnification versus resolution.
7. [[Interference]] (L1): predict constructive and destructive interference from path differences. Bio: phase-contrast and DIC microscopy.
8. [[Diffraction]] (L1): describe diffraction by slits, gratings and apertures, and Bragg's law for crystals. Bio: X-ray diffraction by protein crystals.

### Stage 2 - Core (L2)

9. [[Diffraction Limit]] (L2): compute the Abbe and Rayleigh resolution from wavelength and numerical aperture (about $\lambda / 2\,\mathrm{NA}$, roughly 200 nm for visible light) and read a point-spread function. Bio: organelles are resolved, single proteins are not.
10. [[Polarization]] (L2): describe linear and circular polarization and polarizers. Bio: the basis of [[Circular Dichroism]] and fluorescence anisotropy.
11. [[Laser]] (L2): explain stimulated emission, coherence and monochromatic output. Bio: excitation sources of confocal microscopes, [[Flow Cytometry|flow cytometers]], sequencers and optical tweezers.
12. [[Fluorescence Microscopy]] (L2): explain excitation and emission filters, fluorophores and fluorescent proteins, and multichannel imaging. Bio: GFP fusions, fluorescence in situ hybridization.
13. [[Confocal Microscopy]] (L2): explain optical sectioning with a pinhole and laser scanning. Bio: three-dimensional imaging of cells and tissues.
14. [[Super-Resolution Microscopy]] (L2): explain how STED, PALM and STORM beat the diffraction limit; localization precision improves as $1/\sqrt{N}$ with the number of photons. Bio: nanoscale organization of proteins in cells.
15. [[Shot Noise]] (L2): model photon counts as Poisson and the signal-to-noise ratio as $\sqrt{N}$. Bio: limits of low-light imaging and of fluorescence-based measurements.

## Uses from other domains

- [[Spectroscopy]], [[Beer-Lambert Law]], [[Fluorescence]], [[Förster Resonance Energy Transfer]], [[Circular Dichroism]] ([[Physical Chemistry]]).
- [[X-ray Crystallography]], [[Cryo-Electron Microscopy]], [[Optical Tweezers]] ([[Biophysics]]).
- [[Poisson Distribution]] ([[Probability]]): the statistics of [[Shot Noise]].
- [[Cell Biology]]: microscopy is how cell structures were discovered and are still measured.

## Reference courses

No course source note yet for this subdomain; the book below covers it.

## Reference books

- [[University Physics (OpenStax)]]: Volume 1 (waves), Volume 3 Unit 1 "Optics" (nature of light, geometric optics, interference, diffraction) and the photon part of Unit 2 "Modern Physics".[^up]
- [[Physical Biology of the Cell (Phillips)]]: ch. 18 "Light and Life".[^pboc]

## Lab projects

No Lab project implements optics directly.

## References

Scope: waves and optics are part of the calculus-based physics sequence (waves in Volume 1, optics and photons in Volume 3 of University Physics).[^up] This MOC keeps the optics of microscopy and spectroscopy and adds the light-matter topics of a physical biology course.[^pboc]

[^up]: [[University Physics (OpenStax)]], Volume 1 (mechanics, sound, oscillations, waves), Volume 3 Unit 1 "Optics" and Unit 2 "Modern Physics".
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed., ch. 18 "Light and Life".
