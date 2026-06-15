# Basic RAG (Retrieval Augmented Generation)

> Folder: `03-RAG/01-Basic-RAG`

---

# 📌 Overview

RAG stands for:

Retrieval Augmented Generation

It combines:

1. Retrieval System
2. Large Language Model

Instead of relying only on model knowledge, we first retrieve relevant information and then provide it to the LLM.

---

# 🤔 Problem

Normal LLM:

Question
 ↓
LLM
 ↓
Answer

Problem:

- Hallucinations
- Limited Knowledge
- No Access To Private Data

Example:

Question:

What is JDBC?

If model doesn't know:

Wrong Answer ❌

---

# 💡 Solution

Retrieve Information First

Question
    ↓
Retriever
    ↓
Relevant Context
    ↓
LLM
    ↓
Answer

Now the answer is based on actual data.

---

# What Does RAG Mean?

Retrieval
=
Find Relevant Information

Augmented
=
Add Retrieved Information

Generation
=
Generate Final Response

---

# Architecture

+----------------+
| User Question  |
+----------------+
         |
         v
+----------------+
| Retrieval      |
+----------------+
         |
         v
+----------------+
| Context        |
+----------------+
         |
         v
+----------------+
| LLM            |
+----------------+
         |
         v
+----------------+
| Final Answer   |
+----------------+

---

# Workflow

Knowledge Base
      ↓
Embeddings
      ↓
User Question
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Best Context
      ↓
Prompt Building
      ↓
LLM
      ↓
Answer

---

# Prompt Engineering

Instead of:

question

We send:

Context:
JDBC is used to connect Java to databases.

Question:
What is JDBC?

Answer:

---

# Why This Works

LLM now sees:

Relevant Context

before generating.

This reduces hallucinations.

---

# Code Flow

Step 1

Retrieve Best Match

```python
best_sentence
```

Step 2

Build Prompt

```python
prompt = f"""
Context:
{best_sentence}

Question:
{question}

Answer:
"""
```

Step 3

Send To LLM

```python
ollama.generate(...)
```

---

# Example

Knowledge:

JDBC is used to connect Java to databases.

Question:

What is JDBC?

Prompt Sent To Model:

Context:
JDBC is used to connect Java to databases.

Question:
What is JDBC?

Answer:

Result:

JDBC is a technology used to connect Java applications to databases.

---

# Real World Usage

✓ ChatGPT Enterprise

✓ PDF Chatbots

✓ Research Assistants

✓ Internal Company Search

✓ Customer Support Bots

---

# Common Mistakes

Mistake 1

Sending Question Only

Wrong:

Question → LLM

Correct:

Context + Question → LLM

---

Mistake 2

Bad Retrieval

Garbage Context

↓

Garbage Answer

---

# Interview Questions

Q. What is RAG?

Retrieval Augmented Generation is a technique that combines information retrieval with LLM generation.

---

Q. Why is RAG important?

It reduces hallucinations and allows models to answer from external knowledge.

---

Q. What are the two major components?

1. Retriever
2. Generator (LLM)

---

# Revision Cheat Sheet

User Question
      ↓
Retriever
      ↓
Context
      ↓
Prompt
      ↓
LLM
      ↓
Answer

RAG =
Retrieval
+
Generation

Benefits:

✓ Less Hallucination
✓ More Accurate
✓ Private Knowledge
✓ Dynamic Information

---

# Key Takeaways

✅ RAG combines retrieval and generation

✅ Retrieved context improves answer quality

✅ Reduces hallucinations

✅ Foundation of modern AI assistants
