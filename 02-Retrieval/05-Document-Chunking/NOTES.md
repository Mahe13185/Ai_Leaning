# Document Chunking

> Folder: `02-Retrieval/05-Document-Chunking`

---

# 📌 Overview

Document Chunking is the process of breaking a large document into smaller pieces called **chunks**.

Chunking is one of the most important concepts in Retrieval-Augmented Generation (RAG).

Without chunking, large documents become difficult to search efficiently.

Almost every production RAG system uses chunking before generating embeddings.

---

# 🤔 The Problem

Imagine we have a PDF containing:

```text
Java is a programming language.

JDBC is used to connect Java to databases.

Spring Boot is a framework.

MySQL is a relational database.

Docker is a containerization platform.

Kubernetes manages containers.
```

Suppose we create one embedding for the entire document.

```text
Entire Document
       ↓
One Embedding
```

Now the user asks:

```text
What is JDBC?
```

The retriever must search through the meaning of the entire document.

This is inefficient.

---

# 💡 Solution

Split the document into smaller chunks.

Example:

```text
Chunk 1
--------
Java is a programming language.

JDBC is used to connect Java to databases.

Chunk 2
--------
Spring Boot is a framework.

MySQL is a relational database.

Chunk 3
--------
Docker is a containerization platform.

Kubernetes manages containers.
```

Now each chunk gets its own embedding.

---

# 🌎 Real World Example

Imagine a 500-page book.

Question:

```text
Who is Harry Potter?
```

Would you:

```text
Read all 500 pages?
```

or

```text
Read the relevant chapter?
```

Chunking helps AI retrieve only the relevant part.

---

# Without Chunking

```text
PDF
 ↓
One Huge Embedding
 ↓
Search
```

Problems:

❌ Less accurate

❌ Large context

❌ Slower retrieval

❌ Poor scalability

---

# With Chunking

```text
PDF
 ↓
Chunk 1
Chunk 2
Chunk 3
 ↓
Embeddings
 ↓
Search
```

Benefits:

✅ Better retrieval

✅ Better scalability

✅ Better context management

✅ Faster search

---

# 🏗 Architecture

```text
+----------------+
|   Document     |
+----------------+
         |
         v
+----------------+
| Chunking       |
+----------------+
         |
         v
+----------------+
| Chunk 1        |
| Chunk 2        |
| Chunk 3        |
+----------------+
         |
         v
+----------------+
| Embeddings     |
+----------------+
```

---

# 🔄 Workflow

```text
Document
    ↓
Split Into Chunks
    ↓
Create Embeddings
    ↓
Store Embeddings
    ↓
Similarity Search
    ↓
Retrieve Chunks
```

---

# What Is A Chunk?

A chunk is a small section of a document.

Example:

```python
[
    "Java",
    "JDBC"
]
```

This becomes:

```text
Chunk 1
```

---

Another:

```python
[
    "Spring",
    "MySQL"
]
```

This becomes:

```text
Chunk 2
```

---

# Chunking Logic

Suppose:

```python
sentences = [
    "Java",
    "JDBC",
    "Spring",
    "MySQL",
    "Docker",
    "Kubernetes"
]
```

---

# Step 1

Create Empty Chunk List

```python
chunks = []
```

---

# Step 2

Loop Through Data

```python
for i in range(
    0,
    len(sentences),
    2
):
```

---

# Understanding range()

```python
range(
    0,
    len(sentences),
    2
)
```

Meaning:

```text
Start = 0

Stop = Length

Step = 2
```

Generated Indexes:

```text
0
2
4
```

---

# Visual Representation

Indexes:

```text
0 1 2 3 4 5
```

Values:

```text
Java
JDBC
Spring
MySQL
Docker
Kubernetes
```

Loop visits:

```text
0
2
4
```

---

# Step 3

Create Chunk

```python
chunk = sentences[i:i+2]
```

---

# First Iteration

```python
sentences[0:2]
```

Output:

```python
[
    "Java",
    "JDBC"
]
```

---

# Second Iteration

```python
sentences[2:4]
```

Output:

```python
[
    "Spring",
    "MySQL"
]
```

---

# Third Iteration

```python
sentences[4:6]
```

Output:

```python
[
    "Docker",
    "Kubernetes"
]
```

---

# Final Result

```python
[
    ["Java","JDBC"],
    ["Spring","MySQL"],
    ["Docker","Kubernetes"]
]
```

---

# Joining Chunks

Problem:

```python
[
    ["Java","JDBC"]
]
```

Embedding models work better with text.

---

Solution:

```python
" ".join(chunk)
```

---

Example

```python
chunk = [
    "Java",
    "JDBC"
]
```

Output:

```text
Java JDBC
```

---

# Complete Code

```python
chunks = []

for i in range(
    0,
    len(sentences),
    2
):

    chunk = sentences[i:i+2]

    chunks.append(
        " ".join(chunk)
    )

print(chunks)
```

---

# Output

```python
[
    "Java JDBC",
    "Spring MySQL",
    "Docker Kubernetes"
]
```

---

# What Happens If Sentences Are Odd?

Example:

```python
[
    "Java",
    "JDBC",
    "Spring",
    "MySQL",
    "Docker",
    "Kubernetes",
    "Python"
]
```

Total:

```text
7 Sentences
```

Chunk Size:

```text
2
```

Output:

```python
[
    ["Java","JDBC"],
    ["Spring","MySQL"],
    ["Docker","Kubernetes"],
    ["Python"]
]
```

Notice:

Last chunk contains only one sentence.

Python handles this automatically.

---

# Why Chunk Size Matters

## Very Small Chunks

```text
1 Sentence
```

Problems:

❌ Less context

❌ Incomplete information

---

## Very Large Chunks

```text
50 Sentences
```

Problems:

❌ Too much irrelevant information

❌ Reduced retrieval quality

---

## Balanced Chunks

```text
5-20 Sentences
```

Usually preferred.

---

# Real Industry Usage

Chunking is used in:

### PDF Chatbots

Split PDFs into chunks.

---

### Legal Document Search

Split contracts into sections.

---

### Enterprise Knowledge Bases

Split documentation into chunks.

---

### Research Assistants

Split articles into chunks.

---

### ChatGPT RAG

Chunk documents before retrieval.

---

# Common Mistakes

## Mistake 1

Creating one embedding for the entire PDF.

Result:

Poor retrieval quality.

---

## Mistake 2

Using extremely small chunks.

Result:

Context is lost.

---

## Mistake 3

Using extremely large chunks.

Result:

Too much irrelevant information.

---

## Mistake 4

Forgetting to join chunks into strings.

Wrong:

```python
[
    ["Java","JDBC"]
]
```

Correct:

```python
[
    "Java JDBC"
]
```

---

# 🎤 Interview Questions

## What is Document Chunking?

Document Chunking is the process of splitting large documents into smaller segments before embedding generation and retrieval.

---

## Why is Chunking Important?

Chunking improves retrieval quality and scalability.

---

## Why not embed the entire PDF?

Large documents reduce retrieval precision and make search less efficient.

---

## What is a chunk?

A chunk is a small section of a document used as a retrieval unit.

---

## What happens if chunks are too small?

Important context may be lost.

---

## What happens if chunks are too large?

Retrieval quality decreases due to irrelevant information.

---

# 📝 Revision Cheat Sheet

```text
DOCUMENT CHUNKING

Document
    ↓
Split Into Chunks
    ↓
Chunk Embeddings
    ↓
Search

Chunk Example:

Java JDBC

Spring MySQL

Docker Kubernetes

Important Syntax:

chunk = sentences[i:i+2]

" ".join(chunk)

Benefits:

✓ Better Retrieval
✓ Better Context
✓ Faster Search
✓ RAG Ready

Used In:

✓ PDF Chatbots
✓ RAG Systems
✓ Document Search
✓ AI Assistants
```

---

# 🎯 Key Takeaways

✅ Large documents should be split into chunks.

✅ Each chunk gets its own embedding.

✅ Chunking improves retrieval quality.

✅ Chunk size directly affects performance.

✅ Joining chunks converts lists into searchable text.

✅ Chunking is a core building block of every RAG system.

✅ Modern AI retrieval systems rely heavily on document chunking.
