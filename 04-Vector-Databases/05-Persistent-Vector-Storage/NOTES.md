# 📚 Persistent Vector Storage NOTES

> Learn how to save and load FAISS indexes so embeddings do not need to be regenerated every time the application runs.

---

# 🎯 What is Persistent Vector Storage?

Persistent Vector Storage means saving vector embeddings and FAISS indexes to disk so they can be reused later.

Instead of rebuilding the index every time:

```text
knowledge.txt
      ↓
Embeddings
      ↓
FAISS
      ↓
Search
```

we save the index:

```text
knowledge.txt
      ↓
Embeddings
      ↓
FAISS
      ↓
Save Index
```

and later:

```text
Load Index
      ↓
Search
```

---

# 🤔 Why Do We Need Persistence?

Imagine:

```text
10 sentences
```

No problem.

But imagine:

```text
100,000 documents
```

Generating embeddings every run becomes expensive.

Without Persistence:

```text
Run Program
      ↓
Generate Embeddings
      ↓
Create Index
      ↓
Search
```

Every time.

---

With Persistence:

```text
Run Once
      ↓
Create Index
      ↓
Save Index

Future Runs
      ↓
Load Index
      ↓
Search
```

Much faster.

---

# 🔥 Core Idea

FAISS can save indexes to disk.

Save:

```python
faiss.write_index(
    index,
    "knowledge.index"
)
```

Load:

```python
index = faiss.read_index(
    "knowledge.index"
)
```

---

# 🏗 Project Structure

```text
05-Persistent-Vector-Storage

├── knowledge.txt
├── knowledge.index
├── create_index.py
├── search_index.py
└── NOTES.md
```

---

# 📂 knowledge.txt

Contains:

```text
Java is a programming language.

JDBC is used to connect Java to databases.

Spring Boot is a framework.
```

This is the original data source.

---

# 🏗 create_index.py

Purpose:

```text
knowledge.txt
      ↓
Embeddings
      ↓
FAISS
      ↓
knowledge.index
```

Runs once.

---

# Step 1: Read File

```python
with open("knowledge.txt", "r") as file:
    knowledge = file.read()

sentences = knowledge.splitlines()
```

---

# Step 2: Create Embeddings

```python
embeddings = []

for sentence in sentences:
    embeddings.append(
        model.encode(sentence)
    )
```

---

# Step 3: Convert To NumPy

```python
vectors = np.array(
    embeddings,
    dtype=np.float32
)
```

Example:

```text
(3,384)
```

Meaning:

```text
3 vectors

384 dimensions each
```

---

# Step 4: Create FAISS Index

```python
index = faiss.IndexFlatL2(384)
```

---

# Step 5: Add Vectors

```python
index.add(vectors)
```

---

# Step 6: Save Index

```python
faiss.write_index(
    index,
    "knowledge.index"
)
```

Creates:

```text
knowledge.index
```

---

# Step 7: Verify

```python
print(index.ntotal)
```

Example:

```text
3
```

Meaning:

```text
3 vectors stored in FAISS
```

---

# 🔍 search_index.py

Purpose:

```text
knowledge.index
      ↓
Load
      ↓
Question
      ↓
Search
      ↓
Results
```

Runs many times.

---

# Step 1: Load Index

```python
index = faiss.read_index(
    "knowledge.index"
)
```

No need to recreate the index.

---

# Step 2: Read Original Text

```python
with open("knowledge.txt", "r") as file:
    knowledge = file.read()

sentences = knowledge.splitlines()
```

---

# ❓ Why Read knowledge.txt Again?

FAISS stores:

```text
Vectors Only
```

It does NOT store:

```text
Original Text
```

Example:

FAISS knows:

```text
Vector 0
Vector 1
Vector 2
```

But does not know:

```text
Java

JDBC

Spring
```

Therefore we reload the original text.

---

# Step 3: Ask Question

```python
question = input(
    "Question: "
)
```

---

# Step 4: Create Query Embedding

```python
questionEmbedding = model.encode(
    question
)

questionVector = np.array(
    [questionEmbedding],
    dtype=np.float32
)
```

Shape:

```text
(1,384)
```

---

# Step 5: Search

```python
D, I = index.search(
    questionVector,
    3
)
```

Returns:

```python
D = [[0.31, 0.94, 1.43]]

I = [[1,0,2]]
```

---

# 🧠 Understanding I

```text
Indexes
```

Example:

```python
I = [[1,0,2]]
```

Meaning:

```text
Best Match → Sentence 1

Second Match → Sentence 0

Third Match → Sentence 2
```

---

# 🧠 Understanding D

```text
Distances
```

Example:

```python
D = [[0.31, 0.94, 1.43]]
```

Meaning:

```text
0.31 → Best Match

0.94 → Second Match

1.43 → Third Match
```

Rule:

```text
Smaller Distance = Better Match
```

---

# Step 6: Print Results

```python
for indexValue in I[0]:
    print(
        sentences[indexValue]
    )
```

Output:

```text
JDBC is used to connect Java to databases.

Java is a programming language.

Spring Boot is a framework.
```

---

# 🔥 Important Learning

FAISS stores:

```text
Vectors
```

knowledge.txt stores:

```text
Original Text
```

Both are needed.

---

# Architecture

```text
knowledge.txt
      ↓
create_index.py
      ↓
knowledge.index
      ↓
search_index.py
      ↓
Question
      ↓
Search
      ↓
Results
```

---

# 🎤 Interview Questions

## What is Persistent Vector Storage?

Saving vector indexes to disk so they can be reused later without regenerating embeddings.

---

## Which FAISS function saves an index?

```python
faiss.write_index()
```

---

## Which FAISS function loads an index?

```python
faiss.read_index()
```

---

## What does index.ntotal return?

Total number of vectors stored inside the index.

---

## Does FAISS store original text?

No.

FAISS only stores vectors.

Original text must be stored separately.

---

# 🎯 Key Takeaways

✅ Save FAISS Index

✅ Load FAISS Index

✅ Reuse Embeddings

✅ Faster Search

✅ Persistent Storage

✅ Vector Retrieval

✅ Separation of Vectors and Text

---

# 📈 Progress

```text
04-Vector-Databases

├── 01-FAISS                   ✅
├── 02-FAISS-Semantic-Search   ✅
├── 03-FAISS-RAG              ✅
├── 04-FAISS-Source-Aware-RAG ✅
└── 05-Persistent-Vector-Storage ✅
```

---

# 🚀 Next Topic

```text
04-Vector-Databases
└── 06-Persistent-FAISS-RAG
```

Goal:

```text
Load Saved Index
      ↓
Search
      ↓
Retrieve Context
      ↓
Qwen
      ↓
Answer
```
