from app.core.embeddings import get_collection
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_relevant_chunks(file_id: str, question: str, top_k: int = 5) -> list:
    """Retrieve most relevant chunks for a question."""
    try:
        collection = get_collection(file_id)
        
        # Embed the question
        question_embedding = embedding_model.encode(question).tolist()
        
        # Search ChromaDB
        results = collection.query(
            query_embeddings=[question_embedding],
            n_results=top_k
        )
        
        chunks = results["documents"][0]
        return chunks
    
    except Exception as e:
        raise RuntimeError(f"Retrieval failed: {str(e)}")