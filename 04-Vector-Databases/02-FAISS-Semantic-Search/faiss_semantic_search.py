import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

with open("knowledge.txt" , "r") as file:
    knowledge = file.read()

model = SentenceTransformer("all-MiniLM-L6-v2")
sentences = knowledge.splitlines()

sentencesEmbedding = []
for sentence in sentences:
    sentencesEmbedding.append(model.encode(sentence))

vector = np.array(
    sentencesEmbedding,dtype=np.float32)

index = faiss.IndexFlatL2(384)
index.add(vector)

question = input("Question: ")
questionEmbedding = model.encode(question)

questionVector = np.array(
    [questionEmbedding] , dtype=np.float32
)

D, I =  index.search(questionVector,3)

print("Top matches")
for indexes in I[0]:
     print(sentences[indexes] + "\n")



