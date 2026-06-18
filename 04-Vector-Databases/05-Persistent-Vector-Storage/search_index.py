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

print("\nTop Matches:\n")
for indexValue in I[0]:
    print(sentences[indexValue])

print("Distance:")
print(D)