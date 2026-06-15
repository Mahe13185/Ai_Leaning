from sentence_transformers.util import cos_sim
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

with open("knowledge.txt" , "r") as file:
    knowledge = file.read()

sentences = knowledge.splitlines()

question = input("Question:")
questionEmbedding = model.encode(question)

best_score = -1
best_sentence = ""

knowledgeEmbeddings = []

for sentence in sentences:
    knowledgeEmbeddings.append(model.encode(sentence));

    score = cos_sim(questionEmbedding , knowledgeEmbeddings).item()

    print(sentence)
    print(f"Score: {score:.4f}" )

    if(score > best_score):
        best_score = score
        best_sentence = sentence
    
print("=" * 50)
print("Best Match:")
print(best_sentence)
print("Similarity:", best_score)