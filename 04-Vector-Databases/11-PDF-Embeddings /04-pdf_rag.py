import chromadb
import requests

client = chromadb.PersistentClient(
    path="chroma-db"
)

collection = client.get_collection(
    name="Java_Notes"
)
question = input("Question: ")
result = collection.query(
    query_texts=[question],
    n_results=3
)

context = ""
for doc in  result["documents"][0]:
   context += doc + "\n"

print("=" * 50)
print("Context Used:")
print(context)
print("=" * 50)

# Prompt
prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not found in the context,
say "I don't know based on the provided context."

Context:
{context}

Question:
{question}

Answer:
"""

# Send To Ollama
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen3:4b",
        "prompt": prompt,
        "stream": False
    }
)

result = response.json()

print("\nAI Answer:\n")
print(result["response"])