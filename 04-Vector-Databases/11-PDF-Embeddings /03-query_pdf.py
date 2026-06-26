import chromadb
from pypdf import PdfReader

client = chromadb.PersistentClient(
    path="chroma-db"
)

collection = client.get_collection(
    name="Java_Notes"
)
question = input("enter your Question: ")
result = collection.query(
    query_texts=[question],
    n_results=3
)

for doc in  result["documents"][0]:
    print(doc)