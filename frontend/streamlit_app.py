import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8001/api/v1"

st.set_page_config(
    page_title="AI Legal Contract Analyzer",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ AI Legal Contract Analyzer")
st.markdown("Upload a legal contract and get instant AI-powered analysis.")

# Session state
if "file_id" not in st.session_state:
    st.session_state.file_id = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "analysis" not in st.session_state:
    st.session_state.analysis = None

# Sidebar — Upload
with st.sidebar:
    st.header("📄 Upload Contract")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file:
        if st.button("Upload & Process", type="primary"):
            with st.spinner("Uploading and processing..."):
                files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
                response = requests.post(f"{API_BASE}/upload", files=files)

                if response.status_code == 200:
                    data = response.json()
                    st.session_state.file_id = data["file_id"]
                    st.session_state.chat_history = []
                    st.session_state.analysis = None
                    st.success(f"✅ Uploaded successfully!")
                    st.info(f"Pages: {data['total_pages']} | Chunks: {data['total_chunks']}")
                else:
                    st.error("Upload failed. Please try again.")

    if st.session_state.file_id:
        st.divider()
        st.success("✅ Contract loaded")
        st.code(st.session_state.file_id[:8] + "...", language=None)

# Main area
if not st.session_state.file_id:
    st.info("👈 Upload a PDF contract from the sidebar to get started.")

else:
    tab1, tab2, tab3 = st.tabs(["📊 Analysis", "💬 Chat", "ℹ️ About"])

    # Tab 1 — Analysis
    with tab1:
        st.header("Contract Analysis")

        if st.button("🔍 Analyze Contract", type="primary"):
            with st.spinner("Analyzing contract... this may take a moment"):
                response = requests.post(
                    f"{API_BASE}/analyze",
                    json={"file_id": st.session_state.file_id},
                    headers={"Content-Type": "application/json"}
                )

                if response.status_code == 200:
                    st.session_state.analysis = response.json()
                else:
                    st.error(f"Analysis failed: {response.text}")

        if st.session_state.analysis:
            data = st.session_state.analysis

            st.subheader("📝 Summary")
            st.write(data["summary"])

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📋 Key Clauses")
                for i, clause in enumerate(data["clauses"], 1):
                    st.markdown(f"**{i}.** {clause}")

            with col2:
                st.subheader("⚠️ Risk Analysis")
                for risk in data["risks"]:
                    if risk["risk_level"] == "High":
                        color = "🔴"
                    elif risk["risk_level"] == "Medium":
                        color = "🟡"
                    else:
                        color = "🟢"

                    with st.expander(f"{color} {risk['risk_level']} — {risk['clause']}"):
                        st.write(risk["reason"])

    # Tab 2 — Chat
    with tab2:
        st.header("💬 Chat with Contract")
        st.markdown("Ask any question about your contract.")

        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        question = st.chat_input("Ask a question about the contract...")

        if question:
            with st.chat_message("user"):
                st.write(question)

            st.session_state.chat_history.append({
                "role": "user",
                "content": question
            })

            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = requests.post(
                        f"{API_BASE}/chat",
                        json={
                            "file_id": st.session_state.file_id,
                            "question": question,
                            "chat_history": [
                                {"role": msg["role"], "content": msg["content"]}
                                for msg in st.session_state.chat_history
                            ]
                        },
                        headers={"Content-Type": "application/json"}
                    )

                    if response.status_code == 200:
                        data = response.json()
                        answer = data["answer"]
                        st.write(answer)

                        st.session_state.chat_history.append({
                            "role": "assistant",
                            "content": answer
                        })
                    else:
                        st.error(f"Error: {response.text}")

    # Tab 3 — About
    with tab3:
        st.header("About This App")
        st.markdown("""
        **AI Legal Contract Analyzer** is a production-style GenAI application that helps you understand legal contracts quickly.

        **Tech Stack:**
        - 🔥 FastAPI — Backend API
        - 🦙 Llama 3.3 via Groq — LLM
        - 🔍 Sentence Transformers — Embeddings
        - 🗄️ ChromaDB — Vector Database
        - 🎨 Streamlit — Frontend

        **Features:**
        - Upload and process PDF contracts
        - AI-powered summarization
        - Key clause extraction
        - Risk detection and analysis
        - RAG-powered Q&A chatbot
        """)