---
aliases:
  - Scoring Matrix
  - Amino Acid Substitution Matrix
  - Log-Odds Scoring Matrix
  - PAM and BLOSUM
  - Matrice de substitution
tags:
  - type/concept
  - domain/bioinformatics
  - domain/statistics
  - domain/biology
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Sequence Alignment]]"
  - "[[Sequence Homology]]"
  - "[[Amino Acid]]"
  - "[[Logarithm]]"
  - "[[Conditional Probability]]"
related:
  - "[[Gap Penalty]]"
  - "[[Needleman-Wunsch Algorithm]]"
  - "[[Smith-Waterman Algorithm]]"
  - "[[BLAST]]"
  - "[[E-Value]]"
  - "[[Kullback-Leibler Divergence]]"
  - "[[Markov Chain]]"
  - "[[Transition Matrix]]"
  - "[[Protein Substitution Model]]"
  - "[[Position Weight Matrix]]"
  - "[[Missense Mutation]]"
projects:
  - "[[04-alignment-engine]]"
sources:
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Dayhoff 1978 - A Model of Evolutionary Change in Proteins]]"
  - "[[Henikoff 1992 - Amino Acid Substitution Matrices from Protein Blocks]]"
  - "[[Altschul 1991 - Amino Acid Substitution Matrices from an Information Theoretic Perspective]]"
  - "[[NCBI BLAST]]"
  - "[[Molecular Evolution (Yang)]]"
---

# Substitution Matrix

> [!abstract]
> A substitution matrix scores every pair of residues that can face each other in an alignment; PAM and BLOSUM scores are log-odds, so a positive score means "more frequent in related sequences than by chance", and the matrix you choose sets the evolutionary distance your search sees best.

## Definition

A **substitution matrix** assigns a score $s(a, b)$ to the alignment of residue $a$ with residue $b$; the score of a gapless alignment is the sum over its columns ([[Sequence Alignment]]). Standard matrices are **log-odds** matrices: $s(a, b)$ is proportional to $\log \frac{q_{ab}}{p_a p_b}$, where $q_{ab}$ is the frequency of the pair in alignments of related sequences (the **target frequency**) and $p_a p_b$ the frequency expected by chance from the background residue frequencies.[^durbin] Altschul showed that any substitution matrix is implicitly such a log-odds matrix, with its own target distribution of aligned pairs.[^altschul91] The two classic protein families are **PAM**, extrapolated from closely related proteins with a Markov model,[^dayhoff] and **BLOSUM**, counted directly in conserved blocks of more divergent proteins.[^henikoff]

## Why it matters

- **Every protein alignment uses one.** BLAST+ runs blastp with BLOSUM62 by default (gap costs 11 and 1); its `blastp-short` task, designed for queries shorter than 30 residues, uses PAM30 (gap costs 9 and 1).[^ncbi] [[Needleman-Wunsch Algorithm|Global]] and [[Smith-Waterman Algorithm|local]] aligners take the matrix as a parameter.
- **It decides what you can find.** A matrix is tuned to a divergence level, and a matrix tuned to the wrong one loses sensitivity (Advanced). For database searches Altschul found PAM120 generally more appropriate than PAM250, then the most widely used matrix.[^altschul91]
- **It reads like a biochemistry table.** High scores for I/V, F/Y or K/R mark replacements that proteins tolerate, strongly negative ones replacements rarely accepted; the same intuition helps to judge [[Missense Mutation|missense variants]].
- **Lab.** [[04-alignment-engine]] parses the standard matrix files and plugs them into its aligners. The log-odds logic returns in [[Position Weight Matrix|position weight matrices]] and in the statistics of [[E-Value|E-values]].

## Core (L2)

![[blosum62-heatmap.svg]]

### Reading BLOSUM62

- **Positive, zero, negative.** BLOSUM62 scores are in half-bit units, $s = 2\log_2(\text{odds})$.[^henikoff] So +3 for I/V means the pair is $2^{3/2} \approx 2.8$ times more frequent in aligned blocks of related proteins than by chance, 0 means "as often as chance", and −4 for D/W means 4 times less often.
- **The diagonal is not constant.** Identities score from 4 (A, I, L, S, V) to 11 (W). Since $p_W$ is small, a W/W pair is very unlikely by chance, so finding one is strong evidence; A/A is common in unrelated proteins too.
- **Chemistry shows through.** The best off-diagonal scores are I/V and F/Y (+3), then pairs such as K/R, Q/E, L/M and W/Y (+2): hydrophobic for hydrophobic, aromatic for aromatic, same charge for same charge ([[Amino Acid]]). Grouping residues by side chain, as in the figure, gathers the positive cells into blocks along the diagonal.

### PAM: extrapolating evolution

Dayhoff and colleagues counted accepted point mutations (replacements fixed in evolution) in alignments of closely related proteins, at least 85% identical, and built **PAM1**: replacement probabilities for an evolutionary distance of 1 accepted point mutation per 100 residues.[^dayhoff] Treating each change as independent of earlier ones, a [[Markov Chain]], the matrix for $n$ units is the $n$-th power, PAM$n$ = PAM1$^n$ ([[Transition Matrix]], [[Matrix Multiplication]]); log-odds matrices such as PAM250 serve distant relationships.[^dayhoff] **Higher PAM number, more divergence.**

### BLOSUM: counting divergent blocks

Henikoff and Henikoff counted amino acid pairs directly in about 2,000 ungapped blocks of aligned segments from more than 500 groups of related proteins.[^henikoff] Segments at least X% identical are clustered and count as one, which gives BLOSUM-X: BLOSUM62 clusters segments at least 62% identical, so the replacements it records are those between less similar segments.[^henikoff] **Lower BLOSUM number, more divergence**: BLOSUM45 for distant homologs, BLOSUM80 for close ones. The matrices gave marked improvements in alignments and database searches over those of the time.[^henikoff]

### Choosing a matrix

| Situation | Typical choice | Why |
|---|---|---|
| Very short query (< 30 residues) | PAM30, in BLAST+ `blastp-short`[^ncbi] | much information per position, needed when there are few positions |
| Closely related proteins | BLOSUM80 | built from more similar segments[^henikoff] |
| General database search | BLOSUM62, the blastp default[^ncbi] | the usual compromise |
| Remote homologs, long alignments | BLOSUM45, PAM250 | built for, or extrapolated to, large distances[^henikoff][^dayhoff] |

Both families point the same way: distant relatives call for a low BLOSUM or high PAM number, close ones for a high BLOSUM or low PAM number. Nucleotide alignments often use plain match/mismatch scores ([[Sequence Alignment]]); such a pair of numbers is also an implicit log-odds matrix,[^altschul91] one that treats every mismatch alike.

## Advanced (L3)

### Relative entropy: information per aligned pair

In true alignments, pairs occur with the target frequencies $q_{ab}$, so the average score per aligned pair, in bits, is

$$H = \sum_{a,b} q_{ab} \log_2 \frac{q_{ab}}{p_a p_b},$$

the [[Kullback-Leibler Divergence|relative entropy]] of the target distribution with respect to chance. This information view, scores in bits and matrices adapted to different purposes, is Altschul's.[^altschul91] The standard matrix files print their units and $H$ in their headers (Computational representation):

| Matrix | Units | $H$ (bits per pair) | Pairs for 30 bits, $30/H$ |
|---|---|---|---|
| PAM30 | 1/2 bit | 2.57 | 12 |
| BLOSUM80 | 1/3 bit | 0.9868 | 30 |
| BLOSUM62 | 1/2 bit | 0.6979 | 43 |
| BLOSUM45 | 1/3 bit | 0.3795 | 79 |
| PAM250 | 1/3 bit | 0.354 | 85 |

The last column is the number of aligned positions an average true alignment needs to accumulate 30 bits, an illustrative threshold (real thresholds depend on the search space, see [[E-Value]]). A 15-residue peptide cannot reach it with BLOSUM62; with PAM30 it can, if its match is close, which is why short queries get high-entropy matrices.[^ncbi]

### The matched matrix wins

Suppose true homologs have target frequencies $q$ and you score them with a matrix built for $q'$. The expected score per pair in bits is

$$\sum_{a,b} q_{ab} \log_2 \frac{q'_{ab}}{p_a p_b} = H(q) - D_{\mathrm{KL}}(q \,\|\, q') \le H(q),$$

with equality only when $q' = q$ (Gibbs' inequality): the matrix built for the right divergence accumulates evidence fastest. A toy 4-letter "PAM" model (uniform bases, 1% change per step, PAM$n$ = $n$ steps) makes it concrete. Rows are the true divergence $n$ with the resulting identity, columns the matrix used:

```text
n    id    expected score per pair with the matrix built for n' = (10, 50, 100, 250)
10   0.91   1.400   1.117   0.715   0.125
50   0.63   0.079   0.471   0.369   0.072
100  0.45  -0.830   0.026   0.130   0.036
250  0.28  -1.654  -0.377  -0.086   0.003
random pairs: [-1.78, -0.439, -0.119, -0.003]
```

Each row peaks on the diagonal. A matrix built for close sequences ($n' = 10$) even gives true homologs at $n = 100$ a negative expected score: they become invisible. Every matrix gives random pairs a negative expected score, the condition local alignment needs ([[Smith-Waterman Algorithm]]).[^durbin] And after 250 steps this 4-letter model keeps only 28% identity, barely above the 25% of chance: almost no information is left.

## Frontier (M1)

- **From scoring matrices to evolutionary models.** PAM's one-step matrix and its powers form a discrete-time Markov chain.[^dayhoff] Phylogenetics works instead with continuous-time rate matrices $Q$, transition probabilities $P(t) = e^{Qt}$ and empirical amino acid models estimated from large data sets ([[Protein Substitution Model]], [[Continuous-Time Markov Chain]], [[Matrix Exponential]]).[^yang]
- **One matrix for all positions is a simplification.** A matrix averages over all positions of many proteins, while the constraint on a residue depends on its site. Position-specific scores estimated from a family alignment replace the single matrix in [[PSI-BLAST]] and in [[Profile Hidden Markov Model|profile HMMs]].[^durbin5]
- **Background composition matters.** Log-odds scores assume background frequencies $p$; sequences of very biased composition break that assumption, one reason to mask [[Low-Complexity Region|low-complexity regions]] before searching.

## Mathematical representation

- Alphabet $\Sigma$ (20 amino acids), background frequencies $p_a$, symmetric target frequencies $q_{ab}$ with $\sum_{a,b} q_{ab} = 1$.
- **Log-odds score** with scale $\lambda > 0$: $s(a, b) = \frac{1}{\lambda}\ln\frac{q_{ab}}{p_a p_b}$, rounded to integers. Half-bit units mean $\lambda = \frac{\ln 2}{2}$, so $\text{odds} = 2^{s/2}$.
- **Every matrix is log-odds.** Let $f(\lambda) = \sum_{a,b} p_a p_b e^{\lambda s(a,b)}$. Then $f(0) = 1$, $f'(0) = \sum p_a p_b\, s(a,b) = E < 0$ if the expected score is negative, $f$ is convex, and $f(\lambda) \to \infty$ if some $s(a,b) > 0$. Hence a unique $\lambda > 0$ solves $f(\lambda) = 1$, and $q_{ab} = p_a p_b e^{\lambda s(a,b)}$ are the target frequencies the matrix implicitly assumes.[^altschul91]
- **Alignment score.** For an ungapped alignment $x, y$ of length $L$, $\lambda S = \lambda \sum_i s(x_i, y_i) = \ln \frac{\prod_i q_{x_i y_i}}{\prod_i p_{x_i} p_{y_i}}$, the log-likelihood ratio "related versus unrelated" when columns are independent.[^durbin]
- **PAM.** One-step matrix $M_{ab} = P(b \mid a)$; $n$ steps: $M^n$; target $q^{(n)}_{ab} = p_a (M^n)_{ab}$, so $s_n(a, b) = \frac{1}{\lambda}\ln\frac{(M^n)_{ab}}{p_b}$.
- **Expected score on random pairs** (in nats): $\lambda E = \sum_{a,b} p_a p_b \ln\frac{q_{ab}}{p_a p_b} = -D_{\mathrm{KL}}(p \otimes p \,\|\, q) \le 0$.
- **Toy model.** Uniform 4-letter background, change probability $\mu$ per step spread evenly over the 3 other bases: $M = (1-\mu) I + \frac{\mu}{3}(J - I)$, with eigenvalues $1$ and $1 - \frac{4\mu}{3}$, so $P_n(\text{same}) = \frac{1}{4} + \frac{3}{4}\left(1 - \frac{4\mu}{3}\right)^n$, match score $\log_2\big(4 P_n(\text{same})\big)$ and mismatch score $\log_2\big(\tfrac{4}{3}(1 - P_n(\text{same}))\big)$.

## Computational representation

A matrix file has a header row and one row per residue; the 20 standard amino acids of BLOSUM62, with the values of the NCBI file, parse into a dictionary keyed by pairs:

```python
BLOSUM62 = """\
     A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V
A    4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0
R   -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3
N   -2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3
D   -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3
C    0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1
Q   -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2
E   -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2
G    0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3
H   -2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3
I   -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3
L   -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1
K   -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2
M   -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1
F   -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1
P   -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2
S    1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2
T    0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0
W   -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3
Y   -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1
V    0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4
"""

def parse_matrix(text: str) -> dict[tuple[str, str], int]:
    """Parse a square score table in the NCBI layout (header row, then one row per residue)."""
    rows = [line.split() for line in text.splitlines() if line.strip()]
    header = rows[0]
    return {(row[0], col): int(v) for row in rows[1:] for col, v in zip(header, row[1:])}

B62 = parse_matrix(BLOSUM62)
AA = "ARNDCQEGHILKMFPSTWYV"
assert len(B62) == 400 and all(B62[x, y] == B62[y, x] for x, y in B62)   # symmetric

def ungapped_score(a: str, b: str, m) -> int:
    return sum(m[x, y] for x, y in zip(a, b))

def odds_ratio(score: int, bits_per_unit: float = 0.5) -> float:
    """BLOSUM62 is in half-bit units: s = 2 log2(odds), so odds = 2 ** (s / 2)."""
    return 2 ** (score * bits_per_unit)

diagonal = sorted((B62[x, x], x) for x in AA)
pairs = sorted((B62[x, y], x + y) for i, x in enumerate(AA) for y in AA[i + 1:])
print("identities, lowest and highest:", diagonal[:3], diagonal[-3:])
print("best substitutions:", pairs[-6:][::-1])
print("worst substitutions:", pairs[:4])
q, s = "KIVDF", "RVIEY"                        # invented: no identical residue
print(ungapped_score(q, s, B62), [B62[x, y] for x, y in zip(q, s)])
print([round(odds_ratio(v), 2) for v in (3, 0, -4, 11)])
```

```text
identities, lowest and highest: [(4, 'A'), (4, 'I'), (4, 'L')] [(8, 'H'), (9, 'C'), (11, 'W')]
best substitutions: [(3, 'IV'), (3, 'FY'), (2, 'WY'), (2, 'RK'), (2, 'QE'), (2, 'LM')]
worst substitutions: [(-4, 'CE'), (-4, 'DL'), (-4, 'DW'), (-4, 'FP')]
13 [2, 3, 3, 2, 3]
[2.83, 1.0, 0.25, 45.25]
```

The toy table of the Advanced section, standard library only:

```python
import math

def pam_like(n: int, p1: float = 0.01) -> tuple[float, float, float]:
    """Return P(identical after n steps), match and mismatch log-odds scores in bits."""
    same = 0.25 + 0.75 * (1 - 4 * p1 / 3) ** n
    return same, math.log2(4 * same), math.log2(4 * (1 - same) / 3)

ns = (10, 50, 100, 250)
print("n    id    expected score per pair with the matrix built for n' =", ns)
for n in ns:
    same = pam_like(n)[0]
    row = [same * pam_like(k)[1] + (1 - same) * pam_like(k)[2] for k in ns]
    print(f"{n:<4} {same:.2f}  " + "  ".join(f"{x:6.3f}" for x in row))
print("random pairs:", [round(0.25 * pam_like(k)[1] + 0.75 * pam_like(k)[2], 3) for k in ns])
```

Once the parser is yours, [[Biopython]] loads the same files, whose header lines state units and relative entropy (Biopython 1.85):

```python
import os
from Bio.Align import substitution_matrices

folder = os.path.join(os.path.dirname(substitution_matrices.__file__), "data")
for name in ("PAM30", "BLOSUM80", "BLOSUM62", "BLOSUM45", "PAM250"):
    with open(os.path.join(folder, name)) as handle:
        notes = [line.strip("# \n") for line in handle if line.startswith("#")]
    print(f"{name:9s}", [n for n in notes if "Entropy" in n or "Units" in n or "scale" in n])
pam250 = substitution_matrices.load("PAM250")
blosum62 = substitution_matrices.load("BLOSUM62")
for x, y in (("W", "W"), ("F", "Y"), ("W", "C")):
    print(x, y, int(blosum62[x][y]), int(pam250[x][y]))
```

```text
PAM30     ['PAM 30 substitution matrix, scale = ln(2)/2 = 0.346574', 'Expected score = -5.06, Entropy = 2.57 bits']
BLOSUM80  ['BLOSUM Clustered Scoring Matrix in 1/3 Bit Units', 'Entropy =   0.9868, Expected =  -0.7442']
BLOSUM62  ['BLOSUM Clustered Scoring Matrix in 1/2 Bit Units', 'Entropy =   0.6979, Expected =  -0.5209']
BLOSUM45  ['BLOSUM Clustered Scoring Matrix in 1/3 Bit Units', 'Entropy =   0.3795, Expected =  -0.2789']
PAM250    ['PAM 250 substitution matrix, scale = ln(2)/3 = 0.231049', 'Expected score = -0.844, Entropy = 0.354 bits']
W W 11 17
F Y 3 7
W C -2 -8
```

Every header reports a negative expected score, as the Mathematical representation requires.

## Worked example

> [!example] Zero identity, strong similarity (invented peptides)
> ```text
> query     K   I   V   D   F
> subject   R   V   I   E   Y
> BLOSUM62 +2  +3  +3  +2  +3    total +13
> ```
> 1. **Identity**: no position is identical, so 0% identity, and a +1/−1 match/mismatch scheme would score −5.
> 2. **Similarity**: every pair is a conservative replacement: K/R (basic), I/V and V/I (aliphatic), D/E (acidic), F/Y (aromatic). BLOSUM62 scores them +2 or +3, total +13.
> 3. **In bits**: 13 half-bits = 6.5 bits, an odds ratio of $2^{6.5} \approx 90$ in favour of "related" over "chance" for this segment, if columns are independent.
> 4. **Contrast**: against the invented subject `WGPKC`, the same query scores −3, −4, −2, −1, −2, total −12: radical replacements are evidence *against* relatedness.
> 5. **Caution**: five positions are far too few for significance in a database search ([[E-Value]]); the example shows how similarity is graded, not that these peptides are homologs.

## Common misconceptions

> [!warning] "A higher score means two amino acids are more alike"
> A score compares an observed pair frequency with chance. W/W scores 11 and A/A 4 not because tryptophans are "more identical" but because a W/W pair is far less likely by chance.

> [!warning] "PAM250 means 250% difference" (or "PAM$n$ means $n$% difference")
> PAM counts accepted mutations per 100 residues, and repeated changes at the same site hide each other, so the observed difference grows ever more slowly. In the toy 4-letter model, identity is still 28% after 250 steps (Exercise 4).

> [!warning] "Scores can be compared across matrices"
> Units differ: BLOSUM62 is in half bits, BLOSUM45 and PAM250 in third bits. W/W is 11 in BLOSUM62 and 17 in PAM250, that is 5.5 and 5.7 bits, nearly the same evidence. Convert to bits first.

> [!warning] "BLOSUM62 comes from sequences 62% identical"
> Segments at least 62% identical are clustered and counted once, so the counted pairs come from less similar segments.[^henikoff] And a higher BLOSUM number means *closer* sequences, the opposite of PAM.

## Exercises

> [!question] Exercise 1 (L2)
> In BLOSUM62, which is more favourable, L/I or L/W? Convert both scores to odds ratios.

> [!success]- Solution
> L/I = +2, L/W = −2. In half bits, odds = $2^{s/2}$: $2^{1} = 2$ (twice as frequent as chance in related proteins) and $2^{-1} = 0.5$ (half as frequent). Two hydrophobic aliphatic residues replace each other easily; a bulky aromatic W rarely replaces L.

> [!question] Exercise 2 (L2)
> Choose a matrix and justify: (a) a 12-residue peptide from a mass spectrometry run, searched against a protein database; (b) two orthologous proteins of human and mouse that look highly identical; (c) a bacterial protein with suspected distant homologs in eukaryotes.

> [!success]- Solution
> (a) PAM30: a short query needs a high-entropy matrix, and BLAST+ uses it in `blastp-short` for queries under 30 residues.[^ncbi] (b) BLOSUM80, built from more similar segments (BLOSUM62 also works). (c) BLOSUM45 or PAM250, low-entropy matrices for distant relationships; if they fail, profile methods ([[PSI-BLAST]]).

> [!question] Exercise 3 (L3, Python)
> Assume uniform background frequencies (a simplification). Compute the expected BLOSUM62 score of two random residues. Why must it be negative for local alignment?

> [!success]- Solution
> With $p_a = 1/20$, $E = \frac{1}{400}\sum_{a,b} s(a,b)$:
> ```python
> print(round(sum(B62.values()) / 400, 3), "half bits")
> ```
> Output: `-1.065 half bits`. The header of the BLOSUM62 file also reports a negative expected score. If $E$ were positive, the score of an alignment of unrelated sequences would grow with its length, and a local alignment would extend over everything instead of isolating the related segment.[^durbin]

> [!question] Exercise 4 (L3)
> In the toy model with $\mu = 0.01$, after how many steps is the identity 50%? What does that say about "PAM $n$ = $n$% difference"?

> [!success]- Solution
> Solve $\frac14 + \frac34 x^n = \frac12$ with $x = 1 - \frac{4\mu}{3}$: $x^n = \frac13$, so $n = \frac{\ln(1/3)}{\ln(1 - 0.04/3)}$. In Python, `math.log(1 / 3) / math.log(1 - 4 * 0.01 / 3)` gives 81.8. About 82 changes per 100 sites leave only 50% of sites different: multiple hits make the observed difference lag behind the number of changes, ever more as $n$ grows.

> [!question] Exercise 5 (M1)
> Prove that for any log-odds matrix with target $q$, (a) the expected score of random pairs is $\le 0$, and (b) scoring true pairs of target $q$ with a matrix built for $q'$ gives at most $H(q)$, with equality iff $q' = q$.

> [!success]- Solution
> (a) $\lambda E = \sum p_a p_b \ln\frac{q_{ab}}{p_a p_b} \le \ln \sum p_a p_b \frac{q_{ab}}{p_a p_b} = \ln 1 = 0$ by Jensen's inequality (concavity of $\ln$), with equality iff $q = p \otimes p$, a matrix of zeros. (b) $\sum q \log_2\frac{q'}{pp} = \sum q \log_2\frac{q}{pp} - \sum q \log_2 \frac{q}{q'} = H(q) - D_{\mathrm{KL}}(q\,\|\,q')$, and $D_{\mathrm{KL}} \ge 0$ with equality iff $q' = q$ (Gibbs' inequality, [[Kullback-Leibler Divergence]]).

## Mastery checklist

- [ ] 1 Recognized: I can say what a substitution matrix is and name PAM and BLOSUM with the meaning of their numbers.
- [ ] 2 Understood: I can read a BLOSUM62 score as a log-odds ratio in half bits and explain how PAM and BLOSUM are built.
- [ ] 3 Practiced: I can parse a matrix file, score alignments with it and convert scores to bits and odds.
- [ ] 4 Applied: in [[04-alignment-engine]], I compared alignments and search results of real proteins with PAM30, BLOSUM62 and BLOSUM45 and explained the differences.
- [ ] 5 Explained: I can derive relative entropy, show why the matched matrix maximizes the expected score, and explain why short queries need high-entropy matrices.

## References

[^durbin]: [[Biological Sequence Analysis (Durbin)]], ch. 2 "Pairwise alignment" (log-odds substitution scores, local alignment and the negative expected score).
[^durbin5]: [[Biological Sequence Analysis (Durbin)]], ch. 5 "Profile HMMs for sequence families".
[^dayhoff]: [[Dayhoff 1978 - A Model of Evolutionary Change in Proteins]], *Atlas of Protein Sequence and Structure* 5(3):345-352.
[^henikoff]: [[Henikoff 1992 - Amino Acid Substitution Matrices from Protein Blocks]], *PNAS* 89(22):10915-10919; BLOSUM62 values as in the matrix file distributed with Biopython.
[^altschul91]: [[Altschul 1991 - Amino Acid Substitution Matrices from an Information Theoretic Perspective]], *Journal of Molecular Biology* 219(3):555-565.
[^ncbi]: [[NCBI BLAST]], BLAST+ command-line manual, parameter table of the blastp and blastp-short tasks.
[^yang]: [[Molecular Evolution (Yang)]], models of amino acid substitution.
