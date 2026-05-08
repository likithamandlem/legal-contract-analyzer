from app.core.llm import get_llm_response

def extract_clauses(text: str) -> list:
    """Extract important clauses from the contract."""
    
    prompt = f"""
You are a legal contract analyst.
Extract the most important clauses from this contract.

Return ONLY a Python list of strings, each string being one important clause.
Format: ["clause 1", "clause 2", "clause 3"]

Focus on:
- Payment terms
- Termination conditions
- Liability clauses
- Confidentiality terms
- Renewal terms
- Penalty clauses

Contract Text:
{text[:4000]}

Important Clauses (return as Python list only):
"""
    response = get_llm_response(prompt)
    
    try:
        # Clean response and parse list
        cleaned = response.strip()
        if cleaned.startswith("["):
            clauses = eval(cleaned)
            return clauses if isinstance(clauses, list) else [cleaned]
    except Exception:
        pass
    
    # Fallback — split by newlines
    lines = [line.strip("- ").strip() for line in response.split("\n") if line.strip()]
    return lines