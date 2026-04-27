from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
doc_sources = []
index = None

def add_document(text, source):
    global index
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    embeddings = model.encode(chunks)

    if index is None:
        index = faiss.IndexFlatL2(embeddings.shape[1])

    index.add(np.array(embeddings))
    documents.extend(chunks)
    doc_sources.extend([source]*len(chunks))

def retrieve(query, k=5):
    if index is None:
        return []
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), k)
    return [(documents[i], doc_sources[i]) for i in I[0]]
