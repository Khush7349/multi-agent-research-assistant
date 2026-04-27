# AI Research Assistant (Agentic)

## Setup

pip install -r requirements.txt

## Run Ollama
ollama pull mistral

## Run Backend
uvicorn backend.main:app --reload

## Run Frontend
streamlit run frontend/app.py
