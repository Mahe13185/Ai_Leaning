import chromadb

client = chromadb.PersistentClient(
    path="chroma-db"
)

collection = client.create_collection(
    name="Tech_Topics"
)
collection.add(
    documents=[
        "Java is a programming language.",
        "JDBC is used to connect Java to databases.",
        "Spring Boot is a framework.",
        "RAG stands for Retrieval Augmented Generation.",
        "FAISS is a vector database library."
    ],
    metadatas=[
        {"topic":"java"},
        {"topic":"database"},
        {"topic":"Spring"},
        {"topic":"RAG"},
        {"topic":"FAISS"}
    ],
    ids=[
        "id1",
        "id2",
        "id3",
        "id4",
        "id5"
    ]
)

print("Created")