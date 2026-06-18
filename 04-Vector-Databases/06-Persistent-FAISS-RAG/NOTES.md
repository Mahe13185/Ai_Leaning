# 📚 Persistent FAISS RAG NOTES

> Building a Retrieval-Augmented Generation (RAG) system using a saved FAISS index.

---

# 🎯 What is Persistent FAISS RAG?

Persistent FAISS RAG combines:

* Persistent Vector Storage
* FAISS Retrieval
* Qwen
* Context Injection

Unlike normal FAISS RAG, embeddings are generated only once.

---

# 🤔 Problem with Normal FAISS RAG

Every run:

```text
knowledge.txt
      ↓
Generate Embeddings
      ↓
Create FAISS
      ↓
Search
      ↓
Qwen
```

This becomes expensive when documents grow.

---

# 🚀 Persistent FAISS RAG Solution

Generate embeddings once:

```text
knowledge.txt
      ↓
Embeddings
      ↓
FAISS
      ↓
knowledge.index
```

Then:

```text
knowledge.index
      ↓
Load
      ↓
Search
      ↓
Qwen
```

No document embeddings are regenerated.

---

# 📂 Project Structure

```text
06-Persistent-FAISS-RAG

├── knowledge.txt
├── knowledge.index
├── create_index.py
├── persistent_faiss_rag.py
└── NOTES.md
```

---

# Step 1: Create Index

Read knowledge:

```python
with open("knowledge.txt", "r") as file:
    knowledge = file.read()

sentences = knowledge.splitlines()
```

---

Generate embeddings:

```python
embeddings = []

for sentence in sentences:
    embeddings.append(
        model.encode(sentence)
    )
```

---

Convert to vectors:

```python
vectors = np.array(
    embeddings,
    dtype=np.float32
)
```

---

Create FAISS:

```python
index = faiss.IndexFlatL2(384)
```

---

Store vectors:

```python
index.add(vectors)
```

---

Save index:

```python
faiss.write_index(
    index,
    "knowledge.index"
)
```

---

# Step 2: Load Saved Index

Instead of recreating:

```python
index = faiss.read_index(
    "knowledge.index"
)
```

---

# Step 3: Read Original Text

FAISS stores:

```text
Vectors
```

Not:

```text
Original Text
```

Therefore:

```python
with open("knowledge.txt", "r") as file:
    knowledge = file.read()

sentences = knowledge.splitlines()
```

---

# Step 4: Ask Question

```python
question = input(
    "Question: "
)
```

---

# Step 5: Create Query Embedding

```python
questionEmbedding = model.encode(
    question
)

questionVector = np.array(
    [questionEmbedding],
    dtype=np.float32
)
```

---

# Step 6: Search FAISS

```python
D, I = index.search(
    questionVector,
    3
)
```

Returns:

```python
I = [[1,0,2]]
```

and

```python
D = [[0.31,0.94,1.43]]
```

---

# Understanding I

```text
Indexes
```

Example:

```python
I = [[1,0,2]]
```

Meaning:

```text
Best Match     → Sentence 1

Second Match   → Sentence 0

Third Match    → Sentence 2
```

---

# Understanding D

```text
Distances
```

Example:

```python
D = [[0.31,0.94,1.43]]
```

Rule:

```text
Smaller Distance = Better Match
```

---

# Step 7: Build Context

```python
context = ""

for indexValue in I[0]:
    context += (
        sentences[indexValue]
        + "\n"
    )
```

Example:

```text
JDBC is used to connect Java to databases.

Java is a programming language.

Spring Boot is a framework.
```

---

# Step 8: Create Prompt

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

# Step 9: Send To Qwen

```python
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen3:4b",
        "prompt": prompt,
        "stream": False
    }
)
```

---

# Step 10: Generate Answer

```python
print(
    ai_response["response"]
)
```

---

# Example Run

Question:

```text
What is JDBC?
```

Retrieved Context:

```text
JDBC is used to connect Java to databases.

Java is a programming language.

Spring Boot is a framework.
```

Answer:

```text
JDBC is used to connect Java to databases.
```

---

# Architecture

```text
knowledge.txt
      ↓
create_index.py
      ↓
knowledge.index
      ↓
persistent_faiss_rag.py
      ↓
Question
      ↓
FAISS Retrieval
      ↓
Context
      ↓
Qwen
      ↓
Answer
```

---

# Difference from Persistent Search

## Persistent Search

```text
Question
      ↓
FAISS
      ↓
Top Results
```

Output:

```text
Retrieved Sentences
```

---

## Persistent FAISS RAG

```text
Question
      ↓
FAISS
      ↓
Top Results
      ↓
Qwen
      ↓
Answer
```

Output:

```text
Generated Answer
```

---

# Interview Questions

## What is Persistent FAISS RAG?

A RAG system that loads a previously saved FAISS index instead of recreating embeddings every run.

---

## Why is it faster?

Embeddings are generated once and reused through the saved index.

---

## What does FAISS store?

Vectors only.

---

## Why do we still need knowledge.txt?

To map retrieved vector indexes back to human-readable text.

---

## What is the role of Qwen?

Generate answers using retrieved context.

---

# Key Takeaways

✅ Persistent Vector Storage

✅ FAISS Retrieval

✅ Context Building

✅ Query Embeddings

✅ Grounded Generation

✅ Faster RAG Systems

✅ Production-Oriented Design

---

# Progress

```text
04-Vector-Databases

├── 01-FAISS                    ✅
├── 02-FAISS-Semantic-Search    ✅
├── 03-FAISS-RAG               ✅
├── 04-FAISS-Source-Aware-RAG  ✅
├── 05-Persistent-Vector-Storage ✅
└── 06-Persistent-FAISS-RAG    ✅
```

---

# 🚀 Next Topic

```text
04-Vector-Databases
└── 07-ChromaDB-Basics
```

Goal:

```text
Collections
Metadata
Persistent Storage
Built-in Retrieval
Real Vector Database
```
