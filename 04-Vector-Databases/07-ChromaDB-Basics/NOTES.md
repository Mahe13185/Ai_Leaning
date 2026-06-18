# 📚 07 - ChromaDB Basics

---

# 🎯 What is ChromaDB?

ChromaDB is a Vector Database used to store:

* Documents
* Embeddings
* Metadata
* IDs

Unlike FAISS, ChromaDB automatically handles embedding generation and document storage.

---

# 🤔 Why Do We Need ChromaDB?

In FAISS we manually managed:

* knowledge.txt
* Embeddings
* knowledge.index
* Sentence Mapping

Example:

knowledge.txt
↓
Generate Embeddings
↓
Create FAISS Index
↓
Store Index
↓
Search

As projects grow, managing everything manually becomes difficult.

ChromaDB solves this problem by storing everything together.

---

# FAISS vs ChromaDB

## FAISS

Stores:

* Vectors Only

Architecture:

Document
↓
Embedding
↓
FAISS
↓
Vector Search

Problems:

❌ No Metadata

❌ No Document Storage

❌ Manual Mapping Required

---

## ChromaDB

Stores:

* Documents
* Embeddings
* Metadata
* IDs

Architecture:

Document
↓
Embedding
↓
ChromaDB Collection
↓
Search

Advantages:

✅ Automatic Embeddings

✅ Metadata Support

✅ Persistent Storage

✅ Easy Retrieval

---

# 🏗️ ChromaDB Architecture

Documents
↓
Automatic Embeddings
↓
Collection
↓
Persistent Storage
↓
Query
↓
Results

---

# Important Terminologies

## Client

Used to connect with ChromaDB.

Example:

```python
client = chromadb.Client()
```

Temporary storage.

---

## Persistent Client

Used to save collections permanently.

Example:

```python
client = chromadb.PersistentClient(
    path="chroma_db"
)
```

Data remains even after program termination.

---

## Collection

Collection in ChromaDB is similar to a Table in MySQL.

MySQL:

Database
↓
Table
↓
Rows

ChromaDB:

Database
↓
Collection
↓
Documents

Example:

```python
collection = client.create_collection(
    name="Java_Topics"
)
```

---

## Document

Actual text stored inside collection.

Example:

```text
Java is a programming language.
```

---

## Metadata

Additional information about documents.

Example:

```python
{
    "topics":"java"
}
```

Used for:

* Categorization
* Filtering
* Source Tracking

---

## IDs

Unique identifiers for documents.

Example:

```python
ids=[
    "id1",
    "id2",
    "id3"
]
```

---

# Creating Collection

Example:

```python
collection.add(
    documents=[
        "Java is a programming language.",
        "JDBC is used to connect Java to databases.",
        "Spring Boot is a framework."
    ],
    metadatas=[
        {"topics":"java"},
        {"topics":"JDBC"},
        {"topics":"Spring"}
    ],
    ids=[
        "id1",
        "id2",
        "id3"
    ]
)
```

---

# ⚡ Automatic Embeddings

In FAISS:

```python
embedding = model.encode(text)
```

We manually created embeddings.

---

In ChromaDB:

```python
collection.add(...)
```

ChromaDB automatically:

Document
↓
Embedding
↓
Storage

No manual embedding creation required.

---

# Querying Collection

Example:

```python
result = collection.query(
    query_texts=[question],
    n_results=3
)
```

---

# Query Flow

User Question
↓
Generate Query Embedding
↓
Compare With Stored Embeddings
↓
Find Similar Documents
↓
Return Results

---

# Understanding Query Results

ChromaDB returns:

```python
{
    "documents": ...
    "metadatas": ...
    "ids": ...
    "distances": ...
}
```

---

## Documents

```python
result["documents"][0]
```

Output:

```text
Java is a programming language.
JDBC is used to connect Java to databases.
Spring Boot is a framework.
```

---

## Metadata

```python
result["metadatas"][0]
```

Output:

```python
{"topics":"java"}
{"topics":"JDBC"}
{"topics":"Spring"}
```

---

## IDs

```python
result["ids"][0]
```

Output:

```text
id1
id2
id3
```

---

## Distances

```python
result["distances"][0]
```

Example:

```text
0.24
0.76
1.46
```

Rule:

# Smaller Distance

Better Match

---

# 🔥 ChromaDB RAG

Architecture:

Question
↓
ChromaDB Query
↓
Retrieve Documents
↓
Build Context
↓
Prompt
↓
Qwen
↓
Answer

---

# Building Context

Example:

```python
context = ""

for doc in result["documents"][0]:
    context += doc + "\n"
```

Output:

```text
Java is a programming language.
JDBC is used to connect Java to databases.
Spring Boot is a framework.
```

---

# RAG Prompt Structure

A good RAG prompt contains:

1. Instructions
2. Context
3. Question

Example:

Instructions
↓
Context
↓
Question
↓
Answer

---

Prompt Example

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

# Example Outputs

Question:

```text
What is JDBC?
```

Answer:

```text
JDBC is used to connect Java to databases.
```

---

Question:

```text
What is Spring Boot?
```

Answer:

```text
Spring Boot is a framework.
```

---

Question:

```text
What is Python?
```

Answer:

```text
I don't know based on the provided context.
```

This proves that the RAG system is grounded and does not hallucinate.

---

# Real World Uses

✅ PDF Chatbot

✅ Research Assistant

✅ Company Knowledge Base

✅ Resume Analyzer

✅ Customer Support Bot

✅ AI Learning Assistant

---

# Common Mistakes

### Mistake 1

Using:

```python
client = chromadb.Client()
```

for multiple files.

Problem:

Collections disappear after program termination.

Solution:

```python
client = chromadb.PersistentClient(
    path="chroma_db"
)
```

---

### Mistake 2

Printing entire result dictionary.

```python
print(result)
```

Instead:

```python
result["documents"][0]
```

---

### Mistake 3

Sending IDs or Distances to Qwen as Context.

Correct:

```python
result["documents"][0]
```

Only documents should be used as context.

---

# Interview Questions

### What is ChromaDB?

A vector database that stores documents, embeddings, metadata, and IDs together.

---

### Difference Between FAISS and ChromaDB?

FAISS stores vectors only.

ChromaDB stores documents, embeddings, metadata, and IDs.

---

### What is a Collection?

A Collection is similar to a table in MySQL.

---

### What is Metadata?

Additional information associated with a document used for categorization and filtering.

---

### Why use PersistentClient?

To save collections permanently on disk.

---

### What is ChromaDB RAG?

A Retrieval-Augmented Generation system that uses ChromaDB to retrieve relevant documents and send them to an LLM.

---

# Key Takeaways

✅ ChromaDB is a Vector Database

✅ Collection = Table

✅ Document = Row

✅ Supports Metadata

✅ Supports Persistent Storage

✅ Generates Embeddings Automatically

✅ Easy Semantic Search

✅ Easy RAG Integration

✅ More Convenient Than FAISS For Production Projects

---

# Progress Tracker

04-Vector-Databases

✅ 01-FAISS

✅ 02-FAISS-Semantic-Search

✅ 03-FAISS-RAG

✅ 04-Source-Aware-RAG

✅ 05-Persistent-Vector-Storage

✅ 06-Persistent-FAISS-RAG

✅ 07-ChromaDB-Basics

⏭️ 08-ChromaDB-Metadata-Filtering

---

# 🚀 Next Topic

08-ChromaDB-Metadata-Filtering

Goal:

Store multiple categories of documents and retrieve only documents matching specific metadata conditions.
