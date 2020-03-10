# COMP3311 Notes

# Table Content

# Data Modelling

## Introduction
Aims of Data Modelling:
- Describes **information** that's contained in the database.
  - e.g. entities: students, courses, accounts, branches, patients, etc.
- Describes **relationships** between data items.
  - e.g. John is **enrolled** in COMP3311, Tom's account is **held** at Coogee, etc.
- Describes **constraints** on data.
  - e.g. 7-digit IDs, students can enrol in no more than 3 courses a trimester.
  
Data modelling is a *design process*.
- Converting requirements into a data model.

## Kinds of Data Models
- **Logical**:
  - abstract, for conceptual design.
    - e.g. ER, ODL
- **Physical**:
  - record-based, for implementation.
    - e.g. relational

**Strategy**: Design using an abstract model; map to a physical model.

## Important aspects of Data Modelling
- **Correctness**
  - Satisfies requirements accurately.
- **Completeness**
  - All requirements covered, all assumptions explicit.
- **Consistency**
  - No contradictory statements.

# Entity-Relationship (ER) Model
Entity-Relationship Model has three major modelling constructs:
- **attribute**: *data item* describing a property of interest.
- **entity**: collection of attributes describing *object* of interest.
- **relationship**: *association* between entities(objects).

## Entity Sets
An **entity set** can be viewed as:
  - A set of entities with the same set of attributes (extensional).
  - An abstract description of a class of entities (intensional).

**Key(Superkey)**: Any set of attributes:
  - Whose set of values are distinct over entity set.
  - Natural (e.g. name+address+birthday) or Abstract (e.g. SSN)

**Candidate Key**: Minimal Superkey (no subset is a key)

**Primary Key**: Candidate key chosen by DB designer.

**Keys are indicated in ER Diagrams by underlining*

## Relationship Sets
**Relationship**: An association among several entities.
- e.g. Customer(9876) *is the owner of* Account(12345)

**Relationship Set**: Collection of *Relationships* of the same type.

**Degree**: The number of entities involved in a relation.
- In the ER Model, it's >= 2.

**Cardinality**: The number of **associated** entities on each side of a relation.

**Participation**: Must every entity be in the relationship
![]()
