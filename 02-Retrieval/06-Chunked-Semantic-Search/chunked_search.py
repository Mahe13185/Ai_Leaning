from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")
with open("knowledge.txt" , "r") as file:
    knowledge = file.read()

sentences = knowledge.splitlines()

chunks = []

for i in range(0,len(sentences),2):
    chunk= sentences[i:i+2]
    chunks.append(" ".join(chunk))

chunkEmbeddings = []
for chunk in chunks:
    chunkEmbeddings.append(model.encode(chunk))

question = input("Question: ")
questionEmbedding = model.encode(question)

scores = []
for i in range(len(chunkEmbeddings)):
    score = cos_sim(questionEmbedding,chunkEmbeddings[i]).item()
    scores.append((score , chunks[i]))
scores = sorted(scores,reverse=True)

print(scores)
