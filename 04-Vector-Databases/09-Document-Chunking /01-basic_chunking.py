
text = """
Java is a programming language.
Java supports OOP.
Polymorphism allows one interface to have multiple implementations.
Inheritance allows code reuse.
Encapsulation hides implementation details.
"""

sentences = text.strip().splitlines()
chunks = []

for i in range(0,len(sentences),2):
    chunk = " ".join(sentences[i:i+2])
    chunks.append(chunk)

print(chunks)