from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def extract_text_from_pdf(file_path: str) -> str:
    """Extract all text from a PDF file."""
    reader = PdfReader(file_path)
    full_text = ""
    
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    
    return full_text

def get_total_pages(file_path: str) -> int:
    """Get total number of pages in PDF."""
    reader = PdfReader(file_path)
    return len(reader.pages)

def split_text_into_chunks(text: str) -> list:
    """Split text into chunks for embedding."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ".", " "]
    )
    chunks = splitter.split_text(text)
    return chunks