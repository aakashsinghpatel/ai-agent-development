## Advance Agent Planning
    Till now,
    User Request -> Planner think -> Take /Excute action -> update State -> Observe result -> Take action --- loop (Think/Planner )-> Planner only tell the next action.


    NOw, We will break the user goal into subtask first the go to planner.

    User Rquest -> Task Decomposition -> Tasks -> Planner -> Tool -> Observation -> Planner

### Advance AI agent workflow
    Now, AUtonomouse AGent will:
    1. Understant the user request
    2. Breask into subtask. (Task decomposition): One of the Big idea of Advance ai agent
        Break the user request into small intedepnd task.
    3. Execute the task one by one
    4. store intermediate result
    5. Revealute the sutask
    6. change the plan if required.
    7. stop whene overall goal achieved

    Task Decomposition: Break request into smaaller independt task
        Now State will be:

#### Advance AI agent state
    State: {
            User request,
            Task: [{taskName, Status:Pending/completed}]
            current_task
            results:[] list of all intermediate tasks
            current_step
            Max_step
            actions:[]:All excuted actions name 
            onservations: [{step, action, result}]
            finished: Boolean
            final_anser: Result of User request
        }

#### Buiild task decomposor
  task_panner.py > decompose_task(Request): LIst of subtask

### New method for updated state
    state.py
    1. add_task(state, task): new task add wiht pending state
    2. complete_task(state, task): mark the task as compelte
    3. all_completed_task(state): check ALL task compeleted : Boolean
    4. pending_task(state): list ofall pending task
    5. add_result(state, result):All result for all intermediate task compete

Now, ther is 3 concept
1. Task: What need to do
2. Action: What agent actual perform to complete the task
3. Observation: Result after action perfomed

#### Build Agent task planner:
    Now agent planner not only retur the next action.
    But it will return the next pending task and best action to compete the task
    Decision: {TaskName, toolName}

    >planner.py: 
      planner(userRequest. toolList)
       now planner uses: User request, Tool list, pending task, observation and results 
       to define next task and tool to use
       Thi now: what should be done and how shoulb edone
      build_tool_description(toolList)
#### Connection planner with executor
    >executor.py:: execute_action(mcp_client, tool_name)
#### Build agent loop
    >loop.py::  run_agent_loop(user_request, planner, format_response, tool_list, mcp_clint)

    steps:
        1. Create new stete with user request
        2. decompose into subtask
        3. Start agent loop
        4. Ask planner for decision{subtask, toolname}
        5. check if all task compeleted:
            update finish() with formated answer
        6. if any task: extract the tool execute the tool
        7. update actions, intermediate result, step
        8. mark the task as completed with handle error senarion
        9. repeat step

#### Integrate all worked: Runner.py
    > runner.py 
    1. Intialize mcp client
    2. get mcp tool list
    3. take user request
    4. start agent loop with iuser request
    5. diplay the agent loop answer as response


### Now LLM are used at 3 place:
    1. Task Decomposor
    2. Task Planner (What next task and Tool)
    3. AI reponse genrator. answer_formattor

We ahve following file: ( 9 file)
    state.py
    task_planner.py 
    planner.py
    executor.py
    answer.py
    loop.py
    runner.py
    mcp_client.py
    mcp_server.py

### Static planner
 generate plan and follow it
    Genrate password, get_time ad  follow the same
### Dynamic planner:
    updagte plan if requered

    user request -> Task decompose -> task -> Planner -> action -> execute action -> evaluate  -> update paln if result not as expected (reault as failed) -> then ask to reexcute thre action agian :: Dynamic planner

This planner, decomposor and gerator: ALL are on 'prompt' with specific role on same AI model

to make dynamic planner just need to update PROMPT: 
    To handle the failure scenario
    inst: If action failed, then reconsider the current plan.

    If something gone wrong then plannner shoudl considert the old plan

Planner -> tool -> execute -> fails -> palnner -> same tool -> faild......infine
To preven this we habe MAX_STEP

we have deined max_step and can_continue: so that of there is continur fails of tool the Agent do not go in infine loop

* An autonoumos agent must have stop condition (Max_step)


Till now:
Day 8: Agent using tool
Day 9:Autonoumous agent (Planner deciding the tool using agen loop)
Day 10: Advant agent planner: task decomposition

Now later:
    Day 11: Intodice memory so that at any time stop and back will have reume capability and 
    result /state stored in persistant


