import requests
from sentence_transformers.util import cos_sim
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

with open("knowledge.txt", "r") as file:
    knowledge = file.read()

sentences = knowledge.splitlines()

question = input("Question:")
questionEmbedding = model.encode(question)

best_score = -1
best_sentence = ""

knowledgeEmbeddings = []

for sentence in sentences:
    sentenceEmbedding = model.encode(sentence)
    score = cos_sim(questionEmbedding , sentenceEmbedding).item()
    if score > best_score:
        best_score = score
        best_sentence = sentence
    
print("=" * 50)
print(best_sentence)


# creating prompt
prompt = f"""
using this following Context 
{best_sentence}
Answer this Question
{question}
"""

# calling Ollama
url = "http://localhost:11434/api/generate"
payload = {
    "Model":"qwen3:4b",
    "prompt":prompt,
    "stream": False
}
response = requests.post(url,json=payload)

data = response.json()

print("Ai: " , data["response"])

