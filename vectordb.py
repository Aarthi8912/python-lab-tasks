
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


model = SentenceTransformer('all-MiniLM-L6-v2')

texts = [
    "The sun rises in the east",
    "Water boils at 100 degrees Celsius",
    "The human brain controls the body",
    "Plants need sunlight for photosynthesis",
    "Electric cars reduce pollution",
    "The internet connects people worldwide",
    "Exercise improves physical health",
    "Reading books improves knowledge",
    "Sleep is essential for good health",
    "Technology is evolving rapidly"
]


embeddings = model.encode(texts).astype('float32')


dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("Vector DB Created")
print("Total stored vectors:", index.ntotal)

while True:
    query = input("\n Enter your query (or type 'exit'): ")

    if query.lower() == "exit":
        print(" Exiting...")
        break

    query_vec = model.encode([query]).astype('float32')

    k = 3
    distances, indices = index.search(query_vec, k)

    print("\n Top Matching Results:")
    for i in indices[0]:
        print("-", texts[i])