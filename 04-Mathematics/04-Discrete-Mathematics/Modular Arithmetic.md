---
aliases:
  - Congruence
  - Modulo
  - Mod
  - Residue Class
  - Clock Arithmetic
  - Arithmétique modulaire
tags:
  - type/concept
  - domain/mathematics
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Binary Relation]]"
  - "[[Function]]"
related:
  - "[[Reading Frame]]"
  - "[[Hash Function]]"
  - "[[Rolling Hash]]"
  - "[[Rabin-Karp Algorithm]]"
  - "[[K-mer]]"
  - "[[Genomic Coordinate System]]"
  - "[[Plasmid]]"
  - "[[Mitochondrial DNA]]"
projects:
  - "[[02-sequence-translation]]"
  - "[[05-sequence-search]]"
sources:
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[MIT 6.042J - Mathematics for Computer Science]]"
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]]"
  - "[[Anderson 1981 - Sequence and Organization of the Human Mitochondrial Genome]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
---

# Modular Arithmetic

> [!abstract]
> Modular arithmetic computes with remainders: positions repeat every 3 bases in a reading frame and every $G$ bases around a circular genome, and hashes of k-mers stay small because every sum and product can be reduced modulo a fixed number.

## Definition

Fix an integer $m \ge 1$, the **modulus**. Two integers are **congruent modulo $m$**, written $a \equiv b \pmod m$, if $m$ divides $a - b$. By the division theorem, every integer $a$ can be written uniquely as $a = qm + r$ with $0 \le r < m$; the remainder $r$ is written $a \bmod m$, and $a \equiv b \pmod m$ exactly when $a \bmod m = b \bmod m$. Congruence modulo $m$ is an equivalence relation ([[Binary Relation]]) with $m$ classes, the **residue classes** of $0, 1, \dots, m - 1$, and it is compatible with addition and multiplication, so one can compute on remainders.[^lehman][^mcs]

## Why it matters

- **Reading frames** are the residue classes of codon start positions modulo 3 ([[Reading Frame]], [[02-sequence-translation]]).
- **Circular genomes.** Bacterial chromosomes such as that of *E. coli* K-12 (4,639,221 bp)[^blattner] and the human mitochondrial genome (16,569 bp)[^anderson][^alberts] are circular: coordinates wrap around, and every shift, length or distance is computed modulo the genome length ([[Genomic Coordinate System]]).
- **Hashing.** Hash functions reduce keys modulo a table size or a prime; rolling hashes give the hash of every k-mer of a sequence in constant time per position, the idea of the Rabin-Karp string matcher ([[Hash Function]], [[Rolling Hash]], [[Rabin-Karp Algorithm]]).[^clrs]
- **Bit-level k-mer codes.** Sliding a 2-bit k-mer code is arithmetic modulo $4^k$, implemented with a mask ([[K-mer]], [[05-sequence-search]]).

## Core (L1)

### Congruences and residues

- $17 \equiv 2 \pmod 3$ because $3$ divides $15$; $-7 \equiv 2 \pmod 3$ because $3$ divides $-9$.
- **Compatibility.** If $a \equiv a'$ and $b \equiv b' \pmod m$, then $a + b \equiv a' + b'$, $a - b \equiv a' - b'$ and $ab \equiv a'b' \pmod m$ (proof in the Mathematical representation). So reduce as early as you like: $(a \cdot b) \bmod m = ((a \bmod m)(b \bmod m)) \bmod m$, which keeps numbers small.
- **No free division.** $2 \cdot 3 \equiv 2 \cdot 0 \pmod 6$, yet $3 \not\equiv 0 \pmod 6$: one may cancel a factor only if it has an inverse modulo $m$ (Deeper section).
- **In code**, Python's `%` returns a remainder in $\{0, \dots, m-1\}$ for $m > 0$, even for negative $a$: `-7 % 3` is `2`, matching the definition. Check this in any other language before porting coordinate code.

### Bio: reading frames are residues modulo 3

With 0-based coordinates, a codon starting at position $i$ lies in frame $i \bmod 3$, and two codons are in the same frame exactly when their starts are congruent modulo 3. An insertion or deletion of length $d$ keeps the downstream frame if and only if $d \equiv 0 \pmod 3$. Position 1,000,001 is in frame 2 ($1{,}000{,}001 = 3 \times 333{,}333 + 2$). How minus-strand frames line up with plus-strand frames, $(n - f) \bmod 3$, is derived in [[Reading Frame#Mathematical representation]].

### Bio: coordinates on a circular genome

On a circle of length $G$ with 0-based positions $\{0, \dots, G-1\}$:

| Operation | Formula | Note |
|---|---|---|
| move position $p$ by $s$ (either sign) | $(p + s) \bmod G$ | wraps past the origin |
| same with 1-based coordinates | $((p - 1 + s) \bmod G) + 1$ | convert to 0-based first |
| length of 1-based feature $\text{start}..\text{end}$, read forward | $((\text{end} - \text{start}) \bmod G) + 1$ | works when the feature crosses the origin |
| distance between positions $a$ and $b$ | $\min(d, G - d)$ with $d = \lvert a - b \rvert$ | the shorter way round |

On the *E. coli* chromosome, moving 500 bp forward from position 4,639,000 lands on position 279, and a feature from 4,639,000 to 279 is 501 bp long (code below).

## Deeper (L2)

### Rolling hashes of k-mers

Encode bases as $c(A) = 0, c(C) = 1, c(G) = 2, c(T) = 3$ and hash the window starting at $i$ as

$$H_i = \Big(\sum_{j=0}^{k-1} c(s_{i+j})\, B^{\,k-1-j}\Big) \bmod P$$

for a base $B$ and a prime $P$. Sliding one position drops the leftmost term, shifts, and adds the new base:

$$H_{i+1} = \big((H_i - c(s_i) B^{k-1}) \cdot B + c(s_{i+k})\big) \bmod P,$$

valid because reduction modulo $P$ commutes with $+$, $-$ and $\times$. Each hash costs $O(1)$ instead of $O(k)$. Rabin-Karp search compares window hashes with the pattern's hash and checks every equal-hash window character by character, because distinct strings can share a hash.[^clrs] With $B = 4$ and $P = 1{,}000{,}003$, the 12-mers `AAAAAAAAAAAA` and `AATTCAAGCAAT` collide: their base-4 values are $0$ and exactly $P$.

### 2-bit codes: arithmetic modulo $4^k$ as a mask

The base-4 value of a k-mer is below $4^k = 2^{2k}$ ([[K-mer]]). Appending base $x$ and dropping the oldest one is $(4 \cdot \text{code} + x) \bmod 4^k$, which in binary is a shift and a mask: `((code << 2) | x) & (4**k - 1)`. Reduction modulo a power of 2 keeps the low bits. The reverse complement can be updated at the same time: its new base, the complement $3 - x$, enters at the high end, `(rev >> 2) | ((3 - x) << 2*(k-1))`. The canonical k-mer $\min(\text{code}, \text{rev})$ then costs $O(1)$ per position.

### Greatest common divisor and inverses

$a$ has an inverse modulo $m$ (an $x$ with $ax \equiv 1 \pmod m$) if and only if $\gcd(a, m) = 1$; the extended Euclidean algorithm finds integers $x, y$ with $ax + my = \gcd(a, m)$, and $x$ is the inverse when the gcd is 1.[^lehman] Modulo a prime $p$, every $a \not\equiv 0$ is invertible, so $x \mapsto ax \bmod p$ is a bijection of $\{0, \dots, p-1\}$: one reason hash moduli are chosen prime ([[Hash Function#Deeper (L2)]]). Example: $4^{-1} \equiv 76 \pmod{101}$ since $4 \times 76 = 304 = 3 \times 101 + 1$.

## Advanced (L3)

- **Fast powers.** $a^e \bmod m$ by repeated squaring needs $O(\log e)$ multiplications (`pow(a, e, m)` in Python). **Fermat's little theorem**: for a prime $p$ and $a \not\equiv 0$, $a^{p-1} \equiv 1 \pmod p$.[^lehman] Modular exponentiation with large moduli is the core of RSA public-key encryption, which protects data in transit.[^lehman]
- **Circular sequences.** Rotating a circular sequence by $r$ is $i \mapsto (i + r) \bmod n$, and rotations compose by adding shifts modulo $n$. A circular assembly (plasmid, mitochondrial genome) may start anywhere, so two assemblies are compared after rotating each to a canonical start, for example its lexicographically smallest rotation ([[Combinatorics#Advanced (L3)]] counts rotation classes).

## Mathematical representation

- **Equivalence relation.** Reflexive: $m \mid 0$. Symmetric: $m \mid (a - b) \Rightarrow m \mid (b - a)$. Transitive: $m \mid (a - b)$ and $m \mid (b - c)$ give $m \mid (a - c)$.
- **Compatibility.** If $a - a' = km$ and $b - b' = lm$, then $(a + b) - (a' + b') = (k + l)m$ and $ab - a'b' = a(b - b') + b'(a - a') = (al + b'k)m$. $\square$
- $\mathbb{Z}_m = \{0, 1, \dots, m-1\}$ with $a \oplus b = (a + b) \bmod m$ and $a \otimes b = ab \bmod m$; compatibility makes these operations well defined on residue classes.
- **Inverse from Bézout.** If $ax + my = 1$, then $ax \equiv 1 \pmod m$. Conversely, if $ax \equiv 1$, any common divisor of $a$ and $m$ divides $1$.
- **Rolling update.** Over the integers, $\sum_{j=0}^{k-1} c(s_{i+1+j}) B^{k-1-j} = \big(\sum_{j=0}^{k-1} c(s_{i+j}) B^{k-1-j} - c(s_i) B^{k-1}\big) B + c(s_{i+k})$; reducing both sides modulo $P$ gives the update formula.

## Computational representation

```python
m = 6
ok = all(((a + b) - (a2 + b2)) % m == 0 and (a * b - a2 * b2) % m == 0
         for a in range(-12, 13) for b in range(-12, 13)
         for a2 in (a + m, a - 2 * m) for b2 in (b + m, b - 3 * m))
print(ok, -7 % 3, divmod(-7, 3))

def circ_pos(p, shift, G):
    """1-based position p moved by shift (either sign) on a circular genome of length G."""
    return (p - 1 + shift) % G + 1

def circ_length(start, end, G):
    """Length of the 1-based closed interval start..end read forward (may cross the origin)."""
    return (end - start) % G + 1

def circ_distance(a, b, G):
    d = abs(a - b) % G
    return min(d, G - d)

G = 4_639_221                                      # E. coli K-12, one circular chromosome
print(circ_pos(4_639_000, 500, G), circ_pos(5, -10, G), circ_length(4_639_000, 279, G),
      circ_distance(10, 4_639_200, G))

B, P = 4, 1_000_003                                # base and prime modulus
CODE = {"A": 0, "C": 1, "G": 2, "T": 3}

def poly_hash(s):
    h = 0
    for c in s:
        h = (h * B + CODE[c]) % P                  # Horner's rule, reduced at every step
    return h

def rolling_hashes(seq, k):
    """Hash of every k-mer in O(1) per step: drop the left base, shift, add the right base."""
    top = pow(B, k - 1, P)                         # B^(k-1) mod P
    h = poly_hash(seq[:k])
    yield h
    for i in range(k, len(seq)):
        h = ((h - CODE[seq[i - k]] * top) * B + CODE[seq[i]]) % P
        yield h

seq, k = "GATTACAGATTACCGATTACA", 12               # invented toy sequence
print(list(rolling_hashes(seq, k)) == [poly_hash(seq[i:i + k]) for i in range(len(seq) - k + 1)])

def decode(x, k):
    return "".join("ACGT"[(x >> 2 * (k - 1 - j)) & 3] for j in range(k))

w1, w2 = "A" * 12, decode(P, 12)                   # codes 0 and P: same residue mod P
print(w2, poly_hash(w1), poly_hash(w2))

def rolling_codes(seq, k):
    """2-bit codes of each k-mer and of its reverse complement, updated in O(1)."""
    mask, shift = (1 << 2 * k) - 1, 2 * (k - 1)
    fwd = rev = 0
    for i, c in enumerate(seq):
        x = CODE[c]
        fwd = ((fwd << 2) | x) & mask              # = (4 * fwd + x) mod 4^k
        rev = (rev >> 2) | ((3 - x) << shift)      # complement enters at the high end
        if i >= k - 1:
            yield fwd, rev

TO_DIGITS = str.maketrans("ACGT", "0123")
RC = str.maketrans("ACGT", "TGCA")
k = 5
direct = [(int(seq[i:i + k].translate(TO_DIGITS), 4),
           int(seq[i:i + k].translate(RC)[::-1].translate(TO_DIGITS), 4))
          for i in range(len(seq) - k + 1)]
print(list(rolling_codes(seq, k)) == direct)

def egcd(a, b):
    """(g, x, y) with a*x + b*y = g = gcd(a, b): extended Euclidean algorithm."""
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y

print(egcd(4, 101), egcd(4, 101)[1] % 101, pow(4, -1, 101), egcd(6, 21))
```

```text
True 2 (-3, 2)
279 4639216 501 31
True
AATTCAAGCAAT 0 0
True
(1, -25, 1) 76 76 (3, -3, 1)
```

The exhaustive check confirms compatibility on a range of integers; the rolling hash and the rolling 2-bit codes agree with direct recomputation; the constructed pair shows a real collision; and $\gcd(6, 21) = 3$, so 6 has no inverse modulo 21.

## Worked example

> [!example] A feature across the origin of a circular genome (invented, $G = 20$)
> A gene is annotated from position 17 to position 4 (1-based) on a circular genome of 20 bp.
> 1. **Length**: $((4 - 17) \bmod 20) + 1 = (-13 \bmod 20) + 1 = 7 + 1 = 8$: positions 17, 18, 19, 20, 1, 2, 3, 4.
> 2. **Re-origin.** To make the gene start at position 1, map every $p$ to $((p - 17) \bmod 20) + 1$: 17 → 1 and 4 → $(-13 \bmod 20) + 1 = 8$. The gene becomes 1..8 and no longer crosses the origin.
> 3. **Distance** between positions 3 and 18: $d = 15$, so $\min(15, 20 - 15) = 5$, going through the origin.
> 4. **Codon positions relative to the gene.** The offset of position $p$ inside the gene is $(p - 17) \bmod 20$, and its codon position is that offset modulo 3. Position 1 has offset $(1 - 17) \bmod 20 = 4$, so it is the second base (offset $4 \bmod 3 = 1$) of the second codon. Computed this way, the answer does not depend on where the origin of the circle was placed, whereas $p \bmod 3$ does.

## Common misconceptions

> [!warning] "The remainder of a negative number is negative"
> Mathematically $a \bmod m \in \{0, \dots, m-1\}$, and Python agrees (`-7 % 3 == 2`). Languages that return a negative remainder need `((a % m) + m) % m` when moving left past the origin.

> [!warning] "`p % G` handles 1-based coordinates"
> With 1-based positions, `G % G` is 0, a position that does not exist. Subtract 1, reduce, add 1.

> [!warning] "Equal hashes mean equal k-mers"
> A hash modulo $P$ maps infinitely many strings to $P$ values; `AAAAAAAAAAAA` and `AATTCAAGCAAT` collide above. Always verify candidate matches.

## Exercises

> [!question] Exercise 1 (L1)
> In which frame (0, 1 or 2) do codons starting at 0-based positions 0 to 9, at 1,000,001 and at 3,000,000 lie? Does a 6-bp deletion shift the downstream frame? A 4-bp one?

> [!success]- Solution
> Positions 0 to 9: 0, 1, 2, 0, 1, 2, 0, 1, 2, 0. $1{,}000{,}001 \bmod 3 = 2$; $3{,}000{,}000 \bmod 3 = 0$. A 6-bp deletion keeps the frame ($6 \equiv 0$); a 4-bp deletion shifts it by $-4 \equiv 2 \pmod 3$.

> [!question] Exercise 2 (L1)
> The human mitochondrial genome is circular and 16,569 bp long.[^anderson][^alberts] What is the distance between positions 100 and 16,500? Which position lies 200 bp after 16,500?

> [!success]- Solution
> $d = 16{,}400$ and $16{,}569 - 16{,}400 = 169$, so the distance is 169 bp through the origin (`circ_distance(100, 16_500, 16_569)` returns 169). $((16{,}500 - 1 + 200) \bmod 16{,}569) + 1 = 130 + 1 = 131$.

> [!question] Exercise 3 (L2)
> Find the inverse of 4 modulo 101 with the extended Euclidean algorithm. Does 6 have an inverse modulo 21?

> [!success]- Solution
> $101 = 25 \times 4 + 1$, so $1 = 101 - 25 \times 4$ and $4 \times (-25) \equiv 1$; $-25 \equiv 76 \pmod{101}$. `egcd(4, 101)` returns `(1, -25, 1)` and `pow(4, -1, 101)` returns 76. $\gcd(6, 21) = 3 \ne 1$, so 6 has no inverse modulo 21.

> [!question] Exercise 4 (L3, Python)
> Use `rolling_hashes` to find the 5-mers that occur more than once in the toy sequence `ACGTTGCAACGTTGCATTACGTTG`, verifying candidates by string comparison.

> [!success]- Solution
> ```python
> from collections import defaultdict
>
> seq, k = "ACGTTGCAACGTTGCATTACGTTG", 5          # invented
> buckets = defaultdict(list)
> for i, h in enumerate(rolling_hashes(seq, k)):
>     buckets[h].append(i)
> repeats = {seq[v[0]:v[0] + k]: v for v in buckets.values() if len(v) > 1
>            and all(seq[i:i + k] == seq[v[0]:v[0] + k] for i in v)}
> print(repeats)
> ```
> Output: `{'ACGTT': [0, 8, 18], 'CGTTG': [1, 9, 19], 'GTTGC': [2, 10], 'TTGCA': [3, 11]}`. The verification step is cheap and turns a probable match into a certain one.

## Mastery checklist

- [ ] 1 Recognized: I can define $a \equiv b \pmod m$ and $a \bmod m$ and compute small residues.
- [ ] 2 Understood: I can prove compatibility with $+$ and $\times$, explain why division needs an inverse, and relate frames to residues modulo 3.
- [ ] 3 Practiced: I can implement circular coordinates, a rolling hash and rolling 2-bit codes in Python, and find inverses with Euclid.
- [ ] 4 Applied: I handled features crossing the origin of a real circular genome and used frame arithmetic in [[02-sequence-translation]].
- [ ] 5 Explained: I can teach why rolling hashes work, why collisions require verification, and the pitfalls of negative and 1-based coordinates.

## References

[^lehman]: [[Mathematics for Computer Science (Lehman)]], 2017 revision, number theory part: divisibility, gcd and the Euclidean algorithm, modular arithmetic, inverses, Fermat's little theorem, RSA.
[^mcs]: [[MIT 6.042J - Mathematics for Computer Science]], modular arithmetic in the discrete structures third.
[^clrs]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 32 "String Matching" (the Rabin-Karp algorithm).
[^blattner]: [[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]], *Science* (one circular chromosome of 4,639,221 bp).
[^anderson]: [[Anderson 1981 - Sequence and Organization of the Human Mitochondrial Genome]], *Nature* 290:457-465 (16,569 bp).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of mitochondrial genomes.
