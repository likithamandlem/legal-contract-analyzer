from app.core.retriever import retrieve_relevant_chunks
from app.core.llm import get_llm_response

def answer_question(file_id: str, question: str, chat_history: list = []) -> dict:
    
    chunks = retrieve_relevant_chunks(file_id, question)
    context = "\n\n".join([f"Source {i+1}:\n{chunk}" for i, chunk in enumerate(chunks)])
    
    history_text = ""
    for msg in chat_history[-4:]:
        if hasattr(msg, 'role'):
            history_text += f"{msg.role}: {msg.content}\n"
        else:
            history_text += f"{msg.get('role', '')}: {msg.get('content', '')}\n"
    
    prompt = f"""
You are a legal contract assistant. Answer the user's question based ONLY on the contract context provided below.

If the answer is not in the context, say "This information is not found in the contract."

Always cite which source you used (Source 1, Source 2, etc.)

Contract Context:
{context}

Chat History:
{history_text}

User Question: {question}

Answer:
"""
    answer = get_llm_response(prompt)
    
    return {
        "answer": answer,
        "sources": chunks
    }