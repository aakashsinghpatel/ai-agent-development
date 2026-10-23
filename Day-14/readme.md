## Multi Agent system and orchestrations:
1> Creating and multi agent with manager (having fixed/sequencial flow of agernt this does not able t  mke dynamic agent call)


## Sequential/ (code drivem) Multi agent workflow
Till Now we have create an autonomous agent: That recieve request, Take decision (What to do next) -> Execute action -> Observer result -> If require run loop  and send result back.


Now we create multiple specialized agent.: Devide responsibilty based on agent specialization.

For this there is 2 concept:
1. Agent Manager: For orchestration/Decision/Routing to specific agent.
2. Agent Worker: SPecialized agent to perform specific task.

Here we will develope multi agent orchestration:
Worker Agents:  Each agent having specific promp and LLM call to perform specific responsibility
    Research Agent
    Coding Agent
    Review Agent
Manager:
    This will manager the worker and route the query and result specifically based on workflow

Now, we are orchestrating sequencial flow:

    User Query -> Manager -> Research Agent -> RESEARCH_RESULT -> Codign Agent/worker -> CODING_RESULT ->
    Review worker -> REVIEW_RESULT -> (ALL result conclussion)-> Final Result

But this worflow has limitation(Manager.py):
    It only run a fixed sequencial flow. Flow is decided programatically.

### Intelligent multi agent workflow (Agent decision by Manager based on prompt):
    Here, LLM is used to decide the workflow, Worker based on thr user query (dynamic_manager.py)
    For this it also need to maintan state to decide based on previos decision and respective results.
    State: It is somethig which is based on orchastration of multi agent flow.

    State: task, [workers result] <Research, code, review>, history
    Intelligent manager: Select next worked based on task and state.


    Now:
    Autonomous Agent: Based on agent State planner decide next action/tool (RAG, MCP) to be execute.
    Autonomous Manager: Based on manager state, decide next worker/agent (LLM, Agent).

    Workflow:
                                            User Query
                                                |
                                            Manager state
                                                |
                                            Intelligent Manager
                                                |
                                            who act next
                                                |
                               Research-------Coding----------Review
                                  |_____________|_______________|
                                                |
                                              Update State 
                                                |
                                            Manager Agent 

Limitation: 
1. Till now, worked provide text response that is tedius for next worker to process and do necessary job.
Hence making structured output for worked make the work easy for agents.
2. As of now, worker is promtt driven and LLM. But we can not completely relie on LLM for expected ouput
hence we need to make prompt very specific even mention corner case, output format what should and should not be there to get expected result.

### Building structured communication between workers:
    Rather LLM respond with text response make the response structure like JSON with specific key value pair. That easy to understand for bot next worked and evaluator.

    Here, we make response of reviewer stucture to decide wheter the generated code is fine to finish task to agian generate the code using codi agent.

    ```Feedback Loop```: here based in Review agent output either task will be finish or regenerat the code.
    Im code generation the reviewal feedback will be used to generate the code as per review.
    This is know as feedback loop machanism.

    Flow: changes Require in(Review_agent, Manager, Coding agent <Feedback Loop>)

    Task -> Research -> code -> Review -------------------> APPROVED -> YES -> Finish
                          |            (Structure Result)        |  
                          |                                      |   
                          ---<--------- Feedback --<- -----------No    


                                           Intelligent Manager (Manager Agent)
                                                |
                                             AI Decision
                                                |
                               Research-------Coding----------Review
                                                                |
                                                            Structure Result
                                                                |
                                                            Manager Agent 

    limitation:
    As impelemented feedback loop between reviewer agent and coding agent trap in infine loop by manager.
### Building safeguard Multiagent (Manager):
    > Need update in state.py, manager.py
    Till now out multiagent workflow is ready with manager.
    But there can be situation where manager trap in infinite loop for selecting worker again and again.
    This make workflow in infinite loop duwe to feed ack .

    But in real time this need to be handle to prevent for loop. 

    1. Add variable in manager state:
        "Revision_count": Use this in prompt to return finish if revision count is reached as MAXIMUM_REVISION.
    2. Add globla variable: MAXIMUM_REVISION: Fixed value at code level

    Also other that LLM dependancy for FINISH code condition need to be manage for fallback machanism if LLM fail to return finish.

Limitation:
    1. As this flow is sequencial, mean manager run worker sequentially:

### Sequential and Paraller Agents: (FanIn and Fan Out)

#### Sequential:
    In this only one run at a time and respective output on one's sent to next worker.

         Research Agent -> Code Agent -> Review Agent

#### Parallel Agents:

    Worker are being decided by manager and they run parallely and at end output are merged and sent.

                                        Manager
                                           | 
                                     <<< FAN OUT >>> Task distribution
                                ___________|_________            
                                |          |        |
                            Research     code    review   [PARALLEL EXECUTION of WORKERS]
                                |___________|________| 
                                            | 
                                     <<< FAN IN >>> Result Collection
                                            |
                                        Manager/ Result

Fan out: Means manger distribute work to multiple workers/agent
Fan In: Once agent's complete the assigned work, thier result back together to manager


This will be simulate by: Parraller_execution.py (Both sequential and ||el flow)
    Implement 3 agent : This agent will be simulate by having sleep by differnt time rather LLM call.

    Squential: RUn each agent one afetr other sequenctila
    Paraller execution: Run all agent together parallelly (asyncio.together)


### Turning workers into autonomous worker agent:
    Tiil now alll worker are using LLM just to simulate agent work.
    manager with state, intelligence and stop condition, Worker with LLM call, feedback loop and parallel execution.

    They are not yet impelement as autonomous agent.

    This agent can be converted into autonomous agent as done in ```DAY_9``` based on need of worker and can be implement Task decomposition, Planner, tool integration (MCP), RAG, Agent(Execution) Loop, Memory (Longterm) i.e full fledged agent.

    But this need to be done based on need, no need to make worked/Agent unnecessary complicated.

    Agent: Planner -> Next action -> execute action -> Observer result -> loop if required .

### Review:
    In Day 9: Autonomous agent: Assistant with decision ability and can execute multi step workflow (Execution loop)
    In day 14: Multi step agent:
        Intelligent manager with state, dynamic routin (Agent selection), Stop condition
        Structure communication between agent and feed back loop
        Orchastrion of sequential and parraller execution of workers/agents 

    ```Manager```: Decide which worker to be use for task 
    ```Worked```: How to perform the task and responsibility

    Till now we ahve implemented whole autonomous agent and multi agent workflow from scratch.
    There are multiple modern framework to impelment the same 
    like : crewAI, Langchain, lang graph etc.