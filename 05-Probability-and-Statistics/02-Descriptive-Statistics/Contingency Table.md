---
aliases:
  - Cross-Tabulation
  - Crosstab
  - Two-Way Table
  - 2x2 Table
  - Table de contingence
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Level of Measurement]]"
  - "[[Frequency Distribution]]"
  - "[[Conditional Probability]]"
related:
  - "[[Chi-Square Test]]"
  - "[[Fisher's Exact Test]]"
  - "[[Independence (Probability)]]"
  - "[[Joint Distribution]]"
  - "[[Effect Size]]"
  - "[[Simpson's Paradox]]"
  - "[[Confusion Matrix]]"
  - "[[Genome-Wide Association Study]]"
  - "[[Hardy-Weinberg Equilibrium]]"
  - "[[Correspondence Analysis]]"
projects: []
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Clarke 2011 - Basic Statistical Analysis in Genetic Case-Control Studies]]"
  - "[[Leek 2010 - Tackling the Widespread and Critical Impact of Batch Effects]]"
  - "[[Python for Data Analysis (McKinney)]]"
---

# Contingency Table

> [!abstract]
> A contingency table counts how often each combination of categories of two categorical variables occurs, for example how many cases and how many controls carry each genotype.

## Definition

A **contingency table** (two-way table, cross-tabulation) displays the frequencies of two categorical variables together: the categories of one variable label the rows, those of the other label the columns, and each cell counts the observations that fall in that row and that column. Its row and column totals, the **margins**, are the [[Frequency Distribution|frequency distributions]] of each variable alone, and the table makes joint and conditional probabilities easy to read.[^os3]

## Why it matters

- **Genetic association.** A case-control study at one SNP starts as a table of genotype counts in cases and in controls; the allelic, genotypic and trend tests and the odds ratio are all computed from it.[^clarke] A [[Genome-Wide Association Study]] builds one such table per [[Single Nucleotide Polymorphism|SNP]].
- **Design checks.** Cross-tabulating condition by sequencing run or processing date shows at once whether technical batches line up with biological groups, the situation in which batch effects masquerade as biology.[^leek] See [[Batch Effect]].
- **Everywhere else.** A gene list against a Gene Ontology term is a 2 × 2 table ([[Over-Representation Analysis]], [[Fisher's Exact Test]]); predicted against true labels is a [[Confusion Matrix]]; cluster labels against annotated cell types is a table to read before trusting a clustering.

## Core (L1)

**From records to a table.** A sample sheet has one row per individual and one column per variable ([[Tidy Data]]). Counting each (status, genotype) pair gives the table. Invented toy data, one SNP with alleles A and G:

| | AA | AG | GG | Total |
|---|---:|---:|---:|---:|
| Cases | 180 | 240 | 80 | **500** |
| Controls | 245 | 210 | 45 | **500** |
| Total | **425** | **450** | **125** | **1000** |

**Three kinds of proportions** come out of one table:[^os3]

- **Joint**: a cell over the grand total, $80/1000 = 0.08$ of everyone is a GG case.
- **Marginal**: a total over the grand total, $125/1000 = 0.125$ of everyone is GG.
- **Conditional**: a cell over its row or column total. Row profile: $P(\text{GG} \mid \text{case}) = 80/500 = 0.16$ against $45/500 = 0.09$ in controls. Column profile: $P(\text{case} \mid \text{GG}) = 80/125 = 0.64$.

**Which percentages to compare.** Percentages should run within the groups you want to compare. In a case-control study the investigator fixes the numbers of cases and controls, so the row profiles (genotype distribution in cases against controls) are the meaningful comparison. The column profiles depend on that choice: the 64 % of cases among GG carriers reflects a 50:50 design, not the risk of disease of a GG person in the population.

![[contingency-mosaic-genotype.svg]]

A **mosaic plot** draws the table: column widths are the genotype totals, and each column is split by the share of cases. If status and genotype were unrelated, every split would sit at the same height.

## Deeper (L2)

**Independence and expected counts.** The two variables are independent when every joint probability is the product of its margins ([[Independence (Probability)]]); then all row profiles are identical, and so are all column profiles. The counts expected under independence are

$$E_{ij} = \frac{n_{i+}\, n_{+j}}{n},$$

so for the toy cases: $500 \times 425 / 1000 = 212.5$ AA, $225$ AG and $62.5$ GG, against 180, 240 and 80 observed. Cases carry G more often than independence predicts.

**From description to inference.** The [[Chi-Square Test]] of independence measures how far observed counts are from expected ones; its validity requires expected counts of at least 5 in each cell.[^os] With smaller counts, [[Fisher's Exact Test]] computes the probability exactly. This note stops at description: the tests belong to [[Statistical Inference]].

**The odds ratio.** For a 2 × 2 table $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the odds of the first column are $a/b$ in row 1 and $c/d$ in row 2, and their ratio is

$$\mathrm{OR} = \frac{a/b}{c/d} = \frac{ad}{bc}.$$

$\mathrm{OR} = 1$ under independence; $\mathrm{OR} > 1$ means the first column is relatively more frequent in the first row. It is the standard measure of association in genetic case-control studies.[^clarke] Collapsing the toy genotypes to alleles (each person carries two) gives G:A = 400:600 in cases and 300:700 in controls, so the allelic odds ratio is $(400 \times 700)/(600 \times 300) \approx 1.56$, an [[Effect Size]] to report next to any p-value.

## Advanced (L3)

**Genotype tables in association studies.** One SNP gives several tables, each matching a disease model:[^clarke]

| Table | Built from | Question |
|---|---|---|
| 2 × 3 genotypic | counts of AA, AG, GG | any difference in genotype distribution |
| 2 × 2 allelic | $2n$ allele counts | is allele G more frequent in cases? |
| 2 × 2 dominant or recessive | AG + GG against AA, or GG against AA + AG | does one copy, or two copies, matter? |
| 2 × 3 with ordered columns | 0, 1, 2 copies of G | is there a dose trend (Cochran-Armitage)? |

The allelic table counts $2n$ alleles as if they were independent draws. That holds only when the two alleles of a person are independent, which is [[Hardy-Weinberg Equilibrium]]; the trend test keeps people as the unit and works on the genotype table. The toy data were built in Hardy-Weinberg proportions in both groups (controls: $0.7^2, 2 \times 0.7 \times 0.3, 0.3^2$ of 500 give 245, 210, 45).

**Three-way tables and confounding.** Splitting a table by a third variable (population, batch, sex) gives one table per stratum. An association in the pooled table can vanish or reverse within strata ([[Simpson's Paradox]], [[Confounding]]): if cases are recruited mostly from a population where a variant is common, pooling creates an association with no biological link (Exercise 5, and [[Population Stratification]] for the GWAS version).

**Large tables.** Codon counts by gene or taxon counts by site are tables with many rows and columns. Their row and column profiles can be mapped in a few dimensions by [[Correspondence Analysis]].

## Mathematical representation

Let $X$ have categories $1, \dots, I$ (rows) and $Y$ categories $1, \dots, J$ (columns), observed on $n$ units.

- Cell counts $n_{ij} = \#\{\text{units with } X = i,\ Y = j\}$; margins $n_{i+} = \sum_j n_{ij}$, $n_{+j} = \sum_i n_{ij}$, and $n = \sum_{i,j} n_{ij}$.
- Joint, marginal and conditional relative frequencies: $\hat p_{ij} = n_{ij}/n$, $\hat p_{i+} = n_{i+}/n$, $\hat p_{j \mid i} = n_{ij}/n_{i+}$.
- **Independence**: $p_{ij} = p_{i+}\, p_{+j}$ for all $i, j$, equivalently $p_{j \mid i} = p_{+j}$ for every row. Plugging in the observed margins gives $E_{ij} = n \hat p_{i+} \hat p_{+j} = n_{i+} n_{+j}/n$, and the $E_{ij}$ have the same margins as the data.
- **Free cells**: once the margins are fixed, filling $(I - 1)(J - 1)$ cells determines the rest (the last row and column follow by subtraction). This is the degrees of freedom of the [[Chi-Square Test]] of independence.
- **Odds ratio invariance**: multiplying row 2 by $k > 0$ (sampling $k$ times more controls) gives $\frac{a \cdot kd}{b \cdot kc} = \frac{ad}{bc}$; the same holds for a column. This is why the odds ratio, unlike the column percentages, does not depend on the case:control ratio chosen by the design.

## Computational representation

A `Counter` of tuples is a sparse contingency table: absent combinations have count 0.

```python
from collections import Counter

# Invented toy data: genotypes at one SNP (alleles A and G) in 500 cases and 500 controls.
COUNTS = {("case", "AA"): 180, ("case", "AG"): 240, ("case", "GG"): 80,
          ("control", "AA"): 245, ("control", "AG"): 210, ("control", "GG"): 45}
records = [key for key, k in COUNTS.items() for _ in range(k)]   # one (status, genotype) per person


def crosstab(pairs):
    """Count (row, column) pairs: the table, its row labels and column labels."""
    table = Counter(pairs)
    rows = sorted({r for r, _ in table})
    cols = sorted({c for _, c in table})
    return table, rows, cols


def margins(table, rows, cols):
    row_tot = {r: sum(table[r, c] for c in cols) for r in rows}
    col_tot = {c: sum(table[r, c] for r in rows) for c in cols}
    return row_tot, col_tot, sum(row_tot.values())


table, rows, cols = crosstab(records)
row_tot, col_tot, n = margins(table, rows, cols)
print(f"{'':<8}" + "".join(f"{c:>6}" for c in cols) + f"{'total':>7}")
for r in rows:
    print(f"{r:<8}" + "".join(f"{table[r, c]:>6}" for c in cols) + f"{row_tot[r]:>7}")
print(f"{'total':<8}" + "".join(f"{col_tot[c]:>6}" for c in cols) + f"{n:>7}")

print({r: {c: round(table[r, c] / row_tot[r], 3) for c in cols} for r in rows})   # row profiles
print({c: round(table["case", c] / col_tot[c], 3) for c in cols})                  # P(case | genotype)
print({c: row_tot["case"] * col_tot[c] / n for c in cols})                         # expected case counts


def odds_ratio(a, b, c, d):
    """Odds ratio of the 2x2 table [[a, b], [c, d]]: (a*d) / (b*c)."""
    return a * d / (b * c)


alleles = {r: {"G": 2 * table[r, "GG"] + table[r, "AG"],
               "A": 2 * table[r, "AA"] + table[r, "AG"]} for r in rows}
print(alleles)
print(round(odds_ratio(alleles["case"]["G"], alleles["case"]["A"],
                       alleles["control"]["G"], alleles["control"]["A"]), 3))
```

```text
            AA    AG    GG  total
case       180   240    80    500
control    245   210    45    500
total      425   450   125   1000
{'case': {'AA': 0.36, 'AG': 0.48, 'GG': 0.16}, 'control': {'AA': 0.49, 'AG': 0.42, 'GG': 0.09}}
{'AA': 0.424, 'AG': 0.533, 'GG': 0.64}
{'AA': 212.5, 'AG': 225.0, 'GG': 62.5}
{'case': {'G': 400, 'A': 600}, 'control': {'G': 300, 'A': 700}}
1.556
```

With a data frame, `pandas.crosstab` does the counting and the margins in one call.[^mckinney]

## Worked example

> [!example] Reading the toy genotype table (invented data)
> 1. **Margins.** 500 cases and 500 controls (fixed by design); genotype totals 425, 450, 125.
> 2. **Row profiles.** GG is 16 % of cases and 9 % of controls; AA is 36 % against 49 %. The G allele looks enriched in cases.
> 3. **Expected under independence.** Cases would have 212.5, 225 and 62.5 people in AA, AG, GG; they have 180, 240 and 80. The departure is in the same direction at every genotype: fewer AA, more G carriers.
> 4. **Effect size.** Allele counts G:A are 400:600 in cases and 300:700 in controls; OR $= (400 \times 700)/(600 \times 300) \approx 1.56$.
> 5. **What not to say.** "64 % of GG carriers get the disease" is false: that column percentage reflects the 50:50 recruitment, not a population risk.
> 6. **Next step.** Whether a departure of this size could arise by chance is the job of the [[Chi-Square Test]], not of the table.

## Common misconceptions

> [!warning] "Column percentages of a case-control table estimate risk"
> The proportion of cases in each genotype column is set by how many cases and controls were recruited. Recruit twice as many controls and every column percentage drops, while the row profiles and the odds ratio do not change.

> [!warning] "Counting alleles doubles the sample size for free"
> The allelic table has $2n$ entries, but the two alleles of one person are independent only under [[Hardy-Weinberg Equilibrium]]. When that fails, the allelic table overstates the information; the genotype table keeps the person as the unit.

> [!warning] "An association in the pooled table holds in every subgroup"
> Pooling strata with different category frequencies can create, hide or reverse an association ([[Simpson's Paradox]]). Cross-tabulate by population, batch or sex before interpreting.

## Exercises

> [!question] Exercise 1 (L1)
> From the toy genotype table, give: the joint proportion of AG controls, the marginal proportion of AG, $P(\text{AG} \mid \text{control})$ and $P(\text{control} \mid \text{AG})$. Which of the last two depends on the number of controls recruited?

> [!success]- Solution
> Joint: $210/1000 = 0.21$. Marginal: $450/1000 = 0.45$. $P(\text{AG} \mid \text{control}) = 210/500 = 0.42$. $P(\text{control} \mid \text{AG}) = 210/450 \approx 0.467$. The last one depends on the design: with more controls recruited, the share of controls in every column rises.

> [!question] Exercise 2 (L1)
> Twelve invented records (status, carrier of a variant): 4 × (case, carrier), 2 × (case, non-carrier), 1 × (control, carrier), 5 × (control, non-carrier). Build the 2 × 2 table with margins, the row profiles and the odds ratio. Is a chi-square approximation appropriate here?

> [!success]- Solution
> | | carrier | non-carrier | total |
> |---|---:|---:|---:|
> | case | 4 | 2 | 6 |
> | control | 1 | 5 | 6 |
> | total | 5 | 7 | 12 |
>
> Carriers: $4/6 \approx 67\,\%$ of cases, $1/6 \approx 17\,\%$ of controls. OR $= (4 \times 5)/(2 \times 1) = 10$. Expected counts are $6 \times 5/12 = 2.5$ and $6 \times 7/12 = 3.5$, all below 5, so the chi-square approximation is not appropriate; use [[Fisher's Exact Test]]. With 12 people, an OR of 10 is also very imprecise.

> [!question] Exercise 3 (L2)
> In the allelic toy table (cases G:A = 400:600, controls 300:700), recruit three times more controls with the same allele frequencies. Compute the new odds ratio and the new share of G alleles that come from cases. Prove the general result.

> [!success]- Solution
> Controls become 900:2100. OR $= (400 \times 2100)/(600 \times 900) \approx 1.556$, unchanged. The share of G alleles from cases falls from $400/700 \approx 0.571$ to $400/1300 \approx 0.308$. Proof: multiplying a row by $k$ multiplies both $c$ and $d$ by $k$, which cancels in $ad/(bc)$; a column share $a/(a + c)$ has no such cancellation.

> [!question] Exercise 4 (L2, Python)
> Using `table` and `odds_ratio` from the code above, compute the odds ratios of AG and GG against AA, and the dominant (AG + GG against AA) and recessive (GG against AA + AG) odds ratios. What relation do you see between the AG and GG odds ratios, and why?

> [!success]- Solution
> ```python
> def genotype_odds_ratios(t):
>     """OR of each genotype against the AA reference, plus dominant and recessive ORs."""
>     ref = (t["case", "AA"], t["control", "AA"])
>     out = {g: round(odds_ratio(t["case", g], ref[0], t["control", g], ref[1]), 3) for g in ("AG", "GG")}
>     dom = odds_ratio(t["case", "AG"] + t["case", "GG"], t["case", "AA"],
>                      t["control", "AG"] + t["control", "GG"], t["control", "AA"])
>     rec = odds_ratio(t["case", "GG"], t["case", "AA"] + t["case", "AG"],
>                      t["control", "GG"], t["control", "AA"] + t["control", "AG"])
>     out["dominant"], out["recessive"] = round(dom, 3), round(rec, 3)
>     return out
>
> print(genotype_odds_ratios(table))
> # {'AG': 1.556, 'GG': 2.42, 'dominant': 1.708, 'recessive': 1.926}
> ```
> $\mathrm{OR}_{GG} = 2.42 \approx 1.556^2 = \mathrm{OR}_{AG}^2$: each copy of G multiplies the odds by the same factor (a multiplicative model). It happens because both groups are in Hardy-Weinberg proportions with G frequency 0.4 in cases and 0.3 in controls, so $\mathrm{OR}_{AG} = \frac{2 \cdot 0.4 \cdot 0.6 / 0.6^2}{2 \cdot 0.3 \cdot 0.7 / 0.7^2} = \frac{0.4/0.6}{0.3/0.7}$, the allelic odds ratio, and $\mathrm{OR}_{GG}$ is its square.

> [!question] Exercise 5 (L3, Python)
> Two invented populations. Population 1: cases 180 carriers and 120 non-carriers, controls 60 and 40. Population 2: cases 20 and 80, controls 60 and 240. Compute the odds ratio in each population and in the pooled table, and explain the result.

> [!success]- Solution
> ```python
> strata = {  # invented: (carriers, non-carriers) among cases and among controls
>     "population 1": {"case": (180, 120), "control": (60, 40)},
>     "population 2": {"case": (20, 80), "control": (60, 240)},
> }
> pooled = {s: tuple(sum(strata[p][s][i] for p in strata) for i in (0, 1)) for s in ("case", "control")}
> for name, t in {**strata, "pooled": pooled}.items():
>     print(name, t, round(odds_ratio(*t["case"], *t["control"]), 3))
> # population 1 {'case': (180, 120), 'control': (60, 40)} 1.0
> # population 2 {'case': (20, 80), 'control': (60, 240)} 1.0
> # pooled {'case': (200, 200), 'control': (120, 280)} 2.333
> ```
> Within each population, carriers are equally frequent in cases and controls (OR = 1). But the carrier frequency is 60 % in population 1 and 20 % in population 2, and cases come mostly from population 1 (300 of 400) while controls come mostly from population 2 (300 of 400). Pooling turns a difference in ancestry into a spurious association (OR ≈ 2.33). Stratify, or match cases and controls, before interpreting ([[Population Stratification]]).

## Mastery checklist

- [ ] 1 Recognized: I can say what a contingency table, its cells and its margins are.
- [ ] 2 Understood: I can compute joint, marginal and conditional proportions and explain which conditional percentages a case-control design allows.
- [ ] 3 Practiced: I can build a table from records in Python, compute expected counts under independence and odds ratios, and collapse genotypes into allelic, dominant and recessive tables.
- [ ] 4 Applied: I cross-tabulated the metadata of a public sequencing or genotype dataset (condition by batch, status by genotype) and spotted any confounded design.
- [ ] 5 Explained: I can teach why the odds ratio survives case-control sampling, when allele counting is valid, and how pooling strata creates spurious associations.

## References

[^os3]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 3 "Probability Topics" (contingency tables).
[^os]: [[Introductory Statistics (OpenStax)]], 2nd ed., chapter on the chi-square distribution (test of independence).
[^clarke]: [[Clarke 2011 - Basic Statistical Analysis in Genetic Case-Control Studies]], *Nature Protocols* 6(2):121-133.
[^leek]: [[Leek 2010 - Tackling the Widespread and Critical Impact of Batch Effects]], *Nature Reviews Genetics*.
[^mckinney]: [[Python for Data Analysis (McKinney)]], pandas part.
