---
aliases:
  - HGeom(w, b, n)
  - Hypergeometric Law
  - Sampling Without Replacement
  - Hypergeometric Test
  - Loi hypergéométrique
tags:
  - type/concept
  - domain/statistics
  - domain/mathematics
  - domain/bioinformatics
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Binomial Distribution]]"
  - "[[Binomial Coefficient]]"
  - "[[Combinatorics]]"
  - "[[Expected Value]]"
  - "[[Variance]]"
  - "[[Cumulative Distribution Function]]"
related:
  - "[[Fisher's Exact Test]]"
  - "[[Contingency Table]]"
  - "[[Over-Representation Analysis]]"
  - "[[Gene Set Enrichment Analysis]]"
  - "[[Gene Ontology Annotation]]"
  - "[[Multiple Testing Correction]]"
  - "[[False Discovery Rate]]"
  - "[[P-Value]]"
  - "[[Differential Expression Analysis]]"
  - "[[Multinomial Distribution]]"
projects: []
sources:
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Rivals 2007 - Enrichment or Depletion of a GO Category Within a Class of Genes - Which Test]]"
  - "[[Young 2010 - Gene Ontology Analysis for RNA-Seq - Accounting for Selection Bias]]"
  - "[[Gene Ontology]]"
  - "[[Benjamini 1995 - Controlling the False Discovery Rate]]"
---

# Hypergeometric Distribution

> [!abstract]
> The hypergeometric distribution counts the marked items in a sample drawn without replacement from a finite population: how many of your 300 differentially expressed genes belong to a pathway of 40 genes, out of 12,000 genes measured. Its upper tail is the p-value of the classic enrichment test.

## Definition

A population of $N$ items contains $K$ marked ones; a sample of $n$ items is drawn without replacement, every subset of size $n$ being equally likely. The number $X$ of marked items in the sample has the **hypergeometric distribution**:[^blitz3][^openstax]

$$P(X = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}, \qquad \max(0,\, n - N + K) \le k \le \min(n, K),$$

with mean $nK/N$ and variance $n\,\frac{K}{N}\big(1 - \frac{K}{N}\big)\frac{N-n}{N-1}$. Blitzstein and Hwang write it $\mathrm{HGeom}(w, b, n)$, for an urn with $w = K$ white and $b = N - K$ black balls.[^blitz3]

## Why it matters

- **Gene Ontology and pathway enrichment.** With $N$ genes tested, $K$ of them annotated to a term and a list of $n$ differentially expressed genes, the overlap $k$ is hypergeometric when the list is unrelated to the term. The p-value $P(X \ge k)$ is the hypergeometric test, the same test as a one-sided Fisher's exact test ([[Over-Representation Analysis]], [[Gene Ontology]], [[Gene Ontology Annotation]]).[^rivals][^go]
- **Small 2×2 tables.** Conditioning a 2×2 table on its margins gives a hypergeometric count, the basis of [[Fisher's Exact Test]] for tables too small for a chi-square test ([[Contingency Table]], [[Chi-Square Test]]).[^rivals]
- **Subsampling reads.** Keeping $n$ reads drawn without replacement from a library of $N$, of which $K$ come from one gene, gives a hypergeometric count for that gene: downsampling libraries to a common depth adds this noise.
- **Thousands of terms.** An enrichment analysis tests every term, so its p-values need multiple-testing control ([[Multiple Testing Correction]], [[False Discovery Rate]]).[^bh]

## Core (L2)

### Counting subsets

All $\binom{N}{n}$ samples are equally likely, and those with exactly $k$ marked items are formed by choosing $k$ of the $K$ marked items and $n - k$ of the $N - K$ others: there are $\binom{K}{k}\binom{N-K}{n-k}$ of them ([[Binomial Coefficient]], [[Combinatorics]]).

![[hypergeometric-enrichment-urn.svg]]

In the toy universe of the figure ($N = 100$, $K = 10$, $n = 20$) the expected overlap is $nK/N = 2$, and an overlap of 5 or more has probability $0.026$ when the list ignores the term.

### With or without replacement

Drawing **with** replacement would give $\mathrm{Bin}(n, K/N)$ ([[Binomial Distribution]]). Without replacement, each marked item drawn makes the next one less likely: the draws are negatively correlated, and the variance shrinks by the **finite population correction** $(N - n)/(N - 1)$ (Mathematical representation). When $n \ll N$ the correction is close to 1 and $\mathrm{HGeom} \approx \mathrm{Bin}(n, K/N)$; when $n = N$ the variance is 0, since the whole population is drawn. In the worked example ($n/N = 2.5$ %), the binomial tail is $5.7 \times 10^{-4}$ against the exact $4.4 \times 10^{-4}$.

### The 2×2 table

| | in the list | not in the list | total |
|---|---:|---:|---:|
| in the term | $k$ | $K - k$ | $K$ |
| not in the term | $n - k$ | $N - K - n + k$ | $N - K$ |
| total | $n$ | $N - n$ | $N$ |

Given the margins, one cell fixes all the others, and when membership in the term and in the list are independent the top-left cell is hypergeometric. The hypergeometric test and Fisher's exact test are therefore the same test,[^rivals] and the code below gets identical p-values from both. The table is symmetric in its two factors: $(N, K, n)$ and $(N, n, K)$ give the same distribution (Exercise 3), so it does not matter whether one imagines drawing the list or drawing the term.

## Advanced (L3)

### Choosing the universe

The model assumes that every gene of the universe could have entered the list with the same probability. The universe is therefore the set of genes that were **tested** (expressed and measured), not the whole genome. Adding genes that could never have been selected lowers the expected overlap and inflates enrichment: in the worked example, a universe of 20,000 instead of 12,000 genes turns $p = 4.4 \times 10^{-4}$ into $2.7 \times 10^{-5}$ for the same data.

### Discreteness and small terms

A term with $K$ genes allows only $\min(n, K) + 1$ overlaps, so its p-values take few values, and the smallest attainable one, $P(X = K)$ when $K \le n$, can be large. With $n = 300$ of $N = 12{,}000$ genes, a 3-gene term cannot go below $1.5 \times 10^{-5}$, so it never passes a Bonferroni threshold of $10^{-5}$ for 5,000 terms (Exercise 4). Exact tests on discrete data are conservative;[^rivals] filtering terms by size before testing removes tests that could never succeed ([[Cumulative Distribution Function#Discrete p-values are conservative]]).

### Many related terms

GO terms are organized in a graph from general to specific ([[Gene Ontology]]),[^go] and related terms often share genes, so their tests are correlated. The Benjamini-Hochberg procedure was proved to control the false discovery rate for independent test statistics,[^bh] a guarantee that correlated GO tests do not satisfy by construction. Read enrichment results as families of related terms: an enriched broad term is often carried by one enriched narrower term.

## Frontier (M1)

### Selection bias in RNA-seq: GOseq

The hypergeometric null fails when genes do not have the same chance of being selected. In RNA-seq, differential expression is over-detected in long and highly expressed transcripts, which carry more reads and hence more power, so standard GO tests are biased toward categories of long genes.[^young] GOseq estimates how the probability of selection depends on transcript length; its default method approximates the null distribution of the overlap with Wallenius' noncentral hypergeometric distribution,[^young] a biased-urn model in which items are drawn one by one with probabilities proportional to weights. Exercise 5 simulates the problem: a term made of long genes, unrelated to any biology, comes out "enriched" at $p < 0.05$ in 67 % of length-biased null lists, against 4 % of unbiased ones.

### Cutoffs and ranks

The hypergeometric test needs a list, so its results depend on the threshold that defined "differentially expressed". Methods that use the whole ranking of genes instead are covered in [[Gene Set Enrichment Analysis]].

## Mathematical representation

- **Normalization** (Vandermonde's identity): $\sum_k \binom{K}{k}\binom{N-K}{n-k} = \binom{N}{n}$, since choosing $n$ of $N$ items can be sorted by the number of marked items chosen.
- **Mean by indicators.** Let $I_t = 1$ if the $t$-th draw is marked. By symmetry every draw is marked with probability $q = K/N$, so $E[X] = \sum_{t=1}^n E[I_t] = nq$ ([[Expected Value]]).
- **Variance.** For two draws $s \ne t$, $P(I_s = I_t = 1) = q\,\frac{K-1}{N-1}$, so $\operatorname{Cov}(I_s, I_t) = q\frac{K-1}{N-1} - q^2 = -\frac{q(1-q)}{N-1}$. Hence

$$\operatorname{Var}(X) = nq(1-q) - n(n-1)\frac{q(1-q)}{N-1} = nq(1-q)\,\frac{N-n}{N-1}.$$

- **Symmetry.** In factorials, $\dfrac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}} = \dfrac{K!\,(N-K)!\,n!\,(N-n)!}{k!\,(K-k)!\,(n-k)!\,(N-K-n+k)!\,N!}$, which is unchanged when $K$ and $n$ are swapped.
- **Binomial limit.** With falling factorials $x^{\underline{j}} = x(x-1)\cdots(x-j+1)$, $P(X = k) = \binom{n}{k}\dfrac{K^{\underline{k}}\,(N-K)^{\underline{n-k}}}{N^{\underline{n}}}$. If $N \to \infty$ with $K/N \to p$ and $n$ fixed, each of the $n$ ratios of factors tends to $p$ or $1 - p$, so $P(X = k) \to \binom{n}{k}p^k(1-p)^{n-k}$ ([[Limit]]).
- **Enrichment and depletion.** The enrichment p-value is the upper tail $P(X \ge k) = \sum_{j=k}^{\min(n,K)} P(X = j)$; depletion uses the lower tail $P(X \le k)$ ([[P-Value]]).

## Computational representation

`math.comb` works with exact integers and `/` returns a float, so the PMF can be computed directly for tens of thousands of genes; `math.lgamma` (log space) is the alternative for larger problems.

```python
import math


def hypergeom_pmf(k: int, N: int, K: int, n: int) -> float:
    """P(X = k): k marked items in a sample of n drawn without replacement from N items, K of them marked."""
    if k < max(0, n - (N - K)) or k > min(n, K):
        return 0.0
    return math.comb(K, k) * math.comb(N - K, n - k) / math.comb(N, n)


def hypergeom_sf(k: int, N: int, K: int, n: int) -> float:
    """P(X >= k): the one-sided enrichment p-value."""
    return sum(hypergeom_pmf(j, N, K, n) for j in range(k, min(n, K) + 1))


N, K, n, k = 12_000, 40, 300, 6          # invented: tested genes, genes in the term, DE genes, overlap
print("expected overlap:", n * K / N)
print("P(X = 6):", f"{hypergeom_pmf(k, N, K, n):.2e}", "| P(X >= 6):", f"{hypergeom_sf(k, N, K, n):.2e}")
binom_tail = sum(math.comb(n, j) * (K / N) ** j * (1 - K / N) ** (n - j) for j in range(k, n + 1))
print("binomial approximation P(X >= 6):", f"{binom_tail:.2e}")

from scipy import stats
print("SciPy hypergeom:", f"{stats.hypergeom.sf(k - 1, N, K, n):.2e}")   # SciPy's order: (M total, n marked, N drawn)
table = [[k, K - k], [n - k, N - K - n + k]]          # rows: in term / not; columns: in list / not
print("Fisher exact, one-sided:", f"{stats.fisher_exact(table, alternative='greater').pvalue:.2e}")
```

```text
expected overlap: 1.0
P(X = 6): 3.83e-04 | P(X >= 6): 4.36e-04
binomial approximation P(X >= 6): 5.74e-04
SciPy hypergeom: 4.36e-04
Fisher exact, one-sided: 4.36e-04
```

SciPy names the parameters differently from this note: `hypergeom(M, n, N)` takes the population size $M$, the number of marked items $n$ and the number of draws $N$, a classic source of bugs; `sf(k - 1)` is $P(X \ge k)$. The one-sided Fisher's exact test returns the same p-value.

## Worked example

> [!example] Is a GO term enriched in a list of differentially expressed genes?
> An RNA-seq experiment tested $N = 12{,}000$ expressed genes and called $n = 300$ differentially expressed; a GO term annotates $K = 40$ of the tested genes, 6 of which are in the list (invented numbers). Continuing the code above:
>
> ```python
> for universe in (12_000, 20_000):
>     expected = n * K / universe
>     print(universe, "| expected", round(expected, 2), "| fold enrichment", round(k / expected, 1),
>           "| P(X >= 6)", f"{hypergeom_sf(k, universe, K, n):.1e}")
> print("Bonferroni threshold for 5,000 terms:", 0.05 / 5_000)
> ```
>
> ```text
> 12000 | expected 1.0 | fold enrichment 6.0 | P(X >= 6) 4.4e-04
> 20000 | expected 0.6 | fold enrichment 10.0 | P(X >= 6) 2.7e-05
> Bonferroni threshold for 5,000 terms: 1e-05
> ```
>
> 1. **Expected overlap.** If the list ignored the term, $nK/N = 1$ term gene would be in it; 6 is a 6-fold enrichment.
> 2. **p-value.** $P(X \ge 6) = 4.4 \times 10^{-4}$, the same as the one-sided Fisher's exact test on the 2×2 table.
> 3. **Universe.** Declaring the whole genome (20,000 genes, a round number) as the universe lowers the expected overlap to 0.6 and the p-value to $2.7 \times 10^{-5}$, sixteen times smaller, with no new data.
> 4. **Multiple testing.** If 5,000 terms were tested, neither value passes the Bonferroni threshold of $10^{-5}$. Controlling the false discovery rate is less strict ([[False Discovery Rate]]),[^bh] but one term at $p \approx 10^{-4}$ among thousands remains weak evidence.

## Common misconceptions

> [!warning] "The universe is the genome"
> The universe is the set of genes that could have been selected: those measured and tested. A larger universe makes every term look more enriched (Worked example).

> [!warning] "Fold enrichment measures the evidence"
> A 6-fold enrichment from 6 genes against 1 expected is weak evidence among thousands of terms; the same ratio from 60 genes against 10 expected is overwhelming. The p-value depends on the counts, not only on their ratio: report both.

> [!warning] "The hypergeometric, Fisher and chi-square tests give three different answers"
> The hypergeometric test and the one-sided Fisher's exact test are the same test. The chi-square test and the binomial approximation are large-sample approximations, unreliable for the small counts of most GO terms.[^rivals]

> [!warning] "Each enriched term is an independent discovery"
> Related GO terms share genes, so enrichments come in correlated families, and a term of long genes can look enriched only because long genes are easier to call differentially expressed in RNA-seq (Frontier (M1)).[^young]

## Exercises

> [!question] Exercise 1 (L2)
> A toy universe has 20 genes, 4 of which belong to a pathway. You pick 5 genes at random. Compute $P(X = 2)$, the mean and the variance of the number of pathway genes picked, and compare the variance with the binomial one.

> [!success]- Solution
> $P(X = 2) = \binom{4}{2}\binom{16}{3}/\binom{20}{5} = 6 \times 560 / 15{,}504 = 0.217$. Mean $5 \times 4/20 = 1$. Variance $5 \times 0.2 \times 0.8 \times \frac{15}{19} = 0.632$, against $0.8$ with replacement: a quarter of the sample is the population, so the correction $15/19$ matters.

> [!question] Exercise 2 (L2)
> Write the 2×2 table of the worked example. Which tail would test depletion of the term? Approximately how likely is an overlap of 0 under the null?

> [!success]- Solution
>
> | | in the list | not in the list | total |
> |---|---:|---:|---:|
> | in the term | 6 | 34 | 40 |
> | not in the term | 294 | 11,666 | 11,960 |
> | total | 300 | 11,700 | 12,000 |
>
> Depletion uses the lower tail $P(X \le k)$. With the binomial approximation, $P(X = 0) \approx (1 - 300/12{,}000)^{40} = 0.975^{40} \approx 0.36$: even a complete absence of the term from the list would not be evidence of depletion. A 40-gene term is too small to show depletion in a 300-gene list.

> [!question] Exercise 3 (L2)
> Prove that the hypergeometric probabilities are unchanged when $K$ and $n$ are swapped, and explain what this means for an enrichment test.

> [!success]- Solution
> Writing each binomial coefficient with factorials gives the symmetric expression of the Mathematical representation, in which $K$ and $n$ play the same role. The test conditions on both margins of the 2×2 table; it cannot tell which set was "drawn". Asking how many term genes fall in the list or how many list genes fall in the term is the same question with the same p-value.

> [!question] Exercise 4 (L3, Python)
> Continuing the code above, compute the smallest attainable p-value $P(X = K)$ for terms of $K = 1$ to 5 genes, with $N = 12{,}000$ and $n = 300$. Which terms can pass a Bonferroni threshold of $10^{-5}$?

> [!success]- Solution
> ```python
> for size in range(1, 6):
>     print(size, f"{hypergeom_pmf(size, N, size, n):.1e}")
> ```
>
> ```text
> 1 2.5e-02
> 2 6.2e-04
> 3 1.5e-05
> 4 3.8e-07
> 5 9.5e-09
> ```
>
> The minimum is about $(n/N)^K = 0.025^K$. Terms of 1 to 3 genes can never pass $10^{-5}$, whatever the data: including them only adds tests to the correction. Restrict the analysis by term size before testing, and record the limits used.

> [!question] Exercise 5 (M1, Python)
> Continuing the code above, simulate a universe of 2,000 genes with invented lengths and a 40-gene term drawn from the 20 % longest genes. Draw 1,000 null lists of 200 genes, either uniformly or with probability proportional to length (as when long genes are easier to call differentially expressed), and record how often the hypergeometric test gives $p < 0.05$.

> [!success]- Solution
> ```python
> import random
>
> rng = random.Random(2010)
> G, n_de, term_size = 2_000, 200, 40
> lengths = [rng.lognormvariate(7.5, 0.7) for _ in range(G)]          # invented gene lengths (bp)
> long_genes = sorted(range(G), key=lambda g: lengths[g])[-400:]        # the 20 % longest genes
> term = set(rng.sample(long_genes, term_size))                         # a term made of long genes
>
>
> def weighted_list(weights: list[float], size: int, rng: random.Random) -> set[int]:
>     """Weighted sampling without replacement: keep the `size` largest keys u**(1/w) (Efraimidis-Spirakis)."""
>     keys = sorted(range(len(weights)), key=lambda g: rng.random() ** (1 / weights[g]), reverse=True)
>     return set(keys[:size])
>
>
> for label, weights in (("uniform", [1.0] * G), ("length-biased", lengths)):
>     hits = 0
>     for _ in range(1_000):
>         overlap = len(weighted_list(weights, n_de, rng) & term)
>         hits += hypergeom_sf(overlap, G, term_size, n_de) < 0.05
>     print(label, "| fraction of null lists with p < 0.05:", hits / 1_000)
> ```
>
> ```text
> uniform | fraction of null lists with p < 0.05: 0.043
> length-biased | fraction of null lists with p < 0.05: 0.672
> ```
>
> With uniform selection the test is valid, slightly conservative (4.3 % below 0.05, because of discreteness). With length-biased selection the term of long genes is "significant" in two thirds of the null lists although it has nothing to do with the experiment. The sampling above, item by item with probabilities proportional to weights, is the biased urn of Wallenius' distribution, the null model that GOseq uses instead of the hypergeometric.

## Mastery checklist

- [ ] 1 Recognized: I can write the hypergeometric PMF and its mean $nK/N$, and recognize sampling without replacement.
- [ ] 2 Understood: I can explain the 2×2 table, the equivalence with Fisher's exact test, the finite population correction and the role of the universe.
- [ ] 3 Practiced: I can compute enrichment p-values in Python, by hand and with SciPy in the right parameter order, and check them against Fisher's exact test.
- [ ] 4 Applied: I ran a GO over-representation analysis on a real list of differentially expressed genes, with the tested genes as universe, a term-size filter and FDR control.
- [ ] 5 Explained: I can teach how discreteness, related terms and length bias distort enrichment results, and what GOseq changes in the null model.

## References

[^blitz3]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 3 "Random Variables and Their Distributions" (the hypergeometric distribution).
[^openstax]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 4 "Discrete Random Variables" (the hypergeometric distribution).
[^rivals]: [[Rivals 2007 - Enrichment or Depletion of a GO Category Within a Class of Genes - Which Test]], *Bioinformatics* 23(4):401-407: equivalence of the hypergeometric and Fisher's exact tests, large-sample tests, one- and two-sided p-values, discreteness and conservatism.
[^young]: [[Young 2010 - Gene Ontology Analysis for RNA-Seq - Accounting for Selection Bias]], *Genome Biology* 11(2):R14: over-detection of differential expression in long and highly expressed transcripts; GOseq and its Wallenius approximation.
[^go]: [[Gene Ontology]], the ontology (terms and the relations between them) and its annotations.
[^bh]: [[Benjamini 1995 - Controlling the False Discovery Rate]], *J R Stat Soc Series B* 57(1):289-300: the false discovery rate and a procedure proved to control it for independent test statistics.
