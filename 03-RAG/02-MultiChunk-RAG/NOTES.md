# 📚 Multi-Chunk RAG NOTES

> Retrieving multiple chunks and sending them to the LLM for better answers.

---

# 🎯 What is Multi-Chunk RAG?

Multi-Chunk RAG is an improvement over Basic RAG.

Instead of retrieving only one chunk, we retrieve multiple relevant chunks and provide them to the LLM.

---

# 🤔 Why Not Basic RAG?

## Basic RAG

```text
Question
    ↓
Retrieve Best Chunk
    ↓
LLM
    ↓
Answer
```

Example:

```text
Question:
What is JDBC?

Retrieved Chunk:
JDBC is used to connect Java to databases.
```

Works well but only uses one source.

---

## Multi-Chunk RAG

```text
Question
    ↓
Top-K Retrieval
    ↓
Top Chunks
    ↓
Combine Context
    ↓
LLM
    ↓
Answer
```

Example:

```text
Chunk 1:
JDBC is used to connect Java to databases.

Chunk 2:
JDBC drivers allow Java to communicate with MySQL.

Chunk 3:
Java is a programming language.
```

All chunks are sent to the LLM.

---

# 🧠 Why Multi-Chunk RAG?

Benefits:

* More context
* Better answers
* Less hallucination
* Higher accuracy
* Production-ready retrieval

---

# 🔄 Workflow

knowledge.txt
↓
Split Into Sentences
↓
Create Chunks
↓
Generate Chunk Embeddings
↓
Question Embedding
↓
Top-K Retrieval
↓
Build Context
↓
Send To LLM
↓
Generate Answer

---

# 🏗 Step 1: Create Chunks

Example:

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

Chunk Size = 2

```python
chunks = []

for i in range(0, len(sentences), 2):
    chunk = sentences[i:i+2]
    chunks.append(" ".join(chunk))
```

Output:

```text
[
 "Java JDBC",
 "Spring MySQL",
 "Docker Kubernetes"
]
```

---

# 🏗 Step 2: Generate Chunk Embeddings

```python
chunkEmbeddings = []

for chunk in chunks:
    chunkEmbeddings.append(
        model.encode(chunk)
    )
```

Each chunk becomes a vector.

---

# 🏗 Step 3: Question Embedding

```python
questionEmbedding = model.encode(question)
```

Example:

```text
"What is JDBC?"
       ↓
Question Vector
```

---

# 🏗 Step 4: Top-K Retrieval

```python
scores = []

for i in range(len(chunkEmbeddings)):
    score = cos_sim(
        questionEmbedding,
        chunkEmbeddings[i]
    ).item()

    scores.append(
        (score, chunks[i])
    )
```

---

# 🏗 Step 5: Sort Results

```python
scores = sorted(
    scores,
    reverse=True
)
```

Example:

```python
[
 (0.84, chunk1),
 (0.66, chunk2),
 (0.52, chunk3)
]
```

---

# 🏗 Step 6: Get Top 3 Chunks

```python
top3 = scores[:3]
```

Output:

```python
[
 (0.84, chunk1),
 (0.66, chunk2),
 (0.52, chunk3)
]
```

---

# 🏗 Step 7: Build Context

```python
context = ""

for score, chunk in top3:
    context += chunk + "\n"
```

Output:

```text
Chunk A
Chunk B
Chunk C
```

---

# 🏗 Step 8: Create Prompt

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

# 🏗 Step 9: Send To Qwen

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

# 🏗 Step 10: Print Answer

```python
print(
    aiResponse["response"]
)
```

---

# 🔥 Architecture

Question
↓
Embedding
↓
Top-K Retrieval
↓
Top Chunks
↓
Context Building
↓
Prompt
↓
Qwen
↓
Answer

---

# 🎤 Interview Questions

## What is Multi-Chunk RAG?

Multi-Chunk RAG retrieves multiple relevant chunks using Top-K retrieval and provides them to the LLM as context.

---

## Why is Multi-Chunk RAG better than Basic RAG?

Basic RAG retrieves only one chunk.

Multi-Chunk RAG retrieves multiple chunks, providing richer context and improving answer quality.

---

## What is Context Building?

Context building is the process of combining retrieved chunks into a single text block before sending it to the LLM.

---

## Why do we use Top-K Retrieval?

Top-K retrieval returns multiple relevant chunks rather than only the highest-scoring chunk.

---

## What happens after retrieval?

Retrieved chunks are combined into context and inserted into the prompt sent to the LLM.

---

# 🎯 Key Takeaways

✅ Multiple Chunks Retrieved

✅ Top-K Retrieval Used

✅ Context Building

✅ Better LLM Answers

✅ Reduced Hallucination

✅ Foundation For Production RAG

---

# 🚀 Next Topic

```text
03-RAG
└── 03-Source-Aware-RAG
```

Goal:

```text
Answer
   +
Sources
```
