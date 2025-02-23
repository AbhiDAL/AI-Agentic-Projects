import chromadb
from sentence_transformers import SentenceTransformer
import os

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="chroma_db")

# Load Sentence Transformer Model (Embedding Model)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load summary from file
def load_summary():
    with open("summary.txt", "r", encoding="utf-8") as f:
        return f.read()

# Store summary in ChromaDB
def store_summary(summary_text):
    collection = chroma_client.get_or_create_collection(name="ai_research_summaries")
    
    # Convert text into embeddings
    embedding = embedding_model.encode(summary_text).tolist()

    # Store in ChromaDB with an ID
    collection.add(
        ids=["summary_1"],  # Unique ID
        embeddings=[embedding],
        metadatas=[{"source": "summary.txt"}],
        documents=[summary_text]
    )
    print("✅ Summary stored successfully in ChromaDB!")

# Main Execution
if __name__ == "__main__":
    summary = load_summary()
    if summary:
        store_summary(summary)
    else:
        print("⚠️ No summary found to store!")
