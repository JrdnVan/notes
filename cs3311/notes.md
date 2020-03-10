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
- How many Entities are connected to a relationship.  
  - In the ER Model, it's >= 2.
  
**Cardinality**: The number of **associated** entities on each side of a relation.
  - One to one (<-[]->), one to many (<-[]--), many to many (--[]--).

**Participation**: Must every entity be in the relationship
![alt text](https://raw.githubusercontent.com/JrdnVan/notes/master/cs3311/image.png "Participation Example")
- **Total**: All Loans are taken out by Customers.
- **Partial**: Some Customers are allowed to take out Loans.

## Weak Entities
Weak entities exist only because of associations with strong entities.
- Have no key of their own; have a discriminator.

![alt text](https://raw.githubusercontent.com/JrdnVan/notes/master/cs3311/Weak%20Entity%20example.PNG "Weak Entities Example")

## Subclasses and Inheritance

A **subclass** of an entity set A is a set of entities:
- With all attributes of A, plus (usually) it's own attributes.
- Is involved in all of A's relationships, plus it's own.

**Properties** of subclasses:
- **Overlapping** or **disjoint** (Can an entity be in multiple subclasses?)
  - **Overlapping**: Can be a subset of subclasses.
  - **Disjoint**: Can only be one of the subclasses.
- **Total** or **partial** (Does every entity have to also be in a subclass?)
  
Example: Person is a Employee is a Manager.

![alt text](https://www.cse.unsw.edu.au/~cs3311/20T1/lectures/week01/Pics/er-rel/inherit.png "Subclasses Example")

## Relationship Data Model

The **Relationship Data Model** describes the world as a collection of inter-connected relations (or tables).

The goal of the Relation Model:
  - Simple, general data modelling formalism.
  - Maps easily to file structures. (i.e. implementable).

Has two styles of terminologies:
  - Mathematical: relation, tuple, attribute, ...
  - Data-oriented: table, record, field/column, ...

### Structuring mechanisms
- A **relation** corresponds to a mathematical "relation".
- A **relation** can also be viewed as a "table".

Each **relation** (denoted R, S, T,...) has:
- A **name** (unique within a given database)
- A set of **attributes** (which can be viewed as column headings)

Each **attribute** (denoted A, B,... or a1, a2,...) has:
- a **name** (unique within a given relation)
- an associated **domain** (set of allowed values)

DB definition also uses **constraints** (logic expressions)

![alt text](https://www.cse.unsw.edu.au/~cs3311/20T1/lectures/week01/Pics/er-rel/table.png "Relationship Data Model example")

- Attribute values are **atomic**** (no composite or multi-valued variables)
- Each relation has a **key** (subset of attributes unique for each tuple)

Consider relation R with attributes A1, A2,..., An.

- **Relation Schema** of R:  R(A1:D1, A2:D2,...,An:Dn)
- **Tuple** of R: an element of D1 * D2 * ... * Dn (i.e. list of values)
- **Instance** of R: subset of D1 * D2 * ... Dn (i.e. set of tuples)
- **Database Schema**: A colleciton of relation schemas.
- **Database (instance)**: A collection of relation instances. 