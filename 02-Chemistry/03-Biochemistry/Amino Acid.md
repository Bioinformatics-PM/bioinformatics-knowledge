---
aliases:
  - Amino Acids
  - α-Amino Acid
  - Standard Amino Acid
  - Residue
  - Acide aminé
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Functional Group]]"
  - "[[Chirality]]"
  - "[[Acid-Base Equilibrium]]"
  - "[[Hydrophobic Effect]]"
related:
  - "[[Peptide Bond]]"
  - "[[Protein]]"
  - "[[Protein Structure]]"
  - "[[Genetic Code]]"
  - "[[Codon]]"
  - "[[Translation]]"
  - "[[Missense Mutation]]"
  - "[[Substitution Matrix]]"
  - "[[Hydropathy Plot]]"
  - "[[Henderson-Hasselbalch Equation]]"
  - "[[Isoelectric Point]]"
  - "[[FASTA Format]]"
  - "[[Post-Translational Modification]]"
  - "[[Amino Acid Metabolism]]"
projects:
  - "[[02-sequence-translation]]"
  - "[[06-mutation-lab]]"
sources:
  - "[[Biochemistry (Berg)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[Kyte 1982 - A Simple Method for Displaying the Hydropathic Character of a Protein]]"
  - "[[NCBI BLAST]]"
---

# Amino Acid

> [!abstract]
> Amino acids are the 20 building blocks of proteins: all share the same backbone (an amino group, a carboxyl group and a hydrogen on one central carbon) and differ only by a side chain, whose size, charge and love or fear of water give each protein its properties.

## Definition

An **α-amino acid** is a molecule in which a central carbon, the **α-carbon (Cα)**, carries an amino group, a carboxyl group, a hydrogen atom and a variable **side chain (R group)**. The **20 standard amino acids**, specified by the [[Genetic Code]], are the monomers of [[Protein|proteins]]; they differ only in their side chains.[^berg][^os3] Inside a polypeptide, each amino acid unit is called a **residue**, because it has lost the elements of water when the [[Peptide Bond|peptide bonds]] formed.[^berg]

## Why it matters

- **The alphabet of protein data.** Every protein sequence in [[FASTA Format|FASTA]] files and [[UniProt]] is a string of one-letter amino acid codes; NCBI tools also accept a few extra symbols (B, Z, X, U, `*`, `-`, below).[^ncbi]
- **Properties are the features.** Hydropathy, charge and size are the inputs of [[Hydropathy Plot|hydropathy plots]], [[Isoelectric Point|isoelectric point]] calculators and the first filter of variant interpretation ([[Missense Mutation]]); [[Substitution Matrix|substitution matrices]] summarize which residues replace each other in evolution.
- **Translation tools end here.** [[02-sequence-translation]] maps codons to these letters; [[06-mutation-lab]] shows how one base change becomes one residue change.
- **Mass spectrometry** identifies peptides from residue masses ([[Monoisotopic Mass]], [[Bottom-Up Proteomics]]).

## Core (L1)

### The common structure

```text
            H                       side chain R: one of 20
            |
   H3N(+) — Cα — COO(−)             zwitterion: the form that dominates near pH 7
            |
            R
```

- **Zwitterion.** Near neutral pH the amino group is protonated (–NH₃⁺) and the carboxyl group deprotonated (–COO⁻): the free amino acid is a dipolar ion.[^berg]
- **Chirality.** Except in glycine, whose side chain is a second hydrogen, Cα carries four different groups and is a stereocenter ([[Chirality]]). Proteins are built from **L**-amino acids only.[^berg] Isoleucine and threonine have a second stereocenter in their side chain.[^lehninger]

### The 20 standard amino acids

Grouped by side chain. Names and codes from the biochemistry texts;[^berg][^lehninger][^mcmurry] hydropathy is the Kyte-Doolittle value (positive = hydrophobic).[^kyte]

| Amino acid | 3-letter | 1-letter | Class | Side chain, key feature | Hydropathy |
|---|---|---|---|---|---:|
| Alanine | Ala | A | hydrophobic | methyl | 1.8 |
| Valine | Val | V | hydrophobic | branched aliphatic | 4.2 |
| Leucine | Leu | L | hydrophobic | branched aliphatic | 3.8 |
| Isoleucine | Ile | I | hydrophobic | branched aliphatic, second stereocenter | 4.5 |
| Methionine | Met | M | hydrophobic | thioether (–S–CH₃) | 1.9 |
| Phenylalanine | Phe | F | hydrophobic | aromatic: phenyl ring | 2.8 |
| Tryptophan | Trp | W | hydrophobic | aromatic: indole (two fused rings) | −0.9 |
| Serine | Ser | S | polar | hydroxyl (–CH₂OH) | −0.8 |
| Threonine | Thr | T | polar | hydroxyl, second stereocenter | −0.7 |
| Asparagine | Asn | N | polar | amide (the amide of Asp) | −3.5 |
| Glutamine | Gln | Q | polar | amide (the amide of Glu) | −3.5 |
| Tyrosine | Tyr | Y | polar | aromatic ring with hydroxyl (phenol) | −1.3 |
| Aspartate | Asp | D | acidic | carboxylate, negative | −3.5 |
| Glutamate | Glu | E | acidic | carboxylate, negative | −3.5 |
| Lysine | Lys | K | basic | amino group at the end of a long chain, positive | −3.9 |
| Arginine | Arg | R | basic | guanidinium, positive | −4.5 |
| Histidine | His | H | basic | imidazole, only partly positive at pH 7 | −3.2 |
| Glycine | Gly | G | special | a hydrogen atom: achiral, flexible backbone | −0.4 |
| Proline | Pro | P | special | ring bonded to its own backbone nitrogen: rigid | −1.6 |
| Cysteine | Cys | C | special | thiol (–SH): forms disulfide bonds | 2.5 |

**The three special cases.**[^berg]

- **Glycine** has the smallest side chain, so its backbone can adopt conformations forbidden to the others, and it fits where nothing else does.
- **Proline**'s side chain closes a ring onto the backbone nitrogen: the residue is rigid, has no N–H to donate a hydrogen bond, and tends to break α helices ([[Protein Structure]]).
- **Cysteine**'s thiol can be oxidized with another cysteine thiol into a covalent **disulfide bond**, a cross-link within or between chains.

> [!info] Classes are conventions
> Borderline residues move between textbooks. Lehninger uses five groups: nonpolar aliphatic (Gly, Ala, Pro, Val, Leu, Ile, Met), aromatic (Phe, Tyr, Trp), polar uncharged (Ser, Thr, Cys, Asn, Gln), positively charged (Lys, Arg, His) and negatively charged (Asp, Glu).[^lehninger] [[Missense Mutation]] follows Alberts, who puts Gly and Cys among the nonpolar residues. Check which convention a tool uses before comparing "class changes".

### Ionizable groups

Every amino acid has an α-carboxyl and an α-amino group; in a polypeptide only the two termini keep them free. Seven side chains are also ionizable. Typical pKa values in proteins:[^berg]

| Group | Where | pKa | Charged form | Charge at pH 7 |
|---|---|---:|---|---|
| α-carboxyl | C-terminus | 3.1 | –COO⁻ | −1 |
| carboxyl | Asp, Glu | 4.1 | –COO⁻ | −1 |
| imidazole | His | 6.0 | imidazolium (+) | about +0.1 |
| α-amino | N-terminus | 8.0 | –NH₃⁺ | about +0.9 |
| thiol | Cys | 8.3 | –S⁻ | about 0 |
| ε-amino | Lys | 10.8 | –NH₃⁺ | +1 |
| phenol | Tyr | 10.9 | –O⁻ | 0 |
| guanidinium | Arg | 12.5 | (+) | +1 |

The last column follows from the [[Henderson-Hasselbalch Equation]] (Mathematical representation). In a free amino acid the α groups have different values, for glycine 2.34 and 9.60.[^lehninger]

> [!tip] One-letter codes that are not initials
> Eleven codes are initials (A C G H I L M P S T V). For the other nine: **F** = "Fenylalanine", **R** = "aRginine", **Y** = "tYrosine", **W** = "tWo rings" (tryptophan), **D** = "asparDic", **E** = "glutEmic", **N** = "asparagiNe", **Q** = "Q-tamine", **K** = the letter next to L, lysine. These are memory aids, not the official reasons.

## Deeper (L2)

**Charge depends on pH and on the neighbourhood.** Each ionizable group is charged in a fraction of molecules given by its pKa and the pH. Histidine, with a pKa near 6, is the one residue whose charge changes over the physiological range, which suits it to accept and donate protons in enzyme active sites ([[Enzyme Catalysis]]).[^berg] The tabulated pKa values are typical: inside a folded protein, nearby charges or a nonpolar environment shift them.[^berg] Summing all groups gives a protein's net charge and its [[Isoelectric Point]], the pH at which it does not move in an electric field.

**Beyond the 20.** Two further amino acids are inserted during translation in a few proteins: **selenocysteine** (Sec, one-letter code U), read from a UGA codon in a special mRNA context ([[Genetic Code#Advanced (L3)]]), and **pyrrolysine** (Pyl), read from UAG in some archaea and bacteria.[^lehninger] Many more appear **after** translation, by modification of standard residues: 4-hydroxyproline in collagen, phosphorylated serine, threonine and tyrosine, γ-carboxyglutamate in clotting factors ([[Post-Translational Modification]]).[^lehninger] A sequence string records the gene product, not these modifications.

**Hydropathy scales disagree at the margins.** Trp is grouped with the hydrophobic residues, yet its Kyte-Doolittle value is slightly negative (−0.9); Tyr is aromatic but hydrophilic on this scale.[^kyte] Different scales rank such residues differently, so a prediction depends on the scale chosen: record it ([[Hydropathy Plot]]).

## Advanced (L3)

**Amino acids as vectors.** Machine-learning methods need numbers. The simplest encoding, **one-hot**, maps each residue to a 20-dimensional vector with a single 1; every pair of distinct residues is then at the same distance ($\sqrt{2}$), so the encoding says nothing about similarity. Physicochemical encodings (hydropathy, charge, volume) place Leu near Ile and far from Lys (Exercise 5); learned representations pursue the same goal from data ([[Protein Language Model]]).

**Ambiguity in sequence data.** Database sequences use extra letters: **B** (Asp or Asn), **Z** (Glu or Gln), **X** (any amino acid), **U** (selenocysteine), `*` (translation stop) and `-` (gap).[^ncbi] A parser that assumes 20 letters will crash on, or silently drop, real data.

## Mathematical representation

- **Alphabets.** $\mathcal{A} = \{A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y\}$, $|\mathcal{A}| = 20$. The NCBI protein alphabet is $\mathcal{E} = \mathcal{A} \cup \{B, Z, X, U, *, -\}$,[^ncbi] with ambiguity sets $B \mapsto \{D, N\}$, $Z \mapsto \{E, Q\}$, $X \mapsto \mathcal{A}$.
- **Properties** are functions on the alphabet: a hydropathy scale $h : \mathcal{A} \to \mathbb{R}$, a class map $\kappa : \mathcal{A} \to \{\text{hydrophobic}, \text{polar}, \text{acidic}, \text{basic}, \text{special}\}$.
- **Composition** of $s \in \mathcal{A}^n$: $f_a(s) = \#_a(s)/n$, with $\sum_a f_a = 1$. The **mean hydropathy** $\bar h(s) = \frac{1}{n}\sum_i h(s_i) = \sum_a f_a\, h(a)$ depends only on composition, not on order.
- **Ionization.** For a group of acid dissociation constant $pK_a$, the protonated fraction at a given pH is $\theta = 1/(1 + 10^{\,\mathrm{pH} - pK_a})$. With $\mathcal{B}$ the basic groups (N-terminus, Lys, Arg, His: charged when protonated) and $\mathcal{C}$ the acidic groups (C-terminus, Asp, Glu, Cys, Tyr: charged when deprotonated), the net charge is
$$Q(\mathrm{pH}) = \sum_{j \in \mathcal{B}} \frac{1}{1 + 10^{\,\mathrm{pH} - pK_j}} - \sum_{j \in \mathcal{C}} \frac{1}{1 + 10^{\,pK_j - \mathrm{pH}}}.$$
Every term decreases with pH, so $Q$ is strictly decreasing and has a unique root, the isoelectric point $pI$: $Q(pI) = 0$, found by bisection ([[Root Finding]]).
- **One-hot encoding.** $e : \mathcal{A} \to \{0,1\}^{20}$, $e(a)_k = 1$ iff $a$ is the $k$-th letter; $\lVert e(a) - e(b) \rVert = \sqrt{2}$ for all $a \ne b$.

## Computational representation

A dictionary keyed by the one-letter code holds the per-residue properties ([[Hash Table]]); everything else is a loop over the string.

```python
# one-letter code: (three-letter code, class, Kyte-Doolittle hydropathy)
AMINO_ACIDS = {
    "A": ("Ala", "hydrophobic", 1.8),  "V": ("Val", "hydrophobic", 4.2),
    "L": ("Leu", "hydrophobic", 3.8),  "I": ("Ile", "hydrophobic", 4.5),
    "M": ("Met", "hydrophobic", 1.9),  "F": ("Phe", "hydrophobic", 2.8),
    "W": ("Trp", "hydrophobic", -0.9), "S": ("Ser", "polar", -0.8),
    "T": ("Thr", "polar", -0.7),       "N": ("Asn", "polar", -3.5),
    "Q": ("Gln", "polar", -3.5),       "Y": ("Tyr", "polar", -1.3),
    "D": ("Asp", "acidic", -3.5),      "E": ("Glu", "acidic", -3.5),
    "K": ("Lys", "basic", -3.9),       "R": ("Arg", "basic", -4.5),
    "H": ("His", "basic", -3.2),       "G": ("Gly", "special", -0.4),
    "P": ("Pro", "special", -1.6),     "C": ("Cys", "special", 2.5),
}
THREE_TO_ONE = {three: one for one, (three, _, _) in AMINO_ACIDS.items()}
EXTRA = set("BZXU*-")          # other symbols accepted in NCBI protein FASTA

# typical pKa values of ionizable groups in proteins (Berg), and the charge of the protonated form
PKA = {"Nterm": (8.0, +1), "K": (10.8, +1), "R": (12.5, +1), "H": (6.0, +1),
       "Cterm": (3.1, -1), "D": (4.1, -1), "E": (4.1, -1), "C": (8.3, -1), "Y": (10.9, -1)}


def to_one_letter(three_letter: str) -> str:
    """'Met-Lys-Trp' -> 'MKW'."""
    return "".join(THREE_TO_ONE[t.capitalize()] for t in three_letter.split("-"))


def invalid_positions(seq: str) -> list[tuple[int, str]]:
    """1-based positions of characters that are not protein FASTA symbols."""
    return [(i, c) for i, c in enumerate(seq.upper(), 1) if c not in AMINO_ACIDS and c not in EXTRA]


def mean_hydropathy(seq: str) -> float:
    return sum(AMINO_ACIDS[aa][2] for aa in seq) / len(seq)


def net_charge(seq: str, pH: float) -> float:
    """Henderson-Hasselbalch sum over the termini and ionizable side chains."""
    groups = ["Nterm", "Cterm"] + [aa for aa in seq if aa in PKA]
    total = 0.0
    for g in groups:
        pka, z = PKA[g]
        if z > 0:   # fraction protonated (charged) for a base
            total += 1 / (1 + 10 ** (pH - pka))
        else:       # fraction deprotonated (charged) for an acid
            total -= 1 / (1 + 10 ** (pka - pH))
    return total


def isoelectric_point(seq: str, tol: float = 1e-4) -> float:
    """pH where net_charge = 0, by bisection (the charge decreases with pH)."""
    lo, hi = 0.0, 14.0
    while hi - lo > tol:
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if net_charge(seq, mid) > 0 else (lo, mid)
    return (lo + hi) / 2


peptide = to_one_letter("Gly-His-Lys-Asp-Glu")        # invented toy peptide
print(peptide, round(mean_hydropathy(peptide), 2))
print(invalid_positions("MKV3LJX*"))
for pH in (3.0, 7.0, 11.0):
    print(pH, round(net_charge(peptide, pH), 2))
print("pI", round(isoelectric_point(peptide), 2))
```

```text
GHKDE -2.9
[(4, '3'), (6, 'J')]
3.0 2.41
7.0 -1.0
11.0 -2.61
pI 5.23
```

Real pI calculators use other pKa sets and give somewhat different values; the model also ignores pKa shifts inside folded proteins. Treat the result as an estimate, and state the pKa table used.

## Worked example

> [!example] Net charge of the toy peptide GHKDE at pH 7 (invented)
> 1. **List the ionizable groups**: N-terminus (Gly), His, Lys, Asp, Glu, C-terminus (Glu). Gly has no ionizable side chain.
> 2. **Charged fractions** with $\theta = 1/(1 + 10^{\pm(\mathrm{pH} - pK_a)})$ and the pKa table above: N-terminus $+0.909$; His $+0.091$; Lys $+0.9998$; Asp $-0.9987$; Glu $-0.9987$; C-terminus $-0.9999$.
> 3. **Sum**: $0.909 + 0.091 + 1.000 - 0.999 - 0.999 - 1.000 \approx -1.0$.
> 4. **Read it**: three negative charges against two positive ones and a mostly neutral His. The peptide is negative at pH 7, so its pI is below 7 (the code finds 5.23), where His and the N-terminus are fully protonated and the carboxylates start to pick up protons.

## Common misconceptions

> [!warning] "Basic residues are positive and acidic residues negative, full stop"
> Charge is a fraction set by pKa and pH. Lys and Arg are essentially fully positive at pH 7, but His is only about 10 % protonated (pKa 6.0), and in a folded protein pKa values shift with the environment.[^berg]

> [!warning] "A residue is just a free amino acid in a chain"
> A residue has lost the elements of water to its peptide bonds: only the N-terminal residue keeps a free α-amino group and only the C-terminal one a free α-carboxyl group. Masses and charges must be computed for residues, plus one water and the two termini ([[Peptide Bond]], [[Monoisotopic Mass]]).

## Exercises

> [!question] Exercise 1 (L1)
> Write `Met-Gly-Trp-Lys-Asp-Phe` in one-letter code, and `QYERN` in three-letter code.

> [!success]- Solution
> `MGWKDF`. `QYERN` = Gln-Tyr-Glu-Arg-Asn. The trap letters are W (Trp), K (Lys), D (Asp), F (Phe), Q (Gln), Y (Tyr), E (Glu), R (Arg), N (Asn): exactly the nine codes that are not initials.

> [!question] Exercise 2 (L2)
> With pKa 6.0, compute the fraction of histidine side chains protonated at pH 5.0, 6.0, 7.0 and 7.4. Why is His, and not Lys, the usual proton shuttle of active sites?

> [!success]- Solution
> $\theta = 1/(1 + 10^{\,\mathrm{pH} - 6.0})$: 0.909 at pH 5.0, 0.5 at 6.0, 0.091 at 7.0, 0.038 at 7.4. Near neutral pH, His exists in both forms in appreciable amounts and switches between them with small pH or environment changes, so it can both accept and give back a proton. Lys (pKa 10.8) is almost always protonated, so it cannot shuttle protons at pH 7.[^berg]

> [!question] Exercise 3 (L2, Python)
> Write `to_three_letter(seq)`, which accepts lowercase input and returns the dash-separated three-letter form. Then explain the output of `invalid_positions("MKV3LJX*")` from the code above: why are `3` and `J` rejected but `X` and `*` accepted?

> [!success]- Solution
> ```python
> def to_three_letter(seq: str) -> str:
>     """'mkw' -> 'Met-Lys-Trp' (standard residues only)."""
>     return "-".join(AMINO_ACIDS[aa][0] for aa in seq.upper())
>
> print(to_three_letter("mkwde"))           # Met-Lys-Trp-Asp-Glu
> print(invalid_positions("MKV3LJX*"))      # [(4, '3'), (6, 'J')]
> ```
> Digits are never sequence, and `J` is not in the NCBI list of accepted amino acid codes, whereas `X` (any amino acid) and `*` (translation stop) are.[^ncbi] `to_three_letter` raises `KeyError` on `X`: decide explicitly how a tool should render ambiguity codes instead of letting it crash.

> [!question] Exercise 4 (L3, Python)
> Use `isoelectric_point` and `net_charge` to compute the pI and the charge at pH 7.4 of the toy peptides `KKKGG` and `DDEGG`. Explain both values from the pKa table, then say why a real protein's measured pI can differ from such a calculation.

> [!success]- Solution
> ```python
> for s in ("KKKGG", "DDEGG"):
>     print(s, round(isoelectric_point(s), 2), round(net_charge(s, 7.4), 2))
> # KKKGG 11.1 2.8
> # DDEGG 3.28 -3.2
> ```
> `KKKGG` carries four basic groups (three Lys, N-terminus) and one acidic group: it stays positive until the Lys groups lose protons, so its pI lies near their pKa (10.8), at 11.1. `DDEGG` has four acidic groups against one basic group: it becomes neutral only when the carboxylates are mostly protonated, near pH 3.3. In real proteins the pKa of each group depends on its environment, and modifications (phosphorylation adds negative charge) change the count, so the sequence-based pI is an estimate ([[Isoelectric Point]]).[^berg]

> [!question] Exercise 5 (L3, Python)
> Compare two encodings of residues: one-hot vectors, and a 2-feature vector (Kyte-Doolittle value divided by 4.5, charge −1/0/+1 from the class). Compute the Euclidean distances for the pairs Leu-Ile, Leu-Lys, Asp-Glu and Asp-Lys. What does each encoding "know"?

> [!success]- Solution
> ```python
> import math
>
> ORDER = "ACDEFGHIKLMNPQRSTVWY"
>
> def one_hot(aa):
>     return [1.0 if a == aa else 0.0 for a in ORDER]
>
> def features(aa):
>     _, cls, kd = AMINO_ACIDS[aa]
>     return [kd / 4.5, {"acidic": -1.0, "basic": 1.0}.get(cls, 0.0)]
>
> for a, b in (("L", "I"), ("L", "K"), ("D", "E"), ("D", "K")):
>     print(a, b, round(math.dist(one_hot(a), one_hot(b)), 3),
>           round(math.dist(features(a), features(b)), 3))
> ```
> ```text
> L I 1.414 0.156
> L K 1.414 1.982
> D E 1.414 0.0
> D K 1.414 2.002
> ```
> One-hot puts every pair at $\sqrt{2}$: it knows identity only. The feature encoding makes Leu-Ile and Asp-Glu close and charge reversals far, matching the conservative substitutions of [[Missense Mutation]]. But Asp and Glu become identical (distance 0): two features lose information (size, for instance), which is why practical encodings use more properties or learn them from data.

## Mastery checklist

- [ ] 1 Recognized: I can draw the common structure, and give the one- and three-letter codes of the 20 standard amino acids.
- [ ] 2 Understood: I can classify each side chain, explain the special roles of Gly, Pro and Cys, and say which groups are charged at pH 7.
- [ ] 3 Practiced: I can compute composition, mean hydropathy, net charge and pI of a sequence in Python, and validate a protein alphabet.
- [ ] 4 Applied: I used these properties on real proteins in [[02-sequence-translation]] and [[06-mutation-lab]] (class change and charge change of a missense variant).
- [ ] 5 Explained: I can teach why classes and scales are conventions, why pKa values shift in proteins, and how residue encodings shape what a model can learn.

## References

[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of protein composition: the 20 amino acids, chirality, zwitterions, side-chain properties, typical pKa values of ionizable groups in proteins, disulfide bonds.
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of amino acids: classification in five groups, second stereocenters of Ile and Thr, titration of glycine, uncommon and modified amino acids (selenocysteine, pyrrolysine, hydroxyproline, phosphorylated residues, γ-carboxyglutamate).
[^os3]: [[Biology 2e (OpenStax)]], Unit 1, chapter "Biological Macromolecules", section on proteins and amino acids.
[^mcmurry]: [[Organic Chemistry (OpenStax)]], ch. 26 "Biomolecules: Amino Acids, Peptides, and Proteins".
[^kyte]: [[Kyte 1982 - A Simple Method for Displaying the Hydropathic Character of a Protein]], *Journal of Molecular Biology* 157:105-132, the hydropathy scale.
[^ncbi]: [[NCBI BLAST]], BLAST documentation "Query Input and database selection", FASTA format description: accepted amino acid codes (including B, Z, X, U, `*` and `-`).
