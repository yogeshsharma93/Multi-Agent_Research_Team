from typing import TypedDict, List
from langgraph.graph import StateGraph
from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.critic import critic_agent
from agents.retry_researcher import retry_researcher
from agents.writer import writer_agent

# Define the expected schema of the state
class GraphState(TypedDict):
    topic: str
    subquestions: List[str]
    claims: List[dict]
    retry_claims: List[dict]
    validated_claims: List[dict]
    report: str

def build_graph():
    graph = StateGraph(GraphState)  # passing schema here

    graph.add_node("planner", planner_agent)
    graph.add_node("researcher", researcher_agent)
    graph.add_node("critic", critic_agent)
    graph.add_node("retry", retry_researcher)
    graph.add_node("writer", writer_agent)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "critic")
    graph.add_edge("critic", "retry")
    graph.add_edge("retry", "writer")
    graph.set_finish_point("writer")

    return graph.compile()
