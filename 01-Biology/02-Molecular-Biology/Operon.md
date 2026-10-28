---
aliases:
  - lac Operon
  - trp Operon
  - Opéron
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Transcription]]"
  - "[[Promoter]]"
  - "[[Gene Regulation]]"
  - "[[Bacteria]]"
related:
  - "[[Transcription Factor]]"
  - "[[Allosteric Regulation]]"
  - "[[Feedback Loop]]"
  - "[[Bistability]]"
  - "[[Hill Function]]"
  - "[[Two-State Model]]"
  - "[[Boolean Network]]"
  - "[[Gene Regulatory Network]]"
  - "[[Gene Finding]]"
projects: []
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Microbiology (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Jacob 1961 - Genetic Regulatory Mechanisms in the Synthesis of Proteins]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[MIT 8.591J - Systems Biology]]"
  - "[[Ozbudak 2004 - Multistability in the Lactose Utilization Network of Escherichia coli]]"
---

# Operon

> [!abstract]
> An operon is a cluster of bacterial genes transcribed together from one promoter into one mRNA, and switched on or off as a unit by a regulatory protein bound next to that promoter. The lac and trp operons are the textbook models of how a cell senses a nutrient and adjusts transcription.

## Definition

An **operon** is a set of adjacent genes transcribed from a single promoter into one **polycistronic** mRNA, together with the regulatory sequences, such as an **operator**, that control this transcription.[^os16][^micro11][^alberts] The model and its vocabulary (regulator gene, repressor, operator, inducer) come from François Jacob and Jacques Monod, who proposed that regulator genes make repressors acting on operators, with small molecules controlling the repressors.[^jacob]

## Why it matters

- **Bacterial annotation.** The genes of an operon are adjacent, on the same strand and co-transcribed: RNA-seq coverage runs continuously across them, and one start site precedes the first gene. A bacterial transcript can therefore span several coding sequences (Exercise 5, [[Gene Finding]]).
- **Function by context.** In both models, the genes of the operon serve one process, lactose use or tryptophan synthesis,[^os16] so membership in the same operon is a useful hint of related function for unannotated genes.
- **The first regulatory circuit.** Positive and negative control, induction and repression, cis and trans action were all defined on the lac and trp operons;[^jacob][^griffiths] the lac system is also a reference circuit for quantitative models of regulation and bistability (Frontier).[^phillips][^ozbudak]

## Core (L2)

![[lac-trp-operon-maps.svg]]

### The lac operon: an inducible operon

- **Genes.** *lacZ* encodes β-galactosidase, which cleaves lactose into glucose and galactose; *lacY* a permease that imports lactose; *lacA* a transacetylase. They are transcribed as one mRNA.[^os16][^alberts]
- **Negative control.** The repressor encoded by *lacI*, a gene with its own promoter, binds the operator, which overlaps the start of transcription, and blocks RNA polymerase. When lactose is present, its isomer **allolactose** binds the repressor and changes its shape: the repressor releases the operator (allosteric control).[^alberts][^griffiths]
- **Positive control.** When glucose is scarce, cyclic AMP (cAMP) accumulates; the **catabolite activator protein** (CAP) binds cAMP, then binds the CAP site upstream of the promoter and helps RNA polymerase bind.[^os16][^alberts]

| Glucose | Lactose | Repressor | CAP-cAMP | Transcription of *lacZYA* |
|---|---|---|---|---|
| present | absent | bound to the operator | not bound (low cAMP) | off |
| present | present | released by allolactose | not bound | low |
| absent | absent | bound to the operator | bound | off |
| absent | present | released by allolactose | bound | high |

(After [^os16].) The cell makes the lactose enzymes at a high rate only when lactose is available **and** its preferred sugar, glucose, is not.

### The trp operon: a repressible operon

The *trpEDCBA* genes encode the enzymes that synthesize tryptophan. The trp repressor is inactive alone; tryptophan, acting as a **corepressor**, binds it and allows it to bind the operator and shut off transcription. When tryptophan is abundant, the cell stops making the enzymes that make it: end-product repression.[^os16][^micro11]

| | Inducible (lac) | Repressible (trp) |
|---|---|---|
| Pathway | breaks down a nutrient | builds a product |
| Small molecule | inducer (allolactose) inactivates the repressor | corepressor (tryptophan) activates the repressor |
| Default state | off until the substrate appears | on until the product accumulates |

### Cis and trans: the genetic proof

Jacob and Monod's model rested on mutants analysed in **partial diploids**, cells carrying a second copy of the lac region on an F' factor.[^jacob][^griffiths]

- *lacI⁻* (no functional repressor): constitutive expression; **recessive**, because a wild-type *lacI* on the other copy makes a diffusible repressor that acts on both operators (trans).
- *lacO^c* (operator that no longer binds repressor): constitutive expression of the genes **on the same DNA molecule only**; it cannot be complemented (cis-dominant).
- *lacI^s* (repressor that cannot bind inducer): uninducible, and dominant over wild type, because it binds every operator.

## Advanced (L3)

### Attenuation of the trp operon

Repression is not the only control. Upstream of *trpE* lies a leader region whose RNA can fold into alternative hairpins; it also encodes a short leader peptide with two adjacent tryptophan codons. Because bacterial ribosomes translate the leader while it is being transcribed, the ribosome's progress decides the fold. With abundant tryptophan, the ribosome passes the tryptophan codons quickly and a terminator hairpin forms: transcription stops before the structural genes. With scarce tryptophan, the ribosome stalls at those codons, an alternative (antiterminator) hairpin forms, and transcription continues.[^alberts][^griffiths] Attenuation reads the supply of charged tRNA^Trp through translation, a mechanism impossible in eukaryotes, where transcription and translation are separated by the nuclear envelope ([[Gene Regulation#Core (L2)]]).

## Frontier (M1)

The lac permease brings in the inducer that induces more permease: a **positive feedback loop**. Ozbudak and colleagues followed reporters of lac expression in single *E. coli* cells over concentrations of glucose and of TMG, a non-metabolizable inducer. The network is **bistable** over a range of conditions: identical cells in the same medium are either induced or uninduced depending on their history (hysteresis), and the authors mapped the phase diagram with a mathematical model of uptake and regulation, then showed how the hysteretic switch can be turned into a graded response.[^ozbudak] Positive feedback and bistability are general mechanisms of cellular memory ([[Feedback Loop]], [[Bistability]]);[^mit8591] the one-variable model of the Mathematical representation, with cooperative self-activation, already shows two stable states and hysteresis. The experiments used a gratuitous inducer, so their quantitative conclusions do not transfer directly to growth on lactose.[^ozbudak]

## Mathematical representation

**Logic.** With $L$ = "lactose present" and $G$ = "glucose present", high lac transcription is the Boolean function $L \land \lnot G$ ([[Boolean Network]]).

**Repression.** Let $r$ be the concentration of active repressor and $K_d$ its dissociation constant from the operator. At equilibrium the operator is free with probability
$$P_{\text{free}} = \frac{1}{1 + r/K_d}.$$
If the inducer, at concentration $I$, inactivates repressor following a [[Hill Function]] with half-effect concentration $K_I$ and Hill coefficient $n$,[^mit8591] and $R$ is the total repressor,
$$r(I) = \frac{R}{1 + (I/K_I)^n}, \qquad E(I) = E_{\max}\, P_{\text{free}}\big(r(I)\big), \qquad \frac{E(\infty)}{E(0)} = 1 + \frac{R}{K_d}.$$
More repressor gives tighter repression but needs more inducer to lift it (Exercise 4). Statistical-mechanics versions of this [[Two-State Model]], which also count the repressor's nonspecific binding to the rest of the genome, are developed in *Physical Biology of the Cell*.[^phillips]

**Positive feedback.** Let $y$ be the permease level (proportional to the internal inducer), $a$ a basal induction set by the external inducer, and self-activation cooperative:
$$\frac{dy}{dt} = a + \beta \frac{y^n}{K^n + y^n} - y.$$
Steady states solve $a + \beta y^n/(K^n + y^n) = y$; with $n \ge 2$ there can be three, two stable and one unstable between them: bistability.

## Computational representation

The repression model, and a naive grouping of genes into candidate operons from an annotation (invented data):

```python
def lac_expression(inducer: float, r_tot: float = 50.0, k_d: float = 1.0,
                   k_i: float = 10.0, n: float = 2.0) -> float:
    """Relative transcription (1 = fully induced) of a repressed promoter.
    The operator is free with probability 1 / (1 + r / k_d); inducer inactivates repressor."""
    r_active = r_tot / (1 + (inducer / k_i) ** n)      # active repressor left (Hill function)
    return 1 / (1 + r_active / k_d)


GENES = [  # invented annotation: (name, start, end, strand), 1-based inclusive
    ("geneA", 100, 1300, "+"), ("geneB", 1315, 2400, "+"), ("geneC", 2390, 3100, "+"),
    ("geneD", 3500, 4200, "-"), ("geneE", 4230, 5000, "-"), ("geneF", 5600, 6300, "+")]


def candidate_operons(genes, max_gap: int = 50) -> list[list[str]]:
    """Group consecutive same-strand genes separated by at most max_gap bp (overlaps give negative gaps)."""
    groups = [[genes[0]]]
    for prev, cur in zip(genes, genes[1:]):
        gap = cur[1] - prev[2] - 1
        if cur[3] == prev[3] and gap <= max_gap:
            groups[-1].append(cur)
        else:
            groups.append([cur])
    return [[g[0] for g in grp] for grp in groups]


print([(i, round(lac_expression(i), 4)) for i in (0, 10, 30, 70, 200)])
print("induction ratio:", round(lac_expression(1e9) / lac_expression(0), 1))
print(candidate_operons(GENES))
```

```text
[(0, 0.0196), (10, 0.0385), (30, 0.1667), (70, 0.5), (200, 0.8891)]
induction ratio: 51.0
[['geneA', 'geneB', 'geneC'], ['geneD', 'geneE'], ['geneF']]
```

With $R/K_d = 50$ (invented), the uninduced promoter runs at 2% of its maximum and full induction gives the predicted ratio $1 + 50 = 51$. The grouping rule (same strand, small gap) is a heuristic, not an operon map; on the `-` strand the first transcribed gene is the rightmost one (geneE).

## Worked example

> [!example] Lactose arrives, glucose runs out
> A culture grows on glucose with some lactose present.
> 1. **Glucose present, lactose present.** Allolactose releases the repressor, but cAMP is low, CAP does not bind: weak transcription (row 2 of the table).
> 2. **Glucose exhausted.** cAMP rises, CAP-cAMP binds the CAP site: transcription becomes high (row 4). β-galactosidase and permease accumulate, and lactose consumption speeds up.
> 3. **Lactose exhausted.** Allolactose disappears, the repressor rebinds the operator: transcription stops (row 3), and the existing enzymes are diluted by growth and degradation.
> 4. **Reading the data.** In an RNA-seq time course, *lacZ*, *lacY* and *lacA* rise and fall together because they share one mRNA; the coverage is continuous across the three genes.

## Common misconceptions

> [!warning] "Lactose is the inducer"
> The inducer is allolactose, an isomer of lactose; lactose itself is the substrate.[^alberts] Laboratory inducers such as TMG are not metabolized at all,[^ozbudak] which is why they keep the system induced.

> [!warning] "Glucose represses the lac operon through the repressor"
> Glucose acts through the activator: low glucose raises cAMP, and CAP-cAMP stimulates transcription. The Lac repressor responds to allolactose only.[^os16]

## Exercises

> [!question] Exercise 1 (L2)
> Predict lac operon expression (off, low, high, constitutive) for: (a) wild type, glucose and lactose; (b) wild type, lactose only; (c) *lacI⁻*, glucose only; (d) *lacO^c*, no sugar; (e) *lacI^s*, lactose only; (f) a CAP-deficient mutant, lactose only.

> [!success]- Solution
> (a) Low: repressor released, but CAP inactive. (b) High. (c) Constitutive: no repressor; low CAP activity still limits the rate, so expression is at the "low" level. (d) Constitutive: the repressor cannot bind the operator; with no glucose, CAP-cAMP makes it high. (e) Off: the repressor cannot bind allolactose. (f) Low: derepressed but without activation.[^os16][^griffiths]

> [!question] Exercise 2 (L2)
> Partial diploids (chromosome / F'): (a) *I⁻ O⁺ Z⁺* / *I⁺ O⁺ Z⁻*; (b) *I⁺ O^c Z⁻* / *I⁺ O⁺ Z⁺*; (c) *I⁺ O^c Z⁺* / *I⁺ O⁺ Z⁻*. Is functional β-galactosidase made inducibly or constitutively?

> [!success]- Solution
> (a) Inducible: the F' *I⁺* repressor acts in trans on the chromosomal operator controlling *Z⁺*. (b) Inducible: the only functional *Z* is on the F', behind a normal operator; the constitutive operator drives a defective *Z⁻*. (c) Constitutive: *Z⁺* sits next to *O^c*, which no repressor can shut, whatever the other copy carries.[^griffiths]

> [!question] Exercise 3 (L2)
> Predict trp operon transcription: (a) high tryptophan, wild type; (b) low tryptophan, wild type; (c) high tryptophan, repressor gene deleted; (d) high tryptophan, repressor deleted and both leader Trp codons replaced by other codons.

> [!success]- Solution
> (a) Very low: active repressor plus attenuation. (b) High: inactive repressor, and the ribosome stalls at the Trp codons, so the antiterminator forms. (c) Reduced but not off: no repression, yet attenuation still terminates most transcripts. (d) Mostly terminated as in (c): without Trp codons the ribosome never stalls, so the leader always forms the terminator, even when tryptophan runs out; attenuation can no longer sense tryptophan.[^alberts][^griffiths]

> [!question] Exercise 4 (L3, Python)
> With `lac_expression`, compare $R = 50$ and $R = 100$ (invented units, $K_d = 1$): give the induction ratio and the inducer concentration giving half-maximal expression.

> [!success]- Solution
> Half expression needs $r(I) = K_d$, so $(I/K_I)^2 = R/K_d - 1$ and $I_{1/2} = K_I\sqrt{R/K_d - 1}$.
> ```python
> for r in (50.0, 100.0):
>     i_half = 10.0 * (r / 1.0 - 1) ** 0.5            # solves r(I) = K_d with K_I = 10, n = 2
>     print(r, round(1 / lac_expression(0, r_tot=r), 1), round(i_half, 2), round(lac_expression(i_half, r_tot=r), 3))
> ```
> ```text
> 50.0 51.0 70.0 0.5
> 100.0 101.0 99.5 0.5
> ```
> Doubling the repressor doubles the induction ratio ($1 + R/K_d$) but raises the inducer needed for half induction from 70 to 99.5: tight repression costs sensitivity.

> [!question] Exercise 5 (L3, Python)
> Run `candidate_operons(GENES, max_gap)` with gaps of 0, 20, 50 and 1000 bp. Explain each change and why no threshold proves an operon.

> [!success]- Solution
> ```python
> for gap in (0, 20, 50, 1000):
>     print(gap, candidate_operons(GENES, max_gap=gap))
> ```
> ```text
> 0 [['geneA'], ['geneB', 'geneC'], ['geneD'], ['geneE'], ['geneF']]
> 20 [['geneA', 'geneB', 'geneC'], ['geneD'], ['geneE'], ['geneF']]
> 50 [['geneA', 'geneB', 'geneC'], ['geneD', 'geneE'], ['geneF']]
> 1000 [['geneA', 'geneB', 'geneC'], ['geneD', 'geneE'], ['geneF']]
> ```
> At 0 only the overlapping pair B-C groups; 20 bp adds the A-B gap (14 bp); 50 bp adds D-E (29 bp). geneF never joins: it is on the other strand from its neighbour. Distance is only a proxy: two adjacent genes can have separate promoters, and a long intergenic region can sit inside an operon. Transcript data (continuous coverage, start sites) are needed to confirm.

## Mastery checklist

- [ ] 1 Recognized: I can define operon, operator, repressor, inducer, corepressor and polycistronic mRNA.
- [ ] 2 Understood: I can explain the lac operon in the four glucose and lactose conditions, the trp operon with attenuation, and cis versus trans mutations.
- [ ] 3 Practiced: I solved partial-diploid problems and coded the repression model and the operon grouping heuristic.
- [ ] 4 Applied: on a bacterial genome annotation with RNA-seq coverage, I identified co-transcribed gene clusters and checked them against coverage and start sites.
- [ ] 5 Explained: I can teach how the operon model founded gene regulation, its quantitative versions, and the limits of predicting operons from gene positions.

## References

[^os16]: [[Biology 2e (OpenStax)]], ch. 16 "Gene Expression" (prokaryotic gene regulation: the trp operon, the lac operon, catabolite activator protein, and the table of glucose and lactose conditions).
[^micro11]: [[Microbiology (OpenStax)]], ch. 11 "Mechanisms of Microbial Genetics" (gene regulation and operon theory in bacteria).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of bacterial gene regulatory proteins (Lac repressor and allolactose, CAP and cAMP, trp repressor) and of transcription attenuation.
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), treatment of the regulation of gene transcription in bacteria (lac mutants, partial diploids, cis and trans action, attenuation of the trp operon).
[^jacob]: [[Jacob 1961 - Genetic Regulatory Mechanisms in the Synthesis of Proteins]], *Journal of Molecular Biology* 3:318-356.
[^phillips]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), statistical-mechanics models of transcriptional regulation.
[^mit8591]: [[MIT 8.591J - Systems Biology]], lectures "Input Function, Michaelis-Menten Kinetics, and Cooperativity" and "Autoregulation, Feedback and Bistability".
[^ozbudak]: [[Ozbudak 2004 - Multistability in the Lactose Utilization Network of Escherichia coli]], *Nature* 427:737-740.
