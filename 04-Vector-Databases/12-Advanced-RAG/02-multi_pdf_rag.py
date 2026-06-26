import chromadb
from pypdf import PdfReader

all_chunks = []
all_ids = []
all_metadata = []
pdf_files = [
    "Java_Notes.pdf",
    "SpringBoot.pdf",
    "Data Structures and Algorithms.pdf"
]
for pdf_file in pdf_files:
    reader = PdfReader(pdf_file)

    text = ""
    for page in reader.pages:
        text += page.extract_text() + " "

    text = text.replace("\n", " ")
    words = text.split()

    chunk_size = 50

    chunk_couner = 0
    for i in range(0,len(words),chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        all_chunks.append(chunk)
        chunk_couner += 1

    client = chromadb.PersistentClient(
        path="chroma-db"
    )

    # Create Collection
    collection = client.get_or_create_collection(
        name="Tech_Knowledge_Base"
    )


    for i in range(chunk_couner):
        all_ids.append(
            "chunk" + str(len(all_ids) + 1)
        )

        all_metadata.append(
            {
                "source": pdf_file
            }
        )
# Store Data
collection.add(
    documents=all_chunks,
    ids=all_ids,
    metadatas=all_metadata
)

print("Chunks:", len(all_chunks))
print("IDs:", len(all_ids))
print("Metadata:", len(all_metadata))