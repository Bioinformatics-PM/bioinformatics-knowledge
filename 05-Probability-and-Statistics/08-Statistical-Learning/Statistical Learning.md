---
aliases:
  - Machine Learning
  - Apprentissage statistique
tags:
  - type/moc
  - domain/statistics
  - domain/computer-science
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Linear Models]]"
  - "[[Multivariate Analysis]]"
  - "[[Optimization]]"
projects:
  - "[[05-sequence-search]]"
sources:
  - "[[An Introduction to Statistical Learning (James)]]"
  - "[[Stanford - Statistical Learning with Python]]"
  - "[[MIT 6.036 - Introduction to Machine Learning]]"
  - "[[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[MIT 6.047 - Computational Biology]]"
---

# Statistical Learning

> [!abstract]
> Learning predictive models from data and measuring how well they generalize: the supervised-learning workflow, classic classifiers, regularization, tree ensembles, support vector machines and the basics of neural networks.

## Why it matters for bioinformatics

- Prediction is everywhere: variant pathogenicity, cancer subtypes from expression, taxonomic classification of reads, cell-type annotation, protein structure and function.
- Genomic data have **many more features than samples** ($p \gg n$), which makes overfitting, regularization and honest validation central, not optional.
- **Data leakage** is the classic failure of machine learning in biology: homologous sequences or related patients in both training and test sets give results that do not replicate.

## Before you start

- [[Linear Models]]: [[Linear Regression]], [[Logistic Regression]], [[Generalized Linear Model]].
- [[Statistical Inference]]: [[Maximum Likelihood Estimation]], [[Bootstrap]], [[Sensitivity and Specificity]] (before item 10).
- [[Multivariate Analysis]]: [[Principal Component Analysis]], [[Clustering]].
- [[Optimization]]: [[Gradient Descent]], [[Stochastic Gradient Descent]], [[Convex Optimization]].
- [[Calculus]]: [[Multivariable Chain Rule]]; [[Probability]]: [[Bayes' Theorem]], [[Conditional Probability]].
- [[Discrete Mathematics]]: [[Directed Acyclic Graph]] (before item 34).

## Learning path

### Stage 2 - Core (L2)

1. [[Supervised Learning]] (L2): frame prediction from labeled examples as regression or classification. Bio: predicting a phenotype or a subtype from expression.
2. [[Unsupervised Learning]] (L2): frame structure discovery without labels and link it to [[Clustering]] and [[Dimensionality Reduction]]. Bio: discovering cell types.
3. [[Classification]] (L2): predict a category and estimate class probabilities. Bio: tumor versus normal; coding versus non-coding transcripts.
4. [[Loss Function]] (L2): choose squared error, cross-entropy or hinge loss and link it to a likelihood. Bio: what a model is actually trained to minimize.
5. [[Train-Test Split]] (L2): hold out data that the model never sees. Bio: splitting by patient, chromosome or protein family rather than by row.
6. [[Overfitting]] (L2): recognize a model that fits noise; relate it to model complexity. Bio: perfect training accuracy with 20,000 genes and 100 patients.
7. [[Bias-Variance Tradeoff]] (L2): decompose prediction error and pick model complexity.
8. [[Cross-Validation]] (L2): estimate generalization error and tune hyperparameters with k-fold and leave-one-out; nest it when selecting models. Bio: choosing a penalty for a biomarker model.
9. [[K-Nearest Neighbors Algorithm]] (L2): classify by majority vote of neighbors; choose $k$. Bio: transferring cell-type labels from a reference atlas.

### Stage 3 - Advanced (L3)

10. [[Confusion Matrix]] (L3): tabulate predictions against truth and derive sensitivity, specificity and accuracy for a classifier. Bio: evaluating a variant caller or a diagnostic classifier.
11. [[Receiver Operating Characteristic Curve]] (L3): trace ROC curves and compute the AUC. Bio: comparing pathogenicity predictors.
12. [[Precision and Recall]] (L3): use precision-recall curves and F1 under class imbalance. Bio: rare positives such as binding sites or pathogenic variants.
13. [[Linear Discriminant Analysis]] (L3): classify with Gaussian class models and shared covariance. Bio: a classic baseline for expression-based subtype prediction.
14. [[Naive Bayes Classifier]] (L3): classify with conditionally independent features. Bio: taxonomic classification of 16S sequences from k-mer counts.
15. [[Curse of Dimensionality]] (L3): explain why distances and densities degrade in high dimensions. Bio: why nearest neighbors on raw gene space work poorly.
16. [[Regularization]] (L3): add a penalty to control complexity (shrinkage). Bio: stable models with more genes than samples.
17. [[Ridge Regression]] (L3): shrink coefficients with an $L_2$ penalty. Bio: genomic prediction and polygenic scores from many small effects.
18. [[Lasso]] (L3): select variables with an $L_1$ penalty; elastic net. Bio: sparse biomarker panels.
19. [[Feature Selection]] (L3): compare filter, wrapper and embedded methods, inside cross-validation. Bio: gene selection without selection bias.
20. [[Spline]] (L3): fit smooth curves with basis functions and a smoothing penalty. Bio: expression trends over time.
21. [[Generalized Additive Model]] (L3): combine smooth functions of several predictors. Bio: gene expression along a pseudotime trajectory.
22. [[Decision Tree]] (L3): grow and prune classification and regression trees. Bio: interpretable clinical decision rules.
23. [[Bootstrap Aggregating]] (L3): reduce variance by averaging models fit on bootstrap samples (bagging).
24. [[Random Forest]] (L3): decorrelate bagged trees; read out-of-bag error and variable importance. Bio: prioritizing genes or variants; microbiome-based classifiers.
25. [[Boosting]] (L3): build additive ensembles of weak learners (gradient boosting). Bio: strong baselines on tabular omics data.
26. [[Support Vector Machine]] (L3): find maximum-margin classifiers; soft margins. Bio: cancer classification from microarrays; protein function prediction.
27. [[Kernel Method]] (L3): replace dot products by kernels to get nonlinear models. Bio: string and spectrum kernels on k-mers for sequence classification.
28. [[Neural Network]] (L3): build multilayer perceptrons with nonlinear activations. Bio: nonlinear predictors of expression or variant effect.
29. [[Backpropagation]] (L3): compute gradients layer by layer with the chain rule. Bio: how every deep model in genomics is trained.
30. [[Data Leakage]] (L3): detect information from the test set leaking into training (preprocessing, duplicates, homologs, related samples). Bio: the most common reason genomic predictors fail to replicate.

### Stage 4 - Frontier (M1)

31. [[Convolutional Neural Network]] (M1): learn local patterns with convolutional filters. Bio: first-layer filters of sequence models behave like position weight matrices (transcription-factor binding, chromatin accessibility).
32. [[Transformer (Deep Learning)]] (M1): model long-range dependencies with attention. Bio: protein and DNA language models; attention in structure prediction.
33. [[Autoencoder]] (M1): learn compressed latent representations, including variational autoencoders. Bio: latent spaces of single-cell data.
34. [[Bayesian Network]] (M1): encode conditional independence in a directed acyclic graph and learn its structure from data. Bio: inferring gene regulatory networks from expression data.

> [!tip] Order of study
> Follow ISL chapter by chapter with its Python labs (Stanford's Statistical Learning with Python course uses the same book), then take MIT 6.036 for the optimization and neural-network view. Learn items 5, 8 and 30 on a real genomic dataset before any model: most published errors in biological machine learning are validation errors.

## Uses from other domains

- [[Variant Annotation]] ([[Genomics]]): pathogenicity predictors.
- [[Transcriptomics]]: classifiers of samples and cells; GAMs along trajectories.
- [[Metagenomics]] ([[Genomics]]): taxonomic classifiers.
- [[Sequence Motif]] ([[Sequence Analysis]]): motifs learned by convolutional filters.
- [[Protein Language Model]] ([[Structural Bioinformatics]]): transformers trained on protein sequences.
- [[Gene Regulatory Network Inference]] ([[Systems Biology]]): random forests and Bayesian networks.
- [[Polygenic Risk Score]] ([[Population Genomics]]): penalized regression on many small effects.
- [[Clinical Genomics]] and [[Drug Discovery]]: predictive models under regulatory scrutiny.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[Stanford - Statistical Learning with Python]] | Stanford Online | L3 | Regression, classification, resampling, regularization, splines and GAMs, trees and boosting, SVMs, neural networks (items 1-29)[^slp] |
| [[MIT 6.036 - Introduction to Machine Learning]] | MIT | L3 | Formulation of learning problems, overfitting and generalization, supervised learning, neural networks (items 1-8, 28-31)[^6036] |
| [[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]] | MIT | L3 | Stochastic gradient descent and neural networks from the linear-algebra side (items 28-29)[^18065] |
| [[MIT 6.047 - Computational Biology]] | MIT | L3-M1 | Classification of gene expression data[^6047] |

## Reference books

- [[An Introduction to Statistical Learning (James)]]: chapter 2 (statistical learning), 4 (classification), 5 (resampling), 6 (model selection and regularization), 7 (moving beyond linearity), 8 (tree-based methods), 9 (support vector machines), 10 (deep learning).[^isl]
- [[Modern Statistics for Modern Biology (Holmes)]]: supervised learning on biological data.[^msmb]

## Lab projects

- [[05-sequence-search]]: sensitivity versus specificity of search heuristics, measured with a confusion matrix and ROC curves.

## References

[^slp]: [[Stanford - Statistical Learning with Python]]: coverage table of the source note.
[^6036]: [[MIT 6.036 - Introduction to Machine Learning]]: foundations (representation, over-fitting, generalization), supervised learning, neural networks.
[^18065]: [[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]], lecture 25 and the deep-learning part.
[^6047]: [[MIT 6.047 - Computational Biology]], networks part (clustering and classification).
[^isl]: [[An Introduction to Statistical Learning (James)]], Python edition; chapter topics checked against the official ISLP lab notebooks (Ch02 to Ch10).
[^msmb]: [[Modern Statistics for Modern Biology (Holmes)]], learning and design part.

Scope check: the target is L3 with an M1 extension (curriculum Stage 4), following the scope of ISL rather than a full machine-learning degree; reinforcement learning is left out.[^6036]
