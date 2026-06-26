# 09 - Document Chunking

## What is Chunking?

Chunking is the process of breaking a large document into smaller pieces called chunks.

Example:

```text
Java is a programming language.
Java supports OOP.
Polymorphism allows one interface to have multiple implementations.
Inheritance allows code reuse.
Encapsulation hides implementation details.
```

Instead of storing the entire document as one piece:

```text
One Huge Document
```

We split it into:

```text
Chunk 1
Chunk 2
Chunk 3
```

---

## Why Do We Need Chunking?

Without Chunking:

```text
Entire PDF
↓
One Embedding
```

Problems:

* Retrieval becomes inaccurate
* Too much information in one vector
* Harder to find relevant content

---

With Chunking:

```text
Document
↓
Chunk 1
Chunk 2
Chunk 3
↓
Embeddings
```

Benefits:

* Better retrieval
* More relevant context
* Faster search
* Better RAG answers

---

# Basic Chunking

Example:

```python
text = """
Java is a programming language.
Java supports OOP.
Polymorphism allows one interface to have multiple implementations.
Inheritance allows code reuse.
Encapsulation hides implementation details.
"""
```

Convert into lines:

```python
sentences = text.strip().splitlines()
```

Output:

```python
[
    "Java is a programming language.",
    "Java supports OOP.",
    "Polymorphism allows one interface to have multiple implementations.",
    "Inheritance allows code reuse.",
    "Encapsulation hides implementation details."
]
```

---

## Create Chunks

```python
chunks = []

for i in range(0, len(sentences), 2):
    chunk = " ".join(sentences[i:i+2])
    chunks.append(chunk)
```

Output:

```python
[
    "Java is a programming language. Java supports OOP.",
    "Polymorphism allows one interface to have multiple implementations. Inheritance allows code reuse.",
    "Encapsulation hides implementation details."
]
```

---

# Why Use Join?

Wrong:

```python
chunk = "".join(sentences[i:i+2])
```

Output:

```text
Java is a programming language.Java supports OOP.
```

No spaces.

---

Correct:

```python
chunk = " ".join(sentences[i:i+2])
```

Output:

```text
Java is a programming language. Java supports OOP.
```

---

# Overlapping Chunks

Problem:

```text
Chunk 1:
Line 1
Line 2

Chunk 2:
Line 3
Line 4
```

Information between:

```text
Line 2
Line 3
```

can be lost.

---

Solution:

```text
Overlap
```

Example:

```text
Chunk 1:
Line 1
Line 2

Chunk 2:
Line 2
Line 3

Chunk 3:
Line 3
Line 4

Chunk 4:
Line 4
Line 5
```

---

## Chunk Size & Overlap

Example:

```text
Chunk Size = 2
Overlap = 1
```

Formula:

```text
Step Size
=
Chunk Size - Overlap
```

Example:

```text
2 - 1 = 1
```

Loop:

```python
for i in range(0, len(sentences), 1):
```

---

# Production Formula

```python
step = chunk_size - overlap
```

Example:

```python
for i in range(
    0,
    len(sentences),
    step
):
```

Works for any chunk size.

---

# Why Overlapping Helps

Without overlap:

```text
Polymorphism means...

multiple implementations.
```

may get split across chunks.

---

With overlap:

```text
Chunk:
Polymorphism means...
multiple implementations.
```

Meaning stays together.

---

# Chunking In Real RAG Systems

Pipeline:

```text
PDF
↓
Extract Text
↓
Chunking
↓
Embeddings
↓
Vector Database
↓
Retrieval
```

Chunking is one of the most important steps in RAG.

---

# Interview Questions

### What is Chunking?

Chunking is the process of splitting a large document into smaller pieces for efficient retrieval and embedding generation.

---

### Why Do We Chunk Documents?

Large documents contain too much information.

Chunking improves retrieval quality and helps LLMs receive only relevant context.

---

### What is Overlapping Chunking?

Overlapping chunking repeats some content between neighboring chunks to preserve context.

Example:

```text
Chunk 1:
Line 1
Line 2

Chunk 2:
Line 2
Line 3
```

---

### Why Is Overlap Useful?

Overlap prevents important information from being split between chunks.

---

### What Happens After Chunking?

```text
Chunks
↓
Embeddings
↓
Vector Database
↓
Retrieval
```

---

# Key Takeaways

✅ Chunking improves retrieval

✅ Smaller chunks create better embeddings

✅ Overlap preserves context

✅ Used in all production RAG systems

✅ Chunking happens before embeddings

---

# Flowchart

Document
↓
Chunking
↓
Embeddings
↓
Vector Database
↓
Similarity Search
↓
RAG
↓
LLM Answer
