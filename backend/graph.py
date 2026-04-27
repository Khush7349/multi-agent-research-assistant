from langgraph.graph import StateGraph
from agents import summarize_agent, insight_agent

def build_graph():
    def summarize_node(state):
        return {"summary": summarize_agent(state["text"])}

    def insight_node(state):
        return {"insights": insight_agent(state["text"])}

    graph = StateGraph(dict)
    graph.add_node("summarize", summarize_node)
    graph.add_node("insights", insight_node)

    graph.set_entry_point("summarize")
    graph.add_edge("summarize", "insights")

    return graph.compile()
