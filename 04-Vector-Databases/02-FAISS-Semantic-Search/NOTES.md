# 📚 FAISS Semantic Search NOTES

> Using FAISS to perform fast semantic search on knowledge.txt

---

# 🎯 What is FAISS Semantic Search?

FAISS Semantic Search replaces manual cosine similarity calculations with a vector database.

Instead of:

Question
↓
Loop Through All Embeddings
↓
Cosine Similarity
↓
Sort
↓
Top Results

We use:

Question
↓
FAISS Search
↓
Top Results

---

# 🤔 Why Use FAISS?

Traditional Search:

```python
for embedding in embeddings:
    score = cos_sim(...)
```

Problems:

* Slow for large datasets
* Manual sorting required
* Not scalable

FAISS:

```python
D, I = index.search(queryVector, k)
```

Benefits:

* Fast
* Scalable
* Optimized for millions of vectors

---

# 🔄 Workflow

knowledge.txt
↓
Read File
↓
Split Into Sentences
↓
Generate Embeddings
↓
Create FAISS Index
↓
Store Vectors
↓
Question
↓
Question Embedding
↓
FAISS Search
↓
Top-K Results

---

# 🏗 Step 1: Read Knowledge Base

```python
with open("knowledge.txt", "r") as file:
    knowledge = file.read()

sentences = knowledge.splitlines()
```

---

# 🏗 Step 2: Generate Embeddings

```python
embeddings = []

for sentence in sentences:
    embeddings.append(
        model.encode(sentence)
    )
```

---

# 🏗 Step 3: Convert To NumPy

```python
vectors = np.array(
    embeddings,
    dtype=np.float32
)
```

Example Shape:

```text
(5,384)
```

Meaning:

```text
5 vectors
384 dimensions each
```

---

# 🏗 Step 4: Create FAISS Index

```python
index = faiss.IndexFlatL2(384)
```

---

# 🏗 Step 5: Add Vectors

```python
index.add(vectors)
```

Stores embeddings inside FAISS.

---

# 🏗 Step 6: Create Query Vector

```python
questionEmbedding = model.encode(question)

queryVector = np.array(
    [questionEmbedding],
    dtype=np.float32
)
```

Shape:

```text
(1,384)
```

---

# 🏗 Step 7: Search

```python
D, I = index.search(
    queryVector,
    3
)
```

Returns:

```python
D = [[0.2,0.5,1.1]]

I = [[1,0,2]]
```

---

# 🧠 Understanding D

```text
Distance
```

Smaller Distance = Better Match

Example:

```text
0.2 → Best

0.5 → Second

1.1 → Third
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
Best Match → Index 1

Second → Index 0

Third → Index 2
```

---

# 🔥 Print Results

```python
for indexValue in I[0]:
    print(sentences[indexValue])
```

---

# 🎤 Interview Questions

## What is FAISS Semantic Search?

Using FAISS to retrieve semantically similar text based on vector embeddings.

---

## Why is FAISS better than manual cosine similarity?

FAISS performs optimized similarity search and scales to large datasets.

---

## What does index.search() return?

```text
D → Distances

I → Indexes
```

---

# 🎯 Key Takeaways

✅ knowledge.txt

✅ Embeddings

✅ Vector Storage

✅ FAISS Search

✅ Top-K Retrieval

✅ Semantic Search

---

# 🚀 Next Topic

FAISS RAG
