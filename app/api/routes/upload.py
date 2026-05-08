from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.schemas import UploadResponse
from app.core.pdf_parser import extract_text_from_pdf, get_total_pages, split_text_into_chunks
from app.core.embeddings import store_embeddings
from app.config import UPLOAD_DIR
import uuid
import os
import shutil

router = APIRouter()

@router.post("/upload", response_model=UploadResponse)
async def upload_contract(file: UploadFile = File(...)):
    
    # Validate file type
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed")
    
    # Generate unique file ID
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}.pdf")
    
    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Extract text
    text = extract_text_from_pdf(file_path)
    if not text.strip():
        raise HTTPException(status_code=400, detail="Could not extract text from PDF")
    
    # Split into chunks
    chunks = split_text_into_chunks(text)
    
    # Store embeddings in ChromaDB
    store_embeddings(file_id=file_id, chunks=chunks)
    
    return UploadResponse(
        message="Contract uploaded and processed successfully",
        filename=file.filename,
        file_id=file_id,
        total_pages=get_total_pages(file_path),
        total_chunks=len(chunks)
    )