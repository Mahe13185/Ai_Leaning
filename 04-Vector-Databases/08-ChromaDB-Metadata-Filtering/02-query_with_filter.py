import chromadb

client = chromadb.PersistentClient(
    path="chroma-db"
)
collection = client.get_collection(
    name="Tech_Topics"
)

question = input("Question: ")

result = collection.query(
    query_texts=[question],
    n_results=3,
    where = {
        "topic":"java"
    }
)
print(collection.get())

print(result["documents"])
q
for doc in result["documents"][0]:
    print(doc)