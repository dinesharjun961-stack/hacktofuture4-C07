from langgraph.graph import StateGraph, END
from orchestrator.state import RedBlueState
from red_agent.redagent import red_agent_node
from blue_agent.blueagent import blue_agent_node

def decide_next_step(state: RedBlueState) -> str:
    if state["system_secure"]:
        return "end"
    if state["attack_attempts"] >= 3:
        return "end"
    return "red_attacking"

def build_graph():
    graph = StateGraph(RedBlueState)
    graph.add_node("red_agent", red_agent_node)
    graph.add_node("blue_agent", blue_agent_node)
    graph.set_entry_point("red_agent")
    graph.add_edge("red_agent", "blue_agent")
    graph.add_conditional_edges(
        "blue_agent",
        decide_next_step,
        {
            "red_attacking": "red_agent",
            "end": END
        }
    )
    return graph.compile()