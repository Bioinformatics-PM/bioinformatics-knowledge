---
aliases:
  - Bacterium
  - Eubacteria
  - Gram Stain
  - Gram-Positive
  - Gram-Negative
  - Bactérie
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Prokaryote]]"
  - "[[Cell Membrane]]"
  - "[[Microorganism]]"
related:
  - "[[Archaea]]"
  - "[[Microscopy]]"
  - "[[Protein Targeting]]"
  - "[[GC Content]]"
  - "[[Antibiotic]]"
  - "[[Pathogen]]"
  - "[[Tree of Life]]"
projects: []
sources:
  - "[[Microbiology (OpenStax)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Woese 1977 - Phylogenetic Structure of the Prokaryotic Domain]]"
  - "[[Yu 2010 - PSORTb 3.0]]"
---

# Bacteria

> [!abstract]
> Bacteria are one of the two domains of prokaryotes: small cells without a nucleus, recognized by their shapes and, above all, by their envelope, which the Gram stain sorts into a thick-walled Gram-positive type and a Gram-negative type with a second, outer membrane.

## Definition

**Bacteria** form one of the three domains of life and one of the two prokaryotic ones, next to [[Archaea]]; Woese and Fox first separated the two by comparing ribosomal RNA.[^woese] A bacterium has the prokaryotic cell plan ([[Prokaryote]]); its membrane lipids are fatty acids linked to glycerol by ester bonds, and its cell wall, when present, is made of **peptidoglycan**.[^ospro][^os42]

## Why it matters

- **Envelope type is a parameter of annotation tools.** PSORTb, a predictor of where a prokaryotic protein ends up, uses five localization sites for Gram-negative bacteria and four for Gram-positive bacteria and for archaea.[^psortb] Running it with the wrong envelope type yields compartments that do not exist in the organism (Computational representation; [[Protein Targeting]]).
- **Shape and Gram reaction describe an isolate.** "Gram-negative rods" or "Gram-positive cocci in clusters" summarizes what a light microscope shows, before any sequencing ([[Microscopy]]).[^m24][^m33]
- **The envelope is a drug target.** Antibiotics such as penicillin act on the synthesis of the peptidoglycan wall, a structure human cells do not have,[^micro] the starting point of [[Antibiotic]] and [[Antimicrobial Resistance]].

## Core (L1)

### Shapes and arrangements

| Shape[^m33] | Description | Arrangement (how cells stay together after division) |
|---|---|---|
| Coccus | sphere | diplococci (pairs), streptococci (chains), staphylococci (clusters), tetrads, sarcinae (cubes of 8) |
| Bacillus | rod | single, pairs or chains |
| Coccobacillus | short rod | |
| Vibrio | curved rod | |
| Spirillum | rigid spiral | |
| Spirochete | flexible spiral | |

### The Gram stain

Developed by Hans Christian Gram in 1884, it is a **differential stain** in four steps:[^m24]

1. **Crystal violet** (primary stain) colors every cell purple.
2. **Iodine** (mordant) forms a complex with crystal violet inside the cell.
3. **Alcohol** (decolorizer) washes the complex out of Gram-negative cells only.
4. **Safranin** (counterstain) colors the now colorless Gram-negative cells pink or red.

Gram-positive cells end **purple**, Gram-negative cells **pink**. The difference comes from the envelope.

### Two envelopes

![[gram-positive-negative-envelope.svg]]

| Feature | Gram-positive | Gram-negative |
|---|---|---|
| Peptidoglycan | thick, many layers | thin layer |
| Teichoic acids | present | absent |
| Outer membrane | absent | present, with lipopolysaccharide (LPS) and porins |
| Periplasm | none in the classic sense (no outer membrane) | space between the two membranes, holding the peptidoglycan |

Peptidoglycan is a mesh of sugar chains, alternating *N*-acetylglucosamine (NAG) and *N*-acetylmuramic acid (NAM), cross-linked by short peptides; it gives the wall its strength and the cell its shape.[^m33] The thick Gram-positive wall retains the crystal violet-iodine complex; in Gram-negative cells, alcohol disrupts the outer membrane and the thin peptidoglycan cannot hold the dye.[^m24][^m33]

## Deeper (L2)

- **Lipopolysaccharide.** The LPS of the outer membrane is also called endotoxin; it is a defining component of the Gram-negative envelope.[^m33]
- **Exceptions to the two types.** Mycoplasmas have no cell wall at all, and mycobacteria have waxy walls rich in mycolic acids, which resist the Gram stain and are revealed by the acid-fast stain instead.[^m24][^micro4] "Gram-positive" and "Gram-negative" describe envelopes, not every bacterium.
- **Gram reaction and phylogeny.** The microbiology text organizes bacterial diversity into proteobacteria, other Gram-negative groups, Gram-positive bacteria (split into high G+C and low G+C groups, a genome property, see [[GC Content]]) and deeply branching bacteria.[^micro4] The Gram reaction tracks some lineages, but it is a phenotype, not a phylogeny ([[Tree of Life]]).
- **Archaea are different.** Archaea look like bacteria under the microscope, but have no peptidoglycan and use ether-linked isoprenoid lipids ([[Archaea]]).[^ospro]

## Advanced (L3)

- **Compartments as a classification scheme.** PSORTb 3.0 predicts, for Gram-negative bacteria, the cytoplasm, the cytoplasmic membrane, the periplasm, the outer membrane and the extracellular space; for Gram-positive bacteria and for archaea, the cytoplasm, the cytoplasmic membrane, the cell wall and the extracellular space. It also handles bacteria with atypical membrane or wall topologies.[^psortb] Each scheme is a direct translation of the envelope figure.
- **Inferring the envelope from a genome.** An uncultured bacterium known only from its genome ([[Microorganism#Why it matters]]) cannot be stained. Its envelope type has to be inferred from genes, for instance genes for the synthesis of lipopolysaccharide, which only an outer membrane needs (Exercise 3).

## Mathematical representation

Model a **coccus** as a sphere of radius $r$ and a **bacillus** as a cylinder of radius $r$ and length $\ell$ closed by two hemispherical caps (a spherocylinder):

$$S_{\text{sphere}} = 4\pi r^2,\quad V_{\text{sphere}} = \tfrac{4}{3}\pi r^3,\qquad S_{\text{rod}} = 2\pi r \ell + 4\pi r^2,\quad V_{\text{rod}} = \pi r^2 \ell + \tfrac{4}{3}\pi r^3 .$$

For the sphere $S/V = 3/r$. For the rod, $S/V$ decreases with $\ell$ but tends to $2/r$, not to 0, as $\ell \to \infty$: growing in length at constant width keeps the surface-to-volume ratio high, whereas a sphere's $S/V$ falls as $V^{-1/3}$, one physical consequence of shape for exchange with the environment ([[Cell#Why cells are small]]).

## Computational representation

```python
import math

# Localization categories of PSORTb 3.0, by envelope type
SITES = {
    "gram-negative": ["cytoplasm", "cytoplasmic membrane", "periplasm",
                      "outer membrane", "extracellular"],
    "gram-positive": ["cytoplasm", "cytoplasmic membrane", "cell wall", "extracellular"],
    "archaea": ["cytoplasm", "cytoplasmic membrane", "cell wall", "extracellular"],
}

def inconsistent(predictions: dict[str, str], envelope: str) -> dict[str, str]:
    """Predicted sites that do not exist in this envelope's scheme."""
    allowed = set(SITES[envelope])
    return {protein: site for protein, site in predictions.items() if site not in allowed}

# Invented predictions for proteins of a Gram-positive genome
PRED = {"prot_001": "cytoplasm", "prot_002": "periplasm",
        "prot_003": "cell wall", "prot_004": "outer membrane"}
print(inconsistent(PRED, "gram-positive"))
print(inconsistent(PRED, "gram-negative"))

def sphere(r: float) -> tuple[float, float]:
    return 4 * math.pi * r ** 2, 4 / 3 * math.pi * r ** 3

def rod(r: float, length: float) -> tuple[float, float]:
    """Cylinder of radius r and given length, closed by two hemispherical caps."""
    return (2 * math.pi * r * length + 4 * math.pi * r ** 2,
            math.pi * r ** 2 * length + 4 / 3 * math.pi * r ** 3)

s_rod, v_rod = rod(0.5, 2.0)                      # illustrative rod, in micrometres
r_eq = (3 * v_rod / (4 * math.pi)) ** (1 / 3)      # sphere of the same volume
s_sph, v_sph = sphere(r_eq)
print(round(v_rod, 3), round(r_eq, 3), round(s_rod / v_rod, 2), round(s_sph / v_sph, 2))
```

```text
{'prot_002': 'periplasm', 'prot_004': 'outer membrane'}
{'prot_003': 'cell wall'}
2.094 0.794 4.5 3.78
```

Two of four invented predictions are impossible for a Gram-positive cell; checked against the Gram-negative scheme, a different one fails. The illustrative rod (radius 0.5 µm, 2 µm long) has $S/V = 4.5$ µm⁻¹, against 3.78 µm⁻¹ for a sphere of the same volume.

## Worked example

> [!example] Reading two Gram stains
> 1. **Sample A**: purple spheres in grape-like clusters. Purple after decolorization means the crystal violet-iodine complex stayed: thick peptidoglycan, **Gram-positive cocci, staphylococcal arrangement**.[^m24][^m33]
> 2. **Sample B**: pink rods. The complex was washed out and safranin took over: outer membrane and thin wall, **Gram-negative bacilli**.
> 3. **Consequence for annotation**: for B, a predicted periplasmic or outer-membrane protein is plausible; for A, the same prediction signals a wrong envelope setting.[^psortb]
> 4. **Check**: the decolorizer is the only step that treats the two envelopes differently, so it is the step whose timing decides the result.

## Common misconceptions

> [!warning] "Gram-negative bacteria have no peptidoglycan"
> They have a thin layer, in the periplasm between the two membranes.[^m33]

> [!warning] "Every bacterium is either Gram-positive or Gram-negative"
> Mycoplasmas have no wall and mycobacteria need the acid-fast stain:[^m24][^micro4] the two categories cover typical envelopes, not all bacteria.

## Exercises

> [!question] Exercise 1 (L1)
> Name the shape and arrangement of: (a) spheres in chains; (b) comma-shaped cells; (c) flexible spirals.

> [!success]- Solution
> (a) Cocci, streptococcal arrangement. (b) Vibrios. (c) Spirochetes. A rigid spiral would be a spirillum.

> [!question] Exercise 2 (L2, Python)
> Using `rod` from the code above, compute $S/V$ for a rod of radius 0.5 µm and lengths 0, 1, 2, 4 and 8 µm. What is the limit, and what does it mean?

> [!success]- Solution
> ```python
> for length in (0.0, 1.0, 2.0, 4.0, 8.0):
>     s, v = rod(0.5, length)
>     print(length, round(s / v, 2))
> ```
> ```text
> 0.0 6.0
> 1.0 4.8
> 2.0 4.5
> 4.0 4.29
> 8.0 4.15
> ```
> Length 0 is a sphere ($3/r = 6$). The ratio decreases toward $2/r = 4$ µm⁻¹ but never below: a rod can grow in volume by elongation while keeping most of its relative surface.

> [!question] Exercise 3 (L3)
> A bacterial genome assembled from a soil metagenome has no cultured relative. How could you decide whether to annotate it with the Gram-negative or the Gram-positive scheme of a localization predictor, and what would a mistake produce?

> [!success]- Solution
> Look for genes that only a Gram-negative envelope needs: lipopolysaccharide synthesis and outer-membrane components such as porins ([[Gene Annotation]]). Their presence points to an outer membrane. With the wrong scheme, the predictor either cannot place outer-membrane and periplasmic proteins (Gram-positive scheme on a Gram-negative cell) or proposes compartments that do not exist (the reverse).[^psortb] Ambiguous cases (atypical envelopes) deserve a tool mode for atypical organisms and a note in the annotation.

## Mastery checklist

- [ ] 1 Recognized: I can name bacterial shapes and arrangements and the colors of the Gram stain.
- [ ] 2 Understood: I can draw both envelopes and explain the Gram stain from them.
- [ ] 3 Practiced: I can compute surface-to-volume ratios for cocci and rods and check localization predictions against an envelope scheme.
- [ ] 4 Applied: I annotated the predicted localizations of a real bacterial proteome with the correct envelope setting.
- [ ] 5 Explained: I can explain the exceptions (no wall, acid-fast) and why the Gram reaction is a phenotype, not a phylogeny.

## References

[^woese]: [[Woese 1977 - Phylogenetic Structure of the Prokaryotic Domain]], *PNAS* 74:5088-5090.
[^os42]: [[Biology 2e (OpenStax)]], section 4.2 "Prokaryotic Cells" (cell wall made of peptidoglycan in bacteria).
[^ospro]: [[Biology 2e (OpenStax)]], chapter "Prokaryotes: Bacteria and Archaea" (structure of prokaryotes: bacterial and archaeal membrane lipids and cell walls).
[^m24]: [[Microbiology (OpenStax)]], section 2.4 "Staining Microscopic Specimens" (the Gram stain, its steps and its interpretation; the acid-fast stain and mycolic acids).
[^m33]: [[Microbiology (OpenStax)]], section 3.3 "Unique Characteristics of Prokaryotic Cells" (cell shapes and arrangements; peptidoglycan; Gram-positive and Gram-negative cell walls, teichoic acids, outer membrane, lipopolysaccharide, periplasm, porins).
[^micro4]: [[Microbiology (OpenStax)]], ch. 4 "Prokaryotic Diversity" (the major bacterial groups, high and low G+C Gram-positive bacteria, mycoplasmas without cell walls, mycobacteria).
[^micro]: [[Microbiology (OpenStax)]] (antimicrobial drugs acting on cell wall synthesis; selective toxicity).
[^psortb]: [[Yu 2010 - PSORTb 3.0]], *Bioinformatics* 26(13):1608-1615.
