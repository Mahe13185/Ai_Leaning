# 11 - PDF Embeddings & PDF RAG

---

# Introduction

After loading and chunking a PDF, the next step is making it searchable.

This is achieved by:

```text
PDF
↓
Chunks
↓
Embeddings
↓
ChromaDB
↓
Semantic Search
↓
LLM
```

This module transforms a static PDF into an intelligent question-answering system.

---

# Learning Objectives

By the end of this module you should understand:

✅ PDF Embeddings

✅ Vector Representations

✅ ChromaDB Storage

✅ Semantic Search

✅ Context Retrieval

✅ PDF RAG Pipeline

---

# Module Structure

```text
11-PDF-Embeddings

├── 01-create_pdf_embeddings.py
├── 02-store_chunks_chromadb.py
├── 03-query_pdf.py
├── 04-pdf_rag.py
└── NOTES.md
```

---

# Architecture Overview

```text
Java_Notes.pdf
↓
Extract Text
↓
Chunking
↓
Embeddings
↓
ChromaDB
↓
Question
↓
Retrieve Chunks
↓
Qwen
↓
Answer
```

---

# Concept 1: Embeddings

An embedding is a numerical representation of text.

Example:

```text
Java is a programming language.
```

becomes:

```python
[
  0.12,
  -0.43,
  0.98,
  ...
]
```

---

# Why Embeddings?

Computers cannot understand:

```text
Java
Spring
Database
```

directly.

Embeddings convert text into numbers.

---

# Flowchart

Text
↓
Embedding Model
↓
Vector

---

# Creating Embeddings

Model Used:

```python
from sentence_transformers import SentenceTransformer
```

Load Model:

```python
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
```

---

# Generate Embeddings

```python
embedding = model.encode(chunk)
```

Output:

```python
numpy.ndarray
```

---

# Embedding Dimension

```python
print(
    len(embedding)
)
```

Output:

```text
384
```

---

# Important Rule

```text
1 Chunk
↓
1 Embedding
```

Example:

```text
9 Chunks
↓
9 Embeddings
```

---

# Flowchart

Chunk
↓
Embedding Model
↓
384-D Vector

---

# Concept 2: ChromaDB Storage

After generating embeddings:

```text
Chunks
↓
Store
```

inside ChromaDB.

---

# Creating Database

```python
client = chromadb.PersistentClient(
    path="chroma-db"
)
```

---

# Creating Collection

```python
collection = client.create_collection(
    name="Java_Notes"
)
```

---

# Documents

Example:

```python
documents=[
    "Chunk 1",
    "Chunk 2",
    "Chunk 3"
]
```

---

# IDs

Rule:

```text
1 Document
↓
1 ID
```

Example:

```python
ids=[
    "chunk1",
    "chunk2",
    "chunk3"
]
```

---

# Storing Chunks

```python
collection.add(
    documents=chunks,
    ids=ids
)
```

---

# Verifying Storage

```python
print(
    collection.count()
)
```

Output:

```text
9
```

if 9 chunks are stored.

---

# Flowchart

Chunks
↓
IDs
↓
ChromaDB
↓
Persistent Storage

---

# Concept 3: Semantic Search

User Question:

```text
What is HashMap?
```

---

# Query ChromaDB

```python
result = collection.query(
    query_texts=[question],
    n_results=3
)
```

---

# Retrieved Results

```python
result["documents"]
```

Output:

```text
Chunk About HashMap
Chunk About Collections
Chunk About Java
```

---

# Why Semantic Search?

Normal Search:

```text
HashMap
```

must appear exactly.

---

Semantic Search:

```text
Dictionary
Key Value Storage
Mapping
```

can still retrieve HashMap content.

---

# Flowchart

Question
↓
Embedding
↓
Vector Search
↓
Relevant Chunks

---

# Concept 4: Context Building

Retrieved Chunks:

```python
for doc in result["documents"][0]:
```

Combine into:

```python
context
```

Example:

```text
Chunk A
Chunk B
Chunk C
```

↓

```text
One Context
```

---

# Building Context

```python
context += doc + "\n"
```

---

# Flowchart

Chunk 1
+
Chunk 2
+
Chunk 3
↓
Context

---

# Concept 5: Prompt Engineering

Prompt:

```python
prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not found in the context,
say "I don't know based on the provided context."

Context:
{context}

Question:
{question}

Answer:
"""
```

---

# Why Prompt Engineering?

Without instructions:

```text
LLM Hallucinates
```

With instructions:

```text
Uses Retrieved Context
```

---

# Concept 6: Ollama Integration

Send Prompt:

```python
requests.post(
    "http://localhost:11434/api/generate"
)
```

---

# Model Used

```text
qwen3:4b
```

---

# Response

```python
response.json()
```

---

# AI Answer

```python
print(
    result["response"]
)
```

Output:

```text
HashMap stores key-value pairs...
```

---

# Complete RAG Flow

User Question
↓
ChromaDB Search
↓
Top Chunks
↓
Context
↓
Prompt
↓
Qwen
↓
Answer

---

# Real World Applications

Used in:

✅ ChatPDF

✅ PrivateGPT

✅ Company Knowledge Bases

✅ Research Assistants

✅ Legal Search Systems

✅ Medical Document Search

---

# Interview Questions

## What Is An Embedding?

A numerical vector representation of text used for semantic understanding.

---

## Why Use Embeddings?

Embeddings allow semantic search instead of exact keyword matching.

---

## What Is ChromaDB?

A vector database used to store embeddings, documents, and metadata.

---

## What Is RAG?

Retrieval Augmented Generation retrieves relevant information before generating an answer.

---

## Why Build Context?

The LLM needs relevant information before answering.

---

## What Is Semantic Search?

A search technique that retrieves results based on meaning rather than exact words.

---

## Why Use ChromaDB Instead Of Normal Databases?

Traditional databases store rows and columns.

Vector databases store embeddings and perform similarity search.

---

# Common Mistakes

❌ Using 1 ID for multiple documents

❌ Forgetting chunking before embeddings

❌ Forgetting context building

❌ Sending question directly to LLM

❌ Not checking response.json()

❌ Using documents=[chunks] instead of documents=chunks

---

# Key Takeaways

✅ Embeddings convert text into vectors

✅ ChromaDB stores chunks and embeddings

✅ Semantic Search retrieves relevant chunks

✅ Context is built from retrieved chunks

✅ Qwen answers using retrieved information

✅ This is a complete PDF RAG system

---

# Folder Summary

01-create_pdf_embeddings.py

Learned:

* Embeddings
* Sentence Transformers
* Vector Dimensions

---

02-store_chunks_chromadb.py

Learned:

* ChromaDB Storage
* Collections
* IDs

---

03-query_pdf.py

Learned:

* Semantic Search
* Querying
* Retrieval

---

04-pdf_rag.py

Learned:

* Context Building
* Prompt Engineering
* Ollama Integration
* Complete RAG Pipeline

---

# Final Flowchart

PDF
↓
Extract Text
↓
Chunking
↓
Embeddings
↓
ChromaDB
↓
Question
↓
Retrieve Chunks
↓
Context
↓
Qwen
↓
Answer
