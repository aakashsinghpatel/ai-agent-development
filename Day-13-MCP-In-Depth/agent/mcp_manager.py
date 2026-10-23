from pathlib import Path 
from mcp_client  import connect, disconnet, discover_tool, execute_tool


async def create_tool_registory(servers_path):
    """ Method to connect with all mcp server whole path are passed as argument
     Retunt: 
     CLients:[] list of all mcp clients connect with respective server
     tool_registory: dicttionary: {tool_name: {client: mcp_client_of _mcp_server,tool_name, tool:{name, description}}}  """
    clients = []
    tool_registory = {}

    for server in servers_path:
        client = await connect(Path(server))
        clients.append(client)
        server_tools = await discover_tool(client)

        for tool in server_tools:
            tool_registory[tool.name] = {"client": client, 'tool': tool}

    return clients, tool_registory

async def run_tool(tool_name:str, tool_registory,argument=None):
    """ Method to execute named tool name from the cliet available in toll registory for 
    respectve tool """
    # tool_client = tool_registory[tool_name.lower().strip()]
    entry = tool_registory.get(tool_name)
    if entry is None:
        raise ValueError(f"Unknown tool: {tool_name}")

    client  = entry['client']
    result = await execute_tool(client, tool_name, argument)
    return result

async def close_server(clients):
    for client in clients:
        await disconnet(client)
