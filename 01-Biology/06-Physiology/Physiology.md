---
aliases:
  - Physiologie
  - Human Physiology
tags:
  - type/moc
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Cell Biology]]"
  - "[[Molecular Biology]]"
projects: []
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Anatomy and Physiology 2e (OpenStax)]]"
  - "[[Janeway's Immunobiology (Murphy)]]"
  - "[[University of Cambridge - Natural Sciences Tripos]]"
  - "[[Tsinghua University - BS Biological Sciences]]"
  - "[[Sorbonne Université - Licence Sciences de la Vie]]"
  - "[[Université Paris Cité - Licence Sciences de la Vie]]"
  - "[[Stanford University - BS Biomedical Computation]]"
---

# Physiology

> [!abstract]
> How the human body works as a system of tissues and organs, with immunology as its main thread: the physiology a bioinformatician needs to read biomedical and immunogenomic data.

## Why it matters for bioinformatics

- Biomedical datasets are organized by [[Tissue]], organ and blood cell type (tissue expression atlases, blood transcriptomes, clinical measurements); interpreting them needs the organ-level picture.
- Immunogenomics works on highly polymorphic and somatically rearranged genes: [[Major Histocompatibility Complex]] typing, [[T Cell Receptor]] and [[Antibody]] repertoires built by [[V(D)J Recombination]], and neoantigen prediction in [[Drug Discovery]].
- [[Hematopoiesis]] is a standard test case for the single-cell trajectory methods of [[Transcriptomics]].

## Before you start

- [[Cell Biology]]: [[Cell Signaling]], [[Cell Differentiation]], [[Stem Cell]].
- [[Molecular Biology]]: [[Gene Expression]], [[Gene Regulation]].

## Learning path

Order: control principles and the body plan, then the systems met in biomedical data (blood, nervous, endocrine, immune), then immunology in depth. Organismal physiology is a year-1 subject in some programs and a required course in others,[^cam][^thu] and an L3 track in French licences;[^l3] the introductory text covers it in one unit.[^openstax] Immunology is the deep dive because immunogenomics is where physiology meets sequence data.

### Stage 1 - Foundations (L1)

1. [[Homeostasis]] (L1): explain negative feedback as the control principle of physiology.
2. [[Tissue]] (L1): describe the four animal tissue types (epithelial, connective, muscle, nervous) and how they build organs.
3. [[Organ System]] (L1): map the major human organ systems to their functions.
4. [[Blood]] (L1): list the components and cell types of blood and what a routine blood count measures.
5. [[Nervous System]] (L1): describe the central and peripheral nervous systems and the reflex arc.
6. [[Endocrine System]] (L1): explain hormones as long-range signals, the main glands and their feedback loops.
7. [[Immune System]] (L1): distinguish physical barriers, innate and adaptive defenses, and the organs and cells involved.

### Stage 2 - Core (L2)

8. [[Neuron]] (L2): explain the action potential and synaptic transmission.
9. [[Hematopoiesis]] (L2): follow the blood-cell lineage tree from the hematopoietic stem cell to mature cells.
10. [[Innate Immunity]] (L2): explain pattern recognition, inflammation, phagocytes and complement.
11. [[Adaptive Immunity]] (L2): explain antigen specificity, clonal selection and immunological memory.
12. [[Lymphocyte]] (L2): distinguish B cells, helper and cytotoxic T cells and natural killer cells by role and surface markers.
13. [[Antibody]] (L2): describe antibody structure (heavy and light chains, variable and constant regions) and the isotypes.

### Stage 3 - Advanced (L3)

14. [[V(D)J Recombination]] (L3): explain how somatic recombination of gene segments generates receptor diversity.
15. [[T Cell Receptor]] (L3): describe the T cell receptor and how it recognizes peptides presented by MHC molecules.
16. [[Major Histocompatibility Complex]] (L3): explain class I and class II antigen presentation, and why HLA polymorphism matters for transplantation, disease association and neoantigen prediction.
17. [[Immune Repertoire]] (L3): define the repertoire of B and T cell receptor clonotypes and what repertoire sequencing measures.

> [!tip] What to skip
> Organ-by-organ anatomy, plant physiology and exercise physiology add little to data work. Go deep on blood and immunity instead, and come back to other organ systems when a dataset needs them.

## Uses from other domains

- [[Biophysics]]: [[Membrane Potential]] and [[Diffusion]] (with [[Neuron]]).
- [[Cell Biology]]: [[Membrane Transport]] (with [[Neuron]]), [[Cell Type]] (with [[Blood]] and [[Hematopoiesis]]).
- [[Genetics]]: [[Genetic Recombination]] (contrast with [[V(D)J Recombination]]), [[Somatic Mutation]].
- [[Evolution]]: [[Balancing Selection]] (with [[Major Histocompatibility Complex]]).
- [[Microbiology]]: [[Pathogen]], [[Microbiome]].
- [[Mathematical Modeling]]: [[Compartmental Model]] (hormone and drug kinetics).

## Reference courses

No dedicated physiology or immunology course note yet; the reference books below cover the syllabus.

## Reference books

- [[Biology 2e (OpenStax)]]: Unit 7 "Animal Structure and Function" for the L1 pass.
- [[Anatomy and Physiology 2e (OpenStax)]]: the human physiology reference for Stages 1 and 2.
- [[Janeway's Immunobiology (Murphy)]]: the immunology reference for Stages 2 and 3.

## Lab projects

No Lab project implements physiology yet. It is the biological ground of the biomedical data science and immunogenomics specializations after Stage 4.

## References

[^cam]: [[University of Cambridge - Natural Sciences Tripos]]: "Physiology of Organisms" is one of the Part IA (year 1) experimental subjects.
[^thu]: [[Tsinghua University - BS Biological Sciences]]: Physiology (3 credits) is a major required course. [[Stanford University - BS Biomedical Computation]] offers an "Organs/Organ Systems" track.
[^l3]: [[Sorbonne Université - Licence Sciences de la Vie]], L3 major MOrga ("from the molecule to the organism"); [[Université Paris Cité - Licence Sciences de la Vie]], L3 parcours "Biochimie, biologie intégrative et physiologie".
[^openstax]: [[Biology 2e (OpenStax)]], Unit 7 "Animal Structure and Function".
