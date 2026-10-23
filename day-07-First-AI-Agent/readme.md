### Build Your first AI Agent
    AI Assiatnt                                 AI Agent
    =================================================================
    Follow Instruction                          Make Decision
    Use tools when tols                         Choose tools by itself
    Execute predefined workflow                 Plan workflow dynamically
    Reaction                                    Goal Oriented

Till Now: Application can
```* Generate Response 
* Memory 
* Personality 
* Tool Calling 
* File Reading 
* RAG```
What is  missing: Decision making
    When and which tool to call -> till now python program decide this

Now:
    User Query -> AI think -> I Need to call tool -> Tool call -> Get Result -> Generate ANswer

How Ai agent choose tool:
We provide 3 thing to AI assistant:
* User Query * All available toll * Instrunction to decide tool


** THe saperation of planning and execution is the main characterstics of modern AI Agent.

Leter we will have::
Multiple tools, Multiple Steps, Memory, Refletion, Error recovery

### Agentic AI is fundamentally about decision making and orchestration of workflow not just adding more api's and using more powerful LLM.

##$$ Building Agent Brain: Not solve problem, but let know how to solve problem
    Agent planner which decide what to do next, means
    * Do we need to call tool
    * and which tool to be call
    Based on user query

To create Tool Planner /Agent Brain
* User Instruction, * Available tools, * Instruction to define tool calls


Now flow will be:
Use goal(request) -> Planner(LLM model: Decide which tool to be call) -> Tool name -> Python -> execute tool -> Result -> LLM model (Genrate response: In natural language) -> Final Answer 

Now LLM (AI model) will be used twice, once for AI planner and 2nd for AI assistant.

Means, model can behave differently based on system instruction (Promp) can adopt different personality.


AI planner : LLM model that take user request and return the tool name which will becalle

Now:
Step 1: User Request -> 
Step 2: Planner  (LLM Invoke with prompt to decide)->   Tool Name ->
Step 3: Python execute tool -> Tool Result ->
Step 4:Sent result to AI Assistant (LLM Invoke to react) -> 
Step 5:Natural response -> 
Step 6:Show result

file: planner .py and test_plnner.py

connect the planner with assistant:: assitant.py
Python code decide the tool, AI planner decide the tool and python run the code

Each component has saperate responsibiltu

Planner : Decides -> what tool to be call
Tools : Execute the task
Assiatnt: Make response natural

As tool increas not need to change assiatnt or python just planner need to update.

Many modent AI system use the same with differ name like:
 Planner, decision engine, orchestrator, Router..

THe work same under he hoos:
* Understand the user goad.
* Decide the tool.
* execute the tool
* Communicate the response.

AI Planner : Decide what tool to call with LLM model rather python code decide it.
* Limitation:
    currently AI planner just decide one tool at a time can not select mutliple tool at a time to fullfile use goal.

