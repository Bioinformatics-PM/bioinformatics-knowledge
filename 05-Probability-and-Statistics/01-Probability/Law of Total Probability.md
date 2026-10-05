---
aliases:
  - Total Probability Theorem
  - LOTP
  - Marginalization
  - Formule des probabilités totales
tags:
  - type/concept
  - domain/statistics
  - domain/mathematics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Probability Space]]"
  - "[[Conditional Probability]]"
  - "[[Summation Notation]]"
related:
  - "[[Bayes' Theorem]]"
  - "[[Independence (Probability)]]"
  - "[[Genotype Likelihood]]"
  - "[[Hardy-Weinberg Equilibrium]]"
  - "[[Mixture Model]]"
  - "[[Hidden Markov Model]]"
  - "[[Felsenstein Pruning Algorithm]]"
projects:
  - "[[10-genomic-pipeline]]"
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Felsenstein 1981 - Evolutionary Trees from DNA Sequences]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
---

# Law of Total Probability

> [!abstract]
> When an event can happen in several mutually exclusive ways, its probability is the weighted sum of its probability in each way, weighted by how likely each way is. It is how we compute the probability of what we observe (a read base) when the cause behind it (the true genotype) is hidden.

## Definition

Let $B_1, B_2, \dots, B_n$ be a **partition** of the sample space: pairwise disjoint events whose union is $\Omega$, with $P(B_i) > 0$. Then for every event $A$

$$P(A) = \sum_{i=1}^{n} P(A \mid B_i)\, P(B_i).$$

This is the **law of total probability**.[^blitz2][^1805-3] The same holds for a countable partition.

## Why it matters

- **The hidden variable is summed out.** Sequencing observes read bases, not genotypes. The probability of an observation is a sum over the genotypes that could have produced it, each weighted by its prior probability ([[Genotype Likelihood]], [[10-genomic-pipeline]]).
- **It is the denominator of Bayes' theorem.** Every posterior probability divides by $P(\text{data}) = \sum_h P(\text{data} \mid h) P(h)$, computed with this law ([[Bayes' Theorem]]).
- **Hidden-state models are nested sums.** The probability of a sequence under a [[Hidden Markov Model]] sums over all state paths (forward algorithm), and the likelihood of an alignment column on a tree sums over all unobserved ancestral bases; both algorithms organize these sums by dynamic programming.[^durbin3][^durbin8][^f81]
- **Mixtures.** A population of cells, reads or genes made of several sub-populations has a distribution that is a weighted sum of the components' distributions ([[Mixture Model]]).[^msmb]

## Core (L1)

### Split, condition, weight, add

To compute a hard probability $P(A)$:

1. choose a partition $B_1, \dots, B_n$ such that each $P(A \mid B_i)$ is easy;
2. compute each $P(A \mid B_i)$ and each weight $P(B_i)$;
3. add the products $P(A \mid B_i) P(B_i) = P(A \cap B_i)$.

The pieces $A \cap B_i$ are disjoint and together make up $A$, so their probabilities add up to $P(A)$. On a probability tree, $P(A)$ is the sum over all branches that end in $A$.[^1805-3]

![[total-probability-genotype-partition.svg]]

### Bio: the probability of observing a base, summed over genotypes

At a diploid site with reference base C and alternative base T, the genotype is CC, CT or TT. Under [[Hardy-Weinberg Equilibrium]] with alternative-allele frequency $q$, these genotypes have probabilities $(1-q)^2$, $2q(1-q)$ and $q^2$.[^hartl][^os-u4] A read samples one of the two chromosome copies at random, and the sequencer reports the wrong base with probability $e$, each of the three wrong bases being equally likely (a simple error model, chosen here). Then

$$P(T \mid CC) = \tfrac{e}{3}, \qquad P(T \mid CT) = \tfrac12(1-e) + \tfrac12 \cdot \tfrac{e}{3} = \tfrac12 - \tfrac{e}{3}, \qquad P(T \mid TT) = 1 - e,$$

and

$$P(T) = \tfrac{e}{3}(1-q)^2 + \big(\tfrac12 - \tfrac{e}{3}\big)\, 2q(1-q) + (1 - e)\, q^2.$$

With $q = 0.1$ and $e = 0.01$ (Q20), $P(T) = 0.0027 + 0.0894 + 0.0099 = 0.1020$ (see the [[#Worked example]]).

## Deeper (L2)

### The conditional version

For an event $C$ with $P(C) > 0$ and a partition with $P(B_i \cap C) > 0$,

$$P(A \mid C) = \sum_{i} P(A \mid B_i \cap C)\, P(B_i \mid C).$$

It is the law applied inside the conditional probability $P(\cdot \mid C)$, which is itself a probability ([[Conditional Probability]]).[^blitz2] Typical use: $C$ = "the first read shows T", $B_i$ = the genotypes, $A$ = "the second read shows T".

### Two reads and a shared hidden cause

Reads are modelled as independent **given** the genotype. For two reads,

$$P(T_1 \cap T_2) = \sum_{g} P(T \mid g)^2 \, P(g) = 0.0542 \quad \text{while} \quad P(T_1)\,P(T_2) = 0.102^2 = 0.0104$$

(Exercise 4). Summing over the hidden genotype turns conditional independence into marginal dependence: the reads are correlated through the genotype they share ([[Independence (Probability)]]).

### Partitions by a quantity

Any variable that takes finitely or countably many values defines a partition, $B_k = \{\text{the variable equals } k\}$ ([[Random Variable]]). The overall error rate of a run is a sum over quality values, $P(\text{error}) = \sum_q P(\text{error} \mid Q = q)\, P(Q = q)$ (Exercise 1). When the conditioning quantity is continuous, for instance an unknown allele frequency $\theta$ with density $f$, the sum becomes an integral, $P(A) = \int_0^1 P(A \mid \theta)\, f(\theta)\, d\theta$ ([[Probability Density Function]], [[Beta Distribution]]).

### Weights matter: Simpson's paradox

Because $P(A)$ is a weighted average of the $P(A \mid B_i)$, a group can have a lower rate in every stratum and a higher rate overall if its weights differ; this reversal is **Simpson's paradox**.[^blitz2] Exercise 6 builds one with two sequencing runs.

## Advanced (L3)

- **Marginalization is exponential, dynamic programming makes it linear.** The probability of an alignment column on a rooted tree with $k$ internal nodes is a sum over $4^k$ assignments of ancestral bases, each term a product of branch transition probabilities. Felsenstein's pruning algorithm computes this sum from the leaves to the root, one node at a time;[^f81] the forward algorithm of hidden Markov models does the same over state paths, replacing a sum over $N^L$ paths ($N$ states, sequence length $L$) by $O(N^2 L)$ operations.[^durbin3] Both are the law of total probability applied recursively, with the distributive law $\sum_a \sum_b f(a)g(a,b) = \sum_a f(a) \sum_b g(a,b)$ doing the work ([[Felsenstein Pruning Algorithm]], [[Dynamic Programming]]).
- **Genotype likelihoods become data likelihoods.** Multiplying $P(\text{reads} \mid g)$ over individuals and summing over genotypes gives the likelihood of an allele frequency from sequencing data without calling any genotype ([[Likelihood Function]], [[Allele Frequency]]): uncertain genotypes are carried forward instead of being fixed too early.
- **Mixtures and latent classes.** Expression of a gene across cells of two unknown types, or read coverage over regions with 1, 2 or 3 copies, follow mixture distributions $\sum_k w_k f_k(x)$; fitting them (for example by expectation-maximization) is inferring the weights and components of a total-probability decomposition ([[Mixture Model]]).[^msmb]

## Mathematical representation

**Statement.** $(\Omega, \mathcal{F}, P)$ a probability space, $\{B_i\}_{i \in I}$ a finite or countable family with $B_i \cap B_j = \varnothing$ for $i \ne j$, $\bigcup_i B_i = \Omega$ and $P(B_i) > 0$. For $A \in \mathcal{F}$:

$$P(A) = \sum_{i \in I} P(A \cap B_i) = \sum_{i \in I} P(A \mid B_i)\, P(B_i).$$

**Proof.** $A = A \cap \Omega = \bigcup_i (A \cap B_i)$, and the sets $A \cap B_i$ are pairwise disjoint because the $B_i$ are. Countable additivity gives the first equality; the multiplication rule $P(A \cap B_i) = P(A \mid B_i) P(B_i)$ gives the second. $\square$

**Conditional version.** Apply the statement to the probability $P_C = P(\cdot \mid C)$: $P(A \mid C) = \sum_i P_C(A \mid B_i)\, P_C(B_i)$, and $P_C(A \mid B_i) = P(A \cap B_i \cap C)/P(B_i \cap C) = P(A \mid B_i \cap C)$.

**Marginalization notation.** For two discrete quantities $X, Y$, the law reads $P(X = x) = \sum_y P(X = x, Y = y) = \sum_y P(X = x \mid Y = y)\, P(Y = y)$: the marginal of $X$ is obtained by summing $Y$ out of the joint ([[Joint Distribution]]).

**Genotype model used here.** Genotypes $g \in \{CC, CT, TT\}$ with prior $\pi_g$; for a read base $b$ and error rate $e$,

$$P(b \mid g) = \frac{1}{2} \sum_{a \in g} \Big[(1 - e)\,\mathbb{1}(b = a) + \frac{e}{3}\,\mathbb{1}(b \ne a)\Big], \qquad P(b) = \sum_g P(b \mid g)\, \pi_g,$$

where the sum runs over the two alleles $a$ of $g$ and $\mathbb{1}$ is the indicator function.

## Computational representation

The sum over a partition is a dictionary comprehension; a simulation that first draws the hidden genotype, then the read, checks it.

```python
import random

E = 0.01                                    # per-base error rate (Q20)
Q = 0.1                                     # alternative-allele (T) frequency, invented
PRIOR = {"CC": (1 - Q) ** 2, "CT": 2 * Q * (1 - Q), "TT": Q ** 2}   # Hardy-Weinberg


def p_read(base: str, genotype: str, e: float = E) -> float:
    """P(read shows base | genotype): pick one allele at random, then an error
    turns it into one of the 3 other bases with probability e."""
    return sum((1 - e) if allele == base else e / 3 for allele in genotype) / 2


# Law of total probability over the partition {CC, CT, TT}
terms = {g: p_read("T", g) * PRIOR[g] for g in PRIOR}
for g, t in terms.items():
    print(f"{g}: P(T|g) = {p_read('T', g):.5f}, P(g) = {PRIOR[g]:.2f}, product = {t:.5f}")
print("P(read shows T) =", round(sum(terms.values()), 5))

# Monte Carlo: draw a genotype, then one read from it.
random.seed(5)
n, hits = 1_000_000, 0
genotypes, weights = list(PRIOR), list(PRIOR.values())
for g in random.choices(genotypes, weights, k=n):
    allele = random.choice(g)
    if random.random() < E:
        allele = random.choice([b for b in "ACGT" if b != allele])
    hits += allele == "T"
print("simulated        =", hits / n)
```

```text
CC: P(T|g) = 0.00333, P(g) = 0.81, product = 0.00270
CT: P(T|g) = 0.49667, P(g) = 0.18, product = 0.08940
TT: P(T|g) = 0.99000, P(g) = 0.01, product = 0.00990
P(read shows T) = 0.102
simulated        = 0.101758
```

## Worked example

> [!example] Probability that one read shows T at a site
> Model (invented numbers): alternative allele T at frequency $q = 0.1$, Hardy-Weinberg genotype probabilities, error rate $e = 0.01$.
>
> 1. **Partition.** $\Omega$ splits by the true genotype: $P(CC) = 0.81$, $P(CT) = 0.18$, $P(TT) = 0.01$ (sum 1).
> 2. **Conditional probabilities.** $P(T \mid CC) = 0.01/3 = 0.00333$ (an error that happens to produce T); $P(T \mid CT) = 0.5 - 0.00333 = 0.49667$; $P(T \mid TT) = 0.99$.
> 3. **Weight and add.** $0.00333 \times 0.81 + 0.49667 \times 0.18 + 0.99 \times 0.01 = 0.0027 + 0.0894 + 0.0099 = 0.1020$.
> 4. **Read the pieces.** Of all T reads, $0.0894/0.1020 = 88\%$ come from heterozygotes, $9.7\%$ from TT homozygotes and $2.6\%$ from errors on CC sites. These ratios are posterior probabilities ([[Bayes' Theorem]]): the law of total probability supplies their common denominator.
> 5. **Check.** The simulation above gives 0.1018 from $10^6$ draws. The four bases' probabilities sum to 1 (Exercise 2).

## Common misconceptions

> [!warning] "Average the conditional probabilities"
> $(0.00333 + 0.49667 + 0.99)/3 = 0.50$ is not $P(T)$. Each conditional probability must be weighted by the probability of its condition; the rare TT genotype contributes little despite $P(T \mid TT) \approx 1$.

> [!warning] "Any list of cases is a partition"
> The cases must be disjoint and cover everything. Summing over "carries T" and "is heterozygous" counts CT twice; forgetting TT leaves a gap. Check that the weights $P(B_i)$ sum to 1.

> [!warning] "Swap the conditioning: $P(A) = \sum_i P(B_i \mid A) P(B_i)$"
> The law conditions $A$ on the parts, not the parts on $A$. $\sum_i P(B_i \mid A) = 1$ always; that is a different statement.

> [!warning] "Better in every subgroup means better overall"
> Not when the subgroups have different weights in the two groups being compared (Simpson's paradox, Exercise 6).

## Exercises

> [!question] Exercise 1 (L1)
> In an invented run, 5 % of bases have Q10, 15 % Q20 and 80 % Q30, and qualities are calibrated. What is the overall per-base error rate?

> [!success]- Solution
> $P(\text{error}) = 0.05 \times 0.1 + 0.15 \times 0.01 + 0.80 \times 0.001 = 0.005 + 0.0015 + 0.0008 = 0.0073$. The 5 % of Q10 bases cause 68 % of the errors.

> [!question] Exercise 2 (L1)
> With the worked-example model, compute $P(\text{read shows C})$ and $P(\text{read shows A})$, and check that the probabilities of the four bases sum to 1.

> [!success]- Solution
> $P(C) = 0.99 \times 0.81 + 0.49667 \times 0.18 + 0.00333 \times 0.01 = 0.80190 + 0.08940 + 0.00003 = 0.89133$. A and G can only arise from errors, whatever the genotype: $P(A) = P(G) = e/3 = 0.00333$. Sum: $0.89133 + 0.10200 + 2 \times 0.00333 = 1.0000$.

> [!question] Exercise 3 (L2)
> Prove the conditional version $P(A \mid C) = \sum_i P(A \mid B_i \cap C)\, P(B_i \mid C)$ directly from the definition of conditional probability.

> [!success]- Solution
> $P(A \cap C) = \sum_i P(A \cap B_i \cap C)$ by the unconditional law applied to the event $A \cap C$. Each term equals $P(A \mid B_i \cap C)\, P(B_i \cap C) = P(A \mid B_i \cap C)\, P(B_i \mid C)\, P(C)$. Divide both sides by $P(C)$.

> [!question] Exercise 4 (L2, Python)
> Two reads are drawn at the same site, independently given the genotype. Compute $P(T_1 \cap T_2)$ with the law of total probability and compare it with $P(T_1) P(T_2)$. Also print the probability of each base for one read.

> [!success]- Solution
> ```python
> E, Q = 0.01, 0.1
> PRIOR = {"CC": (1 - Q) ** 2, "CT": 2 * Q * (1 - Q), "TT": Q ** 2}
>
>
> def p_read(base, genotype, e=E):
>     return sum((1 - e) if allele == base else e / 3 for allele in genotype) / 2
>
>
> one_read = {b: sum(p_read(b, g) * PRIOR[g] for g in PRIOR) for b in "ACGT"}
> print({b: round(v, 5) for b, v in one_read.items()}, round(sum(one_read.values()), 12))
> both_t = sum(p_read("T", g) ** 2 * PRIOR[g] for g in PRIOR)
> print(round(both_t, 5), round(one_read["T"] ** 2, 5))
> ```
>
> ```text
> {'A': 0.00333, 'C': 0.89133, 'G': 0.00333, 'T': 0.102} 1.0
> 0.05421 0.0104
> ```
>
> $P(T_1 \cap T_2) = 0.054$ is five times $P(T_1)P(T_2)$: given one T read, a second T has probability $0.054/0.102 = 0.53$, not 0.10. The reads are dependent because they share the unknown genotype.

> [!question] Exercise 5 (L3, Python)
> A root with a uniformly random base has two leaves; each leaf keeps the root base with probability 0.7 and otherwise changes to one of the three other bases with probability 0.1 each, independently. Compute $P(\text{leaf}_1 = A, \text{leaf}_2 = A)$ and $P(A, C)$ by summing over the unobserved root, check that the 16 patterns sum to 1, and confirm by simulation.

> [!success]- Solution
> ```python
> import random
>
> P_CHANGE = 0.3                               # probability that a leaf differs from the root
> BASES = "ACGT"
>
>
> def p_leaf(x: str, root: str) -> float:
>     return 1 - P_CHANGE if x == root else P_CHANGE / 3
>
>
> def site_probability(x1: str, x2: str) -> float:
>     """Sum over the unobserved root state (law of total probability)."""
>     return sum(0.25 * p_leaf(x1, a) * p_leaf(x2, a) for a in BASES)
>
>
> def evolve(root: str) -> str:
>     if random.random() < P_CHANGE:
>         return random.choice([b for b in BASES if b != root])
>     return root
>
>
> print("P(A, A) =", round(site_probability("A", "A"), 4))
> print("P(A, C) =", round(site_probability("A", "C"), 4))
> print("sum over all 16 patterns =", round(sum(site_probability(x, y) for x in BASES for y in BASES), 10))
>
> random.seed(2)
> n, aa, ac = 500_000, 0, 0
> for _ in range(n):
>     root = random.choice(BASES)
>     x1, x2 = evolve(root), evolve(root)
>     aa += (x1, x2) == ("A", "A")
>     ac += (x1, x2) == ("A", "C")
> print("simulated", aa / n, ac / n)
> ```
>
> ```text
> P(A, A) = 0.13
> P(A, C) = 0.04
> sum over all 16 patterns = 1.0
> simulated 0.130018 0.040334
> ```
>
> By hand: $P(A, A) = \frac14\big[0.7^2 + 3 \times 0.1^2\big] = 0.13$. This is the smallest case of the pruning algorithm: the site likelihood of a tree is a sum over ancestral states.[^f81]

> [!question] Exercise 6 (L3)
> Two invented runs are compared on the same library. Run X: 10 % of bases in the low-quality bin with error rate 0.09, 90 % in the high-quality bin with error rate 0.0009. Run Y: 5 % low-quality with error rate 0.10, 95 % high-quality with error rate 0.001. Which run is better in each bin, and overall? Explain.

> [!success]- Solution
> In each bin X has the lower error rate (0.09 < 0.10 and 0.0009 < 0.001). Overall: X gives $0.1 \times 0.09 + 0.9 \times 0.0009 = 0.00981$; Y gives $0.05 \times 0.10 + 0.95 \times 0.001 = 0.00595$. Y is better overall because it puts fewer bases in the bad bin: the overall rate is a weighted average, and the weights differ (Simpson's paradox). Which comparison matters depends on the question: per-bin rates judge the base caller's calibration, the overall rate judges the data you get.

## Mastery checklist

- [ ] 1 Recognized: I can state the law of total probability and name what a partition is.
- [ ] 2 Understood: I can prove it from the axioms and the multiplication rule, and explain it on a tree and on the genotype partition figure.
- [ ] 3 Practiced: I can compute the probability of a read base summed over genotypes, by hand and in Python, and check it by simulation.
- [ ] 4 Applied: in [[10-genomic-pipeline]], I compute the marginal probability of the observed bases at a site for several allele frequencies and error rates, as the denominator of a genotype posterior.
- [ ] 5 Explained: I can teach marginalization over hidden variables, why it creates dependence between reads, how pruning and the forward algorithm reorganize the sum, and Simpson's paradox.

## References

[^blitz2]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 2 "Conditional Probability" (law of total probability, conditional version, Simpson's paradox).
[^1805-3]: [[MIT 18.05 - Introduction to Probability and Statistics]], Reading 3 "Conditional Probability, Independence and Bayes' Theorem" (law of total probability, probability trees).
[^hartl]: [[Principles of Population Genetics (Hartl)]], Hardy-Weinberg genotype frequencies.
[^os-u4]: [[Biology 2e (OpenStax)]], Unit 4, chapter "The Evolution of Populations" (Hardy-Weinberg principle).
[^durbin3]: [[Biological Sequence Analysis (Durbin)]], ch. 3 "Markov chains and hidden Markov models" (the forward algorithm).
[^durbin8]: [[Biological Sequence Analysis (Durbin)]], ch. 8 "Probabilistic approaches to phylogeny".
[^f81]: [[Felsenstein 1981 - Evolutionary Trees from DNA Sequences]], Felsenstein J, *Journal of Molecular Evolution* 17(6):368-376: likelihood of a site computed recursively from the tips to the root.
[^msmb]: [[Modern Statistics for Modern Biology (Holmes)]], mixture models part.
