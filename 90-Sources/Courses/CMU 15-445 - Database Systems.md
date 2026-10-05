---
aliases:
  - CMU Intro to Database Systems
  - 15-445/645
tags:
  - type/source
  - domain/computer-science
  - level/L2
  - level/L3
kind: course
tier: S
authors:
  - Andy Pavlo
institution: Carnegie Mellon University
year: 2025
url: "https://15445.courses.cs.cmu.edu/fall2025/"
access: free
---

# CMU 15-445 - Database Systems

> [!abstract]
> Carnegie Mellon's introductory course on the design and implementation of database management systems, with free recorded lectures, notes, homework and open-source projects.

## Why this source

Most database courses teach how to use SQL; this one teaches how a database system works inside: storage, buffer management, indexes, query execution, concurrency control and recovery. All lectures are recorded and posted on YouTube, and the slides, notes, homework and project code are open to learners outside CMU. The projects build components of BusTub, a disk-oriented relational database written for teaching.

## Coverage

This note uses the Fall 2025 edition; topics are summarized from the course description, not from a verified lecture list.

| Part | Content | Vault notes |
|---|---|---|
| Relational model | Relational model, SQL, relational algebra | [[Relational Database]], [[SQL]], [[Relational Algebra]] |
| Storage | Disk-oriented storage, buffer pool, storage models | [[Columnar Storage]] |
| Indexes | Hash tables and B+ trees | [[Database Index]] |
| Query processing | Query execution and optimization | [[Query Processing]] |
| Transactions | Concurrency control and crash recovery | [[Database Transaction]] |
| Projects | BusTub: buffer pool manager, B+ tree, query executors and optimizer, concurrency control | [[Relational Database]] |

Cited in [[Databases]].

## How to use it

- L2: watch the lectures on the relational model, storage and indexes for Stage 2 of [[Databases]]; do the SQL homework.
- L3: attempt the BusTub projects if you want to understand performance; otherwise watch the query processing and transaction lectures.

## Caveats

- Systems course: projects are in C++ and demanding.
- Each semester's site and playlist differ; earlier editions remain online.
- Verified in this pass: course number, instructor, Fall 2025 website, free lectures and materials, BusTub projects.
