

def create_state(user_request, max_step=5):
    """ Intialize the agent state """
    state={
        "user_request": user_request,
        "tasks":[],
        "current_task": None,
        "current_step": 0,
        "max_step": max_step,
        "actions": [],
        "observations":[],
        "results":[],
        "finished": False,
        "final_answer": ""
    }

    return state

def add_action(state, action):
    """ Method to update action list with executed action """
    state['actions'].append(action)

def record_observation(state, action, result):
    """  Method to record action completed with result and respective step on whcih done """
    state['observations'].append({"step":state['current_step'], 'action': action, 'observation': result})

def next_step(state):
    """ Method to move to next step on current step completed """
    state['current_step']+=1

def finish(state, answer):
    """ Method to maek agent loop as completed for user request/goal """
    state['finished'] = True
    state['final_answer'] = answer

def can_continue(state):
    """  Importan method : to cehck whether to contine loop to stao agen loop
     This make Agent prevent from infinite loop  """
    return (not state['finished'] and state['current_step'] < state['max_step'])

"""  Now added new methos to handle task planner which is integrated before planner """

def add_task(state, task):
    """ Method to update task state: add new state with respective status """
    state['tasks'].append({'task': task, "status": "PENDING"})

def add_result(state, result):
    state['results'].append(result)

def complete_task(state, task):
    "Mark the specific task of state as completed"
    
    # Normalize the task received from the planner.
    # This makes the comparison tolerant of:
    # "Generate password"
    # "generate password"
    # "generate_password"

    normalized_task = (
        task
        .strip()
        .lower()
        .replace("_", " ")
    )

    for item in state["tasks"]:
        normalized_existing_task = (
            item["task"]
            .strip()
            .lower()
            .replace("_", " ")
        )
        if normalized_existing_task == normalized_task:
            item["status"] = "COMPLETED"
            return True
    return False

def all_task_completed(state):
    """ Method to check all task completed """
    if not state["tasks"]:
        return False
    return all(item["status"] == "COMPLETED" for item in state["tasks"])
