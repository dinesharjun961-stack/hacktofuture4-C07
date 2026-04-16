from typing import TypedDict, List

class RedBlueState(TypedDict):
    current_phase: str
    system_components: List[str]
    vulnerabilities_found: List[str]
    patches_applied: List[str]
    attack_attempts: int
    system_secure: bool