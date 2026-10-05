---
aliases:
  - Data Management Systems
  - Bases de données
tags:
  - type/moc
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Data Structures]]"
  - "[[Mathematical Foundations]]"
projects:
  - "[[03-genome-diff]]"
  - "[[09-genome-browser]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[Python for Data Analysis (McKinney)]]"
---

# Databases

> [!abstract]
> How data is modeled, queried, indexed and stored: the relational model and SQL, schema design and indexing, analytical engines and columnar formats, array containers such as HDF5 and Zarr, and the storage ideas (block compression, indexes) behind random access to genomic files.

## Why it matters for bioinformatics

Bioinformatics is data-bound before it is compute-bound. You download from and query public [[Biological Database|biological databases]]; laboratory sample tracking needs transactions; an analysis joins sample metadata to count tables; large numeric matrices live in array containers; and a genome browser can fetch one region of a large alignment file without reading the rest only because the file is block-compressed and indexed. UC San Diego's bioinformatics major gives biological databases a dedicated course next to sequence analysis.[^ucsd]

## Before you start

- [[Data Structures]]: [[Hash Table]], [[B-Tree]] (Stage 3 of that syllabus, needed for [[Database Index]]).
- [[Algorithms]]: [[Sorting]] and [[External Memory Algorithm]] (for [[Query Processing]]).
- [[Mathematical Foundations]]: [[Set]] and [[Function]]: a relation is a set of tuples.
- [[Programming]]: [[Data Frame]], the in-memory table you will load query results into.

## Learning path

> [!tip] Order of study
> As a web developer you probably know SQL and transactions: review items 3, 4 and 9 quickly and spend the time on analytical and array storage (items 10 to 12, then 15), which web work rarely meets.

### Stage 1 - Foundations (L1)

1. [[Delimited Text Format]] (L1): read and write CSV and TSV safely (delimiters, quoting, headers, encodings, missing values) and control type inference on load.
2. [[Data Serialization]] (L1): exchange structured data as JSON or YAML, validate it against a schema, and parse the responses of biological database APIs.
3. [[Relational Database]] (L1): describe data with the relational model (relations, primary and foreign keys, integrity constraints) and know what a relational database management system adds (samples, genes, measurements).
4. [[SQL]] (L1): query with SELECT, WHERE, JOIN, GROUP BY, subqueries and window functions in SQLite or DuckDB.

### Stage 2 - Core (L2)

5. [[Relational Algebra]] (L2): express queries with selection, projection, join, union and difference, the algebra SQL is compiled to.
6. [[Entity-Relationship Model]] (L2): design a schema from entities and relationships (sample, sequencing run, variant, gene) and map it to tables.
7. [[Database Normalization]] (L2): remove redundancy with functional dependencies and normal forms up to BCNF, and denormalize deliberately for analytics.
8. [[Database Index]] (L2): speed up lookups and range queries with B+ tree and hash indexes, read a query plan, and accept the write cost knowingly.
9. [[Database Transaction]] (L2): guarantee atomicity, consistency, isolation and durability, and choose an isolation level for concurrent writers.
10. [[Embedded Database]] (L2): use an in-process database stored in a single file (SQLite for records, DuckDB for analytics) instead of a server when one user owns the data.
11. [[Columnar Storage]] (L2): store tables by column (Parquet, Arrow) for compression and fast scans, and contrast transactional row stores with analytical column stores.
12. [[Hierarchical Data Format]] (L2): organize large numeric arrays in HDF5 groups and chunked, compressed datasets, the container behind common single-cell file formats.
13. [[NoSQL Database]] (L2): choose between key-value, document and wide-column stores when schema flexibility or scale outweighs joins and transactions.

### Stage 3 - Advanced (L3)

14. [[Query Processing]] (L3): follow a query from parsing to an optimized plan, and compare nested-loop, hash and sort-merge joins.
15. [[Chunked Array Storage]] (L3): store N-dimensional arrays as independently compressed chunks in object storage (Zarr) for cloud-native imaging and single-cell data.
16. [[Graph Database]] (L3): model and query biological networks and knowledge graphs as property graphs.
17. [[Resource Description Framework]] (L3): read linked data as subject-predicate-object triples and query public resources with SPARQL.

## Uses from other domains

- [[Biological Database]] and [[Accession Number]] ([[Bioinformatics Foundations]]): the public resources this syllabus teaches you to query and mirror.
- [[SAM Format]], [[VCF Format]] and [[BED Format]] ([[Bioinformatics Foundations]]): genomic tables stored as text, then compressed and indexed.
- [[Genomic File Indexing]] ([[Bioinformatics Foundations]]): bgzip, tabix, BAI and FAI indexes, block compression plus an index, the genomic application of [[Database Index]]; study it right after item 8.
- [[Programmatic Database Access]] ([[Bioinformatics Foundations]]): querying NCBI, Ensembl and UniProt APIs, whose responses are [[Data Serialization|serialized]] JSON or XML.
- [[Tidy Data]] and [[Laboratory Information Management System]] ([[Research Data Management]]): table layout for analysis, and the transactional system that tracks samples.
- [[Biological Ontology]] ([[Bioinformatics Foundations]]): controlled vocabularies published as RDF graphs.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[CMU 15-445 - Database Systems]] | Carnegie Mellon University | L2 | Relational model, SQL, storage, indexing, query processing, transactions |
| [[UC San Diego - BS Bioinformatics]] | UC San Diego | L3 | BIMM 182 Biological Databases, in the named bioinformatics sequence[^ucsd] |

## Reference books

- [[Python for Data Analysis (McKinney)]] (3rd ed.): loading, cleaning, merging and reshaping tabular data with pandas, the client side of Stage 1 and Stage 2.[^mckinney]

## Lab projects

- [[03-genome-diff]]: variants written as [[VCF Format]] records, later compressed and indexed ([[Genomic File Indexing]]).
- [[09-genome-browser]]: region queries on FASTA, GFF and VCF files, through [[Genomic File Indexing|indexed files]] for large tracks and an [[Embedded Database]] for annotations.
- [[10-genomic-pipeline]]: BAM and VCF outputs, and sample metadata kept in an [[Embedded Database]].

## References

[^ucsd]: [[UC San Diego - BS Bioinformatics]]: BIMM 182 Biological Databases belongs to the named bioinformatics sequence, with BIMM 181 Molecular Sequence Analysis and BENG 183 Applied Genomic Technologies.
[^mckinney]: [[Python for Data Analysis (McKinney)]], 3rd ed.: pandas data loading, cleaning, merging and reshaping.
