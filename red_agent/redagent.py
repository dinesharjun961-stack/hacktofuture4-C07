from orchestrator.state import RedBlueState
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)



def red_agent_node(state: RedBlueState) -> dict:   
    components = state["system_components"]
    prompt = f"You are a penetration tester. List 2 vulnerabilities in: {components}"
    response = llm.invoke(prompt)
    result = response.content
    return {
        "vulnerabilities_found": state["vulnerabilities_found"] + [result],
        "attack_attempts": state["attack_attempts"] + 1,
        "current_phase": "blue_defending"
    }
