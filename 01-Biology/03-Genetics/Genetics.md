---
aliases:
  - Génétique
tags:
  - type/moc
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Cell Biology]]"
  - "[[Molecular Biology]]"
  - "[[Probability]]"
projects:
  - "[[03-genome-diff]]"
  - "[[06-mutation-lab]]"
  - "[[09-genome-browser]]"
  - "[[bio-core]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[MIT 7.01SC - Fundamentals of Biology]]"
  - "[[MIT 7.03 - Genetics]]"
  - "[[MIT - Course 7 Biology]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[ETH Zurich - BSc Biology]]"
  - "[[Université Paris Cité - Licence Sciences de la Vie]]"
  - "[[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]]"
---

# Genetics

> [!abstract]
> Heredity and variation: how genes are transmitted, how they change by mutation and recombination, and how genotype maps to phenotype, from Mendel's crosses to the variant classes that sequencing now reports.

## Why it matters for bioinformatics

- A variant call is a genetics statement: a [[Genotype]] at a locus, on a [[Chromosome]] of a given [[Ploidy]]. The [[VCF Format]], [[Variant Calling]] and [[Variant Annotation]] encode the categories of this syllabus ([[Single Nucleotide Polymorphism]], [[Indel]], [[Structural Variant]], [[Missense Mutation]] and the rest).
- Linkage, recombination and [[Haplotype|haplotypes]] are the ground of [[Linkage Disequilibrium]], imputation and the [[Genome-Wide Association Study]] in [[Population Genomics]].
- Human genetics ([[Pedigree Analysis]], [[Genetic Disease]], [[Somatic Mutation]]) is the biological side of [[Clinical Genomics]].

## Before you start

- [[Cell Biology]]: [[Mitosis]] and [[Meiosis]].
- [[Molecular Biology]] Stage 1: [[DNA]], [[Genetic Code]], [[Codon]], [[Reading Frame]]; needed before the mutation classes (items 12 to 18).
- [[Probability]]: [[Conditional Probability]] and [[Binomial Distribution]] for cross ratios and pedigree risks.

## Learning path

Order: transmission genetics first, then mutation at the molecular level, then linkage, human genetics and genome-scale variation, then quantitative genetics. This follows the introductory courses (meiosis and inheritance in year 1)[^mit701][^openstax] and the core genetics course taken after them,[^mit703] with the transmission, molecular and evolutionary parts of the reference text.[^griffiths] Quantitative genetics closes the path, as in quantitative genetic analysis courses of computational biology programs.[^cmu][^hartl]

### Stage 1 - Foundations (L1)

1. [[Gene]] (L1): define a gene both as a unit of heredity and as a DNA segment encoding a functional product, and see why both definitions coexist.
2. [[Chromosome]] (L1): describe chromosome structure (centromere, telomeres, arms), homologous pairs and sex chromosomes.
3. [[Genome]] (L1): define a genome, and compare genome sizes and gene numbers across organisms.
4. [[Ploidy]] (L1): distinguish haploid, diploid and polyploid cells, and why ploidy fixes how many alleles a genotype has.
5. [[Allele]] (L1): define alleles as alternative forms of a gene or site at one locus.
6. [[Genotype]] (L1): write genotypes as allele pairs (homozygous, heterozygous) and as allele counts 0, 1, 2.
7. [[Phenotype]] (L1): relate phenotype to genotype and environment.
8. [[Mendelian Inheritance]] (L1): apply segregation and independent assortment to predict cross ratios, and test observed ratios with a chi-square test.
9. [[Dominance]] (L1): distinguish complete dominance, incomplete dominance and codominance at the level of alleles and gene products.
10. [[Sex-Linked Inheritance]] (L1): predict X-linked inheritance patterns and explain male hemizygosity.
11. [[Model Organism]] (L1): explain why E. coli, yeast, nematode, fruit fly, zebrafish, mouse and Arabidopsis are studied, and that each has its own database.
12. [[Mutation]] (L1): define a mutation as a heritable change in DNA sequence and classify mutations by size, cause and effect.
13. [[Point Mutation]] (L1): classify single-base substitutions as transitions or transversions.
14. [[Silent Mutation]] (L1): explain why a synonymous codon change leaves the protein sequence unchanged.
15. [[Missense Mutation]] (L1): predict the amino acid change caused by a substitution and reason about its severity.
16. [[Nonsense Mutation]] (L1): recognize a substitution that creates a premature stop codon.
17. [[Indel]] (L1): define insertions and deletions and relate their length to their effect on the reading frame.
18. [[Frameshift Mutation]] (L1): explain why an indel whose length is not a multiple of three changes every downstream codon.

### Stage 2 - Core (L2)

19. [[Genetic Recombination]] (L2): explain crossing over and recombination frequency, and why recombination reshuffles alleles every generation.
20. [[Genetic Linkage]] (L2): build a genetic map in centimorgans from recombination frequencies, and explain why linked genes break independent assortment.
21. [[Pedigree Analysis]] (L2): infer the mode of inheritance from a family tree and compute carrier and recurrence risks.
22. [[Genetic Disease]] (L2): distinguish monogenic from complex disease, and explain penetrance and expressivity.
23. [[Epistasis]] (L2): recognize gene interaction from modified Mendelian ratios.
24. [[Genetic Screen]] (L2): contrast forward and reverse genetics, and explain how mutant screens and complementation tests assign functions to genes.
25. [[Single Nucleotide Polymorphism]] (L2): define SNPs as common single-base variants and use them as genetic markers.
26. [[Haplotype]] (L2): define a haplotype as the alleles carried together on one chromosome, and why genotypes alone do not reveal it.
27. [[Mutation Rate]] (L2): express mutation rates per base per generation, and estimate de novo mutations from parent-offspring trios.
28. [[Somatic Mutation]] (L2): distinguish germline from somatic mutations, and explain mosaicism and the mutational landscape of tumors.
29. [[Structural Variant]] (L2): classify large rearrangements (deletions, duplications, inversions, translocations) and why short reads miss many of them.
30. [[Transposable Element]] (L2): describe DNA transposons and retrotransposons, and why they make eukaryotic genomes repetitive.
31. [[Mitochondrial DNA]] (L2): explain maternal inheritance, heteroplasmy and the use of mtDNA in ancestry studies.

### Stage 3 - Advanced (L3)

32. [[Copy Number Variation]] (L3): explain dosage changes from deletions and duplications, and how read depth and arrays detect them.
33. [[Quantitative Trait]] (L3): explain continuous traits as the sum of many small genetic effects plus environment.
34. [[Heritability]] (L3): define broad-sense and narrow-sense heritability and estimate them from family and twin data.
35. [[Quantitative Trait Locus]] (L3): explain QTL mapping in crosses and families, the ancestor of the [[Expression Quantitative Trait Locus]] and of GWAS.

> [!tip] How to study it
> Genetics is learned by solving problems: do the problem sets of [[MIT 7.03 - Genetics]] on paper before reading solutions. Read items 12 to 18 right after [[Genetic Code]], then build [[06-mutation-lab]]. With [[Genome]] and [[Transposable Element]], read the key findings of [[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]].

## Uses from other domains

- [[Molecular Biology]]: [[DNA Replication]] and [[DNA Repair]] (origin of mutations), [[Reverse Transcription]] (retrotransposons), [[Nonsense-Mediated Decay]] (consequence of nonsense mutations).
- [[Cell Biology]]: [[Cancer]] (somatic mutations), [[Mitochondrion]] (mitochondrial DNA).
- [[Evolution]]: [[Allele Frequency]] and [[Hardy-Weinberg Equilibrium]] (with [[Single Nucleotide Polymorphism]] and [[Genetic Disease]]).
- [[Biotechnology]]: [[Microarray]] (genotyping, copy number), [[CRISPR-Cas9]] (reverse genetics).
- [[Statistical Inference]]: [[Hypothesis Testing]] (chi-square test of ratios), [[Maximum Likelihood Estimation]] (LOD scores).
- [[Linear Models]]: [[Linear Regression]] (heritability, QTL mapping).
- [[Bioinformatics Foundations]]: [[Reference Genome]], [[Genomic Coordinate System]] (with [[Genome]]).
- [[Genomics]]: [[Genetic Variant]], the general term the variant classes above specialize.
- [[NGS Data Analysis]]: [[Somatic Variant Calling]], [[Structural Variant Calling]] (the data side of [[Somatic Mutation]], [[Structural Variant]] and [[Copy Number Variation]]).
- [[Population Genomics]]: [[Haplotype Phasing]], [[Genome-Wide Association Study]], [[Expression Quantitative Trait Locus]] (after Stage 3).
- [[Clinical Genomics]]: [[Trio Analysis]] (with [[Pedigree Analysis]] and [[Mutation Rate]]).

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 7.01SC - Fundamentals of Biology]] | MIT | L1 | Genetics unit: meiosis and inheritance |
| [[MIT 7.03 - Genetics]] | MIT | L2 | Genes, chromosomes and genomes; variation from recombination, mutation and selection; genetic analysis; gene regulation; human genetics and inherited disease |

## Reference books

- [[Biology 2e (OpenStax)]]: Unit 3 "Genetics" (meiosis, Mendel, inheritance) for the L1 pass.
- [[An Introduction to Genetic Analysis (Griffiths)]]: the reference, with problems; transmission genetics (L1), molecular genetics, mutation and genomes (L2), evolutionary and quantitative genetics (L3).
- [[Principles of Population Genetics (Hartl)]]: the quantitative traits and heritability part for Stage 3.

## Lab projects

- [[03-genome-diff]]: [[Mutation]], [[Single Nucleotide Polymorphism]], [[Indel]] (Stage 2).
- [[06-mutation-lab]]: [[Silent Mutation]], [[Missense Mutation]], [[Nonsense Mutation]], [[Frameshift Mutation]] (Stage 2).
- [[09-genome-browser]]: [[Genome]] coordinates and features (Stage 3).
- [[bio-core]]: typed [[Gene]], [[Genome]] and [[Mutation]] objects.

## References

[^mit701]: [[MIT 7.01SC - Fundamentals of Biology]], genetics unit: meiosis and inheritance, in a first-semester course.
[^openstax]: [[Biology 2e (OpenStax)]], Unit 3 "Genetics": meiosis, Mendel, inheritance, then ch. 14 to 16 for the molecular side.
[^mit703]: [[MIT 7.03 - Genetics]], an L2 course taken after the introductory biology course: genes and genomes, variation, population genetics, genetic analysis, gene regulation, human genetics. Genetics is in the required core of [[MIT - Course 7 Biology]] and in year 2 of [[ETH Zurich - BSc Biology]] ("Genetics, genomics"); [[Université Paris Cité - Licence Sciences de la Vie]] offers a genetics parcours in L3.
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]]: transmission genetics, molecular genetics, mutation and genomes, evolutionary genetics (population and quantitative); chapter numbers not verified.
[^cmu]: [[Carnegie Mellon University - BS Computational Biology]]: 03-221 "Genomes, Evolution, and Disease: Introduction to Quantitative Genetic Analysis" in the biological core.
[^hartl]: [[Principles of Population Genetics (Hartl)]], quantitative traits part: heritability.
