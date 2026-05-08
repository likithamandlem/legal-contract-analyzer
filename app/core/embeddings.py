import chromadb
from sentence_transformers import SentenceTransformer
from app.config import CHROMA_DB_PATH

# Initialize ChromaDB client
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

# Free local embedding model - no API needed
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def store_embeddings(file_id: str, chunks: list):
    """Embed chunks and store in ChromaDB with metadata."""
    try:
        collection = client.get_or_create_collection(name=file_id)

        try:
            embedded_chunks = embedding_model.encode(chunks).tolist()
        except Exception as e:
            raise RuntimeError(f"Embedding failed: {str(e)}")

        collection.add(
            ids=[f"{file_id}_chunk_{i}" for i in range(len(chunks))],
            embeddings=embedded_chunks,
            documents=chunks,
            metadatas=[
                {"file_id": file_id, "chunk_index": i}
                for i in range(len(chunks))
            ]
        )

    except RuntimeError:
        raise
    except Exception as e:
        raise RuntimeError(f"Failed to store embeddings: {str(e)}")


def get_collection(file_id: str):
    """Get existing ChromaDB collection for a file."""
    try:
        return client.get_collection(name=file_id)
    except Exception:
        raise ValueError(f"No embeddings found for file_id: {file_id}")