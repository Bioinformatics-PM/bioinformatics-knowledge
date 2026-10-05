---
aliases:
  - Oxidation-Reduction Reaction
  - Redox
  - Oxidation State
  - Oxidation Number
  - Half-Reaction
  - Réaction d'oxydoréduction
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Electronegativity]]"
  - "[[Stoichiometry]]"
  - "[[Acid-Base Reaction]]"
related:
  - "[[Reduction Potential]]"
  - "[[Metabolism]]"
  - "[[Oxidative Phosphorylation]]"
  - "[[Point Mutation]]"
  - "[[DNA Repair]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
---

# Redox Reaction

> [!abstract]
> A redox reaction moves electrons from a reductant, which is oxidized, to an oxidant, which is reduced; oxidation states keep the books, and the same bookkeeping explains how NADH powers respiration and how an oxidized guanine becomes a mutation.

## Definition

**Oxidation** is the loss of electrons and **reduction** the gain of electrons; a **redox reaction** transfers electrons and changes the **oxidation number** (oxidation state) of at least one element. The species oxidized is the **reducing agent** (reductant), the species reduced the **oxidizing agent** (oxidant): the oxidant is itself reduced.[^c4] Mnemonic: OIL RIG, **o**xidation **i**s **l**oss, **r**eduction **i**s **g**ain.

## Why it matters

- **Energy metabolism is electron transfer.** Fuels are oxidized step by step; their electrons are loaded onto NAD⁺ and FAD and delivered to O₂ by the respiratory chain ([[Metabolism]], [[Oxidative Phosphorylation]]).[^berg]
- **Models must balance electrons.** A metabolic model that oxidizes a substrate without reducing a carrier creates hydrogen atoms from nothing ([[Stoichiometry#Exercises]]); the NAD⁺/NADH pool must be regenerated ([[Metabolism]]).
- **Oxidized bases are mutagenic.** Oxidation of guanine produces a base that mispairs, leaving a characteristic substitution in sequencing data ([[Point Mutation]]).[^griffiths]

## Core (L1)

### Oxidation states

An element in its elemental form is 0 and a monatomic ion has its charge; oxygen is −2 (−1 in peroxides such as H₂O₂), hydrogen +1 with nonmetals (−1 in metal hydrides), fluorine −1; the states of a species add up to its charge.[^c4] In MnO₄⁻, $x + 4(-2) = -1$ gives Mn = +7. In $\mathrm{Zn + Cu^{2+} \to Zn^{2+} + Cu}$, zinc goes from 0 to +2 (oxidized: the reductant) and copper from +2 to 0 (reduced: the oxidant).[^c4]

Oxidation states are bookkeeping, not real charges, but they rank carbon compounds by how oxidized they are, two electrons per step:

$$\underset{-4}{\mathrm{CH_4}} \to \underset{-2}{\mathrm{CH_3OH}} \to \underset{0}{\mathrm{HCHO}} \to \underset{+2}{\mathrm{HCOO^-}} \to \underset{+4}{\mathrm{CO_2}}$$

This ladder (alcohol, aldehyde, acid) is the backbone of [[Organic Redox Reaction|organic redox chemistry]].

### Balancing with half-reactions

Write the oxidation and the reduction separately, then, in acidic water:[^half]

1. balance atoms other than O and H;
2. balance O with H₂O, then H with H⁺;
3. balance charge with electrons;
4. multiply so that both halves exchange the same number of electrons, add, and cancel.

In basic solution, add OH⁻ to both sides to turn H⁺ into water. The method is the hand version of the charge-balanced linear system of [[Stoichiometry#Deeper (L2)]].

### Bio: NAD⁺/NADH and oxidative damage

NAD⁺ accepts two electrons and one proton, together a hydride ion, on its nicotinamide ring: $\mathrm{NAD^+ + H^+ + 2\,e^- \to NADH}$.[^berg] Lactate dehydrogenase uses NADH to reduce pyruvate, $\mathrm{pyruvate + NADH + H^+ \to lactate + NAD^+}$,[^berg] whose carbons go from an average +2/3 to 0: two electrons for three carbons (computed below).

Partial reduction of O₂ yields toxic species such as superoxide and peroxide (reactive oxygen species),[^berg] whose oxygen sits between 0 and −2. They oxidize biomolecules, including DNA bases: guanine oxidized to **8-oxoguanine** pairs with adenine, so after replication a G:C pair becomes T:A, a transversion.[^griffiths] Damaged bases are removed by base excision repair ([[DNA Repair]]).[^alberts]

## Deeper (L2)

### Reduction potentials and free energy

The standard reduction potential $E^{\circ\prime}$ of a couple measures its tendency to accept electrons at pH 7; electrons flow spontaneously toward the more positive couple, and $\Delta G^{\circ\prime} = -nF\Delta E^{\circ\prime}$ for $n$ electrons, $F$ being the Faraday constant ([[Reduction Potential]], [[Gibbs Free Energy]]).[^berg]

![[redox-tower-nadh-oxygen.svg]]

With $E^{\circ\prime} = -0.32$ V for NAD⁺/NADH, $-0.19$ V for pyruvate/lactate and $+0.82$ V for O₂/H₂O,[^berg] NADH → O₂ releases about 220 kJ/mol and NADH → pyruvate about 25 kJ/mol (computed below). Cells are not at standard concentrations, so the actual $\Delta G$ also depends on the ratios of the species ([[Nernst Equation]]).

### Counting electrons through metabolism

Glucose has an average carbon oxidation state of 0 and CO₂ +4, so oxidizing one glucose releases $6 \times 4 = 24$ electrons. They leave as 10 NADH and 2 FADH₂, 12 pairs,[^berg] and end on $6\,\mathrm{O_2}$, which accepts $6 \times 4 = 24$: the redox books of $\mathrm{C_6H_{12}O_6 + 6\,O_2 \to 6\,CO_2 + 6\,H_2O}$ balance.

## Mathematical representation

- Oxidation states $x_k$ of the atoms of a species of charge $q$: $\sum_k x_k = q$. For $\mathrm{C}_c\mathrm{H}_h\mathrm{O}_o\mathrm{N}_n$ (H +1, O −2, N −3), the average carbon state is $\bar{x}_{\mathrm{C}} = (q - h + 2o + 3n)/c$, and complete oxidation to CO₂ releases $c\,(4 - \bar{x}_{\mathrm{C}})$ electrons.
- $\Delta G^{\circ\prime} = -nF\Delta E^{\circ\prime}$, $\Delta E^{\circ\prime} = E^{\circ\prime}_{\text{acceptor}} - E^{\circ\prime}_{\text{donor}}$, $F = 96.485$ kJ V⁻¹ mol⁻¹.[^c17]

## Computational representation

```python
import re

FARADAY = 96.485          # kJ per volt per mole of electrons


def parse(formula: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for element, n in re.findall(r"([A-Z][a-z]?)(\d*)", formula):
        counts[element] = counts.get(element, 0) + int(n or 1)
    return counts


def carbon_oxidation_state(formula: str, charge: int = 0) -> float:
    """Average oxidation state of C, taking H = +1, O = -2, N = -3."""
    c = parse(formula)
    return (charge - c.get("H", 0) + 2 * c.get("O", 0) + 3 * c.get("N", 0)) / c["C"]


def electrons_to_co2(formula: str, charge: int = 0) -> float:
    """Electrons released when every carbon is oxidized to CO2 (oxidation state +4)."""
    return parse(formula)["C"] * (4 - carbon_oxidation_state(formula, charge))


for name, formula, q in [("methane", "CH4", 0), ("formate", "CHO2", -1), ("glucose", "C6H12O6", 0),
                         ("pyruvate", "C3H3O3", -1), ("lactate", "C3H5O3", -1)]:
    print(f"{name:9s} C = {carbon_oxidation_state(formula, q):+.2f}   electrons to CO2: {electrons_to_co2(formula, q):.0f}")
for donor, acceptor, e_d, e_a in [("NADH", "O2", -0.32, 0.82), ("NADH", "pyruvate", -0.32, -0.19)]:
    print(f"{donor} -> {acceptor}: dE = {e_a - e_d:+.2f} V, dG = {-2 * FARADAY * (e_a - e_d):.0f} kJ/mol")
```

```text
methane   C = -4.00   electrons to CO2: 8
formate   C = +2.00   electrons to CO2: 2
glucose   C = +0.00   electrons to CO2: 24
pyruvate  C = +0.67   electrons to CO2: 10
lactate   C = +0.00   electrons to CO2: 12
NADH -> O2: dE = +1.14 V, dG = -220 kJ/mol
NADH -> pyruvate: dE = +0.13 V, dG = -25 kJ/mol
```

Lactate holds 2 more electrons than pyruvate: exactly the pair NADH delivers. Full redox equations, charges included, are balanced by `balance` in [[Stoichiometry#Computational representation]].

## Worked example

> [!example] Fe²⁺ oxidized by permanganate in acid
> 1. **Oxidation states**: Mn +7 → +2 (reduced: MnO₄⁻ is the oxidant); Fe +2 → +3 (oxidized: Fe²⁺ is the reductant).
> 2. **Reduction half**: MnO₄⁻ → Mn²⁺; 4 O need 4 H₂O on the right; 8 H need 8 H⁺ on the left; charge $-1 + 8 = +7$ against $+2$: add 5 e⁻ on the left. $\mathrm{MnO_4^- + 8\,H^+ + 5\,e^- \to Mn^{2+} + 4\,H_2O}$.
> 3. **Oxidation half** $\mathrm{Fe^{2+} \to Fe^{3+} + e^-}$, times 5, then **add**: $\mathrm{MnO_4^- + 5\,Fe^{2+} + 8\,H^+ \to Mn^{2+} + 5\,Fe^{3+} + 4\,H_2O}$, the result of the matrix method in [[Stoichiometry#Computational representation]]. Charge: $-1 + 10 + 8 = +17$ on each side.

## Common misconceptions

> [!warning] "Oxidation needs oxygen"
> Oxidation is electron loss. Dehydrogenases oxidize substrates with NAD⁺ and no O₂ at all.

> [!warning] "Oxidation states are real charges"
> They assign shared electrons to the more electronegative atom by convention. Carbon in CH₄ is not a C⁴⁻ ion.

## Exercises

> [!question] Exercise 1 (L1)
> Give the oxidation state of S in H₂SO₄, SO₂ and H₂S; of N in NH₄⁺, NO₃⁻ and N₂; of Cr in Cr₂O₇²⁻.

> [!success]- Solution
> S: +6, +4, −2. N: −3, +5, 0. Cr: $2x + 7(-2) = -2$, so $x = +6$.

> [!question] Exercise 2 (L1)
> Name the oxidant and the reductant: (a) 2 Fe³⁺ + Sn²⁺ → 2 Fe²⁺ + Sn⁴⁺; (b) lactate + NAD⁺ → pyruvate + NADH + H⁺; (c) 2 H₂O₂ → 2 H₂O + O₂.

> [!success]- Solution
> (a) Fe³⁺ oxidant, Sn²⁺ reductant. (b) NAD⁺ oxidant, lactate reductant (its carbons go from 0 to +2/3 on average). (c) H₂O₂ is both: oxygen goes from −1 to −2 in water and to 0 in O₂ (a disproportionation).

> [!question] Exercise 3 (L2)
> Balance the oxidation of Fe²⁺ by dichromate (Cr₂O₇²⁻ → Cr³⁺) in acid with half-reactions, then check with `balance` from [[Stoichiometry]].

> [!success]- Solution
> Reduction: $\mathrm{Cr_2O_7^{2-} + 14\,H^+ + 6\,e^- \to 2\,Cr^{3+} + 7\,H_2O}$ (7 O give 7 H₂O, 14 H give 14 H⁺, charge $-2 + 14 = 12$ against $6$: 6 e⁻). Six Fe²⁺ → Fe³⁺ supply them: $\mathrm{Cr_2O_7^{2-} + 6\,Fe^{2+} + 14\,H^+ \to 2\,Cr^{3+} + 6\,Fe^{3+} + 7\,H_2O}$. `balance([("Cr2O7", -2), ("Fe", 2), ("H", 1)], [("Cr", 3), ("Fe", 3), "H2O"])` returns `Cr2O72- + 6 Fe2+ + 14 H+ -> 2 Cr3+ + 6 Fe3+ + 7 H2O`.

> [!question] Exercise 4 (L2, Python)
> Compare palmitic acid (C₁₆H₃₂O₂) with glucose: average carbon oxidation state and electrons released on complete oxidation. What does it suggest about fat as a fuel?

> [!success]- Solution
> ```python
> for name, formula in [("palmitic acid", "C16H32O2"), ("glucose", "C6H12O6")]:
>     print(name, round(carbon_oxidation_state(formula), 2), round(electrons_to_co2(formula)))
> # palmitic acid -1.75 92
> # glucose 0.0 24
> ```
> Per carbon, $92/16 = 5.75$ electrons against $24/6 = 4$: fatty-acid carbons are more reduced, so each has more electrons to pass to O₂ (92 electrons for 23 O₂). Fats carry more oxidation energy per carbon than sugars ([[Metabolism]]).

> [!question] Exercise 5 (L2)
> A tumor sequencing study reports an excess of G>T substitutions, also written C>A. Explain why both notations describe the same event, and which redox lesion could produce it.

> [!success]- Solution
> A G:C pair read from the other strand is C:G, so G→T on one strand is C→A on the complementary one: both are the G:C → T:A transversion. Oxidation of guanine to 8-oxoguanine, which pairs with A, produces exactly this change after replication;[^griffiths] the excess is a hypothesis to test (other processes cause transversions), not a proof ([[Point Mutation]]).

## Mastery checklist

- [ ] 1 Recognized: I can define oxidation, reduction, oxidant and reductant, and state the oxidation-state rules.
- [ ] 2 Understood: I can explain the carbon oxidation ladder, the role of NAD⁺/NADH, and how 8-oxoguanine causes a transversion.
- [ ] 3 Practiced: I can balance redox equations with half-reactions, count electrons in Python and compute $\Delta G^{\circ\prime}$ from potentials.
- [ ] 4 Applied: I checked the NAD⁺/NADH balance of the reactions of a real metabolic model, or the substitution spectrum of a real variant set.
- [ ] 5 Explained: I can teach the link between electron counting, reduction potentials and free energy, and why standard potentials do not fix the direction in cells.

## References

[^c4]: [[Chemistry 2e (OpenStax)]], ch. 4 "Stoichiometry of Chemical Reactions", section 4.2 "Classifying Chemical Reactions" (oxidation-reduction reactions, oxidation numbers, oxidizing and reducing agents).
[^half]: [[Chemistry 2e (OpenStax)]], treatment of balancing redox reactions by the half-reaction method in acidic and basic solution; section not verified.
[^c17]: [[Chemistry 2e (OpenStax)]], treatment of electrochemistry (Faraday constant); section not verified.
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of oxidative phosphorylation (standard reduction potentials of NAD⁺/NADH, pyruvate/lactate and O₂/H₂O, $\Delta G^{\circ\prime} = -nF\Delta E^{\circ\prime}$, toxic partial reduction products of O₂), of NAD⁺ as a hydride acceptor, of lactate dehydrogenase, and of the NADH and FADH₂ yield of glucose oxidation.
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), treatment of gene mutation (oxidative damage: 8-oxoguanine pairs with adenine, G:C → T:A transversions).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of DNA repair (base excision repair).
