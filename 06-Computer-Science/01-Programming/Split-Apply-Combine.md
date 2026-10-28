---
aliases:
  - Group By
  - groupby
  - Long and Wide Format
  - Diviser-appliquer-combiner
tags:
  - type/concept
  - domain/computer-science
  - domain/statistics
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Data Frame]]"
  - "[[Tidy Data]]"
  - "[[SQL]]"
related:
  - "[[Count Normalization]]"
  - "[[Sparse Matrix]]"
  - "[[Pseudobulk Differential Expression]]"
projects:
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Wickham 2011 - The Split-Apply-Combine Strategy for Data Analysis]]"
  - "[[Python for Data Analysis (McKinney)]]"
  - "[[Wickham 2014 - Tidy Data]]"
---

# Split-Apply-Combine

> [!abstract]
> Split-apply-combine is the pattern behind every per-group computation: split the rows of a table by a key, apply a function to each group independently, and combine the results into one row per group (aggregate), one value per input row (transform) or the surviving groups (filter); reshaping between long and wide layouts is its companion.

## Definition

**Split-apply-combine** is the strategy of breaking a problem into manageable pieces, operating on each piece independently and putting the pieces back together; Wickham named it and implemented it in the R package plyr.[^wickham11] In pandas, `groupby` splits a `Series` or `DataFrame` by one or more keys, applies a function to each group and combines the results, a design credited to Wickham's term.[^mck10] An **aggregation** returns one value per group; a **transform** returns an object of the same shape as the group, or a scalar broadcast to it.[^mck10] A **filter** keeps or drops whole groups (Core). The aggregation case is SQL's `GROUP BY` ([[SQL]]). **Reshaping** moves between the **long** layout, one row per observation,[^wickham14] and the **wide** layout, one column per value of a variable: `melt` lengthens a table and `pivot` widens it back.[^mck8]

## Why it matters

- **Normalization within groups**: library sizes and counts per million are per-sample transforms ([[Count Normalization]]); per-gene z-scores for a heatmap are per-gene transforms ([[Standard Score]]).
- **Summaries and filters**: mean expression per gene and condition, reads per batch, variants per chromosome and sample in [[10-genomic-pipeline]]; genes kept only if they have enough reads in enough samples.
- **Collapsing replicates**: summing the lanes of a library, or the cells of a sample in single-cell data, the aggregation step of [[Pseudobulk Differential Expression]].
- **Layouts**: count matrices are exchanged wide (genes × samples, [[Count Matrix]]), while joins with metadata, grouping and plotting want long tables ([[Tidy Data]]).

## Core (L2)

Outputs come from pandas 3.0.6, NumPy 2.4.6 and SciPy 1.17.1 on Python 3.11.

![[split-apply-combine-groupby.svg]]

**By hand first.** The invented count matrix (4 genes × 6 samples) of [[Data Frame]], melted to one row per measurement, then the mean per gene and condition with a dictionary of lists:

```python
from collections import defaultdict

import numpy as np
import pandas as pd

samples = ["S1", "S2", "S3", "S4", "S5", "S6"]
condition = dict(zip(samples, ["ctrl"] * 3 + ["heat"] * 3))
wide = pd.DataFrame([[120, 100, 90, 400, 380, 420],
                     [30, 45, 38, 10, 12, 9],
                     [0, 2, 1, 1, 0, 3],
                     [50, 53, 47, 0, 60, 55]],
                    index=pd.Index(["g1", "g2", "g3", "g4"], name="gene_id"),
                    columns=pd.Index(samples, name="sample_id"))          # invented: genes x samples
long = wide.reset_index().melt(id_vars="gene_id", value_name="count")   # wide -> long
long["condition"] = long["sample_id"].map(condition)

groups = defaultdict(list)                                    # split: key -> list of values
for gene, cond, n in zip(long["gene_id"], long["condition"], long["count"]):
    groups[(gene, cond)].append(int(n))
means = {key: sum(v) / len(v) for key, v in groups.items()}  # apply: one value per group
print({f"{g}/{c}": round(m, 1) for (g, c), m in sorted(means.items())})   # combine
```

```text
{'g1/ctrl': 103.3, 'g1/heat': 400.0, 'g2/ctrl': 37.7, 'g2/heat': 10.3, 'g3/ctrl': 1.0, 'g3/heat': 1.3, 'g4/ctrl': 50.0, 'g4/heat': 38.3}
```

**Aggregate.** `groupby(keys)[column]` followed by a reduction gives one row per group, indexed by the keys:

```python
by = long.groupby(["gene_id", "condition"])["count"].mean()
print(by.round(1).unstack())
summary = long.groupby("gene_id").agg(total=("count", "sum"), n_zero=("count", lambda s: int((s == 0).sum())),
                                      n_samples=("sample_id", "nunique"))
print(summary.to_dict("index"))
```

```text
condition   ctrl   heat
gene_id                
g1         103.3  400.0
g2          37.7   10.3
g3           1.0    1.3
g4          50.0   38.3
{'g1': {'total': 1510, 'n_zero': 0, 'n_samples': 6}, 'g2': {'total': 144, 'n_zero': 0, 'n_samples': 6}, 'g3': {'total': 7, 'n_zero': 2, 'n_samples': 6}, 'g4': {'total': 265, 'n_zero': 1, 'n_samples': 6}}
```

`unstack` moves the condition level of the index to the columns, a long-to-wide reshape of the result. Named aggregations (`total=("count", "sum")`) build a per-gene summary table in one call.

**Transform.** The library size of each sample, broadcast back to every row of that sample:

```python
long["lib_size"] = long.groupby("sample_id")["count"].transform("sum")
long["cpm"] = long["count"] / long["lib_size"] * 1e6
print(long.drop_duplicates("sample_id")["lib_size"].tolist(), long.groupby("sample_id")["cpm"].sum().round(6).unique(), long.shape)
```

```text
[200, 200, 176, 411, 452, 487] [1000000.] (24, 6)
```

The table keeps its 24 rows, and each sample's counts per million sum to $10^6$. In SQL the same result is a window function, `sum(count) OVER (PARTITION BY sample_id)` ([[SQL]]).

**Filter.** Keep the genes with at least 10 reads in at least 3 samples:

```python
kept = long.groupby("gene_id").filter(lambda g: (g["count"] >= 10).sum() >= 3)
n_ok = (long["count"] >= 10).groupby(long["gene_id"]).transform("sum")
print(sorted(kept["gene_id"].unique()), long.loc[n_ok >= 3, "gene_id"].unique().tolist())
```

```text
['g1', 'g2', 'g4'] ['g1', 'g2', 'g4']
```

`filter` calls a Python function once per group; the second form gets the same selection from a built-in group sum and a row mask.

**Reshape: long and wide.** `melt` (above) lengthens; `pivot` widens and needs each (row, column) pair to occur once:

```python
back = long.pivot(index="gene_id", columns="sample_id", values="count")
print(back.equals(wide), back.shape)
lane2 = pd.DataFrame({"gene_id": ["g1"], "sample_id": ["S1"], "count": [35]})   # invented second lane
dup = pd.concat([long[["gene_id", "sample_id", "count"]], lane2], ignore_index=True)
try:
    dup.pivot(index="gene_id", columns="sample_id", values="count")
except ValueError as err:
    print("ValueError:", err)
print(dup.pivot_table(index="gene_id", columns="sample_id", values="count").loc["g1", "S1"],
      dup.pivot_table(index="gene_id", columns="sample_id", values="count", aggfunc="sum").loc["g1", "S1"])
```

```text
True (4, 6)
ValueError: Index contains duplicate entries, cannot reshape
77.5 155
```

A second lane for S1 and g1 makes the cell ambiguous. `pivot` refuses; `pivot_table`, which aggregates,[^mck10] silently averages the two lanes (77.5) unless told to sum them (155). Reads of one library sequenced on two lanes add up, so the mean halves the count without any error.

## Advanced (L3)

**Keys with missing values, and categories.**

```python
batch = {"S1": "b1", "S2": "b1", "S3": "b2", "S4": "b1", "S5": None, "S6": "b2"}   # S5: batch unknown
long["batch"] = long["sample_id"].map(batch)
print(long.groupby("batch")["sample_id"].nunique().to_dict(),
      long.groupby("batch", dropna=False)["sample_id"].nunique().to_dict())
m = pd.DataFrame({"g": ["a", "a", "b"], "x": [1.0, np.nan, 3.0]})
print(m.groupby("g")["x"].agg(["size", "count", "mean"]).to_dict())
long["condition"] = long["condition"].astype(pd.CategoricalDtype(["ctrl", "heat", "cold"]))
print(long.groupby("condition")["count"].sum().to_dict(),
      long.groupby("condition", observed=False)["count"].sum().to_dict())
```

```text
{'b1': 3, 'b2': 2} {'b1': 3, 'b2': 2, nan: 1}
{'size': {'a': 2, 'b': 1}, 'count': {'a': 1, 'b': 1}, 'mean': {'a': 1.0, 'b': 3.0}}
{'ctrl': 576, 'heat': 1350} {'ctrl': 576, 'heat': 1350, 'cold': 0}
```

Rows whose key is missing belong to no group by default: S5 vanishes from the batch summary. `size` counts rows, while `count` and `mean` skip missing values. Categorical keys list only the observed categories here; the same call run under pandas 2.3.3 also listed the unused `cold` with a sum of 0, with a warning that the default of `observed` would change. Pass `dropna=` and `observed=` explicitly.

**How the groups are found.** Grouping turns each key into an integer code, then reduces the values by code. `np.unique` finds the codes by sorting, so they follow the sorted keys; `pd.factorize` numbers keys in order of first appearance, the order that a single pass with a [[Hash Table]] produces. One `np.bincount` then sums every group at once:

```python
keys, codes = np.unique(long["sample_id"].to_numpy(), return_inverse=True)   # sort-based codes
sums = np.bincount(codes, weights=long["count"].to_numpy())
print(keys, sums, np.array_equal(sums, long.groupby("sample_id")["count"].sum().to_numpy()))
codes_h, uniques_h = pd.factorize(pd.Series(["S2", "S1", "S2", "S3"]))           # first-appearance codes
print(codes_h, uniques_h.tolist())
```

```text
['S1' 'S2' 'S3' 'S4' 'S5' 'S6'] [200. 200. 176. 411. 452. 487.] True
[0 1 0 2] ['S2', 'S1', 'S3']
```

**Group sums as a matrix product.** With the one-hot membership matrix $G$ (rows × groups), group sums are $G^\top X$. For a sparse cells × genes count matrix, this is the per-sample, per-cell-type aggregation of [[Pseudobulk Differential Expression]], computed without densifying ([[Sparse Matrix]]):

```python
import scipy.sparse as sp

X = sp.csr_matrix(np.array([[0, 3, 1], [2, 0, 0], [0, 0, 4], [1, 1, 0],
                            [0, 5, 0], [3, 0, 2], [0, 0, 1], [1, 2, 0]]))   # invented: 8 cells x 3 genes
cells = pd.DataFrame({"sample": list("AAAABBBB"), "cell_type": list("TTMMTMMM")})
codes_c, groups_c = pd.factorize(cells["sample"] + "|" + cells["cell_type"])
G = sp.csr_matrix((np.ones(len(codes_c)), (np.arange(len(codes_c)), codes_c)))   # cells x groups, one-hot
pseudo = (G.T @ X).toarray()
ref = pd.DataFrame(X.toarray()).groupby([cells["sample"], cells["cell_type"]], sort=False).sum()
print(groups_c.tolist(), G.shape, np.array_equal(pseudo, ref.to_numpy()))
print(pseudo.tolist())
```

```text
['A|T', 'A|M', 'B|T', 'B|M'] (8, 4) True
[[2.0, 3.0, 1.0], [1.0, 1.0, 4.0], [0.0, 5.0, 0.0], [4.0, 2.0, 3.0]]
```

## Mathematical representation

- Rows $R = \{1, \dots, n\}$ and a key function $\kappa : R \to K$ (a column, or a tuple of columns). The groups $R_k = \kappa^{-1}(k)$, $k \in \kappa(R)$, **partition** $R$: they are non-empty, disjoint and cover $R$ (rows with a missing key are excluded first unless `dropna=False`).
- **Aggregate**: $f$ maps a multiset of values to one value, and the result $g(k) = f(\{\!\{x_r : r \in R_k\}\!\})$ has $|\kappa(R)|$ rows.
- **Transform**: $t$ maps the vector $x_{R_k}$ to a vector of the same length, and $y_r = t(x_{R_{\kappa(r)}})_r$ has $n$ rows; counts per million are $y_r = 10^6\, x_r / \sum_{s \in R_{\kappa(r)}} x_s$. **Filter**: keep $\bigcup \{R_k : p(x_{R_k})\}$ for a predicate $p$ on groups.
- **Matrix form**: $G \in \{0, 1\}^{n \times |K|}$ with $G_{rk} = [\kappa(r) = k]$. Group sums are $G^\top x$, group sizes $G^\top \mathbf{1}$, group means $(G^\top x) \oslash (G^\top \mathbf{1})$ (element-wise division), and the transform "group total on every row" is $G G^\top x$.
- **Decomposability**: if the rows are split into chunks $A$ and $B$, $\mathrm{sum}(A \cup B) = \mathrm{sum}(A) + \mathrm{sum}(B)$ and $\mathrm{mean}(A \cup B) = \frac{\mathrm{sum}(A) + \mathrm{sum}(B)}{|A| + |B|}$, so chunked or parallel group-bys combine partial (sum, count) pairs; no function of the two medians alone gives the median of $A \cup B$ (Exercise 3).
- **Reshape**: the long table is a relation on (gene, sample, value). `pivot` builds the matrix $X_{ij}$ only if (gene, sample) is a key, so that the relation is a function of the pair; otherwise one value per cell must be chosen by an aggregation.

## Computational representation

| Operation | pandas | SQL |
|---|---|---|
| aggregate | `df.groupby(k)[c].agg(f)`, named `agg(name=(c, f))` | `SELECT k, f(c) FROM t GROUP BY k` |
| keep groups by a condition | `df.groupby(k).filter(p)`, or a transform plus a mask | `HAVING` (on aggregated rows) |
| transform | `df.groupby(k)[c].transform(f)` | `f(c) OVER (PARTITION BY k)` |
| wide → long | `df.melt(id_vars=..., var_name=..., value_name=...)` | |
| long → wide | `pivot` (unique pairs), `pivot_table(aggfunc=...)`, `unstack` | |

## Worked example

> [!example] Mean counts per million of the filtered genes, per condition
> 1. **Transform, filter, aggregate**: counts per million within each sample (library sizes 200, 200, 176, 411, 452, 487); drop g3, which has fewer than 3 samples with 10 reads or more; mean per gene and condition, unstacked to gene × condition, with the $\log_2$ ratio heat over control.
> ```python
> kept_cpm = long[n_ok >= 3]
> table = kept_cpm.groupby(["gene_id", kept_cpm["condition"].astype(str)])["cpm"].mean().unstack()
> table["log2_ratio"] = np.log2(table["heat"] / table["ctrl"])
> print(table.round(2))
> ```
> ```text
> condition       ctrl       heat  log2_ratio
> gene_id                                    
> g1         537121.21  892122.32        0.73
> g2         196969.70   23120.02       -3.09
> g4         260681.82   81893.24       -1.67
> ```
> 2. **Read with care**: three samples per condition and no variance model, so these ratios describe the toy data, nothing more; testing them is [[Differential Expression Analysis]]. g4's ratio is pulled down by S4's zero, which a mean over three samples cannot absorb.

## Common misconceptions

> [!warning] "`pivot_table` is a `pivot` that never fails"
> It never fails because it aggregates duplicate cells, by default with the mean. Two lanes of one library are averaged instead of summed: use `pivot` to detect duplicates, then aggregate deliberately.

> [!warning] "A group-by keeps every row"
> Rows with a missing key are dropped by default, and unused categories are hidden in pandas 3.0.6 but were shown by default in 2.3.3. State `dropna` and `observed`.

> [!warning] "The mean of the group means is the overall mean"
> Only when the groups have equal sizes (or equal means). With invented values 1, 2, 3 (ctrl) and 10 (heat), the group means 2 and 10 average to 6, while the overall mean is $16/4 = 4 = \sum_k \frac{n_k}{n} \bar x_k$, the mean of the group means weighted by the group sizes $n_k$.

## Exercises

> [!question] Exercise 1 (L2)
> With `long`, write one expression each for: (a) the number of zero counts per sample; (b) the mean count per gene and condition as a gene × condition table; (c) each count as a fraction of its sample's total. Which are aggregations and which transforms?

> [!success]- Solution
> ```python
> zeros = long.groupby("sample_id")["count"].agg(lambda s: int((s == 0).sum()))                # aggregate
> cond_mean = long.groupby(["gene_id", "condition"], observed=True)["count"].mean().unstack()  # aggregate, reshape
> frac = long["count"] / long.groupby("sample_id")["count"].transform("sum")                   # transform
> print(zeros.to_dict(), cond_mean.loc["g2"].round(1).to_dict(), frac.groupby(long["sample_id"]).sum().round(12).unique())
> ```
> ```text
> {'S1': 1, 'S2': 0, 'S3': 0, 'S4': 1, 'S5': 1, 'S6': 0} {'ctrl': 37.7, 'heat': 10.3} [1.]
> ```
> (a) and (b) return one row per group; (c) returns one value per row, which is why it can be divided into `long["count"]` directly, and its per-sample sums equal 1.

> [!question] Exercise 2 (L2)
> A count matrix of 20,000 genes × 12 samples is melted to long form. How many rows result? After a join with an annotation table, two rows share the gene symbol `ABC1` (two gene identifiers with one symbol). What happens if you pivot back with the symbol as index, and what is the fix?

> [!success]- Solution
> $20\,000 \times 12 = 240\,000$ rows. With the symbol as index, (`ABC1`, sample) occurs twice for every sample: `pivot` raises a `ValueError` and `pivot_table` silently averages the two genes. Pivot on the unique gene identifier and keep the symbol as an attribute ([[Accession Number]]).

> [!question] Exercise 3 (L3, Python)
> Split `long` into two chunks (rows 0 to 9 and 10 to 23), as if they came from two files. Recover the per-gene mean from per-chunk partial results, and show that the median cannot be recovered from per-chunk medians.

> [!success]- Solution
> ```python
> chunks = [long.iloc[:10], long.iloc[10:]]                     # e.g. two files or two workers
> partial = [c.groupby("gene_id")["count"].agg(["sum", "count"]) for c in chunks]
> tot = partial[0].add(partial[1], fill_value=0)
> print((tot["sum"] / tot["count"]).round(2).to_dict())
> print(long.groupby("gene_id")["count"].mean().round(2).to_dict())
> med_of_med = pd.concat([c.groupby("gene_id")["count"].median() for c in chunks], axis=1).median(axis=1)
> print(med_of_med.to_dict(), long.groupby("gene_id")["count"].median().to_dict())
> ```
> ```text
> {'g1': 251.67, 'g2': 24.0, 'g3': 1.17, 'g4': 44.17}
> {'g1': 251.67, 'g2': 24.0, 'g3': 1.17, 'g4': 44.17}
> {'g1': 250.0, 'g2': 24.0, 'g3': 1.0, 'g4': 51.25} {'g1': 250.0, 'g2': 21.0, 'g3': 1.0, 'g4': 51.5}
> ```
> The (sum, count) pairs combine exactly; the median of the chunk medians misses the true median for g2 and g4. Exact medians need all values of a group, or a sort, which is why out-of-memory and parallel group-bys favour decomposable statistics ([[Out-of-Core Computation]]).

## Mastery checklist

- [ ] 1 Recognized: I can name the three steps and the three kinds of apply (aggregate, transform, filter), and the two layouts (long, wide).
- [ ] 2 Understood: I can predict the shape of each kind of result, explain why `pivot` can fail and `pivot_table` can mislead, and relate each operation to SQL.
- [ ] 3 Practiced: I can implement a group-by by hand and with `np.unique` and `np.bincount`, and normalize, filter, summarize and reshape a count table with pandas.
- [ ] 4 Applied: [[10-genomic-pipeline]] summarizes per-sample and per-chromosome results with group-bys whose keys, missing values and categories are explicit.
- [ ] 5 Explained: I can teach the partition model, the matrix form $G^\top X$, why means decompose and medians do not, and the pseudobulk aggregation of single-cell counts.

## References

[^wickham11]: [[Wickham 2011 - The Split-Apply-Combine Strategy for Data Analysis]], *Journal of Statistical Software* 40(1):1-29: the strategy of splitting a problem into pieces, operating on each independently and recombining, implemented in the plyr package.
[^mck10]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 10 "Data Aggregation and Group Operations": the split-apply-combine term credited to Hadley Wickham, `groupby` on one or more keys, `apply` and `transform` (a scalar broadcast to the group or a result of the group's shape), pivot tables as aggregations.
[^mck8]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 8 "Data Wrangling: Join, Combine, and Reshape": `melt` from wide to long as the inverse of `pivot`.
[^wickham14]: [[Wickham 2014 - Tidy Data]], *Journal of Statistical Software* 59(10): each observation forms a row, each variable a column.
