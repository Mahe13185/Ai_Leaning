# Embeddings Basics

> Folder: `02-Retrieval/01-Embeddings-Basics`

---

# 📌 Overview

Embeddings are the foundation of modern AI retrieval systems.

Before learning Semantic Search, RAG, Vector Databases, LangChain, or AI Agents, it is important to understand embeddings.

An embedding converts human-readable text into a numerical representation (vector) that a computer can understand and compare.

---

# 🤔 The Problem

Computers do not understand language.

For example:

```text
Java
JDBC
Database
Dog
Cat
```

To humans:

```text
Java ↔ JDBC ✅ Related
Java ↔ Database ✅ Related
Java ↔ Dog ❌ Unrelated
```

To a computer:

```text
Java = String
JDBC = String
Dog = String
```

The computer sees only characters.

It cannot understand meaning.

---

# 💡 The Solution

Convert text into numbers.

```text
Java
  ↓
Embedding Model
  ↓
[-0.23, 0.11, 0.76, ...]
```

Now the computer can compare vectors mathematically.

---

# 🌎 Real World Example

Imagine Google Search.

User searches:

```text
How can Java connect to a database?
```

Google should understand:

```text
JDBC
Database Connection
MySQL
```

even though the exact words may not match.

This is possible because of embeddings.

---

# 🏗 Architecture

```text
+-----------+
|   Text    |
+-----------+
      |
      v
+----------------------+
| Embedding Model      |
| all-MiniLM-L6-v2     |
+----------------------+
      |
      v
+----------------------+
| Numerical Vector     |
| 384 Dimensions       |
+----------------------+
      |
      v
AI Processing
```

---

# 🔄 Workflow

```text
Input Text
     ↓
Tokenization
     ↓
Embedding Model
     ↓
Vector Generation
     ↓
Store Embedding
     ↓
Similarity Search
```

---

# 📚 What Is an Embedding?

An embedding is a numerical vector representation of text.

Example:

Text:

```text
Java
```

Embedding:

```text
[-0.021, 0.114, -0.532, 0.871, ...]
```

This vector contains semantic information about the text.

---

# 📏 Dimensions

When you ran:

```python
print(len(embedding))
```

Output:

```text
384
```

This means:

```text
Java
```

was converted into:

```text
384 numerical values
```

These values together represent the meaning of the text.

---

# 🧠 Important Concept

Think of embeddings like coordinates on a map.

Example:

```text
Java
Database
JDBC
```

might be close together.

```text
Dog
Cat
Tiger
```

might form another cluster.

Visual Representation:

```text
                    Dog
                     *
                    /
                   /
                  *

Cat ------------------- Tiger


Java *---- JDBC
        \
         \
          * Database
```

Similar meanings are closer together.

Different meanings are farther apart.

---

# ⚙ Model Used

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
```

---

# 🔍 Syntax Breakdown

## Creating Model

```python
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
```

### Explanation

| Part                | Meaning                    |
| ------------------- | -------------------------- |
| SentenceTransformer | Loads embedding model      |
| all-MiniLM-L6-v2    | Pretrained embedding model |

---

## Creating Embedding

```python
embedding = model.encode(
    "Java"
)
```

### Explanation

| Part     | Meaning                   |
| -------- | ------------------------- |
| model    | Loaded embedding model    |
| encode() | Converts text into vector |
| "Java"   | Input text                |

---

# 💻 Complete Example

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embedding = model.encode("Java")

print(embedding)
print(len(embedding))
```

---

# 📤 Example Output

```text
[-0.12 0.45 0.89 ...]
```

Length:

```text
384
```

---

# 🎯 Why Embeddings Matter

Without embeddings:

```text
Keyword Search
```

Search:

```text
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

With embeddings:

```text
Database Connection
```

↓

```text
Embedding
```

↓

```text
JDBC
```

↓

```text
Match Found
```

This is called Semantic Search.

---

# 🚀 Applications

Embeddings are used in:

### Semantic Search

```text
Google Search
ChatGPT Search
Knowledge Search
```

### RAG Systems

```text
PDF Chatbots
Research Assistants
Document Search
```

### Recommendation Systems

```text
Netflix
YouTube
Amazon
Spotify
```

### Clustering

Grouping similar documents together.

---

# ❌ Common Mistakes

## Mistake 1

Thinking embeddings store text.

Wrong:

```text
Embedding = Text
```

Correct:

```text
Embedding = Numerical Meaning
```

---

## Mistake 2

Trying to read embeddings manually.

Wrong:

```text
[-0.12, 0.56, ...]
```

These numbers are not meant for humans.

---

## Mistake 3

Comparing vectors manually.

Always use:

```python
cos_sim()
```

for similarity comparison.

---

# 🧪 Practice Questions

### Question 1

What is the output of:

```python
embedding = model.encode(
    "Spring Boot"
)
```

Answer:

A numerical vector representation of the text.

---

### Question 2

What does:

```python
len(embedding)
```

return?

Answer:

The number of dimensions in the embedding vector.

---

# 🎤 Interview Questions

## Beginner

### What is an embedding?

An embedding is a numerical vector representation of text that captures semantic meaning.

---

### Why do we need embeddings?

Computers cannot understand text directly. Embeddings convert text into numerical vectors that can be compared mathematically.

---

## Intermediate

### What does the dimension size represent?

The dimension size represents the number of numerical features used to represent semantic meaning.

---

### Why are embeddings useful in AI?

Embeddings enable semantic search, clustering, recommendation systems, and retrieval-augmented generation (RAG).

---

## Advanced

### Can two different sentences have similar embeddings?

Yes.

If they have similar meanings, their embeddings will be close in vector space.

Example:

```text
Java Database Connection

JDBC
```

---

# 📝 Revision Cheat Sheet

```text
EMBEDDINGS

Text
 ↓
Vector

Code:

model.encode(text)

Model:

all-MiniLM-L6-v2

Output:

384 Dimensions

Used In:

✓ Semantic Search
✓ RAG
✓ Vector Databases
✓ Recommendation Systems

Key Idea:

Similar Meaning
↓
Similar Embeddings
```

---

# 🎯 Key Takeaways

✅ Embeddings convert text into vectors.

✅ Computers understand numbers better than text.

✅ Similar meanings create similar vectors.

✅ Embeddings are the foundation of Semantic Search.

✅ Embeddings are the foundation of RAG.

✅ Embeddings are one of the most important concepts in modern AI.
