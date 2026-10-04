## Memory Engineering (Build Autonomous agent with memory)

    Till now, Once agent stop it stop everythig it loo the state and it reset.
    User request->store new state -> agent work -> program stop -> state disacpper
    Means, state is temporary.
    
    This is difference between remembering  state during execution and across execution.

    What is memory engineering: The process of designing how agent
    1. Store information
    2. Retrieve information
    3. decide what is useful (to store and for use request)
    4. uses previous information
    5. maintain information afetr execution

                state                 |         Memory
                --------------------------------------
                current execution       Previous Execution
                Temporary               Persistant
                Current task            Previous information
                current step            previous conversation
    Return->    Action                  useful fact
    Store ->    onservation             store exeperience


    State has: current Task, current step, Current Observatio 
        It remeber and disappear after execution of user query
    Memory: This user user conversatiom
        This help to survive program restart.

    Before:
        User request -> state -> planner ->MCP ->Answer

    Now:
        User request -> Memory retrieval -> state -> Planner -> MCP ->Answer

    Just Inetgrated memory to AI Agent (Autonomous Agent with Memory)


### Building persistant memory with squlite:
 >Memory.py
 Now:
    User request -> Agent -> Memory ->SQLIte ->memories.db

#### why sqlite? (No need to install sqlite specifically )
        1. Built in python (No need to install sqlite specifically - as already part of python)
        2.No DB server 3. DB is a file 4. uses SQL 5. Lightweight
        6. perfact for out agent
#### DB design:
> Memories.py
1. create database
2. create table (id, query, ai_respons, embedding)
3. create methods:
    > create_embedding(text)
    > cosine_similarity(embedding1, embedding2)
    > save_memory(query, answer) 
        insert into memories (query, answer , embedding(aquery+answer))
    > serch_semantic_memorry(user_query,top_k, thresholt): 
        retunr top_k memory(row) whose embeddings semantic similarities >= thresolt

### Integrating memory into AI agent
step 1: state.py
    1. Add new key into state: memories:[]
        It contain list of all relevant memories for user queries
    2. Add method-> add_memory(state, memory):
                        state["memories"].append(memory)
step 2: Modify loop.py
    user query -> search memory -> relevant memory -> state
    call method on correct place:
        from memory.py> search_relevant_memory(memory), save_memory(query, ai_answer)
        from state.py > add_memory(state, memory)
step 3: Give memory to planner
        It will still return task and tool to complete it {task, tool}
        Here, we need to update prompt with providing previous conversation of state
        the change:
         
step 4: Give memory to answer:
    Here also change prompt with providing previous conversation
    to genrate the natural response and ask to use previous conversation

step 5: save the conversation
    > loop.py
        save the conversation once all task finish (task==finish) 

step 6: update planner instruction:
        update the prompt to handle what to return :
            1. handle condition if no task is there.
            2. also handle if request is of type conversation memory, any knowledge abase etc..
step 7: update runner.py
    1. create DB

step 8: update task_planner.py
    Update task planner to return taska d difine various scenario when to retun none:
        Personal question variosu scnario

#### Now workflow::
 user Query -> Memory Retrival -> Planner -> MCP -> Answer -> Save To Memory


### Building Memory Extractor for intelligent long-term memory:
    Tiil now we are story all the thing to memory (Quesgion, AI_response) foreach loop/request of User.
    But is it required to rember all thing like: time, genration question etc :: NO
    So, Memory extractor
#### Memory Extractor:
>extractor.py
    It is method, part of Agent that extact userful pesoanl identical information from the user_query and ai_response.

    If it is useful the store into memory else don't.

    ```methods```:
    > extract_memory(user_query, answer):
        here we will have prompt, that will dicide whether conversation is usefull (worth to remember< preferences, interests, goals, skills, projects, important user facts>) else retur none.
    Final integration: Adding semantic memory to AI agent:
    > memory.py
        save_semantic_memory(fact):
            inser(user_request, embedding) values(fact, embeding(fact))
    > loop.py:
        call save_semantic_memory at "finish" action planner for user request
        after extract_memory return any fact that need to bes store

### Now architecture:
    User request -> Search long term memory -> Relevant information -> State -> Task Decomposor -> Tasks -> Planner -> MCP tool -> Observation -> Final Anser
                                                        |
                                            -----------------------------            
                                            |                           |
                                        Save_memory()<SQLITE>        Extract_memory
                                                                        |
                                                                    useful Information
                                                                    |           |
                                                                    |           |
                                                                   <YES>         No
                                                                    |
                                                                save_semantic_memory(SQLITE)

## Compete workflow Now:
user query -> create state -> retrieve relevant memory -> update state -> task decomposition -> update state with task as pending status -> agent loop (Check all task completed: finish)-> planner -> next action -> Execute action -> update action -> update observation -> update result -> update task (status as complete/failed) -> update step -> Agent loop -> planner -> (Check all task completed: finish) -> save memory (query, final answer)<sqlite> retrieved_semantic fact ->
 if available -> store into Sqite save_semantic_meanin()<sqlite>

### Now LLM work as 34 role:
    Task Decomposer, Task Planner, Answer generator, Memory extractor

## Review:
    1. We only retrieve information from memory that sementicaly equivalnt to user query.
    2. Only store conversatio that user for future {user information}
    3. Now agent can also remeber previous conversation that can help in futher intraction.
Tiill now:
Day 9: It could act <Agent loop>
Day 10:It could plan <Task decomposer>
Day 11: It can remeber <Memory-sqlite>

Take away:
1. State is temporary 
2. Memory service the restart with giving last conversation
3. sqlite built in python 
4. embedding allow sementic memory retrieval
5. Agent retrieve memory before answer and also save useful information to memory back.


        


