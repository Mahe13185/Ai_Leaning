# Semantic Search

> Folder: `02-Retrieval/02-Semantic-Search`

---

# 📌 Overview

Semantic Search is a search technique that retrieves information based on meaning rather than exact keyword matches.

Traditional search looks for matching words.

Semantic search looks for matching meaning.

This is one of the core technologies behind:

* ChatGPT Retrieval
* Google Search
* RAG Systems
* AI Assistants
* Recommendation Engines

---

# 🤔 The Problem

Imagine we have:

```text
JDBC is used to connect Java to databases.
```

User asks:

```text
How can Java connect to a database?
```

Traditional search:

```text
Search keyword:
"connect"
"database"

No exact JDBC keyword.
```

Result:

```text
No Match ❌
```

---

# 💡 The Solution

Instead of comparing words:

Compare meaning.

Question:

```text
How can Java connect to a database?
```

↓

Embedding

↓

Compare with stored embeddings

↓

JDBC sentence identified

↓

Result Found ✅

---

# 🌎 Real World Example

### Google Search

Search:

```text
Best phone for photography
```

Google may return:

```text
iPhone Camera Review
Samsung Camera Comparison
Pixel Camera Test
```

Even though the exact words don't match.

Why?

Because Google understands meaning.

This is Semantic Search.

---

# Traditional Search vs Semantic Search

## Traditional Search

```text
Query
 ↓
Keyword Matching
 ↓
Result
```

Example:

```text
Query:
Database Connection
```

Knowledge:

```text
JDBC
```

Result:

```text
No Match
```

---

## Semantic Search

```text
Query
 ↓
Embeddings
 ↓
Similarity Search
 ↓
Result
```

Example:

```text
Database Connection
```

↓

Meaning

↓

JDBC

↓

Match Found

---

# 🏗 Architecture

```text
+----------------+
| User Question  |
+----------------+
         |
         v
+----------------+
| Embedding      |
+----------------+
         |
         v
+----------------+
| Compare With   |
| Knowledge Base |
+----------------+
         |
         v
+----------------+
| Similarity     |
| Scores         |
+----------------+
         |
         v
+----------------+
| Best Match     |
+----------------+
```

---

# 🔄 Workflow

```text
Question
    ↓
Question Embedding
    ↓
Knowledge Embeddings
    ↓
Cosine Similarity
    ↓
Score Calculation
    ↓
Highest Score
    ↓
Best Result
```

---

# Core Idea

Instead of comparing text:

```text
Java
JDBC
Database
```

we compare vectors:

```text
[0.12, -0.34, ...]

[0.18, -0.31, ...]
```

The closer the vectors are:

```text
Higher Similarity
```

---

# Cosine Similarity

Semantic search uses cosine similarity.

Purpose:

```text
Measure how similar two embeddings are.
```

---

## Formula

Cosine Similarity measures the angle between vectors.

Interpretation:

```text
1.0
↓
Very Similar

0.5
↓
Somewhat Similar

0
↓
Unrelated

-1
↓
Opposite
```

---

# Example

Question:

```text
JDBC
```

Knowledge:

```text
Database Connection
```

Score:

```text
0.41
```

---

Question:

```text
JDBC
```

Knowledge:

```text
Dog
```

Score:

```text
0.13
```

Result:

```text
JDBC ↔ Database Connection
```

is more related.

---

# Code Walkthrough

## Step 1

Load Model

```python
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
```

---

## Step 2

Create Embeddings

```python
emb1 = model.encode("JDBC")

emb2 = model.encode(
    "Database Connection"
)
```

---

## Step 3

Calculate Similarity

```python
score = cos_sim(
    emb1,
    emb2
)
```

---

## Step 4

Print Score

```python
print(score)
```

Output:

```text
tensor([[0.4112]])
```

---

# Building Semantic Search

Knowledge:

```python
knowledge = [
    "JDBC is used to connect Java to databases.",
    "Spring Boot is a framework.",
    "Polymorphism allows one interface multiple implementations."
]
```

---

Question:

```python
question = input("Question:")
```

---

Generate Embedding:

```python
questionEmbedding = model.encode(
    question
)
```

---

Compare Against Every Sentence:

```python
for sentence in knowledge:
```

---

Generate Sentence Embedding:

```python
sentenceEmbedding = model.encode(
    sentence
)
```

---

Calculate Similarity:

```python
score = cos_sim(
    questionEmbedding,
    sentenceEmbedding
)
```

---

Store Best Match

```python
best_score = score
best_sentence = sentence
```

---

Return Result

```python
print(best_sentence)
```

---

# Visual Example

Question:

```text
What is JDBC?
```

Knowledge:

```text
Java Programming
JDBC Database Connection
Spring Framework
```

Similarity Scores:

```text
Java Programming      0.52

JDBC Database         0.84

Spring Framework      0.21
```

Best Result:

```text
JDBC Database
```

---

# Common Mistakes

## Mistake 1

Using keywords instead of embeddings.

Wrong:

```python
if question in sentence:
```

This is keyword search.

---

Correct:

```python
cos_sim(...)
```

This is semantic search.

---

## Mistake 2

Forgetting `.item()`

Wrong:

```python
score = cos_sim(...)
```

Returns Tensor.

---

Correct:

```python
score = cos_sim(...).item()
```

Returns Float.

---

## Mistake 3

Comparing raw text.

Always compare embeddings.

---

# Real Industry Usage

Semantic Search is used in:

### ChatGPT

Document Retrieval

### Google

Meaning-based Search

### Amazon

Product Search

### Netflix

Movie Recommendations

### Spotify

Music Recommendations

---

# Interview Questions

## Beginner

### What is Semantic Search?

Semantic Search retrieves information based on meaning rather than exact keyword matches.

---

### Why is Semantic Search better than keyword search?

Because it understands context and meaning.

---

## Intermediate

### How does Semantic Search work?

It converts text into embeddings and compares them using similarity metrics such as cosine similarity.

---

### What metric is commonly used?

Cosine Similarity.

---

## Advanced

### Why are embeddings required for Semantic Search?

Embeddings convert text into numerical vectors that preserve semantic meaning, enabling mathematical comparison.

---

# Revision Cheat Sheet

```text
SEMANTIC SEARCH

Question
 ↓
Embedding
 ↓
Compare
 ↓
Cosine Similarity
 ↓
Highest Score
 ↓
Best Match

Key Function:

cos_sim()

Used In:

✓ Google Search
✓ ChatGPT Retrieval
✓ RAG
✓ Recommendation Systems

Difference:

Keyword Search
=
Matching Words

Semantic Search
=
Matching Meaning
```

---

# 🎯 Key Takeaways

✅ Semantic Search understands meaning.

✅ Embeddings make Semantic Search possible.

✅ Cosine Similarity measures similarity.

✅ Higher score means more related content.

✅ Semantic Search is the foundation of retrieval systems.

✅ RAG systems rely heavily on Semantic Search.
