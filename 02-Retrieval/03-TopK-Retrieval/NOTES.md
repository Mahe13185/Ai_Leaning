# Top-K Retrieval

> Folder: `02-Retrieval/03-TopK-Retrieval`

---

# 📌 Overview

In Semantic Search, we retrieve only the single best result.

However, real-world AI systems rarely rely on a single result.

Instead, they retrieve multiple relevant results and use them together.

This technique is called **Top-K Retrieval**.

Where:

* K = Number of results to retrieve
* Top-1 = Best result
* Top-3 = Best 3 results
* Top-5 = Best 5 results

---

# 🤔 Problem Statement

Suppose we have the following knowledge:

```text
Java is a programming language.

JDBC is used to connect Java to databases.

JDBC drivers allow Java to communicate with MySQL.

Spring Boot is a framework.
```

User asks:

```text
What is JDBC?
```

Semantic Search may return:

```text
JDBC is used to connect Java to databases.
```

This is correct.

But we lose useful information:

```text
JDBC drivers allow Java to communicate with MySQL.
```

Returning only one result may remove important context.

---

# 💡 Solution

Instead of retrieving:

```text
Top 1 Result
```

Retrieve:

```text
Top 3 Results
```

Example:

```text
1. JDBC is used to connect Java to databases.

2. JDBC drivers allow Java to communicate with MySQL.

3. Java is a programming language.
```

Now the AI has more information.

---

# 🌍 Real World Example

## Google Search

When you search:

```text
Python Tutorial
```

Google doesn't return:

```text
Only One Website
```

It returns:

```text
Top Results
```

because multiple pages may be useful.

---

## ChatGPT RAG

Question:

```text
What is JDBC?
```

Retriever may return:

```text
Chunk 1
Chunk 2
Chunk 3
```

The LLM reads all retrieved chunks before answering.

This is Top-K Retrieval.

---

# 🏗 Architecture

```text
+----------------+
| User Question  |
+----------------+
         |
         v
+----------------+
| Embedding      |
+----------------+
         |
         v
+----------------+
| Similarity     |
| Calculation    |
+----------------+
         |
         v
+----------------+
| Store Scores   |
+----------------+
         |
         v
+----------------+
| Sort Scores    |
+----------------+
         |
         v
+----------------+
| Top K Results  |
+----------------+
```

---

# 🔄 Workflow

```text
Question
    ↓
Question Embedding
    ↓
Compare With Knowledge
    ↓
Generate Scores
    ↓
Store Scores
    ↓
Sort Scores
    ↓
Take Top K
    ↓
Return Results
```

---

# 🧠 Core Concept

Instead of storing only:

```python
best_score
best_sentence
```

Store every score:

```python
[
    (0.84, "JDBC"),
    (0.66, "MySQL"),
    (0.52, "Java")
]
```

Then sort them.

---

# 📚 Why Tuples?

Tuple Structure:

```python
(score, sentence)
```

Example:

```python
(0.84, "JDBC")
```

Meaning:

```text
Score    → 0.84
Sentence → JDBC
```

The score and sentence stay connected.

---

# ⚙ Syntax Breakdown

## Step 1: Create Empty List

```python
scores = []
```

Purpose:

Store all similarity scores.

---

## Step 2: Add Score

```python
scores.append(
    (score, sentence)
)
```

Example:

```python
scores.append(
    (0.84, "JDBC")
)
```

Result:

```python
[
    (0.84, "JDBC")
]
```

---

## Step 3: Sort Scores

```python
scores = sorted(
    scores,
    reverse=True
)
```

Purpose:

Sort scores from highest to lowest.

---

### Without reverse=True

```python
0.12
0.31
0.84
```

Lowest first ❌

---

### With reverse=True

```python
0.84
0.31
0.12
```

Highest first ✅

---

# ✂ Slicing

Suppose:

```python
scores = [
    (0.84, "JDBC"),
    (0.66, "MySQL"),
    (0.52, "Java"),
    (0.21, "Spring")
]
```

Take Top 3:

```python
top3 = scores[:3]
```

Output:

```python
[
    (0.84, "JDBC"),
    (0.66, "MySQL"),
    (0.52, "Java")
]
```

---

# 💻 Complete Code

```python
scores = []

for sentence in knowledge:

    sentenceEmbedding = model.encode(
        sentence
    )

    score = cos_sim(
        questionEmbedding,
        sentenceEmbedding
    ).item()

    scores.append(
        (score, sentence)
    )

scores = sorted(
    scores,
    reverse=True
)

top3 = scores[:3]

print(top3)
```

---

# 📤 Example Output

Question:

```text
What is JDBC?
```

Output:

```python
[
 (0.84,
  "JDBC is used to connect Java to databases."),

 (0.66,
  "JDBC drivers allow Java to communicate with MySQL."),

 (0.52,
  "Java is a programming language.")
]
```

---

# 🎯 Why Top-K Retrieval Matters

Without Top-K:

```text
Only One Context
```

With Top-K:

```text
Multiple Relevant Contexts
```

This improves:

* Answer Quality
* Context Understanding
* RAG Performance
* Retrieval Accuracy

---

# ❌ Common Mistakes

## Mistake 1

Using only:

```python
best_score
```

This keeps only one result.

---

## Mistake 2

Forgetting:

```python
reverse=True
```

Results become sorted from lowest score to highest score.

---

## Mistake 3

Wrong slicing

Wrong:

```python
scores[3:]
```

Correct:

```python
scores[:3]
```

---

# 🎤 Interview Questions

## What is Top-K Retrieval?

Top-K Retrieval returns the K highest-scoring results instead of a single result.

---

## What does K represent?

K represents the number of results retrieved.

Examples:

```text
Top-3
Top-5
Top-10
```

---

## Why is Top-K Retrieval important?

Multiple relevant results provide more context and improve answer quality.

---

## What data structure did we use?

A list of tuples.

Example:

```python
(score, sentence)
```

---

## Why is Top-K Retrieval used in RAG?

RAG systems retrieve multiple relevant chunks before sending them to the LLM.

This improves response quality.

---

# 📝 Revision Cheat Sheet

```text
TOP-K RETRIEVAL

Question
    ↓
Similarity Scores
    ↓
Store Scores
    ↓
Sort Scores
    ↓
Top K Results

Important Syntax:

scores.append(
    (score, sentence)
)

scores = sorted(
    scores,
    reverse=True
)

top3 = scores[:3]

Used In:

✓ RAG
✓ Google Search
✓ Recommendation Systems
✓ Document Retrieval

One Result ❌

Multiple Relevant Results ✅
```

---

# 🎯 Key Takeaways

✅ Top-K Retrieval returns multiple relevant results.

✅ We use tuples to store score and sentence together.

✅ Sorting helps find the most relevant results.

✅ Slicing extracts the top K results.

✅ Top-K Retrieval provides better context.

✅ Top-K Retrieval is a core component of modern RAG systems.

✅ Most production AI systems use Top-K Retrieval before generating answers.
