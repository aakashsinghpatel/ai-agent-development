
from state import create_state, add_action, can_continue, record_observation, next_step, finish

async def run_agent_loop(user_request, planner, execute_action, formate_answer, tool_list, mcp_client):
    """ This is agen loop: it will run the whol loopl of 
   start agent loop-> Planner -> Next action -> update action -> Execute action 
    -> Record result -> update state -> check does need to next action (Planner) -> format response
     """

    # Intialize state
    state = create_state(user_request)

    # start agent loop
    # While can_continue: "This is the heart of our agent.“
    while can_continue(state):

        # Planner decide what to do next:
        next_action = planner(state, tool_list)

        print("Planner selectd action:", next_action)

        if next_action == 'FINISH':
            answer = formate_answer(state)
            finish(state, answer)
            break

        # We execute the actiom
        tool_result = await execute_action(mcp_client, next_action)

        # Add executed action to agent state
        add_action(state, next_action)

        # Record the observation in Agent state
        record_observation(state, next_action, tool_result)

        next_step(state)

    return state
        
