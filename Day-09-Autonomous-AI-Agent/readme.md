## Building an autonomous AI Agent
  Think -> Action -> Observe-> think -> Action ------- Finish (Goal acheived)
### What is an autonomous AI agent?
     AI agent the independently plan, take decision and execute multi step worlkflow(multiple tool call for single user request if requed)  to achieve user goal w/o human intervention is Autonomous AI agent.
     does not stop on singl etool call
    Till now: Our planner can provide on one tool name, but in real time an user request can require multi tool to  achive the goal.

    ** Agent state and Agent loop ** 
    There for we need something that can execute and provide multi tool?

    Agent loop: It is repetative cycle in which AI agent:
        1. Think abour current situation
        2. Take decion on next action
        3. Execute action
        4. Observe the result
        5. Decide whether another actio require or not 

    The lopp continiues unti final resilt achieved.

    Process:
     Think -> Act -> Observe -> Think (loop)

### Design of Agent loop:
 Once the planner compelte the one iteration, in second iteration how it know, what happend in first iterration.

#### Agent loop workflow:
 User request -> 
 Create Intial Agent State -> 
 Start Agent loop -> 
 Planner think -> select next Action -> Execute Action (RAG OR MCP <Tool Call> OR LLM call) -> 
 Record Observation -> 
 Task Completed -> Yes-> Send respone
            |___ No -> Next Iteration (Loop) -> Planner think-......

 Here Agent state come into picture.
    Problem: Once first iteration compelte how Agennt/Planner know what is current state (like which tool execute/goal acheived etc.)

#### Agent State: 
    The state/Dictionaly/ value tell the Agent about the current state.

Agent loop desing Step:
1. Create Agent state: As neew request come create/inialize the state.
2. Start Agent loop: Ask planner with query.
3. Planner think: need 3 input
    > User request
    > Previous Action
    > Previose observation (Action result)
4. Execute Action : Tool call or LLM call OR RAG
5. record Observation: Store action result
6. Think Again: 
    the plannenr need previos Action and Observation so that it does not provide same action agin as to be execute
7. Next action and execite:
8. Decide whether continue:?
    Pass result/observation to planner and decide if goal achieved the stop elase continue iteratiom
9. combine all observation and return output


### Building Agent state:
    Agent state is disctinary of
        1. User request
        2. next_action: Action that to be do as per planner asked
        3. actions: list of all action alreadt taken as per planner
        4. observations: list of resulut/observation by each action execution 
            [{
                step: In what step this action/observation
                action: name of action
                observation: result of action
            }]
        5. max_step: max iteration that loop can have to achieve goal, this to prevent infinite loop
        6. finished: Boolean, to check loop finished (either on final result or max_step )
        7. final_answwr: final answer as per user request

    It has 6 method :
        1. create_state(user_request, max_step): Dict{agent_state}
        2. next_action(state, action): actions.append(action)
        3. record_observation(state, action, observation): onservation.append({step,action,observation})
        4. next_step(state): step+1 (Call after excution of action given pby planner)
        5. finish(state, answer): finish:true, final_answer=answer
        6. can_continue(state): not finished and current_step < max_step

#### Implementation the agent state 
    state.py (agent state)


###  Building Agent loop:
1.  Create agent loop: agetnt> loop.py (run_agent_loop(user_request, planner, execute_action, formate_answer, tool_list, mcp_client))
2. create planner<primpt based on state> : planner.py < planner(state, tool_list)>:
    Plan a provide next action
3. create executor: <executor.py>: Saperation of concer: run the next action on MCP server
4. format_anser: LLM Model: acces to fomat anser based on user quesy, inter responsena action
5. Runnuer: runner.py: Ru the whol e agen handle all : client, planner, executor and all copnent,

Limitation:: 
1. Multiple invoke to llm in agennt loop for single use rrequest to full file the goal asd erive next action. this make the whole execution slow.
2.  what if planner never return 'FINISH'
    hence we have handled it via 'max_step'.

Alse can continue: make the Autonous system prevennt to go into infinite loop.

* currently Agent take one action at a time and agai loop.
in future we will decidel the larger goal and break the goal into multiple step.
    

