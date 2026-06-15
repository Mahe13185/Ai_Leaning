# Semantic Search

## Simple Explanation

Search by meaning, not exact words.

---

## Professional Explanation

Semantic search retrieves information based on contextual meaning using vector embeddings and similarity calculations rather than exact keyword matching.

---

## Concepts Learned

- Semantic Search
- Cosine Similarity
- Vector Search

---

## Important Syntax

```python
score = cos_sim(
    questionEmbedding,
    sentenceEmbedding
).item()
```

---

## Interview Question

Q: Why is semantic search better than keyword search?

Simple:
It understands meaning.

Professional:
Semantic search retrieves relevant information even when the query and stored text use different wording but share similar meaning.

---

## Key Takeaway

Meaning > Keywords