# Conversational Memory

## Simple Explanation

The chatbot remembers previous messages and sends them back to the model.

---

## Professional Explanation

Conversation history is maintained and included in future prompts, allowing the model to generate context-aware responses.

---

## Concepts Learned

- Prompt History
- Context Window
- Stateful Conversations

---

## Important Syntax

```python
history.append(f"User: {prompt}")

full_prompt = "\n".join(history)
```

---

## Interview Question

Q: How did you implement memory?

Simple:
I stored old messages in a list.

Professional:
I maintained conversation history and included it in subsequent prompts to provide context to the language model.

---

## Key Takeaway

Current Prompt + History = Memory