# 📚 FAISS NOTES

> First Vector Database Implementation using FAISS

---

# 🎯 What is FAISS?

FAISS (Facebook AI Similarity Search) is a library developed by Meta for efficient similarity search and retrieval of vector embeddings.

It is commonly used in:

* RAG Systems
* Semantic Search
* Recommendation Systems
* Vector Databases
* AI Agents

---

# 🤔 Why Do We Need FAISS?

## Traditional Search

```python
for embedding in embeddings:
    score = cos_sim(queryEmbedding, embedding)
```

Workflow:

Question
↓
Compare with Vector 1
↓
Compare with Vector 2
↓
Compare with Vector 3
↓
...
↓
Find Best Match

Problems:

* Slow for large datasets
* Not scalable
* Millions of comparisons required

---

## FAISS Search

Question
↓
FAISS Index
↓
Top-K Results

Benefits:

* Fast
* Optimized
* Scalable
* Production Ready

---

# 🧠 Core Idea

FAISS does NOT store text.

FAISS stores:

```text
Vectors (Embeddings)
```

Example:

Text:

```text
JDBC is used to connect Java to databases.
```

Embedding:

```text
[0.12, -0.44, 0.91, ...]
```

FAISS stores:

```text
[0.12, -0.44, 0.91, ...]
```

NOT:

```text
JDBC is used to connect Java to databases.
```

---

# 🔄 FAISS Workflow

Sentence
↓
Embedding Model
↓
Vector
↓
FAISS Index

Question
↓
Embedding Model
↓
Question Vector
↓
FAISS Search
↓
Best Vector Index
↓
Original Text

---

# 🏗 Step 1: Generate Embeddings

```python
embeddings = []

for sentence in sentences:
    embeddings.append(
        model.encode(sentence)
    )
```

Output:

```text
[
 vector1,
 vector2,
 vector3
]
```

---

# 🏗 Step 2: Convert To NumPy Array

```python
vectors = np.array(
    embeddings,
    dtype=np.float32
)
```

Why?

FAISS expects:

```text
numpy.ndarray
```

and

```text
float32
```

---

# 🏗 Step 3: Create FAISS Index

```python
index = faiss.IndexFlatL2(384)
```

Meaning:

```text
Create Empty Vector Database
```

---

## Why 384?

Model Used:

```python
all-MiniLM-L6-v2
```

Output:

```text
384-dimensional embeddings
```

Therefore:

```python
faiss.IndexFlatL2(384)
```

---

# 🏗 Step 4: Add Vectors

```python
index.add(vectors)
```

Meaning:

```text
Store vectors inside FAISS
```

Example:

Index 0 → Vector 1

Index 1 → Vector 2

Index 2 → Vector 3

---

# 🏗 Step 5: Total Vectors

```python
print(index.ntotal)
```

Output:

```text
3
```

Meaning:

```text
Total vectors stored = 3
```

---

# 🏗 Step 6: Create Query Vector

```python
questionEmbedding = model.encode(question)

queryVector = np.array(
    [questionEmbedding],
    dtype=np.float32
)
```

Why [] ?

Without:

```text
(384,)
```

With:

```text
(1,384)
```

FAISS requires:

```text
(Number_of_Vectors, Dimensions)
```

---

# 🏗 Step 7: Search

```python
D, I = index.search(
    queryVector,
    1
)
```

Meaning:

```text
Search Query
Return Top 1 Result
```

---

# 🧠 Understanding D and I

## D = Distances

Example:

```python
D = [[0.24]]
```

Meaning:

```text
Distance between query vector
and retrieved vector
```

Rule:

```text
Smaller Distance = Better Match
```

---

## I = Indexes

Example:

```python
I = [[1]]
```

Meaning:

```text
Best Match Found At Index 1
```

---

# 🤔 Why I[0][0] ?

FAISS returns:

```python
I = [[1]]
```

Step 1:

```python
I[0]
```

Output:

```python
[1]
```

Step 2:

```python
I[0][0]
```

Output:

```python
1
```

Now:

```python
sentences[I[0][0]]
```

becomes:

```python
sentences[1]
```

Output:

```text
JDBC is used to connect Java to databases.
```

---

# 🔥 Top-K Retrieval

Top 1:

```python
D, I = index.search(
    queryVector,
    1
)
```

Top 3:

```python
D, I = index.search(
    queryVector,
    3
)
```

Example:

```python
I = [[1,0,2]]
```

Meaning:

Rank 1 → Index 1

Rank 2 → Index 0

Rank 3 → Index 2

---

# 🔄 Print Top K Results

```python
for index in I[0]:
    print(sentences[index])
```

Output:

```text
JDBC is used to connect Java to databases.

Java is a programming language.

Spring Boot is a framework.
```

---

# 🎤 Interview Questions

## What is FAISS?

FAISS is a vector similarity search library developed by Meta that enables efficient retrieval of high-dimensional embeddings.

---

## Why use FAISS?

FAISS provides fast similarity search and scales efficiently to millions of vectors, unlike brute-force comparison.

---

## What does index.add() do?

It stores vector embeddings inside the FAISS index for future retrieval.

---

## What does index.search() return?

```text
D → Distances

I → Indexes
```

---

## Why do we use Top-K Retrieval?

Top-K retrieval returns multiple relevant results, providing richer context for RAG systems.

---

## Does FAISS store text?

No.

FAISS stores vector embeddings.

Original text is stored separately and retrieved using returned indexes.

---

# 🎯 Key Takeaways

✅ FAISS stores vectors

✅ FAISS performs similarity search

✅ D = Distance

✅ I = Index

✅ Smaller Distance = Better Match

✅ Top-K Retrieval supported

✅ Used in RAG Systems

✅ Used in Production AI Applications

---

# 🚀 Next Topic

```text
04-Vector-Databases
└── 02-FAISS-Semantic-Search
```

Goal:

```text
knowledge.txt
      ↓
Embeddings
      ↓
FAISS
      ↓
Top-K Retrieval
      ↓
Best Matching Sentences
```
