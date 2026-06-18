import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

with open("knowledge.txt", "r") as file:
    knowledge = file.read()

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = knowledge.splitlines()

embeddings = []

for sentence in sentences:
    embeddings.append(model.encode(sentence))

vector = np.array(
    embeddings,dtype=np.float32
)

index = faiss.IndexFlatL2(384)
index.add(vector)

faiss.write_index(index,"knowledge.index")

print(index.ntotal)
print("Index saved sucxessfully")