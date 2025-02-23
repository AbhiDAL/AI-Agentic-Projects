import chromadb
from sentence_transformers import SentenceTransformer
import openai
import os

# Load OpenAI API Key securely
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API key not found! Set the 'OPENAI_API_KEY' environment variable.")

# ✅ Initialize OpenAI Client (required for v1.0+)
client = openai.Client(api_key=OPENAI_API_KEY)

# ✅ Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="chroma_db")
collection = chroma_client.get_or_create_collection(name="ai_research_summaries")

# ✅ Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Function to search ChromaDB
def search_chroma(query):
    query_embedding = embedding_model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1  # Get the most relevant summary
    )
    if results["documents"]:
        return results["documents"][0][0]  # Return the most relevant document
    return "No relevant information found."

# Function to generate AI-powered response
def generate_response(query):
    summary = search_chroma(query)
    if summary == "No relevant information found.":
        return summary
    
    # ✅ Corrected API Call (OpenAI v1.0+)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an AI research assistant."},
            {"role": "user", "content": f"Summarize and provide insights on: {summary}"}
        ],
        temperature=0.7
    )
    
    return response.choices[0].message.content  # ✅ Corrected response format

# ✅ Main Execution
if __name__ == "__main__":
    query = input("Enter your query: ")
    response = generate_response(query)
    
    print("\n🔹 AI Response:\n")
    print(response)
