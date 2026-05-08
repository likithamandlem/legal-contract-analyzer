# ⚖️ AI Legal Contract Analyzer

An end-to-end Generative AI application that analyzes legal contracts using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), semantic search, and vector databases.

The system allows users to upload PDF contracts, extract and analyze clauses, detect legal risks, generate summaries, and interact with contracts using a contextual AI chatbot.

---

# 🚀 Features

## 📄 Contract Processing
- Upload and parse PDF legal contracts
- Extract text from multi-page documents
- Automatic chunking for semantic retrieval

## 🧠 AI-Powered Analysis
- Contract summarization
- Clause extraction
- Risk detection and flagging
- Legal Q&A chatbot using RAG

## 🔍 Semantic Search
- OpenAI embeddings (`text-embedding-3-small`)
- ChromaDB vector storage
- Context-aware retrieval pipeline

## 💬 RAG Chatbot
- Ask questions about uploaded contracts
- Contextual answers with retrieval
- Chat memory support
- Source-aware responses

## 🐳 Deployment Ready
- FastAPI backend
- Streamlit frontend
- Dockerized application
- Modular production-style architecture

---

# 🏗️ System Architecture

```text
PDF Upload
    ↓
Text Extraction
    ↓
Chunking
    ↓
OpenAI Embeddings
    ↓
ChromaDB Vector Store
    ↓
Retriever
    ↓
GPT-4o LLM
    ↓
------------------------------------------------
| Summary | Clause Extraction | Risk Detection |
| Chatbot | Semantic Search   | Legal Q&A      |
------------------------------------------------
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Backend | FastAPI |
| Frontend | Streamlit |
| LLM | OpenAI GPT-4o |
| Embeddings | text-embedding-3-small |
| Vector Database | ChromaDB |
| Frameworks | LangChain |
| PDF Parsing | PyPDF |
| Deployment | Docker |
| Language | Python |

---

# 📂 Project Structure

```text
legal-contract-analyzer/
│
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── upload.py
│   │       ├── analyze.py
│   │       └── chat.py
│   │
│   ├── core/
│   │   ├── pdf_parser.py
│   │   ├── embeddings.py
│   │   ├── retriever.py
│   │   └── llm.py
│   │
│   ├── services/
│   │   ├── summarizer.py
│   │   ├── clause_extractor.py
│   │   ├── risk_detector.py
│   │   └── rag_chain.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── config.py
│   └── main.py
│
├── frontend/
│   └── streamlit_app.py
│
├── vectorstore/
├── uploads/
├── screenshots/
├── tests/
│
├── Dockerfile
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/likithamandlem/legal-contract-analyzer.git
cd legal-contract-analyzer
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Setup Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
CHROMA_DB_PATH=./vectorstore
UPLOAD_DIR=./uploads
```

---

# ▶️ Running the Application

## Run FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend available at:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

## Run Streamlit Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend available at:

```text
http://localhost:8501
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t legal-contract-analyzer .
```

## Run Docker Container

```bash
docker run -p 8001:8001 legal-contract-analyzer
```

Docker API:

```text
http://localhost:8001/docs
```

---

# 📸 Screenshots

## Contract Analysis

![Analysis](screenshots/analysis.png)

## Chat Interface

![Chat](screenshots/chat.png)

---

# 💬 Example Questions to Ask

- What are the termination clauses?
- Are there any high-risk liabilities?
- Summarize the payment obligations
- Who owns the intellectual property?
- What happens if the contract is breached?
- Are there any indemnification clauses?
- What are the confidentiality obligations?

---

# 📊 Project Highlights

- Supports semantic contract retrieval using embeddings
- Handles multi-page PDF contracts efficiently
- Modular RAG pipeline architecture
- Retrieval-aware AI chatbot
- Production-style backend organization
- Dockerized for deployment readiness

---

# 📈 Performance Notes

- Uses OpenAI `text-embedding-3-small` for semantic retrieval
- Optimized chunking strategy for retrieval relevance
- Supports large PDF contracts efficiently
- Average response latency depends on OpenAI API response time

---

# 🧩 Challenges Faced

- Handling large multi-page PDF contracts efficiently during text extraction and embedding generation
- Optimizing chunk size and overlap to improve retrieval relevance while reducing hallucinations
- Managing OpenAI API rate limits and token usage during development and testing
- Resolving ChromaDB collection conflicts caused by repeated uploads and re-indexing
- Handling dependency and SDK version conflicts across LLM-related packages
- Ensuring retrieved context remained accurate and relevant for legal-domain queries
- Maintaining modular and scalable architecture for future deployment and vector database migration

---

# 🔮 Future Improvements

- Migrate to Pinecone for scalable vector storage
- Add OCR support for scanned contracts
- Implement role-based access control
- Deploy to AWS with auto-scaling
- Add multi-language contract support
- Build multi-user support with authentication
- Add evaluation pipelines for retrieval and response quality
- Add observability and monitoring dashboards

---

# 🧪 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/upload` | POST | Upload and process contract |
| `/api/v1/analyze` | POST | Analyze uploaded contract |
| `/api/v1/chat` | POST | Ask questions about contract |

---

# 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

- Retrieval-Augmented Generation (RAG)
- Vector databases and embeddings
- FastAPI backend development
- LLM application architecture
- Semantic search systems
- Docker containerization
- Production-style AI system design

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit pull requests.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Likitha Mandlem**

GitHub:  
https://github.com/likithamandlem