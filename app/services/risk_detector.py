from app.core.llm import get_llm_response
from app.models.schemas import RiskItem
import json

def detect_risks(text: str) -> list:
    """Detect risky clauses in the contract."""
    
    prompt = f"""
You are a legal risk analyst.
Analyze this contract and identify risky clauses.

Return ONLY a valid JSON array like this:
[
  {{
    "clause": "description of the clause",
    "risk_level": "High",
    "reason": "why this is risky"
  }}
]

Risk levels must be: High, Medium, or Low
Find 3-6 risks maximum.

Contract Text:
{text[:4000]}

JSON Response:
"""
    response = get_llm_response(prompt)
    
    try:
        # Clean and parse JSON
        cleaned = response.strip()
        if "```json" in cleaned:
            cleaned = cleaned.split("```json")[1].split("```")[0].strip()
        elif "```" in cleaned:
            cleaned = cleaned.split("```")[1].split("```")[0].strip()
        
        risks_data = json.loads(cleaned)
        
        risks = []
        for item in risks_data:
            risks.append(RiskItem(
                clause=item.get("clause", ""),
                risk_level=item.get("risk_level", "Medium"),
                reason=item.get("reason", "")
            ))
        return risks
    
    except Exception:
        return [RiskItem(
            clause="Could not parse risks",
            risk_level="Medium",
            reason="Please review contract manually"
        )]