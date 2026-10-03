## Model context protocol (MCP)

install> pip install fastmcp
verify> pip show fastmcp


Till now out too planner decided the tool and python use to execute the tool.

But as the tool increases the tool planner also need to handle it with manual handling with prompt.

If thee are 100's of tool then such handling need be done in planner and each assistant need to keep such tool list on local.

Now, we want tool can be create and added by anyone ans AI assistant able to use it  w/o any change.
How??
 Here MCP help.
  Here, tool are created once and putted on server. and from there it exeuted and get response to assistnt.
  AI assitan tdoes not need to worry about tool and handling.

  MCP provide standard communication layer between AI assistant and external capabilities (Tool, DB, File, API's ect.). It alllow open standard between AI assitan tand external capabiliites.

  MCP has 3 component:
  -- AI Agent: Ai assistant+ memory +  RAG + Planner + tool selection
  --MCP Client: Like interopreter: Act between AI Agent and MCP server
    It job:
        > Discover all available tool of MCP server
        > Ask server fot tool description
        > Sent tool request to serer to run
        > Get the result form server and sent to assistant.
 -- MCP Server: Owns the tool

 AI agent talso to MCP server via MCP client.
 AI agent not limited to single MCP server , it can connect to multiple MCP server via client and use the too.
 There can be multiple MCP server with tools specialized in domain

 Workflow:
    User query -> Planner -> Too name -> MCP Client -> MCP clientr Request to exeute too to  MCP server -> MCP Server Execute tool -> Sent return to CLient -> Sent result to Assitant

    If there new tool added to MCP server, then does client need to update/changes? No
    MCP client should get auto updated with updated tools .

### Devlopmemt MCP server:
     It has all tools > in mcp_server.py
    > mcp_server = FastMCP("First Time Server"):: create fast MCP serve instance.
    create tools:
    1. decorator: @mcp_server.too(): tell the mcp server that this functions are too, that are available to MCP client.
    2. doc String/desctiptio (Not for progrrammer but for server and AI agennt): """"""": Descript with tool, this help mcp server to know what is purpose of tool. As MCP server expose it to AI agent, thn the use case of tool should also know to AI agent.

    __name__== "__manin__"::
     as each file in pythion given name, this blok thel pytho  that if file is directly execited via python the run the code under it.
     mcp_server.run() --> run the python server as file run :: python mcp_server.py

### Devlopmemt MCP Client: mcp_clint.py
    responsibility:
        1> Connect to MCP server :
            client (): Create/hold configuration for mcp server to be connect
            client.__aenter__():
                1. start the MCP serve (As subprocess > python mcp_server.py)
                2. coonect to mcp server 
        2> Get/discover all availble tool
            client.list_tools(): get lis t of all server tool [{name, description.doc string}]
        3> Call the MCP tool or request server to execute the tool
            client.call_tool(toolname, argument?):: Request the too to be execute on server and get result
        4> Diconnect to MCP server 
            client.__aexit__()
                close the connetion with MCP server
                sto/terminate the server

        flow:
          Application -> Client(nae of serverpath/URL) ---> client.__aenter--()<Launth subpricess and satrt( mcp.run as main)>


asyncio:: if there asyn method that usinf await then those method need to be run as coroutean as this need not to be blocking process, as per that it need to pause so that call compet and the resum so that asyncio is use.

to run asycn methosd: asyncio.run(async_method())


### Builld AI agent with MCP
> agent.py : Agen tthat use MCP client server tool all and just anser only query and close
step 1: Connet to MCP
Step 2: Discover all tools
step 3: Create tool description
    planner: it will be function take use input, and toolist 
    create tool desctipion, and prompt with tool descriptiona  user query and ask to return best tool name
step 4: Ask ollama to select tool
    With created propt ollma with select best match tool based on tool description and user query
step 5: request MCP to execute selected tool
    now call MCP client to request MCP to execute tool;
        Now no tool execution on local
step 6: Get the response in natural lanugare
    

code:
if __name__ == "__main_":  (code to check if file run directly or vis some moduleimport)
 execute _funtion() // if file run dieectly the this code run
  This check is there if fily directly run via <python cammnd> the  run the code inside it

  Pythos defult assing name value to each executable file.
  if file executin ids amain then there should be some intilization point the start execution so this is that.


NoteL: As of now our Agent only use only one MCP
Bur there can be multiple MCP specilized in differ domain <gmail, db, file etc>
then:
Does planned need to know, tool from which MCP server?
Does cleintconnect to each MCP saperately?

ALl this question are encountred in production ready AI applications.



Tiill Now:

Ai AGennt has planner without 
    > Hard coding /check to know which tool to use
    > No local tool executio from server.

    Means now agent: Just has e AI Assitant + Planner + RAG + Memory
        nO need to maintain tool and dicision (Python code with if else) to execute it

MCP: Model context protocaol
Model: LLM model
COntent: Capability to acces external tool, DB, file
Protocaol: Standard rule to have acces to contest (Cleint server)