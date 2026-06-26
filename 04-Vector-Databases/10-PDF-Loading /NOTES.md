# 10 - PDF Loading

---

# Introduction

Most RAG systems do not work with:

```text
knowledge.txt
```

They work with:

```text
PDF Files
Research Papers
Books
Resumes
Documentation
Reports
Contracts
```

Therefore the first step of any real-world RAG application is:

```text
PDF
↓
Extract Text
```

Before creating embeddings or storing data in a vector database.

---

# Learning Objectives

By the end of this module you should understand:

✅ Reading PDFs

✅ Accessing PDF pages

✅ Extracting text

✅ Cleaning extracted text

✅ Preparing text for chunking

---

# Why PDF Loading?

Without PDF Loading:

```text
User
↓
Manual Text Input
↓
RAG
```

Not practical.

---

With PDF Loading:

```text
User
↓
Upload PDF
↓
Extract Text
↓
RAG
```

Used in:

* ChatPDF
* PrivateGPT
* Document Assistants
* Enterprise Knowledge Bases

---

# Module Structure

```text
10-PDF-Loading

├── 01-read_pdf.py
├── 02-extract_text.py
├── 03-pdf_chunking.py
└── NOTES.md
```

---

# Concept 1: Reading PDFs

Library Used:

```python
from pypdf import PdfReader
```

Install:

```bash
pip install pypdf
```

---

# Creating a PDF Reader

```python
from pypdf import PdfReader

reader = PdfReader(
    "sample.pdf"
)
```

---

# Accessing Pages

```python
reader.pages
```

Returns:

```python
[
 Page1,
 Page2,
 Page3,
 Page4
]
```

---

# Getting Number Of Pages

```python
print(
    len(reader.pages)
)
```

Example:

```text
4
```

if the PDF contains four pages.

---

# Flowchart

PDF
↓
PdfReader
↓
reader.pages
↓
Number Of Pages

---

# Concept 2: Extracting Text

Each page can contain text.

Use:

```python
page.extract_text()
```

---

# Example

```python
for page in reader.pages:
    print(
        page.extract_text()
    )
```

Output:

```text
Java is a programming language.
JDBC is used to connect databases.
```

---

# What Does extract_text() Return?

Datatype:

```python
str
```

Example:

```python
text = page.extract_text()

print(type(text))
```

Output:

```python
<class 'str'>
```

---

# Flowchart

PDF
↓
Page
↓
extract_text()
↓
String

---

# Concept 3: Combining Multiple Pages

A PDF usually contains multiple pages.

Example:

```python
text = ""

for page in reader.pages:
    text += page.extract_text()
```

Result:

```text
One Large Text
```

containing all pages.

---

# Better Version

Add a space:

```python
text += page.extract_text() + " "
```

Why?

Without a space:

```text
JavaSpring
```

can occur between pages.

With a space:

```text
Java Spring
```

Text remains readable.

---

# Concept 4: Cleaning Extracted Text

PDFs often contain:

```text
Extra Spaces
Line Breaks
Formatting Issues
```

Example:

```text
Java

is

good
```

---

# Cleaning New Lines

```python
text = text.replace(
    "\n",
    " "
)
```

Output:

```text
Java is good
```

---

# Why Cleaning Is Important

Raw PDF:

```text
Java

supports

OOP
```

Cleaned:

```text
Java supports OOP
```

Better for:

```text
Chunking
Embeddings
Retrieval
```

---

# Common Problems In PDF Extraction

## Problem 1

Tables become messy.

Example:

```text
Name   Age
John   20
```

might become:

```text
Name Age John 20
```

---

## Problem 2

Code formatting may be lost.

Example:

```java
for(int i=0;i<5;i++)
```

can become:

```text
for(int i=0;i<5;i++)
```

without indentation.

---

## Problem 3

Extra Spaces

Example:

```text
Java  is  a  programming  language
```

This is normal in PDF extraction.

---

# Real World Pipeline

PDF
↓
Read PDF
↓
Extract Text
↓
Clean Text
↓
Chunking
↓
Embeddings
↓
Vector Database
↓
RAG

---

# Interview Questions

## What Is PdfReader?

PdfReader is a class from the pypdf library used to load and read PDF documents.

---

## What Does reader.pages Return?

A collection of pages inside the PDF.

---

## How Do You Count Pages?

```python
len(reader.pages)
```

---

## What Does extract_text() Return?

A string containing text from the page.

---

## Why Clean Extracted Text?

To remove formatting issues such as:

* New lines
* Extra spaces
* PDF artifacts

before chunking and embedding generation.

---

## Why Add A Space Between Pages?

Without a space:

```text
JavaSpring
```

can occur.

Adding:

```python
+ " "
```

keeps words separated.

---

# Real World Usage

Used in:

✅ ChatPDF

✅ PrivateGPT

✅ Enterprise Knowledge Bases

✅ Resume Chatbots

✅ Research Paper Assistants

✅ Legal Document Search Systems

---

# Common Mistakes

❌ Forgetting to install pypdf

❌ Using extract_text() on the entire PDF instead of pages

❌ Forgetting to clean text

❌ Forgetting to add spaces between pages

❌ Assuming PDFs store text like TXT files

---

# Key Takeaways

✅ PDFs are the primary source of data in modern RAG systems

✅ PdfReader loads PDF files

✅ extract_text() converts pages into strings

✅ Cleaning improves chunk quality

✅ PDF Loading happens before chunking

---

# Folder Summary

01-read_pdf.py

Learned:

* PdfReader
* reader.pages
* len(reader.pages)

---

02-extract_text.py

Learned:

* extract_text()
* Combining pages
* Cleaning text

---

03-pdf_chunking.py

Learned:

* Word splitting
* Chunk creation
* Preparing text for embeddings

---

# Final Flowchart

PDF
↓
PdfReader
↓
Extract Text
↓
Clean Text
↓
Chunking
↓
Embeddings
↓
Vector Database
↓
Retrieval
↓
LLM
↓
Answer
