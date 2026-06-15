from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")

pairs = [
    ("JDBC", "Database Connection"),
    ("JDBC", "Dog"),
    ("Spring Boot", "Java Framework"),
    ("Java", "Programming Language"),
    ("Java", "Pizza")
]

for text,text2 in pairs:
    emb = model.encode(text)
    emb1 = model.encode(text2)
    score = cos_sim(emb,emb1)
    print(f"{text} <--> {text2}")
    print(f"Score: {score.item():.4f}")
    print()



