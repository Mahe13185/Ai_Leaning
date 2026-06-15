# Conversational Memory

> Folder: `01-Foundations/02-Conversational-Memory`

---

# 📌 Overview

A basic chatbot forgets previous messages.

Conversational Memory allows a chatbot to remember previous interactions and maintain context.

This is one of the most important features in modern AI assistants.

---

# 🤔 Problem Statement

Without Memory:

```text
You: My name is Mahendra

AI: Nice to meet you.

You: What is my name?

AI: I don't know.
```

Why?

Because the model only sees the current prompt.

---

# 💡 Solution

Store previous conversation messages and send them with every new request.

---

# Without Memory

```text
Question
   ↓
Model
   ↓
Answer
```

No history.

---

# With Memory

```text
Question
   ↓
History
   ↓
Model
   ↓
Answer
```

The model now sees previous messages.

---

# 🌎 Real World Examples

Used in:

* ChatGPT
* Gemini
* Claude
* Character AI
* Customer Support Bots

---

# 🏗 Architecture

```text
+---------+
| User    |
+---------+
     |
     v
+---------+
| History |
+---------+
     |
     v
+---------+
| Prompt  |
+---------+
     |
     v
+---------+
| Model   |
+---------+
     |
     v
+---------+
| Answer  |
+---------+
```

---

# 🔄 Workflow

```text
User Message
      ↓
Store Message
      ↓
Build History
      ↓
Send To Model
      ↓
Receive Response
      ↓
Store Response
      ↓
Repeat
```

---

# Core Concept

We create a list:

```python
history = []
```

Purpose:

Store all messages.

---

# Saving User Message

```python
history.append(
    f"User: {prompt}"
)
```

Example:

```python
[
 "User: My name is Mahendra"
]
```

---

# Saving AI Response

```python
history.append(
    f"AI: {answer}"
)
```

Example:

```python
[
 "User: My name is Mahendra",
 "AI: Nice to meet you."
]
```

---

# Building Full Context

```python
full_prompt = "\n".join(
    history
)
```

---

# Example Output

```text
User: My name is Mahendra

AI: Nice to meet you.

User: What is my name?
```

This entire conversation is sent to the model.

---

# Visual Representation

```text
History

User: My name is Mahendra

AI: Nice to meet you.

User: What is my name?

        ↓

Model Sees Everything

        ↓

Answer:

Your name is Mahendra.
```

---

# Why Join?

History is stored as:

```python
[
 "Message 1",
 "Message 2",
 "Message 3"
]
```

AI expects text.

So:

```python
"\n".join(history)
```

becomes:

```text
Message 1

Message 2

Message 3
```

---

# Common Mistakes

## Forgetting To Store Messages

Wrong:

```python
prompt
```

Only current message.

---

Correct:

```python
history.append(...)
```

---

## Forgetting AI Responses

Store both:

```python
User
AI
```

---

## Sending Only Current Prompt

Wrong:

```python
prompt
```

Correct:

```python
full_prompt
```

---

# Memory Limitation

Current Memory:

```text
Stored In RAM
```

When program closes:

```text
Memory Lost
```

Future Solution:

```text
File Storage
Database
Vector Database
```

---

# Interview Questions

## What is Conversational Memory?

Conversational Memory is the ability of a chatbot to remember previous interactions.

---

## Why is Memory Important?

It helps maintain context across multiple messages.

---

## Does an LLM Remember Automatically?

No.

The previous conversation must be provided as context.

---

## How Did We Implement Memory?

Using a Python list to store conversation history.

---

# 📝 Revision Cheat Sheet

```text
CONVERSATIONAL MEMORY

Problem:

AI Forgets

Solution:

Store History

Workflow:

User Message
 ↓
Save Message
 ↓
Build Context
 ↓
Send To Model
 ↓
Save Response

Key Functions:

history.append()

"\n".join(history)

Purpose:

Remember Previous Messages
```

---

# 🎯 Key Takeaways

✅ Chatbots forget by default

✅ Memory requires storing history

✅ History is sent back to the model

✅ Context improves responses

✅ Foundation for advanced AI assistants

✅ First step toward persistent memory systems
