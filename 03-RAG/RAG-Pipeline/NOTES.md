# Retrieval Augmented Generation (RAG)

## Simple Explanation

Find information first, then ask AI to answer.

---

## Professional Explanation

RAG combines retrieval and generation by fetching relevant context from a knowledge source and supplying it to an LLM before generating a response.

---

## Architecture

Question
↓
Embedding Search
↓
Retrieve Context
↓
LLM
↓
Answer

---

## Concepts Learned

- Retrieval
- Context Injection
- Semantic Search
- RAG

---

## Important Syntax

```python
prompt = f"""
Use this context:

{best_sentence}

Answer:

{question}
"""
```

---

## Interview Question

Q: What is RAG?

Simple:
AI searches information before answering.

Professional:
Retrieval Augmented Generation is a technique where relevant information is retrieved from an external knowledge source and supplied to a language model to improve response quality and accuracy.

---

## Interview Question

Q: Difference between Chatbot and RAG?

Simple:
Chatbot uses model knowledge. RAG uses external knowledge.

Professional:
A traditional chatbot relies solely on the model's pre-trained knowledge, whereas a RAG system dynamically retrieves external information and incorporates it into the generation process.

---

## Key Takeaway

Retrieval + Generation = RAG