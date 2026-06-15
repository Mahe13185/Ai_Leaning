from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")
with open("knowledge.txt" , "r") as file:
    data = file.read()
sentences = data.splitlines()

question = input("Enter Your Question: ")
questionEmbedding = model.encode(question)

scores = []
sentencesEmbedding = []
for sentence in sentences:
    sentencesEmbedding.append(model.encode(sentence))

for i in range(len(sentencesEmbedding)):
    conSin_score = cos_sim(questionEmbedding,sentencesEmbedding[i]).item()
    scores.append( (conSin_score,sentences[i] ))
scores = sorted(scores, reverse=True)
top3 = scores[:3]

print(top3)