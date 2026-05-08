from fastapi import APIRouter, HTTPException
from app.models.schemas import AnalyzeRequest, AnalyzeResponse
from app.services.summarizer import summarize_contract
from app.services.clause_extractor import extract_clauses
from app.services.risk_detector import detect_risks
from app.config import UPLOAD_DIR
from app.core.pdf_parser import extract_text_from_pdf
import os

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_contract(request: AnalyzeRequest):
    
    # Find the uploaded file
    file_path = os.path.join(UPLOAD_DIR, f"{request.file_id}.pdf")
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found. Please upload first.")
    
    # Extract text
    text = extract_text_from_pdf(file_path)
    
    if not text.strip():
        raise HTTPException(status_code=400, detail="Could not extract text from PDF")
    
    # Run all analysis
    summary = summarize_contract(text)
    clauses = extract_clauses(text)
    risks = detect_risks(text)
    
    return AnalyzeResponse(
        file_id=request.file_id,
        summary=summary,
        clauses=clauses,
        risks=risks
    )