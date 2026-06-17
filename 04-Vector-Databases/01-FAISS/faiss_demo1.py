import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

# model creation
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Java is a programming language.",
    "JDBC is used to connect Java to databases.",
    "Spring Boot is a framework."
]

embeddings = []
# embedding into vectors
for sentence in sentences:
    embeddings.append(model.encode(sentence))


vectors = np.array(embeddings , dtype=np.float32)
index = faiss.IndexFlatL2(384)
index.add(vectors)

question = input("Question: ")
questionEmbedding = model.encode(question)
questionVector = np.array(
    [questionEmbedding], dtype=np.float32
)

D , I = index.search(questionVector,3)

for indexs in I[0]:
    print(sentences[indexs])

print(index.ntotal)

print("Distance: ")
print(D)
print("Index:")
print(I)

print("Sentences: ")
print(sentences[I[0][0]])
print("Shapes")
print(vectors.shape)
