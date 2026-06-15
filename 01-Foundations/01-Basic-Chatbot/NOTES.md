# Basic Chatbot

## Simple Explanation

A chatbot takes user input, sends it to an AI model, and returns the response.

---

## Professional Explanation

A chatbot is an application that interacts with users using a Large Language Model (LLM). User prompts are sent to the model through an API, and the generated response is displayed back to the user.

---

## Concepts Learned

- Ollama
- Local LLMs
- API Calls
- JSON
- Python Requests

---

## Important Syntax

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

## Interview Question

Q: Why use Ollama?

Simple:
To run AI models locally.

Professional:
Ollama provides a simple interface for running open-source LLMs locally, reducing dependency on paid cloud APIs.

---

## Key Takeaway

Question → LLM → Response