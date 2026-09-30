---
aliases:
  - Regression
  - Regression Models
  - Modèles linéaires
tags:
  - type/moc
  - domain/statistics
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Statistical Inference]]"
  - "[[Linear Algebra]]"
projects: []
sources:
  - "[[MIT 18.650 - Statistics for Applications]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[Stanford - Statistical Learning with Python]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[An Introduction to Statistical Learning (James)]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Introduction to Linear Algebra (Strang)]]"
---

# Linear Models

> [!abstract]
> Explaining a response by predictors: linear regression and ANOVA, design matrices and contrasts, generalized linear models for binary and count data, mixed models and survival models.

## Why it matters for bioinformatics

- **Differential expression is a linear model.** Tools for RNA-seq fit a negative binomial generalized linear model per gene, with a design matrix that encodes condition, batch and pairing, and test contrasts.
- **Genetic association is regression**: logistic regression for case-control GWAS, linear regression for quantitative traits and eQTLs, linear mixed models to correct for relatedness and population structure.
- **Clinical genomics** relates molecular profiles to patient survival with Kaplan-Meier curves and Cox models.

## Before you start

- [[Statistical Inference]]: [[Maximum Likelihood Estimation]], [[Hypothesis Testing]], [[F-Distribution]], [[Likelihood Ratio Test]] and [[Model Selection]] (for GLMs).
- [[Linear Algebra]]: [[Matrix]], [[Least Squares]], [[Orthogonal Projection]], [[Matrix Rank]].
- [[Probability]]: [[Binomial Distribution]], [[Poisson Distribution]], [[Negative Binomial Distribution]].
- [[Descriptive Statistics]]: [[Correlation]], [[Scatter Plot]].

## Learning path

### Stage 2 - Core (L2)

1. [[Linear Regression]] (L2): fit $y = \beta_0 + \beta_1 x + \varepsilon$ by least squares, test the slope and predict with intervals. Bio: a qPCR standard curve; regression of offspring on mid-parent phenotype, whose slope estimates narrow-sense heritability.
2. [[Coefficient of Determination]] (L2): compute and interpret $R^2$ as variance explained. Bio: the share of expression variance explained by genotype at an eQTL.
3. [[Regression Diagnostics]] (L2): check residuals, leverage, influence and constant variance. Bio: count data violate constant variance, which motivates transformations and GLMs.
4. [[Multiple Linear Regression]] (L2): fit several predictors, including polynomial terms, and interpret adjusted coefficients. Bio: an association test adjusted for age, sex and ancestry components.
5. [[Design Matrix]] (L2): encode an experiment as a matrix $X$ and check that it has full rank. Bio: the `~ batch + condition` design of a differential expression analysis.
6. [[Dummy Variable]] (L2): encode categorical predictors with a reference level. Bio: conditions and tissues; additive genotype coding 0/1/2.
7. [[Interaction Effect]] (L2): model effects that depend on another variable. Bio: genotype by environment; treatment response that differs between strains.
8. [[Multicollinearity]] (L2): detect correlated predictors and their effect on estimates. Bio: SNPs in linkage disequilibrium; batch confounded with condition.
9. [[Analysis of Variance]] (L2): compare several group means with the F-test, one-way and two-way, with post hoc comparisons. Bio: expression across several tissues; partitioning variance between factors.

### Stage 3 - Advanced (L3)

10. [[Linear Contrast]] (L3): test specific combinations of coefficients. Bio: treated versus control within one genotype in a multi-group design.
11. [[Generalized Linear Model]] (L3): combine a linear predictor, a link function and an exponential-family response; read deviance. Bio: the common framework of logistic, Poisson and negative binomial models in genomics.
12. [[Logistic Regression]] (L3): model a binary outcome and interpret odds ratios. Bio: case-control association tests; simple disease classifiers.
13. [[Poisson Regression]] (L3): model counts with an offset for exposure. Bio: read counts with library size as offset; mutation counts per gene length.
14. [[Overdispersion]] (L3): detect variance above the Poisson mean. Bio: biological variability between RNA-seq replicates.
15. [[Negative Binomial Regression]] (L3): fit counts with a dispersion parameter. Bio: the model of standard RNA-seq differential expression tools.
16. [[Survival Analysis]] (L3): handle time-to-event data with censoring; hazard and survival functions. Bio: patient survival related to a mutation or an expression signature.
17. [[Kaplan-Meier Estimator]] (L3): estimate and compare survival curves (log-rank test). Bio: survival curves by tumor subtype.
18. [[Cox Proportional Hazards Model]] (L3): estimate hazard ratios adjusted for covariates. Bio: prognostic value of a biomarker beyond clinical stage.

### Stage 4 - Frontier (M1)

19. [[Linear Mixed Model]] (M1): combine fixed and random effects; understand variance components. Bio: repeated measures on patients; GWAS models that correct for relatedness and population structure.

> [!tip] How to study it
> Do items 1 to 9 with the matrix view from [[Linear Algebra]] (the fit is a projection). Then learn GLMs (items 11 to 15) on real RNA-seq counts: fit one gene by hand, then compare with a differential expression tool.

## Uses from other domains

- [[Genome-Wide Association Study]], [[Population Stratification]] ([[Population Genomics]]): regression with covariates and mixed models.
- [[Differential Expression Analysis]], [[Dispersion Estimation]] ([[Transcriptomics]]): negative binomial GLMs, design matrices, contrasts.
- [[Clinical Genomics]]: survival models.
- [[Randomized Block Design]], [[Batch Effect]] ([[Experimental Design]]): design matrices are decided before the experiment; confounding makes them rank-deficient.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 18.650 - Statistics for Applications]] | MIT | L3 | Linear regression and generalized linear models, theory (items 1-5, 11-15)[^18650] |
| [[Stanford - Statistical Learning with Python]] | Stanford Online | L3 | Linear and polynomial regression, logistic regression, survival models (items 1-4, 12, 16-18)[^slp] |
| [[HarvardX PH525x - Data Analysis for the Life Sciences]] | Harvard (edX) | L2-L3 | Linear models and matrix algebra for life-science data (items 1-10)[^ph525] |
| [[MIT 18.05 - Introduction to Probability and Statistics]] | MIT | L1-L2 | Linear regression as the end of a first course (item 1)[^1805] |

## Reference books

- [[An Introduction to Statistical Learning (James)]]: chapter 3 (linear regression), chapter 4 (classification, including logistic regression), chapter 11 (survival analysis and censored data).[^isl]
- [[Modern Statistics for Modern Biology (Holmes)]]: count data from sequencing and generalized linear models for differential expression (items 11-15).[^msmb]
- [[Introductory Statistics (OpenStax)]]: linear regression and correlation; F distribution and one-way ANOVA (items 1, 9).[^openstax]
- [[Introduction to Linear Algebra (Strang)]]: least squares and projections, the geometry of items 1 to 5.[^strang]

## Lab projects

No Lab project is built on linear models yet. They enter the Lab with differential expression in [[Transcriptomics]] and association testing in [[Population Genomics]].

## References

[^18650]: [[MIT 18.650 - Statistics for Applications]], regression and GLM part (structure of the Fall 2016 run as described in the source note).
[^slp]: [[Stanford - Statistical Learning with Python]]: regression, classification, survival models.
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.2x to 4x (linear models and matrix algebra).
[^1805]: [[MIT 18.05 - Introduction to Probability and Statistics]], regression part.
[^isl]: [[An Introduction to Statistical Learning (James)]], Python edition; chapter numbers checked against the official ISLP lab notebooks (Ch03, Ch04, Ch11).
[^msmb]: [[Modern Statistics for Modern Biology (Holmes)]], high-throughput count data.
[^openstax]: [[Introductory Statistics (OpenStax)]], 2nd ed., later chapters.
[^strang]: [[Introduction to Linear Algebra (Strang)]], least squares part.
