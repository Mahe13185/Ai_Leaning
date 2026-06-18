import chromadb

client = chromadb.PersistentClient(
    path="chroma_db"
)
collection = client.get_collection(
    name="Java_Topics"
)

question = input("Enter your Question: ")

result = collection.query(
    query_texts=[question],n_results=3
)
print(result)
print("====Documents====")
for docs in result["documents"][0]:
    print(docs)
print("====Meta Data====")

for metadata in result["metadatas"][0]:
    print(metadata["topics"])
print("====ids====")

for ids in result["ids"][0]:
    print(ids)

print("====distance====")

for dis in result["distances"][0]:
    print(dis)