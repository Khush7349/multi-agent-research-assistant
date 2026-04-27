# 🧠 Multi-Agent Research Assistant

> A multi-agent AI system for understanding, analyzing, and comparing research papers using local LLMs, RAG, and agentic workflows.

---

## 🚀 Overview

This project is an **AI-powered research assistant** that helps users:

- 📄 Upload and understand research papers  
- ❓ Ask context-aware questions (RAG-based)  
- ⚖️ Compare multiple papers intelligently  
- 🧠 Extract insights using multiple AI agents  

Built using a **modular, production-style architecture**, the system demonstrates how modern AI systems combine:

- Local LLMs  
- Retrieval-Augmented Generation (RAG)  
- Multi-agent orchestration  

---

## 🧩 Key Features

### 🤖 Multi-Agent System

- **Summarizer Agent** → Generates structured summaries  
- **Insight Agent** → Extracts contributions, methodology, and limitations  
- **QA Agent (RAG)** → Answers questions using retrieved context  
- **Comparison Agent** → Compares multiple research papers  

---

### 📚 Retrieval-Augmented Generation (RAG)

- Uses **FAISS** for vector similarity search  
- Embeds document chunks using sentence transformers  
- Retrieves relevant context before generating answers  

---

### ⚙️ Local LLM Integration

- Runs fully locally using **Ollama**  
- No external API costs  
- Supports models like `mistral`  

---

### 🌐 Full-Stack Architecture

- Backend → FastAPI  
- Frontend → Streamlit  
- Agents → LangGraph  
- Storage → Local + FAISS  

---

## 🏗️ Architecture
```
User (Streamlit UI)
        ↓
FastAPI Backend
        ↓
LangGraph (Agent System)
   ├── Summarizer Agent
   ├── Insight Agent
   ├── QA Agent (RAG)
   ├── Comparison Agent
        ↓
FAISS (Vector DB)
        ↓
Ollama (Local LLM)
```

---

## 📦 Project Structure
```
multi-agent-research-assistant/
│
├── backend/
│   ├── main.py
│   ├── agents.py
│   ├── graph.py
│   ├── rag.py
│   ├── utils.py
│   └── ollama_client.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
- git clone https://github.com/YOUR_USERNAME/multi-agent-research-assistant.git
- cd multi-agent-research-assistant
# AI Research Assistant (Agentic)
pip install -r requirements.txt
## Run Ollama
ollama pull mistral
## Run Backend
uvicorn backend.main:app --reload
## Run Frontend
streamlit run frontend/app.py

---

## 🛠️ Tech Stack
- Python
- FastAPI
- Streamlit
- LangGraph
- FAISS
- Sentence Transformers
- Ollama

---

👤 Author

Built as part of an advanced AI systems project demonstrating:

- Multi-agent design
- RAG pipelines
- Local LLM integration
