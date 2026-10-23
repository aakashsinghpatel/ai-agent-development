""" Create various state funtion : It has total 6 function"""

def create_state(user_query, max_step=5):
    """ Metthod to create intial state of Agent loop"""
    state = {
        "user_request": user_query,
        "current_step": 0,
        "max_steps": max_step,
        "actions": [],
        "observations":[],
        "finished": False,
        "final_answer":""
    }
    return state

def add_action(state, action):
    """ Method to update the action as per decided by Planner """
    state["actions"].append(action)

def record_observation(state, action, observation):
    """ Method to record observation as per resulted by taking latets action of planner by tools """
    state["observations"].append({
        "step":state["current_step"],
        "action":action,
        "observation": observation
    })

def next_step(state):
    """ update thr current step as per competed previos one """
    state["current_step"]+=1

def can_continue(state):
    """  Method to check whether Planner should Think again or not """
    return (not state["finished"] and state["current_step"] < state["max_steps"])

def finish(state, final_answer):
    state["final_answer"] = final_answer
    state["finished"] = True