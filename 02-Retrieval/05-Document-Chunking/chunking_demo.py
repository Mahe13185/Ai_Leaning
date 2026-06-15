sentences = [
    "Java",
    "JDBC",
    "Spring",
    "MySQL",
    "Docker",
    "Kubernetes"
]

chunks = []

for i in range(0,len(sentences),2):
    chunk= sentences[i:i+2]
    chunks.append(chunk)

print(chunks)
