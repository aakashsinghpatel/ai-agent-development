
from state import create_state, add_action, can_continue, record_observation, next_step, finish

async def run_agent_loop(user_request, planner, execute_action, formate_answer, tool_list, tool_registry):
    """ This is agen loop: it will run the whol loopl of 
   start agent loop-> Planner -> Next action -> update action -> Execute action 
    -> Record result -> update state -> check does need to next action (Planner) -> format response
     """

    # Intialize state
    state = create_state(user_request)

    # start agent loop
    # While can_continue: "This is the heart of our agent.“
    while can_continue(state):
        print(f"\n--------Step {int(state['current_step'])+1}--------------")
        # Planner decide what to do next:
        action = planner(state, tool_list)

        print("Planner selected action:", action)

        if action['tool'] == 'FINISH':
            answer = formate_answer(state)
            finish(state, answer)
            break

        # We execute the actiom
        tool_result = await execute_action(tool_registry, action['tool'], action['arguments'])
        print("Result of execution of tool: ", tool_result)
        # Add executed action to agent state
        add_action(state, action['tool'])

        # Record the observation in Agent state
        record_observation(state, action['tool'], tool_result)

        next_step(state)

    return state
        
