from typing import TypedDict

class AgentState(TypedDict):
    user_request: str
    current_step: int
    max_step: int
    actions: list
    observations: list
    finish: bool
    final_answer: str