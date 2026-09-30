---
aliases:
  - Network Biology
  - Computational Systems Biology
tags:
  - type/moc
  - domain/bioinformatics
  - domain/biology
  - domain/mathematics
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Transcriptomics]]"
  - "[[Biochemistry]]"
  - "[[Molecular Biology]]"
  - "[[Discrete Mathematics]]"
  - "[[Differential Equations]]"
  - "[[Optimization]]"
  - "[[Mathematical Modeling]]"
projects: []
sources:
  - "[[MIT 8.591J - Systems Biology]]"
  - "[[MIT 7.91J - Foundations of Computational and Systems Biology]]"
  - "[[MIT 6.047 - Computational Biology]]"
  - "[[Galaxy Training Network - Training Material]]"
  - "[[Nonlinear Dynamics and Chaos (Strogatz)]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[Shanghai Jiao Tong University - BS Bioinformatics]]"
  - "[[KEGG]]"
  - "[[Gene Ontology]]"
---

# Systems Biology

> [!abstract]
> Studying biological systems as networks and dynamical models: interaction and regulatory networks, pathway and enrichment analysis, kinetic and logical models of regulation, and constraint-based metabolic modeling (flux balance analysis).

## Why it matters for bioinformatics

Omics analyses end with lists of genes, proteins or metabolites; systems biology turns those lists into mechanisms. Enrichment analysis is a routine interpretation step in genomics papers, network analysis organizes interactome data, and genome-scale metabolic models are used in metabolic engineering and microbiome research. Systems biology and biological modeling are core courses of computational biology and bioinformatics majors.[^cmu][^sjtu]

## Before you start

- [[Molecular Biology]]: [[Gene Regulation]], [[Transcription Factor]], [[Promoter]], [[Operon]]; [[Cell Biology]]: [[Cell Signaling]].
- [[Biochemistry]]: [[Enzyme]], [[Michaelis-Menten Kinetics]], [[Metabolism]]; [[Physical Chemistry]]: [[Reaction Kinetics]], [[Chemical Equilibrium]].
- [[Discrete Mathematics]]: [[Graph]], [[Directed Graph]], [[Bipartite Graph]], [[Adjacency Matrix]], [[Random Graph]]; [[Algorithms]]: [[Graph Traversal]], [[Shortest Path]].
- [[Differential Equations]]: [[Ordinary Differential Equation]], [[Fixed Point]], [[Phase Portrait]], [[Linear Stability Analysis]], [[Bifurcation]].
- [[Mathematical Modeling]]: [[Hill Function]], [[Quasi-Steady-State Approximation]], [[Compartmental Model]].
- [[Optimization]]: [[Linear Programming]]; [[Linear Algebra]]: [[Matrix]], [[Eigenvalues and Eigenvectors]].
- [[Probability]]: [[Hypergeometric Distribution]], [[Mutual Information]]; [[Statistical Inference]]: [[False Discovery Rate]].
- [[Transcriptomics]]: [[Differential Expression Analysis]]; [[Bioinformatics Foundations]]: [[Gene Ontology Annotation]].

## Learning path

### Stage 2 - Core (L2)

1. [[Biological Network]] (L2): represent molecules as nodes and interactions as directed, undirected or weighted edges.
2. [[Degree Distribution]] (L2): compute node degrees and their distribution and compare them with random graphs.
3. [[Network Centrality]] (L2): rank nodes by degree, betweenness and closeness and interpret hubs and bottlenecks.
4. [[Biological Pathway]] (L2): read a curated pathway ([[KEGG]], Reactome) as a set of reactions and interactions.

### Stage 3 - Advanced (L3)

5. [[Over-Representation Analysis]] (L3): test a gene list for enriched [[Gene Ontology]] terms or pathways with the hypergeometric test and the right background.
6. [[Gene Set Enrichment Analysis]] (L3): test ranked gene lists without a threshold and read enrichment scores.
7. [[Protein-Protein Interaction Network]] (L3): build an interactome from yeast two-hybrid, AP-MS and databases (STRING) and know its biases.
8. [[Scale-Free Network]] (L3): recognize power-law degree distributions and weigh the evidence for them in biology.
9. [[Network Module]] (L3): identify functional modules in interaction networks by community detection (modularity, Louvain, Leiden) and test their biological coherence.
10. [[Gene Regulatory Network]] (L3): model transcription factors and their targets as a directed network.
11. [[Network Motif]] (L3): find over-represented subgraphs (feed-forward loop, autoregulation) and their functions.
12. [[Gene Co-Expression Network]] (L3): build correlation networks from expression data and extract modules (WGCNA-style).
13. [[Boolean Network]] (L3): model regulation with logical rules and find attractors.
14. [[Biochemical Kinetic Model]] (L3): write mass-action and Michaelis-Menten ODEs for a small reaction network and simulate them.
15. [[Feedback Loop]] (L3): compare negative autoregulation and positive feedback in response time, noise and memory.
16. [[Bistability]] (L3): find the two stable states of a positive-feedback switch by phase-plane and steady-state analysis.
17. [[Metabolic Network]] (L3): represent metabolism as a bipartite graph of metabolites and reactions.
18. [[Stoichiometric Matrix]] (L3): encode a reaction network as $S$ and write the steady-state constraint $S v = 0$.
19. [[Flux Balance Analysis]] (L3): predict fluxes by linear programming with an objective (biomass) and flux bounds.
20. [[Systems Biology Markup Language]] (L3): exchange models in SBML and run them in standard tools.

### Stage 4 - Frontier (M1)

21. [[Genome-Scale Metabolic Model]] (M1): reconstruct and curate a whole-organism metabolic model and simulate knockouts (COBRA).
22. [[Flux Variability Analysis]] (M1): compute the range of each flux compatible with optimal growth.
23. [[Gene Regulatory Network Inference]] (M1): infer regulatory edges from expression data (mutual information, regression, tree ensembles) and benchmark them.
24. [[Stochastic Gene Expression]] (M1): model noise in expression with stochastic simulation and relate it to cell-to-cell variability.
25. [[Multi-Omics Integration]] (M1): combine genomic, transcriptomic, proteomic and metabolic data in joint models.

> [!tip]
> Items 14 to 16 are best learned by coding: integrate each model numerically in Python and vary one parameter at a time. Items 17 to 19 need only a linear programming solver and a toy network of five reactions.

## Uses from other domains

- [[Gillespie Algorithm]] (from [[Stochastic Processes]]): stochastic simulation for item 24.
- [[Sensitivity Analysis]] and [[Model Calibration]] (from [[Mathematical Modeling]]): fitting and probing items 14 to 16.
- [[Random Forest]] (from [[Statistical Learning]]) and [[Bayesian Network]] (from [[Bayesian Statistics]]): network inference in item 23.
- [[Graph-Based Clustering]] (from [[Multivariate Analysis]]): the clustering machinery behind item 9.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 8.591J - Systems Biology]] | MIT | L3 | "Input Function, Michaelis-Menten Kinetics, and Cooperativity"; "Autoregulation, Feedback and Bistability"; "Causes and Consequences of Stochastic Gene Expression" (items 10 to 16, 24)[^mit8591] |
| [[MIT 7.91J - Foundations of Computational and Systems Biology]] | MIT | L3-M1 | Network modeling of complex biological systems[^mit791] |
| [[MIT 6.047 - Computational Biology]] | MIT | L3-M1 | "Networks" part: regulatory genomics, Bayesian networks[^mit6047] |
| [[Galaxy Training Network - Training Material]] | Galaxy Project | L3 | "Transcriptomics" tutorials "GO Enrichment Analysis", "3: RNA-seq genes to pathways", "Network analysis with Heinz" (items 5 to 7)[^gtn] |
| 02-512 Computational Methods for Biological Modeling and Simulation, in [[Carnegie Mellon University - BS Computational Biology]] | CMU | L3 | Required modeling course[^cmu] |

## Reference books

- [[Nonlinear Dynamics and Chaos (Strogatz)]]: one-dimensional flows and bifurcations, phase plane analysis and limit cycles, with biological examples, behind items 14 to 16.[^strogatz]

## Lab projects

No Lab project validates this syllabus yet. An enrichment and network analysis module (items 1 to 9) or a small FBA solver (items 17 to 19) would extend the Lab; neither is planned in [[Bioinformatics Lab]].

## References

Gene-network dynamics (input functions, feedback, bistability, noise) follow the lecture sequence of MIT 8.591J;[^mit8591] enrichment and network analysis follow the Galaxy training material;[^gtn] pathway and ontology resources are those of the curated databases;[^kegg][^go] the placement of systems biology at the end of the curriculum follows the programs that teach it after the genomics core.[^cmu][^sjtu]

[^mit8591]: [[MIT 8.591J - Systems Biology]], lectures "Input Function, Michaelis-Menten Kinetics, and Cooperativity", "Autoregulation, Feedback and Bistability" and "Causes and Consequences of Stochastic Gene Expression".
[^mit791]: [[MIT 7.91J - Foundations of Computational and Systems Biology]], systems part.
[^mit6047]: [[MIT 6.047 - Computational Biology]], "Networks" part.
[^gtn]: [[Galaxy Training Network - Training Material]], topic "Transcriptomics" (tutorial titles as listed in the table).
[^strogatz]: [[Nonlinear Dynamics and Chaos (Strogatz)]], parts on one-dimensional flows and two-dimensional flows.
[^kegg]: [[KEGG]]: pathway maps as interaction and reaction networks.
[^go]: [[Gene Ontology]]: ontology, annotations and evidence codes.
[^cmu]: [[Carnegie Mellon University - BS Computational Biology]]: 02-512 Computational Methods for Biological Modeling and Simulation is in the computational biology core, next to 02-510 Computational Genomics.
[^sjtu]: [[Shanghai Jiao Tong University - BS Bioinformatics]]: Systems Biology is in the bioinformatics core.
