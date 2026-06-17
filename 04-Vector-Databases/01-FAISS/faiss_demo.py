import faiss
import numpy as np
vectors = np.array([
    [1.0, 2.0],
    [2.0, 3.0],
    [4.0, 5.0]
], dtype="float32")

index1 = faiss.IndexFlatL2(2)

index = faiss.IndexFlatL2(2)
index.add(vectors)

query = np.array([
    [1.5, 2.5]
], dtype="float32")

distance, index_position = index.search(
    query,
    2
)
print(distance)
print(index_position)