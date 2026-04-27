import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="AI Research Assistant",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📚 AI Research Assistant")
st.sidebar.markdown("Agentic Academic Copilot")

page = st.sidebar.radio(
    "Navigate",
    ["Upload Paper", "Ask Questions", "Compare Papers"]
)

# ---------------- HEADER ----------------
st.title("🧠 AI Research Assistant")
st.caption("Multi-Agent System powered by RAG + Local LLM")

# ---------------- UPLOAD PAGE ----------------
if page == "Upload Paper":
    st.subheader("📄 Upload Research Paper")

    uploaded = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded:
        with st.spinner("Processing paper..."):
            res = requests.post(
                f"{API_URL}/upload",
                files={"file": uploaded}
            )

        st.success("✅ Paper uploaded and indexed successfully!")

# ---------------- ASK PAGE ----------------
elif page == "Ask Questions":
    st.subheader("❓ Ask Questions")

    query = st.text_area("Enter your question", height=100)

    col1, col2 = st.columns([1, 4])

    with col1:
        ask_btn = st.button("Ask")

    if ask_btn and query:
        with st.spinner("Thinking..."):
            res = requests.post(
                f"{API_URL}/ask",
                params={"q": query}
            )

        answer = res.json().get("answer", "")

        st.markdown("### 🧾 Answer")
        st.write(answer)

# ---------------- COMPARE PAGE ----------------
elif page == "Compare Papers":
    st.subheader("⚖️ Compare Papers")

    col1, col2 = st.columns(2)

    with col1:
        p1 = st.text_input("Paper 1 filename")

    with col2:
        p2 = st.text_input("Paper 2 filename")

    if st.button("Compare Papers"):
        if p1 and p2:
            with st.spinner("Analyzing papers..."):
                res = requests.post(
                    f"{API_URL}/compare",
                    params={"p1": p1, "p2": p2}
                )

            comparison = res.json().get("comparison", "")

            st.markdown("### 📊 Comparison Result")
            st.write(comparison)
        else:
            st.warning("Please enter both filenames")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built with FastAPI + LangGraph + Ollama + FAISS")