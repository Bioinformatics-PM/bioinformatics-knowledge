---
aliases:
  - Base Substitution
  - Single-Base Substitution
  - Single-Nucleotide Substitution
  - SNV
  - Transition
  - Transversion
  - Mutation ponctuelle
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Mutation]]"
  - "[[Nucleotide]]"
  - "[[Base Pairing]]"
  - "[[DNA Replication]]"
related:
  - "[[Silent Mutation]]"
  - "[[Missense Mutation]]"
  - "[[Nonsense Mutation]]"
  - "[[Indel]]"
  - "[[Single Nucleotide Polymorphism]]"
  - "[[DNA Repair]]"
  - "[[Kimura Two-Parameter Model]]"
  - "[[Variant Calling]]"
  - "[[Haplotype Phasing]]"
projects:
  - "[[03-genome-diff]]"
  - "[[06-mutation-lab]]"
sources:
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Freeland 1998 - The Genetic Code Is One in a Million]]"
  - "[[Molecular Evolution (Yang)]]"
  - "[[Lobry 1996 - Asymmetric Substitution Patterns in the Two DNA Strands of Bacteria]]"
  - "[[HTS Format Specifications]]"
---

# Point Mutation

> [!abstract]
> A point mutation replaces one base pair of DNA by another. The twelve possible changes form two chemical classes, transitions and transversions, which arise by different mechanisms, at different rates, and leave recognizable fingerprints in sequence data.

## Definition

A **point mutation** (single-base substitution) changes one base pair into another, for example C:G into T:A.[^griffiths] It is a **transition** when a purine replaces a purine or a pyrimidine a pyrimidine (A ↔ G, C ↔ T), and a **transversion** when a purine and a pyrimidine are exchanged.[^griffiths] Some textbooks use "point mutation" more broadly for any change of one or a few base pairs, including single-base insertions and deletions;[^griffiths] in this vault those are [[Indel|indels]]. A single-base difference observed between a genome and a reference is a **single-nucleotide variant** (SNV); a common one is a [[Single Nucleotide Polymorphism]].

[[Mutation]] introduces the classes; this note goes into their chemistry, their bookkeeping in data and their rates.

## Why it matters

- **The simplest VCF record.** An SNV is one position, one `REF` base and one `ALT` base.[^hts] [[03-genome-diff]] reports them and [[06-mutation-lab]] models them.
- **Ts/Tv is a quality signal.** Real mutations are enriched in transitions,[^freeland][^alberts] whereas random errors do not favour them. A call set whose transition fraction is lower than expected contains errors (see the mixture model below).
- **Substitution models separate the classes.** Phylogenetic models such as [[Kimura Two-Parameter Model|K80]] give transitions and transversions different rates.[^yang]
- **Spectra point to causes.** Counting substitutions by class and neighbouring bases reveals the processes that produced them, from methyl-CpG deamination to ultraviolet light ([[Mutation#Advanced (L3)]]).

## Core (L1)

### Twelve substitutions, two classes

![[transitions-transversions.svg]]

Each base has one transition partner and two transversion partners: 4 of the 12 ordered substitutions are transitions, 8 are transversions.

### A mutation changes a base pair, not a letter

DNA is double-stranded, so a substitution changes a **pair**: C:G → T:A reads as C>T on one strand and G>A on the other. The 12 single-strand substitutions therefore form only **6 base-pair classes**. By convention they are named from the pyrimidine of the original pair: C>A, C>G, C>T, T>A, T>C, T>G, of which two (C>T, T>C) are transitions.

### How a mismatch becomes a mutation

A wrong base inserted during replication is at first only a mismatch; if proofreading and mismatch repair miss it, the next replication copies it into both strands of one daughter molecule ([[DNA Replication]], [[DNA Repair]]).[^alberts]

```text
original pair              G:C
replication 1              G·T   (T wrongly inserted opposite G: a mismatch)   +   G:C
replication 2 of G·T       G:C   (the G strand is copied correctly)            +   A:T   (the T strand templates an A)
result                     one granddaughter molecule carries A:T instead of G:C: a transition, now on both strands
```

### Effect depends on position

In a coding sequence, the same substitution can be [[Silent Mutation|silent]], [[Missense Mutation|missense]] or [[Nonsense Mutation|nonsense]], depending on the codon and the position within it; outside genes it usually changes no protein at all ([[Genetic Code]]).

## Deeper (L2)

### Mechanisms and their fingerprints

| Mechanism | Typical change | Class |
|---|---|---|
| Deamination of cytosine to uracil (U pairs with A) | C:G → T:A | transition[^alberts] |
| Deamination of 5-methylcytosine to thymine, at methylated CpG | C:G → T:A at CpG | transition[^alberts] |
| Base analogs (5-bromouracil, 2-aminopurine) that mispair | A:T ↔ G:C | transitions[^griffiths] |
| Alkylation by ethyl methanesulfonate (EMS): O⁶-ethylguanine pairs with T | G:C → A:T | transition[^griffiths] |
| Oxidation of guanine to 8-oxoguanine, which pairs with A | G:C → T:A | transversion[^griffiths] |
| Ultraviolet light, acting on adjacent pyrimidines | C → T at dipyrimidines | transition[^griffiths][^alberts] |

Several frequent mechanisms produce transitions, consistent with the transition bias of real mutation;[^alberts][^freeland] 5-methylcytosine deamination makes CpG sites hotspots because the product, thymine, is a normal base that repair cannot recognize as damage.[^alberts]

### From counts to rates: the Ts/Tv ratio

If every substitution were equally likely, the ratio of transitions to transversions would be $4/8 = 0.5$ ([[Mutation#Mathematical representation]]). In the K80 model, each base mutates to its transition partner at rate $\alpha$ and to each of its two transversion partners at rate $\beta$, with $\kappa = \alpha / \beta$.[^yang] The expected ratio of new transitions to transversions is then

$$\frac{\text{Ts}}{\text{Tv}} = \frac{\alpha}{2\beta} = \frac{\kappa}{2},$$

so a ratio of 2 corresponds to $\kappa = 4$: each transition is four times as likely as each particular transversion. Keep the two quantities apart: Ts/Tv counts events, $\kappa$ compares per-pathway rates.

### Context matters

Mutation rates depend on the neighbouring bases (CpG is the classic case).[^alberts] Describing a substitution with its 5' and 3' neighbours gives a **trinucleotide context**, such as `T[C>T]G`: 6 classes x 4 x 4 flanking bases = **96 channels**.

## Advanced (L3)

- **Mutational spectra.** A set of SNVs summarized as counts over the 96 channels is a spectrum; comparing spectra, or decomposing many of them into recurring components ([[Non-Negative Matrix Factorization]]), links observed mutations to the processes that caused them.
- **Collapsing strands is an assumption.** Naming C>T and G>A alike assumes both strands mutate the same way. In bacteria, the leading and lagging strands of replication accumulate different substitution patterns, which is visible as GC skew;[^lobry] strand-aware analyses keep all 12 classes.
- **Neighbouring substitutions are not independent.** Two SNVs in the same codon and on the same chromosome act together: `CTT` (Leu) with C>T at position 1 alone gives `TTT` (Phe), but combined with T>A at position 3 gives `TTA`, still Leu (Exercise 4). Annotating each SNV separately mispredicts the protein; phasing decides ([[Haplotype Phasing]]).
- **Ts/Tv as a mixture.** If a fraction $f$ of calls are errors with transition fraction $1/3$ (uniform) and the rest are real with transition fraction $\tau$, the observed fraction is $\tau_{\text{obs}} = (1 - f)\tau + f/3$, hence $f = \dfrac{\tau - \tau_{\text{obs}}}{\tau - 1/3}$ (Exercise 5). The model is only as good as the assumed $\tau$, which can differ between genomic regions (CpG-rich regions carry more C>T hotspots).

## Mathematical representation

- $\Sigma = \{A, C, G, T\}$, purines $R = \{A, G\}$, pyrimidines $Y = \{C, T\}$, complement $c$ ([[Nucleotide#Mathematical representation]]).
- The substitutions are the ordered pairs $(b, b')$ with $b \ne b'$: $4 \times 3 = 12$. Transitions: $\{b, b'\} \subseteq R$ or $\{b, b'\} \subseteq Y$ (4 pairs); transversions: the other 8.
- **Strand equivalence**: $(b, b') \sim (c(b), c(b'))$. Each class has exactly two members, giving 6 classes; the canonical name uses the member with $b \in Y$.
- **Context**: for a substitution at the centre of the trinucleotide $x\,b\,y$, if $b \in R$ use the reverse complement $c(y)\,c(b)\,c(x)$ with $(c(b), c(b'))$. The number of channels is $6 \times 4^2 = 96$.
- **K80 rates**: total rate out of a base $\mu = \alpha + 2\beta$; $P(\text{transition} \mid \text{substitution}) = \dfrac{\alpha}{\alpha + 2\beta} = \dfrac{\kappa}{\kappa + 2}$; uniform case $\kappa = 1$ gives $1/3$.

## Computational representation

A substitution is a triple (position, `REF`, `ALT`); its class and context are computed from the reference sequence.

```python
from collections import Counter

PURINES = set("AG")
COMPLEMENT = str.maketrans("ACGT", "TGCA")


def kind(ref: str, alt: str) -> str:
    """Transition if both bases are purines or both pyrimidines, else transversion."""
    return "Ts" if (ref in PURINES) == (alt in PURINES) else "Tv"


def collapse(ref: str, alt: str, left: str = "", right: str = "") -> str:
    """Name a base-pair change from the pyrimidine (C or T) side, with optional flanking bases."""
    if ref in PURINES:                                   # read the other strand instead
        ref, alt = ref.translate(COMPLEMENT), alt.translate(COMPLEMENT)
        left, right = right.translate(COMPLEMENT), left.translate(COMPLEMENT)
    return f"{left}[{ref}>{alt}]{right}"


# every ordered substitution, grouped by base-pair class
classes = {}
for ref in "ACGT":
    for alt in "ACGT":
        if ref != alt:
            classes.setdefault(collapse(ref, alt), []).append(f"{ref}>{alt} ({kind(ref, alt)})")
for name, members in classes.items():
    print(name, members)

seq = "ACGTTCGAGGCATCGA"                                     # invented toy sequence
mutations = [(2, "T"), (5, "T"), (8, "A"), (11, "G"), (14, "A")]  # (0-based position, new base)
spectrum = Counter(collapse(seq[i], alt, seq[i - 1], seq[i + 1]) for i, alt in mutations)
print(spectrum)
print(Counter(kind(seq[i], alt) for i, alt in mutations))
```

```text
[T>G] ['A>C (Tv)', 'T>G (Tv)']
[T>C] ['A>G (Ts)', 'T>C (Ts)']
[T>A] ['A>T (Tv)', 'T>A (Tv)']
[C>A] ['C>A (Tv)', 'G>T (Tv)']
[C>G] ['C>G (Tv)', 'G>C (Tv)']
[C>T] ['C>T (Ts)', 'G>A (Ts)']
Counter({'T[C>T]G': 2, 'A[C>A]G': 1, 'C[C>T]T': 1, 'A[T>C]G': 1})
Counter({'Ts': 4, 'Tv': 1})
```

## Worked example

> [!example] Five substitutions in a toy sequence (invented)
> Sequence `ACGTTCGAGGCATCGA`, positions 0-based.
>
> | Pos | Context | Change | Class | Collapsed channel |
> |---:|---|---|---|---|
> | 2 | `CGT` | G>T | Tv | `A[C>A]G` |
> | 5 | `TCG` | C>T | Ts | `T[C>T]G` (CpG) |
> | 8 | `AGG` | G>A | Ts | `C[C>T]T` |
> | 11 | `CAT` | A>G | Ts | `A[T>C]G` |
> | 14 | `CGA` | G>A | Ts | `T[C>T]G` (CpG) |
>
> Positions 5 and 14 look different on the given strand (C>T and G>A), but both are C:G → T:A changes at a CpG: position 14 is the G of `CG`, whose partner strand reads `TCG` around the mutated C. After collapsing, they fall in the same channel, the one expected from methyl-CpG deamination.[^alberts] Ts/Tv = 4/1 here, far above the uniform 0.5; with five events this means little, but on thousands of calls it is informative.

## Common misconceptions

> [!warning] "C>T and G>A are two different mutation types"
> They are the same base-pair change seen from the two strands. Only strand-aware questions (replication or transcription direction) keep them apart.[^lobry]

> [!warning] "Transversions should be twice as common as transitions"
> That is the count of possible pathways (8 vs 4), not their rates. Real mutation is transition-biased, so transitions usually dominate.[^freeland]

> [!warning] "Each SNV can be annotated on its own"
> Two substitutions in one codon on the same haplotype change it together; their joint effect can differ from both separate predictions (L3).

## Exercises

> [!question] Exercise 1 (L1)
> For each substitution, give the class (Ts or Tv) and its collapsed name: A>G, C>A, G>T, T>A, G>C, T>C.

> [!success]- Solution
> A>G: Ts, [T>C]. C>A: Tv, [C>A]. G>T: Tv, [C>A]. T>A: Tv, [T>A]. G>C: Tv, [C>G]. T>C: Ts, [T>C]. Purine references (A, G) are renamed from the complementary strand.

> [!question] Exercise 2 (L1)
> An A:T base pair gets a G misincorporated opposite the T during replication, and the mismatch is not repaired. Draw the two following rounds of replication and name the final change.

> [!success]- Solution
> Round 1: the new strand carries G opposite T (a T·G mismatch). Round 2: the G-containing strand templates a C, giving a G:C pair in one granddaughter molecule; the T-containing strand gives the original A:T. Result: A:T → G:C, a transition, in one of the four granddaughter molecules and in all its descendants.

> [!question] Exercise 3 (L2, Python)
> Using `collapse` from the code above, enumerate every substitution in every trinucleotide context (64 trinucleotides x 3 alternative bases), collapse them, and check that there are 96 channels. List the channels of C>T at CpG.

> [!success]- Solution
> ```python
> channels = {collapse(b, alt, x, y)
>             for x in "ACGT" for b in "ACGT" for y in "ACGT" for alt in "ACGT" if alt != b}
> print(len(channels), sorted(channels)[:4])
> print(sorted(ch for ch in channels if ch.endswith("G") and "[C>T]" in ch))
> # 96 ['A[C>A]A', 'A[C>A]C', 'A[C>A]G', 'A[C>A]T']
> # ['A[C>T]G', 'C[C>T]G', 'G[C>T]G', 'T[C>T]G']
> ```
>
> The 192 context-substitutions pair up across the two strands into 96 channels. The four `N[C>T]G` channels hold the C:G → T:A changes at CpG, including those observed as G>A on the given strand, as in the worked example.

> [!question] Exercise 4 (L3, Python)
> The codon `CTT` (Leu) carries two SNVs: C>T at its first position and T>A at its third. Translate the codon with each SNV alone and with both, and explain why phasing matters.

> [!success]- Solution
> ```python
> BASES = "TCAG"
> CODE = dict(zip((a + b + c for a in BASES for b in BASES for c in BASES),
>                 "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"))
>
>
> def apply(codon: str, changes: dict[int, str]) -> str:
>     return "".join(changes.get(i, base) for i, base in enumerate(codon))
>
>
> codon = "CTT"                                        # Leu
> for label, changes in [("SNV 1 alone", {0: "T"}), ("SNV 2 alone", {2: "A"}), ("both, same haplotype", {0: "T", 2: "A"})]:
>     new = apply(codon, changes)
>     print(f"{label:22} {codon} -> {new}: {CODE[codon]} -> {CODE[new]}")
> # SNV 1 alone            CTT -> TTT: L -> F
> # SNV 2 alone            CTT -> CTA: L -> L
> # both, same haplotype   CTT -> TTA: L -> L
> ```
>
> Annotated separately, the first SNV is a Leu → Phe missense. If both SNVs are on the same chromosome, the codon is `TTA`, still Leu: no amino acid change. If they are on different chromosomes, one copy encodes Phe and the other Leu. Only the phase tells which is true.

> [!question] Exercise 5 (L3)
> Suppose (an assumption, not a measured value) that real SNVs in a region have Ts/Tv = 2.0 and that calling errors are uniform substitutions. A call set shows Ts/Tv = 1.5. Estimate the error fraction $f$, and name one reason the estimate could be wrong.

> [!success]- Solution
> $\tau = 2/3$ (Ts/Tv 2.0), $\tau_{\text{obs}} = 1.5 / 2.5 = 0.6$. $f = (2/3 - 0.6)/(2/3 - 1/3) = 0.0667 / 0.3333 = 0.2$: about 20 % of calls would be errors. It could be wrong if the true $\tau$ of the region differs from the assumption (CpG-rich regions, with their C>T hotspots, are more transition-rich), or if errors are not uniform substitutions.

## Mastery checklist

- [ ] 1 Recognized: I can define a point mutation and classify any substitution as a transition or a transversion.
- [ ] 2 Understood: I can explain why 12 substitutions form 6 base-pair classes, how a mismatch becomes a mutation, and which mechanisms produce which class.
- [ ] 3 Practiced: I can derive Ts/Tv from $\kappa$ and compute class and trinucleotide spectra in Python.
- [ ] 4 Applied: I computed the Ts/Tv ratio and 96-channel spectrum of a real VCF and used them to judge its quality.
- [ ] 5 Explained: I can teach the assumptions behind strand collapsing, the pitfalls of annotating neighbouring SNVs separately, and what Ts/Tv can and cannot say about errors.

## References

[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), treatment of gene mutation: point mutations, transitions and transversions, base analogs, alkylating agents, oxidative damage and ultraviolet light.
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of DNA replication fidelity and DNA repair: mismatches, deamination of cytosine and 5-methylcytosine, ultraviolet damage.
[^freeland]: [[Freeland 1998 - The Genetic Code Is One in a Million]], Freeland SJ, Hurst LD, *Journal of Molecular Evolution* 47:238-248, error model weighting transitions and transversions.
[^yang]: [[Molecular Evolution (Yang)]], models of nucleotide substitution (K80 and the transition/transversion rate ratio $\kappa$).
[^lobry]: [[Lobry 1996 - Asymmetric Substitution Patterns in the Two DNA Strands of Bacteria]], *Molecular Biology and Evolution* 13(5):660-665.
[^hts]: [[HTS Format Specifications]], VCF specification (`REF`, `ALT` and genotype encoding).
