from pydantic import BaseModel, Field
from typing import Optional, List

class UploadResponse(BaseModel):
    message: str
    filename: str
    file_id: str
    total_pages: int
    total_chunks: int

class AnalyzeRequest(BaseModel):
    file_id: str

class RiskItem(BaseModel):
    clause: str
    risk_level: str
    reason: str

class AnalyzeResponse(BaseModel):
    file_id: str
    summary: str
    clauses: List[str]
    risks: List[RiskItem]

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    file_id: str
    question: str
    chat_history: Optional[List[ChatMessage]] = Field(default=[])

class ChatResponse(BaseModel):
    answer: str
    sources: List[str]