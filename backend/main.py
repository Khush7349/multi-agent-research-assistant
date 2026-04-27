from fastapi import FastAPI, UploadFile
import shutil, os

from utils import load_pdf
from rag import add_document
from agents import qa_agent, compare_agent
from graph import build_graph

app = FastAPI()
graph = build_graph()

UPLOAD_DIR = "backend/data"
os.makedirs(UPLOAD_DIR, exist_ok=True)

papers = {}

@app.post("/upload")
def upload(file: UploadFile):
    path = f"{UPLOAD_DIR}/{file.filename}"
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    text = load_pdf(path)
    papers[file.filename] = text
    add_document(text, file.filename)

    return {"message": "Uploaded & indexed"}

@app.post("/ask")
def ask(q: str):
    return {"answer": qa_agent(q)}

@app.post("/analyze")
def analyze(paper: str):
    text = papers.get(paper, "")
    result = graph.invoke({"text": text})
    return result

@app.post("/compare")
def compare(p1: str, p2: str):
    return {"comparison": compare_agent(papers[p1], papers[p2])}
