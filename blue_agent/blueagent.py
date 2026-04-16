from orchestrator.state import RedBlueState
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)



def blue_agent_node(state: RedBlueState) -> dict:
    vulns = state["vulnerabilities_found"]
    
    
    patch_prompt = f"You are a security engineer. Suggest patches for: {vulns}"
    patch_response = llm.invoke(patch_prompt)
    result = patch_response.content
    
    
    secure_prompt = f"""
    The following vulnerabilities were found: {vulns}
    The following patches were applied: {result}
    Is the system now secure? Reply with only one word: YES or NO.
    """
    secure_response = llm.invoke(secure_prompt)
    answer = secure_response.content.strip().upper()
    
    is_secure = "YES" in answer  
    
    return {
        "patches_applied": state["patches_applied"] + [result],
        "current_phase": "red_attacking",
        "system_secure": is_secure
    }
