from fastapi import FastAPI
from app.api.routes import upload, analyze, chat

app = FastAPI(
    title="AI Legal Contract Analyzer",
    description="Upload and analyze legal contracts using AI",
    version="1.0.0"
)

app.include_router(upload.router, prefix="/api/v1", tags=["Upload"])
app.include_router(analyze.router, prefix="/api/v1", tags=["Analyze"])
app.include_router(chat.router, prefix="/api/v1", tags=["Chat"])

@app.get("/")
def root():
    return {"message": "AI Legal Contract Analyzer is running"}