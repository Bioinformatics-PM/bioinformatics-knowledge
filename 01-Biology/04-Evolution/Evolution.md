---
aliases:
  - Évolution
  - Evolutionary Biology
tags:
  - type/moc
  - domain/biology
  - domain/statistics
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Genetics]]"
  - "[[Probability]]"
projects:
  - "[[07-evolution-simulator]]"
  - "[[08-phylogenetic-engine]]"
  - "[[bio-simulation]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Evolution (Futuyma)]]"
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[Molecular Evolution (Yang)]]"
  - "[[MIT 7.03 - Genetics]]"
  - "[[MIT 6.047 - Computational Biology]]"
  - "[[MIT 8.591J - Systems Biology]]"
  - "[[Université Paris-Saclay - Licence Double Diplôme Informatique Sciences de la Vie]]"
  - "[[University of Cambridge - Natural Sciences Tripos]]"
  - "[[Sorbonne Université - Licence Sciences de la Vie]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[Kimura 1968 - Evolutionary Rate at the Molecular Level]]"
---

# Evolution

> [!abstract]
> How populations and sequences change over generations under mutation, selection, drift and migration, from Darwin's argument to the stochastic models and the neutral null hypothesis that sequence analysis relies on.

## Why it matters for bioinformatics

- Comparing sequences only makes sense because of [[Common Descent]]: [[Sequence Homology]], [[Substitution Matrix|substitution matrices]], [[Phylogenetic Tree|phylogenetic trees]] and annotation transfer between [[Ortholog|orthologs]] are all evolutionary inferences.
- Population genetics ([[Allele Frequency]], [[Genetic Drift]], [[Wright-Fisher Model]]) is the model behind [[Population Genomics]]: [[Coalescent Theory]], [[Linkage Disequilibrium]], [[Genome-Wide Association Study|GWAS]].
- Tests for selection and conservation scores used in [[Variant Annotation]] start from the [[Neutral Theory of Molecular Evolution]] as the null model.

## Before you start

- [[Genetics]] Stage 1: [[Allele]], [[Genotype]], [[Mendelian Inheritance]], [[Mutation]].
- [[Probability]]: [[Random Variable]], [[Expected Value]], [[Variance]], [[Binomial Distribution]].

## Learning path

Order: Darwinian concepts and the history of life (L1, taught in year 1 of life-science licences),[^l1] then population genetics and molecular evolution (L2), then the stochastic models and the detection of selection (L3). This is the progression from the introductory text to the evolution and population-genetics references.[^openstax][^futuyma][^hartl][^yang] Population genetics is part of the core genetics course,[^mit703] and the evolution part of computational biology courses covers selection and human ancestry.[^mit6047]

### Stage 1 - Foundations (L1)

1. [[Common Descent]] (L1): explain that all living things share ancestors, and weigh the evidence from fossils, anatomy and molecules.
2. [[Natural Selection]] (L1): state Darwin's argument (variation, heredity, differential reproduction) and distinguish directional, stabilizing and disruptive selection.
3. [[Fitness]] (L1): define fitness as relative reproductive success and express it with a selection coefficient.
4. [[Adaptation]] (L1): explain adaptation as the product of selection, and avoid "for the good of the species" reasoning.
5. [[Convergent Evolution]] (L1): distinguish similarity by descent (homology) from similarity by independent origin (homoplasy).
6. [[Speciation]] (L1): apply the biological species concept and explain allopatric and sympatric speciation through reproductive isolation.
7. [[Tree of Life]] (L1): read the history of life as a branching tree with three domains, and see where horizontal transfer blurs it.

### Stage 2 - Core (L2)

8. [[Allele Frequency]] (L2): compute allele and genotype frequencies from counts in a sample.
9. [[Hardy-Weinberg Equilibrium]] (L2): derive genotype frequencies under random mating and test a sample for departure from equilibrium.
10. [[Heterozygosity]] (L2): compute observed and expected heterozygosity as a first measure of genetic diversity.
11. [[Genetic Drift]] (L2): explain random changes in allele frequency and why they are stronger in small populations.
12. [[Effective Population Size]] (L2): explain why effective size is usually below census size, and how bottlenecks and founder events reduce it.
13. [[Gene Flow]] (L2): model migration between populations and its homogenizing effect on allele frequencies.
14. [[Inbreeding]] (L2): compute the inbreeding coefficient and explain the excess of homozygotes it causes.
15. [[Molecular Evolution]] (L2): distinguish mutation from substitution, and compare rates at synonymous and nonsynonymous sites.
16. [[Gene Duplication]] (L2): explain how duplicated genes are lost, subfunctionalized or neofunctionalized, and how gene families and [[Paralog|paralogs]] arise.

### Stage 3 - Advanced (L3)

17. [[Wright-Fisher Model]] (L3): model a finite population as binomial resampling of alleles each generation, the engine of [[07-evolution-simulator]].
18. [[Moran Model]] (L3): contrast overlapping generations with the Wright-Fisher model, and know when each is used.
19. [[Fixation Probability]] (L3): compute the probability that a neutral or selected allele reaches fixation, and its expected time to fixation.
20. [[Neutral Theory of Molecular Evolution]] (L3): explain Kimura's claim that most substitutions are neutral, and use it as the null model of molecular evolution.
21. [[Mutation-Selection Balance]] (L3): explain why deleterious alleles persist at low frequency.
22. [[Purifying Selection]] (L3): explain how selection against harmful changes creates sequence conservation, the basis of [[Evolutionary Constraint]] scores.
23. [[Positive Selection]] (L3): recognize the signatures of adaptive change: dN/dS above 1 between species, [[Selective Sweep|selective sweeps]] within them.
24. [[Balancing Selection]] (L3): explain heterozygote advantage and frequency-dependent selection, with the sickle-cell and HLA examples.
25. [[Coevolution]] (L3): explain reciprocal evolution between species and between interacting residues, the signal behind contact prediction from alignments.
26. [[Experimental Evolution]] (L3): describe evolution experiments with microbes and how sequencing their populations tests the models above.
27. [[Human Evolution]] (L3): outline the origin and dispersal of modern humans and archaic admixture, as reconstructed from genomes.

> [!tip] How to study it
> Implement before you read further: after [[Genetic Drift]], simulate drift with a few lines of Python, then formalize it as the [[Wright-Fisher Model]] in [[07-evolution-simulator]]. Read [[Kimura 1968 - Evolutionary Rate at the Molecular Level]] with item 20. Skip behavioral ecology and paleontology details: they rarely meet sequence data.

## Uses from other domains

- [[Genetics]]: [[Mutation Rate]], [[Genetic Recombination]], [[Haplotype]], [[Silent Mutation]] and [[Missense Mutation]] (synonymous and nonsynonymous sites).
- [[Molecular Biology]]: [[Genetic Code]] (synonymous codons).
- [[Microbiology]]: [[Horizontal Gene Transfer]] and [[16S Ribosomal RNA]] (with [[Tree of Life]]).
- [[Physiology]]: [[Major Histocompatibility Complex]] (with [[Balancing Selection]]).
- [[Stochastic Processes]]: [[Markov Chain]], [[Random Walk]] (Stage 3 models).
- [[Scientific Computing]]: [[Random Number Generation]] (simulation).
- [[Sequence Analysis]]: [[Sequence Homology]], [[Ortholog]] and [[Paralog]] (after [[Gene Duplication]] and [[Speciation]]), [[Codon Usage Bias]] (after [[Molecular Evolution]]), [[Multiple Sequence Alignment]] (with [[Coevolution]]).
- [[Phylogenetics]]: [[Phylogenetic Tree]], [[Molecular Clock]].
- [[Population Genomics]]: [[Coalescent Theory]], [[Population Structure]], [[Linkage Disequilibrium]], [[Selective Sweep]] (the sequel of Stage 3).
- [[Genomics]]: [[Evolutionary Constraint]] (with [[Purifying Selection]]).

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 7.03 - Genetics]] | MIT | L2 | Variation from recombination, mutation and selection; allele frequencies in populations |
| [[MIT 6.047 - Computational Biology]] | MIT | L3 | Evolution part: gene and species trees, coalescent, population genomics, human ancestry, recent selection |
| [[MIT 8.591J - Systems Biology]] | MIT | L3 | Evolutionary systems biology: microbial evolution experiments, survival in fluctuating environments |

## Reference books

- [[Biology 2e (OpenStax)]]: Unit 4 "Evolutionary Processes", including "The Evolution of Populations" and "Phylogenies and the History of Life" (L1).
- [[Evolution (Futuyma)]]: history of life, evolutionary processes, species and speciation, molecular evolution and genomics (L2 to L3).
- [[Principles of Population Genetics (Hartl)]]: random mating, evolutionary forces, inbreeding, then molecular population genetics (L2 to M1).
- [[Molecular Evolution (Yang)]]: tests of selection and codon models, after Stage 3 (L3 to M1).

## Lab projects

- [[07-evolution-simulator]]: [[Natural Selection]], [[Genetic Drift]], [[Fitness]], [[Allele Frequency]], [[Hardy-Weinberg Equilibrium]], [[Wright-Fisher Model]] (Stage 3).
- [[bio-simulation]]: the reusable population engine behind it.
- [[08-phylogenetic-engine]]: [[Common Descent]] as the biology that trees reconstruct (Stage 3).

## References

[^l1]: [[Université Paris-Saclay - Licence Double Diplôme Informatique Sciences de la Vie]], L1 unit "Biology 1: unity, diversity and evolution of living things"; [[University of Cambridge - Natural Sciences Tripos]], Part IA option "Evolution and Behaviour" (year 1). [[Sorbonne Université - Licence Sciences de la Vie]] devotes an L3 major (OBEE) to organisms, biodiversity, ecology and evolution.
[^openstax]: [[Biology 2e (OpenStax)]], Unit 4 "Evolutionary Processes", including "The Evolution of Populations" and "Phylogenies and the History of Life".
[^futuyma]: [[Evolution (Futuyma)]]: history of life, evolutionary processes (variation, mutation, drift, selection, gene flow), species and speciation, molecular evolution and genomics; chapter numbers not verified.
[^hartl]: [[Principles of Population Genetics (Hartl)]]: Hardy-Weinberg, drift and selection at L2; population structure, inbreeding, linkage disequilibrium and molecular population genetics at L3 to M1.
[^yang]: [[Molecular Evolution (Yang)]]: models of sequence evolution and phylogenetic tests for selection (L3 to M1).
[^mit703]: [[MIT 7.03 - Genetics]]: variation from recombination, mutation and selection; population genetics. [[Carnegie Mellon University - BS Computational Biology]] likewise joins genomes, evolution and disease in 03-221.
[^mit6047]: [[MIT 6.047 - Computational Biology]], evolution part: gene and species trees, phylogenomics, coalescent, population genomics, human ancestry, recent selection, disease mapping.
