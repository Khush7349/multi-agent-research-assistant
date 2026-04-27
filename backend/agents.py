from ollama_client import call_llm
from rag import retrieve

def summarize_agent(text):
    prompt = f"""You are an academic assistant.
Summarize the research paper clearly with:
- Objective
- Method
- Key Results
- Conclusion

{text[:3000]}
"""
    return call_llm(prompt)

def insight_agent(text):
    prompt = f"""Extract:
- Key contributions
- Novel ideas
- Limitations

{text[:3000]}
"""
    return call_llm(prompt)

def qa_agent(question):
    contexts = retrieve(question)
    context_text = "\n".join([c[0] for c in contexts])

    prompt = f"""Answer using context only.
Context:
{context_text}

Question:
{question}
"""
    return call_llm(prompt)

def compare_agent(text1, text2):
    prompt = f"""Compare two research papers:

Paper 1:
{text1[:1500]}

Paper 2:
{text2[:1500]}

Give:
- Similarities
- Differences
- Which is better and why
"""
    return call_llm(prompt)
