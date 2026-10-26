from langgraph.graph import (START, END, StateGraph)
from agent.state import AgentState
from  agent.planner import planner
from agent.executor import execute_action
from agent.answer import format_answer
# import to raise intruppt for human approval
from langgraph.types import interrupt
# in memmory check point to save agent state so the agent can resume from same rather restart 
from langgraph.checkpoint.memory import InMemorySaver

def create_planner_node(tools):
    # This is langgraph node:
        #  Langgraph node only take state ans input and returrn updated state
    # As planner alos need toollist therefor the function wrap into function to get 
    # tool as param as use te planner to call it
    def planner_node(state: AgentState):
        action = planner(state, tools)

        print("\nPlanner Selected:")
        print(action)

        return {
            "actions": state["actions"],
            "observations": state["observations"],
            "current_step": state["current_step"],
            "finished": action == "FINISH",
            "action": action,
            "final_answer": state["final_answer"]
        }
    return planner_node

def approval_node(state:AgentState):
    decision = interrupt({
                "message": "Approve this tool call?",
                "action": state["action"]
            })
    # update approval value of state base on interrupt decision
    return {"approval":decision}


def create_tool_node(client):
    async def tool_node(state: AgentState):
        print("Tool name to execute:", state['action'])

        result =  await execute_action(client, state['action'])

        print(f"Result of executed tool {state['action']} : {result}")

        return {
           "actions": (state['actions']+ [state['action']]),
            "observations": (state['observations']+ 
            [{"action":state['actions'], "step": state['current_step'], "observation": result}]),
            "current_step": state['current_step']+1
        }
    return tool_node


def answer_node(state: AgentState):
    answer = format_answer(state)
    
    print("\nFinal Answer:")
    print(answer)
    
    return {
        "final_answer": answer,
        "finished": True
    }
    
# Roting handling
def route_after_planner(state: AgentState):
    if state['action'] == 'FINISH':
        return "finish"
    else:
        return "approval"   

# Routung handlinf
def route_after_tool(state: AgentState):
    if(state["current_step"] >= state['max_step']):
        return "stop"
    else:
        return "continue"


def route_after_approval(state:AgentState):
    if state["approval"] == "yes":
        return "approved"

    return "rejected"



def build_graph(tools, client):
    builder = StateGraph(AgentState)

    planner_node = create_planner_node(tools)
    tool_node = create_tool_node(client)
    

    builder.add_node("planner", planner_node)
    builder.add_node("tool", tool_node)
    builder.add_node("answer", answer_node)
    builder.add_node("approval", approval_node)

    builder.add_edge(START, "planner")

    # builder.add_conditional_edges("planner", route_after_planner,
    #                               {"finish": END, "tool": "tool"})
    # builder.add_conditional_edges("planner", route_after_planner,
    #                               {"finish": "answer", "tool": "tool"})

    """ Add human in loop for tool execution  """
    builder.add_conditional_edges("planner", route_after_planner,
                                      {"finish": "answer", "approval": "approval"})

    builder.add_conditional_edges("approval",route_after_approval ,{"approved":"tool", "rejected":"answer"})
    
    builder.add_conditional_edges("tool", route_after_tool,
                                      {"stop": "answer", "continue": "planner"})
    
    builder.add_edge("answer", END)

    # Act as checkpoint with respect to threadid  onfigured at invoke to
    # resume on intruppted
    checkpoint = InMemorySaver()
    # configured checkpoint into graph: at compile time
    return builder.compile(checkpointer=checkpoint)

