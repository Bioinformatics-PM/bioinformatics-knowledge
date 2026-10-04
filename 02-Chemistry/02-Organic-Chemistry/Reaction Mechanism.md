---
aliases:
  - Curved-Arrow Mechanism
  - Arrow Pushing
  - Electron-Pushing Formalism
  - Mécanisme réactionnel
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Lewis Structure]]"
  - "[[Covalent Bond]]"
  - "[[Electronegativity]]"
  - "[[Functional Group]]"
related:
  - "[[Nucleophile]]"
  - "[[Electrophile]]"
  - "[[Hydrolysis]]"
  - "[[Enzyme Catalysis]]"
  - "[[Activation Energy]]"
  - "[[Transition State Theory]]"
  - "[[Rate Law]]"
projects: []
sources:
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[MIT 5.12 - Organic Chemistry I]]"
---

# Reaction Mechanism

> [!abstract]
> A reaction mechanism is the story of a reaction told one electron pair at a time: curved arrows show which bonds break, which form, and in which order.

## Definition

A **reaction mechanism** describes, step by step, what happens during a chemical transformation: which bonds break and in what order, which bonds form and in what order, and the relative rates of the steps.[^os6] In **polar** mechanisms, the type that dominates organic and biological chemistry, each step is drawn with **curved arrows**: an arrow moves one electron pair from an electron-rich source (a lone pair or a bond) to an electron-poor sink (an atom, or the space between two atoms where a new bond forms).[^os63][^os65]

## Why it matters

- **Reading enzyme papers and textbooks.** Enzyme mechanisms are drawn with the same arrows as test-tube reactions; reading them tells which residue is the [[Nucleophile]], which is the acid or base, and which bond of the substrate breaks ([[Enzyme Catalysis]]).[^berg]
- **Interpreting mutations.** A residue that carries an arrow in the mechanism is a catalytic residue; a missense change there is expected to destroy activity even when the fold is intact ([[Missense Mutation]]).[^berg]
- **Metabolism as a short list of mechanisms.** The reactions of glycolysis, the citric acid cycle and fatty acid metabolism are a handful of polar mechanisms repeated with different substrates, the Stage 2 list of [[Organic Chemistry]].[^os29]
- **Chemical damage to DNA.** Alkylation, deamination and depurination are mechanisms too: water or a reactive chemical attacks a specific atom of a base ([[Nucleophilic Substitution]], [[Hydrolysis]], [[DNA Repair]]).

## Core (L1)

**Breaking a bond, two ways.** A bond can break **homolytically**, one electron to each fragment (radicals, drawn with half-headed "fishhook" arrows), or **heterolytically**, both electrons to one fragment (ions, drawn with full arrows). Polar reactions are heterolytic: electron-rich sites react with electron-poor sites created by bond polarity.[^os6][^os63]

**The rules of curved arrows.**[^os65]

1. Electrons flow from a nucleophilic **source** (lone pair or π/σ bond) to an electrophilic **sink**.
2. The tail starts at the electrons, never at an atom's nucleus or at a + charge.
3. The head ends on an atom (the pair becomes a lone pair there) or between two atoms (the pair becomes a new bond).
4. The nucleophile can be neutral or negative. Charges follow the electrons: an atom that donates a lone pair into a new bond becomes one unit more positive (HO⁻ becomes a neutral OH group), and an atom that keeps the pair of a broken bond becomes one unit more negative.
5. The octet rule holds: if an arrow brings a pair to an atom that already has an octet, another arrow must take a pair away from it in the same step.

**Reading a mechanism.** For each step ask: which bond is new, which bond is gone, where are the charges now. Intermediates are real species with a lifetime; between them, each step passes through a transition state that cannot be isolated ([[Activation Energy]]).[^os6]

![[ester-hydrolysis-curved-arrows.svg]]

## Deeper (L2)

**Three recurring step types.** The ester hydrolysis above contains the three moves found again and again in biochemical mechanisms: **addition** of a nucleophile to an electrophilic atom (step 1), **loss of a leaving group** as electrons return (step 2), and **proton transfer** (step 3). Carbonyl chemistry, a major block of [[MIT 5.12 - Organic Chemistry I|5.12]] and the core of metabolism, is mostly combinations of these.[^512][^os29]

**Mechanism and rate.** A multistep mechanism has as many transition states as steps; the step with the highest barrier limits the overall rate, and the rate law observed experimentally constrains which mechanisms are possible ([[Rate Law]], [[Transition State Theory]]).[^os6] A mechanism is a model: it must agree with the rate law, the stereochemistry of the products and the intermediates detected, and it is revised when it does not.

**Enzymes use the same arrows.** In chymotrypsin, Ser 195 attacks the carbonyl carbon of the peptide bond while His 57 takes its proton, a tetrahedral intermediate forms, and its collapse breaks the C–N bond: the ester-hydrolysis pattern with a protein nucleophile ([[Nucleophile]]).[^berg] What the enzyme changes is the energy of each step, not the rules of electron flow ([[Enzyme Catalysis]]).

## Mathematical representation

Treat a molecule as a set of atoms $X$ with valence electrons $V(X)$, lone-pair electrons $\ell(X)$ and bond orders $b(X, Y)$. A curved arrow is an operation that moves **two** electrons: a lone pair on $X$ into bond $X$–$Y$ does $\ell(X) \mathrel{-}= 2$, $b(X, Y) \mathrel{+}= 1$; a bond $X$–$Y$ onto atom $Y$ does $b(X, Y) \mathrel{-}= 1$, $\ell(Y) \mathrel{+}= 2$.

The formal charge is $q(X) = V(X) - \ell(X) - \sum_Y b(X, Y)$. Every arrow leaves the electron count $N = \sum_X \ell(X) + 2 \sum_{\{X,Y\}} b(X, Y)$ unchanged, and therefore the net charge $\sum_X q(X) = \sum_X V(X) - N$ too. The octet rule is the constraint $\ell(X) + 2\sum_Y b(X, Y) = 8$ for C, N, O (2 for H) after each step, which is why arrows come in pairs.

## Computational representation

The base-promoted ester hydrolysis of the figure, as bond bookkeeping:

```python
# Base-promoted ester hydrolysis, RC(=O)OR' + HO-, as bond bookkeeping.
# Atoms: Oh, Hh (hydroxide), C (carbonyl carbon), Oc (carbonyl O), Or (ester O);
# R and R' are carbon groups whose own bonds never change.
ELEMENT = {"Oh": "O", "Hh": "H", "C": "C", "Oc": "O", "Or": "O"}
VALENCE = {"O": 6, "C": 4, "H": 1}
lone = {"Oh": 6, "Hh": 0, "C": 0, "Oc": 4, "Or": 4, "R": 0, "R'": 0}   # lone-pair electrons
bonds = {frozenset(p): order for p, order in
         [(("Oh", "Hh"), 1), (("C", "Oc"), 2), (("C", "Or"), 1), (("C", "R"), 1), (("Or", "R'"), 1)]}


def arrow(tail, head):
    """One curved arrow = one electron pair.
    tail: an atom (its lone pair) or a 2-tuple (a bond); head: an atom or a 2-tuple."""
    if isinstance(tail, str):
        lone[tail] -= 2
    else:
        bonds[frozenset(tail)] -= 1
    if isinstance(head, str):
        lone[head] += 2
    else:
        bonds[frozenset(head)] = bonds.get(frozenset(head), 0) + 1


def formal_charge(atom):
    attached = sum(o for pair, o in bonds.items() if atom in pair)
    return VALENCE[ELEMENT[atom]] - lone[atom] - attached


def report(label):
    fc = {a: formal_charge(a) for a in ELEMENT}
    shells = {a: lone[a] + 2 * sum(o for p, o in bonds.items() if a in p) for a in ELEMENT}
    total = sum(lone.values()) + 2 * sum(bonds.values())
    charged = ", ".join(f"{a} {q:+d}" for a, q in fc.items() if q) or "none"
    full = all(shells[a] == (2 if ELEMENT[a] == "H" else 8) for a in ELEMENT)
    print(f"{label:24} charges: {charged:16} octets ok: {full}  electrons: {total}")


report("0 ester + HO-")
arrow("Oh", ("Oh", "C")); arrow(("C", "Oc"), "Oc")
report("1 addition")
arrow("Oc", ("C", "Oc")); arrow(("C", "Or"), "Or")
report("2 loss of R'O-")
arrow("Or", ("Or", "Hh")); arrow(("Oh", "Hh"), "Oh")
report("3 proton transfer")
```

```text
0 ester + HO-            charges: Oh -1            octets ok: True  electrons: 26
1 addition               charges: Oc -1            octets ok: True  electrons: 26
2 loss of R'O-           charges: Or -1            octets ok: True  electrons: 26
3 proton transfer        charges: Oh -1            octets ok: True  electrons: 26
```

The negative charge travels from hydroxide to the carbonyl oxygen, to the leaving alkoxide, and ends on the carboxylate; the electron count never changes.

## Worked example

> [!example] Reading the ester hydrolysis mechanism (figure above)
> | Step | Arrows (source → sink) | Bond formed | Bond broken | Charge ends on |
> |---|---|---|---|---|
> | 1 Addition | HO⁻ lone pair → C; C=O π bond → O | C–OH | C=O π | carbonyl O (−1) |
> | 2 Loss of leaving group | O⁻ lone pair → C–O; C–OR′ bond → OR′ | C=O π | C–OR′ | R′O⁻ |
> | 3 Proton transfer | R′O⁻ lone pair → H; O–H bond → O | R′O–H | O–H of the acid | carboxylate |
>
> Net: RCOOR′ + HO⁻ → RCOO⁻ + R′OH. Hydroxide adds to the carbonyl to give a **tetrahedral intermediate**; losing the alkoxide gives the carboxylic acid, which is deprotonated to the carboxylate.[^os216] Steps 1 and 2 each use two arrows, because carbon cannot exceed an octet.

## Common misconceptions

> [!warning] "Arrows show where atoms move"
> Arrows move **electrons**. In a proton transfer the arrow goes from the base's lone pair to the H, not from the H to the base: the proton is the sink, not the source.[^os65]

> [!warning] "One arrow per step"
> Whenever electrons arrive at an atom that already has a full octet, a second arrow must leave it in the same step (the C=O π bond in step 1).[^os65]

## Exercises

> [!question] Exercise 1 (L1)
> In step 1 of the figure, name the nucleophile, the electrophilic atom, the source and the sink of each arrow.

> [!success]- Solution
> Nucleophile: HO⁻ (its oxygen lone pair). Electrophilic atom: the carbonyl carbon. Arrow 1: source = O lone pair of HO⁻, sink = new O–C bond. Arrow 2: source = C=O π bond, sink = the carbonyl O, which becomes O⁻.[^os65]

> [!question] Exercise 2 (L2, Python)
> Starting from the original molecule, apply step 1, then the reverse of step 1 (the O⁻ lone pair re-forms C=O and the C–OH bond returns to the hydroxide oxygen). Which species do you get, and is the octet check satisfied?

> [!success]- Solution
> ```python
> arrow("Oh", ("Oh", "C")); arrow(("C", "Oc"), "Oc")
> report("1 addition")
> arrow("Oc", ("C", "Oc")); arrow(("Oh", "C"), "Oh")
> report("1 reversed")
> ```
> ```text
> 1 addition               charges: Oc -1            octets ok: True  electrons: 26
> 1 reversed               charges: Oh -1            octets ok: True  electrons: 26
> ```
> Back to ester + HO⁻, with valid octets. The intermediate can expel HO⁻ instead of R′O⁻ and return to the ester: steps 1 and 2 are reversible, and which group leaves depends on their relative stability as anions.

> [!question] Exercise 3 (L2)
> Why does step 3 make base-promoted ester hydrolysis effectively irreversible?

> [!success]- Solution
> It transfers a proton from a carboxylic acid (pKa near 5) to an alkoxide, the conjugate base of an alcohol (pKa near 16).[^os] The equilibrium constant is about $10^{16-5} = 10^{11}$ in favour of carboxylate + alcohol, and the carboxylate is a poor electrophile, so the reverse attack does not happen.

## Mastery checklist

- [ ] 1 Recognized: I can tell a curved arrow from a reaction arrow and say what it moves.
- [ ] 2 Understood: I can apply the arrow rules (source, sink, charges, octet) and list bonds formed and broken per step.
- [ ] 3 Practiced: I can write the arrows of ester hydrolysis and of a proton transfer, and check charges and octets in code.
- [ ] 4 Applied: I read an enzyme mechanism from a paper or textbook and identified its catalytic residues and the bond that breaks.
- [ ] 5 Explained: I can explain why a mechanism is a model constrained by rate laws and intermediates, and why enzymes change energies, not electron-flow rules.

## References

[^os6]: [[Organic Chemistry (OpenStax)]], ch. 6, overview of organic reactions (mechanisms, polar and radical reactions, energy diagrams).
[^os63]: [[Organic Chemistry (OpenStax)]], sec. 6.3 "Polar Reactions".
[^os65]: [[Organic Chemistry (OpenStax)]], sec. 6.5 "Using Curved Arrows in Polar Reaction Mechanisms".
[^os216]: [[Organic Chemistry (OpenStax)]], sec. 21.6 "Chemistry of Esters".
[^os29]: [[Organic Chemistry (OpenStax)]], ch. 29 "The Organic Chemistry of Metabolic Pathways".
[^os]: [[Organic Chemistry (OpenStax)]], acidity of carboxylic acids and alcohols.
[^512]: [[MIT 5.12 - Organic Chemistry I]], Spring 2005, lecture handout titles (carbonyl chemistry).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002).
