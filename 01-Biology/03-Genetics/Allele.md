---
aliases:
  - Alleles
  - Allèle
  - Reference Allele
  - Alternate Allele
  - Wild-Type Allele
  - REF and ALT
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Gene]]"
  - "[[Chromosome]]"
  - "[[Ploidy]]"
related:
  - "[[Genotype]]"
  - "[[Mutation]]"
  - "[[Allele Frequency]]"
  - "[[Haplotype]]"
  - "[[Single Nucleotide Polymorphism]]"
  - "[[Indel]]"
  - "[[Dominance]]"
  - "[[Variant Normalization]]"
  - "[[Star Allele]]"
projects:
  - "[[03-genome-diff]]"
  - "[[07-evolution-simulator]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[GA4GH hts-specs]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
---

# Allele

> [!abstract]
> Alleles are the different versions of the same gene, or of the same DNA position, that can occupy one locus: yellow or green pods, an A or a G at a given base.

## Definition

An **allele** is one of two or more alternative forms of a gene, occupying the same locus on homologous chromosomes.[^os12] Alleles differ in their DNA sequence; they arise by [[Mutation|mutation]], and the form found in nature or in the standard laboratory strain is called the **wild type**, the others **mutant** alleles.[^griffiths] At the molecular level the word applies to any site or segment: the different sequences observed at one position (an A or a G at a single base, a sequence with or without an insertion) are the alleles of that site. Sequencing files list them as the **reference allele** (`REF`, the sequence of the reference genome) and one or more **alternative alleles** (`ALT`).[^hts]

## Why it matters

- **A variant record is a list of alleles.** In [[VCF Format]], `REF` and `ALT` define the alleles of a site, numbered 0 (REF), 1 (first ALT), 2 (second ALT) and so on; every genotype of the file refers to these numbers ([[Genotype]]).[^hts]
- **Population genetics counts alleles.** [[Allele Frequency]], [[Hardy-Weinberg Equilibrium]], [[Genetic Drift]] and GWAS effect sizes are all statements about alleles ([[07-evolution-simulator]], [[Genome-Wide Association Study]]).
- **Comparing sequences produces alleles.** [[03-genome-diff]] reports, for each difference between a reference and a sample, the reference and the sample alleles; the same change can be written in several ways, which must be reconciled ([[Variant Normalization]]).
- **Clinical names are alleles.** In pharmacogenomics, named alleles of drug-metabolism genes combine several variants on one chromosome ([[Star Allele]], [[Haplotype]]).

## Core (L1)

**Gene, locus, allele.** A [[Gene]] sits at a **locus**, a fixed position on a [[Chromosome]]. Homologous chromosomes carry the same loci, so a diploid individual carries **two alleles of each gene**, one per homolog, identical (homozygous) or different (heterozygous) ([[Genotype]]).[^os12] In Mendel's peas, the gene for pod colour has a "yellow" allele and a "green" allele.[^os12]

**Many alleles in a population.** One individual carries at most as many alleles per locus as its [[Ploidy]] allows (two in a diploid), but a population can carry many alleles of the same gene.[^os12][^griffiths] Which of them are more common is a question of [[Allele Frequency]], not of [[Dominance]].

**Alleles at the DNA level.** Six chromosomes (from three invented diploid individuals) aligned to an invented reference:

```text
position        1234567890123
reference       ACGTTAGCCTGAA
chromosome 1    ACGTTAGCCTGAA
chromosome 2    ACGTCAGCCTGAA
chromosome 3    ACGTCAGCCAGAA
chromosome 4    ACGTTAGCCAGAA
chromosome 5    ACGTCAGCCTGAA
chromosome 6    ACGTCAGCCTGAA
                    ^    ^
                    5    10
```

Site 5 has two alleles, T (the reference) and C; site 10 has T (the reference) and A. Every other site has a single allele in this sample. Each chromosome carries one allele per site; the combination it carries along the region (T-T, C-T, C-A...) is a [[Haplotype]].

## Deeper (L2)

### Alleles in a VCF record

A record lists the alleles of one site: `REF` is the reference sequence at that position, `ALT` a comma-separated list of alternative sequences.[^hts]

```text
#CHROM  POS  ID  REF  ALT    (invented records)
chr1    5    .   T    C      biallelic SNV: allele 0 = T, allele 1 = C
chr1    10   .   T    A,G    multiallelic: 0 = T, 1 = A, 2 = G
chr2    31   .   CAT  C      deletion: 0 = CAT, 1 = C
```

For insertions and deletions, both alleles share the first (anchor) base, as in the third record: the event is the loss of `AT` after the `C` ([[Indel]]).[^hts]

### Reference, alternative, minor, ancestral

These words answer different questions:

| Term | Defined by | Example at site 5 above |
|---|---|---|
| reference allele | the base in the reference assembly | T |
| alternative allele | any other observed allele | C |
| minor allele | the less frequent allele in a given sample or population | T (2 of 6 chromosomes) |
| ancestral allele | the allele present before the mutation, inferred by comparing related species | needs an outgroup sequence |

The reference allele is simply what one assembled genome carries: T2T-CHM13, for instance, comes from a single, essentially homozygous cell line.[^nurk] It can be the minor allele, as here, and it says nothing about health or function.

### Gene-level alleles are haplotypes

A named allele of a gene, such as a "wild type" versus a "mutant" allele, is a whole sequence: the combination of site alleles on one chromosome across the gene. Two people can share the same allele at each of two sites and still carry different gene-level alleles if the sites are combined differently on their chromosomes ([[Haplotype]], [[Haplotype Phasing]]).

## Advanced (L3)

- **One allele, several spellings.** In a repeat, deleting one unit at different positions gives the same chromosome sequence: in `GGCACACAT`, deleting the first, second or third `CA` yields `GGCACAT`. Different tools may therefore report the same allele at different positions. **Normalization** picks one representation, conventionally the leftmost with the shortest alleles, so that alleles can be compared across files (code below, [[Variant Normalization]]).
- **Multiallelic sites.** A site with `ALT` = `A,G` can be kept as one record or split into two biallelic records; the choice changes allele numbering and counts, so pipelines fix a convention ([[Variant Normalization]]).
- **Reference bias.** A read carrying the alternative allele differs from the reference by at least one more base than a read carrying the reference allele. An aligner that penalizes mismatches is therefore slightly more likely to misplace or discard it, which can pull allele counts toward the reference allele ([[Read Mapping]]). This is one motivation for graph and [[Pangenome]] references that contain several alleles.
- **Alleles as the unit of evolution.** Mutation creates alleles; drift and selection change their frequencies; the neutral and selective fates of new alleles are the subject of [[Fixation Probability]] and [[Molecular Evolution]].

## Mathematical representation

- A locus $\ell$ is a position (or interval) $(c, p)$ on chromosome $c$. Its allele set is $\mathcal{A}_\ell = \{a_0, a_1, \dots, a_m\}$, with $a_0$ the reference sequence at $\ell$ and $a_1, \dots, a_m$ the alternative sequences, in the order of the `ALT` field; alleles are referred to by their index $i \in \{0, \dots, m\}$.
- **Applying an allele.** For a reference sequence $s$ and an allele $a_i$ at 1-based position $p$ replacing $a_0$, the resulting chromosome sequence is
$$s^{(i)} = s[1..p-1]\; a_i \; s[p + |a_0| .. |s|].$$
- **Equivalence.** Two records $(p, a_0, a_i)$ and $(p', a_0', a_j')$ describe the same allele if and only if they produce the same sequence: $s^{(i)} = s'^{(j)}$. Normalization chooses the representative with the smallest $p$ and shortest alleles in each equivalence class.
- **Allele counts.** In a sample of $N$ individuals of ploidy $k$ there are $kN$ allele copies at a locus; the count $n_i$ of allele $a_i$ satisfies $\sum_i n_i = kN$, and $n_i / kN$ is its sample frequency ([[Allele Frequency]]).

## Computational representation

```python
REFERENCE = "GGCACACATTAGC"          # invented toy reference, positions 1..13


def alleles(ref: str, alt: str) -> list[str]:
    """VCF-style allele list: index 0 is REF, then the comma-separated ALT alleles."""
    return [ref] + ([] if alt == "." else alt.split(","))


def apply(seq: str, pos: int, ref: str, allele: str) -> str:
    """Sequence of a chromosome carrying `allele` instead of `ref` at 1-based `pos`."""
    if seq[pos - 1:pos - 1 + len(ref)] != ref:
        raise ValueError(f"REF {ref} does not match the reference at {pos}")
    return seq[:pos - 1] + allele + seq[pos - 1 + len(ref):]


def normalize(seq: str, pos: int, ref: str, alt: str) -> tuple[int, str, str]:
    """Leftmost, shortest representation of a biallelic variant (VCF anchor base kept)."""
    while ref[-1] == alt[-1] and not (len(ref) == 1 and len(alt) == 1):
        ref, alt = ref[:-1], alt[:-1]              # trim a shared last base...
        if not ref or not alt:                     # ...and re-anchor on the base to the left
            pos -= 1
            ref, alt = seq[pos - 1] + ref, seq[pos - 1] + alt
    while len(ref) > 1 and len(alt) > 1 and ref[0] == alt[0]:
        ref, alt, pos = ref[1:], alt[1:], pos + 1  # trim a shared first base
    return pos, ref, alt


print(alleles("A", "G,T"), alleles("CAT", "C"))
print(apply(REFERENCE, 9, "T", "G"))
# Three ways of writing the deletion of one "CA" unit from the CACACA repeat
for record in [(2, "GCA", "G"), (4, "ACA", "A"), (6, "ACA", "A")]:
    print(record, apply(REFERENCE, *record), normalize(REFERENCE, *record))
```

```text
['A', 'G', 'T'] ['CAT', 'C']
GGCACACAGTAGC
(2, 'GCA', 'G') GGCACATTAGC (2, 'GCA', 'G')
(4, 'ACA', 'A') GGCACATTAGC (2, 'GCA', 'G')
(6, 'ACA', 'A') GGCACATTAGC (2, 'GCA', 'G')
```

The three records look different but produce the same sequence and normalize to the same record. This simplified `normalize` assumes the variant does not start at position 1; production tools handle that edge and multiallelic records.

## Worked example

> [!example] Alleles, counts and the reference in the toy alignment
> Using the six invented chromosomes of Core (three diploid individuals: chromosomes 1-2, 3-4, 5-6):
> 1. **Site 5.** Alleles T (REF, index 0) and C (ALT, index 1). Counts: T on chromosomes 1 and 4, C on 2, 3, 5, 6: $n_0 = 2$, $n_1 = 4$, total $2N = 6$. The reference allele is the minor allele, frequency $2/6 \approx 0.33$.
> 2. **Site 10.** Alleles T (REF) and A (ALT). A is on chromosomes 3 and 4, both in individual 2: frequency $2/6$, and individual 2 is homozygous A/A while individuals 1 and 3 are T/T ([[Genotype]]).
> 3. **Haplotypes.** Along both sites, the chromosomes carry T-T, C-T, C-A, T-A, C-T, C-T: four different combinations of two biallelic sites, the maximum possible ($2^2$) ([[Haplotype]]).
> 4. **VCF.** Site 5 becomes `chr1 5 . T C`, and site 10 `chr1 10 . T A` (toy chromosome name).

## Common misconceptions

> [!warning] "The reference allele is the normal allele"
> REF is the base of one assembled genome, chosen as a coordinate system.[^nurk] It can be rare in the population (site 5 above), and it can even be a disease-associated allele.

> [!warning] "An allele is a mutation"
> Every version of a gene is an allele, including the wild type.[^griffiths] "Mutant" or "alternative" describes a comparison, not a kind of allele.

> [!warning] "A gene has two alleles"
> A diploid individual carries at most two alleles per locus, but a population can carry many.[^os12] VCF numbers the alternative alleles of a multiallelic site 1, 2, 3 and so on.[^hts]

> [!warning] "Dominant alleles are the most common"
> Dominance describes which phenotype a heterozygote shows ([[Dominance]]); frequency describes how common an allele is in a population ([[Allele Frequency]]). The two are independent: a dominant allele can be rare.

## Exercises

> [!question] Exercise 1 (L1)
> Distinguish gene, locus and allele in one sentence each. How many alleles of one gene can (a) one diploid person, (b) a population of 1,000 diploid people carry at most?

> [!success]- Solution
> Gene: a DNA sequence encoding a functional product. Locus: its position on a chromosome. Allele: one version of the sequence at that locus. (a) Two, one per homolog. (b) Up to 2,000 in principle, one per chromosome copy; in practice far fewer distinct alleles, since most copies share alleles.

> [!question] Exercise 2 (L1)
> In the toy alignment of Core, which alleles does individual 3 (chromosomes 5 and 6) carry at sites 5 and 10? Is individual 1 homozygous or heterozygous at each site?

> [!success]- Solution
> Individual 3: C and C at site 5 (homozygous), T and T at site 10 (homozygous). Individual 1 (chromosomes 1 and 2): T and C at site 5 (heterozygous), T and T at site 10 (homozygous).

> [!question] Exercise 3 (L2)
> A VCF record reads `chr3 500 . G A,T`. List the alleles with their indices. What do the genotypes `0/2` and `1/2` mean for a diploid sample?

> [!success]- Solution
> 0 = G (REF), 1 = A, 2 = T.[^hts] `0/2`: one chromosome carries G, the other T. `1/2`: one carries A, the other T; this sample carries no reference allele at this site, although it is heterozygous ([[Genotype]]).

> [!question] Exercise 4 (L3, Python)
> With `apply` and `normalize` from the code above, show that the insertions `(2, "G", "GCA")`, `(4, "A", "ACA")` and `(8, "A", "ACA")` on `REFERENCE` describe the same allele, and give its normalized form. Then check that a SNV is left unchanged by `normalize`.

> [!success]- Solution
> ```python
> insertions = [(2, "G", "GCA"), (4, "A", "ACA"), (8, "A", "ACA")]
> print({apply(REFERENCE, *r) for r in insertions})
> print({normalize(REFERENCE, *r) for r in insertions})
> print(normalize(REFERENCE, 9, "T", "G"), normalize(REFERENCE, 9, "TT", "GT"))
> ```
> Output: `{'GGCACACACATTAGC'}`, then `{(2, 'G', 'GCA')}`, then `(9, 'T', 'G') (9, 'T', 'G')`. All three insertions add one `CA` unit to the repeat and produce one sequence; the leftmost representation inserts `CA` after position 2. The SNV is already normalized, and the padded form `TT > GT` is trimmed back to it.

> [!question] Exercise 5 (L3)
> In a sample, 30 reads cover a heterozygous site. Reads carrying the ALT allele have one extra mismatch against the reference, and the aligner discards 10% of reads with that many mismatches (and none of the REF reads). What ALT fraction do you expect instead of 0.5? Name one way to reduce the bias.

> [!success]- Solution
> Of 15 expected ALT reads, 1.5 are lost: expected fraction $13.5 / 28.5 \approx 0.47$ instead of 0.5. The shortfall is small at one site but systematic across the genome, and it grows for alleles that differ more from the reference (indels, clustered SNVs). Remedies include aligners and references that contain the alternative alleles ([[Pangenome]]) or realigning reads around candidate indels ([[Variant Calling]]).

## Mastery checklist

- [ ] 1 Recognized: I can define allele, locus, wild type, REF and ALT.
- [ ] 2 Understood: I can explain why a diploid carries two alleles per locus while a population carries many, and the difference between reference, minor and ancestral alleles.
- [ ] 3 Practiced: I can read allele lists from VCF records, apply an allele to a reference sequence and normalize an indel.
- [ ] 4 Applied: in [[03-genome-diff]], I report each difference as REF and ALT alleles in normalized VCF form; in [[07-evolution-simulator]], I track allele counts across generations.
- [ ] 5 Explained: I can explain allele representation pitfalls (repeats, multiallelic sites, reference bias) and why the reference allele carries no biological meaning.

## References

[^os12]: [[Biology 2e (OpenStax)]], ch. 12 "Mendel's Experiments and Heredity" (alleles, homozygous and heterozygous, Mendel's pod colour).
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), treatment of alleles, wild-type and mutant alleles, and multiple alleles.
[^hts]: [[GA4GH hts-specs]], VCF specification (`REF`, `ALT` and allele indices in `GT`).
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science* (T2T-CHM13, a single essentially homozygous genome).
