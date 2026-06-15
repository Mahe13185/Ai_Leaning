# Basic Chatbot

> Folder: `01-Foundations/01-Basic-Chatbot`

---

# 📌 Overview

A chatbot is an application that accepts user input and generates a response using an AI model.

This is the first step in understanding how Large Language Models (LLMs) interact with applications.

In this project, we built a chatbot using:

* Python
* Ollama
* Qwen Model

---

# 🤔 Problem Statement

Normally:

```text
User
 ↓
Google Search
 ↓
Read Articles
```

This takes time.

We want:

```text
User
 ↓
AI Model
 ↓
Direct Answer
```

---

# 💡 Solution

Create a chatbot that:

1. Accepts user input
2. Sends prompt to AI model
3. Receives response
4. Displays answer

---

# 🌎 Real World Examples

* ChatGPT
* Gemini
* Claude
* Perplexity
* Copilot

All follow the same core architecture.

---

# 🏗 Architecture

```text
+---------+
|  User   |
+---------+
     |
     v
+---------+
| Python  |
+---------+
     |
     v
+---------+
| Ollama  |
+---------+
     |
     v
+---------+
|  Qwen   |
+---------+
     |
     v
+---------+
| Response|
+---------+
```

---

# 🔄 Workflow

```text
User Input
     ↓
Python Program
     ↓
HTTP Request
     ↓
Ollama Server
     ↓
Qwen Model
     ↓
Generated Response
     ↓
Display Output
```

---

# What Is Ollama?

Ollama allows us to run AI models locally.

Instead of:

```text
Python
 ↓
OpenAI API
 ↓
Internet
```

We use:

```text
Python
 ↓
Ollama
 ↓
Local Model
```

Benefits:

✅ Privacy

✅ No API Cost

✅ Offline Usage

---

# Core Code

## User Input

```python
prompt = input("You: ")
```

Purpose:

Accept user message.

---

## API Request

```python
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model":"qwen3:4b",
        "prompt":prompt,
        "stream":False
    }
)
```

---

## Response Extraction

```python
aiResponse = response.json()
```

Convert JSON into Python dictionary.

---

## Print Response

```python
print(
    "AI:",
    aiResponse["response"]
)
```

---

# Request Flow

```text
You: What is Java?

        ↓

{
 "model":"qwen3:4b",
 "prompt":"What is Java?"
}

        ↓

Qwen

        ↓

Java is a programming language.
```

---

# Common Mistakes

## Wrong Ollama URL

```python
http://localhost:11434
```

must be running.

---

## Wrong Model Name

```python
qwen3:4b
```

must exist locally.

---

## Forgetting JSON Response

Wrong:

```python
print(response)
```

Correct:

```python
response.json()
```

---

# Interview Questions

## What is a Chatbot?

A chatbot is a software application that interacts with users using natural language.

---

## What is Ollama?

Ollama is a local inference platform used to run Large Language Models on personal hardware.

---

## Why use local models?

* Privacy
* No API Cost
* Offline Usage

---

## What is a Prompt?

A prompt is the input given to an AI model.

---

# 📝 Revision Cheat Sheet

```text
BASIC CHATBOT

User
 ↓
Python
 ↓
Ollama
 ↓
Qwen
 ↓
Response

Key Function:

requests.post()

Used:

prompt
model
response

Purpose:

Build Local AI Chatbot
```

---

# 🎯 Key Takeaways

✅ Built first chatbot

✅ Learned Ollama

✅ Learned API Requests

✅ Learned Prompt → Response Flow

✅ Understood LLM Interaction
