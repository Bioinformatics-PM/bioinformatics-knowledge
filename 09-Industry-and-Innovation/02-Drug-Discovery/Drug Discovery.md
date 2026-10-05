---
aliases:
  - Drug Discovery and Development
  - Computational Drug Discovery
  - Découverte de médicaments
tags:
  - type/moc
  - domain/industry
  - domain/chemistry
  - domain/bioinformatics
  - level/L3
  - level/M1
prerequisites:
  - "[[Biochemistry]]"
  - "[[Organic Chemistry]]"
  - "[[Structural Bioinformatics]]"
  - "[[Statistical Learning]]"
  - "[[Experimental Design]]"
  - "[[Industry Landscape]]"
projects: []
sources:
  - "[[MIT 7.016 - Introductory Biology]]"
  - "[[MIT 15.136J - Principles and Practice of Drug Development]]"
  - "[[Basic Principles of Drug Discovery and Development (Blass)]]"
  - "[[Hughes 2011 - Principles of Early Drug Discovery]]"
  - "[[Nelson 2015 - The Support of Human Genetic Evidence for Approved Drug Indications]]"
  - "[[Lipinski 1997 - Experimental and Computational Approaches to Estimate Solubility and Permeability]]"
  - "[[KEGG]]"
---

# Drug Discovery

> [!abstract]
> How a medicine is found and brought to patients, from the choice of a biological target through screening, hit-to-lead and lead optimization, preclinical studies, clinical phases I to III and approval to post-marketing surveillance, and where computation contributes at each step.

## Why it matters for bioinformatics

Computation enters the pipeline early and everywhere: human genetics and omics to choose targets, structure prediction and virtual screening to find hits, QSAR and machine learning to optimize molecules, and biomarkers and statistics in clinical trials. Targets with human genetic support are markedly more likely to succeed in development, which makes genomics a direct input of drug discovery.[^nelson][^hughes] The process is long and costly, so the value of computation is judged by whether it reduces late failures.[^hughes]

## Before you start

- [[Biochemistry]]: [[Protein]], [[Protein Structure]], [[Enzyme]], [[Michaelis-Menten Kinetics]].
- [[Organic Chemistry]]: functional groups and molecular structure.
- [[Structural Bioinformatics]]: [[Protein Structure Prediction]] and binding sites.
- [[Statistical Learning]]: [[Cross-Validation]], [[Overfitting]], [[Random Forest]], [[Neural Network]].
- [[Experimental Design]]: [[Randomized Controlled Trial]], [[Blinding]], [[Statistical Power]].

## Learning path

### Stage 3 - Advanced (L3)

1. [[Drug Development]] (L3): name the stages of the pipeline from target to market, their typical duration and attrition, and the cost debate.[^hughes]
2. [[Therapeutic Modality]] (L3): compare small molecules, antibodies and other biologics, oligonucleotides, and cell and gene therapies.
3. [[Drug Target]] (L3): explain what makes a protein druggable and the main target classes (GPCRs, kinases, ion channels, nuclear receptors).
4. [[Target Identification]] (L3): use human genetics, expression data and pathways to propose targets, and the evidence that genetic support raises success.[^nelson]
5. [[Target Validation]] (L3): test a target's causal role with knockouts, CRISPR screens and genetic evidence before investing in chemistry.
6. [[High-Throughput Screening]] (L3): describe assays, compound libraries, hit rates and assay quality metrics (Z'-factor) in screening campaigns.[^hughes]
7. [[Molecular Representation]] (L3): encode molecules as SMILES strings, InChI identifiers and molecular graphs.
8. [[Molecular Fingerprint]] (L3): compute structural fingerprints and Tanimoto similarity to search chemical space.
9. [[Molecular Docking]] (L3): predict the pose and score of a ligand in a protein binding site, and know why scoring functions rank poorly.
10. [[Virtual Screening]] (L3): rank large libraries by ligand-based similarity or structure-based docking on experimental or predicted structures, and measure enrichment.
11. [[Hit to Lead]] (L3): triage hits (assay artifacts, promiscuous compounds) and expand series with structure-activity relationships.[^hughes]
12. [[Quantitative Structure-Activity Relationship]] (L3): build and validate models predicting activity from descriptors, with applicability domain.
13. [[Lead Optimization]] (L3): balance potency, selectivity, safety, pharmacokinetics and drug-likeness (Lipinski's rule of five) in multiparameter optimization.[^lipinski]
14. [[ADMET]] (L3): explain absorption, distribution, metabolism, excretion and toxicity, and the in silico models that predict them.
15. [[Preclinical Development]] (L3): list the safety, toxicology and pharmacology studies required before first-in-human trials.[^mit15136]
16. [[Biomarker]] (L3): classify biomarkers (diagnostic, prognostic, predictive, pharmacodynamic) and their use in patient selection.
17. [[Clinical Trial]] (L3): describe phases I to IV, their questions, sizes and endpoints, and master protocols (basket, umbrella, platform trials).[^mit15136]
18. [[Drug Approval]] (L3): follow a marketing application at the FDA (NDA, BLA) and the EMA (centralized procedure), including expedited and orphan pathways.
19. [[Pharmacovigilance]] (L3): explain post-marketing safety surveillance and signal detection in adverse event databases.
20. [[Drug Repurposing]] (L3): find new indications for existing drugs with expression signatures, networks and real-world data.

### Stage 4 - Frontier (M1)

21. [[Neoantigen Prediction]] (M1): predict tumor neoantigens from somatic variants and HLA binding for personalized cancer vaccines and cell therapies.
22. [[AI-Driven Drug Design]] (M1): assess generative models, property predictors and structure prediction in discovery, and the clinical evidence so far.

> [!tip]
> Computational drug discovery is one of the Stage 4 specializations in [[Curriculum]]. If you take it, add [[Organic Chemistry]] depth and cheminformatics practice with RDKit after items 7 to 12.

## Uses from other domains

- [[Genome-Wide Association Study]] and [[Population Structure]] ([[Population Genomics]]): genetic evidence for targets.
- [[CRISPR-Cas9]] ([[Biotechnology]]): target validation screens.
- [[Protein Structure Prediction]] and [[Protein Language Model]] ([[Structural Bioinformatics]]): target structures and learned protein representations.
- [[Somatic Variant Calling]] ([[NGS Data Analysis]]) and [[Major Histocompatibility Complex]] ([[Physiology]]): inputs of neoantigen prediction.
- [[Graph]] ([[Discrete Mathematics]]): molecules as graphs.
- [[Compartmental Model]] ([[Mathematical Modeling]]): pharmacokinetic models.
- [[Randomized Controlled Trial]] ([[Experimental Design]]): the design of phase II and III trials.
- [[Regulatory Agency]], [[GxP]] ([[Regulation and Standards]]) and [[Companion Diagnostic]]: the regulatory side of development.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 15.136J - Principles and Practice of Drug Development]] | MIT | M1 | Discovery and preclinical development, clinical investigation, manufacturing and regulation, economics of drug development[^mit15136] |
| [[MIT 7.016 - Introductory Biology]] | MIT | L1 | Applications: therapeutics and tools for advancing research (a first look)[^mit7016] |

## Reference books

- [[Basic Principles of Drug Discovery and Development (Blass)]]: the whole pipeline, from targets and screening to clinical trials and regulation.[^blass]
- [[KEGG]] (database): disease and drug databases linked to pathways (items 3, 20).[^kegg]

## Lab projects

No Lab project covers drug discovery yet. [[Bioinformatics Lab]] rules keep AI and new specializations after the ten core projects.

## References

[^hughes]: [[Hughes 2011 - Principles of Early Drug Discovery]], *British Journal of Pharmacology*.
[^nelson]: [[Nelson 2015 - The Support of Human Genetic Evidence for Approved Drug Indications]], *Nature Genetics*.
[^lipinski]: [[Lipinski 1997 - Experimental and Computational Approaches to Estimate Solubility and Permeability]], *Advanced Drug Delivery Reviews*.
[^mit15136]: [[MIT 15.136J - Principles and Practice of Drug Development]].
[^mit7016]: [[MIT 7.016 - Introductory Biology]], applications.
[^blass]: [[Basic Principles of Drug Discovery and Development (Blass)]].
[^kegg]: [[KEGG]], diseases and drugs.
