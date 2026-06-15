# Chunked Semantic Search

> Folder: `02-Retrieval/06-Chunked-Semantic-Search`

---

# 📌 Overview

Chunked Semantic Search combines multiple concepts learned earlier:

* Embeddings
* Cosine Similarity
* Semantic Search
* Top-K Retrieval
* Embedding Caching
* Document Chunking

Instead of searching individual sentences, we search chunks of related information.

This is the first step toward building real-world RAG systems.

---

# 🎯 Goal

Before:

```text
Question
   ↓
Search Sentences
   ↓
Return Best Sentence
```

After:

```text
Question
   ↓
Search Chunks
   ↓
Return Best Chunk
```

This provides more context.

---

# 🤔 Problem Statement

Suppose our knowledge file contains:

```text
Java is a programming language.

JDBC is used to connect Java to databases.

MySQL is a relational database.

JDBC drivers allow Java to communicate with MySQL.

Spring Boot is a framework.

Polymorphism allows one interface multiple implementations.
```

Question:

```text
What is JDBC?
```

If we search sentence-by-sentence:

```text
Result:

JDBC is used to connect Java to databases.
```

Correct.

But context is missing.

---

# 💡 Solution

Group related information into chunks.

Chunk 1:

```text
Java is a programming language.

JDBC is used to connect Java to databases.
```

Chunk 2:

```text
MySQL is a relational database.

JDBC drivers allow Java to communicate with MySQL.
```

Chunk 3:

```text
Spring Boot is a framework.

Polymorphism allows one interface multiple implementations.
```

Now search chunks instead of sentences.

---

# 🌍 Real World Example

Imagine a textbook.

Question:

```text
What is JDBC?
```

Would you rather read:

```text
One Sentence
```

or

```text
A Paragraph
```

A paragraph contains more useful context.

Chunked retrieval works exactly like this.

---

# 🏗 Architecture

```text
+------------------+
| Knowledge File   |
+------------------+
          |
          v
+------------------+
| Split Lines      |
+------------------+
          |
          v
+------------------+
| Create Chunks    |
+------------------+
          |
          v
+------------------+
| Chunk Embeddings |
+------------------+
          |
          v
+------------------+
| User Question    |
+------------------+
          |
          v
+------------------+
| Question Vector  |
+------------------+
          |
          v
+------------------+
| Similarity Search|
+------------------+
          |
          v
+------------------+
| Top Chunks       |
+------------------+
```

---

# 🔄 Workflow

```text
Knowledge File
      ↓
Split Into Lines
      ↓
Chunk Creation
      ↓
Chunk Embeddings
      ↓
Question Embedding
      ↓
Cosine Similarity
      ↓
Sort Scores
      ↓
Top Chunks
```

---

# Step 1: Load Knowledge

```python
with open("knowledge.txt", "r") as file:
    knowledge = file.read()
```

Purpose:

Read knowledge from file.

---

# Step 2: Split Into Sentences

```python
sentences = knowledge.splitlines()
```

Example:

```python
[
 "Java is a programming language.",
 "JDBC is used to connect Java to databases.",
 "MySQL is a relational database."
]
```

---

# Step 3: Create Chunks

```python
chunks = []
```

---

Loop:

```python
for i in range(
    0,
    len(sentences),
    2
):
```

---

Create Chunk:

```python
chunk = sentences[i:i+2]
```

---

Join Chunk:

```python
chunks.append(
    " ".join(chunk)
)
```

---

Result:

```python
[
 "Java is a programming language. JDBC is used to connect Java to databases.",

 "MySQL is a relational database. JDBC drivers allow Java to communicate with MySQL.",

 "Spring Boot is a framework. Polymorphism allows one interface multiple implementations."
]
```

---

# Why Join?

Before:

```python
[
 ["Java", "JDBC"]
]
```

After:

```python
[
 "Java JDBC"
]
```

Embedding models expect text.

---

# Step 4: Generate Chunk Embeddings

```python
chunkEmbeddings = []
```

---

Loop:

```python
for chunk in chunks:

    chunkEmbeddings.append(
        model.encode(chunk)
    )
```

---

Result:

```text
Chunk 1 Embedding

Chunk 2 Embedding

Chunk 3 Embedding
```

These embeddings are cached.

---

# Step 5: Question Embedding

```python
question = input(
    "Question: "
)
```

---

Generate Embedding:

```python
questionEmbedding = model.encode(
    question
)
```

---

# Step 6: Similarity Search

Create Scores:

```python
scores = []
```

---

Loop Through Chunk Embeddings:

```python
for i in range(
    len(chunkEmbeddings)
):
```

---

Calculate Similarity:

```python
score = cos_sim(
    questionEmbedding,
    chunkEmbeddings[i]
).item()
```

---

Store Result:

```python
scores.append(
    (
        score,
        chunks[i]
    )
)
```

---

# Why Use chunks[i]?

Wrong:

```python
scores.append(
    (
        score,
        chunks
    )
)
```

This stores the entire list.

---

Correct:

```python
chunks[i]
```

Stores only the current chunk.

---

# Step 7: Sort Results

```python
scores = sorted(
    scores,
    reverse=True
)
```

Highest score first.

---

# Example Output

Question:

```text
What is JDBC?
```

Output:

```python
[
 (
 0.7895,
 "Java is a programming language. JDBC is used to connect Java to databases."
 ),

 (
 0.6968,
 "MySQL is a relational database. JDBC drivers allow Java to communicate with MySQL."
 ),

 (
 0.1805,
 "Spring Boot is a framework. Polymorphism allows one interface multiple implementations."
 )
]
```

---

# Understanding The Output

Chunk 1:

```text
Java is a programming language.

JDBC is used to connect Java to databases.
```

Score:

```text
0.7895
```

Highest score.

Most relevant.

---

Chunk 2:

```text
MySQL is a relational database.

JDBC drivers allow Java to communicate with MySQL.
```

Score:

```text
0.6968
```

Also relevant.

---

Chunk 3:

```text
Spring Boot...
Polymorphism...
```

Score:

```text
0.1805
```

Almost unrelated.

---

# Why Chunked Search Is Better

Sentence Search:

```text
Question
   ↓
Sentence
```

Result:

```text
JDBC is used to connect Java to databases.
```

---

Chunk Search:

```text
Question
   ↓
Chunk
```

Result:

```text
Java is a programming language.

JDBC is used to connect Java to databases.
```

More context.

Better answers.

---

# Complete Flow Diagram

```text
Knowledge File
      ↓
Split Lines
      ↓
Create Chunks
      ↓
Chunk Embeddings
      ↓
Store Embeddings
      ↓
User Question
      ↓
Question Embedding
      ↓
Cosine Similarity
      ↓
Rank Chunks
      ↓
Best Chunks
```

---

# Common Mistakes

## Mistake 1

Using:

```python
sentence[i]
```

instead of:

```python
sentences[i]
```

Result:

Single character.

Example:

```python
'o'
```

instead of full sentence.

---

## Mistake 2

Appending chunks instead of current chunk.

Wrong:

```python
scores.append(
    (
        score,
        chunks
    )
)
```

---

Correct:

```python
scores.append(
    (
        score,
        chunks[i]
    )
)
```

---

## Mistake 3

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

## Mistake 4

Not sorting scores.

Without sorting:

```text
Random Order
```

Not useful.

---

# Real Industry Usage

Used in:

### PDF Chatbots

Retrieve document chunks.

---

### Legal AI

Retrieve contract sections.

---

### Medical Search

Retrieve medical notes.

---

### Research Assistants

Retrieve article sections.

---

### Enterprise RAG

Retrieve company documentation.

---

# 🎤 Interview Questions

## What is Chunked Semantic Search?

Chunked Semantic Search retrieves chunks of text using embeddings and similarity search.

---

## Why use chunks instead of sentences?

Chunks preserve surrounding context and improve retrieval quality.

---

## Why use chunks instead of an entire document?

Large documents reduce retrieval precision.

Chunks improve search accuracy.

---

## What are the benefits of Chunked Search?

* Better Context
* Better Retrieval
* Better Scalability
* Better RAG Performance

---

## What concepts are combined in Chunked Semantic Search?

* Embeddings
* Cosine Similarity
* Semantic Search
* Top-K Retrieval
* Caching
* Chunking

---

# 📝 Revision Cheat Sheet

```text
CHUNKED SEMANTIC SEARCH

Document
    ↓
Chunks
    ↓
Chunk Embeddings
    ↓
Question Embedding
    ↓
Cosine Similarity
    ↓
Sort Scores
    ↓
Best Chunks

Important Syntax:

chunk = sentences[i:i+2]

" ".join(chunk)

chunkEmbeddings.append(
    model.encode(chunk)
)

score = cos_sim(
    questionEmbedding,
    chunkEmbeddings[i]
).item()

Used In:

✓ PDF Chatbots
✓ RAG Systems
✓ Document Search
✓ AI Assistants

Key Idea:

Search Chunks
Not Sentences
```

---

# 🎯 Key Takeaways

✅ Chunked Search combines all retrieval concepts learned so far.

✅ Chunks provide more context than individual sentences.

✅ Each chunk gets its own embedding.

✅ Similarity search is performed on chunk embeddings.

✅ Results are ranked by cosine similarity.

✅ Chunked Search is the foundation of real-world RAG systems.

✅ This is the final step before moving into Multi-Chunk RAG and full document chatbots.
