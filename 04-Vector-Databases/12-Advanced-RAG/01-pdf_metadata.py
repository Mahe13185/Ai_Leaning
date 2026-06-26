import chromadb
from pypdf import PdfReader

# Read PDF
reader = PdfReader("Java_Notes.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text() + " "

# Clean Text
text = text.replace("\n", " ")

# Split Into Words
words = text.split()

# Chunking
chunk_size = 50

chunks = []

for i in range(0, len(words), chunk_size):
    chunk = " ".join(words[i:i + chunk_size])
    chunks.append(chunk)

# Create ChromaDB Client
client = chromadb.PersistentClient(
    path="chroma-db"
)

# Create Collection
collection = client.get_or_create_collection(
    name="Java_Notes"
)

# Create IDs and Metadata
ids = []
metadatas = []

for i in range(len(chunks)):
    ids.append(
        "chunk" + str(i + 1)
    )

    metadatas.append(
        {
            "source": "Java_Notes.pdf"
        }
    )

# Store Data
collection.add(
    documents=chunks,
    ids=ids,
    metadatas=metadatas
)

# Verify
print("Chunks:", len(chunks))
print("IDs:", len(ids))
print("Stored:", collection.count())

print("\nMetadata Example:")
print(collection.get()["metadatas"][0])

result = collection.get()

print(result["metadatas"])