---
aliases:
  - Sample Space
  - Probability Model
  - Probability Axioms
  - Event (Probability)
  - Espace probabilisé
  - Univers (probabilités)
tags:
  - type/concept
  - domain/statistics
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Set]]"
  - "[[Function]]"
  - "[[Combinatorics]]"
  - "[[Inclusion-Exclusion Principle]]"
related:
  - "[[Conditional Probability]]"
  - "[[Independence (Probability)]]"
  - "[[Random Variable]]"
  - "[[Probability Distribution]]"
  - "[[K-mer]]"
  - "[[Sequence Motif]]"
  - "[[Monte Carlo Method]]"
projects:
  - "[[05-sequence-search]]"
  - "[[06-mutation-lab]]"
sources:
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Harvard Stat 110 - Probability]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
---

# Probability Space

> [!abstract]
> A probability space is the complete description of a random experiment: the list of everything that can happen, the questions (events) we may ask about it, and a rule that gives each event a number between 0 and 1 while respecting three axioms.

## Definition

A **probability space** $(\Omega, \mathcal{F}, P)$ consists of a **sample space** $\Omega$, the set of all possible outcomes of an experiment; a collection $\mathcal{F}$ of **events**, subsets of $\Omega$; and a **probability function** $P$ that assigns to each event $A$ a number $P(A)$ such that $P(A) \ge 0$, $P(\Omega) = 1$, and $P\left(\bigcup_i A_i\right) = \sum_i P(A_i)$ for every finite or countable sequence of pairwise disjoint events.[^blitz1][^1805-2][^6041] An event **occurs** when the actual outcome belongs to it.[^blitz1]

## Why it matters

- **Every probabilistic statement in bioinformatics hides a sample space.** "This 8-mer is unlikely to occur by chance" means: in a stated model of random sequence, the event "the site occurs" has small probability. Changing the model (uniform bases, a genome's base composition, a [[Markov Chain]]) changes the answer.
- **Null models for search.** Alignment scores and motif hits are judged against sequences drawn from a random model in which each residue is chosen independently from background frequencies ([[Sequence Alignment]], [[Sequence Motif]]).[^durbin2] The expected number of random k-mer hits in [[05-sequence-search]] is computed in such a space ([[K-mer]], [[Expected Value]]).
- **Simulation.** [[06-mutation-lab]] and every [[Monte Carlo Method]] draw outcomes from an explicit $\Omega$; writing the space down first is what makes a simulation checkable against an exact answer.

## Core (L1)

### Outcomes, events and the language of sets

An **outcome** $\omega$ is one complete result of the experiment. An **event** is a set of outcomes. Logical words become [[Set]] operations:[^blitz1]

| In words | In sets |
|---|---|
| $A$ or $B$ occurs (at least one) | $A \cup B$ |
| $A$ and $B$ both occur | $A \cap B$ |
| $A$ does not occur | $A^c = \Omega \setminus A$ |
| $A$ and $B$ cannot both occur (disjoint, mutually exclusive) | $A \cap B = \varnothing$ |
| $A$ implies $B$ | $A \subseteq B$ |
| something happens / nothing happens | $\Omega$ / $\varnothing$ |

For the experiment "draw one 8-mer", an outcome is a word such as `GATTACAG`, $\Omega = \{A, C, G, T\}^8$ and "the 8-mer contains CG" is the event $E = \{\omega \in \Omega : \texttt{CG} \text{ is a substring of } \omega\}$.

### The axioms

A probability function must satisfy three rules: probabilities are non-negative, the whole sample space has probability 1, and the probability of a union of disjoint events is the sum of their probabilities.[^blitz1][^1805-2] Everything else (complements, unions of overlapping events, bounds) is **derived** from these three (see [[#Deeper (L2)]]).

### Equally likely outcomes: probability by counting

If $\Omega$ is finite and all outcomes are equally likely, then

$$P(A) = \frac{|A|}{|\Omega|},$$

the **naive definition** of probability: count the favourable outcomes, divide by the total.[^blitz1] Counting is then the whole job, which is why [[Combinatorics]] comes first. The assumption of equal likelihood is part of the model and must be justified, not assumed out of habit.[^blitz1]

**Bio: a random 8-mer against a given site.** With independent, uniform bases every 8-mer is equally likely, $|\Omega| = 4^8 = 65{,}536$, and for a fixed site $s$:

- exact match: $P(\{s\}) = 1/65{,}536 \approx 1.53 \times 10^{-5}$;
- at most one mismatch: $1 + 8 \times 3 = 25$ outcomes (the site itself, plus 3 alternative bases at each of 8 positions), so $25/65{,}536 \approx 3.8 \times 10^{-4}$;
- a match on either strand: the event $\{s, \mathrm{rc}(s)\}$ ([[Reverse Complement]]) has 2 outcomes, or only 1 when $s$ is its own reverse complement.

![[sample-space-8mer-events.svg]]

## Deeper (L2)

### Consequences of the axioms

For any events $A, B$ (proofs in [[#Mathematical representation]]):

1. $P(A^c) = 1 - P(A)$, hence $P(\varnothing) = 0$.
2. If $A \subseteq B$ then $P(A) \le P(B)$ (monotonicity), so $0 \le P(A) \le 1$.
3. $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ([[Inclusion-Exclusion Principle]]).
4. $P\left(\bigcup_{i=1}^{n} A_i\right) \le \sum_{i=1}^{n} P(A_i)$ (the **union bound**, or Boole's inequality).

The complement rule is the workhorse of sequence problems: "at least one CG in an 8-mer" is hard to count directly, "no CG" is easy (Exercise 3).

### Outcomes that are not equally likely

A finite or countable $\Omega$ can carry any weights $p(\omega) \ge 0$ with $\sum_{\omega} p(\omega) = 1$; then $P(A) = \sum_{\omega \in A} p(\omega)$. Genomes are rarely uniform: with base frequencies $\pi_A, \pi_C, \pi_G, \pi_T$ and independent positions ([[Independence (Probability)]]), a word $\omega = \omega_1 \dots \omega_k$ has weight

$$p(\omega) = \prod_{i=1}^{k} \pi_{\omega_i},$$

the random-sequence model used as the null hypothesis of alignment scoring.[^durbin2] In a 60 % GC genome, `GCGGCCGC` is 4.3 times more probable than under the uniform model and `ATATATAT` 6 times less (Exercise 4). The naive definition is the special case $p(\omega) = 1/|\Omega|$.

### Countable and continuous sample spaces

- **Countable**: the number of reads starting at a given position can be $0, 1, 2, \dots$ with no fixed upper limit, so $\Omega = \{0, 1, 2, \dots\}$; countable additivity is then needed, not just finite additivity.
- **Uncountable**: the position of a read start modelled as a real number on a chromosome of length $L$, $\Omega = [0, L]$. With a uniform model $P([a, b]) = (b - a)/L$, and every single point has probability 0 ([[Uniform Distribution]]). Probabilities come from lengths, areas or integrals of a density rather than from counting ([[Probability Density Function]]).

## Advanced (L3)

- **Which subsets are events.** On a finite $\Omega$ every subset can be an event. On $[0, L]$ one cannot assign a length-based probability to every subset while keeping the axioms, so measure-theoretic probability restricts events to a $\sigma$-algebra $\mathcal{F}$: a collection containing $\Omega$ and closed under complements and countable unions.[^blitz1] For applied work the practical rule is: intervals and everything built from them by countable set operations are events.
- **The model is a choice.** Uniform bases, genome composition and a first-order Markov model are three probability spaces on the same $\Omega = \Sigma^k$; they give different probabilities to `CGCGCGCG`, and a real genome agrees with none exactly. Significance statements ("this motif is over-represented") are only as good as the chosen space.
- **Many positions, overlapping events.** In a sequence of length $n$, let $E_i$ be "the site starts at position $i$". The events $E_1, \dots, E_{n-k+1}$ are neither disjoint (a self-overlapping site can occur at $i$ and $i+1$) nor independent. The union bound gives $P(\text{at least one hit}) \le (n - k + 1)/4^k$, which is accurate when hits are rare and do not clump; for self-overlapping words such as `AAAAAAAA` the true probability is noticeably lower (Exercise 5). The expected number of hits, $(n-k+1)/4^k$, does not depend on overlaps ([[Expected Value]]); the probability of at least one does.
- **Probability as a long-run frequency.** Simulating the experiment $N$ times and counting how often $A$ occurs estimates $P(A)$, with a standard error of $\sqrt{P(A)(1 - P(A))/N}$ ([[Variance]], [[Monte Carlo Method]]). Frequentist and Bayesian readings of probability (long-run frequency versus degree of belief) obey the same axioms.[^blitz1][^1805-2]

## Mathematical representation

Let $(\Omega, \mathcal{F}, P)$ be a probability space: $\Omega$ a non-empty set, $\mathcal{F}$ a $\sigma$-algebra of subsets of $\Omega$ (all subsets when $\Omega$ is finite), and $P : \mathcal{F} \to \mathbb{R}$ with

$$\text{(A1) } P(A) \ge 0, \qquad \text{(A2) } P(\Omega) = 1, \qquad \text{(A3) } P\Big(\bigcup_{i \ge 1} A_i\Big) = \sum_{i \ge 1} P(A_i) \text{ if } A_i \cap A_j = \varnothing \ (i \ne j).$$

**Proofs of the consequences.**

- *Complement.* $A$ and $A^c$ are disjoint with union $\Omega$, so by (A3) and (A2) $P(A) + P(A^c) = 1$. With $A = \Omega$: $P(\varnothing) = 0$.
- *Monotonicity.* If $A \subseteq B$, then $B = A \cup (B \setminus A)$, a disjoint union, so $P(B) = P(A) + P(B \setminus A) \ge P(A)$ by (A1).
- *Inclusion-exclusion.* $A \cup B = A \cup (B \setminus A)$ and $B = (A \cap B) \cup (B \setminus A)$, both disjoint unions. Hence $P(A \cup B) = P(A) + P(B \setminus A) = P(A) + P(B) - P(A \cap B)$.
- *Union bound.* By induction: $P(A_1 \cup \dots \cup A_n) = P(A_1 \cup \dots \cup A_{n-1}) + P(A_n) - P(\dots \cap A_n) \le P(A_1 \cup \dots \cup A_{n-1}) + P(A_n)$.

**Counting spaces used in sequence analysis** ($\Sigma = \{A, C, G, T\}$, words of length $k$):

| Event | Size | Probability (uniform) |
|---|---|---|
| $\{s\}$ | $1$ | $4^{-k}$ |
| within Hamming distance $d$ of $s$ | $\sum_{j=0}^{d} \binom{k}{j} 3^j$ | size $\times\, 4^{-k}$ |
| $\{s, \mathrm{rc}(s)\}$, $s \ne \mathrm{rc}(s)$ | $2$ | $2 \cdot 4^{-k}$ |

The middle row uses the [[Binomial Coefficient]]: choose the $j$ mismatched positions, then one of 3 wrong bases at each.

## Computational representation

For a small finite space, list $\Omega$ explicitly, represent each event as a predicate (a function returning `True` or `False`), and count. `itertools.product` enumerates $\Sigma^k$; a seeded simulation checks the counts.

```python
import itertools
import random

ALPHABET = "ACGT"
SITE = "ACGTTGCA"                       # invented 8-bp site
COMPLEMENT = str.maketrans("ACGT", "TGCA")


def reverse_complement(s: str) -> str:
    return s.translate(COMPLEMENT)[::-1]


def hamming(a: str, b: str) -> int:
    return sum(x != y for x, y in zip(a, b))


# Sample space: all 4^8 8-mers, equally likely (naive definition).
omega = ["".join(t) for t in itertools.product(ALPHABET, repeat=len(SITE))]


def prob(event) -> float:
    """P(event) = |event| / |omega| for equally likely outcomes."""
    return sum(1 for w in omega if event(w)) / len(omega)


events = {
    "exact match": lambda w: w == SITE,
    "<= 1 mismatch": lambda w: hamming(w, SITE) <= 1,
    "either strand": lambda w: w in (SITE, reverse_complement(SITE)),
}
print(len(omega), "outcomes")
for name, event in events.items():
    print(f"{name:14s} exact {prob(event):.3e}")

# Monte Carlo check: draw random 8-mers with a fixed seed.
random.seed(1)
n = 1_000_000
draws = ["".join(random.choices(ALPHABET, k=len(SITE))) for _ in range(n)]
for name, event in events.items():
    print(f"{name:14s} simulated {sum(map(event, draws)) / n:.3e}")
```

```text
65536 outcomes
exact match    exact 1.526e-05
<= 1 mismatch  exact 3.815e-04
either strand  exact 3.052e-05
exact match    simulated 1.700e-05
<= 1 mismatch  simulated 3.880e-04
either strand  simulated 2.400e-05
```

A million draws estimate the one-mismatch probability to within about 5 %, but the exact-match probability only roughly (17 hits observed for 15.3 expected): rare events need exact counting or far larger simulations. Enumeration costs $O(4^k)$ and stops being practical near $k = 12$; beyond that, count with formulas.

## Worked example

> [!example] The probability that a random 8-mer matches a site
> Site $s$ = `ACGTTGCA` (invented), random 8-mer with independent, uniform bases.
>
> 1. **Sample space.** $\Omega = \{A, C, G, T\}^8$, $|\Omega| = 4^8 = 65{,}536$, all outcomes equally likely.
> 2. **Exact match.** $A = \{s\}$, $P(A) = 1/65{,}536 = 1.526 \times 10^{-5}$.
> 3. **At most one mismatch.** $B$ contains $s$ and the $8 \times 3 = 24$ words differing at exactly one position: $P(B) = 25/65{,}536 = 3.815 \times 10^{-4}$. Since $A \subseteq B$, $P(A) \le P(B)$ as monotonicity requires.
> 4. **Either strand, one mismatch allowed.** $\mathrm{rc}(s)$ = `TGCAACGT` differs from $s$ at all 8 positions, so no word is within one mismatch of both: $B \cap C = \varnothing$ and $P(B \cup C) = 50/65{,}536 = 7.63 \times 10^{-4}$. Had $s$ and $\mathrm{rc}(s)$ been within distance 2 of each other, the overlap would have to be subtracted (inclusion-exclusion).
> 5. **Interpretation.** In any one window of a random sequence, a one-mismatch match on either strand has probability $7.6 \times 10^{-4}$: about one window in 1,300. A 1 Mb region has about $10^6$ windows, so hundreds of such "matches" are expected by chance ([[Expected Value]]): a hit alone is weak evidence of a functional site ([[Sequence Motif]]).

## Common misconceptions

> [!warning] "Equally likely" is not automatic
> The naive formula $|A|/|\Omega|$ holds only when the model makes all outcomes equally likely. In a genome with 60 % GC, 8-mers are not equally likely, and probabilities computed by counting words are wrong by factors of 5 or more for extreme compositions.

> [!warning] "Disjoint" and "independent" are the same thing
> Disjoint events exclude each other: if one occurs, the other cannot. Independent events do not influence each other. Two disjoint events with positive probability are always dependent ([[Independence (Probability)]]).

> [!warning] "Probability 0 means impossible"
> In a continuous space every single point has probability 0, yet one of them occurs. Probability 0 means "negligible in the model", not "cannot happen"; only $\varnothing$ is truly impossible.

> [!warning] "Adding the probabilities of all positions gives the probability of a hit"
> $\sum_i P(E_i)$ is the expected number of hits and an upper bound on $P(\text{at least one hit})$. It can exceed 1 for a long sequence, which no probability can.

## Exercises

> [!question] Exercise 1 (L1)
> The restriction enzyme EcoRI recognizes `GAATTC`.[^alberts] For a random 6-mer with uniform, independent bases, compute the probability that it is `GAATTC`, and the probability that it matches `GAATTC` read on either strand.

> [!success]- Solution
> $|\Omega| = 4^6 = 4{,}096$, so $P = 1/4{,}096 \approx 2.44 \times 10^{-4}$. The reverse complement of `GAATTC` is `GAATTC` itself, so "either strand" is the same one-outcome event: still $1/4{,}096$, not $2/4{,}096$. For a non-palindromic site the two outcomes differ and the probability doubles.

> [!question] Exercise 2 (L1)
> Using only the three axioms, show that $P(A \cup B) \le P(A) + P(B)$, and give a case from the worked example where equality holds.

> [!success]- Solution
> By inclusion-exclusion (proved from the axioms), $P(A \cup B) = P(A) + P(B) - P(A \cap B)$, and $P(A \cap B) \ge 0$ by (A1). Equality holds exactly when $P(A \cap B) = 0$, e.g. for $B$ and $C$ in the worked example, which are disjoint.

> [!question] Exercise 3 (L2, Python)
> Compute the probability that a random 8-mer contains at least one `CG`, (a) by enumerating $\Omega$, (b) through the complement, using the recurrence $f(n) = 4 f(n-1) - f(n-2)$ for the number $f(n)$ of words of length $n$ without `CG`. Justify the recurrence.

> [!success]- Solution
> A word of length $n$ without `CG` is a word of length $n-1$ without `CG` followed by any base, except that `G` cannot follow a final `C`. So $f(n) = 4 f(n-1) - c(n-1)$, where $c(n-1)$ counts the valid words ending in `C`; and $c(n-1) = f(n-2)$ (append `C` to any valid word). Hence $f(n) = 4f(n-1) - f(n-2)$ with $f(0) = 1$, $f(1) = 4$.
>
> ```python
> import itertools
>
> omega = ["".join(t) for t in itertools.product("ACGT", repeat=8)]
> print(sum("CG" in w for w in omega) / len(omega))
>
> f = [1, 4]                      # f(n): strings of length n without "CG"
> for n in range(2, 9):
>     f.append(4 * f[-1] - f[-2])
> print(f, 1 - f[8] / 4**8)
> ```
>
> ```text
> 0.3813323974609375
> [1, 4, 15, 56, 209, 780, 2911, 10864, 40545] 0.3813323974609375
> ```
>
> $P(\text{at least one CG}) = 1 - 40{,}545/65{,}536 \approx 0.381$: more than a third of random 8-mers contain `CG`.

> [!question] Exercise 4 (L2, Python)
> In a genome with 60 % GC ($\pi_G = \pi_C = 0.3$, $\pi_A = \pi_T = 0.2$) and independent positions, show that the weights $p(\omega) = \prod_i \pi_{\omega_i}$ on $\{A,C,G,T\}^8$ define a probability, and compute the probabilities of `ACGTTGCA`, `GCGGCCGC` and `ATATATAT`, with their ratio to the uniform value $4^{-8}$.

> [!success]- Solution
> Expanding the product, $\sum_{\omega} \prod_{i=1}^{8} \pi_{\omega_i} = \prod_{i=1}^{8} \big(\sum_{b} \pi_b\big) = 1^8 = 1$, and all weights are non-negative: the axioms hold.
>
> ```python
> import itertools
> import math
>
> p = {"A": 0.2, "C": 0.3, "G": 0.3, "T": 0.2}   # 60 % GC, i.i.d. bases
> omega = ["".join(t) for t in itertools.product("ACGT", repeat=8)]
> weight = {w: math.prod(p[b] for b in w) for w in omega}
> print(round(sum(weight.values()), 9))           # the weights form a probability
> for site in ("ACGTTGCA", "GCGGCCGC", "ATATATAT"):
>     print(site, f"{weight[site]:.3e}", round(weight[site] * 4**8, 2))
> ```
>
> ```text
> 1.0
> ACGTTGCA 1.296e-05 0.85
> GCGGCCGC 6.561e-05 4.3
> ATATATAT 2.560e-06 0.17
> ```
>
> A balanced site barely changes (ratio 0.85); a pure GC site is 4.3 times more likely and a pure AT site about 6 times less likely than under the uniform model.

> [!question] Exercise 5 (L3, Python)
> In a uniform random sequence of 1,000 bp, compare $P(\text{the 8-mer occurs at least once})$ for `ACGTTGCA` and `AAAAAAAA` with the union bound $993/4^8$. Compute the exact values by tracking how much of the site has been matched so far, and check them by simulation. Explain the difference.

> [!success]- Solution
> ```python
> import random
>
>
> def p_at_least_one(site: str, n: int) -> float:
>     """Exact P(site occurs in a uniform random sequence of length n), by tracking
>     the longest suffix of the text that is a prefix of the site (a KMP automaton)."""
>     k = len(site)
>
>     def step(state: int, base: str) -> int:
>         s = site[:state] + base
>         while s and not site.startswith(s):
>             s = s[1:]
>         return len(s)
>
>     dist = [1.0] + [0.0] * k          # dist[j]: P(longest matched prefix = j, no hit yet)
>     hit = 0.0
>     for _ in range(n):
>         new = [0.0] * (k + 1)
>         for state, pr in enumerate(dist[:k]):
>             for b in "ACGT":
>                 new[step(state, b)] += pr / 4
>         hit += new[k]
>         new[k] = 0.0
>         dist = new
>     return hit
>
>
> random.seed(7)
> n, reps = 1000, 20_000
> seqs = ["".join(random.choices("ACGT", k=n)) for _ in range(reps)]
> print("union bound", round((n - 8 + 1) / 4**8, 5))
> for site in ("ACGTTGCA", "AAAAAAAA"):
>     sim = sum(site in s for s in seqs) / reps
>     print(site, round(p_at_least_one(site, n), 5), round(sim, 5))
> ```
>
> ```text
> union bound 0.01515
> ACGTTGCA 0.01504 0.0146
> AAAAAAAA 0.0113 0.01145
> ```
>
> Both words have the same expected number of occurrences (0.01515), but occurrences of `AAAAAAAA` come in clumps: once it occurs, one more `A` (probability 1/4) gives another occurrence at the next position. Clumped hits fall in fewer sequences, so the probability of at least one hit is about 25 % lower. The union bound is nearly exact for the non-clumping site. This is why word-count statistics must account for self-overlap ([[K-mer]]).

## Mastery checklist

- [ ] 1 Recognized: I can name the three parts of a probability space and state the three axioms.
- [ ] 2 Understood: I can translate "or", "and", "not", "at least one" into set operations and derive the complement rule, monotonicity and inclusion-exclusion from the axioms.
- [ ] 3 Practiced: I can compute probabilities of k-mer events by counting (exact, with mismatches, on both strands) and check them by enumeration and seeded simulation in Python.
- [ ] 4 Applied: in [[05-sequence-search]], I state the probability space behind every "random hit" estimate and compare uniform and composition-aware models on a real genome.
- [ ] 5 Explained: I can teach why equal likelihood is a modelling choice, why events at overlapping positions break the union bound's accuracy, and what a $\sigma$-algebra is for.

## References

[^blitz1]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 1 "Probability and Counting" (sample spaces and events, naive definition, general definition of probability, frequentist and Bayesian views).
[^1805-2]: [[MIT 18.05 - Introduction to Probability and Statistics]], Reading 2 "Probability: Terminology and Examples".
[^6041]: [[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]], probability models and axioms; see also [[Harvard Stat 110 - Probability]], foundations (sample spaces).
[^durbin2]: [[Biological Sequence Analysis (Durbin)]], ch. 2 "Pairwise alignment" (random model of independent residues).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), restriction enzymes and the EcoRI site.
