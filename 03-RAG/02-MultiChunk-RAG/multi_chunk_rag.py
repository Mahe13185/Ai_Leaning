from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import requests

with open("knowledge.txt", "r") as file:
    knowledge = file.read()
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = knowledge.splitlines()

chunks = []

for i in range(0,len(sentences),2):
    chunk = sentences[i:i+2]
    chunks.append(" ".join(chunk))

chunksEmbeddings = []

question = input("What is the Question?: ")
questionEmbedding = model.encode(question)

for chunk in chunks:
    chunksEmbeddings.append(model.encode(chunk))

scores = []
for i in range(len(chunksEmbeddings)):
    cal_score = cos_sim(questionEmbedding,chunksEmbeddings[i]).item()
    scores.append( (cal_score, chunks[i]) )
scores = sorted(scores,reverse=True)
top3 = scores[:3]

context = ""
for score , chunk in top3:
    context += chunk + "\n"

prompt = f"""
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
aiResponse = response.json()

print("=" * 50)
print("Context Used:")
print(context)

print("=" * 50)
print("AI Answer:")
print(aiResponse["response"])