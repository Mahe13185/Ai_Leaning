import chromadb

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.create_collection(
    name="Java_Topics"
)
collection.add(
    documents=[
    "Java is a programming language.",
    "JDBC is used to connect Java to databases.",
    "Spring Boot is a framework."
    ],
    metadatas=[
        {"topics":"java"},
        {"topics":"JDBC"},
        {"topics":"Spring"}
    ],
    ids=[
        "id1",
        "id2",
        "id3"
    ]
)
