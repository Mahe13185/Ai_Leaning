# 📚 FAISS RAG NOTES

> Building a Retrieval-Augmented Generation (RAG) system using FAISS as the retrieval engine.

---

# 🎯 What is FAISS RAG?

FAISS RAG combines:

* Chunking
* Embeddings
* FAISS
* Top-K Retrieval
* Qwen

to answer questions using external knowledge.

---

# 🤔 Why Do We Need RAG?

LLMs have limitations:

* Hallucinations
* Limited knowledge
* Cannot access custom data

Example:

Question:

```text
What is JDBC?
```

Without RAG:

```text
LLM answers from memory
```

With RAG:

```text
Knowledge Base
    ↓
Retrieve Relevant Data
    ↓
Send To LLM
    ↓
Generate Answer
```

---

# 🔄 Architecture

knowledge.txt
↓
Chunking
↓
Embeddings
↓
FAISS
↓
Question
↓
Question Embedding
↓
Top-K Retrieval
↓
Context Building
↓
Prompt
↓
Qwen
↓
Answer

---

# 🏗 Step 1: Read Knowledge Base

```python
with open("knowledge.txt", "r") as file:
    knowledge = file.read()

sentences = knowledge.splitlines()
```

---

# 🏗 Step 2: Create Chunks

Chunk Size = 2

```python
chunks = []

for i in range(0, len(sentences), 2):
    chunk = sentences[i:i+2]
    chunks.append(
        " ".join(chunk)
    )
```

Example:

```text
Chunk 1:
Java is a programming language.
JDBC is used to connect Java to databases.

Chunk 2:
Spring Boot is a framework.
RAG stands for Retrieval Augmented Generation.
```

---

# 🏗 Step 3: Generate Chunk Embeddings

```python
chunk_embeddings = []

for chunk in chunks:
    chunk_embeddings.append(
        model.encode(chunk)
    )
```

---

# 🏗 Step 4: Create FAISS Index

```python
vectors = np.array(
    chunk_embeddings,
    dtype=np.float32
)

index = faiss.IndexFlatL2(384)

index.add(vectors)
```

---

# 🏗 Step 5: User Question

```python
question = input("Question: ")
```

---

# 🏗 Step 6: Question Embedding

```python
question_embedding = model.encode(question)

query_vector = np.array(
    [question_embedding],
    dtype=np.float32
)
```

---

# 🏗 Step 7: Retrieve Top-K Chunks

```python
D, I = index.search(
    query_vector,
    3
)
```

Example:

```python
I = [[0,2,1]]
```

Meaning:

```text
Best Match → Chunk 0

Second → Chunk 2

Third → Chunk 1
```

---

# 🏗 Step 8: Build Context

```python
context = ""

for index_value in I[0]:
    context += chunks[index_value] + "\n"
```

Example:

```text
JDBC is used to connect Java to databases.

Java is a programming language.

Spring Boot is a framework.
```

---

# 🏗 Step 9: Create Prompt

```python
prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""
```

---

# 🏗 Step 10: Send To Qwen

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

# 🏗 Step 11: Generate Answer

```python
print(
    ai_response["response"]
)
```

---

# 🔥 Difference Between Semantic Search & RAG

## Semantic Search

```text
Question
    ↓
FAISS
    ↓
Top Chunks
```

Output:

```text
Retrieved Chunks
```

---

## RAG

```text
Question
    ↓
FAISS
    ↓
Top Chunks
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

# 🧠 Grounded Generation

Good Prompt:

```text
Answer ONLY using the provided context.
```

Benefits:

✅ Reduces Hallucinations

✅ More Reliable Answers

✅ Better RAG Systems

---

# 🎤 Interview Questions

## What is RAG?

RAG (Retrieval Augmented Generation) combines retrieval and generation to answer questions using external knowledge.

---

## What is the role of FAISS?

FAISS acts as the retrieval engine and returns the most relevant chunks.

---

## What is Context Building?

Combining retrieved chunks into a single text block before sending it to the LLM.

---

## Why use Top-K Retrieval?

To provide more context to the LLM and improve answer quality.

---

# 🎯 Key Takeaways

✅ Chunking

✅ Embeddings

✅ FAISS Retrieval

✅ Top-K Search

✅ Context Building

✅ Qwen Integration

✅ Grounded Generation

---

# 🚀 Next Topic

FAISS Source-Aware RAG
