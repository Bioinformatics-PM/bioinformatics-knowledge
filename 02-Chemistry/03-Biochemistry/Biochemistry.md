---
aliases:
  - Biochimie
  - Biological Chemistry
tags:
  - type/moc
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[General Chemistry]]"
  - "[[Organic Chemistry]]"
  - "[[Physical Chemistry]]"
  - "[[Cell Biology]]"
  - "[[Molecular Biology]]"
projects:
  - "[[02-sequence-translation]]"
  - "[[06-mutation-lab]]"
  - "[[bio-core]]"
sources:
  - "[[MIT 5.07SC - Biological Chemistry I]]"
  - "[[MIT 7.01SC - Fundamentals of Biology]]"
  - "[[MIT 8.591J - Systems Biology]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[KEGG]]"
  - "[[RCSB Protein Data Bank]]"
  - "[[MIT - Course 7 Biology]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[Tsinghua University - BS Biological Sciences]]"
  - "[[ETH Zurich - BSc Biology]]"
  - "[[University of Cambridge - Natural Sciences Tripos]]"
  - "[[Université Paris Cité - Licence Sciences de la Vie]]"
  - "[[Sorbonne Université - Licence Sciences de la Vie]]"
---

# Biochemistry

> [!abstract]
> The chemistry of living matter from L1 to L3: amino acids to protein structure and folding, ligand binding and enzyme kinetics, and the metabolic pathways that turn nutrients into ATP, reducing power and building blocks.

## Why it matters for bioinformatics

- **Protein bioinformatics assumes it.** [[Structural Bioinformatics]] and [[Proteomics]] are built on [[Protein Structure]] levels, [[Protein Domain|domains]], [[Protein Folding|folding]] and [[Post-Translational Modification|modifications]]. The PDB archives experimentally determined structures of these macromolecules.[^pdb]
- **Variant interpretation is biochemistry.** A [[Missense Mutation]] matters when it disturbs folding, binding or catalysis; [[Amino Acid]] properties are the first filter.
- **Kinetics are the input functions of models.** [[Michaelis-Menten Kinetics]] and [[Cooperativity]] are the rate laws of gene-circuit and metabolic models in [[Systems Biology]].[^8591]
- **Pathway maps are metabolism.** KEGG maps link each enzyme of a [[Metabolic Pathway]] to the genes that encode it in each genome, which is how an annotated genome becomes a metabolic reconstruction.[^kegg]
- **Most drugs inhibit enzymes or block binding sites**: [[Enzyme Inhibition]] and [[Ligand Binding]] are the vocabulary of [[Drug Discovery]].

## Before you start

- [[General Chemistry]]: [[Hydrogen Bond]], [[Intermolecular Force]], [[Water]], [[Redox Reaction]].
- [[Organic Chemistry]]: [[Functional Group]], [[Chirality]], [[Hydrolysis]]; Stage 2 of Organic Chemistry before the metabolism items.
- [[Physical Chemistry]] Stage 1: [[Gibbs Free Energy]], [[Chemical Equilibrium]], [[Henderson-Hasselbalch Equation]], [[Reaction Kinetics]], [[Catalysis]].
- [[Cell Biology]] and [[Molecular Biology]] Stage 1: [[Cell]], [[Cell Membrane]], [[Organelle]], [[Nucleotide]], [[Central Dogma]], [[Translation]].

## Learning path

### Stage 1 - Foundations (L1)

1. [[Hydrophobic Effect]] (L1): explain why nonpolar groups cluster in water (an entropy effect of the solvent, not an attraction). Bio: the main driving force of folding, membrane assembly and binding.
2. [[Amino Acid]] (L1): recognize the 20 standard amino acids, their one- and three-letter codes, side-chain classes (hydrophobic, polar, acidic, basic, special cases Gly, Pro, Cys) and ionizable groups. Bio: the alphabet of every protein sequence.
3. [[Peptide Bond]] (L1): explain how residues are linked, why the bond is planar and usually trans, and why sequences are written from N to C terminus.
4. [[Protein]] (L1): describe a protein as a folded polypeptide and list its functions (catalysis, structure, transport, signaling, regulation).
5. [[Protein Structure]] (L1): name the four levels (primary to quaternary) and the interactions that stabilize each.
6. [[Carbohydrate]] (L1): recognize monosaccharides, ring forms, glycosidic bonds and polysaccharides (glycogen, starch, cellulose). Bio: ribose and deoxyribose in nucleic acids; glycosylation.
7. [[Lipid]] (L1): recognize fatty acids, triacylglycerols, phospholipids and sterols; explain amphipathic self-assembly. Bio: membranes, energy storage, signaling.
8. [[Enzyme]] (L1): describe enzymes as specific catalysts with an active site; name the EC classes (oxidoreductases, transferases, hydrolases, lyases, isomerases, ligases, translocases). Bio: EC numbers annotate genes in pathway databases.
9. [[ATP]] (L1): explain ATP as the energy currency: phosphoanhydride bonds, free energy of hydrolysis, coupling to unfavorable reactions.
10. [[Metabolism]] (L1): distinguish catabolism and anabolism; follow carbon, energy (ATP) and electrons (NADH, NADPH) through the cell.
11. [[Metabolic Pathway]] (L1): read a pathway as a sequence of enzyme-catalyzed steps with committed and regulated steps. Bio: read a KEGG map.[^kegg]

### Stage 2 - Core (L2)

12. [[Protein Secondary Structure]] (L2): describe α-helices, β-sheets and turns, their hydrogen-bond patterns, backbone φ/ψ angles and residue preferences. Bio: what [[Secondary Structure Assignment]] (DSSP) assigns and [[Secondary Structure Prediction]] predicts.
13. [[Protein Tertiary Structure]] (L2): explain folds and [[Protein Domain|domains]], hydrophobic cores, disulfide bonds and salt bridges; inspect a structure in a viewer.
14. [[Protein Quaternary Structure]] (L2): describe subunit assembly and symmetry. Bio: hemoglobin, oligomeric enzymes, biological assemblies in PDB entries.
15. [[Protein Folding]] (L2): explain Anfinsen's result (sequence determines structure), the folding energy landscape, marginal stability, chaperones and misfolding diseases.
16. [[Membrane Protein]] (L2): distinguish integral and peripheral proteins, transmembrane helices and β-barrels. Bio: topology prediction from a [[Hydropathy Plot]].
17. [[Protein Purification]] (L2): separate proteins by size, charge and affinity (chromatography) and check purity by SDS-PAGE. Bio: the liquid chromatography step of LC-MS/MS proteomics.
18. [[Ligand Binding]] (L2): define the dissociation constant $K_d$ and fractional saturation; derive the hyperbolic binding curve. Bio: myoglobin and O2; drug-target affinity.
19. [[Cooperativity]] (L2): explain sigmoidal binding with the Hill equation, using hemoglobin. Bio: Hill functions in gene-regulation models.[^8591]
20. [[Allosteric Regulation]] (L2): compare the concerted (MWC) and sequential models and regulation by effectors. Bio: feedback inhibition of pathways.
21. [[Enzyme Catalysis]] (L2): explain transition-state stabilization and acid-base, covalent and metal-ion catalysis, with the serine protease catalytic triad as the worked case.
22. [[Cofactor]] (L2): recognize coenzymes (NAD+, FAD, coenzyme A, PLP, thiamine pyrophosphate, biotin) and metal cofactors, and the group each carries. Bio: vitamins as cofactor precursors.
23. [[Michaelis-Menten Kinetics]] (L2): derive $v = V_{max}[S]/(K_M + [S])$ from the steady-state assumption; interpret $K_M$, $k_{cat}$ and $k_{cat}/K_M$; fit the model to rate data.
24. [[Enzyme Inhibition]] (L2): distinguish competitive, uncompetitive and mixed inhibition from kinetic data; relate $K_i$ and IC50. Bio: how most small-molecule drugs act.
25. [[Glycolysis]] (L2): follow glucose to pyruvate (ten steps, ATP and NADH yield, regulated steps) and the fates of pyruvate.
26. [[Citric Acid Cycle]] (L2): follow acetyl-CoA to CO2, NADH and FADH2, starting at pyruvate dehydrogenase; see the cycle as a hub for biosynthesis.
27. [[Oxidative Phosphorylation]] (L2): explain the electron transport chain, the proton-motive force (chemiosmosis) and ATP synthase; estimate the ATP yield of glucose.
28. [[Gluconeogenesis]] (L2): make glucose from pyruvate through the bypass steps; explain reciprocal regulation with glycolysis.
29. [[Pentose Phosphate Pathway]] (L2): explain the production of NADPH and ribose 5-phosphate. Bio: nucleotide synthesis, oxidative stress, G6PD deficiency.
30. [[Fatty Acid Metabolism]] (L2): compare β-oxidation and fatty acid synthesis (location, carriers, regulation).

### Stage 3 - Advanced (L3)

31. [[Post-Translational Modification]] (L3): catalog phosphorylation, glycosylation, acetylation, methylation, ubiquitination and proteolytic processing, with the enzymes that add and remove them. Bio: [[Histone Modification|histone marks]], PTM site prediction, [[Modification Site Localization]] in [[Mass Spectrometry]] data.
32. [[Amino Acid Metabolism]] (L3): explain transamination, the urea cycle, essential and non-essential amino acids, one-carbon metabolism and inborn errors such as phenylketonuria.
33. [[Nucleotide Metabolism]] (L3): explain de novo and salvage synthesis of purines and pyrimidines and ribonucleotide reduction. Bio: targets of antimetabolite drugs (methotrexate, 5-fluorouracil).
34. [[Metabolic Regulation]] (L3): integrate pathways across tissues and states (fed, fasting) through allosteric control, covalent modification, hormones (insulin, glucagon) and flux control. Bio: the constraints behind a [[Genome-Scale Metabolic Model]].

> [!tip] Order of study
> Items 1 to 11 in Stage 2 of the [[Curriculum]], right after [[Physical Chemistry]] Stage 1. Then protein structure (12 to 17), binding and enzymes (18 to 24, with [[Steady-State Approximation]] read just before item 23), and metabolism last (25 to 30). Photosynthesis, glycogen metabolism and steroid biosynthesis are left out; read them in Lehninger if a project needs them.

## Uses from other domains

- [[Missense Mutation]] ([[Genetics]]) and [[Substitution Matrix]] ([[Sequence Analysis]]): which [[Amino Acid|amino acids]] replace each other without breaking a protein.
- [[Structural Bioinformatics]]: [[Ramachandran Plot]], [[Protein Domain]] and [[Secondary Structure Prediction]] build on [[Protein Secondary Structure]], [[Protein Tertiary Structure]] and [[Protein Folding]].
- [[Proteomics]]: [[Protein Purification]] and [[Post-Translational Modification]], measured by [[Mass Spectrometry]] ([[Biotechnology]]).
- [[Systems Biology]]: [[Metabolic Network]] and [[Flux Balance Analysis]] formalize [[Metabolism]]; [[Michaelis-Menten Kinetics]] and [[Cooperativity]] are rate laws of [[Gene Regulatory Network]] models.
- [[Biophysics]] and [[Structural Bioinformatics]]: [[Binding Free Energy]] and [[Molecular Dynamics Simulation]] extend [[Ligand Binding]] and [[Protein Folding]].
- [[Drug Discovery]] ([[Industry and Innovation]]): [[Enzyme Inhibition]], [[Ligand Binding]].

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 7.01SC - Fundamentals of Biology]] | MIT | L1 | Biochemistry unit: structure and function of macromolecules, basics of metabolism (Stage 1)[^701] |
| [[MIT 5.07SC - Biological Chemistry I]] | MIT | L2 | Building blocks and protein structure; catalysis and cofactors; glycolysis, gluconeogenesis, pentose phosphate pathway; fatty acid metabolism; Krebs cycle and oxidative phosphorylation; regulation (Stages 1 and 2)[^507] |
| [[MIT 8.591J - Systems Biology]] | MIT | L3 | Lecture "Input Function, Michaelis-Menten Kinetics, and Cooperativity": kinetics used as model input[^8591] |

## Reference books

- [[Lehninger Principles of Biochemistry (Nelson)]]: part on structure and catalysis (water, amino acids, proteins, enzymes, carbohydrates, lipids) for Stages 1 and 2; part on bioenergetics and metabolism for items 25 to 34.[^lehninger]
- [[Biochemistry (Berg)]]: free 5th edition; protein structure and exploring proteins (item 17), enzymes (catalysis, kinetics, regulation), metabolism.[^berg]
- [[Organic Chemistry (OpenStax)]]: ch. 26 (amino acids, peptides, proteins) and ch. 29 (organic chemistry of metabolic pathways) as the chemistry-side complement.[^mcmurry]

## Lab projects

- [[02-sequence-translation]]: maps codons to [[Amino Acid|amino acids]].
- [[06-mutation-lab]]: propagates a mutation to the [[Protein]]; amino acid properties explain the consequence.
- [[bio-core]]: implements [[Protein]] as a typed object.

## References

Scope and weight: biochemistry is a core requirement in every program checked: MIT (7.05 or 5.07), Carnegie Mellon (03-232), UC San Diego (BIBC 100 Structural Biochemistry or BIBC 102 Metabolic Biochemistry), Tsinghua (Biochemistry 1 and 2, with a laboratory), ETH (a first-year molecules-to-biochemistry course, then 5 ECTS in year 2) and Cambridge (Part IB Biochemistry and Molecular Biology, including protein structure and function).[^mit7][^cmu][^ucsd][^thu][^eth][^cam] French licences reach L3 in biochemistry through their molecular majors (Paris Cité's "Biochimie, biologie intégrative et physiologie" parcours; Sorbonne's "De la molécule à l'organisme").[^paris][^sorbonne] The split into structure, catalysis and metabolism, and the order within metabolism, follow 5.07SC.[^507]

[^507]: [[MIT 5.07SC - Biological Chemistry I]], course modules: building blocks and protein structure; catalysis and cofactors; carbohydrate metabolism (glycolysis, gluconeogenesis, pentose phosphate pathway); fatty acid synthesis and degradation; Krebs cycle and oxidative phosphorylation; regulation.
[^701]: [[MIT 7.01SC - Fundamentals of Biology]], biochemistry topic of the course description.
[^8591]: [[MIT 8.591J - Systems Biology]], lecture "Input Function, Michaelis-Menten Kinetics, and Cooperativity".
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed., parts on structure and catalysis and on bioenergetics and metabolism (chapter numbers not verified).
[^berg]: [[Biochemistry (Berg)]], 5th ed., parts on the molecular design of life, enzymes and metabolism (chapter numbers not verified).
[^mcmurry]: [[Organic Chemistry (OpenStax)]], ch. 26 "Biomolecules: Amino Acids, Peptides, and Proteins" and ch. 29 "The Organic Chemistry of Metabolic Pathways".
[^kegg]: [[KEGG]]: pathway maps as reaction networks whose enzyme boxes link to genes per organism; metabolic reconstruction through EC numbers.
[^pdb]: [[RCSB Protein Data Bank]]: the archive of experimentally determined macromolecular structures.
[^mit7]: [[MIT - Course 7 Biology]]: molecular core, 7.05 General Biochemistry or 5.07.
[^cmu]: [[Carnegie Mellon University - BS Computational Biology]]: 03-232 Biochemistry I in the biological core.
[^ucsd]: [[UC San Diego - BS Bioinformatics]]: BIBC 100 or BIBC 102 in the upper division.
[^thu]: [[Tsinghua University - BS Biological Sciences]]: Biochemistry (1) and (2) and a biochemistry laboratory in the major.
[^eth]: [[ETH Zurich - BSc Biology]]: "Foundations of Biology 1: from molecules to the biochemistry of the cell" (year 1), Biochemistry 5 ECTS (year 2).
[^cam]: [[University of Cambridge - Natural Sciences Tripos]]: Part IB Biochemistry and Molecular Biology.
[^paris]: [[Université Paris Cité - Licence Sciences de la Vie]]: L3 parcours.
[^sorbonne]: [[Sorbonne Université - Licence Sciences de la Vie]]: L3 major MOrga.
