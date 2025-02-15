import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("medical_data.txt", "r", encoding="utf-8") as f:
    medical_data = f.readlines()

embeddings = model.encode(medical_data)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def search_medical_info(query):
    query_embedding = model.encode([query])
    _, indices = index.search(query_embedding, k=1)
    return medical_data[indices[0][0]] if indices[0][0] < len(medical_data) else "No relevant data found."
