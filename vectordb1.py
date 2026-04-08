

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')


jobs = [
    "Software Engineer develops applications using Python and Java",
    "Data Scientist analyzes data using machine learning and statistics",
    "Web Developer builds websites using HTML, CSS, JavaScript",
    "AI Engineer works on deep learning and neural networks",
    "Database Administrator manages databases and SQL queries",
    "Cybersecurity Analyst protects systems from cyber attacks",
    "Cloud Engineer manages AWS and cloud infrastructure",
    "Mobile App Developer builds Android and iOS apps",
    "DevOps Engineer handles CI/CD pipelines and automation",
    "UI/UX Designer designs user interfaces and user experience"
]


embeddings = model.encode(jobs).astype('float32')


dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("Job Vector DB Created")
print("Total jobs stored:", index.ntotal)


while True:
    query = input("\n🔍 Enter job query (or 'exit'): ")

    if query.lower() == "exit":
        print(" Exiting...")
        break

    
    query_vec = model.encode([query]).astype('float32')

    
    k = 3
    distances, indices = index.search(query_vec, k)

    print("\n Recommended Jobs:")
    for i in indices[0]:
        print("-", jobs[i])