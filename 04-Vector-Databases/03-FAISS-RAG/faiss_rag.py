import faiss
import numpy as np
import requests
from sentence_transformers import SentenceTransformer

# Load Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read Knowledge Base
with open("knowledge.txt", "r") as file:
    knowledge = file.read()

sentences = knowledge.splitlines()

# Create Chunks
chunks = []

for i in range(0, len(sentences), 2):
    chunk = sentences[i:i + 2]
    chunks.append(" ".join(chunk))

# Generate Chunk Embeddings
chunk_embeddings = []

for chunk in chunks:
    chunk_embeddings.append(
        model.encode(chunk)
    )

# Convert To NumPy
vectors = np.array(
    chunk_embeddings,
    dtype=np.float32
)

# Create FAISS Index
index = faiss.IndexFlatL2(384)

# Store Vectors
index.add(vectors)

# User Question
question = input("Question: ")

# Question Embedding
question_embedding = model.encode(question)

query_vector = np.array(
    [question_embedding],
    dtype=np.float32
)

# Top K Search
top_k = min(3, len(chunks))

D, I = index.search(
    query_vector,
    top_k
)

# Build Context
context = ""

for index_value in I[0]:
    context += chunks[index_value] + "\n"

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

ai_response = response.json()

print("AI Answer:")
print(ai_response["response"])