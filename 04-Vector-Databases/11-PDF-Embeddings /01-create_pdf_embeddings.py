from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

reader = PdfReader("Java_Notes.pdf")

model = SentenceTransformer("all-MiniLM-L6-v2")
text = ""

for page in reader.pages:
    text += page.extract_text() + " "

text = text.replace("\n" , " ")

words = text.split()

chunk_size = 50

chunks = []
for i in range(0,len(words),chunk_size):
    chunk = " ".join(words[i:i+chunk_size])
    chunks.append(chunk)

embeddings = []

for chunk in chunks:
    embedding = model.encode(chunk)
    embeddings.append(embedding)

print("Chunks", len(chunks))
print("Embeddings: " ,len(embeddings))

print("\nEmbedding Dimension:")
print(len(embeddings[0]))
print(type(embeddings))
print(type(embeddings[0]))
