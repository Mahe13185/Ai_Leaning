import chromadb
from pypdf import PdfReader

reader = PdfReader("Java_Notes.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + " "
text = text.replace("\n" , " ")
words = text.split()
chunk_size = 50

chunks = []
for i in range(0,len(words),chunk_size):
    chunk = " ".join(words[i:i+chunk_size]) + " "
    chunks.append(chunk)


client = chromadb.PersistentClient(
    path="chroma-db"
)

collection = client.create_collection(
    name="Java_Notes"
)
ids = []
for i in range(len(chunks)):
    id = "Chunks" + str(i)
    ids.append(id)
collection.add(
    documents=chunks,
    ids = ids
)