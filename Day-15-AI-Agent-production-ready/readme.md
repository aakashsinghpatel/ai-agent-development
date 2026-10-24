## Production ready AI agent
 Till now, we have build an autonomous agent with all required tool and multi agent system that can do what is expected.
 But it is not production ready.
 Note: We can not trust the LLM output specifically in decision taking case.
 This could be better in paid LLM but all thing need to be care about.
 ANd prompt need to ne tested for all scenario to handle any failure.

 What if?
 1. ollama is unavailable?
 2. LLm request takes too long?
 3. AI tool fails?
 4. User provide invalid input
 5. An agent tries to access file which is not allowed
 6. An document contain melecious instruction.
 7. The agent make unnecessary agent call.

 so, Production ready sytem is all about handing and taking care of this scenarios and situation.
 It can be build based on takin g care 5 parameters:

 1. Reliability: System should recover from temporary failure
        Via: Error handling(Gracefull error handeling), Retry, Timeout, BackOff 
 2. Security: Agent should not automatically have access to everything on system
        Via: Input validation, tool permission, file/folder access, Prompt  inject prevention
 3. Observability: we should be able to know, what agent did
        Via: Logging
 4. Maintainability: cade should be organized properly
        Via: Folder structure over single file development, Single responsibility priciple file and folder
 5. Performance: Should avoid unnecessary work and LLM calls
        Via: Paraller execution over sequential based on scenario, Only require LLM call, Small Prompt.


``` Configuration should be kept saperated from application code in saperate file
    Use: .env: tyo keep secrate, keep all application congiguration in sinle palce
    Use: config.py: to load the configuration

    Do not keep .env on git : 
        use gitignore to remove file tracking of .env from git
        keep: .env, *.pyc, /__pycache__, /.venv
```

### Centralize LLM acces: (Based on single responsibility)
 Rather creating Ollam client in each agent create in a file and that acces by all agnet
 > llm.py

### Build Obseravibilty with structure logging: Observability
    Logging is use to get important information about production running application:
    like:
    when something happens
    what level of event it was
    what actually happened

    > create: logger.py

### Build reliability with LLM Retries, Backoff and timeout: llm.py> call_llm()
    if ollama LLM faile then
     simple application: get crash
     Prod level application: handle it grafully via retries and machnism and after thresolt (MAX_RETIES) return error.

     Back off: Means do not hammer/call service that already fails.
     In this call service after certain delay.

     Here we have called with sleep machenism.

     But in large system, we can use more sophesticated exponantial machenism like 'jitter'.

#### If LLM failes the retry till limit with backoff
#### If tool get timeout:
    Tool execution taking to much time the we can use 'timeout' machnism to handle rather waiting for too much time.

    call_llm: Retry, timeout, 

    Now, we create llm.py: to handel all llm related task in sinle file that behave like sinle llm controller.

### Building agent security with secrets, input validation and permission:
    Secret: Alway keep secret in .env file and expose it to application vis config
        Do not expose it to git to habdle thos use gitignore.
        `Via`: .gitignore
    Input validation: 
        Alway validate the input of user to agent /llm system before process
        `via`: Input validation logic. 'validation/py'
    Permission check: Before making any tool execution asked by planner do check that tool can be allowed to execute by that requested agent.
        `via`:permissio manager 'permission.py'

        example:
            Input -> Delete file -> permission check -> yes -> delete    
                                                        No-> Reject

    File/folder access: Do not give whole system acces to aAgent it should be controlled.
            liek tool . in permission.py

    
### Building safe file access and protection against prompt injection:
    Give only reuired acces to each agent to folder and file acces.
    for thid check the access beforre any file operation.
    example: permisio.py: safe_file_acess()

    .resolve() of Path: provide absolute path of the same.

#### Specific security proble of AI System:
    Prompt inhection: Inject the instruction/document as input that can produce melecios result.
    Like deleting file or whole folder.

    Do not trust the data retrieved by agent from external system.

    To prevent for this: do not trust the external tool, api's, doc data alway protect from it via any action beeing asked by them via agent with checking permission acces of tool of agent.
    Cansecure system by checking the required action asked by agent allowed or not to it.

### Optimizing AI agent performance :
 1. Parallel execution: Parallize independed task only tha can run concerrenly and at task concreate the result.
 2. Make only necesary LLM call:
    LLm call caused: time, computation, cose and failure opportunity.
    so Before making any LLM call check if that can be completed programatically that will result in fast andreliable computation.
3. keep prompt small:
    Do not pass large context to LLM. Only pass requred, necessary and sufficient context.
    as large prompt is result in large time and cost.

### Maintanance:
    For batter maintanance of prod level application: convert sinle file application to more managable multi folder/file applcation based on signle responsibility.

    `Goal`: Each part of system should have clear responsibility.
     via grouping related related functionality in single folder.

### Final Production Orchestration:
     
     user -> main.py -> Input validation -> Agent Engine -> State
                                                |
                                              Manager  
                                                |
                                             Planner
                                                |
                                    ---------------------------
                                Research     Code Agent       Reviewer Agent
                                Agent

    Each agent has it external resources like: MCP tools, API's, File, RAG
    LLM loyer: Retry, TimeOut, Loggin -> Ollama

    And surrounding system:
        Security: Secrates, Input validation, Tool permission, Safe file access, Prompt injection awareness

### Review:
    Day 9: Autonomous Agent
    Day 13: Addes MCP
    Day 14: Multiple specialized agent
    Day 15: Production ready systerm

#### Production checklist
Reliablity:
    1. Retry
    2. Timeout
    3. Error handling
    4. Stop Condition

Security:
    1. Secrates (.env)
    2. Input validation
    3. Tool Permission
    4. Safe file access
    5. Permission boundary (Agent with prefined tool and file access)
    6. Prompt injection awareness

Observabilty:
    1. Logging

Performance:
    1. Reduce llm call
    2. Small Prompt
    3. Paraller execution

Maintanabilty:
    1. COnfiguration
    2. Modular architecture
    3. Saperation of responsibility

Till now we have have build everything from scratch Autonoumous agent with all tool (MCP, RAG, Memory ect) and multi agent systerm.
We also understood the architecture.

Now there are framework like (Langgraph, crewai) that can help use to build.

Now, question not be what is langgraph but which part of agent this framework can be use to build that we are building manually.
