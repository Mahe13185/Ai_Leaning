import requests
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

index = faiss.read_index("knowledge.index")
with open("knowledge.txt", "r") as file:
    knowledge = file.read()
sentences = knowledge.splitlines()
model = SentenceTransformer("all-MiniLM-L6-v2")

question = input("Question: ")
questionEmbedding = model.encode(question)
questionEmbeddingVector = np.array(
    [questionEmbedding],dtype=np.float32
)

D,I = index.search(
    questionEmbeddingVector,3
)

context = ""
print("\nTop Matches:\n")
for indexValue in I[0]:
    context += sentences[indexValue] + "\n"
print("=" * 50)
print("Context Used:")
print(context)
print("=" * 50)

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
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen3:4b",
        "prompt": prompt,
        "stream": False
    }
)
ai_response = response.json()

print("\nAI Answer:")
print(ai_response["response"])