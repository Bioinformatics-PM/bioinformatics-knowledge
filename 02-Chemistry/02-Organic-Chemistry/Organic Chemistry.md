---
aliases:
  - Chimie organique
tags:
  - type/moc
  - domain/chemistry
  - level/L1
  - level/L2
prerequisites:
  - "[[General Chemistry]]"
projects: []
sources:
  - "[[MIT 5.12 - Organic Chemistry I]]"
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[MIT - Course 7 Biology]]"
  - "[[MIT - Course 6-7 Computer Science and Molecular Biology]]"
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[Tsinghua University - BS Biological Sciences]]"
---

# Organic Chemistry

> [!abstract]
> The organic chemistry of biomolecules: reading structures, functional groups and stereochemistry, then the dozen reaction types that metabolism and molecular biology reuse. Synthesis is out of scope.

## Why it matters for bioinformatics

- **Reading a structure is a prerequisite.** Metabolite and drug records in pathway and compound databases, ligands in PDB entries and SMILES strings all assume you can read a [[Skeletal Formula]] and its [[Functional Group|functional groups]].
- **Biology is stereospecific.** Proteins use L-amino acids and nucleic acids D-sugars; enzymes and drugs discriminate [[Chirality|enantiomers]]. Wrong stereochemistry is a classic error in modeled structures.
- **Mutagenesis has a chemistry.** Base [[Tautomer|tautomers]] mispair; alkylating agents act by [[Nucleophilic Substitution]]; DNA methylation is a methyl transfer.
- **Metabolism is organic chemistry.** Glycolysis, the citric acid cycle and fatty acid metabolism are chains of [[Aldol Reaction|aldol]], [[Claisen Condensation|Claisen]], [[Decarboxylation|decarboxylation]], [[Organic Redox Reaction|redox]] and [[Phosphate Ester|phosphoryl-transfer]] steps.[^mcmurry29]

## Before you start

- [[General Chemistry]]: [[Covalent Bond]], [[Electronegativity]], [[Molecular Geometry]], [[Orbital Hybridization]], [[Resonance (Chemistry)]].
- [[Physical Chemistry]] Stage 1: [[Acid-Base Equilibrium]] (pKa tells which groups are charged at pH 7).

## Learning path

### Stage 1 - Foundations (L1)

1. [[Skeletal Formula]] (L1): read and draw line-angle structures with implicit carbons and hydrogens. Bio: read any metabolite or drug structure.
2. [[Functional Group]] (L1): recognize hydroxyl, carbonyl, carboxyl, amino, amide, ester, thioester, thiol, ether and phosphate groups and predict their polarity and acidity. Bio: amino acid side chains, sugar hydroxyls, the phosphate backbone.
3. [[Isomer]] (L1): distinguish constitutional isomers from stereoisomers. Bio: glucose and fructose share the formula C6H12O6.
4. [[Conformational Analysis]] (L1): rotate around single bonds, read Newman projections and chair conformations, compare their energies. Bio: backbone torsion angles of proteins, puckering of sugar rings.
5. [[Stereochemistry]] (L1): describe the three-dimensional arrangement of atoms and why molecular recognition depends on it.
6. [[Chirality]] (L1): find stereocenters, recognize enantiomers and assign R or S with the Cahn-Ingold-Prelog rules. Bio: proteins are built from L-amino acids.
7. [[Fischer Projection]] (L1): read D and L configurations of sugars and amino acids.
8. [[Cis-Trans Isomerism]] (L1): recognize cis/trans (E/Z) isomers around double bonds and rings. Bio: cis double bonds kink unsaturated fatty acids; retinal isomerization in vision; cis-proline peptide bonds.
9. [[Aromaticity]] (L1): apply Hückel's rule and explain aromatic stability and planarity. Bio: nucleobases, Phe, Tyr, Trp and His; base stacking in DNA.
10. [[Reaction Mechanism]] (L1): read curved-arrow mechanisms (which bonds break and form, in which order).
11. [[Nucleophile]] (L1): identify electron-rich species and rank nucleophilicity. Bio: Ser-OH, Cys-SH and His in active sites; water in hydrolysis.
12. [[Electrophile]] (L1): identify electron-poor centers (carbonyl carbon, phosphorus, alkyl carbon bearing a leaving group).
13. [[Hydrolysis]] (L1): explain how water cleaves esters, amides, glycosidic and phosphoanhydride bonds, and condensation as the reverse. Bio: how every biopolymer is made and degraded.

### Stage 2 - Core (L2)

14. [[Diastereomer]] (L2): tell diastereomers from enantiomers; recognize epimers and anomers. Bio: glucose and galactose (C4 epimers); α and β glycosidic bonds (starch versus cellulose).
15. [[Heterocyclic Compound]] (L2): recognize purine, pyrimidine, imidazole, indole and pyridine rings and their basicity. Bio: nucleobases, His, Trp, NAD+, heme.
16. [[Tautomer]] (L2): recognize keto-enol and amino-imino tautomerism. Bio: enediol intermediates of sugar isomerases; rare base tautomers as a mispairing mechanism.
17. [[Nucleophilic Substitution]] (L2): compare SN1 and SN2 (rate law, stereochemistry, leaving groups). Bio: methyl transfer from S-adenosylmethionine ([[DNA Methylation]]); alkylating mutagens.
18. [[Elimination Reaction]] (L2): recognize eliminations that form double bonds and their reverse, the addition of water. Bio: hydration and dehydration steps of enolase, aconitase and fumarase.
19. [[Carbonyl Group]] (L2): explain the polarity of C=O and the acidity of α-hydrogens; classify aldehydes, ketones, acids and acid derivatives.
20. [[Nucleophilic Addition]] (L2): add nucleophiles to aldehydes and ketones; form hemiacetals and imines. Bio: ring closure of sugars; Schiff bases with lysine in PLP enzymes and class I aldolases.
21. [[Nucleophilic Acyl Substitution]] (L2): rank acyl derivatives by reactivity (thioester, ester, amide) and predict products. Bio: peptide bond formation and proteolysis; acetyl-CoA as an activated thioester.
22. [[Aldol Reaction]] (L2): form carbon-carbon bonds between carbonyl compounds through enolates. Bio: aldolase in glycolysis and gluconeogenesis.
23. [[Claisen Condensation]] (L2): form β-keto esters and thioesters. Bio: citrate synthase, thiolase, fatty acid synthesis.
24. [[Decarboxylation]] (L2): explain why β-keto acids lose CO2 easily. Bio: pyruvate and isocitrate dehydrogenases, amino acid decarboxylases.
25. [[Organic Redox Reaction]] (L2): follow oxidation levels from alcohol to aldehyde to carboxylic acid; hydride transfer to NAD+. Bio: every dehydrogenase.
26. [[Phosphate Ester]] (L2): describe phosphomonoesters, phosphodiesters and phosphoanhydrides and phosphoryl transfer. Bio: the DNA backbone, ATP, kinases and phosphatases.

> [!tip] What to skip
> Multistep synthesis and retrosynthesis, named reactions outside this list, alkyne and organohalide chemistry, electrophilic aromatic substitution and the interpretation of IR and NMR spectra. Stage 2 is complete when every reaction of McMurry's chapter on metabolic pathways reads as a familiar mechanism.[^mcmurry29]

## Uses from other domains

- [[Amino Acid]], [[Carbohydrate]], [[Lipid]], [[Enzyme Catalysis]] and the pathways of [[Metabolism]] ([[Biochemistry]]).
- [[Nucleotide]], [[DNA]] and [[DNA Repair]] ([[Molecular Biology]]): phosphodiester backbone, heterocyclic bases, chemical damage.
- [[Drug Discovery]] ([[Industry and Innovation]]): functional groups and stereochemistry of small molecules.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 5.12 - Organic Chemistry I]] | MIT | L2 | Conformational analysis, alcohols, alkenes and alkynes, aromaticity, carbonyl chemistry; problem sets and exams with solutions[^512] |

## Reference books

- [[Organic Chemistry (OpenStax)]]: ch. 5 for stereochemistry (Stage 1); ch. 26 and 28 for amino acids and nucleic acids; ch. 29 for the organic chemistry of metabolic pathways (the target of Stage 2).[^mcmurry]
- [[Chemistry 2e (OpenStax)]]: ch. 20 "Organic Chemistry", a one-chapter preview of hydrocarbons and functional groups.[^chem2e]

## Lab projects

No Lab project implements organic chemistry directly.

## References

Scope: organic chemistry is required by MIT's biology and computer science-molecular biology majors (5.12), by UC San Diego's bioinformatics major (CHEM 40A-40B) and by Tsinghua's biology program.[^mit7][^mit67][^ucsd][^thu] It is targeted here at biomolecules, the focus advised when taking 5.12 on a bioinformatics path (functional groups, aromaticity, carbonyl chemistry; skim synthesis).[^512] The Stage 2 reaction list is the set of reaction types used by metabolic pathways.[^mcmurry29]

[^512]: [[MIT 5.12 - Organic Chemistry I]], Spring 2005, lecture handout titles (conformational analysis; alcohols, alkenes, alkynes; aromaticity and electrophilic aromatic substitution; carbonyl chemistry).
[^mcmurry]: [[Organic Chemistry (OpenStax)]], ch. 5 "Stereochemistry at Tetrahedral Centers", ch. 26 "Biomolecules: Amino Acids, Peptides, and Proteins", ch. 28 "Biomolecules: Nucleic Acids", ch. 29 "The Organic Chemistry of Metabolic Pathways".
[^mcmurry29]: [[Organic Chemistry (OpenStax)]], ch. 29 "The Organic Chemistry of Metabolic Pathways".
[^chem2e]: [[Chemistry 2e (OpenStax)]], ch. 20 "Organic Chemistry".
[^mit7]: [[MIT - Course 7 Biology]]: 5.12 Organic Chemistry I in the chemistry requirement.
[^mit67]: [[MIT - Course 6-7 Computer Science and Molecular Biology]]: 5.12 Organic Chemistry I in the chemistry block.
[^ucsd]: [[UC San Diego - BS Bioinformatics]]: CHEM 40A and 40B (organic) in the lower division.
[^thu]: [[Tsinghua University - BS Biological Sciences]]: organic chemistry among the natural-science foundations.
