## MCP in depth
    In real time there can be multiple MCP server that need to be connect with Aplication..

    Agent -> Mcp CLinet -> Multiple MCP Server (Time server, Weather server) -> Too Execute -> Result

    Now, after getting tool name from Agent, how to know which MCP server to connect??

    Therefor ther is mcp tool registory:
        IT contains mapping for all available tool of all MCP server serve to which application connect with server details;

        ``` dic :{toolname1: 
                {client: MCP_CLIENT, tool {toolname, description....},
            toolname2: {...}}}
        ```


    Now agent workflow:

    Agent -> Tool registory (mcp_Manager) -> correct MCP Client -> correct MCP server -> Execute tool -> Result

    >mcp_manager: have tool_regisory
        > tool_registry(ALL_SERERS_URL_NAME:[])-> {toll registory}
            client: create client for each m,cp server and storeit
            get all tool for each server and accotdinly create registory
        It contain all the methos to get Tools, resoureces, Prompt and respctive call , read and get respctive capability of server to access it via clinent
        Also have method to connect and dsconnet to all clinents

        Code have > ALl servers, mcp_manger and only one mcp_client file
        mcp_clint file exposes method to connec(server), diconner(server), get tool, resource, prompt and call toolm read resource, get prompt  method from passed client
        This all method are generic call based on clioent passed.
    > mcp_server: Tool the require name argument
        get_temprature(city)

        will mmaking too call via mcp client make sute pass argument into dictionary {"city": "indore"}

### Integrate multiple MCP configuration to agent: using Day 9 Autonomous agent
    update Plnner(planner.py): Update planner code:
        Now tool can alos call with argument.
        extract the toollist with each tool with argument if required of it
        Now update plnanner such that it return tool name with respective argument inthe valid formt
    update executor (exevutor): 
        update executur, such that it retrive the the correct colien for toolresistore ,
        tool name and argument to pass and call the loop via mcp_manager.
    update agent loop (Loop.py)> 
        now loop: ask for tool_registory  and pass the argument in exeute tool call
    update runner.py(ruuner.py)>

### Integrating Multi MCP server in to Autonomous agent
    * rather connecting to client, coonet to multiple MCP server and get clients and too registry
    * Pass tool_registry to loop_agent

1. update runner.py
    *fro mcpmanger  create mcp servand get clinet and mcp re
    & fetch all tool list
    pass run_agent_loop into runagent loop instead on mcp_clinent
2. update planner
    1. build tooldescriptionL addd input schem
    2. ask plnne to retutn JSOn of tool name and argument required it to call
    3. the prompt should be added verucarefully make the json retunt and do not inore space while defining return format 
3. update executor.py :: call run from mcp_regsisotry and passa argument
4. update loop.py (agen loopt)
    tool_registory to planner
    pass tool registory and argument amd tool extracted for plnnner result to run_action of mcp_maanger
    2. update pannker 


* keep aslo special attantion on plane while making json example fto return spacae alo smetter

In python json key are "key "double coute only the json.loads and json.dumb


### MCP tools, resources and prompt:
     MCP server expose multiple cababilites like TOOL, Resource and prompt

     Tool: To excute/run operation and get result 
        Can also pass argument to it
        `Decorator` used : @mcp.tool()
        asked by agent to  call tool

        client.list_tool() : Get all tool availble onMCP server
        client.call_tool(tool_name, arguments=DICT)
            To execute the MCP tool
        
        Agent->Too -> Argument -> Action
    Resource: To get information from MCP no operation
            It is read only
            like: get list of city whose information availbel
            slected or uses manually by client to get information
            Its has unique dentifier: URI
            to provide context and file content to an AI model via a unique URI
            `Decorator`: @mcp.resource(uniquw URI)

            client.list_resources(): List of all resources of mcp server
            client.read_resource('URI): to get the resouce data of MCP server
        Agent-> resouce -> URI -> Get Details
    Prompt: 
            user-controlled, reusable message templates and workflow shortcuts exposed by servers that you can explicitly select and run inside your AI client

            Decorator: @mcp.prompt(): call by funtion name
            this return reusable prompt 
            use to store here if muliplt application use the same prompt hence to
            standarzed it.

            client.list_prompts(): get list of all available prompts on mcp server
            client.get_prompt(prompt name): to get the prompt 

        Agent-> resouce -> prompt_name -> Get Prompt

### Remote MCP and HTTP transport
    I real life MCP server does not available on local. It run on remote.

    When the server exited on soe remoter server has some URL to it.
    The it is access by HTTP/HTTPS (ON production system for security) wit hosta nd post number.

    When server is ther on remote., then __aenter__() does not auto start it.
    Server will be started or strt manually,
    now 'aenter; just connct to it

    to run MCP server: puthon mcp_server.py

    In mcp_server.py
        server.run(transport="http", host="127.0.0.1", 
        port=8000)

    To connect:
        client.Client("http://127.0.0.1:8000/mcp)


    This is biggest sepration: Agent soes ned to know, how systerm work it just call tool and get the result.
    let the server having tool exist anywhere.


    Transport means: How client connect/call MCP server.
    Local process communication: File base connection: server exist on local
    Remote MCP connection: Connect over HTTP or HTTP's transport.


### Authentication and autherization in MCP:
    MCP server should be accesible by lagitimate client and based on restricted aacess to capabilities. Hance authenticatio and autherization used.

    Authentication: Decide to who acess MCP server
    Autherization: Decide which cleint can access what capabilities

    Authnetication does : by token based (Bearer token),cookies
    
    In production system has:
        Https as(transport), Authentication and autherization,
        Secrets, Logging, Timeouts handling


MCP give AI agent standerzied way to connect with external capabilities without tightly coupling.

This makes MCP powerful.
