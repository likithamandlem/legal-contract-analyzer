from app.core.llm import get_llm_response

def summarize_contract(text: str) -> str:
    """Summarize the contract using Gemini."""
    
    prompt = f"""
You are a legal contract analyst. 
Analyze the following contract and provide a clear, concise summary in 5-7 sentences.

Cover:
- What type of contract this is
- Who are the parties involved
- Main purpose of the contract
- Key obligations
- Important dates or durations if mentioned

Contract Text:
{text[:4000]}

Summary:
"""
    return get_llm_response(prompt)