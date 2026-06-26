# 08 - ChromaDB Metadata Filtering

## What is Metadata?

Metadata is "data about data".

Example:

Document:

```text
JDBC is used to connect Java to databases.
```

Metadata:

```python
{
    "topic": "database"
}
```

Document:

```text
Spring Boot is a framework.
```

Metadata:

```python
{
    "topic": "Spring"
}
```

---

## Why Metadata?

Without metadata:

```text
Question
↓
Search Entire Collection
```

With metadata:

```text
Question
↓
Filter Documents
↓
Search Smaller Collection
↓
Better Results
```

---

## Creating Documents With Metadata

```python
collection.add(
    documents=[
        "Java is a programming language.",
        "JDBC is used to connect Java to databases.",
        "Spring Boot is a framework."
    ],
    metadatas=[
        {"topic":"java"},
        {"topic":"database"},
        {"topic":"Spring"}
    ],
    ids=[
        "id1",
        "id2",
        "id3"
    ]
)
```

---

## Query Without Filter

```python
result = collection.query(
    query_texts=["What is Java?"],
    n_results=3
)
```

Searches all documents.

---

## Query With Filter

```python
result = collection.query(
    query_texts=["What is Java?"],
    n_results=3,
    where={
        "topic":"java"
    }
)
```

Only searches documents where:

```python
{
    "topic":"java"
}
```

---

## Common Mistake

Stored:

```python
{
    "topics":"java"
}
```

Queried:

```python
where={
    "topic":"java"
}
```

Result:

```text
No documents found
```

Reason:

```text
topics ≠ topic
```

Metadata key names must match exactly.

---

## Debugging Trick

Check stored metadata:

```python
print(collection.get())
```

Output:

```python
{
    'documents': [...],
    'metadatas': [...]
}
```

Verify metadata keys.

---

## Real World Example

Imagine:

```text
1000 Documents
```

Metadata:

```python
{
    "department":"HR"
}

{
    "department":"Finance"
}

{
    "department":"Engineering"
}
```

Query:

```python
where={
    "department":"Engineering"
}
```

Now ChromaDB searches only engineering documents.

---

## Metadata In RAG

Document
↓
Metadata
↓
Store In ChromaDB
↓
User Question
↓
Apply Filter
↓
Retrieve Relevant Chunks
↓
LLM Answer

---

## Interview Questions

### What is Metadata?

Metadata is additional information stored alongside a document that describes the document.

Example:

```python
{
    "topic":"java"
}
```

---

### Why Use Metadata Filtering?

Metadata filtering reduces the search space and improves retrieval accuracy.

---

### What Happens If Metadata Keys Don't Match?

Filtering fails because ChromaDB performs exact key matching.

Example:

```python
topic
```

is different from:

```python
topics
```

---

## Key Takeaways

✅ Metadata = Data about documents

✅ Used for filtering

✅ Improves retrieval quality

✅ Common in production RAG systems

✅ Metadata keys must match exactly

---

## Flowchart

Documents
↓
Metadata
↓
ChromaDB
↓
Metadata Filter
↓
Relevant Documents
↓
LLM
↓
Answer
